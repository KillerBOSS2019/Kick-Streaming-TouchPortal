from tkinter import *

class Kick2FA:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Kick 2FA")

        self.center_window(300, 100)

        self.root.resizable(False, False)
        self.authCode = ""

        label = Label(self.root, text="Enter your 2FA code")
        label.pack()
        self.entry = Entry(self.root)
        self.entry.pack()

        self.entry.focus_set()

        self.entry.bind("<Return>", self.submit)

        button = Button(self.root, text="Submit", command=self.submit)
        button.pack()
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (300 / 2))
        y = int((screen_height / 2) - (100 / 2))

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def submit(self, event=None):
        self.authCode = self.entry.get()
        self.root.destroy()

    def getPasscode(self):
        self.root.mainloop()
        return self.authCode