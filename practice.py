#aske user name 
name = input("What's your name ? ").strip().title().capitalize()

#split user's name into first name and last name
first, last = name.split(" ")

#say hello to user
print(f"hello , {name}") 

print("your dumb", first)
