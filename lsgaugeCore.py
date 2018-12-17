""" filename: lsgaugeCore.py - Core of the life support gauge display app.

"""

import os
import datetime
import sys

from flask import Flask, render_template, flash, request

import gauge_data

CURRENTDIR = os.path.dirname(__file__)
BASEDIR    = os.path.dirname(CURRENTDIR)

class LSGaugeCore():

    def index(self,request):
        myrole = request.args.get('role', '')
        if myrole == "commander":
            html = self.doCommander(request)
            return html

        elif myrole == "getdata":
            html = self.doGetData()
            return html

        elif myrole == "station":
            html = self.doStation()
            return html

        else:
            html = self.doStation()
            return html

            
    def doStation(self):
        html = render_template("lsgauge_station_template.html")
        return html

    def doGetData(self):
        current_data = gauge_data.get_gauge_data()
        html = render_template("lsgauge_gauge_data_template.html", data=current_data)
        return html

    def doCommander(self, request):
        if request.method == 'POST':
            new_temperature = request.form['new_temperature']
            new_humidity = request.form['new_humidity']
            new_pressure = request.form['new_pressure']
            newdata = {'temperature': new_temperature,
                       'humidity': new_humidity,
                       'pressure': new_pressure
                       }
            gauge_data.set_gauge_data(newdata)
            
        current_data = gauge_data.get_gauge_data()
        html = render_template('lsgauge_commander_template.html', data = current_data)
        return html

if __name__ == "__main__":
    print("Hello World");
