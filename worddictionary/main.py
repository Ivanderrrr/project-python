# have a python dictionary that has a key/value pair that represents a word and it's definition.
# collect input from the user, input is a word.
# check if the word is in the dictionary.
# print the definition.

def main():
    word_dictionaries = {
        "Polymorphism": "Ability of different objects to respond to the same method or function call.",
        "Annotation": "Ability to add metadata, information, or hints to the variables, function parameters, "
                      "and return types.",
        "Decorator": "A design pattern and a special type of function or class that is used to modify or extend the "
                     "behavior of another function or method.",
        "Recursion": "Process where a function calls itself directly or indirectly in order to solve a problem,"
    }
    
    # infinity loop to ask the user.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word.title() in word_dictionaries:
            print(word.title(), ":", word_dictionaries[word.title()])
            
main()
print("Program ended.")

