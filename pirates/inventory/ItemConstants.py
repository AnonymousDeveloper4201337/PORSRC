from panda3d.core import VBase4
WEAPON_RANGE = 10000
CHARM_RANGE = 15000
CONSUMABLE_RANGE = 20000
CLOTHING_RANGE = 30000
JEWELRY_RANGE = 35000
TATTOO_RANGE = 40000
NOT_LIVE = 0
READY_TO_GO_LIVE = 1
LIVE = 2
CRUDE = 1
COMMON = 2
RARE = 3
FAMED = 4
LEGENDARY = 5
WEAPON = 1
HANDHELD = 2
CONSUMABLE = 3
TREASURE = 4
SWORD = 1
GUN = 2
DOLL = 3
DAGGER = 4
GRENADE = 5
STAFF = 6
CANNON = 7
SAILING = 8
AXE = 9
FENCING = 10
POTION = 11
ODDS_AND_ENDS = 12
MONSTER = 13
FISHING = 14
QUEST_PROP = 15
CUTLASS = 1
SABRE = 2
BROADSWORD = 3
SCIMITAR = 4
CURSED_CUTLASS = 5
PISTOL = 6
REPEATER = 7
MUSKET = 8
BLUNDERBUSS = 9
BAYONET = 10
BASIC_DOLL = 11
BANE = 12
MOJO = 13
SPIRIT = 14
DAGGER_SUBTYPE = 15
DIRK = 16
KRIS = 17
BASIC_STAFF = 18
DARK = 19
NATURE = 20
WARDING = 21
RAM = 22
BOARDING = 23
RAPIER = 24
EPEE = 25
CARRONADE = 26
HEALING = 27
NAVIGATION_TOOL = 28
SPYGLASS = 29
SEA_CHARM = 30
POTION_BUFF = 31
DUAL_CUTLASS = 32
MONSTER_SUBTYPE = 33
FISHING_SUBTYPE = 34
QUEST_PROP_TORCH = 35
QUEST_PROP_POWDER_KEG = 36
CURSED_SABRE = 37
CURSED_BROADSWORD = 38
GRENADE_SUBTYPE = 39
DUAL_SCIMITAR = 40
ANY_USE = 1
LOOT_DROP = 2
QUEST_ONLY = 3
SHOP_ONLY = 4
LOOT_AND_QUEST_ITEM = 5
LOOT_AND_SHOP_ITEM = 6
QUEST_AND_SHOP_ITEM = 7
BOSS_ONLY = 8
PVP_REWARD = 9
PROMO = 10
NOT_USED = 11
REASON_NONE = 0
REASON_GENDER = 1
REASON_LEVEL = 2
REASON_CANTPLACE = 3
REASON_INVENTORY = 4
PistolSharpShooter = 1
PistolEagleEye = 2
Scattershot = 3
SAILING_SINK_HER = 4
INCOMING = 5
LeadShot = 1
CRITICAL = 100
VENOM = 101
WOUNDING = 102
POWERFUL = 103
ANTI_VOODOO_ZOMBIE = 105
PROTECT_COMBAT = 110
PROTECT_MISSILE = 111
PROTECT_MAGIC = 112
PROTECT_GRENADE = 113
DAMAGE_MANA = 120
SURE_FOOTED = 121
BLOOD_FIRE = 122
INFINITE_VENOM_SHOT = 130
INFINITE_BANE_SHOT = 131
INFINITE_HEX_EATER_SHOT = 132
INFINITE_SILVER_SHOT = 133
INFINITE_STEEL_SHOT = 134
INFINITE_ASP = 140
INFINITE_ADDER = 141
INFINITE_SIDEWINDER = 142
INFINITE_VIPER_NEST = 143
INFINITE_CHAIN_SHOT = 150
INFINITE_EXPLOSIVE = 151
INFINITE_GRAPE_SHOT = 152
INFINITE_FIREBRAND = 153
INFINITE_THUNDERBOLT = 154
INFINITE_FURY = 155
LEECH_HEALTH = 160
LEECH_VOODOO = 161
CRITICAL_ROUND_SHOT = 170
CRITICAL_CHAIN_SHOT = 171
CRITICAL_EXPLOSIVE = 172
CRITICAL_GRAPE_SHOT = 173
CRITICAL_FIREBRAND = 174
CRITICAL_FURY = 175
RANGE_ROUND_SHOT = 180
RANGE_CHAIN_SHOT = 181
RANGE_EXPLOSIVE = 182
RANGE_GRAPE_SHOT = 183
RANGE_FIREBRAND = 184
RANGE_FURY = 185
IMMUNITY_POISON = 200
IMMUNITY_ACID = 201
IMMUNITY_BLIND = 202
IMMUNITY_FIRE = 203
IMMUNITY_HOLD = 204
IMMUNITY_STUN = 205
IMMUNITY_CURSE = 206
IMMUNITY_PAIN = 207
IMMUNITY_WEAKEN = 208
IMMUNITY_LIFEDRAIN = 209
HALF_DURATION_POISON = 220
HALF_DURATION_ACID = 221
HALF_DURATION_BLIND = 222
HALF_DURATION_FIRE = 223
HALF_DURATION_HOLD = 224
HALF_DURATION_STUN = 225
HALF_DURATION_CURSE = 226
HALF_DURATION_PAIN = 227
HALF_DURATION_WOUND = 228
HALF_DAMAGE_LIFEDRAIN = 229
HALF_DAMAGE_SOULTAP = 230
NAVIGATION = 1001
GOLD = 1
WHITE = 2
RED = 3
BLUE = 4
GREEN = 5
YELLOW = 6
BROWN = 7
REDBROWN = 8
YELLOWBROWN = 9
GRAY = 10
PEACH = 11
LIGHTBLUE = 12
LIGHTGREEN = 13
LIGHTYELLOW = 14
HOTPINK = 15
GRAYBLUE = 16
GRAYGREEN = 17
GRAYRED = 18
GRAYYELLOW = 19
LIGHTGRAY = 20
ORANGE = 21
YELLOWORANGE = 22
TAN = 23
BLUEJEAN = 24
PURPLE = 25
VIOLET = 26
LIGHTPURPLE = 27
DIRTYWHITE = 28
DARKGRAY = 29
AQUA = 30
DARKBROWN = 31
BLACKGRAY = 32
LIGHTAQUA = 33
SOFTPINK = 34
LIGHTBURGUNDY = 35
BURGUNDY = 36
BLUEWHITE = 37
FORESTGREEN = 38
ROSE = 39
DIRTYRED = 40
DARKFORESTGREEN = 41
MONEYGREEN = 42
DARKJEAN = 43
DARKAQUA = 44
DARKERFORESTGREEN = 45
DARKBURGUNDY = 46
DEEPPURPLE = 47
GRAYBROWN = 48
BURGUNDYBROWN = 49
YELLOWGOLD = 50
COLOR_VALUES = {
    WHITE: (1.0, 1.0, 1.0),
    DIRTYWHITE: (0.9, 0.9, 0.8),
    BLUEWHITE: (0.85, 0.9, 1.0),
    RED: (1.0, 0.25, 0.25),
    BLUE: (0.3, 0.4, 1.0),
    GREEN: (0.3, 1.0, 0.3),
    DIRTYRED: (0.8, 0.27, 0.27),
    MONEYGREEN: (0.75, 0.85, 0.45),
    FORESTGREEN: (0.55, 0.7, 0.35),
    DARKFORESTGREEN: (0.3, 0.45, 0.2),
    DARKERFORESTGREEN: (0.23, 0.32, 0.18),
    ORANGE: (1.0, 0.6, 0.1),
    YELLOWORANGE: (1.0, 0.8, 0.2),
    YELLOW: (1.0, 1.0, 0.3),
    TAN: (0.9, 0.75, 0.6),
    YELLOWGOLD: (1.0, 0.95, 0.2),
    GOLD: (1.0, 1.0, 0.7),
    BROWN: (0.65, 0.55, 0.25),
    GRAYBROWN: (0.6, 0.5, 0.35),
    REDBROWN: (0.7, 0.4, 0.2),
    YELLOWBROWN: (0.6, 0.6, 0.2),
    DARKBROWN: (0.4, 0.3, 0.25),
    BURGUNDYBROWN: (0.57, 0.37, 0.36),
    LIGHTGRAY: (0.8, 0.8, 0.8),
    GRAY: (0.6, 0.6, 0.6),
    DARKGRAY: (0.4, 0.4, 0.4),
    BLACKGRAY: (0.3, 0.3, 0.3),
    PEACH: (1.0, 0.7, 0.7),
    ROSE: (1.0, 0.55, 0.45),
    HOTPINK: (1.0, 0.3, 0.9),
    SOFTPINK: (1.0, 0.7, 0.8),
    PURPLE: (0.7, 0.3, 1.0),
    DEEPPURPLE: (0.42, 0.2, 0.38),
    VIOLET: (0.9, 0.7, 0.9),
    LIGHTPURPLE: (0.9, 0.8, 1.0),
    LIGHTBURGUNDY: (0.9, 0.7, 0.8),
    BURGUNDY: (0.75, 0.35, 0.5),
    DARKBURGUNDY: (0.55, 0.25, 0.38),
    LIGHTBLUE: (0.6, 0.7, 1.0),
    LIGHTGREEN: (0.6, 1.0, 0.6),
    LIGHTYELLOW: (1.0, 1.0, 0.65),
    GRAYBLUE: (0.3, 0.4, 0.6),
    GRAYGREEN: (0.4, 0.5, 0.4),
    GRAYRED: (0.6, 0.3, 0.3),
    GRAYYELLOW: (0.6, 0.6, 0.3),
    AQUA: (0.4, 0.9, 0.75),
    LIGHTAQUA: (0.6, 1.0, 0.9),
    DARKAQUA: (0.24, 0.4, 0.37),
    BLUEJEAN: (0.75, 0.8, 1.0),
    DARKJEAN: (0.2, 0.25, 0.4) }
