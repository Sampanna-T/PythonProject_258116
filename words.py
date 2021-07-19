def get_wordlist():
    words_temp = []
    words = []
    try:
        file = open("wordFile.txt","r")
    except:
        print("ERROR OPENING FILE")

    for line in file:
        words_temp += line.split(",")

    for word in words_temp:
        word_trim = word.strip()
        
        if word_trim.isalpha() == True:
            words.append(word_trim)

    return words


