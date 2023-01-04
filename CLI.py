from logic import Human, Computer, Game


if __name__ == "__main__":

    print("Play against :")
    print("1) Human ")
    print("2) AI ")


    choice=int(input("> Pick?: "))
    if choice<=1:

        game=Game(Human(), Human())
    else:
        game=Game(Human(), Computer())



    game.run()