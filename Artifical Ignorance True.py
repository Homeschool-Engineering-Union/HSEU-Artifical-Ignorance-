import random#
import time  #
##############
first_time = True

while True:
    if first_time:
        print("HSEU Artificial Ignorance V1.3")
        time.sleep(1)
        print("Looking for intelligence module")
        time.sleep(1)
        print("Intelligence module not found")
        print()
        print("Enter 'quit' to exit")
        print("Ask me any question or just say something")
    user = input("> ")
    print()
    time.sleep(1.5)
    first_time = False

    ########################################
    #Keywords
    ########################################
    mathematics1 = ["math","algebra","geometry","calculus","trigonometry","equation","inequality","function","graph","derivative","integral","statistics","angle","theorem","formula","solve","simplify","expression","variable"]
    sciences2 = ["science","physics","chemistry","biology","force","energy","atom","cell","molecule","reaction","genetics","electricity","magnetism","evolution","ecosystem","photosynthesis","respiration","motion","wave","experiment"]
    history3 = ["history","war","empire","revolution","timeline","ancient","medieval","modern","colonial","independence","treaty","battle","king","queen","civilisation","event","cause","effect","era","historical"]
    english4 = ["english","essay","writing","grammar","analysis","theme","character","plot","symbolism","metaphor","simile","narrative","argument","thesis","paragraph","literature","poem","prose","edit","structure"]
    business5 = ["business","economics","market","demand","supply","price","profit","revenue","cost","competition","monopoly","trade","inflation","gdp","finance","investment","consumer","firm","strategy","management"]
    geography6 = ["geography","climate","weather","ecosystem","population","urbanisation","migration","map","region","country","continent","resources","environment","sustainability","pollution","landform","river","mountain","climatechange","distribution"]
    helpp7 = ["help","explain","how","why","what","when","where","solve","fix","guide","teach","learn","understand","example","steps","method","answer","question","assist","support"]

    ########################################
    #Responses
    ########################################
    m1 = ["Bro opened math and closed his brain","Algebra saw you coming and hid the answers","You moved one number and destroyed reality","Calculator carrying you harder than ever","That equation solved you instead","You vs math is a one sided battle","Numbers looking at you like please stop","You simplified it into nonsense","Math problem became a life problem","Even the variables are confused"]
    s2 = ["Science question but zero experiment in thinking","Physics works but your logic doesnt","Chemistry mixed confusion with panic","Biology terms defeated you instantly","You read the formula and forgot it immediately","Gravity is the only thing holding this together","Your hypothesis failed before it started","Even the atoms disagree with you","Science explained nothing for you today","Lab results say try again"]
    h3 = ["History repeating because you didnt learn it","You mixed up wars like playlists","Timeline looking like a mess","You asked who won like its a game","Dates got you completely lost","You remembered none of it confidently","Ancient people knew more than you","You just invented new history","Your facts are historically incorrect","Even historians are confused"]
    e4 = ["You wrote words but not meaning","Grammar gave up halfway through","That essay has no direction","You said analysis but told a story","Your thesis went missing","Paragraph fighting for survival","Big words small understanding","Your writing confused even you","Spellcheck couldnt save this","Punctuation is your enemy"]
    b5 = ["Business question no business thinking","Profit is not happening here","Demand for your answer is zero","Supply of confusion is high","You created a failing economy","Your strategy is guessing","CEO of wrong decisions","Finance just crashed reading that","You misunderstood the entire market","Even inflation is more stable"]
    g6 = ["Geography got you lost instantly","Map exists you still lost","You discovered confusion not land","Directions completely wrong","Countries all mixed up","You said north and went nowhere","Earth is confused by you","Population question no idea","Your map reading failed","Even GPS refuses to help"]
    h7 = ["You asked for help and got worse","Explain this I cant even explain you","Your question created more problems","Steps unclear everything unclear","You typed that confidently","Even help is confused now","Your problem spread to me","I need help after that","Instructions made it worse","You asked but why"]
    d8 = ["I have no idea what you just said but it sounded wrong","You typed that like it made sense","Even I cant mess up that badly","That input confused reality itself","You just invented a new kind of wrong","I tried to understand but gave up instantly","That was not a question that was a mistake","You pressed enter with confidence too","I lost brain cells reading that","That sentence needs a refund","You said words but formed chaos","Even randomness would make more sense","I cannot help what I cannot understand","That input should be studied scientifically","You broke the logic system","I regret processing that","Your typing skills are a mystery","That made less sense the more I read it","You unlocked a new level of confusion","Please try again but better"]

    ########################################
    #Logic 
    ########################################
    text = user.lower()
    
    if text == "quit":
        print("SHUTTING DOWN")
        time.sleep(1.5)
        print("CAUSE OF ISSUE:")
        time.sleep(1)
        print("USER'S INCOMPETENCE")
        break

    
    if any(word in text for word in mathematics1):
        print(random.choice(m1))

    elif any(word in text for word in sciences2):
        print(random.choice(s2))

    elif any(word in text for word in history3):
        print(random.choice(h3))

    elif any(word in text for word in english4):
        print(random.choice(e4))

    elif any(word in text for word in business5):
        print(random.choice(b5))

    elif any(word in text for word in geography6):
        print(random.choice(g6))

    elif any(word in text for word in helpp7):
        print(random.choice(h7))

    else:
        print(random.choice(d8))
#This is version 4 of the code
#the 3rd version can be found at: https://www.online-python.com/2yr5mt1W0C
