

question_list= [
    
    "How many continents are there?",              # first question

    "What is the capital of India?",            # second  question

    "NG mei kaun se course padhaya jaata hai?" ,   # third question

    "which state of india has no shortest coastline?" ,  #fourth question

    " which of these viruses taken it is name from a place  in malaysia?"
]

options_list = [

    ["Four", "Nine", "Seven", "Eight"],

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],

    ["maharastra","goa","odisa","west bangal"],

    ["nipah","ebola","influenia","HIV"]
]

solution_list = [3, 4, 1, 2,2]


answer=[["3.seven","4.eight"],["3.chennai","4.delhi"],["1.software enginearing","2. councealing"],["2. goa","3. odisa"],["4.HIV"  ,"2.ebola"]]

i=0
count=0
p=0
print("welcome 🙏!To caun banega cadepati(kbc):")
while i<len(question_list):
    print("your question is 😊 :")
    print(question_list[i])
    print("your option is 😀 :")
    j=0
    z=i
    while j<len(options_list[i]):
        print(options_list[i][j])
        j+=1
    c=input("do you want 50-50 lifeline 🙂:")

    if  c=="yes":
        print("accept")
        if count<1:
            print(answer[z])
            r=int(input("enter answer"))
            if r== solution_list[i]:
                print("  well play !.your answer is Correct: ")
                p=p+10000
                print(" you win" ,p,"🤩")
            else:
                print("Incorrect answer.",("\U0001F612"))
                print("win",p,"🤩")
                break
            count=count+1
        else:
            print("u already use lifeline")
            r2=int(input("enter answer"))
            if r2== solution_list[i]:
                print("  well play 🎊!.your answer is Correct: ")
                p=p+10000
                print(" you win",p,"🤩")
            else:
                print("Incorrect answer","😇")
                print(" you win",p,"🤩")
    else:
        r3=int(input("enter answer"))
        if r3==solution_list[i]:
            print("correct your answer  😎")
            p=p+10000
            print(" you winn",p,"🤩")
        else:
            print("wrong answer",("\U0001F612"))
            print(" you win",p,"🤩")
    i=i+1
print("you win total amount👍",p)
print("congratulations !,🥳🥳")
print("thankyou 😎! for participate in kbc:")
print("Game Over  🙏","\U0001F607")