DYE_COLORS = [
    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 255 / 255.0),
    VBase4(194 / 255.0, 210 / 255.0, 222 / 255.0, 255 / 255.0),
    VBase4(255 / 255.0, 233 / 255.0, 198 / 255.0, 255 / 255.0),
    VBase4(208 / 255.0, 213 / 255.0, 152 / 255.0, 255 / 255.0),
    VBase4(164 / 255.0, 99 / 255.0, 60 / 255.0, 255 / 255.0),
    VBase4(196 / 255.0, 144 / 255.0, 147 / 255.0, 255 / 255.0),
    VBase4(189 / 255.0, 181 / 255.0, 197 / 255.0, 255 / 255.0),
    VBase4(167 / 255.0, 167 / 255.0, 167 / 255.0, 255 / 255.0),
    VBase4(146 / 255.0, 177 / 255.0, 188 / 255.0, 255 / 255.0),
    VBase4(226 / 255.0, 198 / 255.0, 137 / 255.0, 255 / 255.0),
    VBase4(155 / 255.0, 159 / 255.0, 107 / 255.0, 255 / 255.0),
    VBase4(148 / 255.0, 112 / 255.0, 72 / 255.0, 255 / 255.0),
    VBase4(158 / 255.0, 75 / 255.0, 80 / 255.0, 255 / 255.0),
    VBase4(152 / 255.0, 145 / 255.0, 159 / 255.0, 255 / 255.0),
    VBase4(94 / 255.0, 94 / 255.0, 94 / 255.0, 255 / 255.0),
    VBase4(83 / 255.0, 108 / 255.0, 135 / 255.0, 255 / 255.0),
    VBase4(161 / 255.0, 133 / 255.0, 72 / 255.0, 255 / 255.0),
    VBase4(106 / 255.0, 121 / 255.0, 96 / 255.0, 255 / 255.0),
    VBase4(101 / 255.0, 68 / 255.0, 32 / 255.0, 255 / 255.0),
    VBase4(110 / 255.0, 43 / 255.0, 47 / 255.0, 255 / 255.0),
    VBase4(115 / 255.0, 105 / 255.0, 126 / 255.0, 255 / 255.0),
    VBase4(220 / 255.0, 111 / 255.0, 45 / 255.0, 255 / 255.0),
    VBase4(250 / 255.0, 208 / 255.0, 117 / 255.0, 255 / 255.0),
    VBase4(59 / 255.0, 178 / 255.0, 220 / 255.0, 255 / 255.0),
    VBase4(158 / 255.0, 113 / 255.0, 207 / 255.0, 255 / 255.0),
    VBase4(87 / 255.0, 141 / 255.0, 88 / 255.0, 255 / 255.0),
    VBase4(190 / 255.0, 67 / 255.0, 128 / 255.0, 255 / 255.0),
    VBase4(46 / 255.0, 190 / 255.0, 68 / 255.0, 255 / 255.0),
    VBase4(70 / 255.0, 126 / 255.0, 219 / 255.0, 255 / 255.0),
    VBase4(201 / 255.0, 14 / 255.0, 14 / 255.0, 255 / 255.0),
    VBase4(21 / 255.0, 22 / 255.0, 24 / 255.0, 255 / 255.0),
    VBase4(206 / 255.0, 231 / 255.0, 153 / 255.0, 255 / 255.0),
    VBase4(252 / 255.0, 190 / 255.0, 171 / 255.0, 255 / 255.0),
    VBase4(226 / 255.0, 203 / 255.0, 249 / 255.0, 255 / 255.0),
    VBase4(133 / 255.0, 208 / 255.0, 222 / 255.0, 255 / 255.0),
    VBase4(203 / 255.0, 177 / 255.0, 122 / 255.0, 255 / 255.0),
    VBase4(150 / 255.0, 173 / 255.0, 100 / 255.0, 255 / 255.0),
    VBase4(237 / 255.0, 188 / 255.0, 216 / 255.0, 255 / 255.0),
    VBase4(185 / 255.0, 167 / 255.0, 203 / 255.0, 255 / 255.0),
    VBase4(72 / 255.0, 146 / 255.0, 159 / 255.0, 255 / 255.0),
    VBase4(195 / 255.0, 100 / 255.0, 154 / 255.0, 255 / 255.0),
    VBase4(148 / 255.0, 127 / 255.0, 171 / 255.0, 255 / 255.0),
    VBase4(107 / 255.0, 107 / 255.0, 107 / 255.0, 255 / 255.0),
    VBase4(41 / 255.0, 50 / 255.0, 60 / 255.0, 255 / 255.0),
    VBase4(178 / 255.0, 147 / 255.0, 80 / 255.0, 255 / 255.0)]
