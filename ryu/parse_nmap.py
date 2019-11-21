import sys

nmap_result = open(sys.argv[1],'r')
tried = 0
refused = 0
unreachable = 0

for line in nmap_result:
    pos = line.find(':')
    pos_f = line.find('=')
    if(pos == -1 or pos_f == -1): continue
    result = line[pos_f+3:]
    print(result)
    if(result.startswith('Connection refused')): refused+=1
    if(result.startswith('Operation now in progress')): tried+=1
    if(result.startswith('Network is unreachable')): unreachable+=1

print("tried: {}".format(tried))
print("unreachable: {}".format(unreachable))
print("refused: {}".format(refused))
