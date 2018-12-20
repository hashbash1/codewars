def spin_words(sentence):
    store = sentence.split(" ")
    out = []
    for i in store:
        if len(i) > 4:
            i = i[::-1]
        out.append(i)
    return ' '.join(out)