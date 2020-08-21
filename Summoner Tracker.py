from tkinter import *
from PIL import ImageTk, Image
import pyperclip, time, threading

root = Tk()

root.title("Summoner Tracker")
root.configure(background='white')

topImg = ImageTk.PhotoImage(Image.open(r'C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\Personal\League Icons\TOP.png'))
jgImg = ImageTk.PhotoImage(Image.open(r'C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\Personal\League Icons\JUNGLE.png'))
midImg = ImageTk.PhotoImage(Image.open(r'C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\Personal\League Icons\MIDDLE.png'))
adcImg = ImageTk.PhotoImage(Image.open(r'C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\Personal\League Icons\ADC.png'))
suppImg = ImageTk.PhotoImage(Image.open(r'C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\Personal\League Icons\SUPPORT.png'))

message = []
triggered = False
houT = 0
houO = 0
minT = 0
minO = 0


def startTimer():
    def tort():

        temp = 0
        foo = False

        global triggered
        global houT
        global houO
        global minT
        global minO

        if not triggered:
            triggered = True
            # TODO change the clock into a two-two digit system.
            for i in range(3600):
                Label(root, padx=10, pady=5, bg="white",
                      text=str(houT) + str(houO) + ":" + str(minT) + str(minO)).grid(row=1, column=2)
                time.sleep(1)
                if minO < 10:
                    minO += 1

                if minO == 10:
                    minO = 0
                    minT += 1

                if minT == 6 and houT == 0 and houO == 0:
                    houT = 0
                    houO = 1
                    minT = 0
                    foo = True

                if minT == 6 and foo:
                    houO += 1
                    minT = 0

                if houO == 10:
                    houT += 1
                    houO = 0

                if minT == 5 and minO == 9 and houT == 0 and houO == 0:
                    foo = False

                if houT == 0:
                    if houO - minT == minT - minO:
                        temp += 1

                if houT > 0:
                    if houO - minT == minT - minO and houT - houO == minT - minO:
                        temp += 1

                # print(" " + str(houT) + str(houO) + ":" + str(minT) + str(minO))

    thread = threading.Thread(target=tort)
    thread.daemon = True
    thread.start()


def top():
    Button(root, image=topImg, bg="white", borderwidth=2, state=DISABLED, relief="sunken").grid(row=0, column=0,
                                                                                                padx=10, pady=10)
    global message
    global numOfSums

    if houT != 0:
        output = str(houT) + str(houO + 5) + ":" + str(minT) + "0" + "top"
    else:
        output = str(houO + 5) + ":" + str(minT) + "0" + "top"

    message.append(output + " ")
    f = ""
    for s in message:
        f += s
    pyperclip.copy(f)

    def teck():
        global index
        time.sleep(300)
        Button(root, image=topImg, bg="white", borderwidth=2, command=top).grid(row=0, column=0, padx=10, pady=10)
        message.remove(output + " ")
        final = ""
        for summ in message:
            final += summ
        pyperclip.copy(final)

    thread = threading.Thread(target=teck)
    thread.daemon = True
    thread.start()


def jg():
    Button(root, image=jgImg, bg="white", borderwidth=2, state=DISABLED, relief="sunken").grid(row=0, column=1,
                                                                                                padx=10, pady=10)
    global message
    global numOfSums

    if houT != 0:
        output = str(houT) + str(houO + 5) + ":" + str(minT) + "0" + "jg"
    else:
        output = str(houO + 5) + ":" + str(minT) + "0" + "jg"

    message.append(output + " ")
    f = ""
    for s in message:
        f += s
    pyperclip.copy(f)

    def jeck():
        global index
        time.sleep(300)
        Button(root, image=jgImg, bg="white", borderwidth=2, command=jg).grid(row=0, column=1, padx=10, pady=10)
        message.remove(output + " ")
        final = ""
        for summ in message:
            final += summ
        pyperclip.copy(final)

    thread = threading.Thread(target=jeck)
    thread.daemon = True
    thread.start()


def mid():
    Button(root, image=midImg, bg="white", borderwidth=2, state=DISABLED, relief="sunken").grid(row=0, column=2,
                                                                                                padx=10, pady=10)
    global message
    global numOfSums

    if houT != 0:
        output = str(houT) + str(houO + 5) + ":" + str(minT) + "0" + "mid"
    else:
        output = str(houO + 5) + ":" + str(minT) + "0" + "mid"

    message.append(output + " ")
    f = ""
    for s in message:
        f += s
    pyperclip.copy(f)

    def meck():
        global index
        time.sleep(300)
        Button(root, image=midImg, bg="white", borderwidth=2, command=mid).grid(row=0, column=2, padx=10, pady=10)
        message.remove(output + " ")
        final = ""
        for summ in message:
            final += summ
        pyperclip.copy(final)

    thread = threading.Thread(target=meck)
    thread.daemon = True
    thread.start()


def adc():
    Button(root, image=adcImg, bg="white", borderwidth=2, state=DISABLED, relief="sunken").grid(row=0, column=3,
                                                                                                padx=10, pady=10)
    global message
    global numOfSums

    if houT != 0:
        output = str(houT) + str(houO + 5) + ":" + str(minT) + "0" + "adc"
    else:
        output = str(houO + 5) + ":" + str(minT) + "0" + "adc"

    message.append(output + " ")
    f = ""
    for s in message:
        f += s
    pyperclip.copy(f)

    def aeck():
        global index
        time.sleep(300)
        Button(root, image=adcImg, bg="white", borderwidth=2, command=adc).grid(row=0, column=3, padx=10, pady=10)
        message.remove(output + " ")
        final = ""
        for summ in message:
            final += summ
        pyperclip.copy(final)

    thread = threading.Thread(target=aeck)
    thread.daemon = True
    thread.start()


def supp():
    Button(root, image=suppImg, bg="white", borderwidth=2, state=DISABLED, relief="sunken").grid(row=0, column=4,
                                                                                                padx=10, pady=10)
    global message
    global numOfSums

    if houT != 0:
        output = str(houT) + str(houO + 5) + ":" + str(minT) + "0" + "supp"
    else:
        output = str(houO + 5) + ":" + str(minT) + "0" + "supp"

    message.append(output + " ")
    f = ""
    for s in message:
        f += s
    pyperclip.copy(f)

    def seck():
        global index
        time.sleep(300)
        Button(root, image=suppImg, bg="white", borderwidth=2, command=supp).grid(row=0, column=4, padx=10, pady=10)
        message.remove(output + " ")
        final = ""
        for summ in message:
            final += summ
        pyperclip.copy(final)

    thread = threading.Thread(target=seck)
    thread.daemon = True
    thread.start()


Button(root, image=topImg, bg="white", borderwidth=2, command=top).grid(row=0, column=0, padx=10, pady=10)
Button(root, image=jgImg, bg="white", borderwidth=2, command=jg).grid(row=0, column=1, padx=10, pady=10)
Button(root, image=midImg, bg="white", borderwidth=2, command=mid).grid(row=0, column=2, padx=10, pady=10)
Button(root, image=adcImg, bg="white", borderwidth=2, command=adc).grid(row=0, column=3, padx=10, pady=10)
Button(root, image=suppImg, bg="white", borderwidth=2, command=supp).grid(row=0, column=4, padx=10, pady=10)

Label(root, text="00:00", bg="white").grid(row=1, column=2)

b = Button(root, text="Start Timer", padx=10, pady=5, bg="white", borderwidth=0, command=startTimer)
b.grid(row=1, column=1)

root.mainloop()
