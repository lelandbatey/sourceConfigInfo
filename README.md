
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
	[1]    C:\Program Files (x86)\Steam\steamapps\
	[2]    C:\Program Files (x86)\Steam\steamapps\common\alien swarm\swarm\cfg\
	[3]    C:\Program Files (x86)\Steam\steamapps\common\call of duty 2\main\players\user2\
	[4]    C:\Program Files (x86)\Steam\steamapps\common\call of duty 2\main\players\user4\
	[5]    C:\Program Files (x86)\Steam\steamapps\common\call of duty 4\players\profiles\user3\
	[6]    C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\
	[7]    C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\dota\cfg\
	[8]    C:\Program Files (x86)\Steam\steamapps\common\left 4 dead 2\left4dead2\cfg\
	[9]    C:\Program Files (x86)\Steam\steamapps\common\portal 2\portal2\cfg\
	[10]   C:\Program Files (x86)\Steam\steamapps\common\portal 2\update\cfg\
	[11]   C:\Program Files (x86)\Steam\steamapps\common\Quake\Id1\
	[12]   C:\Program Files (x86)\Steam\steamapps\common\quake 2\baseq2\
	[13]   C:\Program Files (x86)\Steam\steamapps\user1\half-life 2 episode two\ep2\cfg\
	[14]   C:\Program Files (x86)\Steam\steamapps\user2\team fortress 2\tf\cfg\
	[15]   C:\Program Files (x86)\Steam\steamapps\user3\team fortress 2\tf\cfg\
	[16]   C:\Program Files (x86)\Steam\steamapps\user4\counter-strike\cstrike\
	[17]   C:\Program Files (x86)\Steam\steamapps\user4\counter-strike\valve\
	[18]   C:\Program Files (x86)\Steam\steamapps\user4\counter-strike source\cstrike\cfg\
	[19]   C:\Program Files (x86)\Steam\steamapps\user4\day of defeat source\dod\cfg\
	[20]   C:\Program Files (x86)\Steam\steamapps\user4\garrysmod\garrysmod\cfg\
	[21]   C:\Program Files (x86)\Steam\steamapps\user4\half-life\valve\
	[22]   C:\Program Files (x86)\Steam\steamapps\user4\half-life 2\hl2\cfg\
	[23]   C:\Program Files (x86)\Steam\steamapps\user4\half-life 2 deathmatch\hl2mp\cfg\
	[24]   C:\Program Files (x86)\Steam\steamapps\user4\half-life 2 lostcoast\lostcoast\cfg\
	[25]   C:\Program Files (x86)\Steam\steamapps\user4\opposing force\gearbox\
	[26]   C:\Program Files (x86)\Steam\steamapps\user4\opposing force\valve\
	[27]   C:\Program Files (x86)\Steam\steamapps\user4\portal\portal\cfg\
	[28]   C:\Program Files (x86)\Steam\steamapps\user4\team fortress 2\tf\cfg\
	[29]   C:\Program Files (x86)\Steam\steamapps\user4\team fortress 2 beta\tf_beta\cfg\
	[30]   C:\Program Files (x86)\Steam\steamapps\user4\team fortress classic\tfc\
	[31]   C:\Program Files (x86)\Steam\steamapps\user4\team fortress classic\valve\
	[32]   C:\Program Files (x86)\Steam\steamapps\smod\cfg\
	[33]   C:\Program Files (x86)\Steam\steamapps\sourcemods\BMS\cfg\
	[34]   C:\Program Files (x86)\Steam\steamapps\sourcemods\FortressForever\cfg\
	[35]   C:\Program Files (x86)\Steam\steamapps\sourcemods\nmrih\cfg\
	[36]   C:\Program Files (x86)\Steam\steamapps\sourcemods\smod\cfg\
	[37]   C:\Program Files (x86)\Steam\steamapps\sourcemods\sourceforts\cfg\
	[38]   C:\Program Files (x86)\Steam\steamapps\sourcemods\thestanleyparable\cfg\
	Enter the config folder to be analyzed (default - 1): 1

	The key       "`"        is bound to "toggleconsole"       
	The key       "w"        is bound to "+forward"            
	The key       "s"        is bound to "+back"               
	The key       "a"        is bound to "+moveleft"           
	The key       "d"        is bound to "+moveright"          
	The key     "space"      is bound to "+jump"               
	The key      "ctrl"      is bound to "+duck"               
	The key      "tab"       is bound to "+showscores"         
	The key       "'"        is bound to "+moveup"             
	The key       "/"        is bound to "+movedown"           
	The key      "pgup"      is bound to "+lookup"             
	The key      "pgdn"      is bound to "+lookdown"           
	The key      "end"       is bound to "centerview"          
	The key      "alt"       is bound to "+strafe"             
	The key      "ins"       is bound to "+klook"              
	The key   "semicolon"    is bound to "+mlook"              
	The key       "r"        is bound to "+reload"             
	The key     "mouse1"     is bound to "+attack"             
	The key     "mouse2"     is bound to "+attack2"            
	The key       "z"        is bound to "saveme"              
	The key       "z"        is bound to "voice_menu_1"        
	The key       "x"        is bound to "voice_menu_2"        
	The key       "c"        is bound to "voice_menu_3"        
	The key       "e"        is bound to "dropitem"            
	The key       "1"        is bound to "slot1"               
	The key       "2"        is bound to "slot2"               
	The key       "3"        is bound to "slot3"               
	The key       "4"        is bound to "slot4"               
	The key       "5"        is bound to "slot5"               
	The key       "6"        is bound to "slot6"               
	The key       "7"        is bound to "slot7"               
	The key       "8"        is bound to "slot8"               
	The key       "9"        is bound to "slot9"               
	The key       "0"        is bound to "slot10"              
	The key    "mwheelup"    is bound to "invprev"             
	The key   "mwheeldown"   is bound to "invnext"             
	The key       "q"        is bound to "lastinv"             
	The key       "f5"       is bound to "screenshot"          
	The key       "f6"       is bound to "save_replay"         
	The key      "f10"       is bound to "quit prompt"         
	The key      "f12"       is bound to "replay_togglereplaytips"
	The key     "pause"      is bound to "pause"               
	The key     "escape"     is bound to "escape"              
	The key       "t"        is bound to "impulse 201"         
	The key       "y"        is bound to "say"                 
	The key       "u"        is bound to "say_team"            
	The key       "v"        is bound to "+voicerecord"        
	The key       "."        is bound to "changeteam"          
	The key       ","        is bound to "changeclass"         
	The key       "f1"       is bound to "+showroundinfo"      
	The key       "g"        is bound to "taunt"               
	The key       "h"        is bound to "use_action_slot_item"
	The key       "e"        is bound to "voicemenu 0 0"       
	The key       "b"        is bound to "lastdisguise"        
	The key       "l"        is bound to "dropitem"            
	The key       "i"        is bound to "showmapinfo"         
	The key       "-"        is bound to "disguiseteam"        
	The key       "m"        is bound to "open_charinfo_direct"
	The key       "n"        is bound to "open_charinfo_backpack"
	The key       "f"        is bound to "inspect"             
	The key       "j"        is bound to "cl_trigger_first_notification"
	The        "\"         key is unbound
	The       "del"        key is unbound
	The       "home"       key is unbound
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
	The        "k"         key is unbound
	The        "o"         key is unbound
	The        "p"         key is unbound
	The         ""         key is unbound
	The        ";"         key is unbound
	The        "’"         key is unbound
	The        "["         key is unbound
	The        "]"         key is unbound
	The        "="         key is unbound
	The        "~"         key is unbound
	The    "leftarrow"     key is unbound
	The    "rightarrow"    key is unbound
	The     "uparrow"      key is unbound
	The    "downarrow"     key is unbound
	The      "enter"       key is unbound
	The      "shift"       key is unbound
	The    "backspace"     key is unbound
	The      "mouse3"      key is unbound
	The      "mouse4"      key is unbound
	The      "mouse5"      key is unbound