# Text Generator

#### Generates fake natural language text based on letter quantity and word length distribution of English.

Customizable variables:
- sentences: number of sentences to be generated
- cap_prob: = proportion of words to start with a capital letter
- comma_prob = density of commas

Parameters are chosen based on a 30,386 word body of English-language text from various sources (journalistic, encyclopedic, legal etc.):

- Letter distribution: see letters.txt
- Word length: mean = 4.93 characters, std = 2.66
- Sentence length: 28 words, std = 16

