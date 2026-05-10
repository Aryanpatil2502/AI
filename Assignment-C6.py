def knowledge_base():
    return {
        "Cold": ["sneezing", "cough"],
        "Fever": ["temperature", "weakness"],
        "Covid-19": ["cough", "temperature", "weakness"],
        "Flu": ["paleness", "temperature"],
        "Iron Deficiency": ["weakness", "paleness"]
    }

def questions():
    return {
        "sneezing": "Are you sneezing frequently?",
        "cough": "Do you have cough?",
        "temperature": "Do you have high temperature?",
        "weakness": "Are you feeling weak?",
        "paleness": "Does your skin look pale?"
    }

def ask(q):
    while True:
        ans = input(q + " (y/n): ").lower()
        if ans in ["y", "n"]:
            return ans == "y"   # FIXED
        print("Please enter y or n.")

def diagnose():
    print("\nWelcome to Smart Medical Expert System\n")

    symptoms_input = {}
    q_list = questions()

    # Collect user input
    for key, question in q_list.items():
        symptoms_input[key] = ask(question)

    kb = knowledge_base()
    scores = {}

    # Calculate matching score
    for disease, symptoms in kb.items():
        score = 0
        for sym in symptoms:
            if symptoms_input.get(sym):
                score += 1
        scores[disease] = score

    # Find best match
    max_score = max(scores.values())

    print("\nPossible Diagnosis:\n")

    found = False

    for disease, score in scores.items():
        if score == max_score and score > 0:
            print(f"{disease} (match score: {score})")
            found = True

    if not found:
        print("No matching disease found.")

diagnose()
