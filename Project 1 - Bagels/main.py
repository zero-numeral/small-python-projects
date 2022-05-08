#!/bin/python

import random
import string

NUM_DIGITS = 3
MAX_ATTEMPTS = 5


def generate_secret():
    assert 1 <= NUM_DIGITS <= 10, "Количество цифр должно быть от 1 до 10"

    secret = "0"
    while secret.startswith('0'):
        secret = "".join(random.sample(string.digits, NUM_DIGITS))

    return secret


def is_correct_input(capture):
    try:
        num = int(capture)  # Проверка на число
        if len(str(num)) != NUM_DIGITS:
            print("Неверное количество символов")
            print("Проверьте, число не должно начинаться нулем")
            return False
    except ValueError:
        print("Неверный формат введенных данных")
        return False

    return True


def get_clues(capture, secret):
    clues = []
    if all([digit not in secret for digit in capture]):
        clues.append("Bagels")
    else:
        for k, digit in enumerate(capture):
            if digit == secret[k]:
                clues.append("Fermi")
            elif digit in secret:
                clues.append("Pico")
    return sorted(clues)


def main():
    game_state = 'y'  # y/n

    while game_state == 'y':
        current_attempts = MAX_ATTEMPTS
        secret = generate_secret()
        guess = ""

        print(f"Угадайте загаданное {NUM_DIGITS} значное число: ", end='')

        while guess != secret:
            guess = input()
            while not is_correct_input(guess):
                guess = input()

            if guess == secret:
                print("Поздравляю, вы угадали.")
                break

            current_attempts -= 1
            if current_attempts <= 0:
                print("Попытки закончились ;{")
                break

            print(f"Осталось попыток: {current_attempts}")
            print(f'Подсказки: {get_clues(guess, secret)}')

        print("Желаете сыграть еще раз (y/n): ", end='')
        game_state = input().lower()
        while game_state not in ['y', 'n']:
            print("Введите y или n!!!")
            game_state = input().lower()

    print('Спасибо за игру!')


if __name__ == "__main__":
    main()
