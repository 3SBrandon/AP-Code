import random
print('\n')
songs = [
    'SONG 0',
    'SONG 1',
    'SONG 2',
    'SONG 3',
]

lyrics = [
    'lyric 0 uju',
    'lyric 1',
    'lyric 2',
    'lyric 3',
]

artists = [
    'artist 0',
    'artist 1',
    'artist 2',
    'artist 3',
]


def UI():
    opt = input('What game would you like to play. 1)Finish the lyric 2)Guess the song or 3)Guess the artist: ')
    rounds = input('How many rounds would you like to play: ')
    print('\n')
    if opt == '1':
        score = 0
        for i in range(int(rounds)):
            score = score + finishLyric()
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    elif opt == '2':
        score = 0
        for i in range(int(rounds)):
            score = score + guessSong()
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    elif opt == '3':
        score = 0
        for i in range(int(rounds)):
            score = score + guessArtist()
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    
def again():
    quben = input('Do you want to play another game? Yes or No: ').upper()
    if quben == 'YES':
        UI()
    elif quben == 'NO':
        print('Thanks for playing!!!')
        exit

def guessSong():
    r = random.randint(0,len(songs)-1)
    print(lyrics[r])
    question = input('What song is this from (Type "HINT" to get one): ')
    if question == 'HINT':
        question = input(f'HINT - This lyric is by "{artists[r]}".\nWhat song is this lyric from: ' )
    if question.upper() == songs[r].upper():
        print('Correct')
        point = 1
    else: 
        print('Incorect')
        point = 0
    return point

def finishLyric():
    r = random.randint(0,len(songs)-1)
    full = lyrics[r]

    print(full)

    words = lyrics[r].split()
    missing = random.randint(0,len(words)-1)
    answer = words[missing].upper()
    words[missing] = '_'*len(words[missing])
    print(' '.join(words))

    question = input('what is the missing word in the lyric (Type "HINT" to get one): ')
    if question == 'HINT':
        question = input(f'HINT - This lyric is from the song "{songs[r]}".\nWhat is the missing word in the lyric: ')
    if question.upper() == answer:
        print('Correct')
        point = 1
    else:
        print('Incorrect')
        point = 0
    return point

def guessArtist():
    r = random.randint(0,len(artists)-1)
    answer = artists[r]
    print(songs[r])
    question = input(f'Who is this song by (Type "HINT" to get one): ')
    if question == 'HINT':
        question = input(f'A lyric from the song is "{lyrics[r]}". Who made this song: ')
    if question.upper() == answer.upper():
        print('Correct')
        point = 1
    else:
        print('Incorect')
        point = 0
    return point
    


UI()




