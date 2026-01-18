import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.pack(padx=20, pady=10)

        self.button = customtkinter.CTkButton(self, text = "Beginner", command=self.button_easy)
        self.button.pack(padx=40, pady=40)


        
        self.button = customtkinter.CTkButton(self, text = "intermediate", command=self.button_intermediate)
        self.button.pack(padx=40, pady=40)

        
        self.button = customtkinter.CTkButton(self, text = "advanced", command=self.button_advanced)
        self.button.pack(padx=40, pady=40)


    def button_easy(self): 
        print("easy")

    def button_intermediate(self): 
        print("intermediate")

    def button_advanced(self): 
        print("advanced")

app = App()
app.mainloop()
