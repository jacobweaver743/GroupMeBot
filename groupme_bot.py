‘’’
You suck at coding if you’re reading this.
‘’’
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from groupy.client import Client
from groupy import attachments
import time
from weather import Weather, Unit
import random
import whitmireisgay
import requests
import re
import datetime
import giphy_client
from giphy_client.rest import ApiException
import sys
import check_apts_import
import json
import os

client = Client.from_token('s8nF3pqk8amht40XY0oCY0HDOx9vyZgQPN10N5Di')
groups = list(client.groups.list())
group = groups[0]
print(group)
bots = client.bots.list()
b = 2
print(bots[b])
supersand = bots[b]
botname = bots[b].name

def get_weather():
	weather = Weather(unit=Unit.FAHRENHEIT)
	weath_message = ""
	lookup = weather.lookup(2420165)
	forecasts = lookup.forecast
	for x in range(3):    
    	#for forecast in forecasts:
    	weath_message += str(forecasts[x].date)
    	weath_message += "\n"
    	weath_message += str(forecasts[x].text)
    	weath_message += "\n"
    	weath_message += str('High: ' + forecasts[x].high)
    	weath_message += "\n"
    	weath_message += str('Low: ' + forecasts[x].low)
    	weath_message += "\n"
   	 
	return(weath_message)

def sgt_email():
	sgt_mail = ""
	sgt_mail += 'kahmeelah.n.lyons.mil@mail.mil'
	sgt_mail += "\n"
	sgt_mail += 'alberto.rueda.mil@mail.mil'
	sgt_mail += "\n"
	sgt_mail += 'clay.a.hines.mil@mail.mil'
	sgt_mail += "\n"
	sgt_mail += 'eliseo.correamacias.mil@mail.mil'
	sgt_mail += "\n"
	sgt_mail += 'francisco.j.estrada12.mil@mail.mil'
	sgt_mail += "\n"
	sgt_mail += 'michael.a.fink3.mil@mail.mil'
    
	return(sgt_mail)

def new_to_group(s):
	if re.search(new_to_group_regex, str(s)):
    	return(True)
	else:
    	print("you suck at coding")
    
def appointments_add(s):
	if re.search(app_regex, str(s)):
    	apt = str(s)[13:]
    	with open('Appointments.txt', 'a') as f:
        	f.write(apt + "\n")
    	yeet = "Appointment successfully added"
	else:
    	yeet = ("Correct format is: !appointment name location month dd hh:mm")
	return(yeet)
    
def appointments_get():
	check_apts_import.check_apts()
	with open('Appointments.txt', 'r') as f:
    	yeet = f.read()
	return(yeet)

def norris_joke():
	response = requests.get("https://api.chucknorris.io/jokes/random")
	data = response.json()

	return(data['value'])

def swanson_joke():
	response = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
	data = response.json()
    
	return(data[0])

def dad_joke():
	response = os.popen('curl -H "Accept: text/plain" https://icanhazdadjoke.com/').read()
	return(response)

def get_commands():
	c = ''
	c += 'More commands to come'
	c += "\n"
	c += '!weather - Gets forecast for the next 3 days'
	c += "\n"
	c += '!temp - Gets current temp and condition'
	c += "\n"
	c += '!sgt - Prints PSGTs email addresses'
	c += "\n"
	c += '!address - Prints the mailing address'
	c += "\n"
	c += '!appointment - add an appointment'
	c += "\n"
	c += '!appointments - list current appointments'
	c += "\n"
	c += '!numbers - Gets important numbers'
	c += "\n"
	c += '!ace - Gets ace card'
	c += "\n"
	c += '!nfg - Upload a picture of the fireguard roster(!nfg image)'
	c += "\n"
	c += '!fg - Get last uploaded fireguard picture'
	c += "\n"
	c += '!npt - Upload a picture of the pt schedule(!npt image)'
	c += "\n"
	c += '!pt - Get last uploaded pt schedule picture'
	c += "\n"
	c += '!fun - Fun commands!'
	c += "\n"
	c += '!pass - Gets emails of people working at the company (for pass and leave stuff)'
	return(c)

