from art import logo, alphabet

alphabet = alphabet
continue_game = True

def caesar(user_text, shift_amount):
    message = ""
    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift_amount) % 26
                message += alphabet[new_position] 
            elif direction == "decode":
                new_position = (position - shift_amount) % 26
                message += alphabet[new_position]
        else:
            message += letter
        
    print(f"Your text is: {message}")   


while continue_game:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(user_text=text,shift_amount=shift)

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if repeat == "no":
        continue_game = False
        print("Good Bye!")

    
