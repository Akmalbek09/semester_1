from words import *
def letters(txt,a):
    listletters = []
    for x in txt:
        if x in a:
            listletters.append(x)
    return len(listletters)
def space_remover(txt,s):
    txtt = ""
    counter = 0
    for x in txt:
        if x == " ":
            if txtt[counter-1] == " " or txtt[counter-1] in s:
                continue
            else:
                pass
        txtt = txtt + x
        counter += 1
    return txtt
symbols = [",", ".", "_", "-", "+", "*", "/", "@", "#", "$", "%", "&", "="]
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(word)
txt = input(":").lower()
txt = txt.strip()
txt = space_remover(txt,symbols)
print(f"quantity of letter: {letters(txt,letter)}")
print(txt)
wtxt = ""
alwords = []
counter = 0
for x in txt:
    wtxt = wtxt + x
    if wtxt in word:
        alwords.append(wtxt[counter:])
        wtxt = ""
    counter += 1
print(alwords)