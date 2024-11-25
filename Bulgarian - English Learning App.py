import random

words = [
    {"bulgarian": "Здравей", "english": "Hello", "pronunciation": "zdrav-ey"},
    {"bulgarian": "Здрасти", "english": "Hi", "pronunciation": "zdras-tee"},
    {"bulgarian": "Добро утро", "english": "Good morning", "pronunciation": "doh-bro oo-tro"},
    {"bulgarian": "Добър ден", "english": "Good day", "pronunciation": "doh-bur den"},
    {"bulgarian": "Добър вечер", "english": "Good evening", "pronunciation": "doh-bur ve-cher"},
    {"bulgarian": "Лека нощ", "english": "Good night", "pronunciation": "leh-ka nosht"},
    {"bulgarian": "Как си?", "english": "How are you? (informal)", "pronunciation": "kahk see"},
    {"bulgarian": "Как сте?", "english": "How are you? (formal/plural)", "pronunciation": "kahk ste"},
    {"bulgarian": "Приятно ми е", "english": "Nice to meet you", "pronunciation": "pree-yat-no mee eh"},
    {"bulgarian": "Довиждане", "english": "Goodbye", "pronunciation": "doh-veezh-da-neh"},
    {"bulgarian": "Чао", "english": "Bye", "pronunciation": "chao"},
    {"bulgarian": "До скоро", "english": "See you soon", "pronunciation": "doh sko-ro"},
    {"bulgarian": "Заповядай", "english": "Here you go / Welcome (informal)", "pronunciation": "za-po-vya-dai"},
    {"bulgarian": "Заповядайте", "english": "Here you go / Welcome (formal)", "pronunciation": "za-po-vya-dai-te"},
    {"bulgarian": "Благодаря", "english": "Thank you", "pronunciation": "blah-go-da-rya"},
]

def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"What is the English translation of {word["bulgarian"]}?")
        user_answer=input("Your Answer: ").strip().lower()
        correct_answer=word["english"].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {word["english"]}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")
    


def main():
    print("Welcome to the Language Learning Flashcards App!")
    input ("Press Enter to start the quiz...")
    quiz_user(words)

if __name__=="__main__":
    main()
    
