from flask import Flask,render_template ,current_app,jsonify,url_for,redirect,request
import subprocess,requests,json,webbrowser,csv,sys
import codecs
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
token = ""
name = ""


app=Flask(__name__,static_url_path="")
#app.debug=True

@app.route('/',methods=['POST','GET'])
def index():
	'''request.headers
	token = request.headers.get('token')
	name = request.headers.get('name')
	json_file = open('/Users/vaishakprashanth/invenio/name.txt','w')
	json_file.write(name)
	json_file.close()
	json_file = open('/Users/vaishakprashanth/invenio/token.txt','w')
	json_file.write(token)
	json_file.close()
	webbrowser.get(chrome_path).open_new('http://localhost:5421/books')'''
	return ("Welcome to PerkHack ! Devs : Suraj, Tushar, Vaishak, Vivek")
	

@app.route('/resto',methods=['POST'])
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
		return ("-1")
@app.route('/wait',methods=['POST'])
def weights():
	request.headers
	object_id = request.headers.get('object_id')
	url1 = "https://graph.facebook.com/v2.2/100010977690590_"+object_id+"/likes?access_token=CAACEdEose0cBAExv0ZCwQw8dJ3i6vbXR2aN266f0ORvXK8GOuy9lapisrqblD4V3hjZBZBX2q3uPxzvV7FZBlGUjMd2Gp1eFZA5XRqgCf3tYbsWeFQZAmJPUxKznkH82cZC8P3XymsNVC2Bj4Q83ffr5ORkT5OcGHf61gyJX7ZB2mowHNwssjM5uSR0sYRixbj9BoCB27UtOKQZDZD"
	r1 = requests.get(url1)
	json_data = r1.json()
	json_data = json_data["data"]
	number = len(json_data)
	#print(txt)
	print (str(number))
	return (str(number))
@app.route('/post_analyze',methods=['POST'])
def post_analyze():
	request.headers
	text = request.headers.get("text")
	url = "https://api.repustate.com/v3/dc88b08e3079785fd126e94a3633fbe817e8d07b/score.json"
	payload = {'api_key': '0f87719617638ba4db6fe9d0e686e077', 'text': text}
	r = requests.post(url, data=payload)
	json_data = r.json()
	json_data = json_data["score"]
	if(json_data>0.7 or json_data<-0.7):
		return ("PA3")
	if(json_data>0.4 or json_data<-0.4):
		return ("PA2")
	if(json_data>0.1 or json_data<-0.1):
		return ("PA1")
	return ("-1")
@app.route('/weight1',methods=['POST'])
def weights1():
	request.headers
	object_id = request.headers.get('object_id')
	url1 = "https://graph.facebook.com/v2.2/101238380252085?access_token=CAACEdEose0cBAExv0ZCwQw8dJ3i6vbXR2aN266f0ORvXK8GOuy9lapisrqblD4V3hjZBZBX2q3uPxzvV7FZBlGUjMd2Gp1eFZA5XRqgCf3tYbsWeFQZAmJPUxKznkH82cZC8P3XymsNVC2Bj4Q83ffr5ORkT5OcGHf61gyJX7ZB2mowHNwssjM5uSR0sYRixbj9BoCB27UtOKQZDZD"
	r1 = requests.get(url1)
	return (r1.text)

@app.route('/test',methods=['POST','GET'])
def test():
	request.headers
	text = request.headers.get('text')
	sentiment = text
	url1 = "https://graph.facebook.com/v2.3/1223469374334702/likes?access_token=CAACEdEose0cBAExv0ZCwQw8dJ3i6vbXR2aN266f0ORvXK8GOuy9lapisrqblD4V3hjZBZBX2q3uPxzvV7FZBlGUjMd2Gp1eFZA5XRqgCf3tYbsWeFQZAmJPUxKznkH82cZC8P3XymsNVC2Bj4Q83ffr5ORkT5OcGHf61gyJX7ZB2mowHNwssjM5uSR0sYRixbj9BoCB27UtOKQZDZD"
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
	payload = {'api_key': '0f87719617638ba4db6fe9d0e686e077', 'text': sentiment}
	r = requests.post(url, data=payload)
	json_data = r.json()
	json_data = json_data["score"]
	return (str(json_data))

@app.route('/testImg',methods=['POST'])
def testImg():
	link=request.headers.get('link')
	var = picMatch(link)
	return (str(var))

