Word Scrambler

Note: This code was not written based on the efficiency or time complexity factor.  
The goal of this script is to design a short working code without the intricacies of time complexity computation.

**Requirements:**
* Python version 3.7+

**Files**
* scrambled-strings.py
* dictionary.txt
* input.txt

**Usage**
* command line format: python3 scrambled-strings --dictionary [PATH TO DICTIONARY FILE] --input [PATH TO INPUT FILE]

**Options**
* dictionary - dictionary file that contains the words to be search inside the "input file".  Each words are separated by a new line.
* input - input file that contains the list of long strings.  These strings will be searched for any occurences of the words in the dictionary file.  Each string is separated by a new line.

**Input Validations**
  * No two words in the dictionary are the same.
  * Each word in the dictionary is between 2 and 105 letters long, inclusive.
  * The sum of lengths of all words in the dictionary does not exceed 105.

**Short Description:**
Count how many of the words from a dictionary appear as substrings in a long string of
characters either in their original form or in their scrambled form. The scrambled form of the
dictionary word must adhere to the following rule: the first and last letter must be maintained
while the middle characters can be reorganised.

Please refer to the google kick start problem https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004.

**Details of the solution**
definition:  
word - each element or word in the dictionary file separated by a new line.

*  The core idea for the solution was the use of hashing(md5) to search for the occurences of the **word** as a substring for each "input" string.
* Because hashing the word using MD5 will result in the same hashed string, it would save us time in trying to check every character on each word to each character in the substring.
* Note: I did not use the **map** function so that i can show the solution line-by-line within the nested loop in one scope. 

On the pseudocode below, we will start on the 80th line, looping through each word in the dictionary.
1. 80: retrieve word from dictionary.
2. 84: loop/enumerate through each of the character in the string of the input.  I used enumerate so i can get the index number without defining any variable as incremental counter.
3. 85: sort the word alphabetically.
4. 86: hash the sorted word.  This hashed word will be used for comparison with the substring extracted from the input string.
5. 88: extract the substring from the input string based on the index location(yvar) and the length of the word being compared.
6. 91: Check if the first character of input substring is equal to the  first character of the word and the last character of the input substring is the same as the last character of the word.
7. 92: If they are the same, sort and hashed this substring to be compared later with the mainhashedtest variable.
8. 94: check if the hashed main word (refer to line 86. mainhashedset) is the same as the hashed and sorted substring (sortedsubstrhash)
9. 96: if the input string is not yet stored in the tmplist variable list, increment dupcntr and append in the tmplist.

