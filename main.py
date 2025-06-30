morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

morse_to_text_dict = {v: k for k, v in morse_code_dict.items()}

final_sentence_array = []
seperator = " "
oper = input("Enter operation, to morse(m) or to actual sentence(s): ")
if oper == "m":
    word = input("Enter the sentence: ").upper()
    character_list = list(word)
    for item in character_list:
        if item in morse_code_dict:
            final_sentence_array.append(morse_code_dict[item])
        elif item == " ":
            final_sentence_array.append("/")
    final_sentence = seperator.join(final_sentence_array)
    print(final_sentence)
    print("Thanks for using the morse to text code generator!")

else:
    morse = input("Enter morse code: ")
    morse_list = morse.split(" ")
    for item in morse_list:
        if item =="/":
            final_sentence_array.append(" ")
        elif item in morse_to_text_dict:
            final_sentence_array.append(morse_to_text_dict[item])
        else:
            final_sentence_array.append("?")
    final_sentence = "".join(final_sentence_array)
    print(final_sentence)
    print("Thanks for using the text to morse code generator!")
