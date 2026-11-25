# Function to count vowels including uppercase ones
def count_vowels(text):
    return sum(1 for c in text if c in "aeiouAEIOU")
