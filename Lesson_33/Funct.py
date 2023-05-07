def menu(c):
    my_list = []
    counter = 0
    p = 0
    while counter < c:
        counter += 1
        quest = input("Enter the question: ")
        p += 1
        my_list.append(f"Press {p} to {quest}")
    return my_list