# Classic
 [Classic](https://classic-meal.herokuapp.com/) is a terminal based game inplomented in Python. It was inspired by the classic game "hangman" but with a twist. 
 
 Classic can be used for playing and fun purposes, but also as an application looking for lunch or dinner ideas. With a simple design and it's own twist. The idea is for users to have fun playing but also to get some inspiration for next coming meal of the day.
 
 The application challenge the user to figure out what the meal of the day is and shows the answer at the end of the game. 

 ![Ami Responsive Design ](/readme/ami.png)
## How to play
Like the classic hangman game:
- The user starts by guessing a letter that could be part of the chosen word. 
- The user is then told how many letters are in the word.
- The letter will be displayed on the terminal as a correct or wrong answer.  
- The user has a maximum number of guesses and wins by entering all the words letters before 10 guesses. 

In my version I have chosen a specific theme for the diffrent words, which is different type of meals. For exampel: Pizza, salad or tacos.  

## Features

### Existing Features
- __Welcome message__ 
    - The game starts by displaying a welcome and introduction message to the user. 
 ![Welcome Message ](/readme/welcomemessage.png)
- __User input__
    - The user is asked to type in a letter that could match the word. 
    - The result of a guess is displayed after each round.
    - The number of remaining rounds is also displayed.
 ![User input ](/readme/userinput.png)
- __Scoring__ 
    - If the letter matches any letter in the word, it will appear in the correct spot in the word. And if the letter does not match it will be displayed in a list of failed guesses. 
- __Duration__ 
    - Repeats 10 times unless the user guesses the word earlier. 
- __Input validation__ 
    - Users will get an error message if numbers, multiple letters, or an already used letter is being entered. 
 ![Error Message ](/readme/errormessage.png)

### Future features 
- I would also like to give users the opputunity to choice between different themes. 
- I have a idea for the furture which is using this as a "special of the day" application for resturants. Visitors can play the game while queueing for the restaurant and also be updated on today's special. 

### Lucid Chart 
 ![Lucid Chart ](/readme/lc.png)

## Technologies Used 

### Languages Used
- __Python__

### Frameworks, Libraries & Programs Used

- __GitPod:__
     GitPod was used to provide the programming environment. 

- __GitHub:__
    GitHub is used to store the project code.
- __Heroku:__
    This projct was deployed using Code Institute's mock terminal for Heroku.

### Testing 
I have tested this project through:
- The PEP8 linter and confirmed there are no problems. 
- Given invalid inputs such as numbers, too many letters and alredy used letters. This makes an error message appear on the terminal.  

### Validator Tester
- PEP8 
    - No errors were returned from PEP8online.com

## Bugs
### Solved
- When reading the txt-file it included a trailing linefeed which became an extra and invinsible character in the word.

### Remaining Bugs
- The terminal emulator does not work on Iphone and not well on Android. 

## Deployment 
- This projct was deployed using Code Institute's mock termial for Heroku.
- The steps to deploy are as follows: 
 - Create a new app
 - Set the buildbacks to Python and NodeJS
 - Link the app to the repository
 - Press Deploy. 

## Credits 
__Content__
- I used W3 School through out my project. 
