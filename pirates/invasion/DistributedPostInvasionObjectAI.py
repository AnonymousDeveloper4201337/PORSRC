from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedPostInvasionObjectAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPostInvasionObjectAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)


