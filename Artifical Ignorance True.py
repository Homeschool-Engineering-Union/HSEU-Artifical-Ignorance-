from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This function will look for 'index.html' in the 'templates' folder
    return render_template('index.html', title='Home Page', message='Hello from Flask!')

if __name__ == '__main__':
    app.run(debug=True)


print("ARTIFICIAL IGNORANCE")
print("Intelligence module not found.")
print("Type quit to exit.")

while True:
    question = input("Ask me something: ").lower()
    
    if question == "quit":
        print("Shutting down... incorrectly.")
        break
        
    print("Thinking.")
    print("Thinking..")
    print("Thinking...")
    

    if "+" in question or "-" in question or "*" in question or "/" in question or "add" in question or "minus" in question:
        print("Final Answer: 67. I think.")
    
    
    elif "who" in question or "when" in question or "why" in question:
        print("Final Answer: That happened during the Penguin Dynasty of 3021 BC.")
    
    
    elif "help" in question or "fix" in question or "problem" in question:
        print("Final Answer: Have you tried turning reality off and on again?")
    
    else:
        print("Final Answer: The answer is purple.")
        print("Correction: No, wait.")
        print("Final Final Answer: Bananas.")

