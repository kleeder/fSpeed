
import struct
import wave

with wave.open('music.wav', 'rb') as wr:
    frames = wr.readframes(wr.getnframes())

# with some settings it may be needed to change the pitch of the original file
# to balance compression with correct pitch

# note which is used when representing pcm
# this doesn't seem change the output wav at all
NOTE = "c1"

# the length of each note which represents a sample
# also doesn't seem to affect the wav file
NOTE_LENGTH = "f"

# any fsound data to be added at the end of each note
APPEND_DATA = "\n"

# try changing this value, some values may offer more compression at the expense
# of more silent gaps between some parts of the audio
EMPTY_SAMPLES_LIMIT = 100

# loops each note write by this number
# affects quality and pitch
NOTE_LOOP = 1

# base 2 number, used to determine how many samples are taken from
# the original pcm data
ITER_SAMPLE = 2

non_zero_counter = 0
file = open('musictest.fss', 'w')
file.write("0\n")

offset = 0

# changed this to a while loop as I wanted to modify the offset value outside
# of this loop
while offset < len(frames):
    data_new = abs(struct.unpack_from('<h', frames, offset)[0])

    if data_new > 258:
        non_zero_counter = 1

    if data_new <= 258 and non_zero_counter > 0:
        ignore_end = False

        if (offset + ITER_SAMPLE) >= len(frames):
            continue

        _data_new = abs(struct.unpack_from('<h', frames, offset + 1)[0])
        empty_samples = 1

        # get number of empty samples while iterating offset
        while _data_new <= 258:
            if (offset + ITER_SAMPLE) >= len(frames):
                ignore_end = True
                break

            offset += ITER_SAMPLE
            _data_new = abs(struct.unpack_from('<h', frames, offset)[0])

            empty_samples += 1

        # complete ignore any end rests + end rests which are less than 10
        # in length
        if not ignore_end and empty_samples > 10:
            # write normal rests if there is a low amount of rests
            if empty_samples < EMPTY_SAMPLES_LIMIT:
                for _ in range(0, round(empty_samples / 2)):
                    file.write("r\n")
            else:
                # slow down the tempo by a lot and write a lot less rests
                file.write("t15\n");
                for _ in range(0, round(empty_samples / EMPTY_SAMPLES_LIMIT / 2)):
                    file.write("r\n")
                file.write("t0\n");

    write_note = ""

    if 258 < data_new <= 1027:
        write_note = (NOTE + NOTE_LENGTH + "1" + APPEND_DATA)
    elif 1027 < data_new <= 1538:
        write_note = (NOTE + NOTE_LENGTH + "2" + APPEND_DATA)
    elif 1538 < data_new <= 2305:
        write_note = (NOTE + NOTE_LENGTH + "3" + APPEND_DATA)
    elif 2305 < data_new <= 3071:
        write_note = (NOTE + NOTE_LENGTH + "4" + APPEND_DATA)
    elif 3071 < data_new <= 3836:
        write_note = (NOTE + NOTE_LENGTH + "5" + APPEND_DATA)
    elif 3836 < data_new <= 5372:
        write_note = (NOTE + NOTE_LENGTH + "6" + APPEND_DATA)
    elif 5372 < data_new <= 6908:
        write_note = (NOTE + NOTE_LENGTH + "7" + APPEND_DATA)
    elif 6908 < data_new <= 8445:
        write_note = (NOTE + NOTE_LENGTH + "8" + APPEND_DATA)
    elif 8445 < data_new <= 9214:
        write_note = (NOTE + NOTE_LENGTH + "9" + APPEND_DATA)
    elif 9214 < data_new <= 9471:
        write_note = (NOTE + NOTE_LENGTH + "a" + APPEND_DATA)
    elif 9471 < data_new <= 10240:
        write_note = (NOTE + NOTE_LENGTH + "b" + APPEND_DATA)
    elif 10240 < data_new <= 11776:
        write_note = (NOTE + NOTE_LENGTH + "c" + APPEND_DATA)
    elif 11776 < data_new <= 16640:
        write_note = (NOTE + NOTE_LENGTH + "d" + APPEND_DATA)
    elif 16640 < data_new <= 20736:
        write_note = (NOTE + NOTE_LENGTH + "e" + APPEND_DATA)
    elif 20736 < data_new:
        write_note = (NOTE + NOTE_LENGTH + APPEND_DATA)

    for _ in range(0, NOTE_LOOP):
        file.write(write_note)

    offset += ITER_SAMPLE

file.close()
