friends = {}

while True:
    person = raw_input("Enter the name of a person:")

    if person == "exit":
        break

    if person == "print":
            print friends
            continue


    if person not in friends:
        friends[person] = []


    friend = raw_input("Enter the name of a friend of " + person + ":")

    #Add friend to friends[person]
    friends[person].append(friend)

    
