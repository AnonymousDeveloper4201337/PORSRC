from panda3d.core import Character
from direct.directnotify import DirectNotifyGlobal

from pirates.npc.DistributedNPCTownfolkAI import DistributedNPCTownfolkAI

from pirates.battle.DistributedBattleNPCAI import *
from pirates.creature.DistributedCreatureAI import *
from pirates.creature.DistributedAnimalAI import *
from pirates.creature.DistributedRavenAI import *
from pirates.npc.DistributedNPCNavySailorAI import *
from pirates.npc.DistributedBountyHunterAI import *
from pirates.npc.DistributedNPCSkeletonAI import *

import random, os

CLASSES = {}

for creature in (AvatarTypes.Crab, AvatarTypes.RockCrab, AvatarTypes.StoneCrab,
                 AvatarTypes.GiantCrab, AvatarTypes.CrusherCrab, AvatarTypes.Chicken,
                 AvatarTypes.Rooster, AvatarTypes.Pig, AvatarTypes.Dog, AvatarTypes.Seagull,
                 AvatarTypes.Raven, AvatarTypes.Stump, AvatarTypes.TwistedStump, AvatarTypes.FlyTrap,
                 AvatarTypes.RancidFlyTrap, AvatarTypes.AncientFlyTrap, AvatarTypes.Scorpion,
                 AvatarTypes.DireScorpion, AvatarTypes.DreadScorpion, AvatarTypes.Alligator,
                 AvatarTypes.BayouGator, AvatarTypes.BigGator, AvatarTypes.HugeGator, AvatarTypes.Bat,
                 AvatarTypes.RabidBat, AvatarTypes.VampireBat, AvatarTypes.FireBat, AvatarTypes.Wasp,
                 AvatarTypes.KillerWasp, AvatarTypes.AngryWasp, AvatarTypes.SoldierWasp,
                 AvatarTypes.Monkey, AvatarTypes.GrabberTentacle, AvatarTypes.HolderTentacle,
                 AvatarTypes.Kraken, AvatarTypes.KrakenHead, AvatarTypes.Cadet, AvatarTypes.Guard,
                 AvatarTypes.Thug, AvatarTypes.Grunt, AvatarTypes.Hiredgun, AvatarTypes.Mercenary,
                 AvatarTypes.Assassin, AvatarTypes.Marine, AvatarTypes.Sergeant, AvatarTypes.Veteran,
                 AvatarTypes.Officer, AvatarTypes.FrenchUndeadA, AvatarTypes.FrenchUndeadB, AvatarTypes.FrenchUndeadC,
                 AvatarTypes.FrenchUndeadD, AvatarTypes.Dragoon, AvatarTypes.SpanishUndeadA, AvatarTypes.SpanishUndeadB,
                 AvatarTypes.SpanishUndeadC, AvatarTypes.SpanishUndeadD, AvatarTypes.Clod, AvatarTypes.Sludge,
                 AvatarTypes.Mire, AvatarTypes.MireKnife, AvatarTypes.Muck, AvatarTypes.MuckCutlass, AvatarTypes.Corpse,
                 AvatarTypes.CorpseCutlass, AvatarTypes.Carrion, AvatarTypes.CarrionKnife, AvatarTypes.Cadaver,
                 AvatarTypes.CadaverCutlass, AvatarTypes.Zombie, AvatarTypes.CaptMudmoss, AvatarTypes.Mossman,
                 AvatarTypes.Drip):
    if creature.isA(AvatarTypes.Animal):
        CLASSES[creature] = DistributedAnimalAI
    elif creature in (AvatarTypes.Grunt, AvatarTypes.Thug, AvatarTypes.Hiredgun, AvatarTypes.Mercenary, AvatarTypes.Assassin):
        #TODO: Characters spawn in default animation, miss their weapons, and attacks dont do damage.
        CLASSES[creature] = DistributedBountyHunterAI
    elif creature in (AvatarTypes.Guard, AvatarTypes.Cadet, AvatarTypes.Marine, AvatarTypes.Sergeant, AvatarTypes.Veteran, AvatarTypes.Officer, AvatarTypes.Dragoon):
        #TODO: Characters spawn in default animation, miss their weapons, and attacks dont do damage.
        CLASSES[creature] = DistributedNPCNavySailorAI
    elif creature == AvatarTypes.Raven:
        CLASSES[creature] = DistributedRavenAI
    elif creature.faction == AvatarTypes.Undead.faction:
        CLASSES[creature] = DistributedNPCSkeletonAI
    else:
        CLASSES[creature] = DistributedCreatureAI

class SpawnNode(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('SpawnNode')

    def __init__(self, spawner, data):
        self.spawner = spawner
        self.air = self.spawner.air
        self.uid = 'SpawnNode-%d' % self.air.allocateChannel()
        self.npcs = {}

        self.data = data
        if 'Spawnables' not in data:
            return

        self.spawnable = self.data['Spawnables']
        if self.spawnable not in AvatarTypes.NPC_SPAWNABLES:
            return

        self.avType = AvatarTypes.NPC_SPAWNABLES[self.spawnable][0]()
        if self.avType not in CLASSES:
            DistributedEnemySpawnerAI.missingClass(self.avType)
            return

        self.avClass = CLASSES[self.avType]

        self.desiredNumAvatars = 1 # TO DO
        self.acceptOnce('startShardActivity', self.died)

    def died(self):
        taskMgr.doMethodLater(random.random() * 7, self.__checkCreatures, self.uniqueName('checkCreatures'))

    def __checkCreatures(self, task):
        deadNpcs = []
        for doId, npc in self.npcs.items():
            if npc.isDeleted():
                deadNpcs.append(doId)

        for doId in deadNpcs:
            del self.npcs[doId]

        # Upkeep population
        numNpcs = len(self.npcs)
        if numNpcs < self.desiredNumAvatars:
            uid = self.uniqueName('spawned-%s' % os.urandom(4).encode('hex'))
            npc = self.avClass.makeFromObjectKey(self.avClass, self, uid,
                                                 self.avType, self.data)
            self.spawner.spawn(npc)
            self.npcs[npc.doId] = npc

        if task:
            return task.done

    def uniqueName(self, name):
        return '%s-%s' % (self.uid, name)

class DistributedEnemySpawnerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEnemySpawnerAI')
    _missing = set() # Debug

    def __init__(self, gameArea):
        self.gameArea = gameArea
        self.air = self.gameArea.air

        self.spawnNodes = {}

    def addSpawnNode(self, objKey, data):
        self.spawnNodes[objKey] = SpawnNode(self, data)

    def spawnNavy(self, objKey, data):
        npc = DistributedNPCPirateAI.makeFromObjectKey(None, self, objKey, data)
        self.spawn(npc, False)
        return npc

    def spawnMarine(self, objKey, data):
        npc = DistributedNPCNavySailorAI.makeFromObjectKey(None, self, objKey, data)
        self.spawn(npc, False)
        return npc

    def spawnNPC(self, objKey, data):
        npc = DistributedNPCTownfolkAI.makeFromObjectKey(None, self, objKey, data)
        self.spawn(npc, False)
        return npc

    def spawn(self, npc, setLevel=True):
        if not npc.getLevel():
            if setLevel:
                npc.setLevel(0) # Random

        self.gameArea.generateChild(npc)

    @classmethod
    def missingClass(cls, avType):
        cls._missing.add(avType)

    @classmethod
    def printMissingTypes(cls):
        if not cls._missing:
            return

        cls.notify.warning('Missing avatar types:')
        for avType in cls._missing:
            print '   %r' % avType

        del cls._missing
