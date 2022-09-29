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
# function for checking the dictionary based on the limit
def limit_check_dict(dictfilename):
    with open(dictfilename, "r") as f:
        dictfile = [line.strip() for line in f] # get original string length
    check_dict_size(dictfile) # limit: Check dictionary element and total size
    check_dict_dup(dictfile) # limit: check duplicate element in list
    return dictfile


@failure('')
def limit_check_input(inputfilename):
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
        dictfile = limit_check_dict(var_dictfile) #validate the dictionary based on the "limit".
        inputfile =limit_check_input(var_inputfile) #validate the input file based on the "limit"

        casecntr = 0
        for inputstr in inputfile:
            casecntr += 1 # case number counter
            dupcntr = 0 # duplicate counter.  show number of times the dictionary value appeared

            for testc in dictfile:
                tmplist = []
                testclen = len(testc) # get the length of the dictionary word element

                for yvar, ycntr in enumerate(inputstr): #enumerate through each of the character in the input file
                    testcsorted = ''.join(sorted(testc)) #before hashing, sort into alphabetical order the dictionary word/element
                    mainhashedtest = hashlib.md5(testcsorted.encode('utf-8')).hexdigest()  # main hash.  hash the sorted dictionary word/element
                    sstr = inputstr[yvar:yvar + testclen] #from the current position in the list, get the word based on the length of the dictionary word/element

                    if sstr[0] == testc[0] and testc[len(sstr) - 1] == sstr[len(sstr) - 1]: # a string with the same first and last char was found
                        sortedsubstrhash = hashlib.md5(''.join(sorted(sstr)).encode('utf-8')).hexdigest() # sort the string and hash. if its equal to the main hash, then they are the same
                        # check if the same value as the main hash.  if true, then they are the same string.
                        # if true, store the original unsorted string and store in the tmplist so we can check later if it already occured.
                        if sortedsubstrhash == mainhashedtest:
                            # check first if this string already exist on the list
                            if sstr not in tmplist:
                                dupcntr += 1
                                tmplist.append(sstr)
            print("case #" + str(casecntr) + ": " + str(dupcntr) )

    except Exception as e:
        print(e)
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "CRITICAL"))

