#Location constants
DATABASE_LOC = "/Users/jean/Documents/Dev/SmartSolarDesign/databases/"
GDRIVE = "/Volumes/GoogleDrive/.shortcut-targets-by-id/0B48f_ri5yfeAcVBIT3M3bTZBTW8/Shared Docs/PROJECTS/Customers - Domestic Jobs"
EXCEL_LOC = "/Users/jean/Documents/Dev/SmartSolarDesign/excel/ExcelTemplatesHCB"
DESKTOP_LOC = "/Users/jean/Desktop"

#Constants for main.py:
APP_NAME = " Smart Solar Design"
WINDOW_SIZE_X = 750
WINDOW_SIZE_Y = 620

#SELECTING THE THEME
#APP_THEME = "black"
#APP_THEME = "aquativo"
APP_THEME = "aqua"

STC_AC_DC_LIMIT = 0.75

###############################################################################
                        #PAGE MENU TECHNICAL POSITION#
###############################################################################$


COLOR_BUTT_HIGHLIGHT_PGMENU = "#EC6A5E"
START_POSX_BUTT_PGMENU = 260
END_POSX_BUTT_PGMENU = 535
START_POSY_BUTT1_PGMENU = 209
END_POSY_BUTT1_PGMENU = 249
START_POSY_BUTT2_PGMENU = 280
END_POSY_BUTT2_PGMENU = 320
START_POSY_BUTT3_PGMENU = 350
END_POSY_BUTT3_PGMENU = 390
START_POSY_BUTT4_PGMENU = 420
END_POSY_BUTT4_PGMENU = 460
START_POSX_BUTT_SETT_PGMENU = 630
END_POSX_BUTT_SETT_PGMENU = 670
START_POSX_BUTT_ACC_PGMENU = 685
END_POSX_BUTT_ACC_PGMENU = 730
START_POSY_SETT_PGMENU = 30
END_POSY_SETT_PGMENU = 70

###############################################################################
                        #PAGE SETTING#
###############################################################################$


COLOR_BUTT_HIGHLIGHT_PGSETT = "#EC6A5E"
WINDOW_SIZE_X_PGSETT = 600
WINDOW_SIZE_Y_PGSETT = 500
START_POSX_BUTT1_PGSETT = 80
END_POSX_BUTT1_PGSETT = 195
START_POSY_BUTT1_PGSETT = 105
END_POSY_BUTT1_PGSETT = 190
START_POSX_BUTT2_PGSETT = 250
END_POSX_BUTT2_PGSETT = 355
START_POSX_BUTT3_PGSETT = 420
END_POSX_BUTT3_PGSETT = 525
START_POSX_BUTT_EXIT_PGSETT = 240
END_POSX_BUTT_EXIT_PGSETT = 380
START_POSY_BUTT_EXIT_PGSETT = 355
END_POSY_BUTT_EXIT_PGSETT = 385



###############################################################################
                        #PAGE INFO TECHNICAL POSITION#
###############################################################################

TITLE_PADY_PGINFO = 10
PADX_CHK_PGINFO = 0
EMPTY_PADY_PGINFO = 5

#ROW_PARAMETRING
ROW_EMPTY0_PGINFO = 1 # Can remove as its useless but might come in handy
ROW_TITLE_1_PGINFO = 1
ROW_CLIENT_NAME_PGINFO =3
ROW_SITE_ADDRESS_PGINFO = 4
ROW_JOB_NUMBER_PGINFO = 5
ROW_MSB_PHASES_PGINFO= 6
ROW_EMPTY1_PGINFO = 7
ROW_TITLE_2_PGINFO = 8
ROW_PANEL_MANUFACTURER_PGINFO = 9
ROW_INV_TYPE_PGINFO = 9
ROW_PANEL_MODEL_PGINFO = 10
ROW_PANEL_SERIAL_PGINFO = 11
ROW_PANEL_NUMBER_PGINFO = 12
ROW_INV_MANUFACTURER_PGINFO = 10
ROW_INV_MODEL_PGINFO = 11
ROW_INV_SERIAL_PGINFO = 12
ROW_BUTT_DATASHEET_PGINFO = 13
ROW_EMPTY2_PGINFO = 14
ROW_TITLE_3_PGINFO= 15
ROW_MONITORING_PGINFO = 16
ROW_EXISTING_ARRAY_PGINFO = 17
ROW_BATTERY_PGINFO = 18
ROW_GATEWAY_PGINFO= 19
ROW_NOTES_PGINFO = 20

#COL_PARAMETRING
COL_GATEWAY_CHK_PGINFO=1
COL_BATTERY_CHK_PGINFO=1
COL_EXISTING_ARRAY_CHK_PGINFO=1
COL_BLOCK_DIAGRAM_CHK_PGINFO=1
COL_MONITORING_CHK_PGINFO=1
COL_NOTES_PGINFO=1



###############################################################################
                        #PAGE VRISE TECHNICAL POSITION#
###############################################################################


COLUMN_PAD_X_TABLE = 100
ROW_SPACING_TABLE_PADY_PGVRISE = 4
SPACING_FROM_TITLE_PGVRISE = 5

#ROW_PARAMETRING
ROW_TITLE_1_PGVRISE = 1
ROW_NAME_ENT_PGVRISE=3
ROW_PHASE_ENT_PGVRISE =4
ROW_CONDUCTOR_ENT_PGVRISE=6
ROW_SIZE_ENT_PGVRISE=7
ROW_IMAX_ENT_PGVRISE=5
ROW_CCC_ENT_PGVRISE=9
ROW_LENGHT_ENT_PGVRISE=8
ROW_AM_ENT_PGVRISE=10
ROW_VDROP_ENT_PGVRISE=11
ROW_TOTAL_PRC_ENT_PGVRISE=12
ROW_CALC_BUTT_PGVRISE=13
ROW_NOTES_ENT_PGVRISE=14



###############################################################################
                        #PAGE LAYOUT TECHNICAL POSITION#
###############################################################################

#Common to all layout pages
Y_POS_CANV_TITLE_PGLAYOUT = 10 # position from top of canvas

#Specific to the string layout page
HEIGHT_CANVAS_LAYOUT_STRING_PGLAYOUT = 600
WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT= 700
HEIGHT_STRING_MPPTA_STRING_PGLAYOUT = 130
HEIGHT_STRING_MPPTB_STRING_PGLAYOUT = 210
HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT = 340
SPACING_MPPTS_STRING_PGLAYOUT = 40

#Specific to the solaredge layout page
WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT = 610
HEIGHT_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT = 600
HEIGHT_STRING_SOLAREDGE_PGLAYOUT = 150



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
