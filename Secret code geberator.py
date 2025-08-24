# ============================================
# Secret Code Generator (Caesar Cipher)
# ============================================

def encode_message(message, shift):
    """
    Encode a message using Caesar cipher by shifting letters forward.
    """
    result = ""
    # --- Loop through each character ---
    for char in message:
        if char.isalpha():
            # --- Handle uppercase vs lowercase ---
            base = ord('A') if char.isupper() else ord('a')
            # --- Shift and wrap around alphabet ---
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # --- Keep non-letters unchanged ---
            result += char
    return result

# ============================================

def decode_message(message, shift):
    """
    Decode a message that was encoded using Caesar cipher.
    """
    return encode_message(message, -shift)

# ============================================

def menu():
    """
    Display the main menu for the Secret Code Generator.
    """
    while True:
        print("\n=== Secret Code Generator ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter the message: ")
            shift = int(input("Enter shift number: "))
            print("Encoded message:", encode_message(text, shift))
        elif choice == "2":
            text = input("Enter the coded message: ")
            shift = int(input("Enter shift number: "))
            print("Decoded message:", decode_message(text, shift))
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# ============================================

if __name__ == "__main__":
    menu()
