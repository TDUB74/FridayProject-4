import random

def generate_powerball_numbers():
    
    first_five_numbers = [random.randint(1, 69) for _ in range(5)]
    sixth_number = random.randint(1, 26)

  
    powerball_numbers = '  '.join(map(str, first_five_numbers)) + '    ' + str(sixth_number)

    return powerball_numbers


print("Welcome to the PowerBall number generator!")


user_input = input("Would you like some PowerBall numbers? (yes/no): ")

if user_input.lower() == 'yes':
   
    powerball_numbers = generate_powerball_numbers()

    
    print("\nHere are your PowerBall numbers:")
    print(powerball_numbers)

  
    print("\nGood luck with your PowerBall ticket!")

else:
    print("\nNo problem. Feel free to come back anytime you need PowerBall numbers.")
