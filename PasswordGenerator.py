import random

def load_file_to_set(file_path):
    'Helper function to load file content into a set for fast lookup'
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return set(line.strip() for line in f)

def load_file_to_list(file_path):
    'Helper function to load file content into a list for random selection'
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f]

def defaultPasswordGenerator(dictionary_file, chars_file, rockyou_file):
    'this function generates a password using the dictionary and numbers and checks rockyou to determine that it is not a vulnerable password'
    
    #Load the dictionary file and rockyou file
    dictionary_words = load_file_to_list(dictionary_file)
    special_chars = load_file_to_list(chars_file)
    rockyou_passwords = load_file_to_set(rockyou_file)
    
    #intial password
    password = ""
    
    while True:
        # Generate password: choose 2 random words, a random number, and a special character
        word1 = random.choice(dictionary_words).capitalize()
        word2 = random.choice(dictionary_words).capitalize()
        random_number = str(random.randint(0, 9))
        special_char = random.choice(special_chars)
        
        password = f"{word1}{word2}{random_number}{special_char}"
        
        # Check if password exists in the rockyou list (AKA the compromised passwords list)
        if password not in rockyou_passwords:
            break  # Password is safe, exit loop


    with open("Passwords.txt", "a") as file:
        file.write(password + "\n")

    print(password)


#example function call (uncheck for testing)
#defaultPasswordGenerator("words.txt", "chars.txt", "rockyou.txt")

