from defs import *
from decide import Decide
from work2target import Work2target

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')



def getCreepType(creep):
    creep_type = []
    for x in range(len(creep.body)):
        creep_type.append(creep.body[x].type)
    return creep_type


def sourceMining(creep):
    # If we have a saved source, use it
    if creep.memory.source:
        source = Game.getObjectById(creep.memory.source)
        # If creep to source is in Range but not harvesting, count the number of waiting tick time.
        if creep.memory.myTickCount1:
            if creep.pos.inRangeTo(source, 4) and creep.memory.myTickCount1 > 13 and not creep.pos.isNearTo(source) :
                # If too much waiting for a source, get a random new source and save it
                sourceOld = source
                source = _.sample(creep.room.find(FIND_SOURCES))
                creep.memory.source = source.id
                creep.memory.myTickCount1 = 1


            creep.memory.myTickCount1 += 1
            print(creep.name, creep.memory.myTickCount1)
        else:
            creep.memory.myTickCount1 = 1
    else:
        # If We don't have saved source, get a random new source and save it
        source = _.sample(creep.room.find(FIND_SOURCES))
        creep.memory.source = source.id
        creep.memory.myTickCount = 1


    # If we're near the source, harvest it - otherwise, move to it.
    if creep.pos.isNearTo(source):
        result = creep.harvest(source)
        creep.memory.myTickCount1 = 1

        #if result != OK:
    #        print("[{}] Unknown result from creep.harvest({}): {}".format(creep.name, source, result))
    else:

        creep.moveTo(source)



def checkNeedFilling(creep):
    # if we're full, stop filling up and remove the saved source'''
    if creep.memory.filling and _.sum(creep.carry) >= creep.carryCapacity:
        creep.memory.filling = False
        del creep.memory.source
    # If we're empty, start filling again and remove the saved target
    elif not creep.memory.filling and creep.carry.energy <= 0:
        creep.memory.filling = True
        del creep.memory.target



def run_harvester(creep):
    """
    Runs a creep as a generic harvester.
    :param creep: The creep to run
    """
    # check if creep needs filling or not
    checkNeedFilling(creep)

    # if creep needs to fill energy, go to source.
    if creep.memory.filling:
        sourceMining(creep)

    # if ceep energy is full, decide target and go to work.
    else:

        decide = Decide()
        decide.decideWorkTarget(creep)

        work2target = Work2target()
        work2target.workingOnTarget(creep)

        ######################## In case target is not decided as expected, run this.
        #target = _(creep.room.find(FIND_STRUCTURES)) \
        #    .filter(lambda s: ((s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION) \
        #    and s.energy < s.energyCapacity) or s.structureType == STRUCTURE_CONTROLLER) \
        #    .sample()
        #
        #creep.memory.target = target.id
        ###################

        creep_type = getCreepType(creep)
        #print("WORK number = {}".format(len([s for s in creep_type if s == 'work'])))
        #print(str(creep_type[0]))


        #Monitoring targeting activities.
        if creep.memory.target:
            target_print = Game.getObjectById(creep.memory.target)

            print ("{}({}) targets name({}) type({}) {}".format(creep.name,creep_type,target_print.name,target_print.structureType,target_print.id))
