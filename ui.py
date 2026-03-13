import customtkinter
import time 

import engine
from sentence_loader import SentenceHandler
import stats


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.handler = SentenceHandler()
        self.menuframe = MenuFrame(self)
        self.gameframe = GameFrame(self)
        self.menuframe.pack()
        
        self.resultsframe = ResultsFrame(self)
        self.final_results = None
        self.stats = stats.RecordResults()
        self.diffuculty = None

    def start_game(self, diffuculty):
        self.diffuculty = diffuculty
        self.menuframe.pack_forget()
        new_text = self.handler.random_sentence(diffuculty)
        self.chosen_sentence = new_text
        self.engine = engine.TypingEngine(new_text)

        self.current_index = 0

        self.gameframe.label.configure(text=new_text)
        self.gameframe.pack()
        self.gameframe.entry.focus()


    def finish_game(self, sentence, chosen_sentence):
        """TODO- fix the logic- want to compare to it each time and flash red"""
        results = self.engine.calculate_score(sentence)
        if results is not None:
            self.stats.print_to_json(results, chosen_sentence)
            self.gameframe.pack_forget()
            self.resultsframe.label.configure(text=results)
            self.resultsframe.pack()
            self.final_results = results
        else:
            print("Not Correct")
            self.gameframe.entry.delete(0, 'end')

    def retry_game(self):
        # uses previous diffuculty
        self.resultsframe.pack_forget()
        self.gameframe.entry.delete(0, "end")
        self.start_game(self.diffuculty)




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

        # for programming 
        self.button = customtkinter.CTkButton(
            self, text="Programming-easy", command=lambda: master.start_game("programming-easy")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="Programming-intermediate", command=lambda: master.start_game("programming-intermediate")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="Programming-advanced", command=lambda: master.start_game("programming-advanced")
        )
        self.button.pack(padx=40, pady=40)

        # for Vim-motions
        self.button = customtkinter.CTkButton(
            self, text="Vim-motions-easy", command=lambda: master.start_game("Vim-motions-easy")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="Vim-motions-intermediate", command=lambda: master.start_game("Vim-motions-intermediate")
        )
        self.button.pack(padx=40, pady=40)

        self.button = customtkinter.CTkButton(
            self, text="Vim-motions-advanced", command=lambda: master.start_game("Vim-motions-advanced")
        )
        self.button.pack(padx=40, pady=40)

    def button_easy(self):
        self.master.start_game("beginner")

    def button_intermediate(self):
        self.master.start_game("intermediate")

    def button_advanced(self):
        self.master.start_game("advanced")

    def button_programming(self):
        self.master.start_game("programming-easy")

    def button_programming_intermediate(self):
        self.master.start_game("programming-intermediate")

    def button_programming_advanced(self):
        self.master.start_game("programming-advanced")

    def button_vim_motions_easy(self):
        self.master.start_game("Vim-motions-easy")

    def button_vim_motions_intermediate(self):
        self.master.start_game("Vim-motions-intermediate")

    def button_vim_motions_advanced(self):
        self.master.start_game("Vim-motions-advanced")



class GameFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self, text=" ")
        self.label.grid(row=0, column=0, padx=400, pady=400)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.entry = customtkinter.CTkEntry(self)
        self.entry.grid(row=1, column=0, padx=0, pady=0, sticky="ew")
        self.entry.bind("<Key>", self.handle_keypress)
        self.entry.bind("<Return>", self.enter_press)



    def handle_keypress(self, event):
        if event.keysym == "BackSpace":
            self.master.engine.process_key("BACKSPACE")
        elif event.char:
            self.master.engine.process_key(event.char)

    def enter_press(self, event):
        input_string = self.entry.get()
        self.master.finish_game(input_string, self.master.chosen_sentence)

class ResultsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text=" ") 
        self.label.grid(row=0, column=0, padx=400, pady=400) 
        
        self.button = customtkinter.CTkButton(self, text = "Retry", command=lambda: self.retry_button())
        self.button.grid(pady=400, padx=400)

    def retry_button(self):
        self.master.retry_game()



app = App()
app.mainloop()
