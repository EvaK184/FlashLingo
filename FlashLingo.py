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
    {"bulgarian": "Съжалявам", "english": "I am sorry", "pronunciation": "sŭ-zha-lya-vam"},
    {"bulgarian": "Извинявай", "english": "I am sorry in", "pronunciation": "iz-vi-nyavai"},
    {"bulgarian": "Извинете", "english": "I am sorry fo", "pronunciation": "iz-vi-ne-te"},
    {"bulgarian": "Моля", "english": "You are welcome", "pronunciation": "mo-lya"},
    {"bulgarian": "Няма проблем", "english": "No problem", "pronunciation": "nya-ma pro-blem"},
    {"bulgarian": "Добре съм. Благодаря. А ти?", "english": "I am fine. Thank you. How about you? (informal)", "pronunciation": "do-bre sŭm. bla-go-da-rya. a ti?"},
    {"bulgarian": "Добре съм. Благодаря. А Вие?", "english": "I am fine. Thank you. How about you? (formal)", "pronunciation": "do-bre sŭm. bla-go-da-rya. a vie?"}
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
    {"bulgarian": "Зима", "english": "Winter", "pronunciation": "zi-ma"},
    
    {"bulgarian": "Какъв ден е днес?", "english": "What day is it today?", "pronunciation": "ka-kuv den eh dnes?"},
    {"bulgarian": "Днес е...", "english": "Today is...", "pronunciation": "dnes eh..."},
    {"bulgarian": "Коя дата е днес?", "english": "What is the date today?", "pronunciation": "ko-ya da-ta eh dnes?"},
    {"bulgarian": "Днес е първи януари.", "english": "Today is January 1st.", "pronunciation": "dnes eh pur-vi ya-nu-a-ri."},
    {"bulgarian": "В кой месец сме?", "english": "What month are we in?", "pronunciation": "v koy me-sets sme?"},
    {"bulgarian": "Ние сме в декември.", "english": "We are in December.", "pronunciation": "ni-ye sme v de-kem-vri."},
    {"bulgarian": "Коя година е?", "english": "What year is it?", "pronunciation": "ko-ya go-di-na eh?"},
    {"bulgarian": "Днес е зимата.", "english": "It is winter today.", "pronunciation": "dnes eh zi-ma-ta."},
    {"bulgarian": "Следващата пролет ще бъде топла.", "english": "Next spring will be warm.", "pronunciation": "sled-vash-ta pro-let shte bu-de top-la."},
    {"bulgarian": "Обичам лятото.", "english": "I love the summer.", "pronunciation": "o-bi-cham lya-to-to."}
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

