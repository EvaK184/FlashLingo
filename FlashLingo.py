import random
from difflib import SequenceMatcher

Greetings = [
    {"bulgarian": "Здравей", "english": "Hello", "pronunciation": "zdrav-ey"},
    {"bulgarian": "Здрасти", "english": "Hi", "pronunciation": "zdras-tee"},
    {"bulgarian": "Добро утро", "english": "Good morning", "pronunciation": "doh-bro oo-tro"},
    {"bulgarian": "Добър ден", "english": "Good day", "pronunciation": "doh-bur den"},
    {"bulgarian": "Добър вечер", "english": "Good evening", "pronunciation": "doh-bur ve-cher"},
    {"bulgarian": "Лека нощ", "english": "Good night", "pronunciation": "leh-ka nosht"},
    {"bulgarian": "Как си?", "english": "How are you?", "pronunciation": "kahk see"},
    {"bulgarian": "Как сте?", "english": "How are you?", "pronunciation": "kahk ste"},
    {"bulgarian": "Приятно ми е", "english": "Nice to meet you", "pronunciation": "pree-yat-no mee eh"},
    {"bulgarian": "Довиждане", "english": "Goodbye", "pronunciation": "doh-veezh-da-neh"},
    {"bulgarian": "Чао", "english": "Bye", "pronunciation": "chao"},
    {"bulgarian": "До скоро", "english": "See you soon", "pronunciation": "doh sko-ro"},
    {"bulgarian": "Благодаря", "english": "Thank you", "pronunciation": "blah-go-da-rya"},
]

Introducing_yourself = [
    {"bulgarian": "Здравей, казвам се...", "english": "Hello, my name is...", "pronunciation": "zdrav-ey, kaz-vam se..."},
    {"bulgarian": "Аз съм от...", "english": "I am from...", "pronunciation": "az sam ot..."},
    {"bulgarian": "Приятно ми е да се запознаем.", "english": "Nice to meet you.", "pronunciation": "pri-yat-no mee eh da se za-poz-na-em"},
    {"bulgarian": "На колко години сте?", "english": "How old are you?", "pronunciation": "na kol-ko go-dee-nee ste?"},
    {"bulgarian": "На ... години съм.", "english": "I am ... years old.", "pronunciation": "na ... go-dee-nee sam."},
    {"bulgarian": "Какво работите?", "english": "What do you do for a living?fo", "pronunciation": "kak-vo ra-bo-ti-te?"},
    {"bulgarian": "Какво работиш?", "english": "What do you do for a living?in", "pronunciation": "kak-vo ra-bo-tish?"},
    {"bulgarian": "Работя като...", "english": "I work as...", "pronunciation": "ra-bo-tya ka-to..."},
    {"bulgarian": "Аз съм студент.", "english": "I am a student.", "pronunciation": "az sam stu-dent."},
    {"bulgarian": "Къде живеете?", "english": "Where do you live?fo", "pronunciation": "ka-deh zhi-veh-eh-te?"},
    {"bulgarian": "Къде живееш?", "english": "Where do you live?in", "pronunciation": "ka-deh zhi-veh-esh?"},
    {"bulgarian": "Живея в...", "english": "I live in...", "pronunciation": "zhi-veh-ya v..."},
    {"bulgarian": "Какви са твоите хобита?", "english": "What are your hobbies?in", "pronunciation": "kak-vee sa tvo-ye-te ho-bi-ta?"},
    {"bulgarian": "Какви са вашите хобита?", "english": "What are your hobbies?fo", "pronunciation": "kak-vee sa va-shee-te ho-bi-ta?"},
    {"bulgarian": "Обичам да...", "english": "I love to...", "pronunciation": "o-bee-cham da..."},
]

