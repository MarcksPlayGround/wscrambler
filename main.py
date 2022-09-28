import hashlib


dfile = ["axpaj","apxaj", "dnrbt", "pjxdn","abd","bb"]
ifile = "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjpdjxnfpvhdhhpxjdnrbt"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for testc in dfile:
        tmplist = []
        dupcntr = 0
        testclen = len(testc)
        for y, ycntr in enumerate(ifile):
            try:
                #get the length of the testing string
                #sorted testc
                testcsorted = ''.join(sorted(testc))
                #main hash.  hash the sorted string.
                mainhashedtest =  hashlib.md5(testcsorted.encode('utf-8')).hexdigest()

                #get the string with the same length as the one in the dfile(list)
                sstr = ifile[y:y+testclen]

                # a string with the same first and last char was found
                if sstr[0] ==  testc[0] and testc[len(sstr)-1] == sstr[len(sstr)-1]:
                    #sort the string and hash. if its equal to the main hash, then they are the same
                    sortedsubstrhash = hashlib.md5(''.join(sorted(sstr)).encode('utf-8')).hexdigest()

                    #check if the same value as the main hash.  if true, then they are the same string. if true, store the original unsorted string and store in the tmplist so we can check later if it already occured.
                    if sortedsubstrhash == mainhashedtest:
                        #check first if this string already exist on the list
                        if sstr not in tmplist:
                            dupcntr += 1
                            tmplist.append(sstr)

            except Exception as e:
                print(e)

        print(dupcntr)
        print(tmplist)
