# Problem Statement
# Program to find frequency of words in a file

from collections import defaultdict
import string

def count_word_frequencies (file_path):
    word_frequency defaultdict(int)
    with open(file_path, 'r') as file:
    for line in file:
        line line.translate(str.maketrans(",", string.punctuation)).lower()
        words line.split()
        
        for word in words:
        word_frequency[word] += 1
    return word_frequency

def get_top_n_words (word_frequency, n=10):
    sorted_words = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

file_path= input("Enter the path to the text file: ")

word_frequency count_word_frequencies (file_path)

top_words = get_top_n_words (word_frequency)

print("\nThe 10 most frequently appearing words are:")
for word, freq in top_words:
    print (f"{word): {freq) time(s)")
