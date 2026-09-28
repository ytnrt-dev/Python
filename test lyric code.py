import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Huwag nang", 0.08),
        ("mag-alangan", 0.08),
        ("Ika'y laling", 0.18),
        ("uunahin", 0.25),       # After this (4th line), clear the first 4 lines
        ("Bawat patak", 0.10),
        ("ng 'yong", 0.18),
        ("luha'y", 0.10),
        ("papawiin", 0.30),
        ("Sa'king", 0.25),
        ("mundong", 0.15),
        ("puno ng", 0.08),
        ("pagsisisi", 0.15),
        ("Sa'yo kailanman ay", 0.08),
        ("hindi", 0.10),
        ("magsisisi", 0.25),
    ]

    delays = [0.08, 0.90, 0.20, 5.20, 0.80, 0.40, 0.70, 5.00, 1.50, 0.90, 0.80, 
              4.60, 1.80, 1.50, 5.00]

    for i, (line, char_delay) in enumerate(lines):
        # Print the line character by character with delay
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        
        # Wait for the line delay after printing
        time.sleep(delays[i])
        
        # For lines 1-4, just move to the next line
        if i < 3:
            print()
        
        # After the 4th line (index 3), clear the first 4 lines
        elif i == 3:
            # Move up and clear each of the 4 lines
            for _ in range(4):
                print('\033[1A\033[2K', end='')  # \033[1A: move up 1 line, \033[2K: clear line
            sys.stdout.flush()
            print()  # Move to the next line after clearing
    
    # Final newline for clean output
    print()

print_lyrics()