alphabet = [
    {"bulgarian": "А", "pronunciation": "a", "english_equivalent": "a in 'apple'"},
    {"bulgarian": "Б", "pronunciation": "b", "english_equivalent": "b in 'boy'"},
    {"bulgarian": "В", "pronunciation": "v", "english_equivalent": "v in 'van'"},
    {"bulgarian": "Г", "pronunciation": "g", "english_equivalent": "g in 'go'"},
    {"bulgarian": "Д", "pronunciation": "d", "english_equivalent": "d in 'dog'"},
    {"bulgarian": "Е", "pronunciation": "e", "english_equivalent": "e in 'pet'"},
    {"bulgarian": "Ж", "pronunciation": "zh", "english_equivalent": "s in 'measure'"},
    {"bulgarian": "З", "pronunciation": "z", "english_equivalent": "z in 'zoo'"},
    {"bulgarian": "И", "pronunciation": "i", "english_equivalent": "i in 'sit'"},
    {"bulgarian": "Й", "pronunciation": "y", "english_equivalent": "y in 'yes'"},
    {"bulgarian": "К", "pronunciation": "k", "english_equivalent": "k in 'kite'"},
    {"bulgarian": "Л", "pronunciation": "l", "english_equivalent": "l in 'lamp'"},
    {"bulgarian": "М", "pronunciation": "m", "english_equivalent": "m in 'man'"},
    {"bulgarian": "Н", "pronunciation": "n", "english_equivalent": "n in 'net'"},
    {"bulgarian": "О", "pronunciation": "o", "english_equivalent": "o in 'or'"},
    {"bulgarian": "П", "pronunciation": "p", "english_equivalent": "p in 'pen'"},
    {"bulgarian": "Р", "pronunciation": "r", "english_equivalent": "rolled r (as in Spanish)"},
    {"bulgarian": "С", "pronunciation": "s", "english_equivalent": "s in 'sun'"},
    {"bulgarian": "Т", "pronunciation": "t", "english_equivalent": "t in 'top'"},
    {"bulgarian": "У", "pronunciation": "u", "english_equivalent": "oo in 'boot'"},
    {"bulgarian": "Ф", "pronunciation": "f", "english_equivalent": "f in 'fish'"},
    {"bulgarian": "Х", "pronunciation": "kh", "english_equivalent": "ch in Scottish 'loch'"},
    {"bulgarian": "Ц", "pronunciation": "ts", "english_equivalent": "ts in 'cats'"},
    {"bulgarian": "Ч", "pronunciation": "ch", "english_equivalent": "ch in 'chess'"},
    {"bulgarian": "Ш", "pronunciation": "sh", "english_equivalent": "sh in 'ship'"},
    {"bulgarian": "Щ", "pronunciation": "sht", "english_equivalent": "sht (no exact English equivalent)"},
    {"bulgarian": "Ъ", "pronunciation": "a", "english_equivalent": "u in 'but' (centralized vowel)"},
    {"bulgarian": "Ь", "pronunciation": "soft sign", "english_equivalent": "softens the preceding consonant"},
    {"bulgarian": "Ю", "pronunciation": "yu", "english_equivalent": "u in 'use'"},
    {"bulgarian": "Я", "pronunciation": "ya", "english_equivalent": "ya in 'yard'"},
]

