# blingjson
Python module to pretty print your json with syntax highlighting and :gem:

### Usage

	import blingjson, json
	
	data = {"weather": [{"id": 800,"main": "Clear","description": "Sky is Clear","icon": "01d"}],"wind": {"speed": 2.66,"deg": 305.501}}
	
	weather = json.dumps(data['weather'])
	
	blingjson.pprint(weather)
	
Run it. Look at the colors.

<img src="http://i.imgur.com/bU9QSyy.png">

	blingjson.pprint(weather, colorize=False)
	
<img src="http://i.imgur.com/PrlBicw.png">
	
	blingjson.pprint(weather, extra_bling=True)
	
<img src="http://i.imgur.com/fT1pyxs.png">

	blingjson.pprint(weather, extra_bling=True, short_code=':blue_heart:')

<img src="http://i.imgur.com/uXqBINs.png">	
