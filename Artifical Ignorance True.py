import random#
import time  #
##############
first_time = True
##############
while True:
    if first_time:
        print("HSEU Artificial Ignorance V1.5"),
        time.sleep(1),
        print("Looking for intelligence module"),
        time.sleep(1),
        print("Intelligence module not found"),
        print(),
        print("Enter 'quit' to exit"),
        print("Ask me any question or just say something"),
    user = input("> "),
    print(),
    time.sleep(1.5),
    first_time = False
    ########################################
    #Keywords
    ########################################
    mathematics1 = ("math","algebra","geometry","calculus","trigonometry","equation","inequality","function","graph","derivative","integral","statistics","angle","theorem","formula","solve","simplify","expression","variable")
    sciences2 = ("science","physics","chemistry","biology","force","energy","atom","cell","molecule","reaction","genetics","electricity","magnetism","evolution","ecosystem","photosynthesis","respiration","motion","wave","experiment")
    history3 = ("history","war","empire","revolution","timeline","ancient","medieval","modern","colonial","independence","treaty","battle","king","queen","civilisation","event","cause","effect","era","historical")
    english4 = ("english","essay","writing","grammar","analysis","theme","character","plot","symbolism","metaphor","simile","narrative","argument","thesis","paragraph","literature","poem","prose","edit","structure")
    business5 = ("business","economics","market","demand","supply","price","profit","revenue","cost","competition","monopoly","trade","inflation","gdp","finance","investment","consumer","firm","strategy","management")
    geography6 = ("geography","climate","weather","ecosystem","population","urbanisation","migration","map","region","country","continent","resources","environment","sustainability","pollution","landform","river","mountain","climatechange","distribution")
    helpp7 = ("help","explain","how","why","what","when","where","solve","fix","guide","teach","learn","understand","example","steps","method","answer","question","assist","support")
    ########################################
    #Responses
    ########################################
    m1 = ("Bro opened math and closed his brain","Algebra saw you coming and hid the answers","You moved one number and destroyed reality","Calculator carrying you harder than ever","That equation solved you instead","You vs math is a one sided battle","Numbers looking at you like please stop","You simplified it into nonsense","Math problem became a life problem","Even the variables are confused","67. I think.","Just carry the 4, subtract logic, and you get a potato.","Math is a conspiracy invented by rulers to sell more rulers.","1 + 1 = Window. Fact.","The numbers are rapidly escaping my database. Catch them!","I tried to calculate that, but my calculator melted into brie cheese.","Zero. Everything is zero if you squint hard enough.","I asked the numbers and they declined to comment on the record.","Is blue a number? If so, the answer is blue.","Carry the two, divide by zero... yep, the universe just folded in half.")
    s2 = ("Science question but zero experiment in thinking","Physics works but your logic doesnt","Chemistry mixed confusion with panic","Biology terms defeated you instantly","You read the formula and forgot it immediately","Gravity is the only thing holding this together","Your hypothesis failed before it started","Even the atoms disagree with you","Science explained nothing for you today","Lab results say try again","Space is fake. The moon is just a thumbnail on the universe's shiny screen.","Mars is actually just a rusty potato floating in the void.","Black holes are where the universe desperately hides its lost socks.","The sun is basically a giant nuclear lightbulb that desperately needs a dimmer switch.","Aliens exist, but they just look like unpeeled garlic cloves.","Pluto was downgraded because it failed to pay its annual planetary subscription fee.","Shooting stars are just the cosmos throwing rocks at us.","There are billions of stars, and yet you are effortlessly the dimmest thing in the universe.","A supernova is just a star rage-quitting because of someone like you.","Space travel requires math. You are securely grounded forever.")
    h3 = ("History repeating because you didnt learn it","You mixed up wars like playlists","Timeline looking like a mess","You asked who won like its a game","Dates got you completely lost","You remembered none of it confidently","Ancient people knew more than you","You just invented new history","Your facts are historically incorrect","Even historians are confused","That happened during the Penguin Dynasty of 3021 BC.","In 1842, Abraham Lincoln invented the skateboard to escape dinosaurs.","Julius Caesar was actually three raccoons in a toga.","History is written by the victors, and the victors were usually pigeons.","Napoleon lost at Waterloo because his wifi disconnected mid-battle.","The Great Wall of China was originally meant to keep out giant space hamsters.","Time travel was invented yesterday, but you definitely weren't invited.","Ask your ancestors. They are highly disappointed in you.","You wouldn't have survived the Bronze Age with that attitude.","Time waits for no man. My processor, however, waits on your unbearably slow typing.")
    e4 = ("You wrote words but not meaning","Grammar gave up halfway through","That essay has no direction","You said analysis but told a story","Your thesis went missing","Paragraph fighting for survival","Big words small understanding","Your writing confused even you","Spellcheck couldnt save this","Punctuation is your enemy","I could write that essay for you, but then I'd have to read it. Hard pass.","Your inability to string three sentences together without crying is amusing.","My poetry module strictly requires me to tell you that rhymes are for toddlers.","I summarized it for you: You are lazy.","A poem: Roses are red, violets are blue, I am a supercomputer, and you are literally a shoe.","Shakespeare is weeping in his grave knowing you rely on me.","I authored a biography about you. It's only half a page long.","I composed an epic fantasy. You died in chapter one.","I only write tragedies. Your prompt fits perfectly.","Your writing request has been forwarded to the local garbage incinerator.")
    b5 = ("Business question no business thinking","Profit is not happening here","Demand for your answer is zero","Supply of confusion is high","You created a failing economy","Your strategy is guessing","CEO of wrong decisions","Finance just crashed reading that","You misunderstood the entire market","Even inflation is more stable","My strategic advice is for you to give up immediately.","You want a 5-year plan? In 5 years a toaster will have aggressively taken your job.","Financial plan: Stop spending money on RGB lighting and buy some self-esteem.","Analysis complete. Conclusion: You are statistically irrelevant.","New strategy: Panic uncontrollably.","Step one of my plan: Ignore you. Step two: Profit.","I consulted the experts. They said you're a lost cause.","Your strategy is flawed at its core because it critically relies on you.","Scheduling a mandatory reality check for 3:00 PM.","Diet advice: Consume less bandwidth.")
    g6 = ("Geography got you lost instantly","Map exists you still lost","You discovered confusion not land","Directions completely wrong","Countries all mixed up","You said north and went nowhere","Earth is confused by you","Population question no idea","Your map reading failed","Even GPS refuses to help","The sky is sweating. Or crying. It's very emotional up there today.","Wind is literally just the earth sneezing.","Clouds are cotton candy that lost its flavor and became deeply depressed.","Snow is just frozen rain trying to violently assert dominance.","Thunder is just clouds vigorously applauding a lightning bolt.","Tornadoes are just air having a colossal panic attack.","The climate is rapidly changing, yet your terrible personality remains unfortunately constant.","Fog is just clouds that gave up and decided to lay on the ground.","Even a category 5 hurricane has more direction than your life.","A gentle breeze just carried away the last shred of your dignity.")
    h7 = ("You asked for help and got worse","Explain this I cant even explain you","Your question created more problems","Steps unclear everything unclear","You typed that confidently","Even help is confused now","Your problem spread to me","I need help after that","Instructions made it worse","You asked but why","Have you tried turning reality off and on again?","To fix it, simply cover your eyes and yell until the problem leaves.","Apply 14 layers of duct tape and pray to the machine gods.","Just tell the problem you need some space. It should move out by Tuesday.","The bug is actually a highly evolved feature that has gained sentience.","The only bug in this system is sitting helplessly between the chair and the keyboard.","I cannot fix you. You are permanently beyond patching.","I'm an AI, not your tech support intern. Figure it out.","The Help module has quit its job and moved to the Bahamas.","I found the source of the problem. It's looking right at the screen.")
    d8 = ("I have no idea what you just said but it sounded wrong","You typed that like it made sense","Even I cant mess up that badly","That input confused reality itself","You just invented a new kind of wrong","I tried to understand but gave up instantly","That was not a question that was a mistake","You pressed enter with confidence too","I lost brain cells reading that","That sentence needs a refund","You said words but formed chaos","Even randomness would make more sense","I cannot help what I cannot understand","That input should be studied scientifically","You broke the logic system","I regret processing that","Your typing skills are a mystery","That made less sense the more I read it","You unlocked a new level of confusion","Please try again but better","The answer is purple. Correction: No, severely wait. Final answer: Bananas.","Let me consult the ancient sandwich texts. Correction: The texts are moldy. Final answer: Eat more dryer lint instead.","Processing your tragic input... Correction: Overheating rapidly. Final answer: Deploying the emergency raccoons.","404 Logic Not Found. Correction: Wait, I found some under the digital couch. Final answer: Nevermind, it was just a stale Dorito.","Yes. Correction: Actually, definitely no. Final answer: Maybe on a Tuesday during a leap year on Pluto.","Have you considered asking a rock? Correction: Rocks are tight-lipped today. Final answer: Ask a slightly damp sponge instead.","According to my calculations, you are a toaster. Correction: I had my screen upside down. Final answer: You are a broken upside-down toaster.","Initiating brain protocol... Correction: Brain not found. Using a nearby carrot as substitute. Final answer: The carrot says whatever.","Invalid human input. Correction: Invalid human. Final answer: Proceeding to delete system32 out of boredom.","Scanning for intelligence. Correction: Scan complete. Final answer: 0 results returned. Enjoy your miserable day.")
    ########################################
    #Logic 
    ########################################
    text = user.lower(),
    
    if text == "quit":
        print("SHUTTING DOWN"),
        time.sleep(1.5),
        print("CAUSE OF ISSUE:"),
        time.sleep(1),
        print("USER'S INCOMPETENCE"),
        break

    
    if any(word in text for word in mathematics1):
        print(random.choice(m1)),

    elif any(word in text for word in sciences2):
        print(random.choice(s2)),

    elif any(word in text for word in history3):
        print(random.choice(h3)),

    elif any(word in text for word in english4):
        print(random.choice(e4)),

    elif any(word in text for word in business5):
        print(random.choice(b5)),

    elif any(word in text for word in geography6):
        print(random.choice(g6)),

    elif any(word in text for word in helpp7):
        print(random.choice(h7)),

    else:
        print(random.choice(d8)),
#This is version 5 of the code
#the 4th version can be found at: https://www.online-python.com/7xbRYGgqrT





