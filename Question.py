from ClassQuestion import Question

question_prompts = [
    "What colour are bananas?\n(a)Red\n(b)Purple\n(c)Yellow\n",
    "What colour are apples?\n(a)Yellow\n(b)Purple\n(c)Red\n"
]

questions = [(question_prompts[0],"c"),
question_prompts[1],"c"
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score+=1
    print("you got "+ str(score)+ "/"+str(len(questions)) + " correct")

run_test(questions)