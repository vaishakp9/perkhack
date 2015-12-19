from flask import Flask,render_template ,current_app,jsonify,url_for,redirect,request
import subprocess,requests,json,webbrowser,Parse
import codecs
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
token = ""
name = ""


app=Flask(__name__,static_url_path="")

@app.route('/',methods=['POST','GET'])
def index():
	request.headers
	token = request.headers.get('token')
	name = request.headers.get('name')
	json_file = open('/Users/vaishakprashanth/invenio/name.txt','w')
	json_file.write(name)
	json_file.close()
	json_file = open('/Users/vaishakprashanth/invenio/token.txt','w')
	json_file.write(token)
	json_file.close()
	webbrowser.get(chrome_path).open_new('http://localhost:5421/books')
	return ("LOPS")
	


@app.route('/test')
def test():
	return render_template('index.html',**locals())
@app.route('/books')
def getbooks():
	json_file = open('/Users/vaishakprashanth/invenio/name.txt','r+')
	name1 = json_file.read()
	print(name1)
	json_file.close()
	json_file = open('/Users/vaishakprashanth/invenio/token.txt','r+')
	token1 = json_file.read()
	json_file.close() 
	print(token1)
	Parse.parseJSON(token1)
	#print(name)
	data=bookrec.recomend(name1)
	books=[]
	for i in data:
		books.append(i[1]+ ' book')
	print(books)
	req="http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="
	images=[]
	nameee = name1
	for i in books:
		urlify=req + i
		resp=requests.get(urlify)
		a=resp.json()
		images.append( a['responseData']['results'][0]['unescapedUrl'])

	#contents = render_template('index.html',**locals())
	#json_file = open('/Users/vaishakprashanth/invenio/index.html','w')
	#json_file.write(contents)
	#json_file.close()
	#webbrowser.open_new('localhost:5421/index.html')
	return render_template('index.html',**locals())




if __name__ =='__main__' :
	app.run(host="0.0.0.0",port=5421)

