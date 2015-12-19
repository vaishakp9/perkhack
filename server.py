from flask import Flask,render_template ,current_app,jsonify,url_for,redirect,request
import subprocess,requests,json,webbrowser
import codecs
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
token = ""
name = ""


app=Flask(__name__,static_url_path="")
#app.debug=True

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
	

@app.route('/resto',methods=['GET'])
def resto():
	request.headers
	uid = request.headers.get('uid')
	if (uid=='1'):
		name = "Perk.com,"
		level = "Michelin 1,"
		message = "Enjoyed Perk.com and its awesome service"
		csv1 = name+level+message
		return (csv1)
	if (uid=='2'):
		name = "Caffe Pascucci,"
		level = "Michelin 2,"
		message = "The gourmet delicacies were a big draw ! Great job."
		csv1 = name+level+message
		return (csv1)
	if (uid=='3'):
		name = "Mainland China,"
		level = "Michelin 3,"
		message = "The food was delectable. Try it out, guys !"
		csv1 = name+level+message
		return (csv1)
	else:
		return ("NULL")
@app.route('/weight',methods=['GET'])
def weights():
	request.headers
	object_id = request.headers.get('object_id')
	url1 = "https://graph.facebook.com/v2.3/"+object_id+"/likes?access_token=CAACEdEose0cBAKRKgIOBPDDXsr4WiTcTwO32OG0cFivSJ6LrEW1KbkHFqo1dWSE6PJjhgar91r6ZBEseVVx07pZAe4oSZAZANnr39ZB9ZAQ3XEf1pPM4BYrbb1L7xavPEc1JDET89XDBFlqpcYZAKNZCCleGd1ioO3aLvlkEGnCpnAhehPZAZCE04SEnq09YiWsRPOsoUMZCZCk7vAZDZD"
	r1 = requests.get(url1)
	json_data = r1.json()
	json_data = json_data["data"]
	number = len(json_data)
	#print(txt)
	return (str(number))



@app.route('/test',methods=['POST','GET'])
def test():
	request.headers
	text = request.headers.get('text')
	sentiment = text
	url1 = "https://graph.facebook.com/v2.3/1223469374334702/likes?access_token=CAACEdEose0cBAKRKgIOBPDDXsr4WiTcTwO32OG0cFivSJ6LrEW1KbkHFqo1dWSE6PJjhgar91r6ZBEseVVx07pZAe4oSZAZANnr39ZB9ZAQ3XEf1pPM4BYrbb1L7xavPEc1JDET89XDBFlqpcYZAKNZCCleGd1ioO3aLvlkEGnCpnAhehPZAZCE04SEnq09YiWsRPOsoUMZCZCk7vAZDZD"
	r1 = requests.get(url1)
	#print r1.json()
	json_data = r1.json()
	json_data = json_data["data"]
	print len(json_data)
	#r1 = json.loads(r1)
	#json_data = json_dumps(r1.text)
	#item_dict = json.loads(json_data)
	#number = len(item_dict)
	#print type(r2)
	url = "https://api.repustate.com/v3/dc88b08e3079785fd126e94a3633fbe817e8d07b/score.json"
	payload = {'text': text}
	r = requests.post(url,data=payload)
	sentiment = r.text

	#return render_template('index.html',**locals())
	#return (sentiment)
	number = len(json_data)
	#print(txt)
	return (str(number))

@app.route('/getSentiment',methods=['POST','GET'])
def getSentiment():
	request.headers
	text = request.headers.get('text')
	sentiment = text
	url = "https://api.repustate.com/v3/dc88b08e3079785fd126e94a3633fbe817e8d07b/score.json"
	payload = {'api_key': '0f87719617638ba4db6fe9d0e686e077', 'text': 'happy'}
	#r = requests.post(url, data=payload)
	return (r.text)
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

