# 1-importing the random module
import random 

# 2-Creating subjects,actions,places_or_things using list
subjects = [
    "Shahrukh Bhai G",
    "Virat Sharma",
    "Nirmala Aunty",
    "A Mumbai Cat",
    "A group of Monkeys",
    "Prime Minister Naren Bhai",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things =[
    "at Red Fort",
    "Mumbai Local Train",
    "A plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India gate"
]

# 3- using while loop to generate the headline
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    head_line=f"BREAKING NEWS: {subject} {action} {places_or_thing} "
    print("\n" + head_line)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#printing goodbye message
print("\n Thanks for using Fake news headline Generator ") 