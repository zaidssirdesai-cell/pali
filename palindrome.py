import sys

def is_palindrome(text):
    normalized = "".join(char.casefold() for char in text if char.isalnum())
    return normalized == normalized[::-1]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        value = " ".join(sys.argv[1:])
    else:
        print("Error: No text provided.", file=sys.stderr)
        sys.exit(1)

    print(f"Checking text: '{value}'")
    if is_palindrome(value):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
        sys.exit(1)  
