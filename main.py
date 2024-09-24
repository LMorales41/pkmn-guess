from src.calls import *

dexNumber = get_dex_number()
nameColorGenArray = get_pokemon_info(dexNumber)

selectedGuess = Pokemon(pokemon_constructor(nameColorGenArray[0], nameColorGenArray[1], nameColorGenArray[2]))
print(selectedGuess)

guesses = 0
print(selectedGuess.answer)
while guesses < 3: 
    selectedGuess.show_info(guesses)
    guess = input()
    if guess == selectedGuess.answer:
        print("Correct!")
        break
    else:
        print("Incorrect!")
        guesses += 1

if guesses > 2:
    print("Womp womp")
else:
    print("Yipee!")


