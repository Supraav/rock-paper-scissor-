import random

def play():
    d = 0
    w = 0
    l = 0
    ended = False
    name = input("enter name: ")
    print("hello " + name + " ,welcome to the game")

    while True:
        user_choice = input(
            name + ",choose (r) for rock, (p) for paper, (s) for scissor and (q) to quit:"
        )
        print("you choose: " + user_choice)
        while user_choice not in ["p", "q", "r", "s"]:
            print("enter correct keyword")
            user_choice = input(name + ",choose (r) for rock, (p) for paper, (s) for scissor and (q) to quit:")
            print("you choose: " + user_choice)
        if user_choice == "q":
            break
        else:
            comp_choice = random.choice(["p", "r", "s"])
            if comp_choice == "r":
                move = "rock"
            elif comp_choice == "p":
                move = "paper"
            else:
                move = "scissor"
            print("computer choose: " + move)
            if user_choice == comp_choice:
                print("draw")
                d += 1
            elif (
                (comp_choice == "r" and user_choice == "p")
                or (comp_choice == "s" and user_choice == "r")
                or (comp_choice == "p" and user_choice == "s")
            ):
                print("user won")
                w += 1
            else:
                print("you loose")
                l += 1
    print("you have " + str(w) + " wins ,")
    print("you have " + str(l) + " loss ,")
    print("you have " + str(d) + " draws ,")

    again=int(input("do you want to play again? type 1 for yes or 2 for no?: "))
    if(again==1):
        play()
    return

play()
