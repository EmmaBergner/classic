# Classic
 [Classic](https://classic-meal.herokuapp.com/) is a Python terminal game, and inspired version of the classic game "hangman" but with a twist. 
 
 Classic can be used for playing and fun purposes, but also as an application looking for lunch or dinner ideas. With a simple design and it's own twist. The idea is for users to have fun playing but also to get some inspiration for next coming meal of the day.
 
 The terminal ask the user what the meal of the day is and shows the result at the end of the game. 

 ![Ami Responsive Design ](/readme/ami.png)
## How to play
Like the classic hangman game:
- The user starts by enter first guess on a letter that could be apart of the chosen word. 
- The user is then told how many letters are in the word.
- The letter will be printed by the terminal as a correct or wrong answer.  
- The user has a certain tries of guesses and wins by entering the right letters before 10 guesses. 

In my version I have choisen a specific theme for the diffrent words, which is different type of meals. For exampel: Pizza, salad or tacos.  

## Features

### Existing Features
- __Welcome message__ 
    - The game starts by displaying a welcome and introduction message to the user. 
 ![Welcome Message ](/readme/welcomemessage.png)
- __User input__
    - The user is asked to type in a letter that could match the word. 
    - Guesses are displayed and updated after each round
 ![User input ](/readme/userinput.png)
- __Input validation__ 
    - Users will get an error message if numbers or already give letter is being entered.
 ![Error Message ](/readme/errormessage.png)
- __Decision__ 
    - If the letter matches any letter in the word, it will appear on the correct spot in the word. And if the letter does not match it will be displayed in a different list. 
    - Repeats 8 times unless user guess word before. 

### Future features 
- I would also like to give users the opputunity to choice between different categories. 
- I have a idea for the furture witch is using this as a "special of the day" application for resturants. Visitors can while queueing for the restaurant play the game and also be updated on today's special. 


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

### Testing 
I have tested this project through:
- Chrome and Safari with no problems. 
- The PEP8 linter and confirmed there are no problems. 
- Given invalid inputs such as numbers, to many letters and alredy given letter. And error message will apear in the terminal.  

### Validator Tester
- PEP8 
    - No errors were returned from PEP8online.com

### Bugs
- No bugs found remaining.

### Remaining Bugs
- Does not work on Iphone and not well on Android. 

## Deployment 
- The site was deployed to GitHub pages. The steps to deploy are as follows: 

## Credits 
__Content__
- I used W3 School through out my project. 
