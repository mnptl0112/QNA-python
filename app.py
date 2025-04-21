questions = ["What is your fav color?","how is the whether?","whats up?"]
answers = ['black','good','nice']
sum=0
for que in questions:
    ans = input(print(que))
    for an in answers:
        if ans == an:
            print("correct answer")
            sum +=10
            break
    else:
        print('wrong answer')
print(F'you have won {sum}, which is your!!\ncongrats!!')
