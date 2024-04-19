# Trivium Blast: Videogame Trivia

#### Video Demo: <URL HERE>
## Introduction:
Videogame trivia game! You the player are presented with a series of questions, each with 4 possible answers, only 1 being the correct one. It's developed using Pygame and CSV.

## Overview
Trivium Blast relies on **Pygame** for the graphical interface. **Pygame** has a lot of different features for drawing and displaying graphics, which made it a suitable choice for a game. Throughout the development process, a goal was to maintain clean, readable code and establishing a straightforward setup to facilitate both understanding and scalability.

### Pygame Features Utilized:
- Event handling: It streamlined the processing of user input allowing for seamless interaction with the GUI elements like buttons and the options menu. By efficiently managing events like mouse clicks so that the player can navigate through the game easily.

### Code Organization
- Main Functionality
    - `main()`:
- Sound Effect Handling
    - `play_sound(sound)`: Called to play sound effects during the game.
- Question Class
    - `class Question`:
- CSV File Handling
    - `read_question_from_csv(file_name)`:
- Start Screen
    - `draw_start_screen(screen, font)`:
    - `display_start_screen(screen, font)`:
    - `sound_option_screen(screen, font, music_volume, sound_effect_volume)`:
    - `tutorial_screen(screen, font)`:
- Question Selection Screen
    - `display_question_selection(screen, font)`:
- Running the game
    - `display_question(screen, font, question, photo_path, countdown_timer)`:
    - `wrap_text(text, font, max_width)`:
    - `run_quiz_game(screen, font, questions)`:
    - `display_result(screen, score, total_questions)`:
    - `display_result_buttons(screen, font)`:

### Challenges and Solutions

## Features
- Start screen with buttons for starting the game, how to play, adjusting the sound options, and quitting.
- Sound effects and music with adjustable volume levels.
- Tutorial screen explaining how to play the game.
- Question selection screen allowing the player to choose the numbers of questions to play with.
- Display the questions with choices, countdown timer, and a picture.
- Randomization of the questions and the choice positions.
- Result screen showing the number of correct answers, with options to replay or quit.

## File Structure
- **python.py**: This file contains the core logic and functionality. It handles tasks such as loading the questions from the CSV file, displaying the questions and answer choices, tracking the player response, and determine the final score.
- **quiz_questions.csv**: Contains the questions, choices, answers and images. This file serves as the database for the game.
- **test_python.py**: Contains testing functionality for different parts of the game logic. Ensures that the game behaves as expected.
- **requirements.txt**: Contains which pip installments are needed for this project.

## Credits
- Cogwheel icon: <a href="https://www.freepik.com/icon/setting_8629952#fromView=search&page=1&position=25&uuid=66919a3a-0206-4c61-966c-9d8194274988">Icon by sfjamil</a>
- Images: Google
- Questions: [WaterCooler Trivia](https://www.watercoolertrivia.com/trivia-questions/video-game-trivia-questions) and Google
- Music and Sounds: Freesound

## Documentation
- https://docs.python.org/3/
- https://www.pygame.org/docs/ 
- https://docs.python.org/3/library/csv.html