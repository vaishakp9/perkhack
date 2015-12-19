#!/Python34/python
#print ("Content-Type: text/html\n\n");
import cgi
import json
import requests
#import sys

#import cgi, cgitb 
#cgitb.enable()  # for troubleshooting
#import sys
#the cgi library gets vars from html
#data = cgi.FieldStorage()
#this is the actual output
#token=sys.argv[1]
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
def parseJSON(ACCESS_TOKEN):
    base_url = 'https://graph.facebook.com/me'
    fields = 'books.rates'
    #print ("DAMNNNN")
    url = '%s?fields=%s&limit=100&access_token=%s' %(base_url, fields, ACCESS_TOKEN,)
    content = requests.get(url).json()
    json_data = content
    json_file = open("MainDatabase.json","r+")
    json_str = json_file.read()
    json_d = json.loads(json_str)
    loc = json_file.tell()
    json_file.seek(loc-2)
    if json_data["books.rates"]["data"][0]["from"]["name"] not in json_d.keys():
      if "error" not in json_data.keys():
         m=len(json_data["books.rates"]["data"])
         json_file.write(",\n   \"%s\":{\n" %(json_data["books.rates"]["data"][0]["from"]["name"]))
         for i in range (0,m-1):
              json_file.write("\t\"%s\":%d,\n"%(json_data["books.rates"]["data"][i]["data"]["book"]["title"],json_data["books.rates"]["data"][i]["data"]["rating"]["value"]))
         json_file.write("\t\"%s\":%d\n"%(json_data["books.rates"]["data"][m-1]["data"]["book"]["title"],json_data["books.rates"]["data"][m-1]["data"]["rating"]["value"]))
         json_file.write("     }\n}")
      
        
    json_file.close()

#token="CAAGGHzq3tgoBAOGfqWKLY3OYcPcM4fcBAxVUIAkhQNVVxauPofbaC156nmwstZAvBu1K2z6ZC3K0bu34zhOEFcYrZBNmQHdAvdQz7wDEjmFVKEDQ3t0GLpRpxZATHhkeY1V4Qz4S5RXmvifa6ic1OwrGg4SsKcFOXhHZCiaiCBXpvVbzOXtUPCkehffOxZCzUkkcV4ldiYDq083Ug1TcTAReZARTC9ZBxq0ZD"
#parseJSON(token)
