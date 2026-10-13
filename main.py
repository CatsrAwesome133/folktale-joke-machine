from random import randint

#jokes & punchlines as list
jokes = [
    "What is pink and fluffy?",
    "What's brown and sticky?",
    "What's black and white and red all over?",
    "What has legs but doesn't walk?",
    "What's the best way to save your dad jokes?",
    "What do you call fake spaghetti?",
    "Why can't dinosaurs clap their hands?",
    "What do you call cheese that isn't yours?",
    "How do you organize a space party?",
    "What do you call a cold puppy?",
    "What do you call a bear with no teeth?",
    "Why did the golfer bring two pairs of pants?",
    "What's a witch's favorite subject in school?",
    "How does a penguin build its house?",
    "What do you call an elephant that doesn't matter?",
    "What did the beach say when the tide came in?",
    "Why can't you give Elsa a balloon?",
    "What do you get if you cross a snowman and a vampire?",
    "Why can't leopards play hide-and-seek?",
    "What's blue and doesn't weigh very much?",
    "Did you know that dogs can't operate the MRI machine? On the other hand, though...",
    "Why shouldn't you trust atoms?"
    ]
punchlines_in = [
    "pink fluff", #called for verifying input
    "a stick",
    "a newspaper",
    "a table",
    "in the dadda-base",
    "an impasta",
    "they're extinct",
    "nacho cheese",
    "you planet",
    "a chili dog",
    "a gummy bear",
    "hole in one",
    "spelling",
    "igloos it together",
    "irrelephant",
    "long time no sea",
    "let it go",
    "frostbite",
    "because they're always spotted",
    "light blue",
    "catscan",
    "they make up everything"
    ]
punchlines_out = [
    "Pink fluff!", #called & sent as text
    "A stick!",
    "A newspaper!",
    "A table!",
    "In the dadda-base! ;3",
    "An impasta!",
    "Because they're extinct!",
    "Nacho cheese!",
    "You planet!",
    "A chili dog!",
    "A gummy bear!",
    "In case he got a hole in one!",
    "Spelling!",
    "Igloos it together!",
    "An irrelephant!",
    "Long time no sea!",
    "Because she will let it go!",
    "Frostbite!",
    "Because they're always spotted!",
    "Light blue, of course!",
    "CATScan!",
    "Because they make up everything!"
    ]

#variables
guess = ""
last_random = 0 #to avoid repeats
random_number = 0
next_random = 0 #to avoid repeats
game_on = True
points = 0
rounds = 0

#introduction
print('Welcome to "Guess the Punchline" game! \n'
      'You will "hear" a joke and try to guess the punchline. \n'
      'Type your answer and press Enter. Type "quit" to exit the game.\n'
      'Fair warning, this is hyperspecific like most puns are :)\n')

# gamemode system
# no pycharm I did NOT misspell that
gm = input("Do you want to guess until you say stop? (Y/N): ").lower()

# checks if infinite is on, if not asks for rounds
if gm == 'n':
    # gives the second option
    gm = input("Alright then. Do you want to set a number of rounds? (Y/N): ").lower()
    # if rounds is set, it asks for a round number until the number is a number
    if gm == 'y':
        gm = 'set'
        valid_rounds = False
        while not valid_rounds:
            try:
                rounds = int(input("Please enter the number of rounds you want: "))
                valid_rounds = True
            except ValueError:
                print("...That's not a number. Try again?")
    # if rounds isn't set... well, we don't have other options ;-;
    else:
        rounds = 10
        gm = 'set'
        print("Uh, we don't have more gamemodes... \nLet's play for 10 rounds!")
else:
    gm = 'repeat'


if gm == 'repeat':
    while game_on: #keeps the below looping until game_on is set to false
        #takes random numbers until the new random number is different from the prev
        #this is to avoid repeats
        while next_random == random_number or next_random == last_random:
            next_random = randint(0,len(jokes)-1)
        last_random = random_number
        random_number = next_random

        #adds a round
        rounds += 1
        print(f"Round {rounds}!")
        #uses random number to select a joke
        print(jokes[random_number])
        guess = input("").lower()
        guess = guess.strip()

        #maps each joke to a punchline which is why random_number had to be a thing
        if guess == punchlines_in[random_number]:
            print("Wow! You got it!\n")
            points += 10
        else:
            print(punchlines_out[random_number])

        #checkpoints!
        if (points/10)%5 == 0.0 and (points/10) != 0.0: #every 5th round
            print(f"{int(points/10)} punchlines guessed correctly! Keep going, you're doing great!")

        guess = input('Press [Enter] to continue or type "quit" to quit\n').lower()

        #this ends the while loop if the user said "quit"
        if guess == "quit":
            game_on = False
            print("\nAlright, bye!")
            print(f"You got {points} points this round!")

            #points stuff
            if points/rounds > 0.5: #if >50% of the questions are right
                print("Hey, you got most of the jokes right! Great job!")
            elif points/rounds <= 0.5: #if <=50% of the questions are right
                print("Good job! You got some of the jokes right! Keep practicing!")
elif gm == 'set':
    for i in range(rounds):
        # makes sure no repeats for 2 questions
        while next_random == random_number or next_random == last_random:
            next_random = randint(0, len(jokes) - 1)
        last_random = random_number
        random_number = next_random

        # adds a round
        rounds += 1
        print(f"Round {rounds}!")
        # uses random number to select a joke
        print(jokes[random_number])
        guess = input("").lower()
        guess = guess.strip()

        # maps each joke to a punchline which is why random_number had to be a thing
        # look in hindsight I could have used a dictionary or something but shhhhhh
        if guess == punchlines_in[random_number]:
            print("Wow! You got it!\n")
            points += 10
        else:
            print(punchlines_out[random_number])
        
        # mostly for consistency reasons... forwards the game on any user input
        input('Press [Enter] to continue\n')

    print(f"\n{rounds} rounds over! Let's see how you did...")
    print(f"You got {points} points this round!")

    # points stuff
    if points / rounds > 0.5:  # if >50% of the questions are right
        print("Hey, you got most of the jokes right! Great job!")
    elif points / rounds <= 0.5:  # if <=50% of the questions are right
        print("Good job! You got some of the jokes right! Keep practicing!")
