'''
from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')
'''


class Work2target:

    def __init__(self):

        #self.target = {}
        self.b = 1


    def workingOnTarget(self, creep):


        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
            # If target is a spawn or extension, we need to be directly next to it - otherwise, we can be 3 away.
            if target.energyCapacity:
                is_close = creep.pos.isNearTo(target)
            else:
                is_close = creep.pos.inRangeTo(target, 3)


            # If Target is near by then...
            if is_close:

                # If Target is a spawn or extension, transfer energy.
                if target.energyCapacity:
                    result = creep.transfer(target, RESOURCE_ENERGY)
                    if result == OK or result == ERR_FULL:
                        del creep.memory.target
                    #else:
                        #print("[{}] Unknown result from creep.transfer({}, {}): {}".format(
                       #     creep.name, target, RESOURCE_ENERGY, result))

                #Otherwise, use upgradeController on it.
                else:

                    if creep.memory.role :
                        print(creep.name, target.id, " hits:", target.hits, " hitsMax:", target.hitsMax)

                        if creep.memory.target and creep.memory.role == 'repair' :
                            if target :
                                result = creep.repair(target)
                                print(creep.name, " reparing ", target.id)

                                if result == OK or result == ERR_NOT_ENOUGH_RESOURCES or ERR_INVALID_TARGET :
                                    print("result ", result)
                                    del creep.memory.target
                                    del creep.memory.role
                        else:
                            del creep.memory.role
                            del creep.memory.target

                    else:

                        # Let the creeps get a little bit closer than required to the controller, to make room for other creeps.
                        if target.structureType == STRUCTURE_CONTROLLER:


                            result = creep.upgradeController(target)

                            if result != OK:
                                del creep.memory.target
                                #print("[{}] Unknown result from creep.upgradeController({}): {}".format(creep.name, target, result))


                        #If target isn't upgradeController, build on it.
                        else:
                            result = creep.build(target)

                             #If build target is already finished, remove the target
                            if result != OK:
                                del creep.memory.target



                        if not creep.pos.inRangeTo(target, 2):
                            creep.moveTo(target)

            #If target is not close enough, move to it.
            else:
                creep.moveTo(target)
        else:
            pass
