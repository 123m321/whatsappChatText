import re
def openlog(file):
    f = open( file, "r",encoding='utf-8')
    chat=[]
    for line in f:
        chat.append(line.strip())
    return chat

def modus():
    print ("we can ignore very small words in the analyses. Minimum length 4 would ignore \"meh\" \nAlso words being used \
only once can be typo's or addresslines. Not interesting.\n") 
    MINWORDLENGTH=input("What is your minimum word length to check? : ")
    MINWORDFREQUENCY=input("How often do words need to be used to check? : ")
    return (MINWORDLENGTH,MINWORDFREQUENCY)

def usernames(chat):
    p1_all_words=p2_all_words="0"
    for line in range(100):
        zoek = re.compile(r"\ (.+])(\s)(.+:)")
        mo=zoek.search(chat[line])
        if p1_all_words=="0":
            p1_all_words=mo.group(3)
        elif p1_all_words!=mo.group(3):
            p2_all_words=mo.group(3)
    return (p1_all_words,p2_all_words)


def checklines(person):
    text=[]
    woord=[]
    woordclean=[]
    for item in chat:
        zoek = re.compile(r"\ ("+ person +")(.+)")
        mo=zoek.search(item)
        if mo:
            text.append(mo.group(2).split())

    for item in text:
        for wrd in item:
            woord.append(wrd)    

    for item in woord:    
        zoek = re.compile(r"([a-zA-Z]+)")
        mol=zoek.search(item)
        if mol:
            woordclean.append(mol.group(1))
    woordclean=[item for item in woordclean if len(item)>1]
    return woordclean

def unique_words(words):
    word_dict={}
    unique=[]
    for i in words:
        if i.lower() in word_dict:
            word_dict[i.lower()]+=1
        else:
            word_dict[i.lower()]=1

    for x in word_dict.items():
        unique.append(x,)
    unique.sort(key=lambda x: x[1], reverse=True)
    return unique, word_dict

def voc(naam):
    voca=[]
    for i in naam:
        voca.append(i[0])
    return voca

chat=openlog("chat.txt")
answers=modus()
MINWORDLENGTH=answers[0]
MINWORDFREQUENCY=answers[1]

p1_username=usernames(chat)[0]
p1_all_words=checklines(p1_username)
p1_all_words_unique=unique_words(p1_all_words)[0]
p1dict=unique_words(p1_all_words)[1]
vocabulary_p1=voc(p1_all_words_unique)
vocabulary_p1=[item for item in vocabulary_p1 if len(item)>=int(MINWORDLENGTH)]

p2_username=usernames(chat)[1]
p2_all_words=checklines(p2_username)
p2_all_words_unique=unique_words(p2_all_words)[0]
p2dict=unique_words(p2_all_words)[1]
vocabulary_p2=voc(p2_all_words_unique)
vocabulary_p2=[item for item in vocabulary_p2 if len(item)>=int(MINWORDLENGTH)]


for p in [p2_all_words_unique,p1_all_words_unique]:
    p=[item for item in p if item[1]>=int(MINWORDFREQUENCY)]
    p=[item for item in p if len(item[0])>=int(MINWORDLENGTH)]

   
print (p2_username + " used " + str(len(vocabulary_p2)) + " different words. Total typed " +str(len(p2_all_words)) + " words\n")
print (p1_username + " used " + str(len(vocabulary_p1)) + " different words. Total typed " +str(len(p1_all_words)) + " words")

print ("-"*30)
print ("Top 25 own words from " + p2_username)
ii=0
for i in range(len(vocabulary_p2)):
   if vocabulary_p2[i] not in vocabulary_p1:
        print (vocabulary_p2[i] + " ("+str(p2dict[vocabulary_p2[i]])+")")
        ii+=1
        if ii>24:
            break

print ("Top 25 own words from " + p1_username)
ii=0
for i in range(len(vocabulary_p1)):
   if vocabulary_p1[i] not in vocabulary_p2:
        print (vocabulary_p1[i] + " ("+str(p1dict[vocabulary_p1[i]])+")")
        ii+=1
        if ii>24:
            break


