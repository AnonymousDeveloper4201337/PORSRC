# File: P (Python 2.4)

global defaultRolloverSound, defaultClickSound
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
MaxTotalRevealTime = 2.0
ItemRevealTime = 0.348
PageFinishWaitTime = 1.0
GridSize = 0.050000
ProgressMsgOffset = 0.299
GridCell = 0.050000
BorderWidth = (0.01, 0.01)
BorderWidthSmall = (0.00500, 0.00500)
FrameColor = (0.27, 0.239, 0.200, 0.75)
OpaqueFrameColor = (0.27, 0.239, 0.200, 1)
FrameColor = (0.27, 0.239, 0.200, 1)
TextFG0 = (0, 0, 0, 1)
TextFG1 = (1, 0.9, 0.696, 1)
TextFG2 = (1, 1, 1, 1)
TextFG3 = (0.75, 0.75, 0.75, 1)
TextFG4 = (0.299, 0.696, 0.25, 1)
TextFG5 = (0.4, 0.598, 1, 1)
TextFG6 = (1.0, 0.100, 0.100, 1)
TextFG7 = (0.16, 0.149, 0.13, 1)
TextFG8 = (0.978, 0.96, 0.540000, 1)
TextFG9 = (0.450, 0.450, 0.450, 1)
TextFG10 = (0.800000, 1.0, 0.800000, 1)
TextFG11 = (1, 0.696, 0, 1)
TextFG12 = (0.598, 0.100, 0.946, 1)
TextFG13 = (0.9, 0.9, 0.0, 1)
TextFG14 = (0.800000, 0.696, 0.5, 1)
TextFG15 = (0.5, 0.100, 0.100, 1)
TextFG16 = (0.209, 0.125, 0.035000, 1)
TextFG17 = (1, 0.800000, 0.4, 1)
TextFG18 = (0.598, 0.9, 0.299, 1)
TextFG19 = (0.0, 1.0, 0.0, 1)
TextFG20 = (0.598, 0.0, 1.0, 1)
TextFG21 = (0.75, 0.75, 0.0, 1)
TextFG22 = (0.598, 0.299, 1.0, 1)
TextFG23 = (0.598, 0.0, 0.0, 1)
TextFG24 = (0.790000, 0.5, 0.140, 1)
TextFG25 = (0.72265625, 0.60546875, 0.23046875, 1)
TextFG26 = (0.5, 0.08, 0.0179, 1)
TextFG27 = (1.0, 1.0, 0.299, 1)
TextLT5 = (0.675000, 0.848, 1, 1)
TextLT11 = (1, 0.800000, 0.200, 1)
TextLT13 = (0.9, 0.9, 0.5, 1)
TextLT12 = (0.946, 0.75, 0.97498, 1)
TextLT14 = (0.9, 0.848, 0.75, 1)
TextLT17 = (1, 0.9, 0.696, 1)
TextOV5 = (0.348, 0.598, 1, 1)
TextOV6 = (0.75, 0.100, 0.100, 1)
TextOV11 = (0.800000, 0.4, 0, 1)
TextOV12 = (0.696, 0.348, 0.75, 1)
TextOV13 = (0.65, 0.65, 0.0, 1)
TextOV14 = (0.696, 0.598, 0.4, 1)
TextOV17 = (0.800000, 0.598, 0.299, 1)
TextOV18 = (0.5, 0.598, 0.200, 1)
TextOV19 = (0.200, 0.800000, 0.25, 1)
TextOV20 = (0.5, 0.0, 0.800000, 1)
TextShadow = (0, 0, 0, 1)
TextScaleTitleJumbo = 0.12
TextScaleTitleLarge = 0.100
TextScaleTitleMed = 0.08
TextScaleTitleSmall = 0.0598
TextScaleExtraLarge = 0.050000
TextScaleLarge = 0.0400
TextScaleMed = 0.035000
TextScaleSmall = 0.0299
TextScaleTiny = 0.0250
TextScaleMicro = 0.023
ButtonColor1 = ((0.33, 0.299, 0.260, 0.800000), (0.260, 0.239, 0.209, 0.800000), (0.489, 0.450, 0.390, 0.800000), (0.16, 0.149, 0.13, 0.800000))
ButtonColor2 = ((0.260, 0.239, 0.209, 0.800000), (0.16, 0.149, 0.13, 0.800000), (0.33, 0.299, 0.260, 0.800000), (0.08, 0.074, 0.0598, 0.800000))
ButtonColor3 = ((0.696, 0.100, 0.100, 0.9), (0.800000, 0.4, 0.4, 0.9), (0.800000, 0.299, 0.299, 0.9), (0.598, 0.200, 0.200, 0.9))
ButtonColor4 = ((0.200, 0.5, 0.200, 0.9), (0.4, 0.598, 0.4, 0.9), (0.299, 0.598, 0.299, 0.9), (0.200, 0.4, 0.200, 0.9))
ButtonColor5 = ((0.576, 0.550000, 0.510, 0.800000), (0.260, 0.239, 0.209, 0.800000), (0.489, 0.450, 0.390, 0.800000), (0.16, 0.149, 0.13, 0.800000))
ButtonColor6 = ((0.4, 0.946, 0.4, 1.0), (0.598, 1.0, 0.598, 1.0), (0.598, 1.0, 0.598, 1.0), (0.200, 0.5, 0.200, 1.0))
ImageButtonColor1 = (1, 1, 1, 1)
ScrollbarColor = (0.100, 0.100, 0.25, 0.9)
ScrollbarSize = 0.0400
TutorialPanelWidth = 0.450
TutorialPanelHeight = 0.450
InventoryPanelWidth = 1.10
InventoryPanelHeight = 1.5
InventoryItemGuiWidth = 0.525
InventoryItemGuiHeight = 0.16
PurchaseListItemWidth = 0.525
PurchaseListItemHeight = 0.050000
InventoryInfoWidth = 0.75
InventoryInfoHeight = 0.149
ShipItemGuiWidth = 0.525
ShipItemGuiHeight = 0.16
SocialPanelWidth = 0.670000
SocialPanelHeight = 0.800000
ShipPanelWidth = 1.0
ShipPanelHeight = 1.39
ShipTargetPanelWidth = 0.696
ShipTargetPanelHeight = 0.200
NamePanelWidth = 1.0
NamePanelHeight = 0.696
ObjectivesPanelWidth = 0.800000
ObjectivesPanelHeight = 0.4
ObjectivesPageWidth = ObjectivesPanelWidth - BorderWidth[0] * 2
ObjectivesPageHeight = ObjectivesPanelHeight - BorderWidth[0] * 2 - GridCell
PVPPanelWidth = 0.5
PVPPanelHeight = 0.25
PVPPageWidth = PVPPanelWidth - BorderWidth[0] * 2
PVPPageHeight = PVPPanelHeight - BorderWidth[0] * 2 - GridCell
TMCompleteTitleHeight = 0.200
TMCompletePanelWidth = 2.5
TMCompletePanelHeight = 1.7
TMCompletePageWidth = TMCompletePanelWidth - BorderWidth[0] * 2
TMCompletePageHeight = TMCompletePanelHeight - BorderWidth[0] * 2 - TMCompleteTitleHeight
PVPCompleteTitleHeight = 0.200
PVPCompletePanelWidth = 2.5
PVPCompletePanelHeight = 1.7
PVPCompletePageWidth = PVPCompletePanelWidth - BorderWidth[0] * 2
PVPCompletePageHeight = PVPCompletePanelHeight - BorderWidth[0] * 2 - PVPCompleteTitleHeight
ScorePanelWidth = PVPCompletePageWidth / 2.0
ScorePanelHeight = PVPCompletePageHeight
PortTitleHeight = 0.0598
PortPanelWidth = 2.10
PortPanelHeight = 1.89
PortPageWidth = PortPanelWidth - BorderWidth[0] * 2
PortPageHeight = PortPanelHeight - BorderWidth[0] * 2 - PortTitleHeight
InventoryPageWidth = InventoryPanelWidth - BorderWidth[0] * 2
InventoryPageHeight = InventoryPanelHeight - GridCell * 2 - BorderWidth[0] * 2
SocialPageWidth = SocialPanelWidth - BorderWidth[0] * 2
SocialPageHeight = SocialPanelHeight - GridCell - BorderWidth[0] * 2
LookoutRequestLVL1Width = 1.0
LookoutRequestLVL1Height = 1.2
LookoutRequestLVL2Width = 1.0
LookoutRequestLVL2Height = 0.5
LookoutRequestLVL3Width = 1.0
LookoutRequestLVL3Height = 1.0
OptionItemWidth = 1.0
OptionItemHeight = 0.299
HelpPopupTime = 0.25
DragStartDelayTime = 0.200
LootPopupTime = 7.0
InventoryTradeEvent = 'InventoryTradeEvent'
InventorySellEvent = 'InventorySellEvent'
InventoryBuyEvent = 'InventoryBuyEvent'
InventoryUseEvent = 'InventoryUseEvent'
InventoryAdd = 1
InventoryRemove = -1
CrewButtonCaptainColor = ButtonColor4
GuildButtonCaptainColor = ButtonColor4
CrewButtonMemberColor = ButtonColor1
GuildButtonMemberColor = ButtonColor1
UIListItemType_Generic = 0
UIListItemType_ColumHeadings = 1
UIItemType_ListItem = 0
UIItemType_Choice = 1
UIItemType_DropDown = 2
UIItemType_Entry = 3
UIItemType_Label = 4
UIItemType_Hidden = 5
REQUEST_CAT_MODE = 0
REQUEST_TYPE_MODE = 1
REQUEST_TYPE_DIRECT_MODE = 2
REQUEST_OPT_MODE = 3
REQUEST_FOUND_MODE = 4
REQUEST_JOIN_MODE = 5
SEARCH_MODE = 6
INVITE_MODE = 7
INVITE_ACCEPTED_MODE = 8
CHALLENGE_MODE = 9
WAIT_FOR_OTHERS = 10
defaultRolloverSound = None
defaultClickSound = None
CREW_HUD_ICON_NONE = 0
CREW_HUD_ICON_CUTLASS = 1
CREW_HUD_ICON_PISTOL = 2
CREW_HUD_ICON_DOLL = 3
CREW_HUD_ICON_DAGGER = 4
CREW_HUD_ICON_GRENADE = 5
CREW_HUD_ICON_STAFF = 6
CREW_HUD_ICON_CANNON = 7
CREW_HUD_ICON_STEERINGWHEEL = 8
CREW_HUD_ICON_ONSHIP = 9
CREW_HUD_ICON_CARDGAME = 10
CREW_HUD_ICON_PVP = 11
CREW_HUD_ICON_AFK = 12
CREW_HUD_ICON_INJURED = 13
PROFILE_ICON_LAND = 0
PROFILE_ICON_OCEAN = 1
PROFILE_ICON_CANNON = 2

def getDefaultRolloverSound():
    global defaultRolloverSound
    if defaultRolloverSound == None:
        defaultRolloverSound = loadSfx(SoundGlobals.SFX_GUI_ROLLOVER_01)
        defaultRolloverSound.setVolume(0.5)

    return defaultRolloverSound


def getDefaultClickSound():
    global defaultClickSound
    if defaultClickSound == None:
        defaultClickSound = loadSfx(SoundGlobals.SFX_GUI_CLICK_01)

    return defaultClickSound

REWARD_PANEL_DOLL = 1
REWARD_PANEL_STAFF = 2
REWARD_PANEL_DAGGER = 3
REWARD_PANEL_GRENADE = 4
REWARD_PANEL_BLACK_PEARL = 5
REWARD_PANEL_RAVENS_COVE_A = 6
REWARD_PANEL_RAVENS_COVE_B = 7
REWARD_PANEL_RAVENS_COVE_C = 8
