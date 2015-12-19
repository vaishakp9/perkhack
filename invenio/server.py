from flask import Flask,render_template ,current_app,jsonify,url_for,redirect
import subprocess,bookrec,requests,json,webbrowser,Parse


app=Flask(__name__,static_url_path="")

@app.route('/')
def index():
	a=json.dumps('meta-data')
	webbrowser.open_new('http://127.0.0.1:5555/books')
	


@app.route('/books',methods=['GET','POST'])
def getbooks():
	#request.headers
	#token = request.form.get('token')
	#name = request.form.get('name')
	Parse.parseJSON('CAACEdEose0cBAAl1fnGLRN0FrN1FOifCuvD78c99OqZB1tGOBa4fLox9swMcQe80c5ADUwwB3OaECkIs6aItViRxwBmZBxMvGq5wZAjo1ZCXUBdT6MwJtZCWPVlm0QGGfZBOFMZCiHEjFKTSZAKCeDivJYDSPn1SEZAOnDBGtkA0WPIwSnZAvrYku8rrkyphAKxragpXwx10uymwZDZD')
	data=bookrec.recomend('Vaishak Prashanth')
	books=[]
	for i in data:
		books.append(i[1]+ ' book')
	print(books)
	req="http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="
	images=[]
	nameee = name
	for i in books:
		urlify=req + i
		resp=requests.get(urlify)
		a=resp.json()
		images.append( a['responseData']['results'][0]['unescapedUrl'])

	return render_template('index.html',**locals())




if __name__ =='__main__' :
	app.run(host="127.0.0.1",port=5555)

