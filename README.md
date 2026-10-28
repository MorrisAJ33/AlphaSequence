# AlphaSequence
Using Alphabet Letter Combinations as Sequence adding letters as the sequence grows.

(A...BC...CFA...BBZD...ALPHA...ZZZZZ)

Class Signature AlphaSequencer(max_chars:int=5, seq_max:int)

Example:

    # sgi sequence_generator_instance
    
    sgi = AlphaSequencer(max_char=4, seq_max=25_000)
    
    for c in sgi.sequence_gen():
    
        # StopIteration at seq_max
        
        chars = c #starts sequence over at max_char finish (e.g. 'ZZZZ' > 'A' happens at 475,255 steps)
        
    print(chars) #c @ 25,000 == 'AJYN'
        
Generator function does all single characters then repeats for duration of sequence maximum steps for each level set in max_char.

max_char = 1;  26 steps per loop (Alphabet Sequence standard)

max_char = 2; 702 steps per loop (26 single characters followed by 676 two character permutations e.g. ..'Z' > 'AA' > 'AB'..)

max_char = 3; 18,287 steps (Preceding single - double sequences followed by 17,576 three letter ordered permutations ..'Z'> 'AA' .. 'ZZ' > 'AAA'>'AAB'..'ZZZ'>'A'..)

max_char = 4; 475,254 step values (preceeding sequence values followed by 456,976 4 letter ordered sequence permutations)

max_char = 5; 12,356,630 unique step values (preceding sequence values followed by 11,881,376 5 letter ordered sequence permuations)

NOTE: All "4 letter words" are present in pemutations and sequence max_char 4 and greater including all Expletives as a result. 

