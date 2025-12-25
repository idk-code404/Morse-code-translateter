# file: english_morse_converter.py

# Dictionary mapping English letters and digits to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Using '/' to separate words
}

# Reverse dictionary for decoding
MORSE_CODE_REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def english_to_morse(text: str) -> str:
    """
    Converts English text to Morse code.
    """
    text = text.upper()
    morse_text = []
    for char in text:
        morse_text.append(MORSE_CODE_DICT.get(char, '?'))
    return ' '.join(morse_text)

def morse_to_english(morse_code: str) -> str:
    """
    Converts Morse code to English text.
    """
    words = morse_code.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_REVERSE_DICT.get(letter, '?') for letter in letters)
        decoded_words.append(decoded_word)
    
    return ' '.join(decoded_words)

if __name__ == "__main__":
    choice = input("Type 'E' to encode or 'D' to decode: ").upper()
    if choice == 'E':
        text = input("Enter English text: ")
        print("Morse Code:", english_to_morse(text))
    elif choice == 'D':
        code = input("Enter Morse code (use '/' for space): ")
        print("English Text:", morse_to_english(code))
    else:
        print("Invalid choice.")