Family_and_Friends = [
    {"bulgarian": "Семейство", "english": "Family", "pronunciation": "se-meys-tvo"},
    {"bulgarian": "Майка", "english": "Mother", "pronunciation": "may-ka"},
    {"bulgarian": "Татко", "english": "Father", "pronunciation": "tat-ko"},
    {"bulgarian": "Брат", "english": "Brother", "pronunciation": "brat"},
    {"bulgarian": "Сестра", "english": "Sister", "pronunciation": "ses-tra"},
    {"bulgarian": "Дете", "english": "Child", "pronunciation": "de-te"},
    {"bulgarian": "Син", "english": "Son", "pronunciation": "sin"},
    {"bulgarian": "Дъщеря", "english": "Daughter", "pronunciation": "dŭ-shte-rya"},
    {"bulgarian": "Баба", "english": "Grandmother", "pronunciation": "ba-ba"},
    {"bulgarian": "Дядо", "english": "Grandfather", "pronunciation": "dya-do"},
    {"bulgarian": "Внук", "english": "Grandson", "pronunciation": "vnuk"},
    {"bulgarian": "Внучка", "english": "Granddaughter", "pronunciation": "vnooch-ka"},
    {"bulgarian": "Роднини", "english": "Relatives", "pronunciation": "rod-nee-nee"},
    {"bulgarian": "Приятел", "english": "Friend (male)", "pronunciation": "pri-ya-tel"},
    {"bulgarian": "Приятелка", "english": "Friend (female)", "pronunciation": "pri-ya-tel-ka"},
    {"bulgarian": "Съпруг", "english": "Husband", "pronunciation": "sŭ-prug"},
    {"bulgarian": "Съпруга", "english": "Wife", "pronunciation": "sŭ-pru-ga"},
    {"bulgarian": "Партньор", "english": "Partner", "pronunciation": "part-nyor"},
    {"bulgarian": "Колега", "english": "Colleague (male)", "pronunciation": "ko-le-ga"},
    {"bulgarian": "Колежка", "english": "Colleague (female)", "pronunciation": "ko-lezh-ka"},
    {"bulgarian": "Познати", "english": "Acquaintances", "pronunciation": "poz-na-ti"},
    {"bulgarian": "Съсед", "english": "Neighbor (male)", "pronunciation": "sŭ-sed"},
    {"bulgarian": "Съседка", "english": "Neighbor (female)", "pronunciation": "sŭ-sed-ka"},
    {"bulgarian": "Кръстник", "english": "Godfather", "pronunciation": "krŭst-nik"},
    {"bulgarian": "Кръстница", "english": "Godmother", "pronunciation": "krŭst-ni-tsa"},
    {"bulgarian": "Кръщелник", "english": "Godson", "pronunciation": "krŭsh-tel-nik"},
    {"bulgarian": "Кръщелница", "english": "Goddaughter", "pronunciation": "krŭsh-tel-ni-tsa"},
    {"bulgarian": "Чичо", "english": "Uncle", "pronunciation": "chee-cho"},
    {"bulgarian": "Леля", "english": "Aunt", "pronunciation": "le-lya"},
    {"bulgarian": "Братовчед", "english": "Cousin (male)", "pronunciation": "bra-tov-ched"},
    {"bulgarian": "Братовчедка", "english": "Cousin (female)", "pronunciation": "bra-tov-ched-ka"},
    {"bulgarian": "Как се казваш?", "english": "What is your name?", "pronunciation": "kak se kaz-vash"},
    {"bulgarian": "Кой е твоят приятел?", "english": "Who is your friend?", "pronunciation": "koy e tvo-yat pri-ya-tel"},
    {"bulgarian": "Имаш ли семейство?", "english": "Do you have a family?", "pronunciation": "i-mash li se-meys-tvo"},
    {"bulgarian": "Къде живеят твоите родители?", "english": "Where do your parents live?", "pronunciation": "kŭ-de zhi-ve-yat tvoi-te ro-di-te-li"},
    {"bulgarian": "Имаш ли братя и сестри?", "english": "Do you have siblings?", "pronunciation": "i-mash li brat-ya i ses-tri"},
    {"bulgarian": "Кой е твоят най-добър приятел?", "english": "Who is your best friend?", "pronunciation": "koy e tvoi-yat nay-do-bŭr pri-ya-tel"}
]

Colors_and_Shapes = [
    {"bulgarian": "Червен", "english": "Red", "pronunciation": "cher-ven"},
    {"bulgarian": "Син", "english": "Blue", "pronunciation": "sin"},
    {"bulgarian": "Зелен", "english": "Green", "pronunciation": "ze-len"},
    {"bulgarian": "Жълт", "english": "Yellow", "pronunciation": "zhŭlt"},
    {"bulgarian": "Черно", "english": "Black", "pronunciation": "cher-no"},
    {"bulgarian": "Бяло", "english": "White", "pronunciation": "byalo"},
    {"bulgarian": "Оранжев", "english": "Orange", "pronunciation": "o-ran-zh-ev"},
    {"bulgarian": "Розов", "english": "Pink", "pronunciation": "ro-zov"},
    {"bulgarian": "Кафяв", "english": "Brown", "pronunciation": "ka-fyav"},
    {"bulgarian": "Сив", "english": "Gray", "pronunciation": "siv"},
    {"bulgarian": "Кръгъл", "english": "Round", "pronunciation": "krŭ-gŭl"},
    {"bulgarian": "Квадратен", "english": "Square", "pronunciation": "kvad-ra-ten"},
    {"bulgarian": "Триъгълен", "english": "Triangular", "pronunciation": "tree-ŭ-gŭ-len"},
    {"bulgarian": "Правоъгълен", "english": "Rectangular", "pronunciation": "pra-vo-ŭ-gŭ-len"}
]

