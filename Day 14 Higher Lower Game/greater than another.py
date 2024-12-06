import random
import game_data

# call for random element from the list
def random_name_generator():
    return random.choice(game_data.data)

# compare two random items
def compare():
    item1 = random_name_generator()     # take random first input
    item2 = random_name_generator()     # take random second input
    game_on = True
    count = 0                           # store the count for score
    used_items = []                     # store the items used
    while game_on:
        print(f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}")
        print(f"Compare B : {item2['name']}, a {item2['description']}, from {item2['country']}")

        # compare the follower of item1 and item2
        count_a = item1['follower_count']
        count_b = item2['follower_count']
        answer = input("Who has more followers? Type 'A' or 'B' :\n").lower()

        if item1 != item2:
            # checks input value and compare with followers value
            if (answer == "a" and count_a > count_b) or (answer == "b" and count_b > count_a):
                count += 1
                print(f"Correct, score: {count}")
                if answer == "a":                                   # input a is correct, a > b
                    used_items.append(item2['name'])                # add item2 to used_items
                    while True:
                        item2 = random_name_generator()             # keeps generating random item2 until item2 is unique
                        if item2['name'] not in used_items and item2 != item1:
                            break
                else:
                    used_items.append(item1['name'])
                    item1 = item2
                    while True:
                        item2 = random_name_generator()             # keeps generating random item2 until item2 is unique
                        if item2['name'] not in used_items and item2 != item1:
                            break
            else:
                print(f"Incorrect, your score is: {count}")
                game_on = False
        else:
            item2 = random_name_generator()
        print(used_items)
print(compare())


