'''
from defs import *
from decide import Decide


__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')
'''

class Decide:

    def __init__(self):

        #self.target = {}
        self.a = 1
        self.nums_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == Game.spawns['Spawn1'].pos.roomName)


    def decideWorkTarget(self, creep):

        constructionSite = creep.pos.findClosestByPath(FIND_CONSTRUCTION_SITES)
        randomStructure = creep.room.find(FIND_STRUCTURES)
        structureNeedRepair = _(randomStructure).filter(lambda s: s.hits < s.hitsMax and s.structureType != STRUCTURE_WALL).sample()

        # If we have a saved target, use it
        if creep.memory.target and Game.getObjectById(creep.memory.target):
            self.target = Game.getObjectById(creep.memory.target)

        else:
            # IF unfinished construction site were, builder random target FIND_CONSTRUCTION_SITES
            if constructionSite:
                # worker creeps is plenty, then target on constructionSites
                if self.nums_creeps > 10 :
                    target_construction = constructionSite
                    target_random = _(randomStructure).filter(lambda s: ((s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapacity) or s.structureType == STRUCTURE_CONTROLLER).sample()

                    ####self.target = random.choice([target_construction, target_random])

                    self.target = _.sample([target_construction, target_random])


                # worker is not plenty, target on spawn and extensions
                else:
                    self.target = _(randomStructure).filter(lambda s: (s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapacity).sample()

                    #even though s.energy is undefined or energy is full, target anyway.
                    if not self.target:
                        self.target = _(randomStructure).filter(lambda s: (s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION)).sample()

                creep.memory.target = self.target.id

            # If there is structures need repair and spawned creeps are plendy.
            elif structureNeedRepair and self.nums_creeps > 10:
                self.target = structureNeedRepair
                if self.target :
                    print("repair ID ", self.target.id)
                    creep.memory.target = self.target.id
                    creep.memory.role = 'repair'


            # IF No constructionSite visible
            else:
                # Plenty worker creeps?
                if self.nums_creeps > 8:
                    # Get a random new target including Controller.
                    self.target = _(randomStructure) \
                    .filter(lambda s: ((s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapacity) or s.structureType == STRUCTURE_CONTROLLER) \
                    .sample()

                # creeps not plenty? Spawn or extension only targeting
                else:
                    self.target = _(randomStructure).filter(lambda s: (s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION) and s.energy < s.energyCapcity).sample()

                    # even though target does not exist or enery is full, target something anyway
                    if not self.target:
                        self.target = _(randomStructure).filter(lambda s: (s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION)).sample()

                creep.memory.target = self.target.id
