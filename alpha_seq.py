#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
alpha_seq.py: Alphabetical Sequence Combination Series Generator
Author: Alex Morris
Created: 2025-09-29
Version: 1.0
Description: Series Generators and Primary Import Sequence Object.
"""
__author__ = "Alex Morris"
__copyright__ = "Copyright 2026"
__license__ = "MIT"
__maintainer__ = __author__
#from memory_profiler import memory_usage
from datetime import datetime

def single_character():
    for x in range(65, 91):
        yield chr(x)

def double_character():
    for x in range(65, 91):
        for y in range(65, 91):
            yield chr(x) + chr(y)

def triple_character():
    for x in range(65, 91):
        for y in range(65, 91):
            for z in range(65,91):
                yield chr(x) + chr(y) + chr(z)

def quad_character():
    for x in range(65, 91):
        for y in range(65, 91):
            for z in range(65,91):
                for a in range(65,91):
                    yield chr(x) + chr(y) + chr(z) + chr(a)

def quint_character():
    for x in range(65, 91):
        for y in range(65, 91):
            for z in range(65,91):
                for a in range(65,91):
                    for b in range(65,91):
                        yield chr(x) + chr(y) + chr(z) + chr(a) + chr(b)

class AlphaSequencer():
    def __init__(self, max_chars=5, as_generator=False, seq_max=False):
        if not max_chars:
            max_chars = 5

        if max_chars > 5 or max_chars <= 0:
            print(f"*** max_chars= {max_chars} *** Invalid Value setting to 5")
            max_chars = 5
            
        self._max_chars = max_chars
        self._character_limit = sum([26 ** (i) for i in range(1, self._max_chars + 1)])
        self._series_max = seq_max
        self._as_gen = as_generator
        self._generate_single = False
        self._generate_double = False
        self._generate_triple = False
        self._generate_four = False
        self._generate_five = False
        self._series_pos = 1
        self.total_steps = 1

    def __letter_generator(self):
        if self._series_pos <= 26:
            return self._generate_single.__next__()
        elif self._series_pos <= 702:
            return self._generate_double.__next__()
        elif self._series_pos <= 18_278:
            return self._generate_triple.__next__()
        elif self._series_pos <= 475_254:
            return self._generate_four.__next__()
        elif self._series_pos <= 12_356_630:
            return self._generate_five.__next__()

    def __initialize_generators(self):
        if self._max_chars >= 1:
            self._generate_single = single_character()

        if self._max_chars >= 2:
            self._generate_double = double_character()

        if self._max_chars >= 3:
            self._generate_triple = triple_character()

        if self._max_chars >= 4:
            self._generate_four = quad_character()

        if self._max_chars == 5:
            self._generate_five = quint_character()

    def sequence_gen(self):
        if not self._series_max:
            raise AttributeError("Must provide series_max input argument for Generator")

        while self.total_steps <= self._series_max:
            if self._series_pos > self._character_limit:
                self._series_pos = 1

            if self._series_pos == 1:
                self.__initialize_generators()

            yield self.__letter_generator()
            self._series_pos += 1
            self.total_steps += 1

def _performance(sequence_max=12_356_630):
    seq = AlphaSequencer(seq_max=sequence_max+1)
    letters = [i for i in seq.sequence_gen()]
    del letters

def _performance2(sequence_max=12_356_630):
    seq = AlphaSequencer(seq_max=sequence_max+1)
    for i in seq.sequence_gen():
        letters = i
    del letters


def numeric_alphabet_lookup():
    alphabet = {a+1:b for a, b in enumerate(single_character())}
    alphabet[0] = " "
    return alphabet

def alphabet_numeral_lookup():
    alphabet = {b: a+1 for a, b in enumerate(single_character())}
    alphabet[" "] = 0
    return alphabet

def at_value(value, chars):
    seq = AlphaSequencer(max_chars=chars, seq_max=value)
    letter = ''
    for c in seq.sequence_gen():
        letter = c
    print(letter)

"""if __name__ == "__main__":
    start = datetime.now()
    mem_usage = memory_usage(_performance)
    print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print('Maximum memory usage: %s' % max(mem_usage))

    print(f"{datetime.now()-start}")"""