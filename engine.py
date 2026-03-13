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
        target_char = self.target[self.current_index]
        if self.start_time == 0:
            self.start_time = time.time()
        
        self.total_keystroke += 1
        if char == "BACKSPACE":
            if len(self.user_input) > 0:
                self.user_input = self.user_input[:-1]
                # self.current_index -= 1

        # can probably add current error checking by text and checking against char

        else:
            self.user_input += char
            print(self.user_input, char, self.target, self.current_index)

        # self.current_index += 1

        


    def calculate_score(self, user_input):
        # Checks if sentence is complete and then return results, is enter is pressed early, prints outbound variable
        if self.target == user_input:
            time_elapsed = time.time() - self.start_time
            wpm = (len(self.target)/5) / (time_elapsed / 60)
            accuracy = ((len(self.target)) / self.total_keystroke) * 100
            print(f" Time: {round(time_elapsed, 2)}, WPM: {round(wpm,2)} , Accuracy: {round(accuracy, 2)}")
            results = { "Time": round(time_elapsed, 2),
                        "WPM": round(wpm, 2),
                        "Accuracy": round(accuracy, 2)}
            return results
        return None
