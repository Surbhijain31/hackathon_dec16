#Defining the function
def show(string, word):
    
    #Counting occurrences of the word in the string
    words = string.split(' ')
    freq  = {}                   #Calculating frequency of words
    for w in words:
        if freq.has_key(w):
            freq[w] += 1
        else:
            freq[w] = 1
    a=freq[word]
    print "Occurence of word in string:",a

    #Removing that word from string
    for words in string:
        if word in string:
            string=string.replace(word,"")
            print "\nRemoving word from String.....\n", string

    #Appending same word equal to number of occurrences in string
    l = []
    while a>0:
        l.append(word)
        a=a-1
    l=''.join(l)
    string=''.join((string,l))
    print "\nAppending same word equal to number of occurrences in string\n",string

#Calling the function
show("This String is a String and a String","String") 
