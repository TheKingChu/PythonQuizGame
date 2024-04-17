#for creating the game ui
import pygame
#the questions
import csv
#for randomization
import random


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
    def __init__(self, question, choices, answer, photo_path):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.photo_path = photo_path


#reads the questions from csv file and creates question objects
def read_question_from_csv(file_name):
    questions = []
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        #skip the header
        next(csv_reader)
        for row in csv_reader:
            question, choice1, choice2, choice3, choice4, answer, photo_path = row
            choices = [choice1, choice2, choice3, choice4]
            questions.append(Question(question, choices, int(answer), photo_path))
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
def display_question(screen, font, question, photo_path, countdown_timer):
    #double buffering for flickering reduction
    back_buffer = pygame.Surface(screen.get_size())
    #background color
    back_buffer.fill((30, 30, 36))

    #display countdown slider
    slider_width, slider_height = 400, 20
    slider_x = (screen.get_width() - slider_width) // 2
    slider_y = 50 #making it be on the top side of the screen
    pygame.draw.rect(back_buffer, (251, 248, 239), (slider_x, slider_y, slider_width, slider_height))
    slider_fill_width = int(countdown_timer / 10 * slider_width)
    pygame.draw.rect(back_buffer, (0, 255, 0), (slider_x, slider_y, slider_fill_width, slider_height))

    #display countdown timer
    timer_text = font.render(str(int(countdown_timer)), True, (255, 255, 255))
    timer_text_rect = timer_text.get_rect(center=(screen.get_width() // 2, slider_y - 20))
    back_buffer.blit(timer_text, timer_text_rect)

    #display the question text with word-wrapping
    question_text = wrap_text(question.question, font, 700)
    y_offset = 100
    for line in question_text:
        text = font.render(line, True, (255, 255, 255))
        back_buffer.blit(text, (50, y_offset))
        y_offset += font.get_linesize()

    #display photo in a rectangle in the center of the screen
    if question.photo_path:
        photo = pygame.image.load(photo_path)
        photo_rect = photo.get_rect()
        photo_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        #set the width and height for the rectangle
        photo_width, photo_height = 400, 300
        #create a new rect with the correct width and height
        photo_rect = pygame.Rect(photo_rect.centerx - photo_width // 2,
                                 photo_rect.centery - photo_height // 2,
                                 photo_width, photo_height)
        pygame.draw.rect(screen, (255, 255, 255), photo_rect, 2)
        #scale the photo to fit to the rect and keep the aspect ratio
        scaled_photo = pygame.transform.scale(photo, (photo_width, photo_height))
        #calculate the position so that the scaled photo will be centered in the rect
        photo_pos = (photo_rect.centerx - scaled_photo.get_width() // 2,
                     photo_rect.centery - scaled_photo.get_height() // 2)
        back_buffer.blit(scaled_photo, photo_pos)

    #color for each choice button
    button_colors = [(41, 110, 180), (177, 24, 200), (205, 56, 19), (31, 111, 91)]

    #display choices as buttons
    choices_buttons = []
    button_width, button_height = 200, 40
    x_start = (screen.get_width() - button_width * len(question.choices)) // 2
    y_start = screen.get_height() - 100
    for i, (choice, color) in enumerate(zip(question.choices, button_colors)):
        choice_button = pygame.Rect(x_start + i * button_width, y_start, button_width, button_height)
        pygame.draw.rect(back_buffer, color, choice_button)
        choice_text = font.render(choice, True, (255, 255, 255))
        text_rect = choice_text.get_rect(center=choice_button.center)
        back_buffer.blit(choice_text, text_rect)
        choices_buttons.append(choice_button)
    
    screen.blit(back_buffer, (0, 0))
    pygame.display.flip()
    return choices_buttons


def wrap_text(text, font, max_width):
    words = text.split(" ")
    wrapped_lines = []
    current_line = ""
    for word in words:
        line = current_line + word + " "
        if font.size(line)[0] <= max_width:
            current_line = line
        else:
            wrapped_lines.append(current_line)
            current_line = word + " "
    wrapped_lines.append(current_line)
    return wrapped_lines


#run the quiz with the chosen amount of questions
def run_quiz_game(screen, font, questions, number_of_questions):
    while True:
        #shuffle the list of questions
        random.shuffle(questions)
        score = 0

        #display the selection of number of questions
        number_of_questions = display_question_selection(screen, font)

        #display each question with this for loop
        for question in questions[:number_of_questions]:
            #start the countdown timer
            start_timer = pygame.time.get_ticks()
            countdown_timer = 10 #10 second countdown
            while countdown_timer > 0:
                #calculate the elapsed time
                elapsed_time = (pygame.time.get_ticks() - start_timer) / 1000.0
                #update the countdown timer
                countdown_timer = max(10 - elapsed_time, 0)
                choice_buttons = display_question(screen, font, question, question.photo_path, countdown_timer)

                #wait for the player to chose an answer
                choice = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for i, button in enumerate(choice_buttons):
                            if button.collidepoint(event.pos):
                                choice = i + 1

                #check if the time is up
                if countdown_timer == 0 or choice is not None:
                    #move to the next question
                    break

                pygame.display.flip()

            #check if the choice is correct and add that to the score
            if choice == question.answer:
                score += 1

        #display the result
        display_result(screen, font, score, number_of_questions)
        #replay and quit button for the result screen
        replay_button, quit_button = display_result_buttons(screen, font)

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

def display_result(screen, font, score, total_questions):
    #calculate percentage of correct answers
    percentage_correct = (score / total_questions) * 100

    #choose background color based on the correctness percentage
    if percentage_correct == 0:
        background_color = (123, 45, 38) #red
    elif percentage_correct < 50:
        background_color = (126, 99, 16) #yellow
    else:
        background_color = (0, 61, 0) #green

    #display result
    screen.fill(background_color)
    result_font_size = 40
    result_font = pygame.font.Font(None, result_font_size)
    result_text = result_font.render("You got " + str(score) + "/" + str(total_questions) + " correct.", True, (255, 255, 255))
    result_text_rect = result_text.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(result_text, result_text_rect)

def display_result_buttons(screen, font):
    #for centering the text and buttons on the screen
    screen_width, screen_height = screen.get_size()

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

    return replay_button, quit_button


if __name__ == "__main__":
    main()
