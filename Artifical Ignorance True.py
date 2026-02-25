import random

print("HSEU Artifical Ignorance V1.1")

mathh = ["67...i think", "2001", "1+1=2", "Yes"]
history = ["Alexander The Ungreat", "2067", "1453", "September 11th", "Yes"]
geography = ["All roads lead to Rome", "Your house", "My house", "Niger", "Yes"]
helpp = ["I don't know", "Ever try turning reality off then on again?", "Ok", "Yes"]

math_keywords = ["add", "subtract", "minus", "divide", "multiply", "times", "plus", "sum", "difference", "product", "quotient", "calculate", "what is", "equals", "squared", "square root", "percent", "fraction", "solve", "total"]
history_keywords = ["who was", "when did", "what happened", "why did", "history", "war", "battle", "president", "king", "queen", "empire", "revolution", "century", "ancient", "historical", "founded", "invented", "discovery", "treaty", "dynasty", "year"]
geography_keywords = ["where is", "capital", "country", "continent", "ocean", "river", "mountain", "population", "city", "located", "border", "largest", "smallest", "island", "desert", "lake", "map", "region", "territory", "flag"]
help_keywords = ["help", "how do i", "how do you", "what is", "explain", "what does", "how to", "can you", "show me", "tell me", "what are", "guide", "assist", "support", "instructions", "tutorial", "tips", "advice"]

while True: 
    print("Ask me ANY question (or type quit to exit and spare me)")
    question = input("I'll get it wrong: ")

    if any(word in question for word in math_keywords):
        print(random.choice(mathh))
    elif any(word in question for word in history_keywords):
        print(random.choice(history))
    elif any(word in question for word in geography_keywords):
        print(random.choice(geography))
    elif any(word in question for word in help_keywords):
        print(random.choice(helpp))
    elif question == "quit":
        print("Goodbye! I was wrong about it all and proud to be")
    else:
     print("I have no idea what you're talking about.")

#This is version 2 of the code
#The 1st version can be found at: https://www.online-python.com/d4PUymGzax
