print("enter ehelp for more in formation")
comand=""
started=False
while True:
    comand=input("> ").lower()
    if comand=="start":
        if started:
            print("Car is already started")
        else:
            started=True
            print("Your car is started.....")       
    elif comand=="stop":
        if not started:
            print("Car is already stoped")
        else:
            started=False
            print("You stop your car now@@@")
    elif comand=="quit":
        print("You are from out side the game") 
        break                 
    elif comand=="help":
        print('''
enter start --If you want to start the car
enter stop -- if you want to stop the car
enter quit -- if you want to quit the game
        ''')
    else:
        print('Dont understand enter help for more information')