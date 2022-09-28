import hashlib
import sys, getopt
import logging



def limit_check_dict(dictfilename):
    try:
        with open(dictfilename, "r") as f:
            dictfile = [line.strip() for line in f] # get original string length
            check_dict_size(dictfile) # limit: Check dictionary element and total size
            check_dict_dup(dictfile) # limit: check duplicate element in list
    except Exception as e:
        print(e)
    return dictfile


def limit_check_input(inputfilename):
    try:
        with open(inputfilename, "r") as d:
            inputfile = [line.strip() for line in d]
    except Exception as e:
        print(e)
    return inputfile

# check the dictionary size
def check_dict_size(dictfile, minsize=2, maxsize = 105, totalmaxsize = 105):
    try:
        totaldictlen = len(''.join(dictfile))
        if totaldictlen > totalmaxsize:
            raise Exception("Greater than total maxsize of " + str(totalmaxsize))
        for dicx in dictfile:
            if len(dicx) < minsize:
                raise Exception("dictionary lesser than " + str(minsize))
            elif len(dicx) > maxsize:
                raise Exception("greater than " + str(maxsize))
    except Exception as e:
        print(e)
        sys.exit(1)

#check for duplicate in dictionary
def check_dict_dup(dictfile):
    try:
        if len(dictfile) != len(set(dictfile)):
            raise Exception("There is a duplicate in the list")
    except Exception as e:
        print(e)
        sys.exit(1)



if __name__ == '__main__':

    argumentList = sys.argv[1:]
    # Options
    options = ""
    # Long options
    long_options = ["dictionary=", "input="]
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

    try:
        dictfile = limit_check_dict(var_dictfile)
        inputfile =limit_check_input(var_inputfile)

        casecntr = 0
        for inputstr in inputfile:
            casecntr += 1
            dupcntr = 0

            for testc in dictfile:
                tmplist = []
                testclen = len(testc)

                for y, ycntr in enumerate(inputstr):
                    # get the length of the testing string
                    # sorted testc prepared for hashing
                    testcsorted = ''.join(sorted(testc))
                    # main hash.  hash the sorted string.
                    mainhashedtest = hashlib.md5(testcsorted.encode('utf-8')).hexdigest()
                    # get the string with the same length as the one in the dictfile(list)
                    sstr = inputstr[y:y + testclen]
                    # a string with the same first and last char was found
                    if sstr[0] == testc[0] and testc[len(sstr) - 1] == sstr[len(sstr) - 1]:
                        # sort the string and hash. if its equal to the main hash, then they are the same
                        sortedsubstrhash = hashlib.md5(''.join(sorted(sstr)).encode('utf-8')).hexdigest()

                        # check if the same value as the main hash.  if true, then they are the same string. if true, store the original unsorted string and store in the tmplist so we can check later if it already occured.
                        if sortedsubstrhash == mainhashedtest:
                            # check first if this string already exist on the list
                            if sstr not in tmplist:
                                dupcntr += 1
                                tmplist.append(sstr)
            print("case #" + str(casecntr) + ": " + str(dupcntr) )

    except Exception as e:
        print(e)


