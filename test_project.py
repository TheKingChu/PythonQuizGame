import project
import pygame
import pytest

pygame.init()

@pytest.fixture(scope="module")
def pygame_display():
    screen = pygame.display.set_mode((800, 600))
    yield screen
    pygame.quit()

def test_read_question_from_csv():
    questions = project.read_question_from_csv("quiz_questions.csv")
    assert len(questions) > 0
    assert isinstance(questions[0], project.Question)
    assert questions[0].choices != ["Choice1", "Choice2", "Choice3", "Choice4"]

def test_display_start_screen(pygame_display):
    font = pygame.font.SysFont(None, 30)
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 300)}))
    assert project.display_start_screen(pygame_display, font)

def test_tutorial_screen(pygame_display):
    font = pygame.font.SysFont(None, 30)
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 450)}))
    assert not project.tutorial_screen(pygame_display, font)

def test_display_question_selection(pygame_display):
    font = pygame.font.SysFont(None, 30)
    selected_questions = project.display_question_selection(pygame_display, font)
    assert selected_questions in [5, 10, 15, "back"]

def test_display_question(pygame_display):
    font = pygame.font.SysFont(None, 30)
    questions = project.Question("Test Question?", ["Choice1", "Choice2", "Choice3", "Choice4"], "Choice1", None)
    choices_buttons = project.display_question(pygame_display, font, questions, None, 10)
    assert len(choices_buttons) == 4

def test_run_quiz_game(pygame_display):
    font = pygame.font.SysFont(None, 30)
    questions = [
        project.Question("Test Question 1?", ["Choice1", "Choice2", "Choice3", "Choice4"], "Choice1", None),
        project.Question("Test Question 2?", ["Choice1", "Choice2", "Choice3", "Choice4"], "Choice2", None),
        project.Question("Test Question 3?", ["Choice1", "Choice2", "Choice3", "Choice4"], "Choice3", None),
        project.Question("Test Question 4?", ["Choice1", "Choice2", "Choice3", "Choice4"], "Choice4", None)
    ]

    with pytest.raises(SystemExit):
        project.run_quiz_game(pygame_display, font, questions)
