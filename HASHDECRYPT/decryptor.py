import os
import pyfiglet
import colorama
def textsd(text, font_style="3-d"):
    ascii_art = pyfiglet.figlet_format(text, font=font_style)
    print(colorama.Fore.WHITE + ascii_art)
def decryptor(hash_to_find):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, 'passwordlist.txt')
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 3 and parts[1] == hash_to_find:
                    print(colorama.Fore.YELLOW + "Decrypted Hash:", parts[2])
                    return
    except:
        print(colorama.Fore.RED + "Hash not found in the list.")

while True:
    os.system("cls")
    # Get input hash from the user
    textsd("""
HASH
DECRYPT
""")
    input_hash = input(colorama.Fore.WHITE + "Enter the hash to decrypt: ")
    decryptor(input_hash)
    input()
    os.system("cls")