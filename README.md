# PIC16a


Project name.
PIC 16a Final Project

Names of group members (if you don’t want to for privacy, add usernames).

Sam Lewis

Rubie Dhillon

Edan Gold


Short description of the project.

Collection of plots to help understand trends in the Wordle solution set


Instructions on how to install the package requirements. If you used the conda line above, your instruction should have the line conda create --name NEWENV --file requirements.txt.

The required python packages are: numpy, plotly.express, seaborn, matplotlib.pyplot, re, string, itertools and pandas. Use this line to get the required packages. conda create --name NEWENV --file requirements.txt


Detailed description of the demo file. This includes detailed instructions on how to run it, what output one should expect to see, and any explanations or interpretations of the result. There should be at least 2 figures embedded in this section. It can be screenshots of your game, or plots generated by your data visualization code. Make sure these figures have appropriate titles and captions, and are sufficiently explained in your text.

The demo file contains a selection of plots that give information on the Wordle solution set. These tell the user things such as frequency of letters, frequency of letters by position in the word, and frequency of letters in words containing a given letter/string. A few of the expected outputs are shown below. 

To change the interactive plots, a user has to call the function with a parameter different from the demo parameters (for example, "EA" and "EAR" plots shown below). 

![imgEA](https://user-images.githubusercontent.com/97066772/158006200-f2758c89-fc6f-4052-9009-bb9804d8f1b2.png)
![imgEAR](https://user-images.githubusercontent.com/97066772/158006202-481972a3-19d5-40ce-93c1-b6434e8d2b03.png)
![imgFreq](https://user-images.githubusercontent.com/97066772/158006203-67c88ca1-073a-4add-9510-8bc6c2c32ef4.png)
![imgPos](https://user-images.githubusercontent.com/97066772/158006204-e74939b1-98be-4e83-bd52-1488b96fcffa.png)



Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions.

Our plots provide some useful insight into Wordle, such as common letter combinations and letter frequencies, given that a certain string is in the word. However, they do not provide any explicit insight as to which words are the best ones to use. There are no major ethical concerns with our project given its subject, though some people may argue analyzing the solution set is against the spirit of the game. 




License and terms of use (probably MIT license).

MIT License (in license file)


References and acknowledgement.

Where we got the data: https://www.kaggle.com/bcruise/wordle-valid-words

Tutorial we used: https://www.kaggle.com/sophiefiola/analysis-of-the-wordle-solution-set
