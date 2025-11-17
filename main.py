from mywordslist import alphabets
from mywordslist import special_characters
from arts import ceaser_cipher_logo

def ceaser_cipher(text, shift, direction):
    if direction == "encode":
        for i in range(len(text)):
            if text[i] in special_characters:
                continue
            place_of_letter = alphabets.index(text[i])
            text[i] = alphabets[(place_of_letter + shift) % len(alphabets)]
        print(f"\nThe encrypted text is: {''.join(text)}")
    elif direction == "decode":
        for i in range(len(text)):
            if text[i] in special_characters:
                continue
            place_of_letter = alphabets.index(text[i])
            text[i] = alphabets[(place_of_letter - shift) % len(alphabets)]
        print(f"\nThe decrypted text is: {''.join(text)}")

print(f"{ceaser_cipher_logo}\n")

choice = True        
while choice:
    direction_given = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    if not(direction_given == "encode" or direction_given == "decode"):
        print("\nWrong Choice!")
        continue
    text_to_shift = input("\nType your message: ").lower()
    text_to_shift = list(text_to_shift)
    shift_digit = int(input("\nType the shift number: "))
    ceaser_cipher(text_to_shift, shift_digit, direction_given)
    
    #To Check if user still want to continue on using the program:
    continue_status = input(f"\nType 'yes' if you want to go again. otherwise type 'no': ")
    if continue_status == "no":
        choice = False
        print("\nGood Bye Then!")