SLOW = 1
NORMAL = 2
FAST = 3
SHORT = 1
MEDIUM = 2
LONG = 3
MotionBlurDefault = 0
MotionBlurRusty = 1
MotionBlurIron = 2
MotionBlurSteel = 3
MotionBlurFine = 4
MotionBlurPirate = 5
MotionBlurDark = 6
MotionBlurGreen = 19
MotionBlurRed = 20
DollDefault = 7
DollCloth = 8
DollWitch = 9
DollPirate = 10
DollTaboo = 11
DollMojo = 12
GemGlowPurple = 13
GemGlowGreen = 14
GemGlowRed = 15
GemGlowBlue = 16
GemGlowMagenta = 17
GemGlowOrange = 18
HAT = 0
SHIRT = 1
VEST = 2
COAT = 3
PANT = 4
BELT = 5
SOCK = 6
SHOE = 7
BROW = 0
EAR = 1
NOSE = 2
MOUTH = 3
HAND = 4
CHEST = 0
ARM = 1
FACE = 2
MaleChestFullTorso = 1
MaleChestUpperChest = 2
MaleChestHPeck = 3
MaleChestRight = 4
MaleChestPBrand = 5
MaleChestLScar = 6
MaleChestBulletHoles = 7
MaleChestLX = 8
MaleChestLY = 9
FemaleChestFullChest = 101
FemaleChestUpperChest = 102
FemaleChestLeftBreast = 103
FemaleChestHPeck = 104
FemaleChestBulletHoles = 105
FemaleChestPBrand = 106
FemaleChestLScar = 107
FemaleChestLX = 108
FemaleChestLY = 109
MaleArmLeftUpper = 210
MaleArmLeftFlag = 211
MaleArmLeftSleeve = 212
MaleArmLeftLower = 213
MaleArmLeftLowerFlag = 214
MaleArmLeftLowerSleeve = 215
FemaleArmLeftUpper = 310
FemaleArmLeftFlag = 311
FemaleArmLeftSleeve = 312
FemaleArmLeftLower = 313
FemaleArmLeftLowerFlag = 314
FemaleArmLeftLowerSleeve = 315
MaleArmRightUpper = 410
MaleArmRightFlag = 411
MaleArmRightSleeve = 412
MaleArmRightLower = 413
MaleArmRightLowerFlag = 414
MaleArmRightLowerSleeve = 415
FemaleArmRightUpper = 510
FemaleArmRightFlag = 511
FemaleArmRightSleeve = 512
FemaleArmRightLower = 513
FemaleArmRightLowerFlag = 514
FemaleArmRightLowerSleeve = 515
MaleFace1 = 601
MaleFace2 = 602
MaleFace3 = 603
MaleFace4 = 604
MaleFace5 = 605
MaleFace6 = 606
MaleFace7 = 607
MaleFace8 = 608
MaleFace9 = 609
MaleFace10 = 610
MaleFace11 = 611
MaleFace12 = 612
MaleFace13 = 613
MaleFace14 = 614
MaleFace15 = 615
MaleFace16 = 616
FemaleFace1 = 701
FemaleFace2 = 702
FemaleFace3 = 703
FemaleFace4 = 704
FemaleFace5 = 705
FemaleFace6 = 706
FemaleFace7 = 707
FemaleFace8 = 708
FemaleFace9 = 709
FemaleFace10 = 710
FemaleFace11 = 711
FemaleFace12 = 712
FemaleFace13 = 713
FemaleFace14 = 714
FemaleFace15 = 715
FemaleFace16 = 716
