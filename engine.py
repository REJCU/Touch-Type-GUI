import time
import sentence_loader

#handler = sentence_loader()
#text = handler.random_sentence("advanced")

class TypingEngine():
    def __init__(self, text):
        self.target = text
        self.current_input = ""
        self.start_time = int(0)
        self.end_time = int(0) 
        self.total_keystroke = 0 


    def process_key(self, char):
        # starts timer 
        if self.start_time == 0:
            self.start_time = time.time()

        if char == "BACKSPACE":
            if len(self.current_input) > 0:
                self.current_input = self.current_input[:-1]
        else:
            self.current_input += char
            self.total_keystroke+= 1
           
        
        if self.current_input == self.target:
            self.end_time = time.time()

    
    def calculate_score(self, user_input):
        time_elapsed = self.end_time - self.start_time
        if time_elapsed > 0:
            wpm = (len(self.target)/5) / (time_elapsed / 60) 
        else:
            wpm = (len(self.target)/5) / (time_elapsed / 60) * 60 
        accuracy = ((len(self.target)) / self.total_keystroke) * 100
        print(f" Time: {round(time_elapsed, 2)}, WPM: {round(wpm,2)} , Accuracy: {round(accuracy, 2)}") 
        results = { "Time": round(time_elapsed, 2),
                    "WPM": round(wpm, 2),
                    "Accuracy": round(accuracy, 2)} 
        return results
