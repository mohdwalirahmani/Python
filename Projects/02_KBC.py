# KBC
questions = [
    ["1. Who is known as the father of Computer?", "Charles Babbage", "Alan Turing", "Dennis Ritchie", "Bill Gates", 1],
    ["2. What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3],
    ["3. Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["4. Who wrote the national anthem of India?", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Subhash Chandra Bose", 1],
    ["5. Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["6. What is the largest ocean on Earth?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["7. Who invented the light bulb?", "Albert Einstein", "Nikola Tesla", "Thomas Edison", "Isaac Newton", 3],
    ["8. Which country hosted the FIFA World Cup 2022?", "Brazil", "Russia", "Qatar", "Germany", 3],
    ["9. What is the chemical symbol for Gold?", "Au", "Ag", "Go", "Gd", 1],
    ["10. Which is the longest river in the world?", "Amazon", "Nile", "Ganga", "Yangtze", 2]
]

levels = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 130000, 150000, 200000]

money = 0
for i in range (0, len(questions)):
    ques = questions[i]
    print(f"\n\nQues for Rs. {levels[i]}")
    print(f"\n{ques[0]}")
    print(f"a. {ques[1]}           b. {ques[2]}")
    print(f"c. {ques[3]}           d. {ques[4]}")
    while True:
        try:
            reply = int(input("Enter your option (1-4): "))
            if reply < 1 or reply > 4:
                print("Invalid option! Choose between 1 to 4 only.")
                continue
            break
        except ValueError:
            print("Please enter a NUMBER (1-4), not text.")

    if reply == ques[-1]:
        print(f"Correct! You won Rs {levels[i]}")
        if i == 3:
            money = 10000
        elif i == 7:
            money = 130000
        elif i == 9:
            money = 200000
    else:
        print("Wrong answer! Game over.")
        break

print(f"\nYou take home Rs {money}")