Numbers = [
    {"bulgarian": "Едно", "english": "One", "pronunciation": "ed-no"},
    {"bulgarian": "Две", "english": "Two", "pronunciation": "dve"},
    {"bulgarian": "Три", "english": "Three", "pronunciation": "tree"},
    {"bulgarian": "Четири", "english": "Four", "pronunciation": "che-tee-ree"},
    {"bulgarian": "Пет", "english": "Five", "pronunciation": "pet"},
    {"bulgarian": "Шест", "english": "Six", "pronunciation": "shest"},
    {"bulgarian": "Седем", "english": "Seven", "pronunciation": "se-dem"},
    {"bulgarian": "Осем", "english": "Eight", "pronunciation": "o-sem"},
    {"bulgarian": "Девет", "english": "Nine", "pronunciation": "de-vet"},
    {"bulgarian": "Десет", "english": "Ten", "pronunciation": "de-set"},
    {"bulgarian": "Двадесет", "english": "Twenty", "pronunciation": "dva-de-set"},
    {"bulgarian": "Тридесет", "english": "Thirty", "pronunciation": "tree-de-set"},
    {"bulgarian": "Петнадесет", "english": "Fifteen", "pronunciation": "pet-na-de-set"},
    {"bulgarian": "Двадесет и пет", "english": "Twenty-five", "pronunciation": "dva-de-set ee pet"},
    {"bulgarian": "Тридесет и пет", "english": "Thirty-five", "pronunciation": "tree-de-set ee pet"},
    {"bulgarian": "Сто", "english": "One hundred", "pronunciation": "sto"},
    {"bulgarian": "Хиляда", "english": "One thousand", "pronunciation": "hee-ya-da"},
    {"bulgarian": "Половина", "english": "Half", "pronunciation": "po-lo-vee-na"},
    {"bulgarian": "Първи", "english": "First", "pronunciation": "pur-vee"},
    {"bulgarian": "Втори", "english": "Second", "pronunciation": "vto-ree"},
    {"bulgarian": "Трети", "english": "Third", "pronunciation": "tre-tee"},
    {"bulgarian": "Четвърти", "english": "Fourth", "pronunciation": "chet-vur-tee"},
    {"bulgarian": "Петти", "english": "Fifth", "pronunciation": "pet-tee"}
]

Days_Months_Seasons = [
    {"bulgarian": "Понеделник", "english": "Monday", "pronunciation": "po-ne-del-nik"},
    {"bulgarian": "Вторник", "english": "Tuesday", "pronunciation": "vto-rnik"},
    {"bulgarian": "Сряда", "english": "Wednesday", "pronunciation": "srya-da"},
    {"bulgarian": "Четвъртък", "english": "Thursday", "pronunciation": "chet-vur-tuk"},
    {"bulgarian": "Петък", "english": "Friday", "pronunciation": "pet-uk"},
    {"bulgarian": "Събота", "english": "Saturday", "pronunciation": "suh-bo-ta"},
    {"bulgarian": "Неделя", "english": "Sunday", "pronunciation": "ne-de-lya"},
    
    {"bulgarian": "Януари", "english": "January", "pronunciation": "ya-nu-a-ri"},
    {"bulgarian": "Февруари", "english": "February", "pronunciation": "fe-vro-a-ri"},
    {"bulgarian": "Март", "english": "March", "pronunciation": "mart"},
    {"bulgarian": "Април", "english": "April", "pronunciation": "a-pril"},
    {"bulgarian": "Май", "english": "May", "pronunciation": "may"},
    {"bulgarian": "Юни", "english": "June", "pronunciation": "yu-ni"},
    {"bulgarian": "Юли", "english": "July", "pronunciation": "yu-li"},
    {"bulgarian": "Август", "english": "August", "pronunciation": "av-goost"},
    {"bulgarian": "Септември", "english": "September", "pronunciation": "sep-tem-vri"},
    {"bulgarian": "Октомври", "english": "October", "pronunciation": "ok-tom-vri"},
    {"bulgarian": "Ноември", "english": "November", "pronunciation": "no-em-vri"},
    {"bulgarian": "Декември", "english": "December", "pronunciation": "de-kem-vri"},
    
    {"bulgarian": "Пролет", "english": "Spring", "pronunciation": "pro-let"},
    {"bulgarian": "Лято", "english": "Summer", "pronunciation": "lya-to"},
    {"bulgarian": "Есен", "english": "Autumn", "pronunciation": "e-sen"},
    {"bulgarian": "Зима", "english": "Winter", "pronunciation": "zi-ma"}
]

