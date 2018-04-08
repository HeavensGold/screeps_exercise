#from defs import *
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


# Clear Dead creeps from Memory
def cleanDeadCreeps():
    if Memory.creeps:
        for name in Object.keys(Memory.creeps):
            if Game.creeps[name] == undefined:
                print ("del from memory " + Memory.creeps[name])
                del Memory.creeps[name]
      #else:
      #    print(Game.creeps[name])
