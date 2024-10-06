import random


def select_category():
    option = ['sports', 'movie', 'series', 'videogames']
    full_options = [['football', 'Cricket', 'Basketball', 'tennis', 'golf'],
                    ['inception', 'goodfellas', 'intersteller', 'gladiator', 'momento'],
                    ['chernobyl', 'succession', 'dark', 'narcos', 'peacemaker'],
                    ['sekiro', 'bloodborne', 'doom', 'minecraft', 'undertale']]
    number = 1
    print("Categories")
    for i in option:
        print(f"{number}. {i.title()}")
        number += 1
    while True:
        try:
            answer = int(input("Please provide a number to select category: "))
            return full_options[answer - 1]
            break
        except Exception as e:
            print("Please provide an appopriate number.")


def blank_words(optionlist):
    option = optionlist
    word = random.choice(option)
    # print(f'word: {word}')
    lengthofword = len(word)
    # print(f'length: {lengthofword}')
    numberofexposedletters = random.randint(1, round(lengthofword / 2))
    # print(f'number of exposed letters: {numberofexposedletters}')
    exposedletter = random.sample(word, k=numberofexposedletters)
    # print(f'letters: {exposedletter}')
    # print(type(numberofexposedletters))
    blankcanvas = (lengthofword) * '_'
    # print(blankcanvas)
    # print(word.index(exposedletter[0]))
    listedcanvas = list(blankcanvas)
    # print(listedcanvas)
    for i in exposedletter:
        # print(f' Word is: {i} index is:{word.index(i)}')
        listedcanvas[word.index(i)] = i
        # print(listedcanvas)
    # print(listedcanvas)
    finalform = ' '.join(listedcanvas)
    return word, finalform, listedcanvas


def final_game(data):
    word, displayedpart, displayedpartinlist = data
    # print(word)
    # print(displayedpart)
    # print(displayedpartinlist)
    chances = 5
    wrongdecision = 0
    indexlist = list()
    print(displayedpart)
    while wrongdecision < chances:
        guess = input("Guess a letter: ")
        if guess in word and word.index(guess) not in indexlist:
            for i in range(len(word)):
                if guess == word[i]:
                    indexlist.append(i)
                    displayedpartinlist[i] = word[i]
            print(" ".join(displayedpartinlist))
            if "".join(displayedpartinlist) == word:
                print("You've guessed the correct word")
                break
        else:
            print(f"The letter {guess} isn't on the word.")
            print(" ".join(displayedpartinlist))
            wrongdecision += 1
    else:
        print("You've ran out of chances")


final_game(blank_words(select_category()))
# print(select_category())
