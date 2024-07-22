# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, but it has errors. 
# Identify and fix them.

"""attendees = int(input("Enter number of attendees: ")) # added int()
venue = "large hall" if attendees > 100 else "conference room"
print(venue)"""

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall and an audio system" if attendees > 100 else "conference room and a projector"
print(f"A {venue} would be reccomended.")

food_preference = input("Would you like vegetarian food? ")
food = "Veggie Delight Caterers" if food_preference == "vegetarian" else "Gourmet Meals Caterers"
print(f"{food} would be reccomended")