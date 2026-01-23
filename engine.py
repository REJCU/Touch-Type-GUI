import time
import sentence_loader

#handler = sentence_loader()
#text = handler.random_sentence("advanced")

class TypingEngine():
    def __init__(self, text):
        self.target = text
        self.current_input = ""
        self.start_time = None
        self.end_time = None 
        self.total_keystroke = 0 


    def process_key(self, char):
        # starts timer 
        if self.start_time is None:
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
        wpm = (len(self.target)/5) / (time_elapsed / 60)
        accuracy = ((len(self.target)) / self.total_keystroke) * 100
        print(f" Time: {time_elapsed}, WPM: {round(wpm,2)} , Accuracy: {accuracy}") 
        return time_elapsed, round(wpm, 2), accuracy
        
