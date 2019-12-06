#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = 'ericmhanson'

import re


def find_words(input_word, dictionary):
    """ finds matching words in the dictionary """
    regex = r'\w'

    new_word = input_word.replace(' ', regex)
    re_word = re.compile(new_word)

    for word in dictionary:
        if len(word) == len(input_word):

            if re.match(re_word, word):
                print(word)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters:\
        ').lower()

    find_words(test_word, words)
    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
