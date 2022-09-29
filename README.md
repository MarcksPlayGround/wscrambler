Word Scrambler

Requirements:
* Python version 3.7+

Usage: command line format: python3 scrmabled-strings --dictionary [PATH TO DICTIONARY FILE] --input [PATH TO INPUT FILE]

* limitations
  * No two words in the dictionary are the same.
  * Each word in the dictionary is between 2 and 105 letters long, inclusive.
  * The sum of lengths of all words in the dictionary does not exceed 105.

Description:
Count how many of the words from a dictionary appear as substrings in a long string of
characters either in their original form or in their scrambled form. The scrambled form of the
dictionary word must adhere to the following rule: the first and last letter must be maintained
while the middle characters can be reorganised.

Please refer to the google kick start problem https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004.

Note: This code was not written based on the efficiency or time complexity factor.  
The goal of this script is to design a short working code without the intricacies of time complexity computation.


Logic:
The main idea in the code was to use hashing to check if the list of words in the dictionary is in each "inputfile" string. 

First we need to loop through each string in the input file. After that, we need to sort and hash(md5) the word in the dictionary.  
The purpose of hashing is to compare the dictionary word and the extracted substring from the input file if they are the same.
For every character of the input string being passed by, the script would extract the word with the same length as the dictionary word/element being compared to.
Then, proceed to check if the last and the first character of the extracted string and the dictionary word is the same.
If it's the same, to make everything much more efficient, we sorted the extracted string, hashed it and compared it to the original hashed dictionary word.
If the 2 hash are the same, then it means that the substring is the same as the one in the dictionary.

* sorry about the brief explanation, a lot of work suddenly needs to get done.