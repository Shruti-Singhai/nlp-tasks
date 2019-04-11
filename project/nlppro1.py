text= input()
sent = text.split('.')

def number_sent(text):
    sent = text.split('.')
    l = 0
    for i in sent:
        l = l+1
    return l
number_sent(text)

#Calculating average sentance length
def avg_sent_len(text):
    sents = text.split('.')
    k = sum(len(x.split()) for x in sents) / len(sents)
    return k
avg_sent_len(text)

def max_sent_len(sent):
    k = 0
    max = 0
    for i in sent:
        k = len(i.split())
        if k > max:
            max = k
    return max
max_sent_len(sent)

#Counting number of syllables in a word
import nltk
from nltk.corpus import cmudict 
d = cmudict.dict() 
def syll_count(word): 
    count = 0
    vowels = "aeiouy"
    if text[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count

#average syllable count of text per sentence
def avg_syll_count(text):
    sent = text.split(".")
    k = 0
    for i in sent:
        for j in i.split(" "):
            k = k+syll_count(j)
    return k/len(text.split('.'))
avg_syll_count(text)

#average word length
def avl(text):
    k = 0
    l = 0
    for i in text.split("."):
        for j in i.split(" "):
            k = k + len(j)
            l = l + 1
    return k/l
avl(text)

def mvl(text):
    k = 0
    l = 0
    for i in text.split("."):
        for j in i.split(" "):
            k = len(j)
            if k>l:
                l = k
    return l
mvl(text)

# 2 syll
def msl(word):
    if syll_count(word)>1:
        return True
    else:
        return False

# 2+ syll
def m2l(word):
    if syll_count(word)>2:
        return True
    else:
        return False

#%age of multisyllable words per sentence
def  per_msl(text):
    mn = 0  
    kl = 0
    for i in text.split("."):
        for j in i.split(" "):
            if(msl(j)==True):
                mn = mn +1
        kl = kl+1
    return mn/kl
per_msl(text)

def flesch_score(text):
    ts = number_sent(text)
    t1 = text.replace("."," ")
    bl = t1.split(" ")
    tw = 0
    tsy = 0
    for i in bl:
        tw = tw + 1
        tsy = tsy + syll_count(i)
    score = (206.835 - 1.015*(tw/ts) - 84.6*(tsy/tw))
    return score

def Gunning_fog(text):
    df = 0
    w = 0
    t = (text.replace("."," ")).split(" ")
    for i in t:
        if(m2l(i)==True):
            df = df+1
        w = w+1
    al = avg_sent_len(text)
    GFS = al + (df/w)
    return 0.4*GFS
Gunning_fog(text)

def r_score(text):
    gf = Gunning_fog(text)/17
    fs = 1-(flesch_score(text)/100)
    wl = avl(text)/mvl(text)
    sl = avg_sent_len(text)/max_sent_len(text.split("."))
    score = (sl + wl + fs + gf)*25
    print(score)
    if wl>=0.6:
        print("Try using shorter words")
    if sl>=0.6:
        print("Try breaking your sentences into parts and avoid using unnescesarry conjunctions.")
    if gf>0.7:
        print("Try using words with less syllables")
    return score

def comment(score):
    if(score>70):
        print("Very Difficult to understand.")
    elif(score>60 and score<70):
        print("Difficult to understand.")
    elif(score>50 and score<60):
        print("Fairly Difficult to understand.")
    elif(score>40 and score<50):
        print("Modern consumer's english")
    elif(score>30 and score<40):
        print("Plain english for teenagers.")
    elif(score>20 and score<30):
        print("Easily understood by Middle school students")
    elif(score>0 and score<20):
        print("Very easy to read. Easily understood by an average 11-year-old student.")

print(comment(r_score(text)))
