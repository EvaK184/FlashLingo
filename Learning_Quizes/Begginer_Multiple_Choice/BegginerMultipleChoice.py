class multi_choice:
    """Define the multiple choice quiz"""

    def __init__(self):


# The quiz in easy mode. The user has to choose an option from a multiple choice.
def multi_choice(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the English translation of {word['bulgarian']}?")
        options = [word['english']]
        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(words)
            if other_word["english"] not in options:
                options.append(other_word["english"])
        random.shuffle(options)
        optionsABCD = {"A": options[0], "B" : options[1], "C" : options[2], "D": options[3]}
        user_answer=input(f"A.{options[0]} B.{options[1]} C.{options[2]} D.{options[3]}\n")
        if optionsABCD[user_answer]==word["english"]:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {word['english']} and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

# English to Bulgarian this time, multiple choice
def multi_choice2(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the Bulgarian translation of {word['english']}?")
        options = [word['bulgarian']]
        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(words)
            if other_word["bulgarian"] not in options:
                options.append(other_word["bulgarian"])
        random.shuffle(options)
        optionsABCD = {"A": options[0], "B" : options[1], "C" : options[2], "D": options[3]}
        user_answer=input(f"A.{options[0]} B.{options[1]} C.{options[2]} D.{options[3]}\n")
        if optionsABCD[user_answer]==word["bulgarian"]:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {word['bulgarian']} and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")