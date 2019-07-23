import scipy.io.wavfile

rate, data = scipy.io.wavfile.read('music.wav')

file = open('musictest.fss', 'w')
file.write("0.5\n")
for i in range(len(data)):
    data_new = abs(data[i])
    if data_new == 0:
        file.write("c4f0\n")
    elif 0 < data_new <= 1000:
        file.write("c4f1\n")
    elif 1000 < data_new <= 1500:
        file.write("c4f2\n")
    elif 1500 < data_new <= 2000:
        file.write("c4f3\n")
    elif 2000 < data_new <= 2500:
        file.write("c4f4\n")
    elif 2500 < data_new <= 3000:
        file.write("c4f5\n")
    elif 3000 < data_new <= 3500:
        file.write("c4f6\n")
    elif 3500 < data_new <= 4000:
        file.write("c4f7\n")
    elif 4000 < data_new <= 5000:
        file.write("c4f8\n")
    elif 5000 < data_new <= 6000:
        file.write("c4f9\n")
    elif 6000 < data_new <= 7500:
        file.write("c4fa\n")
    elif 7500 < data_new <= 10000:
        file.write("c4fb\n")
    elif 10000 < data_new <= 12500:
        file.write("c4fc\n")
    elif 12500 < data_new <= 15000:
        file.write("c4fd\n")
    elif 15000 < data_new <= 20000:
        file.write("c4fe\n")
    elif 20000 < data_new <= 30000:
        file.write("c4ff\n")
    #print(data_new)
file.close()