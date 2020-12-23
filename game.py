import random

rating = open('rating.txt', 'r', encoding='utf-8')  # opens the file with ratings
shapes = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf",
          "tree", "human", "snake", "scissors", "fire"]  # list of files to choose from
user_name = ''
user_score = 0
input_name = input("Enter your name: ")
print(f'Hello, {input_name}')
chosen_shapes = []
input_shapes = input().split(",")  # list of shapes chosen by the player
if len(input_shapes) == 1:  # there's no shapes in player's input, plays the default options
    chosen_shapes.append("rock")
    chosen_shapes.append("paper")
    chosen_shapes.append("scissors")
else:
    chosen_shapes = input_shapes
print("Okay, let's start")
for line in rating:
    if line.split(" ")[0] == input_name:  # checks if the player's name is in the rating file
        user_score += int(line.split(" ")[1])
        user_name = line.split(" ")[0]
        break
if not user_name:
    user_name = input_name
while True:  # main part of the game
    user_shape = input("Input a shape:")
    computer_shape = random.choice(chosen_shapes)
    if user_shape in chosen_shapes:
        if user_shape == computer_shape:
            print("There is a draw ({})".format(user_shape))
            user_score += 50
        elif 0 < abs(shapes.index(computer_shape) - shapes.index(user_shape)) <= 7:
            if shapes.index(computer_shape) > shapes.index(user_shape):
                print("Sorry, but the computer chose {}".format(computer_shape))
            else:
                print("Well done. The computer chose {} and failed".format(computer_shape))
                user_score += 100
        elif 7 < abs(shapes.index(computer_shape) - shapes.index(user_shape)) <= 14:
            if shapes.index(computer_shape) < shapes.index(user_shape):
                print("Sorry, but the computer chose {}".format(computer_shape))
            else:
                print("Well done. The computer chose {} and failed".format(computer_shape))
                user_score += 100
    elif user_shape == "!exit":  # exits the game
        print("Bye!")
        break
    elif user_shape == "!rating":  # checks the player's rating
        print(f'Your rating: {user_score}')
    else:
        print("Invalid input")
rating.close()
