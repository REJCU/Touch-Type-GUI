import customtkinter
from sentence_loader import SentenceHandler
import engine

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
        self.gameframe.label.configure(text=new_text)
        self.gameframe.pack()

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(self, text = "Beginner", command=lambda: master.start_game("beginner"))
        self.button.pack(padx=40, pady=40)
        
        self.button = customtkinter.CTkButton(self, text = "intermediate", command=lambda: master.start_game("intermediate"))
        self.button.pack(padx=40, pady=40)

        
        self.button = customtkinter.CTkButton(self, text = "advanced", command=lambda: master.start_game("advanced"))
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

        self.label = customtkinter.CTkLabel(self, text = " ")
        self.label.grid(row=0, column=0, padx=20)

        self.entry = customtkinter.CTkEntry(self)
        self.entry.grid(row=5, column=5)
        self.entry.bind("<key>", self.handle_keypress)

    def handle_keypress(self, event):
        
        





app = App()
app.mainloop()
