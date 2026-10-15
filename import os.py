import os
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def sing(words):
    for word, char_delay, pause_after in words:
        for ch in word:
            print(ch, end='', flush=True)
            sleep(char_delay)
        sleep(pause_after)


lines = [

    [
        ("Do ",        0.07, 0.05),
        ("you ",       0.08, 0.10),
        ("think ",     0.07, 0.25),
        ("I ",         0.07, 0.05),
        ("have ",      0.10, 0.25),
        ("for",        0.08, 0.00),
        ("got",        0.08, 0.00),
        ("ten?",        0.12, 1.50),
    ],

    [
        ("A",          0.08, 0.00),
        ("bout ",      0.09, 0.50),
        ("you? ",      0.12, 0.35),
        ("(Don't ",    0.09, 0.05),
        ("let ",       0.09, 0.05),
        ("go)",        0.12, 1.70),
    ],

    [
        ("A",          0.08, 0.00),
        ("bout ",      0.09, 0.50),
        ("you",        0.12, 3.70),
    ],

    [
        ("A",          0.08, 0.00),
        ("bout ",      0.09, 0.50),
        ("you",        0.12, 3.40),
    ],

    [
        ("Do ",        0.07, 0.05),
        ("you ",       0.08, 0.10),
        ("think ",     0.07, 0.25),
        ("I ",         0.07, 0.05),
        ("have ",      0.10, 0.25),
        ("for",        0.08, 0.00),
        ("got",        0.08, 0.00),
        ("ten?",       0.12, 1.50),
    ],

    [
        ("A",          0.08, 0.00),
        ("bout ",      0.09, 0.50),
        ("you? ",      0.12, 0.35),
        ("(Don't ",    0.09, 0.05),
        ("let ",       0.09, 0.05),
        ("go)",        0.12, 2.70),
    ],
]

for line in lines:
    clear()
    sing(line)
    print()