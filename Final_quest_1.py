Entry=input("Enter your name:\n")

if "ARTHUR" in Entry.upper():# translate into uppercase
    correct= True           
    if(correct):
        print("My liege! You may pass!")
else:
    GRAILS=input("What is your quest:\n") # ask user for quest
    if "GRAILS" in GRAILS.upper():
            color=input("What is your favorite colour?\n")
            if (color[0]==Entry[0]):
                print("You may pass!")
            else:
                print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")