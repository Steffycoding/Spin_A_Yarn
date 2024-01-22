def spin_a_yarn():
    # Get user inputs
    adjective = input("Enter an adjective: ")
    preposition = input("Enter a preposition: ")
    proper_noun = input("Enter a proper noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Story template
    story_template = "Once upon a time, there was a {adjective} {noun}. " \
                     "It loved to {verb} {preposition} the {adjective} {noun} {adverb}."

    # Fill in the inputs
    yarn_story = story_template.format(adjective=adjective, preposition=preposition,
                                       noun=proper_noun, verb=verb, adverb=adverb)

    # Print the spun yarn
    print("\nSpun Yarn:")
    print(yarn_story)

if __name__ == "__main__":
    spin_a_yarn()
