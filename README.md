# PIC16a


Project name.
PIC 16a Final Project

Names of group members:

Sam Lewis

Rubie Dhillon

Edan Gold


Short description of the project:


Collection of plots to help understand trends in the Wordle solution set



The required python packages are: numpy(https://repo.anaconda.com/pkgs/main/win-64/pandas-1.3.4-py39h6214cd6_0.conda), seaborn(https://repo.anaconda.com/pkgs/main/noarch/seaborn-0.11.2-pyhd3eb1b0_0.conda), matplotlib.pyplot(https://repo.anaconda.com/pkgs/main/win-64/matplotlib-base-3.4.3-py39h49ac443_0.conda), re(https://repo.anaconda.com/pkgs/main/win-64/regex-2021.8.3-py39h2bbff1b_0.conda), string(built in), itertools(https://repo.anaconda.com/pkgs/main/noarch/more-itertools-8.10.0-pyhd3eb1b0_0.conda) and pandas(https://repo.anaconda.com/pkgs/main/win-64/pandas-1.3.4-py39h6214cd6_0.conda).




Demo File Details and Instructions:


The demo file (titled "PIC16AFinalProject.ipynb") contains a selection of plots that provide the user with information on the World solution set. These plots include frequencies of letters in each of the five word positions, frequencies of letters in the solution set, and frequencies of the most common two-letter Wordle solution combinations. A few of the expected outputs are shown in the illustrations below.


To run the demo file, the user must download both the PIC16AFinalProject.ipynb and dictToOrderedList.py files and save them in the same folder. Then, they simply need to run each of the code blocks in order. The first few plots do not require any input and show frequencies for each letter. The plotByString function allows for user input. For instance, to find the frequency of other letters in solutions containing the string "EA," one would run the following code snippet: "plotByString("EA")". The expected result is a plot that shows the frequencies of letters other than "E" and "A" that appear in "EA"-containing words of the solution set, providing the user with the best accompanying letter possibilities to guess the Wordle solution. The plots produced by this specific example can be seen in the figures below. The user can switch the input for plotByString to find letter frequencies for other strings.



![imgFreq](https://user-images.githubusercontent.com/97066772/158006203-67c88ca1-073a-4add-9510-8bc6c2c32ef4.png)
![imgPos](https://user-images.githubusercontent.com/97066772/158006204-e74939b1-98be-4e83-bd52-1488b96fcffa.png)
![imgEA](https://user-images.githubusercontent.com/97066772/158006200-f2758c89-fc6f-4052-9009-bb9804d8f1b2.png)
![imgEAR](https://user-images.githubusercontent.com/97066772/158006202-481972a3-19d5-40ce-93c1-b6434e8d2b03.png)





Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions:


Our plots provide some useful insight into Wordle, such as common letter combinations and letter frequencies, given that a certain string is in the word. However, they do not provide any explicit insight as to which words are the best ones to use. An idea for a potential extension would be using our resultant frequency plot to find he best possible word to guess to solve the puzzle in the least amount of tries. There are no major ethical concerns with our project given its subject, though some people may argue analyzing the solution set is against the spirit of the game. 




License and terms of use (probably MIT license):

MIT License (in license file)



References and acknowledgement:

Thank you to Harlin, Vishnu, And Shruti for helping us develop our python skills.

Where we got the data: https://www.kaggle.com/bcruise/wordle-valid-words

The data is orginally from the wordle source code.

Tutorial we used: https://www.kaggle.com/sophiefiola/analysis-of-the-wordle-solution-set

3 Things That Differentiate our project from the tutorial:
1) We created a dictionary that contained each two letter combination and their frequencies.
2) We created a custom class that can sort dictionaries and plot its keys and values using a barplot.
3) We created a plotByString function that shows letter frequencies given that a certain string is in the word.
