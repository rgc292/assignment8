'''
Created on Nov 6, 2015

@author: Rafael Garcia (rgc292)
'''

import business as bs
import matplotlib.pyplot as plt
import numpy as np


"""This main file is intended to implement the program for calculating the
    investment simulations for a user"""


if __name__ == '__main__':
    pass

while True:
    #A business object is created
    business = bs.Calculation()

    #Interaction explanation 
    print "You will need to type the amount of shares to buy individually."
    print "Please type the amounts for shares costing $1, $10, $100, and/or $1000."
    print "At last, You will need to type the desired number of trials!\n"

    #It reads, validates, and stores users' input 
    for iterator in range(5):
        business.position.append(business.validate_input())
    
    
    #It sets the value per position
    business.set_position_value()

    #It generates a list of 4 arrays being each array 
    #referent to the trials of each share [[trials $1],[trials $10],
    #[trials $100],[trials $1000]]
    business.build_daily_ret(1)
    business.build_daily_ret(10)
    business.build_daily_ret(100)
    business.build_daily_ret(1000)


    print "\nMean for each share: [$1, $10, $100, $1000]"
    print business.mean_daily_return()
    print "\nStandard Deviation for each share: [$1, $10, $100, $1000]" 
    print business.std_daily_return()
    print "\n"
    cumu = business.cumu_ret

    resultsFile = open('results.txt','w')
    resultsFile.write("Trial Result:\n " + 
        "Format: [[for $1],[for $10],[for $100],[for $1000]]\n " + str(cumu) + 
        "\n" + "\nMean:" + "\nFormat: [for $1, for $10, for $100, for $1000]\n" + 
        str(business.mean) + "\n\nStd:" + 
        "\nFormat: [for $1, for $10, for $100, for $1000]\n" + 
        str(business.std) + "\nEnd")
    resultsFile.flush()

    #It plots a histogram for each position and save as a .pdf file
    business.plot_results('histogram_0001_pos.pdf', business.mean[0], 
                          business.cumu_ret[0], '$1')
    business.plot_results('histogram_0010_pos.pdf', business.mean[1], 
                          business.cumu_ret[1], '$10')
    business.plot_results('histogram_0100_pos.pdf', business.mean[2], 
                          business.cumu_ret[2], '$100')
    business.plot_results('histogram_1000_pos.pdf', business.mean[3], 
                          business.cumu_ret[3], '$1000')
