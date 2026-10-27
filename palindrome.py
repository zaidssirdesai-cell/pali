def is_palindrome(text):
	normalized = "".join(char.casefold() for char in text if char.isalnum())
	return normalized == normalized[::-1]


if __name__ == "__main__":
	value = input("Enter text: ")
	if is_palindrome(value):
		print("It is a palindrome.")
	else:
		print("It is not a palindrome.")