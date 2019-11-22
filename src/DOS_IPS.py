import requests
import json

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
        bytes_count = flow['byte_count']
        seconds_alive = flow['duration_sec']


        stats_to_be_saved = (packet_count,bytes_count)
        # Check if flow is a request instead of a response
        if((ip_dst, ip_src, port_dst, port_src) in sent_flows): continue
        else: sent_flows.append((ip_src,ip_dst,port_src,port_dst))
        
        # Check if number of packets is smaller than threshold
        recent_packet = seconds_alive <= 30

        if(recent_packet):
            if(ip_src in ip_to_flow):
                ip_to_flow[ip_src].append(stats_to_be_saved)
            else:
                ip_to_flow[ip_src] = [stats_to_be_saved]
    
    return ip_to_flow
 
def cusum_ps(flows):
    attackers = set()
    for ip in flows:
        total_sum = 0
        cumulative_sum = 0
        index = 0
        attack_count = 0
        for match in flows[ip]:
            average = (total_sum+ match[0])/(index+1)
            cumulative_sum = (match[0] - average) + cumulative_sum
            threshold = 0.3 * average

            is_abnormal =  cumulative_sum > threshold

            if is_abnormal:
                attack_count += 1

            else:
                total_sum += match[0]
                index += 1
    
        num_samples = len(flows[ip])
        if attack_count >= int(num_samples * 0.4):
            attackers.add(ip)
    return attackers


def main():
    flows = get_flow_table_stats(1)
    for f in flows:
        print(f + " : " + str(flows[f]))
    
    for attack in attackers:
        to_del = {'match' : {'nw_src' : attack}}
        print(to_del)
        
        
if __name__ == '__main__':
    main()
