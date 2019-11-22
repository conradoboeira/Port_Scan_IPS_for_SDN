import math

s1 = [29,69,9,133,69,69,9,104,69,9]
s2 = [69,69,69,82,69,69,96,66,69,9]
s3 = [137,169,133,69,232,69,69,144,69,69]
s5 = [334,69,230,9,313,328,9,9,133,215]
s10 = [504,70,588,150,62,435,144,160,109,428] 


scans = [s1,s2,s3,s5,s10]

i1 = [50.2,43.1,46.5,39.5,48.4,43.2,37.9,41.9,43.9,37.7]
i2 = [52.6,41.2,39.6,46.2,44.3,42.7,39.1,48.4,48.2,43.9]
i3 = [53.5,41.5,39.0,39.7,39.8,40.8,43.4,42.0,42.3,42.4]
i5 = [45.7,42.0,41.4,38.0,40.2,43.2,44.4,50.6,51.5,36.3]
i10 =[43.7,40.9,50.7,45.4,41.5,42.5,45.6,46.4,48.0,37.4]

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



