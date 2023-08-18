#!/usr/bin/env python3

def return_evens(num_list):
    numbers = [n for n in num_list if n % 2 == 0]
    return numbers
  
return_evens([0,1,3,5,7,8,9])              

def make_exclamation(sentence_list):
    sentence = [x + '!' for x in sentence_list ]
    return sentence
make_exclamation(['Test', 'Sentence'])

