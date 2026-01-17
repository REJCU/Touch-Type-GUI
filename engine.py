import time

Class TypingEngine():
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
            
            

