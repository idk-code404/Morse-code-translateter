# English ↔ Morse Code Converter

A simple Python script to convert English text to Morse code and vice versa.

## Features

- Convert English text to Morse code.
- Decode Morse code back to English.
- Handles letters, numbers, and spaces.
- Unknown characters are represented as `?`.
- Use `/` to separate words in Morse code.

## Requirements

- Python 3.x

## Usage

1. Clone or download the repository.
2. Run the script:

```bash
python english_morse_converter.py

    Follow the prompts:

        Type E to encode English → Morse.

        Type D to decode Morse → English.

    Example:

Encoding:

Enter English text: Hello World
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Decoding:

Enter Morse code (use '/' for space): .... . .-.. .-.. --- / .-- --- .-. .-.. -..
English Text: HELLO WORLD

Notes

    Unknown characters are replaced with ?.

    Words in Morse code must be separated by /.

License

MIT License
