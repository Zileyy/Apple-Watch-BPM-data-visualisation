#IMPORTS
import util
import os

#MAIN
try:
    #'sample' is number of samples that program is going show (0 - is going to show whole sample)
    sample = int(input('Enter number of samples you want to see (type \'0\' if you want to see whole sample): '))
except:
    raise 'Wrong input! Use whole numbers!'

#Run visualise from util with generated Pandas DataFrame from export.xml
util.visualise(util.getDF(sample))

#Pausing program to prevent CMD from shutting down instantly
os.system('pause')