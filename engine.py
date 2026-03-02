import time
import sentence_loader
import stats 

#handler = sentence_loader()
#text = handler.random_sentence("advanced")

class TypingEngine():
    def __init__(self, text):
        self.target = text
        self.current_input = ""
        self.current_index = 0
        self.start_time = int(0)
        self.end_time = None 
        self.total_keystroke = 0 
        self.diffuculty = ""
        self.user_input = ""



    def process_key(self, char):
        # starts timer 
        if self.start_time == 0:
            self.start_time = time.time()

        elif char == "BACKSPACE":
            if self.current_index > 0:
                # self.current_input = self.current_input[:-1]
                self.current_index -= 1
                print({self.target[self.current_index]}, "pending", print(self.user_input) )
            return

        if self.current_index >= len(self.target):
            return

        target_char = self.target[self.current_index]
        if char == target_char:
            print(target_char, "correct")
        else:
            print(target_char, "wrong")

        self.current_index += 1 


        if self.current_index == len(self.target):
            self.end_time = time.time()
            total_time = time.time()
            print(f"Fin Time: {total_time:.2f} ")
            results = self.calculate_score()
            print(results)

    
    def calculate_score(self):
        # Checks if sentence is complete and then return results, is enter is pressed early, prints outbound variable
        if self.target == self.user_input:
            time_elapsed = time.time() - self.start_time
            wpm = (len(self.target)/5) / (time_elapsed / 60) 
            # if  self.target == self.current_input: 
            accuracy = ((len(self.target)) / self.total_keystroke) * 100
            #else:
            #   print("Try again")
            #  pass 
            print(f" Time: {round(time_elapsed, 2)}, WPM: {round(wpm,2)} , Accuracy: {round(accuracy, 2)}") 
            results = { "Time": round(time_elapsed, 2),
                        "WPM": round(wpm, 2),
                        "Accuracy": round(accuracy, 2)} 
            return results
