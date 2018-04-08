import harvester
import deadcreep
import spawner

import testCommand


# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
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


def main():
    """
    Main game logic loop.
    """
    #Clear Dead creeps from Memory
    deadcreep.cleanDeadCreeps()

    # Run each creep
    #print(dir(Game.creeps))

    if Game.creeps:
        for name in Object.keys(Game.creeps):
            creep = Game.creeps[name]
            harvester.run_harvester(creep)
            testCommand.Command(name, creep)


    # Run each spawn
    spawner.Spawner()




module.exports.loop = main
