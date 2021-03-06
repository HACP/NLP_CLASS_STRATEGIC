import time

"""
06.24.2015

This library contains a classifier of a tweet based on:
MENTION
QUESTION_MARK
LINK
HASHTAG
PRICE
PERCENTAGE

CTA and EGOBOOST are part of the DEEP LEARNING that I am still optimizing. Here I give you a classifier based on key CTA_VERBS

If you need to do a binary classification i.e. link is present count how many times the word LINK is in the output 
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getNames():
    """
    This function tags a name from the CENSUS data base. LAter on I excluded common places like Vegas, Atlanta, Angeles, that happen also to be names
    """
    print 'Loading NAME database'
    t0 = time.time()

    f = open('DATA/NamesStatsCountsGender.dat')
    V  = []
    K = []
    for line in f:
        L = line[:-1].split(',')
        K.append(L[0])
        V.append([L[0],[float(item) for item in L[1:]]])

    t1 = time.time()
    dt = t1-t0
    print 'NAME database done ...', "%.2f" % dt, "seconds"
    return K, V

def textClass(text, NAMES):
    structured_text = []
    L0 = text.replace('-','').replace(':','').replace(',','').replace('!','').replace('&amp;', ' and ').replace('.','').replace('"','').replace('___','').replace('w/','with').replace('W/','with')
    L1 = L0.replace('?', ' QUESTION_MARK ')
    L2 = L1.split(' ')
    for n, i in enumerate(L2):
        if L2[n] == '@':
            L2[n] = 'AT'
        if len(L2[n]) > 1 and '@' in L2[n]:
            L2[n] = 'MENTION'
        if L2[n].lower() in ['hi','hello','hey','hola']:
            L2[n] = 'GREETING'
        if 'we' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'PERSON'
        if 'it' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'PERSON'
        if 'what' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'QUESTION_WORD'
        if 'where' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'QUESTION_WORD'
        if 'who' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'QUESTION_WORD'
        if 'how' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'QUESTION_WORD'
        if 'when' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'QUESTION_WORD'
        if L2[n].lower() in ['what','where', 'when', 'who', 'how']:
            L2[n] = 'QUESTION_WORD'
        if L2[n].lower() in ['we', 'you', 'your', 'our',"we'd", "you're","we're","you've","we've",'I','weve']:
            L2[n] = 'PERSON'
        if 'you' in L2[n].lower() and '_' in L2[n].lower():
            L2[n] = 'PERSON'
        if 'http' in L2[n]:
            L2[n] = 'LINK'
        if '%' in L2[n]:
            L2[n] = 'PERCENTAGE'
        if '$' in L2[n]:
            L2[n] = 'PRICE'
        if '#' in L2[n]:
            L2[n] = 'HASTAG'
        if L2[n] in NAMES and L2[n] not in ['White','Vegas','Atlanta']:
            L2[n] = 'NAME'
        if L2[n] in ['2013', '2014', '2015']:
            L2[n] = 'YEAR'
        if L2[n].lower() in ['a','an','the','those', 'these', 'many', 'few', 'several', 'none', 'little', 'all', 'some', 'plenty', 'lack']:
            L2[n] = 'ADQ'
        if L2[n].lower() in ['or', 'and','too', 'also']:
            L2[n] = 'CONNECTIVE'
        if L2[n].lower() in ['share','follow','tell']:
            L2[n] = 'VERB_CTA'


        try:
            if L2[n].lower() in ['want', 'love', 'like'] and L2[n+1].lower() in ['to'] and 'wed' in L2[n-1].lower() and len(L2[n-1])>3:
                corr_test = L2[n-2].replace('Wed','')
                if corr_test in NAMES:
                    L2[n-1] = 'NAME PERSON'
                    L2[n] = 'INVITATION'
                    L2[n+1] = ''
                else:
                    L2[n-1] = corr_test + ' PERSON'
                    L2[n] = 'INVITATION'
                    L2[n+1] = ''
        except:
            pass

        try:
            if L2[n].lower() in ['want', 'love', 'like'] and L2[n+1].lower() in ['to'] and 'wed' == L2[n-1].lower():
                L2[n-1] = 'PERSON'
                L2[n] = 'INVITATION'
                L2[n+1] = ''
        except:
            pass

        try:
            if L2[n].lower() in ['want', 'love', 'like'] and L2[n+1].lower() in ['to']:
                L2[n] = 'INVITATION'
                L2[n+1] = ''
        except:
            pass

    new_text = ''
    for item in L2[1:]:
        new_text = new_text + ' ' + item

    return new_text.replace('  ', ' ').replace(';','')

    
