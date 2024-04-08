import sys

def cipher(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            # Checking if it's uppercase or lowercase
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 65)
            encrypted_message += encrypted_char

    return encrypted_message

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift>")
        sys.exit(1)

    # Get the shift value from command line arguments
    shift = int(sys.argv[1])

    message = input("Enter the message: ").upper()

    # Encoding each letter
    encoded_message = ''
    for char in message:
        if char.isalpha():
            encoded_message += cipher(char, shift)

    # final encoded message in blocks of five letters
    count = 0
    for char in encoded_message:
        print(char, end='')
        count += 1
        if count == 5:
            print(' ', end='')
            count = 0

if __name__ == "__main__":
    main()