Clothing = [
    {"bulgarian": "Риза", "english": "Shirt", "pronunciation": "ri-za"},
    {"bulgarian": "Панталони", "english": "Pants", "pronunciation": "pan-ta-lo-ni"},
    {"bulgarian": "Тениска", "english": "T-shirt", "pronunciation": "te-nis-ka"},
    {"bulgarian": "Жилетка", "english": "Vest", "pronunciation": "zhil-et-ka"},
    {"bulgarian": "Яке", "english": "Jacket", "pronunciation": "ya-ke"},
    {"bulgarian": "Палто", "english": "Coat", "pronunciation": "pal-to"},
    {"bulgarian": "Обувки", "english": "Shoes", "pronunciation": "o-buv-ki"},
    {"bulgarian": "Сандали", "english": "Sandals", "pronunciation": "san-da-li"},
    {"bulgarian": "Боти", "english": "Boots", "pronunciation": "bo-ti"},
    {"bulgarian": "Чорапи", "english": "Socks", "pronunciation": "cho-ra-pi"},
    {"bulgarian": "Шапка", "english": "Hat", "pronunciation": "shap-ka"},
    {"bulgarian": "Ръкавици", "english": "Gloves", "pronunciation": "rŭ-ka-vi-tsi"},
    {"bulgarian": "Палто", "english": "Coat", "pronunciation": "pal-to"}
]

Weather = [
    {"bulgarian": "Слънчево", "english": "Sunny", "pronunciation": "slŭn-che-vo"},
    {"bulgarian": "Дъждовно", "english": "Rainy", "pronunciation": "dŭzh-dov-no"},
    {"bulgarian": "Облачно", "english": "Cloudy", "pronunciation": "ob-lach-no"},
    {"bulgarian": "Студено", "english": "Cold", "pronunciation": "stu-de-no"},
    {"bulgarian": "Топло", "english": "Warm", "pronunciation": "top-lo"},
    {"bulgarian": "Вятър", "english": "Windy", "pronunciation": "vyatŭr"},
    {"bulgarian": "Мъгла", "english": "Foggy", "pronunciation": "mŭ-gla"},
    {"bulgarian": "Сняг", "english": "Snow", "pronunciation": "snyag"},
    {"bulgarian": "Гръмотевици", "english": "Thunderstorm", "pronunciation": "grŭ-mo-te-vi-tsi"},
    {"bulgarian": "Температура", "english": "Temperature", "pronunciation": "tem-pe-ra-tu-ra"},
    {"bulgarian": "Колко е температурата?", "english": "What is the temperature?", "pronunciation": "kol-ko e tem-pe-ra-tu-ra-ta"}
]

WH_Questions = [
    {"bulgarian": "Какво е това?", "english": "What is this?", "pronunciation": "kak-vo e to-va?"},
    {"bulgarian": "Как се казваш?", "english": "What is your name?", "pronunciation": "kak se kaz-vash?"},
    {"bulgarian": "Къде е това?", "english": "Where is this?", "pronunciation": "kŭ-de e to-va?"},
    {"bulgarian": "Къде живееш?", "english": "Where do you live?", "pronunciation": "kŭ-de zhi-ve-esh?"},
    {"bulgarian": "Кога?", "english": "When?", "pronunciation": "ko-ga?"},
    {"bulgarian": "Защо?", "english": "Why?", "pronunciation": "za-shto?"},
    {"bulgarian": "Как?", "english": "How?", "pronunciation": "kak?"},
    {"bulgarian": "Кой?", "english": "Who?", "pronunciation": "koy?"},
    {"bulgarian": "Колко?", "english": "How many?", "pronunciation": "kol-ko?"},
    {"bulgarian": "Какво правиш?", "english": "What are you doing?", "pronunciation": "kak-vo pra-vish?"},
    {"bulgarian": "Какво ще правиш утре?", "english": "What will you do tomorrow?", "pronunciation": "kak-vo shte pra-vish u-tre?"},
    {"bulgarian": "Как се чувстваш?", "english": "How do you feel?", "pronunciation": "kak se chuv-stash?"},
    {"bulgarian": "Кой е твой приятел?", "english": "Who is your friend?", "pronunciation": "koy e tvoy pri-ya-tel?"},
    {"bulgarian": "Какъв е този звук?", "english": "What is that sound?", "pronunciation": "kak-ŭv e to-zi zvuk?"},
    {"bulgarian": "Какъв е твоят план?", "english": "What is your plan?", "pronunciation": "kak-ŭv e tvo-yat plan?"},
    {"bulgarian": "Колко време?", "english": "How long?", "pronunciation": "kol-ko vre-me?"}
]

