#for creating the game ui
import pygame
#the questions
import csv

def main():
    #init pygame
    pygame.init()
    #set the screen size
    screen = pygame.display.set_mode((800, 600))
    #title
    pygame.display.set_caption("Quiz")
    #FPS
    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Calibri", 30)

    #load questions
    questions = read_question_from_csv("quiz_questions.csv")

    #display start scene

    #quit
    pygame.quit()

#a class for representing each question
class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

#reads the questions from csv file and creates question objects
def read_question_from_csv(file_name):
    questions = []
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        #skip the header
        next(csv_reader)
        for row in csv_reader:
            question, choice1, choice2, choice3, choice4, answer = row
            choices = [choice1, choice2, choice3, choice4]
            questions.append(Question(question, choices, int(answer)))
        return questions

#START SCENE
def display_start_screen(screen, font):
    ...

#choose how many questions to play with
def display_question_selection(screen, font):
    ...

#display a question and the 4 choices
def display_question(screen, font, question):
    ...

#run the quiz with the chosen amount of questions
def run_quiz_game(screen, font, questions, number_of_questions):
    ...

if __name__ == "__main__":
    main()
