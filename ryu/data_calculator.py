import math

s1 = [144,69,68,66,9]
s2 = [9,69,69,111,62]
s3 = [69,69,126,68,142]
s5 = [270,69,222,69,249]
s10 = [69,698,69,493,710]

scans = [s1,s2,s3,s5,s10]

i1 = [36.3,36.5,39.9,34.9,37.0]
i2 = [38.4,37.7,36.0,39.9,39.7]
i3 = [36.5,41.4,39.0,38.0,39.4]
i5 = [37.3,40.2,35.6,36.3,36.7]
i10 = [35.2,38.4,40.3,34.1,33.5]

iperf = [i1,i2,i3,i5,i10]

media_scans = []
for s in scans:
    total = 0
    for val in s:
        total += val
    media = total / len(s)
    media_scans.append(media)

media_iperf= []
for i in iperf:
    total = 0
    for val in i:
        total += val
    media = total / len(s)
    media_iperf.append(media)


desvio_padrao_scans = []
for i in range(len(scans)):
    media = media_scans[i]
    soma = 0
    for val in scans[i]:
        soma += (val - media) ** 2
    desvio = math.sqrt(soma/len(scans[i]))
    desvio_padrao_scans.append(desvio)

tempos = [1,2,3,5,10]
for i in range(5): 
    print("Tempo: {} | Media Scans: {} | D.P. Scans : {} | Media iperf: {}\n".format
            (tempos[i], media_scans[i], desvio_padrao_scans[i], media_iperf[i]))



