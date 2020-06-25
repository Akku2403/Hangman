import random

print('H A N G M A N\n')

def play():
    word_list = ['python', 'kotlin', 'java', 'javascript', 'swift']
    picked_word = random.choice(word_list)
    hidden_word = "-" * (len(picked_word))
    print(hidden_word)

    attempt_set = set()
    attempts = 0

    while attempts < 8:
        letter = input('Input a letter: ')

        if len(letter) != 1:
            print('You should input a single letter')
            print('\n' + hidden_word)
            continue

        if not (ord(letter) >= 97 and ord(letter) <= 122):
            print("It is not an ASCII lowercase letter")
            print('\n' + hidden_word)
            continue

        if letter in picked_word and letter not in attempt_set:
            attempt_set.add(letter)
            for i in range(len(picked_word)):
                hidden_word_list = list(hidden_word)
                if letter == picked_word[i]:
                    hidden_word_list[i] = letter
                    hidden_word = "".join(hidden_word_list)

        elif letter in attempt_set:
            print('You already typed this letter')

        else:
            attempt_set.add(letter)
            print('No such letter in the word')
            attempts += 1

        if attempts == 8:
            break

        print('\n' + hidden_word)

        if hidden_word == picked_word:
            print('You guessed the word!')
            print('You survived!')
            exit(0)

    print('You are hanged!')

while(True):
    user_input = input('Type "play" to play the game, "exit" to quit:')
    if user_input == 'play':
        play()
    elif user_input == 'exit':
        exit()
