question_list = [

    "How many continents are there?",              # pehla question

    "What is the capital of India?",            # doosra question

    "NG mei kaun se course padhaya jaata hai?" ,   # teesra question

    "which state of india has no shortest coastline?"   #fourth question

]

options_list = [

    ["Four", "Nine", "Seven", "Eight"],

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],

    ["maharastra","goa","odisa","west bangal"]
]

solution_list = [3, 4, 1, 2]

i=0
print("welcome !To caun banega cadepati(kbc):")
while i<len(question_list):
    print("your question is:")
    print(question_list[i])
    print("your option is:")
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j+=1
    op=int(input("Enter correct option number: "))
    if op == solution_list[i]:
        print("  well play !.your answer is Correct: ")
    else:
        print("Incorrect answer.")
        break
    i=i+1
print("congratulations 🥳!")



