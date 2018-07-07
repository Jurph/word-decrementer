# word-decrementer

On 5 JUL 18, Ange Albertini posted the following tweet: 
https://twitter.com/angealbertini/status/1014592980018188288

_"I have a request for a MD5-related crypto song/poem...
Each verse is 10-16 char, and the 10th char of each verse
can be swapped with its successor, and give an extra (funny
if possible) meaning. Any taker?"_ 

**letterdecrementer.py** takes the dictionary file listed in the script
and performs the following steps: 
1. Discard words of length 2 or less
2. "Decrement" (including wraparound A decrement to Z) a single letter in the word 
3. Check to see if the word is in the dictionary 
4. Write valid pairs to the output file listed in the script

I have also committed **ange-words.txt** which is the output created
when the Ubuntu `wamerican` package is installed and the dictionary 
`/usr/share/dict/american-english` is used to seed the process. 