def picMatch(pic_link):     
        tag_dict= {'adult':1, 'alcohol':1, 'american lobster':1, 'animal':1, 'appetizer':1, 'art':1, 'arthropod':1, 'attractive':1, 'ball':1, 'barbecue':1, 'barroom':1, 'beef':1, 'beverage':1, 'black':1, 'bouquet':1, 'box':1, 'bread':1, 'breakfast':1, 'building':1, 'business':1, 'cafe':1, 'cake':1, 'candle':1, 'candles':1, 'candy':1, 'caucasian':1, 'celebration':1, 'chair':1, 'cheese':1, 'chicken':1, 'chocolate':1, 'chocolate sauce':1, 'christmas':1, 'close':1, 'coal':1, 'cocktail':1, 'color':1, 'colorful':1, 'computer':1, 'conch':1, 'container':1, 'cooking':1, 'counter':1, 'crab':1, 'cream':1, 'crustacean':1, 'cuisine':1, 'cup':1, 'currency':1, 'decoration':1, 'delicious':1, 'design':1, 'dessert':1, 'diet':1, 'dinner':1, 'dish':1, 'drink':1, 'easter':1, 'eat':1, 'eating':1, 'edible fruit':1, 'education':1, 'egg':1, 'eggs':1, 'ellipse':1, 'fire':1, 'fireplace':1, 'fish':1, 'flame':1, 'flower':1, 'food':1, 'fresh':1, 'fruit':1, 'fungus':1, 'gastropod':1, 'gift':1, 'glass':1, 'gourmet':1, 'grain':1, 'graphic':1, 'grill':1, 'grilled':1, 'gyromitra':1, 'hair':1, 'hand':1, 'hands':1, 'health':1, 'healthy':1, 'holiday':1, 'home':1, 'hot':1, 'hot pot':1, 'hotdog':1, 'ingredient':1, 'interior':1, 'invertebrate':1, 'king crab':1, 'kitchen':1, 'light':1, 'liquid':1, 'lobster':1, 'lunch':1, 'man':1, 'manhattan':1, 'martini':1, 'meal':1, 'meat':1, 'mixed drink':1, 'mollusk':1, 'money':1, 'nutriment':1, 'nutrition':1, 'orange':1, 'organism':1, 'package':1, 'packet':1, 'paper':1, 'party':1, 'pasta':1, 'pencil box':1, 'people':1, 'pepper':1, 'person':1, 'pin':1, 'plate':1, 'pomegranate':1, 'raw':1, 'receptacle':1, 'restaurant':1, 'rice':1, 'round':1, 'salad':1, 'sandwich':1, 'sauce':1, 'seafood':1, 'shell':1, 'snack food':1, 'source of illumination':1, 'spa':1, 'space':1, 'starfish':1, 'stew':1, 'structure':1, 'sushi':1, 'sweet':1, 'symbol':1, 'table':1, 'tabletop':1, 'tasty':1, 'tea':1, 'tomato':1, 'tray':1, 'vegetable':1, 'wealth':1, 'yellow':1, 'brown':1, 'sugar':1, 'soup':1, 'bowl':1, 'emblem':1, 'purse':1, 'old':1, 'bag':1, 'bar':1, 'pizza':1, 'object':1, 'condiment':1, 'flavorer':1, 'trifle':1, 'vegetables':1, 'perfume':1, 'bottle':1, 'toiletry':1, 'gold':1, 'oil':1, 'menu':1, 'fare':1, 'wine':1, 'wineglass':1, 'rotisserie':1, 'oven':1, 'banquet':1, 'pan':1, 'happy':1, 'yogurt':1, 'dairy product':1, 'bbq':1, 'texture':1, 'vintage':1, 'acorn squash':1, 'winter squash':1, 'squash':1, 'produce':1, 'pineapple':1, 'spatula':1, 'knife':1, 'turner':1, 'cooking utensil':1, 'wallet':1, 'pudding':1, 'course':1, 'glassware':1, 'goblet':1, 'meat loaf':1, 'loaf of bread':1, 'baked goods':1, 'case':1, 'zucchini':1, 'summer squash':1, 'xmas':1, 'sphere':1, 'snack':1, 'aquarium':1, '3d':1, 'glasses':1, 'technology':1, 'room':1, 'eggnog':1, 'punch':1, 'milk':1, 'bubble':1, 'water':1, 'globule':1, 'world':1, 'coffee':1, 'espresso':1, 'kitchen appliance':1, 'home appliance':1, 'delicious:1''adult':1, 'healthy:1''hall':1, 'house':1, 'scorpion':1, 'rock crab':1, 'arachnid':1, 'hermit crab':1, 'skin':1, 'body covering':1, 'holding':1, 'consomme':1, 'summer':1, 'flowers':1, 'natural':1, 'meat:1''shield':1, 'clock':1, 'protective covering':1, 'pick':1, 'sign':1, 'armor':1, 'present':1, 'refreshment':1, 'phonograph record':1, 'frying pan':1, 'gong':1, 'circle':1, 'juice':1, 'cappuccino':1, 'mug':1, 'lifestyle':1, 'expression':1, 'cute':1, 'smile':1, 'happiness':1, 'restaurant:1''relaxation':1, 'display':1, 'sour':1, 'cold':1, 'guacamole':1, 'spiny lobster':1, 'crayfish':1, 'insect':1, 'ant':1, 'ice':1, 'board':1, 'spoon':1, 'lager':1, 'beer':1, 'champagne':1, 'wok':1, 'strawberry':1, 'echinoderm':1, 'puzzle':1, 'finger':1, 'jigsaw puzzle':1, 'spice':1, 'sea:1''porcelain':1, 'china':1, 'tableware':1, 'digital clock':1, 'icon':1, 'bright':1, 'lamp':1, 'nut':1, 'savings bank':1, 'piggy bank':1, 'piggy':1, 'bank':1, 'finance':1, 'savings':1, 'financial':1, 'pig':1, 'plant':1, 'leaf':1, 'jellyfish':1, 'season':1, 'lantern':1, 'onion':1, 'hip':1, 'chili':1, 'starches':1, 'painting':1, 'paint':1, 'child':1, 'childhood':1, 'kid':1, 'creativity':1, 'silhouette':1, 'crowd':1, 'audience':1, 'lights':1, 'event':1, 'concert':1, 'stadium':1, 'patriotic':1, 'nation':1, 'digital':1, 'fractal':1, 'futuristic':1, 'fantasy':1, 'wallpaper':1, 'shape':1, 'laser':1, 'optical device':1, 'pattern':1, 'flag':1, 'vestment':1, 'gown':1, 'kimono':1, 'clothing':1, 'outerwear':1, 'robe':1, 'garment':1, 'consumer goods':1, 'covering':1, 'dark':1, 'doughnut':1, 'friedcake':1, 'furniture':1, 'light-emitting diode':1, 'diode':1, 'shiny':1, 'dough':1, 'game':1, 'artwork':1, 'religion':1, 'ancient':1, 'wooden spoon':1, 'berry':1, 'hat':1, 'sombrero':1, 'headdress':1, 'dutch oven':1, 'kitchen utensil:1''modern':1, 'globe':1, 'beer glass':1, 'diet:1'"jack-o'-lantern":1, 'pumpkin':1, 'consumer':1, 'male':1, 'bartender':1, 'breakfast:1''whiskey':1, 'jar':1, 'beaker':1, 'creation':1, 'face':1, 'smiling':1, 'equipment':1, 'compact disk':1, 'dial telephone':1, 'internet':1, 'juicy':1, 'burning':1, 'new':1, 'card':1, 'traditional':1, 'confectionery':1, 'lighter':1, 'device':1, 'success':1, 'ice cream':1, 'dining table':1, 'ornament':1, 'salad:1''timepiece':1, 'metal':1, 'public house':1, 'mousetrap':1, 'trap':1, 'pool table':1, 'game equipment':1, 'cook':1, 'dungeness crab':1, 'stinkhorn':1, 'carrot':1, 'greens':1, 'lettuce':1, 'bakery':1, 'cherry':1, 'apple':1, 'dainty':1, 'cucumber':1, 'asparagus':1, 'clog':1, 'golden':1, 'vitamin':1, 'basket':1, 'hamper':1, 'disk jockey':1, 'broadcaster':1, 'communicator':1, 'baked':1, 'freshness':1, 'fruit:1''cuisine:1''goldfish':1, 'eft':1, 'makeup':1, 'rouge':1, 'powder':1, 'face powder':1, 'cosmetic':1, 'cabaret':1, 'spot':1, 'place of business':1, 'night':1, 'vase':1, 'honey':1, 'sweetening':1, 'conserve':1, 'shop':1, 'mercantile establishment':1, 'stall':1, 'entree':1, 'toast':1, 'stove':1, 'fresh:1''disco':1, 'establishment':1, 'ballroom':1, 'melon':1, 'gourmet':1}

        tag_list=[]
        '''
        requrls = []
        with open('pic_test.csv','r') as f:
                reader = csv.reader(f)
                for row in reader:
                    requrls.append(row[0])
        '''
        url = "http://api.imagga.com/v1/tagging"

        #requrl = 'https://scontent.fmaa1-2.fna.fbcdn.net/hphotos-xlf1/v/t1.0-9/12360163_1002721083103232_2983133825651369852_n.jpg?oh=8d361a7140ab1eef3582166490b08286&oe=56D8F7C6' 
        querystring = {"url": str(pic_link),"version":"2"}

        headers = {
            'accept': "application/json",
            'authorization': "Basic YWNjXzZlMTc3Y2RmMmE2YTdiMzplY2RkNjJlN2NkNDI3YjQ3OWZlOGE2NzVkMjlkN2Q0Zg=="

            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        q = response.text
        q = json.loads(q)

        try:
            if(len(q["results"]) == 0):
                print (requrl)
                print (",")
                print ("Image doesn't exist")

            else:
                #print (str(requrl))
                """
                if(len(q['results'][0]["tags"]) < 10):
                    for i in range(0,len(q['results'][0]["tags"])):
                        try:
                        print ("," + str(q['results'][0]["tags"][i]['tag']) + "(" + str(q['results'][0]["tags"][i]['confidence']) + ")" + ","),
                    print ""
                else:
                    """
                for i in range(0,10):
                    try: 
                        tag_list.append(str(q['results'][0]["tags"][i]['tag']))
                    except:
                        break
        except:
            pass            
            #print ("")
        flag=0
        for j in tag_list:
            try:
                if(tag_dict[j]==1):
                    flag=1
                    break
            except:
                break
        if(flag==0):
            return 0
        else:
            return 1
if __name__ =='__main__' :
	app.run(host="0.0.0.0",port=5992)

