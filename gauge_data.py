"""gauge_data.py - Getter and Setter functions for gauge data file

These functions are the only ones that should create, read, or write 
to the gauge data file. 

The gauge data file contains a json object as text. 
When the file is first created it has default values
If more values are added, be sure to add defaults

2018-12-16 steveberl@gmail.com 
The current implementation has potential for race conditions. 
It should be improved :-)

TODO - 
Make this into a class to better encapsulate
Avoid race conditions

"""

import os
import errno
import json

gauge_data_dir = "/tmp/"
gauge_data_file = gauge_data_dir + "ls_gauge_data.json"

def create_default_gauge_data():
    """Create a new gauge data file"""
    data = {}
    # Set up default values
    data['temperature'] = 70 #Degrees Fahrenheit
    data['humidity'] = 60    #Percentage
    data['pressure'] = 29.8  #Inches of mercury Hg

    # print("Creating new data file")
    with open(gauge_data_file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')
        outfile.close()
        return data

def get_gauge_data():
    """Returns a dictionary containing the gauge data"""
    try:
        json_file = open(gauge_data_file, 'r')
    except IOError as error:
        print("Error opening json file: ", error)
        if error.errno == errno.ENOENT:
            return create_default_gauge_data()
    else:
        with json_file:  
            data = json.load(json_file)
            json_file.close()
            return data

def set_gauge_data(data):
    """Sets the content of the gauge data file using 
    data from dictionary parameter
    """
    
    with open(gauge_data_file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')
    return data
    
    
