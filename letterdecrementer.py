#!usr/bin/python
# July 2018
# This utility is intended to help prospective poets
# take a crack at this challenge:
#
# https://twitter.com/angealbertini/status/1014592980018188288
#
# "I have a request for a MD5-related crypto song/poem...
# Each verse is 10-16 char, and the 10th char of each verse
# can be swapped with its successor, and give an extra (funny
# if possible) meaning. Any taker?"

outfile = 'ange-words.txt'
dictionary = '/usr/share/dict/american-english'
with open(dictionary, 'r') as f:
    wordlist = []
    wordlist = f.readlines()


def lookup(a_word):  # Return a boolean describing whether a word appears in the wordlist
    if a_word in wordlist:
        return True
    else:
        return False


def decrement(a_word, an_index):  # Decrements the ASCII value of the Nth character in a word
    fixed_offset = 1  # Decrement by this many steps. If offset = 1, 'B' becomes 'A'
    ascii_floor = 97  # 'a' is ASCII 97
    ascii_value = ord(a_word[an_index].lower()) - ascii_floor
    new_ascii_value = ((ascii_value - fixed_offset) % 26) + ascii_floor
    new_word = a_word[:an_index] + chr(new_ascii_value) + a_word[an_index+1:]
    return new_word


for currentword in wordlist:
    if len(currentword) > 2:
        for letterindex in range(0, len(currentword)):
            newword = decrement(currentword.lower(), letterindex)
            if lookup(newword):
                with open(outfile, 'a') as o:
                    o.write("{} | {}\n".format(currentword.rstrip(), newword.rstrip()))
                    print "Found pair: {} | {}\n".format(currentword.rstrip(), newword.rstrip())