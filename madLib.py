print("Welcome to the Mad Libs game! Please provide the following words:")

adjective = input("1. An adjective: ")
large_objects_plural = input("2. Large objects (plural): ")
adjective_body_part = input("3. An adjective: ")
body_part = input("4. A body part: ")
restaurant = input("5. A restaurant: ")
first_food = input("6. A food: ")
second_food = input("7. Another food: ")

story = f"I’ve had a very {adjective} day."
story += f"\nThis morning, I dropped a box of {large_objects_plural} on my {body_part}."
story += f"\nThen, at lunch, I went to {restaurant} for their delicious {first_food},"
story += f"\nBut the waiter brought me {second_food}, which I was not hungry for."
story += f"\nFinally, on my way home, I was cut off by a van with a large {adjective_body_part} strapped to the roof."

print("\nHere's your Mad Lib story:\n")
print(story)