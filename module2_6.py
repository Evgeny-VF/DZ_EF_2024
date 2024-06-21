#Домашняя работа по уроку "Способы вызова функции"

def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (word.lower()).find(root_word.lower()) != -1 or (root_word.lower()).find(word.lower()) != -1:
            same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))