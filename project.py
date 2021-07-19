import words
import time
import random
import sys

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def display_word(delay):
    global word_list
    global selected_list

    random_no = random.randint(0,len(word_list))
    selected_word = word_list[random_no]
    print(selected_word.upper())
    time.sleep(delay)

    selected_list.append(selected_word.upper())
    delete_last_line()

def count_down(delay,count):
    for i in range(count):
        print(i+1)
        time.sleep(delay)


word_list = words.get_wordlist()
selected_list = []

print("""The game is described as follows ->
1) You have to memorize the word being displayed
2) At each level you have to memorize 1 word  more than the previous level
3) The word will be displayed only for 3 seconds
""")

print("PRESS 'YES' TO START THE GAME")
while input().strip().upper() != "YES":
    print("PRESS 'YES' TO START THE GAME")

level = 1
flag = False

while True:
    print("Start memorizing ",level," element/s in",end='\n')
    count_down(1,3)


    for i in range(level):
        print("->",end=" ")
        display_word(3)

    for index in range(level):
        
        if input().strip().upper() == selected_list[index]:
            if index == level-1:
                print("CONGRATULATIONS ON PASSING LEVEL ",level)
                level += 1
                print("READY FOR LEVEL ",level,"?(yes/no)")
                if input().strip().upper() != "YES":
                    flag = True
                    break
            continue
        else:
            print("LEVEL ",level ,"FAILED, ANSWER IS ",selected_list)
            flag = True
            break
    selected_list.clear()
    if flag == True:
        break

    