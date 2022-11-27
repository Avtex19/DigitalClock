from tkinter import Label, Tk, mainloop
import time


class digitalClock:

    def __init__(self, window):
        self.window = window
        self.window.title("Digital Clock")
        self.window.geometry("420x150")

        self.dc_label = Label(self.window, fg="green", font=("Boulder", 68, 'bold'), bd=25)
        self.dc_label.pack(anchor='center')
        self.digital_clock()
        self.window.mainloop()

    def digital_clock(self):
        time_live = time.strftime("%H:%M:%S")
        self.dc_label.config(text=time_live)
        self.dc_label.after(200, self.digital_clock)


if __name__ == "__main__":
    root = Tk()
    app = digitalClock(root)
