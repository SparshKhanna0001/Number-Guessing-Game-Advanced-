# Not Your Ordinary Number Guessing Game

* Sections:-
   * Long Story Short
   * Algorithm
   * Future Developments

## Long Story Short
__Ordinary Number Guessing Game__ : You have five turns, guess the number between 1 and 100. 
                                    Winning Probability : 0.05
                                    
__Intermeditiate Number Guessing Game__ : Everything is same except one improvement. Here the machine provides you hint like _the number you guessed is too low_ __OR__ 
                                          _the number you guessed is too high_. This although provides the user with some insight but that not enough.
                                          
The type of number guessing games described above are __good for coding practices__ but actually are __boring in nature.__
I have tried to make it interesting to play.

### My Number Guessing Game :
Suppose gave a wrong guess the following describes how the computer/machine you're using responds:- 
>>>This time you were not able to make it up.
>>>As a hint, the number lies between 32 and 47. 
>>>Please try again !!!

Here's an image :- 
![Image-og-gameplay](https://github.com/SparshKhanna0001/Number-Guessing-Game-Advanced-/blob/main/IMG_20210411_173039.jpg)
                              
Everytime you lose the program will give _the range in which correct option lies_.
__But, does the program give you same range__
_No, it will don't_.  
* First Time you lose : range of 15 numbers
* Second Time you lose : range of 10 numbers
* Third Time you lose : range of 5 numbers 
* Fourth Time you lose : range of 3 numbers

# Algorithm
The range finder algorithm is used to find upper and lower ends of range so as to give a hint.

### How does this works ? 
* First the programs randomly picks a number from 1 to 100. 
* This number and the difference that should be between upper and lower limits of range is passed to the Ranger finder function.
* The algorithm then divides the difference by two and rounds off the number obtained.
* Then the algorithm finds a random number between 0 and difference/2 let's call it A. 
* This random number found is then subtracted from the number which was passed as an argument, and the number so obtained is the lower limit of range.
* For the upper end the algorithm adds (difference-A) to the number, this becomes the upper limit of the range. 
* At the end both upper limit and lower limits are returned. 
* A for loop is used to obtain different Lower and upper limits for different difference values. 

#### For Example:- 
* The computer selects 50 as number.
* The difference is 15 
* 15/2 = 8 (rounded off value)
* The computer then randomly picks a number ranging from 0 to 8
* Let's say the computer picks number 5. 
* Now, 5 is subtracted from 50 and 45 is obtained as lower limit. 
* Now, 5 is subtracted from the difference which is 15 and we obtain 10, 10 is added to the 50 and 50 us obtained as upper limit. 
* Both 45 : lower limit and 60: upper limt are returned. 

## Future Developments

* May add __Graphical User Interface.__ 
* May add a __database to store users scores__ and to implement a __functionality that saves highscores.__
* Since, it a simple game so may be in future i may __integrate this game with other games of this type to a single platform__.
