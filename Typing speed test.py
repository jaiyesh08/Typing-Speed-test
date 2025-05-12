
## TYPING SPEED TEST ##


import time
import random

# Sample sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing tests are a fun way to improve your speed.",
    "Python is a versatile programming language.",
    "Practice makes perfect, especially when typing.",
    "Errors reduce your overall typing accuracy."
]

def typing_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")

    test_sentence = random.choice(sentences)
    print("\nType the following sentence as fast as you can:\n")
    print(f"\"{test_sentence}\"\n")

    input("Press Enter when you're ready...")
    start_time = time.time()

    typed_sentence = input("\nStart typing:\n")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(typed_sentence.split())
    speed_wpm = (words / elapsed_time) * 60

    # Accuracy check
    correct_chars = sum(1 for i, c in enumerate(typed_sentence) if i < len(test_sentence) and c == test_sentence[i])
    accuracy = (correct_chars / len(test_sentence)) * 100

    print("\n--- Results ---")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Typing Speed: {speed_wpm:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()