Telling_the_Time = [
    {"bulgarian": "Колко е часът?", "english": "What time is it?", "pronunciation": "kol-ko e cha-sut"},
    {"bulgarian": "Часът е", "english": "It is", "pronunciation": "cha-sut e"},
    {"bulgarian": "на час", "english": "o'clock", "pronunciation": "na chas"},
    {"bulgarian": "минута", "english": "minute", "pronunciation": "mi-nu-ta"},
    {"bulgarian": "минути", "english": "minutes", "pronunciation": "mi-nu-tee"},
    {"bulgarian": "час", "english": "hour", "pronunciation": "chas"},
    
    {"bulgarian": "една минута", "english": "one minute", "pronunciation": "ed-na mi-nu-ta"},
    {"bulgarian": "пет минути", "english": "five minutes", "pronunciation": "pet mi-nu-tee"},
    {"bulgarian": "десет минути", "english": "ten minutes", "pronunciation": "de-set mi-nu-tee"},
    {"bulgarian": "петнадесет минути", "english": "fifteen minutes", "pronunciation": "pet-na-de-set mi-nu-tee"},
    {"bulgarian": "тридесет минути", "english": "thirty minutes", "pronunciation": "tree-de-set mi-nu-tee"},
    
    {"bulgarian": "преди", "english": "before", "pronunciation": "pre-dee"},
    {"bulgarian": "след", "english": "after", "pronunciation": "sled"},
    {"bulgarian": "половина", "english": "half", "pronunciation": "po-lo-vee-na"},
    
    {"bulgarian": "Сега е", "english": "It is now", "pronunciation": "se-ga e"},
    {"bulgarian": "Вчера", "english": "Yesterday", "pronunciation": "vche-ra"},
    {"bulgarian": "Утре", "english": "Tomorrow", "pronunciation": "oo-tre"},
    
    {"bulgarian": "сутрин", "english": "morning", "pronunciation": "sut-rin"},
    {"bulgarian": "обед", "english": "afternoon", "pronunciation": "o-bet"},
    {"bulgarian": "вечер", "english": "evening", "pronunciation": "ve-cher"},
    {"bulgarian": "нощ", "english": "night", "pronunciation": "nosht"},
    
    {"bulgarian": "дванадесет часа", "english": "12 o'clock", "pronunciation": "dva-na-des-et cha-sut"},
    {"bulgarian": "една и петнадесет минути", "english": "one fifteen", "pronunciation": "ed-na i pet-na-de-set mi-nu-tee"},
    {"bulgarian": "три и тридесет минути", "english": "three thirty", "pronunciation": "tree i tree-de-set mi-nu-tee"},
    {"bulgarian": "пет и четиридесет и пет минути", "english": "five forty-five", "pronunciation": "pet i che-tee-ree-de-set mi-nu-tee"},
    {"bulgarian": "седем часа", "english": "seven o'clock", "pronunciation": "sed-em cha-sut"}
]

Categories = {"a" : Greetings, "b" : Introducing_yourself, "c" : Numbers, "d" : Days_Months_Seasons, "e" : Telling_the_Time}

# The quiz in intermediate mode. The user needs to write the answer.
def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the English translation of {word['bulgarian']}?")
        user_answer=input("Your Answer: ").strip().lower()
        correct_answer=word["english"].lower()

        if SequenceMatcher(None, user_answer, correct_answer).ratio() >0.8:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {word['english']} and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

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


def main():
    print("Welcome to FlashLingo!")
    input ("Press Enter to start the quiz...")
    choice = input("What category do you want to practise today? Your options are:\na - Greetings\nb - Introducing yourself\nc - Numbers\nd - Days, Months and Seasons\ne - Telling the Time\n")
    words = Categories[choice]
    level = input ("What level are you in this category? Press 'b' for begginer or 'i' for intermediate.")
    if level == "i":
        quiz_user(words)
    if level == "b":
        multi_choice(words)
        

if __name__=="__main__":
    main()
    
