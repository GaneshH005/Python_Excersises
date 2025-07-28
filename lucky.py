lucky = 9
guess = 20

if guess < lucky - 2 :
    print("Too low")
elif guess > lucky + 2 :
    print("Too high")
elif guess == lucky :
    print("correct")
else:
    print ("you are Almost There")
