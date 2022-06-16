#--------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        
        check_answer(questions.get(key),guess)

        question_num += 1
    
    display_score(correct_guesses, guesses)



#--------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("WRONG!!!")
        return 0

#--------------
def display_score(correct_guesses, guesses):
    print("-----------")
    print("RESULTS")
    print("-----------")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+str(score)+"%")
#--------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#--------------


questions = {
"When was the Declaration of Independence signed?: ": "A",
"How often do we have a lear year?: ": "B",
"Who sang the song 'Thriller'?: ": "C",
"When did man land on the moon?: ": "A"
}

options = [["A. 1776", "B. 1492", "C. 1849", "D. 1700"],
          ["A. Yearly", "B. Every 4 years", "C. Every other year", "D. Every 5 years"],
          ["A. Stevie Wonder", "B. The Jackson 5", "C. Michael Jackson", "D. The Backstreet Boys"],
          ["A. 1969", "B. 1959", "C. 2001", "D. 1929"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")