Shopping_and_Money = [
    {"bulgarian": "Цената е ...", "english": "The price is ...", "pronunciation": "tse-na-ta e ..."},
    {"bulgarian": "Колко струва това?", "english": "How much is this?", "pronunciation": "kol-ko stru-va to-va?"},
    {"bulgarian": "Имам ли отстъпка?", "english": "Do I have a discount?", "pronunciation": "i-mam li ot-stŭp-ka?"},
    {"bulgarian": "Платете в брой или с карта", "english": "Pay by cash or card", "pronunciation": "pla-te-te v broy ili s kar-ta"},
    {"bulgarian": "Парични средства", "english": "Cash", "pronunciation": "pa-rich-ni sred-stva"},
    {"bulgarian": "Какво е това?", "english": "What is this?", "pronunciation": "kak-vo e to-va?"}
]

Eating_and_Drinking = [
    {"bulgarian": "Храна", "english": "Food", "pronunciation": "khra-na"},
    {"bulgarian": "Напитка", "english": "Drink", "pronunciation": "na-pit-ka"},
    {"bulgarian": "Меню", "english": "Menu", "pronunciation": "me-nyu"},
    {"bulgarian": "Супа", "english": "Soup", "pronunciation": "su-pa"},
    {"bulgarian": "Пица", "english": "Pizza", "pronunciation": "pi-tsa"},
    {"bulgarian": "Месо", "english": "Meat", "pronunciation": "me-so"},
    {"bulgarian": "Риба", "english": "Fish", "pronunciation": "ri-ba"},
    {"bulgarian": "Вода", "english": "Water", "pronunciation": "vo-da"},
    {"bulgarian": "Бира", "english": "Beer", "pronunciation": "bi-ra"},
    {"bulgarian": "Чай", "english": "Tea", "pronunciation": "chai"},
    {"bulgarian": "Кафе", "english": "Coffee", "pronunciation": "ka-fe"},
    {"bulgarian": "Моля, един ...", "english": "Please, one ...", "pronunciation": "mo-lya, e-din ..."}
]

Transportation = [
    {"bulgarian": "Автобус", "english": "Bus", "pronunciation": "av-to-bus"},
    {"bulgarian": "Трамвай", "english": "Tram", "pronunciation": "tram-vay"},
    {"bulgarian": "Метро", "english": "Metro", "pronunciation": "me-tro"},
    {"bulgarian": "Колело", "english": "Bicycle", "pronunciation": "ko-le-lo"},
    {"bulgarian": "Колата", "english": "Car", "pronunciation": "ko-la-ta"},
    {"bulgarian": "Такси", "english": "Taxi", "pronunciation": "tak-si"},
    {"bulgarian": "Влак", "english": "Train", "pronunciation": "vlak"},
    {"bulgarian": "Къде е спирката?", "english": "Where is the stop?", "pronunciation": "kŭ-de e spir-ka-ta?"},
    {"bulgarian": "Билет", "english": "Ticket", "pronunciation": "bi-let"},
    {"bulgarian": "С кола или автобус?", "english": "By car or bus?", "pronunciation": "s ko-la ili av-to-bus?"}
]

