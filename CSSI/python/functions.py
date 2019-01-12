
def go_get_dinner(f):
    print "get up"
    print "go out door"
    print "eat " + f
    return f*5


food = raw_input("What's for dinner: ")
#go_get_dinner(food)
print "yummmmm" + go_get_dinner(food)
go_get_dinner("pasta")
