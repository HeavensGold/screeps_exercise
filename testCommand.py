from defs import *
# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')
i = []
Memory.test = {}
Memory.test.testCounter = 0
#for pName in Object.keys(Game.creeps):
#    print(pName)
#    Memory.test[pName] = {}
#    Memory.test[pName].tickCount = 0
#    print(Memory.test[pName].tickCount)
    
def Execute(creep):
    ########  WRITE HERE!!  #########################

    #whatInfo = []
    #if Game.constructionSites:
    #    for keys in Game.contructionSites:
    #        print (keys, "dd")
    #    print (dir(Game.constructionSites))
        #whatInfo[i] = value

        #print("dir: {}  value: {} ".format(dir(whatInfo[0]), whatInfo[0]))
    #f = open('testData.txt', 'w')
    #f.write()
    

#    if creep.memory.myTickCount :
#        creep.memory.myTickCount += 1

#    else:
#        creep.memory.myTickCount = 1 
#    print(creep.memory.myTickCount)

#    print(Object.keys(Game.spawns))


    ######### UPTO ABOBE ############################
    pass

def Command(name,creep):

    if Memory.test.testCounter and Memory.test.testCounter > 0 :
        #Write codes here!

        Memory.test.testCounter -= 1
        #print("rr " + Memory.test.testCounter)

    else:
        Execute(creep)
        Memory.test.testCounter = 0 

        #print(testCounter)
        #exept Exception as e :
        #    print(e)
        #    testCounter = 10
        #    contine

    #testCounter += -1
