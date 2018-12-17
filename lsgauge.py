""" filename: lsgauge.py

    this is a wrapper for main program, its primary purpose is to 
    manage error messages and output your HTML, XML or JSON as required

    The flask framework is used to interface this code to the web server.
    For more info on flash look at http://flask.pocoo.org/

"""

from flask import Flask, request, make_response
application = Flask(__name__)

import traceback 
import os
import sys

CURRENTDIR = os.path.dirname(os.path.abspath(__file__))
if CURRENTDIR not in sys.path:
    sys.path.append(CURRENTDIR)
    
def wsErrorTextHTML(txt):
    ## displays the python error on the web page - useful for debugging
    ## but on a live system would have it save the error to a database
    ## and give the user an error number
    err = "<p>ERROR!</p>"
    err += "<pre>"+ txt + "</pre>"
    return err

@application.errorhandler(500)
def internalServerError(error): 
    err = "<p>ERROR! 500</p>"
    err += "<pre>"+ str(error) + "</pre>"
    err += "<pre>"+ str(traceback.format_exc()) + "</pre>"
    return err

# This next line is the main entry point for the lsgauge web application
# Flask takes care of linking this together. As it is below, the URL to
# access the web page will be http://servername/lsgauge
@application.route('/lsgauge', methods=['POST', 'GET'])
def indexApp():
    
    application.debug = 0
    try:
        ##
        ## The core code is in lsgaugeCore.py
        ##
        from lsgaugeCore import LSGaugeCore
        lsgaugeCore = LSGaugeCore()
        htmlData = lsgaugeCore.index(request)
        application.logger.debug(htmlData)
        
        ## output your html code
        response = make_response(htmlData)
        response.headers['Content-Type'] = 'text/html'
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    except:
        ## for when you get an error message
        response = make_response(wsErrorTextHTML(traceback.format_exc()))
        response.headers['Content-Type'] = 'text/html'
        return response

    response = make_response("unkown!")
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == "__main__":
    application.debug = True
    application.run()
