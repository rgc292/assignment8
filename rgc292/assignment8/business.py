'''
Created on Nov 6, 2015

@author: Rafael Garcia (rgc292)
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

class Calculation(object):
    '''
    This class intend to manipulate and compute the values involved on the investment
    program 
    '''
    
    position_value = list()
    position = list()
    value = 0
    counter = 0
    share_value = ([1,10,100,1000])
    cumu_ret = list()
    sample = list()
    daily_ret = list()
    mean = list()
    std = list()
    
    
    def __init__(self):
        pass
    
    
    #Check if user's input is in expected format 
    def validate_input(self):
        global value
        global counter
        self.invalid = True
        self.exit = ""
        self.counter = self.counter + 1
        
        #It iterates until input is valid 
        while self.invalid:
            try:
                #Counter counts number of inputs
                if self.counter <= 4:
                    value = int(raw_input("Type an integer >= 0 for the " + 
                                           "number of shares! >>> "))
                else:
                    value = int(raw_input("Type an integer >= 0 for the " + 
                                           "number of trials! >>> "))        
                if value >= 0:
                    self.invalid = False
                    continue
                else:
                    print "The number needs to be >= 0! "     
            except (ValueError, NameError, SyntaxError, TypeError, 
                                                        KeyboardInterrupt):
                self.exit = raw_input("\nWould you like to exit? (y,n) >>> ")
                if self.exit.lower() == "y":
                    print "Good bye!"
                    sys.exit(1)
                elif self.exit.lower() == "n":
                    print "Ok!"
                    continue
                else:
                    continue
            
            except (EOFError, SystemExit):
                print "Good Bye!"
                sys.exit(1)
          
        return value        


    #Set the value that represents the size of each investment    
    def set_position_value(self):               
        global position
        global position_value
        global share_value
      
        #It multiplies entered position and share_value respectively
        for index in range(4):
            self.position_value.append(self.position[index]*self.share_value[index])
        
        return self.position_value
     
      
    #It creates a distribution of wins and losses among trials
    def distribution_wins_loses(self, trials):
        global sample
        global cumu_ret
        self.share_cumu = []
        probability_win = .51
        del self.sample[:]
        
        #It store the random result of each trial in a list
        for trial in range(trials):
            if np.random.random() < probability_win:
                self.sample.append(1)
                self.share_cumu.append(1)
            else:
                self.sample.append(-1)
                self.share_cumu.append(-1)
        self.cumu_ret.append(self.share_cumu)        
        return self.sample      
                
                
    #It creates the daily_ret having the amounts per trial           
    def build_daily_ret(self, share_value):
        global sample
        global daily_ret
        global position
        self.distribution_wins_loses(self.position[4])
        self.share_value = share_value
        self.share_cumu = []
        
        for trial in (range(len(self.sample))):
            if self.sample[trial] == 1:
                self.share_cumu.append(float(2*(self.share_value)))
            else:
                self.share_cumu.append(0)   
        self.daily_ret.append(self.share_cumu)
        return self.daily_ret
        
        
    #Compute the daily mean for each one of the 4 kinds of share                   
    def mean_daily_return(self):
        global daily_ret
        global mean
        
        for index in range(4): 
            self.mean.append(round(np.mean(self.daily_ret[index]), 2))
        return self.mean
        
        
    #Compute the daily standard deviation for each one of the 4 kinds of share    
    def std_daily_return(self):
        global daily_ret
        global std
        global mean
        self.std_calculation = []
        
        for index in range(4):
            self.std.append(round(np.std(self.daily_ret[index]), 2))
        return self.std
    
    #Plots the histogram for each position
    def plot_results(self, filename, mean, cumu_ret, share):
        plt.figure()
        n, bins, patch = plt.hist([cumu_ret])
        plt.title('Distribution of Outcomes for ' + share + ' Share in 10000 Trials with Mean')
        plt.xlabel('Outcomes 1(win) or -1(loss) for Each Trial')
        plt.ylabel('Number of Outcomes')
        plt.axhline(float(mean), color = 'r')
        plt.savefig(filename)
        plt.close()
        
        
        
        
        
        
        
        
        
        
        
          
        