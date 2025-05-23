import random
print('\n')
songs = [
    "Luther",
    "Die With A Smile",
    "Nokia",
    "Pink Pony Club",
    "Ordinary",
    "A Bar Song",
    "Lose Control",
    "All The Way",
    "Beautiful Things",
    "I'm The Problem",
]

lyrics = [
    "If this world was mine I'd take your dreams and make 'em multiply",
    "I'd wanna hold you just for a while and die with a smile If the world was ending I'd wanna be next to you",
    "Who's callin' my phone Is it Stacy Is it Becky Is it Keisha Is it Ellie Was it Dani Is it PARTY Where's the function",
    "God what have you done You're a pink pony girl And you dance at the club Oh mama I'm just having fun",
    "On the edge of your knife stayin' drunk on your vine. The angels up in the clouds are jealous knowin' we found",
    "Someone pour me up a double shot of whiskey They know me and Jack Daniel's got a history There's a party downtown near 5th Street",
    "I lose control When you're not next to me I'm fallin' apart right in front of you can't you see",
    "Don't ask for all your things back cussin' out my name yeah Just to go and take back what you say Burn all the bridges, don't ask forgiveness",
    "I want you I need you oh God Don't take These beautiful things that I've got Please stay",
    "You say I'll never change I'm just a go around town with some gasoline Just tryin' to bum a flame Gonna burn the whole place down",
]

artists = [
    "Kendrick Lamar",
    "Lady Gaga",
    "Drake",
    "Chappell Roan",
    "Alex Warren",
    "Shaboozey",
    "Teddy Swims",
    "BigXthaPlug",
    "Benson Boone",
    "Morgan Wallen",
]

def again():
    quben = input('Do you want to play another game? Yes or No: ').upper()
    if quben == 'YES':
        UI()
    elif quben == 'NO':
        print('Thanks for playing!!!')
        exit
    else:
        print('INPUT ERROR')
        again()

def finishLyric(score):
    r = random.randint(0,len(songs)-1)
    full = lyrics[r]

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
        score = score + 1
    else:
        print('Incorrect')
    return score

def guessSong(score):
    r = random.randint(0,len(songs)-1)
    print(lyrics[r])
    question = input('What song is this from (Type "HINT" to get one): ')
    if question == 'HINT':
        question = input(f'HINT - This lyric is by "{artists[r]}".\nWhat song is this lyric from: ' )
    if question.upper() == songs[r].upper():
        print('Correct')
        score = score + 1
    else: 
        print('Incorect')
    return score

def guessArtist(score):
    r = random.randint(0,len(artists)-1)
    answer = artists[r]
    print(songs[r])
    question = input(f'Who is this song by (Type "HINT" to get one): ')
    if question == 'HINT':
        question = input(f'HINT - A lyric from the song is "{lyrics[r]}". Who made this song: ')
    if question.upper() == answer.upper():
        print('Correct')
        score = score + 1
    else:
        print('Incorect')
    return score
    
def UI():
    opt = input('What game would you like to play. 1)Finish the lyric 2)Guess the song or 3)Guess the artist: ')
    try:
        opt = int(opt)
    except ValueError:
        print('INPUT ERROR')
        UI()

    rounds = input('How many rounds would you like to play: ')
    try:
        rounds = int(rounds)
    except ValueError:
        print('INPUT ERROR')
        UI()

    print('\n')
    if opt == 1:
        score = 0
        for i in range(int(rounds)):
            score = finishLyric(score)
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    elif opt == 2:
        score = 0
        for i in range(int(rounds)):
            score = guessSong(score)
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    elif opt == 3:
        score = 0
        for i in range(int(rounds)):
            score = guessArtist(score)
            print(f'Score: {score}')
            print('\n')
        print(f'Your final score is: {score}')
        again()
    else: 
        print('ERROR')
        UI()
        
UI()




