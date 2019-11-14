
nmap_result = open("3_sec.txt", 'r')
tried = 0
refused = 0

for line in nmap_result:
    pos = line.find(':')
    pos_f = line.find('=')
    if(pos == -1 or pos_f == -1): continue
    result = line[pos_f+3:]
    print(result)
    if(result.startswith('Connection refused')): refused+=1
    if(result.startswith('Operation now in progress')): tried+=1
    '''
    port = line[pos+1:pos_f-1]
    if(port in seen_ports): seen_ports.remove(port)
    else: seen_ports.append(port)
    '''

print(tried)
print(refused)
