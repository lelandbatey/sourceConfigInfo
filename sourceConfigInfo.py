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

by: Leland Batey
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
v0.03
Additions
 - Automatically finds config.cfg files
 - Bit better modulization now

v0.02
Additions
 - Fixed whitespace handling for better parsing

v0.01
First Version
 - What am I even doing
 Bugs:
 - My program is OBVIOUSLY perfect. Nothing to change here.
'''
import os
import fnmatch

def parseConfig(fileFolder,returnList=False):
    bindNames = "\\ ins del home end pgdn pgup kp_ins \
kp_del kp_end kp_downarrow kp_pgdn kp_leftarrow kp_5 kp_rightarrow \
kp_home kp_uparrow kp_pgup kp_slash * kp_minus kp_plus kp_enter a b\
 c d e f g h i j k l m n o p q r s t u v w x y z , . /  ; ’ [ ] - = \
~ leftarrow rightarrow uparrow downarrow enter space shift ctrl alt\
 backspace tab escape pause mouse1 mouse2 mouse3 mouse4 mouse5 mwheelup\
 mwheeldown 0 1 2 3 4 5 6 7 8 9".split(' ')
    # These are all the keys that can be have bindings in the Source engine.
    # The names are the ones given by the Source engine, so they may be a bit strange.

    doneFlag = False
    configFile = open(fileFolder+'\\config.cfg', 'r')
    keyBindList = []
    bindList = []
    
    while not doneFlag:
        curLine = configFile.readline()
        if len(curLine) and curLine.count('bind ') and not curLine.count('\\\\'):
            
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
    
    return(buildLine)
	

	
def getSourceDirectories():
    # This searches the Program Files 
    
    rootPath = os.listdir('C:\\')
    doneFlag = False
    if 'Program Files (x86)' in os.listdir('C:\\'):
        is64bit = True
    configLocation = []

    # Creates an index of all the folders that contain 'config.cfg' files
    if is64bit:
        for root, dirs, files in os.walk('C:\\Program Files (x86)\\Steam\\steamapps'):
            for filename in fnmatch.filter(files, 'config.cfg'):
                configLocation.append(root+'\\')
    else:
        for root, dirs, files in os.walk('C:\\Program Files\\Steam\\steamapps'):
            for filename in fnmatch.filter(files, 'config.cfg'):
                configLocation.append(root+'\\')

    return(configLocation)

def chooseConfigDir(locationArray):
    toReturn = ""

    print("Which file do you want to analyze?: ")
    for index, path in enumerate(locationArray):
        print("{0:<7}".format("["+str(index+1)+"]")+path)
    indexChosen = input("Enter the config folder to be analyzed (default - 1): ") or 0
    if indexChosen: indexChosen = int(indexChosen)-1
    toReturn = locationArray[indexChosen]

    return toReturn

def main():
    locationsArray = getSourceDirectories()
    chosenLocation = chooseConfigDir(locationsArray)
    parsedData = parseConfig(chosenLocation)
    print(parsedData)
main()
