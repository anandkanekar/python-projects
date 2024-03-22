import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle
from PyDictionary import PyDictionary

def get_dictinay_meaning():

    dictionary = PyDictionary()

    while True:
        word = word_input.get()
        if word != "":
            break
      
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, (dictionary.meaning(word)))
    result_text.config(state=tk.DISABLED)
    


# Create the main window
root = tk.Tk()
root.title("Word Dictionary")

# Use a themed style for improved aesthetics
style = ThemedStyle(root)
style.set_theme("arc")  # You can choose from various themes provided by ttkthemes

# Create a label with custom style
label = ttk.Label(
    root, text = "Enter word"
)
label.pack(pady=10)

# Create an input box with custom style
word_input = ttk.Entry(
    root, text = "Enter word"
)
word_input.pack(pady=10, ipadx=10, ipady=5)

# Create a button with the custom style
generate_button = ttk.Button(
    root, text="Generate Meaning", style="BlueGradient.TButton", command=get_dictinay_meaning
)
generate_button.pack(pady=10, ipadx=16, ipady=5)

# Create a scrolled text widget with rounded corners to display the generated story
result_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, height=10, width=60, state=tk.DISABLED
)
result_text.pack(padx=20, pady=10)

# Start the GUI main loop
root.mainloop()