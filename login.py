from pyrogram import Client
import time
import sys
import os
from pyrogram.errors import RPCError

print("""


STARTING LOGIN...

""")

MadeByLlattes = []
fh_r = open("Sessions.txt", "r")
fh_w = open("temp.txt", "w")
alf = open("Sessions.txt", "r").read()
alf1 = alf.split()

i = 1
j = 0

while True:
    try:
        a = str(alf1[j])
        b = int(alf1[j + 1])
        c = str(alf1[j + 2])
        d = str(alf1[j + 3])
    except:
        print("Finished")
        try:
            fh_w.close()
            fh_r.close()
            os.remove("temp.txt")
            sys.exit()
        except:
            sys.exit()
            pass
    app = Client("Sessions/" + a, b, c, phone_number=d)
    try:
        app.start()
        app.send_message("me", str(i))
        app.stop()
        print("Session " + str(d) + " created !")
        i += 1
        j += 4

    except RPCError as e:
        roll_no = int(a)

        s = ' '
        while (s):
            s = fh_r.readline()
            L = s.split(" ")
            if len(s) > 0:
                if int(L[0]) != roll_no:
                    fh_w.write(s)
        fh_w.close()
        fh_r.close()
        os.remove("Sessions.txt")
        os.rename("temp.txt", "Sessions.txt")

        print("Session " + str(d) + " this session is banned !")

        i += 1
        j += 4
