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
    font = pygame.font.SysFont(None, 30)

    #load questions
    questions = read_question_from_csv("quiz_questions.csv")

    #display start scene
    if display_start_screen(screen, font):
        number_of_questions = display_question_selection(screen, font)
        run_quiz_game(screen, font, questions, number_of_questions)

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
    screen.fill((235,200,255)) #white screen
    start_text = font.render("Welcome to quiz!", True, (0, 0, 0))
    screen.blit(start_text, (250, 50))

    #start button
    start_button = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), start_button)
    start_button_text = font.render("Start", True, (0, 0, 0))
    screen.blit(start_button_text, (350, 210))

    #quit button
    quit_button = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    quit_button_text = font.render("Quit", True, (0, 0, 0))
    screen.blit(quit_button_text, (350, 310))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return True
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()


#choose how many questions to play with
def display_question_selection(screen, font):
    screen.fill((100, 200, 100))
    quiestion_text = font.render("Select the number of question:", True, (0, 0, 0))
    screen.blit(quiestion_text, (50, 50))

    #5 questions
    button_5 = pygame.Rect(300, 150, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), button_5)
    button_5_text = font.render("5 questions", True, (0, 0, 0))
    screen.blit(button_5_text, (350, 160))

    #10 questions
    button_10 = pygame.Rect(300, 250, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), button_10)
    button_10_text = font.render("10 questions", True, (0, 0, 0))
    screen.blit(button_10_text, (340, 260))

    #20 questions
    button_20 = pygame.Rect(300, 350, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), button_20)
    button_20_text = font.render("20 questions", True, (0, 0, 0))
    screen.blit(button_20_text, (340, 360))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_5.collidepoint(event.pos):
                    return 5
                elif button_10.collidepoint(event.pos):
                    return 10
                elif button_20.collidepoint(event.pos):
                    return 20

#display a question and the 4 choices
def display_question(screen, font, question):
    screen.fill((100, 200, 100))
    text = font.render(question.question, True, (0, 0, 0))
    screen.blit(text, (50, 50))
    y = 150

    for i, choice in enumerate(question.choices, 1):
        choice_text = font.render(f"{i}. {choice}", True, (0, 0, 0))
        screen.blit(choice_text, (50, y))
        y += 50
    
    pygame.display.flip()

#run the quiz with the chosen amount of questions
def run_quiz_game(screen, font, questions, number_of_questions):
    score = 0

    for question in questions[:number_of_questions]:
        display_question(screen, font, question)
        choice = None
        while choice is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_4:
                        choice = event.key - pygame.K_1 + 1
        if choice == question.answer:
            score += 1

    screen.fill((100, 200, 100))
    result_text = font.render("You got " + str(score) + "/" + str(number_of_questions) + "correct.", True, (0, 0, 0))
    screen.blit(result_text, (50, 50))
    pygame.display.flip()
    #wait 3 seconds before quitting
    pygame.time.wait(3000)


if __name__ == "__main__":
    main()