Rooms_and_Furniture = [
    {"bulgarian": "Стая", "english": "Room", "pronunciation": "sta-ya"},
    {"bulgarian": "Хол", "english": "Living room", "pronunciation": "hol"},
    {"bulgarian": "Спалня", "english": "Bedroom", "pronunciation": "spal-nya"},
    {"bulgarian": "Кухня", "english": "Kitchen", "pronunciation": "kukh-nya"},
    {"bulgarian": "Баня", "english": "Bathroom", "pronunciation": "ba-nya"},
    {"bulgarian": "Трапезария", "english": "Dining room", "pronunciation": "tra-pe-za-ri-ya"},
    {"bulgarian": "Маса", "english": "Table", "pronunciation": "ma-sa"},
    {"bulgarian": "Стол", "english": "Chair", "pronunciation": "stol"},
    {"bulgarian": "Легло", "english": "Bed", "pronunciation": "leg-lo"},
    {"bulgarian": "Диван", "english": "Sofa", "pronunciation": "di-van"}
]

Daily_Routines = [
    {"bulgarian": "Събуждам се", "english": "Wake up", "pronunciation": "sŭ-bu-zh-dam se"},
    {"bulgarian": "Ям", "english": "Eat", "pronunciation": "yam"},
    {"bulgarian": "Спя", "english": "Sleep", "pronunciation": "spya"},
    {"bulgarian": "Работя", "english": "Work", "pronunciation": "ra-bo-tya"},
    {"bulgarian": "Уча", "english": "Study", "pronunciation": "u-cha"},
    {"bulgarian": "Чета", "english": "Read", "pronunciation": "che-ta"},
    {"bulgarian": "Тренирам", "english": "Exercise", "pronunciation": "tre-ni-ram"},
    {"bulgarian": "Пътувам", "english": "Travel", "pronunciation": "pŭ-tu-vam"},
    {"bulgarian": "Пазарувам", "english": "Shop", "pronunciation": "pa-za-ru-vam"},
    {"bulgarian": "Готвя", "english": "Cook", "pronunciation": "got-vya"}
]

Actions_and_Verbs = [
    {"bulgarian": "Отивам", "english": "Go", "pronunciation": "o-ti-vam"},
    {"bulgarian": "Ям", "english": "Eat", "pronunciation": "yam"},
    {"bulgarian": "Спя", "english": "Sleep", "pronunciation": "spya"},
    {"bulgarian": "Говоря", "english": "Speak", "pronunciation": "go-vo-rya"},
    {"bulgarian": "Пиша", "english": "Write", "pronunciation": "pi-sha"},
    {"bulgarian": "Чета", "english": "Read", "pronunciation": "che-ta"},
    {"bulgarian": "Слушам", "english": "Listen", "pronunciation": "slŭ-sham"},
    {"bulgarian": "Работя", "english": "Work", "pronunciation": "ra-bo-tya"},
    {"bulgarian": "Тренирам", "english": "Exercise", "pronunciation": "tre-ni-ram"},
    {"bulgarian": "Пея", "english": "Sing", "pronunciation": "pe-ya"}
]

Categories = {"a" : Greetings, "b" : Introducing_yourself, "c" : Numbers, "d" : Days_Months_Seasons, "e" : Telling_the_Time,
              "f" : alphabet, "g": Family_and_Friends, "h": Colors_and_Shapes, "i": Clothing, "j": Weather, "k": WH_Questions, "l": Shopping_and_Money, "m": Eating_and_Drinking,
              "n": Transportation, "o": Rooms_and_Furniture, "p": Daily_Routines, "r": Actions_and_Verbs}

