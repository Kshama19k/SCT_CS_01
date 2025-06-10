def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (number): "))

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
