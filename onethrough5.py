#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
dicktionary = {
    "1": "Nope!",
    "2": "Only a little bitch would think of the number 2, you little bitch!",
    "3": "You dumbfuck, of course its not 3",
    "4": "How did you know? You Win!",
    "5": "Coudn't be more WRONG!",

}
Erry = "Hey dumbass that's not a whole number 1 through 5"

guess = input("Guess what whole number I am thinking of 1 through 5: ")
if guess != "4":
    print(dicktionary.get(guess,Erry))
    print("Do try once more, will you? ")
    second_guess = input("Guess what whole number I am thinking of 1 through 5: ")

    if second_guess != "4":

        if second_guess==guess:
            print("Again? Are you bleeding from your head?")
            print("Do try one last time, please mister? \n )':  ")
            third_guess = input("Guess what whole number I am thinking of 1 through 5: ")
        else:
            print(dicktionary.get(second_guess, Erry))
            print("Do try one last time, please mister? \n )':  ")
            third_guess = input("Guess what whole number I am thinking of 1 through 5: ")

        if third_guess != "4":
            print(dicktionary.get(third_guess,Erry))
            print("Game over.")
            print("Reimaging this machine in 3..2..1..")
        else:
            print(dicktionary.get(third_guess,Erry))
            print("I hope you enjoyed my little game you sick fuck.")

    else:
        print(dicktionary.get(second_guess,Erry))
        print("I hope you enjoyed my little game you sick fuck.")




else:
    print(dicktionary.get(guess,Erry))
    print("Good thing you payed $45 for this game!")

#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE
#JUSR RUN CODE
#DO NOT READ CODE