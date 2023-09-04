##############################################################################
##
## CS 101
## Program #3
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Give a user-input Dothraki word(s), print the phonetic pronunciation
##
## ALGORITHM: 
##      1.Get and validate user input, then call transliterate function and print
##        return
##          1.Retrieve user input
##          2.While user input is in forbid_char, ask for user input
##          3.Call transliterate function on user input
##              1.For i in user input and j in length of user input
##                  1.If user input[j:j+2] in diphthongs in dothraki dictionary,
##                    add j:j+2 in diphthongs in dothraki dictionary to word
##                  2.Else, if user input[j-1:j+1] not in diphthongs in dothraki
##                    dictionary, add i in dothraki dictionary to word
##              2.If last character of word is h, replace character with ħ
##              3.Return word
##      2.Ask for and then validate user input, then determine if loop program
##        or terminate program
##          1.Retrieve user input
##          2.While user input is not Y, YES, N, or NO
##              1.Inform user that user input is too small
##              2.Ask for user input
##          3.If user input is Y or YES, return to beginning
##          4.Else, terminate program
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
##############################################################################

def transliterate(user_input):
    '''Returns the phonetic pronunciation of user input'''

    word = ['']
    for i, j in zip(user_input, range(len(user_input))):
        if user_input[j:j+2] in doth_dict['diphthongs']:
            word[0]+=doth_dict['diphthongs'][user_input[j:j+2]]
        else:
            if user_input[j-1:j+1] not in doth_dict['diphthongs']:
                word[0]+=doth_dict[i]
    word = word[0]
    if word[-1] == 'h':
        word=word.replace(word[-1],doth_dict['special'])
        
    return word

doth_dict = {
    'diphthongs':{
        'qa':'qɑ',
        'qi':'qe',
        'qe':'qɛ',
        'qo':'qɔ',
        'sh':'ʃ',
        'ch':'t͡ʃ',
        'th':'θ',
        'kh':'x',
        'zh':'ʒ'
        },
    'special':'ħ',
    'a':'a',
    'd':'d̪',
    'e':'e',
    'f':'f',
    'g':'g',
    'h':'h',
    'i':'i',
    'j':'d͡ʒ',
    'k':'k',
    'l':'l̪',
    'm':'m',
    'n':'n̪',
    'o':'o',
    'q':'q',
    'r':'ɾ, r',
    's':'s',
    't':'t̪',
    'v':'v',
    'w':'w',
    'y':'j',
    'z':'z',
    }

forbid_char = ['b','c','p','u']
play_again = [('Y', 'YES'), ('N', 'NO')]
play = True

while play == True:
    #Get and validate that user input is valid, then call transliterate function and print return
    user_word = input('Enter a word to get the Dothroki pronunciation ==>').lower()
    print(user_word)

    while forbid_char[0] in user_word or forbid_char[1] in user_word or forbid_char[2] in user_word or forbid_char[3] in user_word:
        print('Word must not contain the characters {}'.format(','.join(forbid_char)))
        user_word = input('Enter a word to get the Dothroki pronunciation ==>').lower()

    print('{} is pronounced {}'.format(user_word, transliterate(user_word)))
    
    #Ask for and then validate user input, then determine if loop program or terminate program
    play = input('\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
    while not (play in play_again[0] or play in play_again[1]):
        print('You must enter Y YES N or NO')
        play = input('\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
    if play in play_again[0]:
        play = True
    else:
        play = False