def get_gif(query):
	print(str(query))
	if re.search(gif_regex, str(query)):
    	api_instance = giphy_client.DefaultApi()
    	api_key = 's8nF3pqk8amht40XY0oCY0HDOx9vyZgQPN10N5Di'
    	q = query[4:]
    	limit = 5
    	offset = 0
    	rating = 'pg'
    	lang = 'en'
    	fmt = 'yeet'
    	try:
        	# Search Endpoint
        	print(q)
        	api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang)
        	if len(api_response.data) == 0 or len(api_response.data) == '0':
            	response = 'No gifs found'
            	return(response)
        	else:
            	image = (api_response.data[random.randint(0,len(api_response.data))].images.fixed_height_downsampled.url)
            	return(image)
    	except ApiException as e:
        	print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
	else:
    	fault = "Correct format: !gif word or !gif word+word"
    	return(fault)

def happy_birthday():
	None

def update_lopez(link):
	with open('Lopez.txt', 'w') as f:
    	f.write(link)
    	f.close()

def get_lopez():
	with open('Lopez.txt', 'r') as f:
    	link = f.read()
    	print(link)
    	f.close()
    	return(link)

def update_fireguard(link):
	with open('Fireguard_Link.txt', 'w') as f:
    	f.write(link)
    	f.close()
    
def get_fireguard():
	with open('Fireguard_Link.txt', 'r') as f:
    	link = f.read()
    	print(link)
    	f.close()
    	return(link)
    
def magic_ball(s):
	if re.search(magic_regex, str(s)):
    	response = {'1' : 'It is certain', '2' : 'It is decidedly so', '3' : 'Without a doubt', '4' : 'Yes definitely', '5' : 'You may rely on it', '6' : 'Reply hazy try again', '7' : 'Ask again later', '8' : 'Better not tell you now', '9' : 'Cannot predict now', '10' : 'Concentrate and ask again', '11' : 'Don\'t count on it', '12' : 'My reply is no', '13' : 'My sources say no', '14' : 'Outlook not so good', '15' : 'Very doubtful'}
    	return(response[str(random.randint(1, 15))])
	else:
    	return('Correct format: !8ball question')
   	 
def word_day():
	response = ""
	word = requests.get('http://urban-word-of-the-day.herokuapp.com/today')
	meaning = str(word.json()['meaning']).replace('\n','')
	example = str(word.json()['example']).replace('\n','')
	response += ("Word of the day:\n" + str(word.json()['word']))
	response += "\n"
	response += ("Meaning:\n" + meaning)
	response += "\n"
	response += ("Example:\n" + example)
	return(response)

def fun_commands():
	c = ''
	c += 'More commands to come'
	c += "\n"
	c += '!chuck - Gets a random Chuck Norris joke'
	c += "\n"
	c += '!ron - Gets a random Ron Swanson quote'
	c += "\n"
	c += '!pttest - Tells you how you\'ll do on your next pt test'
	c += "\n"
	c += '!autism - Sorrento'
	c += "\n"
	c += '!gif - Gets a gif from a phrase'
	c += "\n"
	c += '!8ball - Ask it a question'
	c += "\n"
	c += '!wotd - UrbanDictionary word of the day, nsfw? You asked for it.'
    
	return(c)

def current_temp():
	weather = Weather(unit=Unit.FAHRENHEIT)
	weath_message = ""
	lookup = weather.lookup(2420165)
	temp = lookup.condition.temp
	condition = lookup.condition.text
	weath_message += str(temp) + "\n"
	weath_message += str(condition) + "\n"
	return(weath_message)

def get_pt():
	with open('Pt_Schedule.txt', 'r') as f:
    	link = f.read()
    	print(link)
    	f.close()
    	return(link)
   	 
def update_pt(link):   	 
	with open('Pt_Schedule.txt', 'w') as f:
    	f.write(link)
    	f.close()

def post(thing_to_post):
	time.sleep(1)
	supersand.post(thing_to_post)
baddies = ['shit','fuck','asshole','retard',' bitch','slut','whore']
magic_regex = r"!8ball .*"
new_to_group_regex = r".+added.+to the group."
month_int = {'january' : '1', 'february' : '2', 'march' : '3', 'april' : '4', 'may' : '5', 'june' : '6', 'july' : '7', 'august' : '8', 'september' : '9', 'october' : '10', 'november' : '11', 'december' : '12'}	 
gif_regex = r"!gif \w+(\+\w+)*$"
app_regex = r"!appointment ([a-zA-Z])\w+ ([a-zA-Z])\w+ ([a-zA-Z])\w+ \d\d? \d\d:\d\d$"
temp = '!weather'
new_appointments = ""    

