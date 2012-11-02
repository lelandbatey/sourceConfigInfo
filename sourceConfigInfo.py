'''

	   _____                          
	  / ___/____  __  _______________ 
	  \__ \/ __ \/ / / / ___/ ___/ _ \
	 ___/ / /_/ / /_/ / /  / /__/  __/
	/____/\____/\__,_/_/   \___/\___/ 
	                                  
	   ______            _____       ____      ____    
	  / ____/___  ____  / __(_)___ _/  _/___  / __/___ 
	 / /   / __ \/ __ \/ /_/ / __ `// // __ \/ /_/ __ \
	/ /___/ /_/ / / / / __/ / /_/ // // / / / __/ /_/ /
	\____/\____/_/ /_/_/ /_/\__, /___/_/ /_/_/  \____/ 
	                       /____/                      

by: Narcoblix
October 26th, 2012
####################
#   Description:   #
####################
This is a simple script that will tell you what your binds are in a source game.
It analyzes what your config.cfg file contains, then it outputs to the console (and optionally
to a file).

It will ask for the location of a Source game's 'cfg' folder, then it will open the
config file and tell you:
 1. What keys have binds, and what those keys are bound to.
 2. The keys that could have binds, but don't.

###############
#   Changes   #
###############

v0.02
Additions
 - Fixed whitespace handling for better parsing

v0.01
First Version
 - What am I even doing
 Bugs:
 - My program is OBVIOUSLY perfect. Nothing to change here.
'''

def main():
    bindNames = "\ ins del home end pgdn pgup kp_ins kp_del kp_end kp_downarrow kp_pgdn kp_leftarrow kp_5 kp_rightarrow kp_home kp_uparrow kp_pgup kp_slash * kp_minus kp_plus kp_enter a b c d e f g h i j k l m n o p q r s t u v w x y z , . /  ; ’ [ ] - = ~ leftarrow rightarrow uparrow downarrow enter space shift ctrl alt backspace tab escape pause mouse1 mouse2 mouse3 mouse4 mouse5 mwheelup mwheeldown 0 1 2 3 4 5 6 7 8 9".split(' ')
    # The above monstrosity is a giant string of all the possible keys that you can bind to. This is a list of the names that the source engine assigns to these keys, so they may be a bit confusing to read.
    doneFlag = False
    configFolder = input("Paste the path to the 'cfg' folder in here(Example: 'C:\Program Files\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg': ")

    try:
        configFile = open(configFolder+'\\config.cfg', 'r')
    except Exception as e:
        print(str(e))
    
    keyBindList = []
    bindList = []

    
    while not doneFlag:
        curLine = configFile.readline()
        
        if len(curLine) > 0 and curLine.count('bind ') > 0:
            
            buildLine = ""
            curLine = curLine.lower()
            curLine = curLine.split('"')

            for keys in curLine:
                if (curLine.index(keys)+1)%2 < 1:
                    buildLine += keys + "@"  
                        
            # Adds the key being bound and the bound-value into differnt arrays for each   
            keyBindList.append(buildLine.split("@")[0])
            bindList.append(buildLine.split("@")[1])
            
        elif len(curLine) == 0:
            doneFlag = True
            
    buildLine = ""

    for keyBind in range(0,len(keyBindList),1):
        buildLine += 'The key {0:^16} is bound to {1:<22}\n'.format('"'+keyBindList[keyBind]+'"','"'+bindList[keyBind]+'"')

        
    for keyBind in bindNames:
        if keyBind in keyBindList:
            pass
        else:
            buildLine += "The {0:^18} key is unbound\n".format('"'+keyBind+'"')
    
    print(buildLine)
	
main()
	
