class Needs():
    pass
need = []
re = open("H:\\pyhton\\lista\\igeny.txt","r")
line = re.readline()
line = re.readline()
rn = int(re.readline())
for i in range(rn):
    line = re.readline()
    line = line.strip()
    datas = line.split()
    need.append(Needs())
    need[i].h = int(datas[0])
    print(datas[0])
    need[i].min = int(datas[1])
    need[i].sec = int(datas[2])
    need[i].team = int(datas[3])
    need[i].start = int(datas[4])
    need[i].stop = int(datas[5])
re.close()