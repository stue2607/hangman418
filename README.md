**Hangman**
--------------------------------------------------------------------

**Contents:**

- [Installation instructions](Installation-instructions)
- A description of the project: what it does, the aim of the project
- Usage instructions
- File structure of the project
- License information
- What i learned
--------------------------------------------------------------------

*A description of the project: what it does, the aim of the project, and what you learned* 

 **Hangman** project, developed as part of my Dev Ops training at [AiCore](#https://www.theaicore.com/). Hangman is a python game were a word is randomly selected from a list of fruits and the player tries to guess that word within five attempts. This is a take on the classic game where normally a player selects the word and another player tries to guess the word within a certain number of tries between 5 and 7 depending on the sketch of the hangman diagram.

 **The aim of the project** The main aim of this project was to practice basic Python in my opinion. It utilises OOP principles and is therefore built around one class which includes three methods: 
- The first initialises the attributes as indicated in the docstring provided throughout the project;
- The second method checks if the input letter provided by the user is in the random word;
- And finally a method that asks the user for a letter and checks if this letter has already been tried, and if the input is correct.

 **Key takeaways in my personal development** I feel as an amateur in the Python programming language that i learned a lot about calling functions within other functions in a clean code and how to plan bringing everything together, one of the hardest parts of the project was cleaning up the code afterwards as the code started to look completely different to my original code which was at first alarming until i realised this seems to be a part of the coding process for many people when creating a new class. As i was progressing through the project i found that the code was not storing the returned values for the next turn and asfter some research and going back over past tutorials provided by AI Core i remembered learning that the self function was used to store values in the code and so experimented where the best places for these were and by trial and error got there after around 30 saves. GitHub proved quite a challenge at first as i found my project was not pushing with a critical error suggesting the repo did not have permissions to pull request through, after research i realised that i had configured 'git bash' slightly wrong by adding a dot in the middle of my username required for GitHub itself, i attempted to change this but as i used credential helper to store this i had to undo everything and redo as well as requesting a new token from GitHub to allow VS Code to push to my repo known as hangman418, all in all this was a very sucsesful learning and gave me a much stronger insight into GitHUb, git bash and VS Code with the way they work together. I have made the decision to add images to reference the hangman during the game after learning how to do this in a tutorial on YouTube, i discovered it is a very similar method to recording losing a life or replacing an underscore with a letter and so it felt the right thing to do. Although i am not 100% happy with the diagram of the hangman as i found using the right arm and leg as a symbol '\ ' moved the rest of the diagram onto the next line after testing and so had to use alternative symbols and the hangman now stands like Elvis, this is something i need to work on.

-------------------------------------------------------------------------------------------------------------------

*Installation instructions*

There is no installation required as this a command line project and can be ran straight from the file, i would suggest it is best used in VS Code as this is where i created all of the code but i can be pasted into any python command program as far as my knowledge goes.

-------------------------------------------------------------------------------------------------------------------

*Usage instructions*

To start the game a function called "play_game" can start this which is wrapped around the code for ease of use, You will then be asked to input a single alphabetical letter and if this is an integer or multiple letters you will be asked to provide another single alphabetical letter. The game is set to have 5 lives and each incorrect guess of a letter will result in a loss of life in the game (but do not worry, you will be able to play again.)

As you play you will find instructions as you go along so please enjoy this game and if you have any questions please feel free to reach out.

-------------------------------------------------------------------------------------------------------------------

*File structure of the project*

Hangman by Stuart Elliott as part of the AI Core dev ops training course has 4 main areas to the file structure;
- A markdown file containing the project documentation and explanation of the hangman project,
- The main project (sourced from a public template made available at the begining on the project) where the   final clean code for the hangman game can be found and executed from,
- Module files that were used to test each section of the project before being cleaned up and put together,
- Licences for the project containing a Python licence and a GitHub licence.

>Within the main code of the game i declared the following using the assignment operator to make cleaner code;
- self.word = random.choice(word_list)
- self.word_guessed = list('_' * len(self.word))
- self.num_letters = len(set(list(self.word)))
- self.num_lives = num_lives
- self.list_letters = []
- self.hang_man = **5 X Images of the hangman at various stages**
           
-------------------------------------------------------------------------------------------------------------------

*License information*

- **Python code (Hangman) = MIT License**

Copyright (c) [2023] [Stuart Elliott] [stue2607] [stu.e2607@gmail.com]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

- **GitHub = Copyright of docstrings**

Copyright (c) {{ 2023 }}, {{ AI CORE }}, {{Stuart Elliott}}

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THE DOCSTRINGS ARE PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
DOCSTRING CONTENT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------------------------------------------
