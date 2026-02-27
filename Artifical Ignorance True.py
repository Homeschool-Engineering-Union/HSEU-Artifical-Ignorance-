import random

print("HSEU Artificial Ignorance V1.1")

mathh = ("67...i think", "2001", "1+1=2", "Yes")

history = ("Alexander The Ungreat", "2067", "1453", "September 11th", "Yes")

geography = ("All roads lead to Rome", "Your house", "My house", "Niger", "Yes")

helpp = ("I don't know", "Ever try turning reality off then on again?", "Ok", "Yes")

science = ("The mitochondria... probably", "Gravity is just a suggestion", "Yes, that's definitely a molecule", "Electrons are just vibes", "Because science said so", "It explodes. Everything explodes.", "Yes")

english = ("Shakespeare wrote that, or was it Shrek?", "A noun is a feeling", "Just add a comma and hope for the best", "The theme is sadness. Always sadness.", "Yes, that's definitely a metaphor", "It means whatever you want it to mean", "Yes")

cs = ("Have you tried turning it off and on again?", "Just delete System32", "It's always a Python problem", "The bug is somewhere in the code", "Try Ctrl+Z until it works", "404: Answer not found", "Yes")



math_keywords = ["add", "subtract", "minus", "divide", "multiply", "times", "plus", "sum", "difference", "product", "quotient", "calculate", "what is", "equals", "squared", "square root", "percent", "fraction", "solve", "total", "average", "mean", "median", "mode", "prime", "factor", "exponent", "power", "root", "algebra", "geometry", "trigonometry", "calculus", "equation", "formula", "number", "digit", "integer", "decimal", "+", "-", "*", "/", "=", "%", "^", "x2", "sqrt"]

history_keywords = ["who was", "when did", "what happened", "why did", "history", "war", "battle", "president", "king", "queen", "empire", "revolution", "century", "ancient", "historical", "founded", "invented", "discovery", "treaty", "dynasty", "year", "civilization", "medieval", "renaissance", "colonial", "independence", "constitution", "election", "politician", "general", "soldier", "conflict", "invasion", "occupation", "liberation", "assassination", "parliament", "government", "republic", "monarchy", "dictator", "communist", "fascist", "world war", "cold war", "bc", "ad", "decade", "era", "period", "age"]

geography_keywords = ["where is", "capital", "country", "continent", "ocean", "river", "mountain", "population", "city", "located", "border", "largest", "smallest", "island", "desert", "lake", "map", "region", "territory", "flag", "timezone", "latitude", "longitude", "coordinates", "north", "south", "east", "west", "hemisphere", "equator", "pole", "arctic", "antarctic", "rainforest", "jungle", "savanna", "tundra", "volcano", "earthquake", "climate", "weather", "bay", "gulf", "strait", "peninsula", "plateau", "valley", "canyon", "waterfall", "sea", "coast", "beach", "port", "village", "town", "state", "province", "district"]

science_keywords = ["atom", "molecule", "cell", "biology", "chemistry", "physics", "element", "compound", "reaction", "energy", "force", "gravity", "mass", "weight", "velocity", "acceleration", "momentum", "wave", "light", "sound", "heat", "temperature", "electric", "magnetic", "nucleus", "electron", "proton", "neutron", "dna", "gene", "evolution", "species", "ecosystem", "photosynthesis", "mitosis", "osmosis", "acid", "base", "ph", "density", "pressure", "volume", "experiment", "hypothesis", "theory", "lab", "microscope", "planet", "star", "galaxy", "orbit", "atmosphere"]

english_keywords = ["poem", "essay", "novel", "book", "author", "write", "writing", "grammar", "punctuation", "sentence", "paragraph", "metaphor", "simile", "alliteration", "theme", "plot", "character", "setting", "narrative", "fiction", "nonfiction", "verb", "noun", "adjective", "adverb", "pronoun", "clause", "synonym", "antonym", "vocabulary", "spelling", "read", "reading", "literature", "shakespeare", "sonnet", "stanza", "rhyme", "tone", "mood", "imagery", "symbolism", "foreshadowing", "irony", "sarcasm", "quote", "citation", "thesis", "conclusion", "introduction"]

cs_keywords = ["code", "coding", "program", "programming", "python", "java", "javascript", "html", "css", "algorithm", "function", "variable", "loop", "array", "list", "class", "object", "debug", "error", "bug", "compile", "run", "execute", "database", "sql", "server", "network", "internet", "website", "app", "software", "hardware", "cpu", "ram", "binary", "bit", "byte", "input", "output", "terminal", "command", "script", "library", "framework", "api", "git", "computer", "keyboard", "mouse", "operating system", "linux", "windows", "mac", "if statement", "syntax"]

help_keywords = ["help", "how do i", "how do you", "explain", "what does", "how to", "can you", "show me", "tell me", "what are", "guide", "assist", "support", "instructions", "tutorial", "tips", "advice", "teach me", "i dont understand", "i don't understand", "confused", "lost", "stuck", "what should", "where do i", "why is", "when should", "who should", "is it possible", "could you", "would you", "please", "help me", "i need", "struggling", "difficult", "hard", "easy", "simple", "quick", "fast"]

while True:
    print("Ask me ANY question (or type quit to exit and spare me)")
    question = input("I'll get it wrong: ").lower()

    if question in ("quit", "exit", "bye"):
        print("Goodbye! I was wrong about it all and proud to be.")
        break
    elif any(word in question for word in math_keywords):
        print(random.choice(mathh))
    
    elif any(word in question for word in history_keywords):
        print(random.choice(history))
    
    elif any(word in question for word in geography_keywords):
        print(random.choice(geography))
    
    elif any(word in question for word in science_keywords):
        print(random.choice(science))
    
    elif any(word in question for word in english_keywords):
        print(random.choice(english))
    
    elif any(word in question for word in cs_keywords):
        print(random.choice(cs))
    
    elif any(word in question for word in help_keywords):
        print(random.choice(helpp))
    else:
        print("I have no idea what you're talking about.")
        
#This is version 3 of the code
#the 2nd version can be found at: https://www.online-python.com/y5xZkS9NXT 
