from langchain_ollama import OllamaLLM
import tkinter as tk

# Initialize two LLaMA3 models
model_1 = OllamaLLM(model="llama3")
model_2 = OllamaLLM(model="llama3")

# Function for running the conversation
def run_conversation():
    # Initialize the conversation
    input_text = "Hello, how are you?"  # Initial prompt for Model 1
    conversation_log = []

    # Run the loop where the models talk to each other
    for i in range(10):  # 10 iterations
        print(f"Iteration {i+1}: Model 1 is generating...")
        result_1 = model_1.invoke(input=input_text)  # Model 1 responds
        conversation_log.append(f"Model 1: {result_1}")
        update_conversation(f"Model 1: {result_1}")

        print(f"Iteration {i+1}: Model 2 is generating...")
        result_2 = model_2.invoke(input=result_1)  # Model 2 responds to Model 1
        conversation_log.append(f"Model 2: {result_2}")
        update_conversation(f"Model 2: {result_2}")
        
        input_text = result_2  # Feed Model 2's output back into Model 1

# Simple UI using tkinter
root = tk.Tk()
root.title("LLaMA3 Model Conversation")

# Create a text widget to display the conversation
text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_widget.pack(pady=20, padx=20)

def update_conversation(text):
    text_widget.insert(tk.END, text + '\n')
    text_widget.update_idletasks()  # Update the UI in real time

# Trigger the conversation when script runs
if __name__ == "__main__":
    root.after(100, run_conversation)  # Delay to ensure UI loads first
    root.mainloop()
