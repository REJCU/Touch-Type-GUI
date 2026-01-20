import customtkinter

import engine
from sentence_loader import SentenceHandler


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.handler = SentenceHandler()
        self.menuframe = MenuFrame(self)
        self.gameframe = GameFrame(self)
        self.menuframe.pack()

    def start_game(self, diffuculty):
        self.menuframe.pack_forget()
        new_text = self.handler.random_sentence(diffuculty)
        self.engine = engine.TypingEngine(new_text)
        self.gameframe.label.configure(text=new_text)
        self.gameframe.pack()
        self.gameframe.entry.focus()


class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(
            self, text="Beginner", command=lambda: master.start_game("beginner")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="intermediate", command=lambda: master.start_game("intermediate")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="advanced", command=lambda: master.start_game("advanced")
        )
        self.button.pack(padx=40, pady=40)

    def button_easy(self):
        self.master.start_game("beginner")

    def button_intermediate(self):
        self.master.start_game("intermediate")

    def button_advanced(self):
        self.master.start_game("advanced")


class GameFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text=" ")
        self.label.grid(row=0, column=0, padx=20)

        self.entry = customtkinter.CTkEntry(self)
        self.entry.grid(row=5, column=5)
        self.entry.bind("<Key>", self.handle_keypress)
        self.entry.bind("<Return>", self.enter_press)

    def handle_keypress(self, event):
        if event.keysym == "BackSpace":
            self.master.engine.process_key("BACKSPACE")
            print("back")
        else:
            self.master.engine.process_key(event.char)

    def enter_press(self, event):
        if event.keysym == "Return":
            print("enter")


app = App()
app.mainloop()
