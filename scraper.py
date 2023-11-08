from selenium import webdriver
import time
from playsound import playsound

def sound():
    playsound(r"C:\Users\Thej Venkat\Desktop\Projects\Trivia\sound\snd1.mp3")

from selenium.webdriver.common.by import By
tgvt={"site":"https://www.wizard101.com/quiz/trivia/game/tenth-grade-vocabulary-trivia","Malicious":"wishing evil or harm upon others","Malcontent":"person dissatisfied with existing state of affairs","Dialogue":"a conversation between two persons","Injunction":"a formal command or admonition","Phonetic":"related to the sounds in a language","Malevolent":"wishing or appearing to wish evil to others","Juncture":"a joining together; the point at which two things are joined; any important point in time","Congregate":"To come together in a group, assemble.","Malady":"a sickness, illness, disease, disorder","Segregate":"separating into different groups","Adjunct":"something attached to but holding an inferior position","Gregarious":"seeking and enjoying the company of others","Soliloquy":"the act of talking to oneself or a dramatic monologue","Junction":"an act of joining or adjoining things","Eloquent":"expressing yourself readily, clearly, effectively"}
egvt={'site':'https://www.wizard101.com/quiz/trivia/game/eleventh-grade-vocabulary-trivia', 'Conceit': "an excessively favorable opinion of one's own ability, importance or wit", 'Buoyancy': 'the power to float or rise in a fluid, the upward pressure exerted by the fluid in which a body is immersed', 'Anecdote': 'a short account of a particular incident or event of an interesting or amusing nature, often biographical.', 'Assuage': 'to relieve or soothe', 'Annotated': 'supplied with or containing explanatory notes and textual comments', 'Discern': 'to recognize the difference', 'Allegory': 'a representation of an abstract or spiritual meaning through concrete or material forms', 'Auspicious': 'favorable, noteworthy', 'Ambiguity': 'doubtfulness or uncertainty of meaning or intention', 'Quandary': 'a state of perplexity or uncertainty', 'Conspicuous': 'noticeable, obvious', 'Euphemism': 'the substitution of a mild, indirect, or vague expression for one thought to be offensive, harsh, or blunt', 'Denotation': 'a word that names or signifies something specific', 'Principle': 'a fundamental, primary, or general law or truth from which others are derived', 'Enigma': 'a mystery', 'Procure': 'to obtain'}
ngvt={'site':'https://www.wizard101.com/quiz/trivia/game/ninth-grade-vocabulary-trivia', 'Recalcitrant': 'marked by stubborn resistance to authority', 'Heed': 'paying particular notice (as to children or helpless people)', 'Deference': 'a disposition or tendency to yield to the will of others', 'Guile': 'shrewdness as demonstrated by being skilled in deception', 'Censure': 'harsh criticism or disapproval', 'Inadvertent': 'without intention (especially resulting from heedless action)', 'Abstract': 'a concept or idea not associated with any specific instance', 'Advocate': 'a person who pleads for a cause or propounds an idea', 'Belittle': 'lessen the authority, dignity, or reputation of', 'Facilitate': 'make easier', 'Parsimony': 'extreme care in spending money', 'Mar': "a mark or flaw that spoils the appearance of something (especially on a person's body)", 'Verbose': 'using or containing too many words', 'Eccentric': 'a person of a specified kind (usually with many eccentricities)', 'Tangible': 'possible to be treated as fact', 'Comply': "act in accordance with someone's rules, commands, or wishes"}
cet={'site':'https://www.wizard101.com/quiz/trivia/game/chemical-elements-trivia', "The symbol 'Co' refers to which chemical element?": 'Cobalt', 'This element when combined with Chlorine makes table salt.': 'Na', 'This element is the building block of life.': 'C', "The symbol 'F' refers to which chemical element?": 'Fluorine', 'Which of these elements is considered a Metal.': 'Fe', 'This element was discovered by Hans Christian Oersted in 1825.': 'Al', "Most of the earth's atmosphere consists of this gas.": 'N', "The symbol 'Cu' refers to which chemical element?": 'Copper', 'This element was discovered by Joseph Priestly and Carl Scheele in 1774.': 'O', 'Which of these elements is NOT considered a Noble Gas.': 'H', "The symbol 'S' refers to which chemical element?": 'Sulfur', 'What is the symbol for Potassium?': 'K', 'This element helps give plants the energy they need to grow.': 'P', 'Which element has a reddish color in a gas and liquid state?': 'Br', 'Which of these elements is NOT considered a Metalloid.': 'Sn', 'Which element has a silver-gray appearance?': 'Zn', "The symbol 'Pb' refers to which chemical element?": 'Lead', "The symbol 'H' refers to which chemical element?": 'Hydrogen', "The symbol 'Au' refers to which chemical element?": 'Gold', 'This element was discovered in 1808.': 'B'}
sst={'site':'https://www.wizard101.com/quiz/trivia/game/solar-system-trivia', 'Which planet is closest to the sun?': 'Mercury', 'Every object in our solar system revolves around the _______.': 'Sun', 'What is the correct term for Pluto?': 'Dwarf Planet', 'How many planets are in our solar system?': 'Eight', 'Which is the smallest planet in the solar system?': 'Mercury', 'What are comets made of?': 'Dirty Ice', "Venus' atmosphere is primarily made up of what gas?": 'Carbon Dioxide', 'Jupiter has a ________ in its atmosphere but no solid surface.': 'Hurricane', 'What separates the inner and outer solar system?': 'Band of asteroids', 'What is the largest planet in the solar system?': 'Jupiter', 'Mars is known as the _____ planet.': 'Red', 'Uranus has a _______ glow to it.': 'Blue', 'Which two planets are Earth\'s "neighbors"?': 'Venus & Mars', 'What man-made objects exist in our solar system?': 'Satellites & Space Junk', 'Which planet is furthest from the sun?': 'Neptune', 'Saturn is famous for its ________ that rotate around it.': 'Rings'}
twvt={'site':'https://www.wizard101.com/quiz/trivia/game/twelfth-grade-vocabulary-trivia', 'Deleterious': 'harmful to living things', 'Sensuous': 'all senses, dealing w/ all senses', 'Antithesis': 'the direct opposite or contrast to a previously given assertion', 'Jovial': 'happy, cheery', 'Benevolent': 'showing or motivated by sympathy and understanding and generosity', 'Enervate': 'to weaken, or to take energy from', 'Guru': 'religious teacher', 'Chicanery': 'deceiving someone, scam', 'Impetuous': 'characterized by undue haste and lack of thought or deliberation', 'Hegemony': 'one country/group has leadership over another', 'Fortuitous': 'occurring by happy chance', 'Brazen': 'unrestrained by convention or propriety', 'Evanescent': 'tending to vanish like vapor', 'Conundrum': 'a difficult problem', 'Peruse': 'reading with careful attention', 'Loquacious': 'talkative, chatty'}
dt={'site':'https://www.wizard101.com/quiz/trivia/game/dinosaur-trivia', 'In what period did the Coelophysis live?': 'Late Triassic', 'In what period did the Tyrannosaurus live?': 'Late Cretaceous', 'In what period did the Triceratops live?': 'Late Cretaceous', 'Which of these is not a dinosaur?': 'Pterodactyl', "What does the name 'Triceratops' mean?": 'three-horned face', 'In what period did the Stegosaurus live?': 'Late Jurassic', 'Which carnivorous dinosaur had teeth up to 8 inches long?': 'Tyrannosaurus', 'In what era did dinosaurs live?': 'Mesozoic', 'When did dinosaurs become extinct?': '65 million years ago', 'The largest dinosaurs were __________________.': 'Sauropods', 'Dinosaurs belonged to which group of animals?': 'Reptiles', 'In what period did the Diplodocus live?': 'Late Jurassic', 'Which dinosaur had hollow limb bones?': 'Coelophysis', 'What caused the extinction of dinosaurs according to scientists?': 'Scientists are not 100% sure. There is still heavy debate.', 'Which of the following was not a flying reptile?': 'Stegosaurus', "What does the word 'dinosaur' mean?": 'Large Reptile', 'Which dinosaur most closely resembles a rhinoceros?': 'Triceratops', 'Which dinosaur had a long neck to help reach high and low vegetation?': 'Diplodocus', "Who coined the term 'dinosauria?'": 'Sir Richard Owen', 'What profession studies dinosaur fossils?': 'Paleontologist'}
wmt={'site':'https://www.wizard101.com/quiz/trivia/game/wizard101-marleybone-trivia', "Which is not a street in Regent's Square?": 'Fleabitten Ave', "What is flying around in Regent's Square?": 'Newspapers', 'What color are the Marleybone mailboxes?': 'Red', 'What event is Abigail Doolittle sending out invitations for?': "Policeman's Ball", 'Who is the dangerous criminal that is locked up, but escapes from Newgate Prison?': 'Meowiarty', 'What course did Herold Digmoore study?': 'Ancient Myths for Parliament', "What initials were on the doctor's glove?": 'XX', 'What transports you from place to place in Marleybone?': 'Hot Air Balloons', 'What time of day is it always in Marleybone?': 'Night', "Which symbol is not on the stained glass window in Regent's Square?": 'A Tennis Ball', 'Which of these folks can you find in the Royal Museum?': 'Clancy Pembroke', 'What two names are on the Statues in the Marleybone cathedral?': 'Saint Bernard and Saint Hubert', 'What style of artifacts are in the Royal Museum?': 'Krokotopian', "What is Sgt. Major Talbot's full name?": 'Sylvester Quimby Talbot III', 'Arthur Wethersfield is A:..': 'Dog', "Who is not an officer you'll find around Marleybone?": 'Officer Digmore', 'What is a very common last name of the cats in Marleybone?': "O'Leary", 'What did Prospector Zeke lose in Marleybone?': 'The Stray Cats', 'What time does the clock always read in Marleybone?': '1:55', 'What sort of beverage is served in Air Dales Hideaway?': 'Root Beer'}
wct={'site':'https://www.wizard101.com/quiz/trivia/game/wizard101-wizard-city-trivia', "What is Mindy's last name (she's on Colossus Blvd)?": 'Pixiecrown', 'What are the school colors of Balance?': 'Tan and Maroon', 'What is the gemstone for Balance?': 'Citrine', 'Who taught Life Magic before Moolinda Wu?': 'Sylvia Drake', 'What is the name of the Ice Tree in Ravenwood?': 'Kelvin', 'What are the main colors for the Myth School?': 'Blue and Gold', 'Who sang the Dragons, Tritons and Giants into existance?': 'Bartleby', 'What is the name of the grandfather tree?': 'Bartleby', 'What is something that the Gobblers are NOT stockpiling in Colossus Way?': 'Broccoli', 'What is the name of the bridge in front of the Cave to Nightside?': 'Rainbow Bridge', "What is Diego's full name?": 'Diego Santiago Quariquez Ramirez the Third', 'What school is all about Creativity?': 'Storm', 'What is the name of the school newspaper? Boris Tallstaff knows...': 'Ravenwood Bulletin', 'Who is the Wizard City mill foreman?': 'Sohomer Sunblade', 'What does every Rotting Fodder in the Dark Caves carry with them?': 'A spade', 'What school does Malorn Ashthorn think is the best?': 'Death', 'Who is the Fire School professor?': 'Dalia Falmea', 'Who is the Princess of the Seraphs?': 'Lady Oriel', 'Who resides in the Hedge Maze?': 'Lady Oriel', 'Where is Sabrina Greenstar?': 'Fairegrounds'}
sct={'site':'https://www.wizard101.com/quiz/trivia/game/state-capitals-trivia', 'What is the capital of Indiana?': 'Indianapolis', 'What is the capital of New Hampshire?': 'Concord', 'What is the capital of Oregon?': 'Salem', 'What is the capital of Montana?': 'Helena', 'What is the capital of Alabama?': 'Montgomery', 'What is the capital of Michigan?': 'Lansing', 'What is the capital of Nevada?': 'Carson City', 'What is the capital of South Carolina?': 'Columbia', 'What is the capital of Rhode Island?': 'Providence', 'What is the capital of South Dakota?': 'Pierre', 'What is the capital of Iowa?': 'Des Moines', 'What is the capital of Virginia?': 'Richmond', 'What is the capital of West Virginia?': 'Charleston', 'What is the capital of Minnesota?': 'Saint Paul', 'What is the capital of Vermont?': 'Montpelier', 'What is the capital of California?': 'Sacramento', 'What is the capital of North Carolina?': 'Raleigh', 'What is the capital of Alaska?': 'Juneau', 'What is the capital of Kentucky?': 'Frankfort', 'What is the capital of Arizona?': 'Phoenix', 'What is the capital of Florida?': 'Tallahassee', 'What is the capital of Illinois?': 'Springfield', 'What is the capital of Utah?': 'Salt Lake City', 'What is the capital of Ohio?': 'Columbus', 'What is the capital of North Dakota?': 'Bismark', 'What is the capital of Kansas?': 'Topeka', 'What is the capital of Louisiana?': 'Baton Rouge', 'What is the capital of New Jersey?': 'Trenton', 'What is the capital of Arkansas?': 'Little Rock', 'What is the capital of Hawaii?': 'Honolulu', 'What is the capital of Georgia?': 'Augusta', 'What is the capital of Idaho?': 'Boise', 'What is the capital of Wisconsin?': 'Madison', 'What is the capital of Missouri?': 'Jefferson City', 'What is the capital of Mississippi?': 'Jackson', 'What is the capital of New York?': 'Albany', 'What is the capital of Pennsylvania?': 'Harrisburg', 'What is the capital of Wyoming?': 'Cheyenne', 'What is the capital of Tennessee?': 'Nashville', 'What is the capital of Maine?': 'Augusta', 'What is the capital of New Mexico?': 'Santa Fe', 'What is the capital of Colorado?': 'Denver', 'What is the capital of Oklahoma?': 'Oklahoma City', 'What is the capital of Texas?': 'Austin', 'What is the capital of Nebraska?': 'Lincoln', 'What is the capital of Maryland?': 'Annapolis', 'What is the capital of Massachusetts?': 'Boston', 'What is the capital of Washington?': 'Olympia', 'What is the capital of Delaware?': 'Dover'}