def reply(data):
	try:
    	last_message = data
    	if str(botname).lower() not in str(data['name']).lower():
        	if '!weather' in str(last_message).lower():
            	yeet = get_weather()
            	post(yeet)
        	elif '!sgt' in str(last_message).lower():
                	yeet = sgt_email()
                	post(yeet)
        	elif 'suicide' in str(last_message).lower() or 'kill ' in str(last_message).lower():
                	post('On call chaplain: CPT KIHIU 708-791-7835')
            	#elif '!meme' in str(last_message).lower():
                	#   yeet = meme()
                	#  post(yeet)'''
        	elif '!address' in str(last_message).lower():
            	post("Last, First M\nB CTB, 15th Sig BDE\n616 Barnes Ave bldg 25705 R#\nFort Gordon, GA 30905")
        	elif '!appointment ' in str(last_message).lower():
            	yeet = appointments_add(last_message['text'])
            	post(yeet)
            	'''
            	yeet = appointments_add(last_message.text)
            	new_appointments += (yeet + "\n")
            	print(new_appointments)
            	'''
            	repeat = last_message
        	elif '\'!appointments\'' in str(last_message):
            	yeet =appointments_get()
            	if yeet != "":
                	post(yeet)
            	else:
                	post('There are no appointments')
        	elif '!chuck' in str(last_message).lower():
            	yeet = norris_joke()
            	post(yeet)
       	#elif '!taylor' in str(last_message).lower():
         	#   post("Wahh!!")
        	elif '!ron' in str(last_message).lower():
            	yeet = swanson_joke()
            	post(yeet)
        	elif '!commands' in str(last_message).lower():
            	yeet = get_commands()
            	post(yeet)
        	elif '!autism' in str(last_message).lower():
            	post('Sorrento')
            	post('https://i.groupme.com/960x716.jpeg.5baaaff3b6b84dc19ae97a8b3ac8e5d3.large')
        	elif '!sorrento' in str(last_message).lower():
            	post('Autism')  
        	elif '!pttest' in str(last_message).lower():
            	if 'bot_daddy' in str(last_message).lower():
                	post('300! Wowee!')
            	else:
                	post('You failed! Loser.')
        	elif '!campise' in str(last_message).lower():
            	post('https://i.groupme.com/873x1552.jpeg.cc0ea5b0010044dc9281b95cccb12b0d.large')
        	elif '!numbers' in str(last_message).lower():
            	post('https://i.groupme.com/722x1280.jpeg.fe019b0465924c29ad51d19b2eaff432.large')
        	elif '!ace' in str(last_message).lower():
            	post('https://i.groupme.com/1488x1984.jpeg.e05fe06b3eef4944b78f510f717bb8d0.large')
        	elif '!gif' in (str(last_message)).lower():
            	yeet = get_gif(last_message['text'])
            	post(str(yeet))
        	elif 'added' in str(last_message).lower():
            	if 'groupme' in str(last_message.name).lower():
                	yeet = new_to_group(last_message['text'])
                	if yeet == True:
                    	post("Welcome to the \'fun\'!\nHere are some commands that you can enter.")
                    	post(get_commands())
        	elif '!foundlopez' in str(last_message).lower():
            	update_lopez(str(last_message['attachments'][0]['url']))
        	elif '!whereislopez' in str(last_message).lower():
            	link = get_lopez()
            	post(str(link))
        	elif '!nfg' in str(last_message).lower():
            	update_fireguard(str(last_message['attachments'][0]['url']))
        	elif '!fg' in str(last_message).lower():
            	link = get_fireguard()
            	post(str(link))
            	#else:
                	#   supersand.post('Nobody has added a fg roster')
        	elif '!8ball' in str(last_message).lower():
            	yeet = magic_ball(last_message['text'])
            	post(yeet)
        	elif '!joke' in str(last_message).lower():
            	yeet = dad_joke()
            	post(yeet)
        	elif '2+2=4' in str(last_message):
            	post('Minus one that\'s three, quick maths')
        	elif '!wotd' in str(last_message):
            	yeet = word_day()
            	post(yeet)
        	elif '!fun' in str(last_message):
            	yeet = fun_commands()
            	post(yeet)
        	elif '!help' in str(last_message):
            	post('You\'re beyond help. Try !commands')
        	elif '!temp' in str(last_message):
            	yeet = current_temp()
            	post(yeet)
        	elif '!pt' in str(last_message):
            	yeet = get_pt()
            	post(yeet)
        	elif'!npt' in str(last_message):
            	yeet = update_pt(str(last_message['attachments'][0]['url']))
            	post(yeet)
        	elif '!johnson' in str(last_message).lower():
            	post('https://i.groupme.com/531x710.jpeg.1b475182d3674994abde157163121942')
        	elif '!nudes' in str(last_message).lower():
            	post('https://i.groupme.com/610x320.png.9c520d0b31684cedb9a9ec7365881367')
        	elif '!apexofthedomain' in str(last_message).lower():
            	post('https://i.groupme.com/409x409.png.0b65d06109534c2aaebc597eeb1cde7f')
        	elif '!pass' in str(last_message).lower():
            	post('brian.r.burns22.mil@mail.mil\nlauren.j.shelsby2.mil@mail.mil')
        	elif '!morale' in str(last_message).lower():
            	post('https://i.groupme.com/1266x2250.jpeg.86f5ea4dada744fe840b9e9d9b149e2e')
        	elif '!mail' in str(last_message).lower():
            	post('get a PO box, nerd')
        	elif '!fullhooah' in str(last_message).lower():
            	post('https://i.groupme.com/720x1280.jpeg.670283276ab341b2985fe82b110b154c')
            	post('You never go full Hooah...')
        	elif '!goofyglassesguy' in str(last_message).lower():
            	post('https://i.groupme.com/1125x1500.jpeg.44169ba17b144c30b0c9d897562f38bd')
            	post('lol')
        	elif '!motto' in str(last_message).lower():
            	post('https://i.groupme.com/780x1040.jpeg.3505cd27f6584d38bdbfbb80767f2a75')
        	elif '!furryboi' in str(last_message).lower():
            	post('https://i.groupme.com/1048x1370.jpeg.a2b4f08c26774737898c21371c7becff.large')
        	elif '!judgingyou' in str(last_message).lower():
            	post('https://i.groupme.com/720x960.png.155386653ae04a24ab12a149e9186636')
        	elif '!ctblink' in str(last_message).lower():
            	post('https://intelshare.intelink.gov/sites/ctb/_layouts/15/start.aspx#/SitePages/Bravo%20Company.aspx')
        	elif '!chestnut' in str(last_message).lower():
            	post('https://i.groupme.com/300x400.png.77e68bc95c504664bd822848aea963fd')
        	elif '!holiday' in str(last_message).lower():
            	post('Columbus Day Weekend – Friday, October 5, 2018 to Monday, October 8, 2018\nVeterans Day Weekend – Friday, November 9, 2018 to Monday, November 12, 2018\nThanksgiving Weekend – Thursday, November 22, 2018 to Sunday, November 25, 2018\nChristmas Day Weekend – Saturday, December 22, 2018 to Monday, December 25, 2018\nNew Year’s Eve Weekend – Saturday, December 30, 2018 to Tuesday, January 2, 2019\nMLK Weekend – Friday, January 18, 2019 to Monday, January, 21, 2019\nPresident’s Day Weekend – Friday, February 15, 2019 to Monday, February 18, 2019\nMemorial Day Weekend – Friday, May 24, 2019 to Monday, May 27, 2019\nLabor Day Weekend – Friday, August 30, 2019 to Monday, September, 2, 2019\n')
        	elif 'no u' in str(last_message).lower():
            	post('https://i.groupme.com/500x751.png.37929a37a1fe46d78975ea4eb9b1b314')
        	else:
            	if 'bot_daddy' in str(data['name']).lower():
                	pass
            	else:
                	for bad in baddies:
                    	if str(bad).lower() in str(last_message).lower():
                        	post('Hacking you, ' + last_message['name'] + '.')
                        	break
           	 
        	#repeat = last_message
       	 
	except:
    	print('ouch')
   	 
class S(BaseHTTPRequestHandler):
	def do_POST(self):
    	content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    	post_data = self.rfile.read(content_length) # <--- Gets the data itself
    	s = post_data
    	data = json.loads(s.decode("utf-8"))
    	reply(data) # <-- Print post data
   	 
def run(server_class=HTTPServer, handler_class=S, port=80):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print('Starting httpd...')
	httpd.serve_forever()

run()
