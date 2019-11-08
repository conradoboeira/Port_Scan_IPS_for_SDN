import requests
import json
import time

list_of_hosts = ["10.0.0.11",
                 "10.0.0.12",
                 "10.0.0.13",
                 "10.0.0.21",
                 "10.0.0.31",
                 "10.0.0.32",
                 "10.0.0.33",
                 "10.0.0.41",
                 "10.0.0.42"
                ]


def get_flow_table_stats(switch):
    # Get flow data for specific switch from the ryu rest API
    data = (requests.get(url='http://localhost:8080/stats/flow/'+str(switch)).json())['1']
    # Create dict to map ip to flow stats   
    ip_to_flow = {}
    #CHECAR ISSO, NAO SEI SE FUNCIONA SEMPRE
    sent_flows = []

    for flow in data:
        if(not 'tp_dst' in flow['match']): continue
        ip_src = flow['match']['nw_src']
        ip_dst = flow['match']['nw_dst']
        port_dst = flow['match']['tp_dst']
        port_src = flow['match']['tp_src']
        packet_count = flow['packet_count']
        seconds_alive = flow['duration_sec']

        stats_to_be_saved = (ip_dst,port_dst,port_src,packet_count)
        # Check if flow is a request instead of a response
        if((ip_dst, ip_src, port_dst, port_src) in sent_flows): continue
        else: sent_flows.append((ip_src,ip_dst,port_src,port_dst))
        # is_req = flow['actions'][0] == 'OUTPUT:2'
        
        # Check if number of packets is smaller than threshold
        packets_restrict = packet_count <= 5
        recent_packet = seconds_alive <= 4

        if(packets_restrict and recent_packet):
            if(ip_src in ip_to_flow):
                ip_to_flow[ip_src].append(stats_to_be_saved)
            else:
                ip_to_flow[ip_src] = [stats_to_be_saved]
    
    return ip_to_flow
    

def check_horizontal_scan(flows):
    attackers = set()
    for ip in flows:
        ports_acessed = {}
        for match in flows[ip]:
            ip_dst = match[0]
            port_dst = match[1]
            if(port_dst in ports_acessed):
                if(ip_dst != ports_acessed[port_dst]):
                    ports_acessed[port_dst].append(ip_dst)
            else:
                ports_acessed[port_dst] = [ip_dst]
        
        for port in ports_acessed:
            if(len(ports_acessed[port]) > 3):
                attackers.add(ip)
    return attackers

def check_vertical_scan(flows):
    CPS_ports = (22,23,25,3389)
    attackers = set()
    for ip in flows:
        hosts_acessed = {}
        for match in flows[ip]:
            ip_dst = match[0]
            port_dst = match[1]
            if(ip_dst in hosts_acessed):
                if(port_dst in CPS_ports): hosts_acessed[ip_dst] += 5
                else: hosts_acessed[ip_dst] += 3
            else:
                if(port_dst in CPS_ports): hosts_acessed[ip_dst] = 5
                else: hosts_acessed[ip_dst] = 3
                
        
        for host in hosts_acessed:
            if(hosts_acessed[host] > 3):
                attackers.add(ip)
    return attackers

def check_mix_scan(flows):
    CPS_ports = (22,23,25,3389)
    attackers = set()
    for ip in flows:
        host_ip_acessed = {} 
        for match in flows[ip]:
            ip_dst = match[0]
            port_dst = match[1]
            if(ip_dst in host_ip_acessed):
                if(host_ip_acessed[ip_dst]):
                    host_ip_acessed[ip_dst].add(port_dst)
                else:
                    host_ip_acessed[ip_dst]=set([port_dst])

            else:
                host_ip_acessed[ip_dst]=set([port_dst])
        
        if(len(host_ip_acessed) < 2):continue
        for host in host_ip_acessed:
            count = 0
            for port in host_ip_acessed[host]:
                if(port in CPS_ports): count += 5
                else: count += 3
            if(count > 15):
                attackers.add(host)
    return attackers

def block_host(host, table):
    url = "http://localhost:8080/stats/flowentry/modify"
    
    for dst in list_of_hosts:
        if(dst == host): continue
        data = '''{{ "dpid": 1,
                    "table_id": {},
                    "match":{{
                        "nw_dst": "{}",
                        "dl_type": 2048,
                        "nw_src": "{}"
                    }}
                }}'''.format(table,host, dst)
        print(data)
        val = requests.post(url, data=data)

def main():
    
    flows = get_flow_table_stats(1)
    
    horizontal = check_horizontal_scan(flows)
    vertical = check_vertical_scan(flows)
    mixed = check_mix_scan(flows)
    attackers = horizontal.union(vertical).union(mixed)
    
    
    for attack in attackers:
        to_del = {'match' : {'nw_src' : attack}}
        print(to_del)
        block_host(attack,0)
        
        
if __name__ == '__main__':
    start_time = time.time()
    while True:
        print("tick")
        main()
        time.sleep(3.0)
