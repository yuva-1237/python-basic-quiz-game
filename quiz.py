import turtle

screen = turtle.Screen()
screen.title("Python Quiz Game")
screen.bgcolor("limegreen")

quiz = turtle.Turtle()
quiz.hideturtle()
quiz.penup()
quiz.goto(-200, 100)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-200, 200)

questions = [
    ["Who created Python?", "Guido Van Rossum"],
    ["When was  Python created?", "1991"],
    ["What is the data type for whole numbers?", "int"],
    ["What keyword starts a conditional statement?", "if"],
    ["What function displays output to the console?", "print"],
    ["What is a sequence enclosed in parentheses?", "tuple"],
    ["What is the operator for checking equality?", "=="],
    ["What is a sequence enclosed in square brackets?", "list"],
    ["What keyword starts a function definition?", "def"],
    ["How do you write a single-line comment in Python?", "#"]
]

score = 0

for q in questions:
    quiz.clear()
    quiz.write(q[0], font=("Verdana", 18, "bold"))
    answer = screen.textinput("Your Answer", q[0])

    if answer and answer.strip().lower() == q[1].lower():
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: " + str(score), font=("Verdana", 16, "bold"))

quiz.clear()
quiz.goto(-100, 0)
quiz.write("Quiz Over!\nFinal Score: " + str(score), font=("Verdana", 20, "bold"))

turtle.done()
