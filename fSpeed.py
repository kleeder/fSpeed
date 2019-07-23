import scipy.io.wavfile

rate, data = scipy.io.wavfile.read('music.wav')
data_min = 0
data_max = 0
for i in range(len(data)):
    if data[i] < data_min:
        data_min = data[i]
    if data[i] > data_max:
        data_max = data[i]

if data_max < abs(data_min):
    biggestValue = abs(data_min)
else:
    biggestValue = data_max

bigF = biggestValue // 15
file = open('musictest.fss', 'w')
file.write("0.5\n")
for i in range(len(data)):
    data_new = abs(data[i])
    if data_new == 0:
        file.write("c4f0\n")
    elif 0 < data_new <= bigF:
        file.write("c4f1\n")
    elif bigF < data_new <= bigF*2:
        file.write("c4f2\n")
    elif bigF*2 < data_new <= bigF*3:
        file.write("c4f3\n")
    elif bigF*3 < data_new <= bigF*4:
        file.write("c4f4\n")
    elif bigF*4 < data_new <= bigF*5:
        file.write("c4f5\n")
    elif bigF*5 < data_new <= bigF*6:
        file.write("c4f6\n")
    elif bigF*6 < data_new <= bigF*7:
        file.write("c4f7\n")
    elif bigF*7 < data_new <= bigF*8:
        file.write("c4f8\n")
    elif bigF*8 < data_new <= bigF*9:
        file.write("c4f9\n")
    elif bigF*9 < data_new <= bigF*10:
        file.write("c4fa\n")
    elif bigF*10 < data_new <= bigF*11:
        file.write("c4fb\n")
    elif bigF*11 < data_new <= bigF*12:
        file.write("c4fc\n")
    elif bigF*12 < data_new <= bigF*13:
        file.write("c4fd\n")
    elif bigF*13 < data_new <= bigF*14:
        file.write("c4fe\n")
    elif bigF*14 < data_new:
        file.write("c4ff\n")
    #print(data_new)
file.close()