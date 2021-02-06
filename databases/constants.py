#Location constants
DATABASE_LOC = "/Users/jean/Documents/Dev/AutoSld/databases/"
GDRIVE = "/Volumes/GoogleDrive/.shortcut-targets-by-id/0B48f_ri5yfeAcVBIT3M3bTZBTW8/Shared Docs/PROJECTS/Customers - Domestic Jobs"

#Constants for main.py:
APP_NAME = "Lets go"
WINDOW_SIZE_X = 730
WINDOW_SIZE_Y = 620

#SELECTING THE THEME
#APP_THEME = "black"
#APP_THEME = "aquativo"
APP_THEME = "aqua"

STC_AC_DC_LIMIT = 1.33

###############################################################################
                        #PAGE INFO TECHNICAL POSITION#
###############################################################################

TITLE_PADY_PGINFO = 16
PADX_CHK_PGINFO = 40

#ROW_PARAMETRING
ROW_TITLE_1_PGINFO = 1
ROW_CLIENT_NAME_PGINFO =2
ROW_SITE_ADDRESS_PGINFO = 3
ROW_JOB_NUMBER_PGINFO = 4
ROW_MSB_PHASES_PGINFO= 5
ROW_TITLE_2_PGINFO = 6
ROW_PANEL_MANUFACTURER_PGINFO = 7
ROW_INV_TYPE_PGINFO = 7
ROW_PANEL_MODEL_PGINFO = 8
ROW_INV_MANUFACTURER_PGINFO = 8
ROW_PANEL_NUMBER_PGINFO = 9
ROW_INV_MODEL_PGINFO = 9
ROW_BUTT_DATASHEET_PGINFO = 10
ROW_TITLE_3_PGINFO= 11
ROW_MONITORING_PGINFO = 12
ROW_EXISTING_ARRAY_PGINFO = 13
ROW_BATTERY_PGINFO = 14
ROW_BLOCK_DIAGRAM_PGINFO = 15
ROW_GATEWAY_PGINFO= 16
ROW_NOTES_PGINFO = 17

#COL_PARAMETRING
COL_GATEWAY_CHK_PGINFO=0
COL_BATTERY_CHK_PGINFO=0
COL_EXISTING_ARRAY_CHK_PGINFO=0
COL_BLOCK_DIAGRAM_CHK_PGINFO=0
COL_MONITORING_CHK_PGINFO=0
COL_NOTES_PGINFO=0



###############################################################################
                        #PAGE INFO TECHNICAL POSITION#
###############################################################################

COLUMN1_NAME_PADX_PGVRISE = COLUMN2_NAME_PADX_PGVRISE = COLUMN3_NAME_PADX_PGVRISE = 40
ROW_SPACING_TABLE_PADY_PGVRISE = 4
SPACING_FROM_TITLE_PGVRISE = 10

#ROW_PARAMETRING
ROW_NAME_ENT_PGVRISE=2
ROW_PHASE_ENT_PGVRISE =3
ROW_CONDUCTOR_ENT_PGVRISE=4
ROW_SIZE_ENT_PGVRISE=5
ROW_IMAX_ENT_PGVRISE=6
ROW_CCC_ENT_PGVRISE=7
ROW_LENGHT_ENT_PGVRISE=8
ROW_AM_ENT_PGVRISE=9
ROW_VDROP_ENT_PGVRISE=10
ROW_TOTAL_PRC_ENT_PGVRISE=11
ROW_CALC_BUTT_PGVRISE=12
ROW_NOTES_ENT_PGVRISE=13



###############################################################################
                        #PAGE LAYOUT TECHNICAL POSITION#
###############################################################################
Y_POS_CANV_TITLE_PGLAYOUT = 30
LAYOUT_STRING_WIDTH_PGLAYOUT = 530
LAYOUT_STRING_HEIGHT_PGLAYOUT = 450



###############################################################################
                        #ALL THE CONSTANT FUNCTIONS DEFINED HERE#
###############################################################################
import darkdetect

def set_entries_background_for_darkmode():
    if darkdetect.isDark() == True:
        return  "#424242"
    else:
        return "#FAFAFA"
#function to set the background color depending on Theme
def set_baground_for_theme():
    if APP_THEME == "black":
        return "#424242"
    if APP_THEME == "aquativo":
        return "#FAFAFA"
