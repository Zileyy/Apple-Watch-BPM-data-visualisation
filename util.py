#IMPORTS
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import pandas as pd
import plotly.express as px

#VARS
tree = ET.parse('export.xml')     
root = tree.getroot()
lista = {'time':[],'bpm':[]}

#Function that return DF of wanted data
#'sample' is number of samples that program is going to show
def getDF(sample):
    #Get information from "InstantaneousBeatsPerMinute" and sort it propperly for turning into Pandas DataFrame
    for hr in root.iter('InstantaneousBeatsPerMinute'):
        lista['time'].append(hr.attrib['time'][0:5])
        lista['bpm'].append(hr.attrib['bpm'])
        
    #Create Pandas Dataframe with infromation of time and bpm
    df = pd.DataFrame(data=lista)
    #Set "time" as index of DataFrame
    df = df.set_index('time')
    #Convert bpm from object to numeric value (int)
    df['bpm'] = df['bpm'].astype(int)

    #If sample equals to zero program will show whole dataset
    if sample == 0: return df
    else: return df.head(sample)

#Function that shows Pandas DataFrame as a graph
def visualise(df):    
    #Plot DataFrame containing heartbeat data
    df.plot()
    plt.show() 