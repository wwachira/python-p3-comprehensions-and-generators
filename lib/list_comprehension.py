#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens
num_list = list(range(0, 100))
print(return_evens(num_list))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentences]

sentences = ["Welcome", "To", "Moringa_School"]
result = make_exclamation(sentences)
print(result)