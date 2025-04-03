def get_word_count(str):
    return len(str.split())

def get_sorted_word_count(words_count):
    sorted_tup = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    for tup in sorted_tup:
        if tup[0].isalpha():
            print(f"{tup[0]}: {tup[1]}")
def get_words_count(str):
    word_count_dic = dict()
    for word in str:
        word_count_dic[word.lower()] = word_count_dic.get(word.lower(), 0) + 1
    return word_count_dic
