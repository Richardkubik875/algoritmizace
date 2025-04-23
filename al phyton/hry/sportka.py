import random

def draw_numbers():
    numbers = random.sample(range(1, 50), 7)  
    return numbers[:6], numbers[6]  

def get_or_generate_user_numbers(use_generated=True):
    if use_generated:
        return random.sample(range(1, 50), 6)  
    else:
        user_numbers = []
        print("Enter 6 different numbers between 1 and 49:")
        while len(user_numbers) < 6:
            try:
                number = int(input(f"Number {len(user_numbers)+1}: "))
                if number < 1 or number > 49:
                    print("The number must be between 1 and 49.")
                elif number in user_numbers:
                    print("This number has already been entered, please choose another.")
                else:
                    user_numbers.append(number)
            except ValueError:
                print("Invalid input! Please enter an integer.")
        return user_numbers

def compare_numbers(user_numbers, drawn_numbers, bonus_number):
    matches = set(user_numbers) & set(drawn_numbers)  
    bonus_match = len(matches) == 5 and bonus_number in user_numbers 
    return matches, bonus_match

drawn_numbers, bonus_number = draw_numbers()

user_numbers = get_or_generate_user_numbers(use_generated=True)

draw_results = sorted(drawn_numbers)
user_results = sorted(user_numbers)

print("\nDrawn numbers:", draw_results)
print("Bonus number:", bonus_number)
print("Your numbers:", user_results)

matches, bonus_match = compare_numbers(user_numbers, drawn_numbers, bonus_number)
print(f"Number of matches: {len(matches)}")
print("Matched numbers:", sorted(matches))

if bonus_match:
    print("You matched 5 numbers and the bonus number!")
