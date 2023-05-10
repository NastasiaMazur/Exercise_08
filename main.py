#1
def write_to_file(text, output_file_path):
    import os
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file from ex1 already exists!")
    with open(output_file_path, 'w') as f:
        f.write(text)

#Usage
write_to_file("Hello, world!", "output_file_ex1_(warning!x2).txt")

#2
#function that generates a file with random text inside
import random
import string

def generate_random_text_file(file_path, num_words):
    with open(file_path, "w") as f:
        words = []
        for i in range(num_words):
            word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 10)))
            words.append(word)
        text = ' '.join(words)
        f.write(text)

import spacy

def count_stopwords(input_file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(input_file_path, 'r') as f:
        text = f.read()
    doc = nlp(text)
    stop_words = spacy.lang.en.stop_words.STOP_WORDS
    count = sum([1 for token in doc if token.text.lower() in stop_words])
    return count

#Usage
random_text_file = 'random_text.txt'
generate_random_text_file(random_text_file, 1000)
num_stopwords = count_stopwords(random_text_file)
print(f'Number of stopwords in {random_text_file}: {num_stopwords}')

#3
import spacy

def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, 'r') as f:
        text = f.read()
    doc = nlp(text)
    stopwords = set([token.text for token in doc if token.is_stop])
    result = ' '.join([token.text for token in doc if not token.is_stop])
    with open(output_file_path, 'w') as f:
        f.write(result)
    print("Removed stopwords:", ', '.join(stopwords))
#Usage
remove_stopwords("random_text.txt", "output_file_ex3.txt")

#4
def generate_file_ex4():
    with open("file_ex4.txt", "w") as file:
        file.write("Hello My name is Matthias and I'm 32 years old")
generate_file_ex4()

import spacy

def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    doc = nlp(text)

    # write the tokenized text to the output file in tabular form
    with open(output_file_path, 'w') as output_file:
        for token in doc:
            output_file.write(f"{token.text:{10}}{token.pos_:{10}}{token.dep_:{10}}\n")

#Usage
input_file_path = 'file_ex4.txt'
output_file_path = 'output_file_ex4.txt'

tokenize_text(input_file_path, output_file_path)

#5
import spacy
from spacy import displacy

def save_visualization(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        text = f.read().strip()

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    svg = displacy.render(doc, style='dep', jupyter=False)
    with open(output_file_path, 'w') as f:
        f.write(svg)
#Usage
save_visualization('file_ex4.txt', 'output_file_ex5.svg')