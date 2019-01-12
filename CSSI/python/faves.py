def shout(food, number):
    food = food.upper()
    vowels= ["A","E","I","O","U"]
    for x in vowels:
        food = food.replace(x,x*number)

    print food
shout ("potatoe",30)
