from random import randint
from turtle import*

#Turtle 1 attributes
t = Turtle()
t.speed(0)
t.hideturtle()

#Turtle 2 attributes
t2 = Turtle()
t2.speed(0)
t2.hideturtle()

#Drawing the hangman
def draw_gallows():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.setheading(0)
    t.forward(200)
    t.back(100)
    t.setheading(90)
    t.forward(300)
    t.setheading(0)
    t.forward(100)
    t.right(90)
    t.forward(50)
    
def draw_head():
    t.right(90)
    t.circle(25)
    t.penup()
    t.right(270)
    t.penup()
    t.forward(50)
    
def draw_body():
    t.pendown()
    t.forward(100)
    
def draw_rleg():
    t.right(315)
    t.forward(75)
    
def draw_lleg():
    t.back(75)
    t.right(90)
    t.forward(75)
    
def draw_larm():
    t.back(75)
    t.right(135)
    t.forward(75)
    t.right(270)
    t.forward(75)
    
def draw_rarm():
    t.back(150)
    

def draw_hangman(limbs):
    if limbs == 0:
        draw_gallows()
    elif limbs == 1:
        draw_head()
    elif limbs == 2:
        draw_body()
    elif limbs == 3:
        draw_rleg()
    elif limbs == 4:
        draw_lleg()
    elif limbs == 5:
        draw_larm()
    elif limbs == 6:
        draw_rarm()

#Checks to see if guessed word is inside of the actual word
def update(word, dash, ch):
    matchmaker = 0
    z = 0
    while z < len(word):
        if ch == word[z:z + 1]:
            dash[z:z + 1] = ch
            matchmaker = 1
        z = z + 1
    return(matchmaker)

#Returns False if the game is over, and returns True if the game is still running
def gameStillRunning(word, dash, gamerunning):
    #Checks to see if game is over
    z = 0
    while z < len(word):
        if word[z:z + 1] != dash[z]:
            break
        z = z + 1
    if z == len(word):
        return False
    else:
        return True

#Writes the dashes to show how many letters in word
def dash_writer(dash):
    t2.color("black")
    t2.penup()
    t2.goto(-200,-200)
    t2.write(''.join(dash),align="center",font=("Comic Sans",30,"normal"))

#Draws a white line over the dashes so they can update the letters
def white_line():
    t2.penup()  
    t2.goto(-400,-200)
    t2.pendown()
    t2.color("white")
    t2.goto(400,-200)

#Creates the pop-up box
def pop_up():
    guessc = ""
    while len(guessc) != 1:
        guessc = sc.textinput("Virus.py","Choose one letter ")
    return guessc

#Either displays you win or you lose after the game
def display_end_of_game_message(xguess, word):
    t2.penup()
    t2.color("green")
    t2.goto(-400,-200)
    if xguess < 6:
        t2.write("You Win!", align="left", font=("Times New Roman",50,"normal"))   
    else:
        t2.color("red")
        t2.write("You Lose", align="left", font=("Times New Roman", 50, "normal"))
    t2.goto(-400,-300)
    t2.write("The word you were guessing was " + word, align="left",font=("Times New Roman",30,"normal"))
      
#Movie list and chooser
movies = ["endgame", "the fault in our stars","now you see me","conjuring", "moana", "toy story", "the book of henry", "hacksaw ridge", "godzilla", "alien", "star wars", "harry potter"]

word = movies[randint(0, len(movies)-1)]

dash = ["-"] * len(word)
#Variables
z = 0

sc = Screen()

gamerunning = 1

xguess = 0

#This loop checks for spaces and adds the spaces 
while z < len(word):
    if " " == word[z:z + 1]:
        dash[z] = " "
    z = z + 1

t2.pensize(100)

draw_hangman(xguess)
    

#This loop contains everything that happens inside the game 
while gamerunning == 1 and xguess < 6:

    #Writers dashes  
    dash_writer(dash)
 
    #This loop just checks if they put one letter into the pop-up and if they didn't it asks again
    guessc = pop_up()
        
    #This If statement checks if they got the guess wrong and if they did then it draws a body part    
    if update(word, dash, guessc) == False:
        xguess = xguess + 1

        draw_hangman(xguess)

    #Is the game over
    gamerunning = gameStillRunning(word, dash, gamerunning)
        
    #Draws a white line over the word to put the updated guessed letters in.
    white_line()
    
#Either writes you win or you lose depending on outcome.
display_end_of_game_message(xguess, word)



            










