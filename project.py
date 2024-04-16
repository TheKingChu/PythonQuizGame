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
    #background color
    screen.fill((30, 30, 36)) 

    #for centering the text and buttons on the screen
    screen_width, screen_heigh = screen.get_size()

    #title text
    start_font_size = 60
    start_font = pygame.font.Font(None, start_font_size)
    start_text = start_font.render("Welcome to quiz!", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(start_text, start_text_rect)

    #start button
    start_button_width, start_button_height = 200, 50
    start_button = pygame.Rect((screen_width - start_button_width) // 2, 200, start_button_width, start_button_height)
    pygame.draw.rect(screen, (0, 200, 0), start_button)
    start_button_text = font.render("Start", True, (255, 255, 255))
    start_button_text_rect = start_button_text.get_rect(center=start_button.center)
    screen.blit(start_button_text, start_button_text_rect)

    #quit button
    quit_button_width, quit_button_height = 200, 50
    quit_button = pygame.Rect((screen_width - quit_button_width) // 2, 300, quit_button_width, quit_button_height)
    pygame.draw.rect(screen, (214, 40, 57), quit_button)
    quit_button_text = font.render("Quit", True, (255, 255, 255))
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.center)
    screen.blit(quit_button_text, quit_button_text_rect)

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
    #background color
    screen.fill((30, 30, 36))

    #selection text
    question_font_size = 40
    quiestion_font = pygame.font.Font(None, question_font_size)
    quiestion_text = quiestion_font.render("Select the number of question:", True, (255, 255, 255))
    screen.blit(quiestion_text, (50, 50))

    #5 questions
    button_5 = pygame.Rect(300, 150, 200, 50)
    pygame.draw.rect(screen, (21, 121, 31), button_5)
    button_5_text = font.render("5 questions", True, (255, 255, 255))
    screen.blit(button_5_text, (350, 160))

    #10 questions
    button_10 = pygame.Rect(300, 250, 200, 50)
    pygame.draw.rect(screen, (21, 121, 31), button_10)
    button_10_text = font.render("10 questions", True, (255, 255, 255))
    screen.blit(button_10_text, (340, 260))

    #20 questions
    button_20 = pygame.Rect(300, 350, 200, 50)
    pygame.draw.rect(screen, (21, 121, 31), button_20)
    button_20_text = font.render("20 questions", True, (255, 255, 255))
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
    #background color
    screen.fill((30, 30, 36))

    #display the question text with word-wrapping
    question_text = font.render(question.question, True, (255, 255, 255))
    question_rect = question_text.get_rect(topleft=(50, 50))
    question_width = 700 #width of the question area box
    question_text = font.render(question.question, True, (255, 255, 255), (30, 30, 30))
    screen.blit(question_text, question_rect)

    #color for each choice button
    button_colors = [(41, 110, 180), (177, 24, 200), (205, 56, 19), (31, 111, 91)]

    #display choices as buttons
    choices_buttons = []
    button_width, button_height = 200, 40
    x_start = (screen.get_width() - button_width * len(question.choices)) // 2
    y_start = screen.get_height() - 100
    for i, (choice, color) in enumerate(zip(question.choices, button_colors)):
        choice_button = pygame.Rect(x_start + i * button_width, y_start, button_width, button_height)
        pygame.draw.rect(screen, color, choice_button)
        choice_text = font.render(choice, True, (255, 255, 255))
        text_rect = choice_text.get_rect(center=choice_button.center)
        screen.blit(choice_text, text_rect)
        choices_buttons.append(choice_button)
    
    pygame.display.flip()
    return choices_buttons

#run the quiz with the chosen amount of questions
def run_quiz_game(screen, font, questions, number_of_questions):
    while True:
        number_of_questions = display_question_selection(screen, font)
        score = 0

        for question in questions[:number_of_questions]:
            choice_buttons = display_question(screen, font, question)

            #wait for the player to chose an answer
            choice = None
            while choice is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for i, button in enumerate(choice_buttons):
                            if button.collidepoint(event.pos):
                                choice = i + 1
                    
            if choice == question.answer:
                score += 1

        #for centering the text and buttons on the screen
        screen_width, screen_heigh = screen.get_size()

        #calculate percentage of correct answers
        percentage_correct = (score / number_of_questions) * 100

        #choose background color based on the correctness percentage
        if percentage_correct > 50:
            background_color = (150, 0, 0) #red
        elif percentage_correct < 50:
            background_color = (100, 100, 0) #yellow
        else:
            background_color = (0, 100, 0) #green

        #display result
        screen.fill(background_color)
        result_font_size = 40
        result_font = pygame.font.Font(None, result_font_size)
        result_text = result_font.render("You got " + str(score) + "/" + str(number_of_questions) + " correct.", True, (255, 255, 255))
        result_text_rect = result_text.get_rect(center=quit_button.center)
        screen.blit(result_text, result_text_rect)

        #play again button
        replay_button_width, replay_button_height = 200, 50
        replay_button = pygame.Rect((screen_width - replay_button_width) // 2, 200, replay_button_width, replay_button_height)
        pygame.draw.rect(screen, (0, 200, 255), replay_button)
        replay_button_text = font.render("Play Again", True, (255, 255, 255))
        replay_button_text_rect = replay_button_text.get_rect(center=replay_button.center)
        screen.blit(replay_button_text, replay_button_text_rect)

        #quit button
        quit_button_width, quit_button_height = 200, 50
        quit_button = pygame.Rect((screen_width - quit_button_width) // 2, 300, quit_button_width, quit_button_height)
        pygame.draw.rect(screen, (200, 0, 0), quit_button)
        quit_button_text = font.render("Quit", True, (255, 255, 255))
        quit_button_text_rect = quit_button_text.get_rect(center=quit_button.center)
        screen.blit(quit_button_text, quit_button_text_rect)
        pygame.display.flip()

        #QUIT
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #restarts the game
                    if replay_button.collidepoint(event.pos):
                        break
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        quit()
            else:
                continue
            break


if __name__ == "__main__":
    main()
