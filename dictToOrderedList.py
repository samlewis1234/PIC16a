from matplotlib import pyplot as plt
import seaborn as sns

class dictToOrderedList(dict):
    """
    A dictionary class that supports sorting by value and also can plot keys and values.
    """
    
    def __init__(self, D, reverse = False, n = 10):
        '''
        Args: 
            D: dictionary
            n: int: first n values to print in __str__ method
            reverse: bool: plot in ascending order if false, descending if true
        Returns: none
        '''
        #make sure args are correct
        if not isinstance(D, dict):
            raise TypeError('D must be a dict')
        if not isinstance(reverse, bool):
            raise TypeError('Reverse must be true or false')
        if not isinstance(n, int):
            raise TypeError('n must be an integer')
        
        #convert dictionary to sorted list of tuples
        self.list_rep = sorted(D.items(), key=lambda x:x[1], reverse = reverse)
        
        self.reverse = reverse
        self.n = n
        
    def plot_dict(self, num = 10, title = "Most common 2 letter combinations"):
        '''
        Plots dictionary in specificed order
    
        Args: 
            num: int: first n values to plot
            title: str: title of plot
    
        Returns: none
        '''
        #makes sure args are correct
        if not isinstance(num, int):
            raise TypeError('num must be an integer')
        if not isinstance(title, str):
            raise TypeError('title must be a string')
        
        #only get first num items
        y = self.list_rep[:num]
        
        plt.figure(figsize=(20,5))
        
        #plot barplots of values
        plt.bar(range(len(y)), [val[1] for val in y], align='center')
        
        #add labels
        plt.xticks(range(len(y)), [val[0] for val in y])
        
        #add title
        if(self.reverse == True):
            plt.title(str(num)+title)
        else:
            plt.title(str(num)+title)
        plt.show()
    def __str__(self):
        '''
        Prints first n items of dictionary
        '''
        return str(dict(self.list_rep[:self.n]))
