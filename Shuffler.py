import os
import random
import time
import tkinter as tk
from tkinter import messagebox
import time

usb = os.getcwd()
all = os.listdir(usb)
songs = [i for i in all if i.endswith('.mp3')]
nums = [i for i in range(len(songs))]
c = 0
shufs = 0


def moreShuffle(window, message):
    global c
    global shufs
    for i in songs:
        tList = i.split(",,")
        ic = tList[-1]
        loto = nums.pop(random.randint(0, len(nums)-1))
        os.rename(i, str(loto) + ',,' + ic)
        c += 1

    #for i in range(5):
    #    time.sleep(1)
    tk.messagebox.showinfo("Info", message)
    window.destroy()

window = tk.Tk()
window.geometry("+0+0")
window.title("Playlist shuffler")
window.attributes('-topmost', True)
window.configure(bg="#000000")
window.after(1, moreShuffle, window, "Песни перемешаны!")
'''
btn_qs = tk.Button(
    text="SHUFFLE!",
    width=14,
    foreground="#ffff00",
    background="#000000",
    font=("Helvetica", 10)
)
btn_qs.bind("<Button-1>", moreShuffle)
btn_qs.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

msg = tk.Label(
    anchor="nw",
    text="Нажми SHUFFLE!, чтобы перемешать песни в этой папке",
    fg="#ffff00",
    bg="#000000",
    font=("Helvetica", 10),
    justify="right"
)
msg.grid(columnspan=2, row=1, column=0, padx=5, pady=5, sticky="ew")

msg2 = tk.Label(anchor="nw",
    text="Нажми SHUFFLE!, чтобы перемешать песни в этой папке",
    fg="#ffff00",
    bg="#000000",
    font=("Helvetica", 10),
    justify="right"
)'''

window.mainloop()