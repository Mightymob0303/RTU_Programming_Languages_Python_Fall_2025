"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""
import re
def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))
def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = re.findall(r"-?\d+", text)  # find all integers (including negatives)
    return [int(num) for num in numbers]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0

    return char_count, word_count, numbers, total, average

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    char_count, word_count, numbers, total, average = analyze_text(text)

    print("\n--- Text Analysis Summary ---")
    print(f"Non-space characters: {char_count}")
    print(f"Word count: {word_count}")
    print(f"Numbers found: {numbers if numbers else 'None'}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")