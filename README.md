# PIC16a


Project name.
PIC 16a Final Project

Names of group members:

Sam Lewis

Rubie Dhillon

Edan Gold


Short description of the project:


Collection of plots to help understand trends in the Wordle solution set



The required python packages are: numpy, plotly.express, seaborn, matplotlib.pyplot, re, string, itertools and pandas.




Demo File Details and Instructions:


The demo file (titled "PIC16AFinalProject.ipynb") contains a selection of plots that provide the user with information on the World solution set. These plots include frequencies of letters in each of the five word positions, frequencies of letters in the solution set, and frequencies of the most common two-letter Wordle solution combinations. A few of the expected outputs are shown in the illustrations below.


To run the demo file, the user must call the "plotByString" function (shown in the last block of "PIC16AFinalProject.ipynb"), calling the function with the argument of an uppercase string. For instance, to find the frequency of other letters in solutions containing the string "EA," one would run the following code snippet: "plotByString("EA")". The expected result is a plot that shows the frequencies of letters other than "E" and "A" that appear in "EA"-containing words of the solution set, providing the user with the best accompanying letter possibilities to guess the Wordle solution. The plots produced by this specific example can be seen in the figures below.




![imgEA](https://user-images.githubusercontent.com/97066772/158006200-f2758c89-fc6f-4052-9009-bb9804d8f1b2.png)
![imgEAR](https://user-images.githubusercontent.com/97066772/158006202-481972a3-19d5-40ce-93c1-b6434e8d2b03.png)
![imgFreq](https://user-images.githubusercontent.com/97066772/158006203-67c88ca1-073a-4add-9510-8bc6c2c32ef4.png)
![imgPos](https://user-images.githubusercontent.com/97066772/158006204-e74939b1-98be-4e83-bd52-1488b96fcffa.png)




Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions:


Our plots provide some useful insight into Wordle, such as common letter combinations and letter frequencies, given that a certain string is in the word. However, they do not provide any explicit insight as to which words are the best ones to use. An idea for a potential extension would be using our resultant frequency plot to find he best possible word to guess to solve the puzzle in the least amount of trues. There are no major ethical concerns with our project given its subject, though some people may argue analyzing the solution set is against the spirit of the game. 




License and terms of use (probably MIT license):

MIT License (in license file)



References and acknowledgement:


Where we got the data: https://www.kaggle.com/bcruise/wordle-valid-words

Tutorial we used: https://www.kaggle.com/sophiefiola/analysis-of-the-wordle-solution-set
