# Write a Python program to count repeated characters in a string . Sample string: 'thequickbrownfoxjumpsoverthelazydog’


def repeated_characters(string):
    lista = set()
    for i in range(len(string)):
        count =0
        for j in string:
            if string[i] == j:
                count += 1
        if count > 1:
            # print(f"{string[i]}        {count}")
            sub_list = [string[i],  [count]]
            lista.add(sub_list)
            print(list(lista))
string = "thequickbrownfoxjumpsoverthelazydog"
repeated_characters(string)