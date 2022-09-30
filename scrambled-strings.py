import hashlib
import sys, getopt, os
import logging

#decorator
def failure(value):
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         return f(*args,**kwargs)
      except Exception as e:
         print(e)
         logging.basicConfig(level=os.environ.get("LOGLEVEL", "CRITICAL"))
    return applicator
  return decorate


@failure('')
# validator: check the dictionary based on limit
def validator_check_dict(dictfilename):
    with open(dictfilename, "r") as f:
        dictfile = [line.strip() for line in f] # get original string length
    check_dict_size(dictfile) # limit: Check dictionary element and total size
    check_dict_dup(dictfile) # limit: check duplicate element in list
    return dictfile


@failure('')
def validator_check_input(inputfilename):
    with open(inputfilename, "r") as d:
        inputfile = [line.strip() for line in d]
    return inputfile

# check the dictionary size
@failure('')
def check_dict_size(dictfile, minsize=2, maxsize = 105, totalmaxsize = 105):
    totaldictlen = len(''.join(dictfile))
    if totaldictlen > totalmaxsize:
        raise Exception("Greater than total maxsize of " + str(totalmaxsize))
    for dicx in dictfile:
        if len(dicx) < minsize:
            raise Exception("dictionary lesser than " + str(minsize))
        elif len(dicx) > maxsize:
            raise Exception("greater than " + str(maxsize))

#check for duplicate in dictionary
@failure('')
def check_dict_dup(dictfile):
    if len(dictfile) != len(set(dictfile)):
        raise Exception("There is a duplicate in the list")


if __name__ == '__main__':

    argumentList = sys.argv[1:]
    options = ""
    long_options = ["dictionary=", "input="] # specify the options for the argument input
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-d", "--dictionary"):
                var_dictfile = currentValue
            elif currentArgument in ("-i", "--input"):
                var_inputfile = currentValue
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "CRITICAL"))
    try:
        dictfile = validator_check_dict(var_dictfile) #validate the dictionary based on the "limit". will return a list
        inputfile = validator_check_input(var_inputfile) #validate the input file based on the "limit". will return a list

        casecntr = 0
        for inputstr in inputfile: # loop for each line in input file
            casecntr += 1 # case number counter
            dupcntr = 0 # duplicate counter.  show number of times the dictionary value appeared

            for dict_word in dictfile: #loop for each element in dictionary
                tmplist = [] #temporary list to store hashed words that already occured.
                dict_word_len = len(dict_word) # get the length of the dictionary word

                for yvar, ycntr in enumerate(inputstr): #enumerate through each of the character in the input file string
                    dict_word_sorted = ''.join(sorted(dict_word)) #dict_word_sorted is a variable for the sorted dictionary word.
                    mainhashedtest = hashlib.md5(dict_word_sorted.encode('utf-8')).hexdigest()  # mainhashedtest  hash the sorted dictionary word/element. (dict_word_sorted)

                    input_substr = inputstr[yvar:yvar + dict_word_len] #retrieve the substring from the "input" string starting from the current position up to the length of the dictionary word.

                    #input_substr is the substring.  dict_word is the dictionary word being checked
                    if input_substr[0] == dict_word[0] and dict_word[len(input_substr) - 1] == input_substr[len(input_substr) - 1]: # compare if the  dictionary words first and last character is the same as the "input" strings' first and last character.
                        sortedsubstrhash = hashlib.md5(''.join(sorted(input_substr)).encode('utf-8')).hexdigest() # sort the string and hash. if its equal to the main hash, then they are the same
                        # check if the same value as the main hash.  if true, then they are the same string.
                        if sortedsubstrhash == mainhashedtest:
                            # check first if this string already exist on the list  #if the input_substr already occured before do not count it and do not append in the tmplist.
                            if input_substr not in tmplist:
                                dupcntr += 1
                                tmplist.append(input_substr)  # if true, store the original unsorted string and store in the tmplist so we can check later if it already occured.

            print("case #" + str(casecntr) + ": " + str(dupcntr) )

    except Exception as e:
        print(e)
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "CRITICAL"))

