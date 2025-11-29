# Strings

def is_palindrome(text:str):
    is_pal = False

    text = text.replace(" ", "").lower()
    text = ''.join(e for e in text if e.isalnum())
    if text == text[::-1]:
        is_pal = True

    return is_pal


def is_palindrome_refined(text: str):
    # Sanitize the string in one go
    clean_text = "".join(char for char in text.lower() if char.isalnum())

    # The comparison itself is a boolean, so no need for is_pal
    return clean_text == clean_text[::-1]

test = "A man, a plan, a canal: Panama"
print(is_palindrome(test))
print(is_palindrome_refined(test))