# The quiz in intermediate mode. The user needs to write the answer.
def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the English translation of {word['bulgarian']}?")
        user_answer=user_input("Your Answer: ").strip().lower()
        correct_answer=word["english"].lower()

        if SequenceMatcher(None, user_answer, correct_answer).ratio() >0.8:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}' and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

#For the alphabet only. Similar to the function above.
def alphabet_quiz(alphabet):
    random.shuffle(alphabet)
    score=0

    for word in alphabet:
        print(f"\nWhat is the pronunciation of {word['bulgarian']}?")
        user_answer=user_input("Your Answer: ").strip().lower()
        correct_answer=word["pronunciation"].lower()

        if SequenceMatcher(None, user_answer, correct_answer).ratio() >0.8:
            print(f"Correct! And it sounds like {word['english_equivalent']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['pronunciation']}' and it sounds like {word['english_equivalent']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(alphabet)}")

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
        user_answer=user_input(f"A.{options[0]} B.{options[1]} C.{options[2]} D.{options[3]}\n")
        if optionsABCD[user_answer]==word["english"]:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}' and it is pronounced {word['pronunciation']}.\n")
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
        user_answer=user_input(f"A.{options[0]} B.{options[1]} C.{options[2]} D.{options[3]}\n")
        if optionsABCD[user_answer]==word["bulgarian"]:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['bulgarian']}' and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

# Build the answer, word-by-word (only english to bulgarian)
def build(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the Bulgarian translation of {word['english']}? (add spaces between the numbers if multiple numbers are needed for the correct answer)")
        options = [word['bulgarian']]
        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(words)
            if other_word["bulgarian"] not in options:
                options.append(other_word["bulgarian"])
        #make a list of individual words made out of 4 different expressions
        split_options = options[0].split(" ") + options[1].split(" ") + options[2].split(" ") + options[3].split(" ")
        random.shuffle(split_options) #shuffle the individual words from all of the expressions
        options_list = []
        for option in split_options:
            option_dict = {str(split_options.index(option)):option} #make a dictionary with the form {individual_word_index(as a string):individual_word}
            options_list.append(option_dict) #put all of the dictionaries together in a list
        for x in options_list:
            print(x)
        user_answer=user_input()
        user_answer = user_answer.split(" ") #make a list with each number in the user's answer
        user_answer2 = []
        for i in user_answer:
            user_answer2.append(options_list[int(i)][i])
        user_answer3=" ".join(user_answer2)
        print(user_answer3)
        if user_answer3 == word['bulgarian']:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['bulgarian']}' and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")

#Give the user a "quit" option
def user_input(prompt):
    user_input1 = input(prompt)
    if user_input1 == "q":
        print("Thank you for using FlashLingo! Goodbye!")
        exit()
    return user_input1

# Initiate the game
def main():
    print("Welcome to FlashLingo!\n \nPress 'q' at any point to close the app")
    user_input ("Press Enter to start the quiz...")
    choice = user_input("What category do you want to practise today? Your options are:\n\
a - Greetings\n\
b - Introducing yourself\n\
c - Numbers\n\
d - Days, Months and Seasons\n\
e - Telling the Time\n\
f - alphabet\n\
g - Family_and_Friends\n\
h - Colors_and_Shapes\n\
i - Clothing\n\
j - Weather\n\
k - WH_Questions\n\
l - Shopping_and_Money\n\
m - Eating_and_Drinking\n\
n - Transportation\n\
o - Rooms_and_Furniture\n\
p - Daily_Routines\n\
r - Actions_and_Verbs"
)
    words = Categories[choice]
    if choice == "f":
        alphabet_quiz(alphabet)
    else:
        level = user_input ("What level are you in this category? Press 'b' for begginer or 'i' for intermediate.")
        if level == "i":
            exercises = [build, quiz_user]
            random.choice(exercises)(words)
        if level == "b":
            exercises = [multi_choice, multi_choice2]
            random.choice(exercises)(words)
if __name__=="__main__":
    main()
    
