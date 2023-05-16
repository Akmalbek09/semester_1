from words import word
def word_sorter(word):
    my_list = []
    word = list(word)
    counter = 0
    b = 0
    z = ""
    for x in word:
        z = z + x
        if x == '#':
            my_list.append(z[1:len(z)-2])
            b = counter+2
            z = ""
        counter +=1
    return my_list
def letters(txt,a):
    listletters = []
    for x in txt:
        if x in a:
            listletters.append(x)
    return len(listletters)
def space_remover(txt):
    txtt = ""
    counter = 0
    for x in txt:
        counter += 1
        if counter == len(txt):
            txtt = txtt + x
            break
        elif x == " " and txt[counter] == " ":
            continue
        elif x == " " and txt[counter] == ".":
            continue
        else:
            txtt = txtt + x
    return txtt
def word_splitter(txt):
    counter = 0
    b = 0
    wordd = []
    for x in txt:
        counter += 1
        if x == " " or x == ".":
            wordd.append(txt[b:counter-1])
            b = counter
    wordd.append(txt[b:])
    return wordd
symbols = [",", ".", "_", "-", "+", "*", "/", "@", "#", "$", "%", "&", "="]
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = word_sorter(word)
txt = input(":").lower()
# txt = txt.strip()
txt = space_remover(txt)
print(f"quantity of letter: {letters(txt,letter)}")
print(txt)
word_splitter(txt)