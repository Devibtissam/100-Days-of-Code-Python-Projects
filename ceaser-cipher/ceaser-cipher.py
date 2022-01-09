logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text,shift,direction):
    if direction=='encode':
        cipher_text = " "
        for char in text:
            if char in alphabet:
                pos = alphabet.index(char)
                if shift+pos >= len(alphabet):
                    cipher_text += alphabet[(pos + shift % 26)-len(alphabet)]
                else:
                    cipher_text += alphabet[pos+shift]
            else:
                cipher_text += char

        
    else:
        cipher_text = " "
        for char in text:
            if char in alphabet:
                pos = alphabet.index(char)
                if pos < shift:
                    cipher_text += alphabet[len(alphabet) - (shift % 26 - pos)]
                else:
                    cipher_text += alphabet[pos-shift]
            else:
                cipher_text += char

    print(cipher_text)


print(logo)

should_end=True

while should_end!=False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text,shift,direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = False
        print("Goodbye")
    