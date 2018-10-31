import re
def openlog(file):
    chat=[]
    with open( file, "r",encoding='utf-8') as f:   
        for line in f:
            chat.append(line.strip())
    return chat

def modus():
    print ("we can ignore very small words in the analyses. Minimum length 4 would ignore \"meh\" \nAlso words being used \
only once can be typo's or addresslines. Not interesting.\n") 
    MINWORDLENGTH=input("What is your minimum word length to check? : ")
    MINWORDFREQUENCY=input("How often do words need to be used to check? : ")
    return MINWORDLENGTH,MINWORDFREQUENCY

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

chat=openlog("chat.txt")
MINWORDLENGTH, MINWORDFREQUENCY = modus()

all_words_unique=[unique_words(checklines(usernames(chat)[0]))[0],unique_words(checklines(usernames(chat)[1]))[0]]
p1dict=unique_words(checklines(usernames(chat)[0]))[1]
p2dict=unique_words(checklines(usernames(chat)[1]))[1]
pdict=[p1dict,p2dict]

for y in [0,1]:
    all_words_unique[y]=[item for item in all_words_unique[y] if len(item[0])>=int(MINWORDLENGTH)]
    all_words_unique[y]=[item for item in all_words_unique[y] if item[1]>=int(MINWORDFREQUENCY)]

def summary():  
    for x in [0,1]:
        print (f"{usernames(chat)[x]} used {str(len(all_words_unique[x]))} different words. \
Total typed {str(len(checklines(usernames(chat)[x])))} words\n")

def print_top25(username,words,p1dict,p2dict):
    print ("-"*30)
    print ("Top 25 own words from " + username)
    ii=0
    for i in words:
       if i[0] not in p1dict.keys():
            print (i[0] + " ("+str(p2dict[i[0]])+")")
            ii+=1
            if ii>24:
                break

summary()
for x in [(usernames(chat)[1],all_words_unique[1],p1dict,p2dict),(usernames(chat)[0],all_words_unique[0],p2dict,p1dict)]:
    print_top25(x[0],x[1],x[2],x[3])

    