Dl=[tgvt,egvt,ngvt,cet,sst,twvt,dt,wmt,wct,sct]

driver = webdriver.Chrome(executable_path=r"C:\Users\Thej Venkat\Desktop\Projects\Trivia\chrome driver\chromedriver.exe")

newentry=False
#driver.maximize_window()

def newEntry(d,q):
    global newentry
    newentry=True
    i=4
    j=0
    ale=driver.find_elements(By.CLASS_NAME, 'answerText')
    l=[]
    for e in ale:
        l.append(e.text)
        print(j,":  ",e.text)
        j+=1
    while i not in range(0,4):
        i=int(input("Ans (0->3):"))
    d[q]=l[i]
    time.sleep(1)
    return i
def solve(d):
    global asb
    asb=False
    try:
        driver.get(d["site"])
        newentry=False
        for count in range(12):
            print("Count:",count)
            time.sleep(5.5)
            i=0
            q= driver.find_element(By.CLASS_NAME, 'quizQuestion').text
            if q not in d:
                print(q)
                sound()
                print("update q.")
                i=newEntry(d,q)
            a=d[q]
            ale=driver.find_elements(By.CLASS_NAME, 'answerText')
            for e in ale:
                e=e.text
                if e==a:
                    break
                i+=1
            #del next line
            if i==4:
                print("ans not found in dict.")
                i=newEntry(d,q)
                time.sleep(1)

            cbe=driver.find_elements(By.CLASS_NAME, 'largecheckbox')
            for e in cbe:
                if i==0:
                    e.click()
                    break
                i-=1
            nb=driver.find_element(By.ID,'nextQuestion')
            nb.click()
    except:
        asb=True
        if(input("Solve again(0:No)")!='0'):
            solve(d)
        else:
            print("Already Solved.")

def trivia():
    global asb,repeat,temp,newentry,n
    asb=False
    driver.get("https://www.wizard101.com/quiz/trivia/game/tenth-grade-vocabulary-trivia")
    
    while input("Login and Enter(0:No)")!='0':
        sound()
        print("Started")
        for elem in Dl[:]:
            asb=False
            newentry=False
            n=input("Solve?(0:No)")
            if n!='0':
                solve(elem)
            else:
                asb=True
            if newentry:
                sound()
                print("dict changed\n")
                print(elem)
                print("\nUpdate it.")
            sound()
            if not asb:
                print("Finished a Trivia")
                nqb=driver.find_element(By.CLASS_NAME, 'kiaccountsbuttongreen')
                nqb.click()
                time.sleep(2)
    time.sleep(5)
    driver.close()
trivia()
