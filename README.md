
SourceConfigInfo
================

SourceConfigInfo is a short and simple python script for getting information about a Source engine game's Config.cfg file.

Specifically, it will tell you:
 1. What keys have binds.
 2. The commands that are bound to each key
 3. What keys are't bound to anything.
 

##Example Output##

This example uses the default Team Fortress 2 "config.cfg" file [which can be found here.](http://wiki.teamfortress.com/wiki/File:Config_default.cfg.txt)

###Output:###
 
	Which file do you want to analyze?: 
	[1]  C:\Program Files (x86)\Steam\steamapps\common\alien swarm\swarm\cfg\
	[2]  C:\Program Files (x86)\Steam\steamapps\common\call of duty 2\main\players\mrblake\
	[3]  C:\Program Files (x86)\Steam\steamapps\common\call of duty 2\main\players\user4\
	[4]  C:\Program Files (x86)\Steam\steamapps\common\call of duty 4\players\profiles\nacro\
	[5]  C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\
	[6]  C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\dota\cfg\
	[7]  C:\Program Files (x86)\Steam\steamapps\common\left 4 dead 2\left4dead2\cfg\
	[8]  C:\Program Files (x86)\Steam\steamapps\common\portal 2\portal2\cfg\
	[9]  C:\Program Files (x86)\Steam\steamapps\common\portal 2\update\cfg\
	[10]  C:\Program Files (x86)\Steam\steamapps\common\Quake\Id1\
	[11]  C:\Program Files (x86)\Steam\steamapps\common\quake 2\baseq2\
	[12]  C:\Program Files (x86)\Steam\steamapps\user1\half-life 2 episode two\ep2\cfg\
	[13]  C:\Program Files (x86)\Steam\steamapps\user2\team fortress 2\tf\cfg\
	[14]  C:\Program Files (x86)\Steam\steamapps\user3\team fortress 2\tf\cfg\
	[15]  C:\Program Files (x86)\Steam\steamapps\user4\counter-strike\cstrike\
	[16]  C:\Program Files (x86)\Steam\steamapps\user4\counter-strike\valve\
	[17]  C:\Program Files (x86)\Steam\steamapps\user4\counter-strike source\cstrike\cfg\
	[18]  C:\Program Files (x86)\Steam\steamapps\user4\day of defeat source\dod\cfg\
	[19]  C:\Program Files (x86)\Steam\steamapps\user4\garrysmod\garrysmod\cfg\
	[20]  C:\Program Files (x86)\Steam\steamapps\user4\half-life\valve\
	[21]  C:\Program Files (x86)\Steam\steamapps\user4\half-life 2\hl2\cfg\
	[22]  C:\Program Files (x86)\Steam\steamapps\user4\half-life 2 deathmatch\hl2mp\cfg\
	[23]  C:\Program Files (x86)\Steam\steamapps\user4\half-life 2 lostcoast\lostcoast\cfg\
	[24]  C:\Program Files (x86)\Steam\steamapps\user4\opposing force\gearbox\
	[25]  C:\Program Files (x86)\Steam\steamapps\user4\opposing force\valve\
	[26]  C:\Program Files (x86)\Steam\steamapps\user4\portal\portal\cfg\
	[27]  C:\Program Files (x86)\Steam\steamapps\user4\team fortress 2\tf\cfg\
	[28]  C:\Program Files (x86)\Steam\steamapps\user4\team fortress 2 beta\tf_beta\cfg\
	[29]  C:\Program Files (x86)\Steam\steamapps\user4\team fortress classic\tfc\
	[30]  C:\Program Files (x86)\Steam\steamapps\user4\team fortress classic\valve\
	[31]  C:\Program Files (x86)\Steam\steamapps\smod\cfg\
	[32]  C:\Program Files (x86)\Steam\steamapps\sourcemods\BMS\cfg\
	[33]  C:\Program Files (x86)\Steam\steamapps\sourcemods\FortressForever\cfg\
	[34]  C:\Program Files (x86)\Steam\steamapps\sourcemods\nmrih\cfg\
	[35]  C:\Program Files (x86)\Steam\steamapps\sourcemods\smod\cfg\
	[36]  C:\Program Files (x86)\Steam\steamapps\sourcemods\sourceforts\cfg\
	[37]  C:\Program Files (x86)\Steam\steamapps\sourcemods\thestanleyparable\cfg\
	[38]  C:\Program Files (x86)\Steam\userdata\38079672\220\remote\cfg\
	[39]  C:\Program Files (x86)\Steam\userdata\38079672\240\remote\cfg\
	[40]  C:\Program Files (x86)\Steam\userdata\38079672\300\remote\cfg\
	[41]  C:\Program Files (x86)\Steam\userdata\38079672\4000\remote\cfg\
	[42]  C:\Program Files (x86)\Steam\userdata\38079672\440\remote\cfg\
	[43]  C:\Program Files (x86)\Steam\userdata\38079672\570\remote\cfg\
	[44]  C:\Program Files (x86)\Steam\userdata\38079672\630\remote\cfg\
	Enter the config folder to be analyzed (default - 1): 17

	The key       "0"        is bound to "slot10"              
	The key       "1"        is bound to "slot1"               
	The key       "2"        is bound to "slot2"               
	The key       "3"        is bound to "slot3"               
	The key       "4"        is bound to "slot4"               
	The key       "5"        is bound to "slot5"               
	The key       "6"        is bound to "slot6"               
	The key       "7"        is bound to "slot7"               
	The key       "8"        is bound to "slot8"               
	The key       "9"        is bound to "slot9"               
	The key       "a"        is bound to "+moveleft"           
	The key       "b"        is bound to "buymenu"             
	The key       "c"        is bound to "radio3"              
	The key       "d"        is bound to "+moveright"          
	The key       "e"        is bound to "+use"                
	The key       "f"        is bound to "impulse 100"         
	The key       "g"        is bound to "drop"                
	The key       "h"        is bound to "commandmenu"         
	The key       "i"        is bound to "showbriefing"        
	The key       "j"        is bound to "cheer"               
	The key       "k"        is bound to "kill"                
	The key       "m"        is bound to "chooseteam"          
	The key       "n"        is bound to "nightvision"         
	The key       "o"        is bound to "buyequip"            
	The key       "q"        is bound to "lastinv"             
	The key       "r"        is bound to "+reload"             
	The key       "s"        is bound to "+back"               
	The key       "t"        is bound to "impulse 201"         
	The key       "u"        is bound to "messagemode2"        
	The key       "v"        is bound to "+voicerecord"        
	The key       "w"        is bound to "+forward"            
	The key       "x"        is bound to "radio2"              
	The key       "y"        is bound to "messagemode"         
	The key       "z"        is bound to "radio1"              
	The key       "`"        is bound to "toggleconsole"       
	The key       ","        is bound to "buyammo1"            
	The key       "."        is bound to "buyammo2"            
	The key     "space"      is bound to "+jump"               
	The key      "tab"       is bound to "+showscores"         
	The key     "escape"     is bound to "cancelselect"        
	The key     "pause"      is bound to "pause"               
	The key     "shift"      is bound to "+duck"               
	The key      "ctrl"      is bound to "+speed"              
	The key       "f1"       is bound to "autobuy"             
	The key       "f2"       is bound to "rebuy"               
	The key       "f3"       is bound to "askconnect_accept"   
	The key       "f4"       is bound to "bug"                 
	The key       "f5"       is bound to "jpeg"                
	The key       "f6"       is bound to "save quick"          
	The key       "f7"       is bound to "load quick"          
	The key      "f10"       is bound to "quit prompt"         
	The key     "mouse1"     is bound to "+attack"             
	The key     "mouse2"     is bound to "+attack2"            
	The key    "mwheelup"    is bound to "invprev"             
	The key   "mwheeldown"   is bound to "invnext"             
	The        "\"         key is unbound
	The       "ins"        key is unbound
	The       "del"        key is unbound
	The       "home"       key is unbound
	The       "end"        key is unbound
	The       "pgdn"       key is unbound
	The       "pgup"       key is unbound
	The      "kp_ins"      key is unbound
	The      "kp_del"      key is unbound
	The      "kp_end"      key is unbound
	The   "kp_downarrow"   key is unbound
	The     "kp_pgdn"      key is unbound
	The   "kp_leftarrow"   key is unbound
	The       "kp_5"       key is unbound
	The  "kp_rightarrow"   key is unbound
	The     "kp_home"      key is unbound
	The    "kp_uparrow"    key is unbound
	The     "kp_pgup"      key is unbound
	The     "kp_slash"     key is unbound
	The        "*"         key is unbound
	The     "kp_minus"     key is unbound
	The     "kp_plus"      key is unbound
	The     "kp_enter"     key is unbound
	The        "l"         key is unbound
	The        "p"         key is unbound
	The        "/"         key is unbound
	The         ""         key is unbound
	The        ";"         key is unbound
	The        "�"         key is unbound
	The        "["         key is unbound
	The        "]"         key is unbound
	The        "-"         key is unbound
	The        "="         key is unbound
	The        "~"         key is unbound
	The    "leftarrow"     key is unbound
	The    "rightarrow"    key is unbound
	The     "uparrow"      key is unbound
	The    "downarrow"     key is unbound
	The      "enter"       key is unbound
	The       "alt"        key is unbound
	The    "backspace"     key is unbound
	The      "mouse3"      key is unbound
	The      "mouse4"      key is unbound
	The      "mouse5"      key is unbound