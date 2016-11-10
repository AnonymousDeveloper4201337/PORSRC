from direct.directnotify import DirectNotifyGlobal
from pirates.npc.DistributedNPCSkeletonAI import DistributedNPCSkeletonAI
from pirates.npc.BossAI import BossAI

class DistributedBossSkeletonAI(DistributedNPCSkeletonAI, BossAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBossSkeletonAI')

    #def __init__(self, spawner):
    #    DistributedNPCSkeletonAI.__init__(self, spawner.air)
    #    BossAI.__init__(self, spawner.air)

    @staticmethod
    def makeFromObjectKey(cls, spawner, uid, avType, data):
        obj = DistributedNPCSkeletonAI.makeFromObjectKey(cls, spawner, uid, avType, data)
        obj._setupBossValues(data['DNA'], avType)
        return obj