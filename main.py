#!/usr/bin/env python

import random as r
import numpy as np

__author__ = "Manuel J. Adams"
__version__ = "1.1"

sentences = 40      # number of sentences to be generated
cap_prob = 0.05     # density of capitalized words
comma_prob = 0.1    # density of commas

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
vowels    = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
letter_weights_EN = [89, 15, 26, 39, 126, 20, 19, 53, 69, 2, 8, 45, 25, 71, 73, 19, 1, 64, 64, 91, 30, 11, 19, 1, 17, 1]
vowel_weights_EN = [89, 126, 69, 73, 30]
cons_weights_EN = [15, 26, 39, 20, 19, 53, 2, 8, 45, 25, 71, 19, 1, 64, 64, 91, 11, 19, 1, 17, 1]

def main():
    text = ''
    for s in range(sentences):
        sentence = ''                                               # start new sentence
        first_letter = letters[r.randint(0, len(letters) - 1)]    # first letter of sentence (cap)
        sentence += first_letter
        sent_length = max(3, int(np.random.normal(28, 16)))          # sentence length: normal(mean, std)
        word_length_last = 0
        for w in range(sent_length):
            word = build_word(w, sent_length, word_length_last)
            comma = True if comma_prob > np.random.rand() and 2 < w < sent_length - 3 else False # determine if comma (not to close to beginning or end)
            sentence += word + ', ' if comma else word + ' ' # add word to sentence (and comma if applicable)
        sentence = (sentence + '.').replace(' .', '. ') if 0.05 < np.random.rand() else (sentence + '?').replace(' ?', '? ') # determine if exclamation point
        text += sentence + '\n' if (s+1)%10 == 0 else sentence # structure text into paragraph

    print(text)

def build_word(w, sent_length, word_length_last):
    # start new word
    word = ''
    # decide if to start with vowel
    vowel_start = True if 0.5 > np.random.rand() else False
    # determine word length: normal(mean, std)
    word_length = max(1, int(np.random.normal(4.9, 2.7)))
    # prevent single-letter word at end of sentence and two in a row
    word_length = word_length + 1 if word_length == 1 and (w == sent_length-1 or word_length_last == 1) else word_length
    word_length_last = word_length
    # determine if word capitalized (extra letter in addition to word length)
    cap = True if cap_prob > np.random.rand() and w > 0 and word_length > 3 else False
    word += letters[r.randint(0, len(letters) - 1)] if cap else word  # start word with cap if so decided above
    for l in range(word_length): # pick letters for word (consonants and vowels take turns, one-letter words are vowels)
        if word_length == 1 or vowel_start:
            letter = r.choices(consonants, cons_weights_EN)[0] if l / 2 != l // 2 else r.choices(vowels, vowel_weights_EN)[0]
        else:
            letter = r.choices(consonants, cons_weights_EN)[0] if l / 2 == l // 2 else r.choices(vowels, vowel_weights_EN)[0]
        word += letter # add letter to word
    return word

if __name__ == '__main__':
    main()
