from string import ascii_lowercase as lower, ascii_uppercase as upper
import sys

def encrypt(shift: int, msg: str) -> str:
    """
    Encrpt a message using the given right-shift.

    :param shift: the number of letters to move rightward
    :param msg: the text to be encrypted
    :return: the encryted message
    """
    shift = shift%26
    ref = {orig: equiv for orig, equiv in zip(lower, lower[shift:]+lower[:shift])}
    ref_upper = {orig: equiv for orig, equiv in zip(upper, upper[shift:]+upper[:shift])}

    ref.update(ref_upper)

    return msg.translate(str.maketrans(ref))

def decrypt(shift: int, msg: str) -> str:
    """
    Decrypt a message using the original right-shift.

    :param shift: the right-shift used for the original encryption
    :param msg: the cipher to be decrypted
    :return: the plaintext message
    """
    shift = shift%26
    ref = {equiv: orig for orig, equiv in zip(lower, lower[shift:]+lower[:shift])}
    ref_upper = {equiv: orig for orig, equiv in zip(upper, upper[shift:]+upper[:shift])}

    ref.update(ref_upper)

    return msg.translate(str.maketrans(ref))


if __name__ == "__main__":
    print("Simple Caesar Cipher Program")
    print("----------------------------")

    print("Options:\n\t(1) ENCRYPT\n\t(2) DECRYPT\n\t(0) EXIT\n")

    while True:
        while True:
            choice: int = input("Select an option(#):\n>")
            try:
                choice = int(choice)
            except:
                print("Invalid input: please enter a number.\n")
            else:
                if choice not in (0,1,2):
                    print("Invaid input: please enter 0, 1, or 2.\n")
                else: break
    
        if choice == 0:
            print("[EXIT]")
            sys.exit()
        
        message: str = input("\nEnter message:\n>")
        while True:
            shift: int = input("\nEnter right-shift value:\n>")
            try:
                shift = int(shift)
                break
            except:
                print("Invalid input: please enter a number.\n")

        match choice:
            case 1:
                translation: str = encrypt(shift, message)
                print(f"\nPlaintext:\n{message}\n\nCiphertext:\n{translation}\n")
            case 2: 
                translation: str = decrypt(shift, message)
                print(f"\nCiphertext:\n{message}\n\nPlaintext:\n{translation}\n")
