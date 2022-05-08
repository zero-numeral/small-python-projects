import string

ALPHABET = string.ascii_lowercase

if __name__ == "__main__":
    message = input("Введите зашифрованное сообщение: ").lower()

    for offset in range(1, len(ALPHABET)):
        decoded = ""
        for char in message:
            if char in ALPHABET:
                decoded += ALPHABET[(ALPHABET.find(char) + offset) % len(ALPHABET)]
            else:
                decoded += char

        print(f'key {offset} -> {decoded}')
