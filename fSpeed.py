import scipy.io.wavfile

rate, data = scipy.io.wavfile.read('music.wav')

file = open('musictest.fss', 'w')
file.write("0\n")
for i in range(len(data)):
    data_new = abs(data[i])
    if data_new <= 258:
        file.write("c4f0\n")
    elif 258 < data_new <= 1027:
        file.write("c4f1\n")
    elif 1027 < data_new <= 1538:
        file.write("c4f2\n")
    elif 1538 < data_new <= 2305:
        file.write("c4f3\n")
    elif 2305 < data_new <= 3071:
        file.write("c4f4\n")
    elif 3071 < data_new <= 3836:
        file.write("c4f5\n")
    elif 3836 < data_new <= 5372:
        file.write("c4f6\n")
    elif 5372 < data_new <= 6908:
        file.write("c4f7\n")
    elif 6908 < data_new <= 8445:
        file.write("c4f8\n")
    elif 8445 < data_new <= 9214:
        file.write("c4f9\n")
    elif 9214 < data_new <= 9471:
        file.write("c4fa\n")
    elif 9471 < data_new <= 10240:
        file.write("c4fb\n")
    elif 10240 < data_new <= 11776:
        file.write("c4fc\n")
    elif 11776 < data_new <= 12544:
        file.write("K-f\n")
    elif 12544 < data_new <= 16640:
        file.write("c4fd\n")
    elif 16640 < data_new <= 20736:
        file.write("c4fe\n")
    elif 20736 < data_new:
        file.write("c4ff\n")
    #print(data_new)
file.close()