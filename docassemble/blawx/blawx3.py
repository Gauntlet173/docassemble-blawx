# This is the third version of an integration between Docassemble and Blawx
# By Jason Morris of Round Table Law
# @RoundTableLaw on Twitter
# See www.blawx.com for details on Blawx, Drag and Drop AI for Legal Rules

from docassemble.base.core import DAObject, DAStaticFile
from docassemble.base.functions import log, all_variables
import requests
from urllib import urlencode
import json

class Blawx(DAObject):
  
  def init(self, *pargs, **kwargs):
    super(Blawx, self).init(*pargs, **kwargs)
    
  def ask(self, blawxfile):
    # This function sends a request to the Blawx reasoner online, passing a 
    # blawxfile as 'code' and a JSON representation of the docassemble variables
    # as 'data', and returns the response as a Python object.
    #
    # The blawxfile parameter is the name of a .blawx file located in the static
    # folder of the current docassemble package.
    #
    # The response is in this format:
    # { 'main': 'Yes' (or 'No'),
    #   'answers': {
    #     '1': {
    #       'variable_name': value,
    #       etc...
    #      }
    #    }
    #  }
    #
    # Answers will not exist if the query was a yes/no query, or if it was a search
    # query that returned no results.
    
    daFile = DAStaticFile(filename=blawxfile)
    file = open(daFile.path())
    if file.mode == 'r':
      blawx_code = file.read()
      file.close()
    else:
      log("Error opening blawx file. Please ensure it is placed in the 'Static' section of your Docassemble package, or playground.", "error")
      file.close()
    
    # put the docassemble variables into JSON
    blawx_data = json.dumps(all_variables())
    
    # Build the request
    payload = {'data': blawx_data, 'code': blawx_code}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://www.blawx.com/cgi-bin/reasoner6.php'
    
    # Post the request
    r = requests.post(url,headers=headers,data=payload)
    output = r.json() 
    return output