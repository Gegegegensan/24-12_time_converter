def caesar_encryption(text, delta):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for c in list(text.lower()):
        if c == " ":
            encrypted_text += " "
        for i, l in enumerate(alphabet):
            if c == l:
                encrypted_text += alphabet[(i+delta)%26]
return encrypted_text
