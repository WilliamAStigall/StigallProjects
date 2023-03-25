import random
import time
start_time = time.time()
def password(password_length):
    #Generate new random password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    new_password = ''.join(random.sample(characters, password_length))

    return new_password


def brute_force_password(password_length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    p_password = password(password_length)
    #Compares each password to the target password and returns the password if found
    for guess in brute_force_generator(characters, password_length):
        if guess == password:
            print("Password found: " + guess)
            return guess

    print("Password not found")
    return None

#recursive method to brute force the password
def brute_force_generator(characters, password_length):
    #base case
    if password_length == 0:
        yield ''
    #decreases the password length until it reaches zero searching each combination at each length iterating over all characters
    else:
        for c in characters:
            for sub in brute_force_generator(characters, password_length - 1):
                yield c + sub


while True:
    #If you want to test how secure Google's suggested password system is and why you should potentially use it run with a length of 12
    try:
        user_input = int(input("Enter the length for the password: "))
        password(user_input)
        brute_force_password(user_input)
        end_time = time.time()
        runtime = end_time-start_time
        print(runtime)
        break
    except ValueError:
        print("Error: Please enter a valid integer value for password length.")
