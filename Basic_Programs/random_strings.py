# Generating random strings until a given string is generated
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for l in range(length))

def generate_until_match(target_string):
    generated_string = ""
    attempts = 0

    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
        attempts += 1
        print(f"Attempt {attempts}: {generated_string}")

    print(f"Target string '{target_string}' generated in {attempts} attempts.")

# Example usage
target_string = "Hello"
generate_until_match(target_string)