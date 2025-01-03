# Imported the tkinter module for creating the GUI
from tkinter import *

# Function to handle language translation
def translationFunction(language, word):
    # Dictionary storing translations for multiple languages; each language has a dictionary of word-translation pairs
    translations = {
        "Italian": {
            "ciao": "hello",
            "grazie": "thank you",
            "amore": "love",
            "gatto": "cat",
            "cane": "dog",
            "buongiorno": "good morning",
            "buonasera": "good evening",
            "per favore": "please",
            "scusa": "sorry",
            "arrivederci": "goodbye",
            "libro": "book",
            "acqua": "water",
            "pane": "bread",
            "vino": "wine",
            "sole": "sun",
            "luna": "moon",
            "mare": "sea",
            "montagna": "mountain",
            "città": "city",
            "famiglia": "family"
        },
        "Spanish": {
            "hola": "hello",
            "gracias": "thank you",
            "amor": "love",
            "gato": "cat",
            "perro": "dog",
            "buenos días": "good morning",
            "buenas tardes": "good afternoon/evening",
            "por favor": "please",
            "lo siento": "sorry",
            "adiós": "goodbye",
            "libro": "book",
            "agua": "water",
            "pan": "bread",
            "vino": "wine",
            "sol": "sun",
            "luna": "moon",
            "mar": "sea",
            "montaña": "mountain",
            "ciudad": "city",
            "familia": "family"
        },
        "Russian": {
            "privet": "hello",
            "do svidaniya": "goodbye",
            "spasibo": "thank you",
            "pozhaluysta": "please",
            "drug": "friend",
            "da": "yes",
            "net": "no",
            "khorosho": "good",
            "ploho": "bad",
            "dom": "house",
            "kniga": "book",
            "voda": "water",
            "chay": "tea",
            "moloko": "milk",
            "kafe": "coffee",
            "sobaka": "dog",
            "koshka": "cat",
            "yeda": "food",
            "rabota": "work",
            "shkola": "school"
        },
        "German": {
            "hallo": "hello",
            "auf Wiedersehen": "goodbye",
            "danke": "thank you",
            "bitte": "please",
            "freund": "friend",
            "ja": "yes",
            "nein": "no",
            "gut": "good",
            "schlecht": "bad",
            "haus": "house",
            "buch": "book",
            "wasser": "water",
            "tee": "tea",
            "milch": "milk",
            "kaffee": "coffee",
            "hund": "dog",
            "katze": "cat",
            "essen": "food",
            "arbeit": "work",
            "schule": "school"
        },
        "French": {
            "bonjour": "hello",
            "au revoir": "goodbye",
            "merci": "thank you",
            "s'il vous plaît": "please",
            "ami": "friend",
            "oui": "yes",
            "non": "no",
            "bon": "good",
            "mauvais": "bad",
            "maison": "house",
            "livre": "book",
            "eau": "water",
            "thé": "tea",
            "lait": "milk",
            "café": "coffee",
            "chien": "dog",
            "chat": "cat",
            "nourriture": "food",
            "travail": "work",
            "école": "school"
        }
    }
    # Returns the English translation of the word if found, otherwise returns "Word not found"
    return translations.get(language, {}).get(word, "Word not found")

# Function to create a new window for translating words from the selected language
def translationWindow(language):
    # Nested function to process the translation when the button is clicked
    def createTranslate(language):
        word = input_entry.get().lower()  # Get the input word in lowercase
        translation = translationFunction(language, word)  # Translate the word
        result_lbl.config(text=translation)  # Update the result label with the translation

    # Create a new top-level window
    transWin = Toplevel(root)
    transWin.title(f"{language} to English Translator")
    
    # Entry widget for user input
    input_entry = Entry(transWin)
    input_entry.pack()
    
    # Label to display the translation result
    result_lbl = Label(transWin, font=("Helvetica", 50))
    result_lbl.pack()
    
    # Button to trigger the translation process
    transBtn = Button(transWin, text ="Translate", command=lambda: createTranslate(language))
    transBtn.pack()

# Main application window
root = Tk()
root.title("Language Translator")
root.geometry("400x300")  # Set the size of the window

# Title label
title_label = Label(root, text="Welcome to the Language Translator!", font=("Helvetica", 16), pady=10)
title_label.pack()

# Subtitle label
subtitle_label = Label(root, text="Choose a language to proceed:", font=("Helvetica", 12), pady=10)
subtitle_label.pack()

# Frame to hold language selection buttons
buttons_frame = Frame(root)
buttons_frame.pack(pady=20)

# Buttons for selecting a language, each opening a translation window for the chosen language
spanish_button = Button(buttons_frame, text="Spanish", font=("Helvetica", 12), width=12, command=lambda: translationWindow("Spanish"))
spanish_button.grid(row=0, column=0, padx=10, pady=5)

french_button = Button(buttons_frame, text="French", font=("Helvetica", 12), width=12, command=lambda: translationWindow("French"))
french_button.grid(row=0, column=1, padx=10, pady=5)

german_button = Button(buttons_frame, text="German", font=("Helvetica", 12), width=12, command=lambda: translationWindow("German"))
german_button.grid(row=1, column=0, padx=10, pady=5)

russian_button = Button(buttons_frame, text="Russian", font=("Helvetica", 12), width=12, command=lambda: translationWindow("Russian"))
russian_button.grid(row=1, column=1, padx=10, pady=5)

italian_button = Button(buttons_frame, text="Italian", font=("Helvetica", 12), width=12, command=lambda: translationWindow("Italian"))
italian_button.grid(row=2, column=0, columnspan=2, pady=5)

# Run the application loop
root.mainloop()
