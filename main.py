import customtkinter
import ui 
import sentence_loader

# Handles the UI
app = ui.App()

# run the loop
app.mainloop()


if app.final_results is not None:
    print(f"Final Typing Test Results: {app.final_results}")
else:
    print("Typing test was closed without completing or generating results.")
