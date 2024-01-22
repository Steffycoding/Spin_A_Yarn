import random
from termcolor import colored

def get_user_input(prompt, color):
    return input(colored(prompt, color))

def spin_a_yarn():
    # Get user inputs
    adjective = get_user_input("Enter an adjective: ", 'red')
    preposition = get_user_input("Enter a preposition: ", 'green')
    proper_noun = get_user_input("Enter a proper noun: ", 'yellow')
    verb = get_user_input("Enter a verb: ", 'blue')
    adverb = get_user_input("Enter an adverb: ", 'magenta')

    # Create versatile story templates
    templates = [
        f"The {adjective} {preposition} {proper_noun} {verb} {adverb}.",
        f"{proper_noun} {adverb} {verb} {preposition} a {adjective} way.",
        f"In a world of {adjective}, {proper_noun} loves to {verb} {adverb}.",
        f"{proper_noun} and {adjective} {proper_noun} {verb} {adverb}.",
        f"A {adjective} {proper_noun} {verb}s {adverb} during the {preposition}.",
        f"{proper_noun} {verb}s {adverb} when it's {adjective}.",
    ]

    # Select a random story template
    selected_template = random.choice(templates)

    # Display the generated story in light blue
    print(colored("\nGenerated Story:", 'cyan'))
    print(colored(selected_template, 'cyan'))

if __name__ == "__main__":
    spin_a_yarn()
