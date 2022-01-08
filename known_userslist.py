known_users = ["Natalija", "Steve", "Claire", "Bob", "Emma", "Bruce", "Georgie", "Harry"]

while True:
    print("Hi! My name is Comp Uter")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I'm glad you're staying!")
            
    else:
        print("Hmmm I don't think we have met yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
             known_users.append(name)
        elif add_me == "n":
            print("No problem, goodbye!")

