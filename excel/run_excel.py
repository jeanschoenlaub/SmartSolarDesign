import tkinter as tk
from tkinter import messagebox
import xlwings as xw
import shutil
import os

import databases.constants as constants

from gui.save_manager import load_user_pref
#jean = 1
#luke = 2

#if os.path.isdir("/Users/hcbsolar-operations/"):
#    computer=luke
#    print("On Luke's Computer")
#    template_dir = "/Users/hcbsolar-operations/Developer/sld-project/ExcelTemplates/{}.xlsm"
#    vrise_print_loc = "/Users/hcbsolar-operations/Developer/sld-project/ExcelTemplates/Design VRC.pdf"
#    sld_print_loc = "/Users/hcbsolar-operations/Developer/sld-project/Design SLD.pdf"

#if os.path.isdir("/Users/jean/"):
#    computer=jean
#    print("On Jean's Computer")
#    template_dir = constants.EXCEL_LOC+"/{}.xlsm"
#    vrise_print_loc = constants.EXCEL_LOC+"/Design VRC.pdf"
#    sld_print_loc = constants.EXCEL_LOC+"/Design SLD.pdf"


template_dir = constants.EXCEL_LOC+"/{}.xlsm"
vrise_print_loc = constants.EXCEL_LOC+"/Design VRC.pdf"
sld_print_loc = constants.EXCEL_LOC+"/Design SLD.pdf"

template_string_inverter = template_dir.format("string_inverter")
template_sonnen = template_dir.format("sonnen_batt")
template_enphase = template_dir.format("enphase")
template_tesla = template_dir.format("Tesla")

duplicate_name = template_dir.format("DesignTemplate")

user_prefs = load_user_pref()


def print_string_inverter(job_dict,panel_dict,inv_dict):
    shutil.copy(template_string_inverter, duplicate_name)

    xl_app = xw.App(visible=False,add_book=False)
    wbSld = xl_app.books.open(duplicate_name)
    wsParam = wbSld.sheets["Param"]
    #Client Information
    wsParam.range("B2").value = job_dict["jobInfo"]["jobNumber"]
    wsParam.range("B3").value = job_dict["jobInfo"]["clientName"]
    wsParam.range("B4").value = job_dict["jobInfo"]["siteName"]
    wsParam.range("B5").value = job_dict["jobInfo"]["numMsbPhases"]
    #Panel Information
    panel_model = job_dict["jobComponents"]["panelModel"]
    panel_manufacturer = job_dict["jobComponents"]["panelManufacturer"]
    wsParam.range("B11").value = panel_model
    wsParam.range("B12").value = panel_dict[panel_manufacturer][panel_model]["model"]
    wsParam.range("B13").value = job_dict["jobComponents"]["panelNumber"]
    wsParam.range("B14").value = panel_dict[panel_manufacturer][panel_model]["P"]
    wsParam.range("B15").value = panel_dict[panel_manufacturer][panel_model]["Voc"]
    wsParam.range("B16").value = panel_dict[panel_manufacturer][panel_model]["Isc"]
    #Inverter Information
    inv_type = job_dict["jobComponents"]["invType"]
    invmanufacturer= job_dict["jobComponents"]["invManufacturer"]
    invmodel= job_dict["jobComponents"]["invModel"]
    wsParam.range("B19").value = inv_dict[inv_type][invmanufacturer][invmodel]["Manufacturer"]
    wsParam.range("B20").value = inv_dict[inv_type][invmanufacturer][invmodel]["Model"]#full model name
    wsParam.range("B21").value = inv_dict[inv_type][invmanufacturer][invmodel]["Phases"]
    wsParam.range("B22").value = inv_dict[inv_type][invmanufacturer][invmodel]["IOutMax"]
    wsParam.range("B23").value = inv_dict[inv_type][invmanufacturer][invmodel]["P"]
    wsParam.range("B24").value = job_dict["jobSetup"]["mpptA1"]
    wsParam.range("B25").value = job_dict["jobSetup"]["mpptA2"]
    wsParam.range("B26").value = job_dict["jobSetup"]["mpptB1"]
    wsParam.range("B27").value = job_dict["jobSetup"]["mpptB2"]
    wsParam.range("B28").value = job_dict["jobExtra"]["monitoring"]
    #Vrise information
    wsParam.range("B30").value = job_dict["jobVrise"]["lenService"]
    wsParam.range("B31").value = job_dict["jobVrise"]["lenConsumer"]
    wsParam.range("B32").value = job_dict["jobVrise"]["lenMsb"]
    wsParam.range("B33").value = job_dict["jobVrise"]["cableSize"]
    wsParam.range("B34").value = job_dict["jobVrise"]["notes"]
    wsParam.range("B35").value = job_dict["jobVrise"]["col1Name"]
    wsParam.range("B36").value = job_dict["jobVrise"]["col2Name"]
    wsParam.range("B37").value = job_dict["jobVrise"]["col3Name"]
    #Extra Information
    wsParam.range("B39").value = job_dict["jobExtra"]["existingArray"]
    wsParam.range("B40").value = job_dict["jobExtra"]["notes"]

    #Optional writes
    if "blockDiagram" in job_dict:
        wsParam.range("D2").value = 1
        wsParam.range("D3").value =job_dict["blockDiagram"]["block1"]
        wsParam.range("D4").value =job_dict["blockDiagram"]["line1up"]
        wsParam.range("D5").value =job_dict["blockDiagram"]["line1down"]
        wsParam.range("D6").value =job_dict["blockDiagram"]["block2"]
        wsParam.range("D7").value =job_dict["blockDiagram"]["line2up"]
        wsParam.range("D8").value =job_dict["blockDiagram"]["line2down"]
        wsParam.range("D9").value =job_dict["blockDiagram"]["block3"]
        wsParam.range("D10").value =job_dict["blockDiagram"]["note"]


    #Run Macro Setup
    if job_dict["jobSetup"]["mpptB1"] != "":
        run_macro_setup = wbSld.app.macro('Setup.Setup2Mppt')
    else:
        run_macro_setup = wbSld.app.macro('Setup.Setup1Mppt')
    run_macro_setup()

    #Run Macro Print (output in FishPython/ExcelTemplates)
    if job_dict["jobSetup"]["mpptB1"] != "":
        run_macro_print = wbSld.app.macro('printer.Print2Mppt')
    else:
        run_macro_print = wbSld.app.macro('printer.Print1Mppt')

    run_macro_print(vrise_print_loc,sld_print_loc)

    wbSld.save()
    wbSld.close()
    xl_app.kill()

    original = constants.EXCEL_LOC+"/DesignTemplate.xlsm"
    target = user_prefs["Paths"]["outputSld"]+"/DesignTemplate.xlsm"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design VRC.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design VRC.pdf"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design SLD.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design SLD.pdf"
    shutil.move(original,target)


def print_hybrid_inverter(job_dict,panel_dict,inv_dict):
    shutil.copy(template_sonnen, duplicate_name)
    xl_app = xw.App(add_book=False,visible=False)
    wbSld = xl_app.books.open(duplicate_name)
    run_macro_hide = wbSld.app.macro('Hide.Hide')
    run_macro_hide()

    wsParam = wbSld.sheets["Param"]

    #Client Information
    wsParam.range("B2").value = job_dict["jobInfo"]["jobNumber"]
    wsParam.range("B3").value = job_dict["jobInfo"]["clientName"]
    wsParam.range("B4").value = job_dict["jobInfo"]["siteName"]
    wsParam.range("B5").value = job_dict["jobInfo"]["numMsbPhases"]
    #Panel Information
    panel_model = job_dict["jobComponents"]["panelModel"]
    panel_manufacturer = job_dict["jobComponents"]["panelManufacturer"]
    wsParam.range("B11").value = panel_model
    wsParam.range("B12").value = panel_dict[panel_manufacturer][panel_model]["model"]
    wsParam.range("B13").value = job_dict["jobComponents"]["panelNumber"]
    wsParam.range("B14").value = panel_dict[panel_manufacturer][panel_model]["P"]
    wsParam.range("B15").value = panel_dict[panel_manufacturer][panel_model]["Voc"]
    wsParam.range("B16").value = panel_dict[panel_manufacturer][panel_model]["Isc"]
    #Inverter Information
    inv_type = job_dict["jobComponents"]["invType"]
    invmanufacturer= job_dict["jobComponents"]["invManufacturer"]
    invmodel= job_dict["jobComponents"]["invModel"]
    wsParam.range("B19").value = inv_dict[inv_type][invmanufacturer][invmodel]["Manufacturer"]
    wsParam.range("B20").value = inv_dict[inv_type][invmanufacturer][invmodel]["Model"]#full model name
    wsParam.range("B21").value = inv_dict[inv_type][invmanufacturer][invmodel]["Phases"]
    wsParam.range("B22").value = inv_dict[inv_type][invmanufacturer][invmodel]["IOutMax"]
    wsParam.range("B23").value = inv_dict[inv_type][invmanufacturer][invmodel]["P"]
    wsParam.range("B24").value = inv_dict[inv_type][invmanufacturer][invmodel]["RatedOutputPower"]
    wsParam.range("B25").value = inv_dict[inv_type][invmanufacturer][invmodel]["NominalCapacity"]
    wsParam.range("B26").value = inv_dict[inv_type][invmanufacturer][invmodel]["IscBatt"]
    wsParam.range("B27").value = inv_dict[inv_type][invmanufacturer][invmodel]["VocBatt"]
    wsParam.range("B28").value = job_dict["jobSetup"]["mpptA1"]
    wsParam.range("B29").value = job_dict["jobSetup"]["mpptB1"]
    wsParam.range("B30").value = job_dict["jobExtra"]["monitoring"]
    wsParam.range("B31").value = job_dict["jobExtra"]["backup"]
    #Vrise information
    wsParam.range("B34").value = job_dict["jobVrise"]["lenService"]
    wsParam.range("B35").value = job_dict["jobVrise"]["lenConsumer"]
    wsParam.range("B36").value = job_dict["jobVrise"]["lenMsb"]
    wsParam.range("B37").value = job_dict["jobVrise"]["cableSize"]
    wsParam.range("B38").value = job_dict["jobVrise"]["notes"]
    #Extra Information
    wsParam.range("B44").value = job_dict["jobExtra"]["existingArray"]
    wsParam.range("B45").value = job_dict["jobExtra"]["notes"]


    run_macro_setup = wbSld.app.macro('Setup.Setup')
    run_macro_setup()

    run_macro_print = wbSld.app.macro('printer.Printer')
    run_macro_print(vrise_print_loc,sld_print_loc)

    wbSld.save()
    wbSld.close()
    xl_app.kill()

    original = constants.EXCEL_LOC+"/DesignTemplate.xlsm"
    target = user_prefs["Paths"]["outputSld"]+"/DesignTemplate.xlsm"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design VRC.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design VRC.pdf"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design SLD.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design SLD.pdf"
    shutil.move(original,target)


def print_enphase_inverter(job_dict,panel_dict,inv_dict):
    shutil.copy(template_enphase, duplicate_name)

    xl_app = xw.App(add_book=False,visible=False)
    wbSld = xl_app.books.open(duplicate_name)
    wsParam = wbSld.sheets["Param"]
    #Client Information
    wsParam.range("B2").value = job_dict["jobInfo"]["jobNumber"]
    wsParam.range("B3").value = job_dict["jobInfo"]["clientName"]
    wsParam.range("B4").value = job_dict["jobInfo"]["siteName"]
    wsParam.range("B5").value = job_dict["jobInfo"]["numMsbPhases"]
    #Panel Information
    panel_model = job_dict["jobComponents"]["panelModel"]
    panel_manufacturer = job_dict["jobComponents"]["panelManufacturer"]
    wsParam.range("B11").value = panel_model
    wsParam.range("B12").value = panel_dict[panel_manufacturer][panel_model]["model"]
    wsParam.range("B13").value = job_dict["jobComponents"]["panelNumber"]
    wsParam.range("B14").value = panel_dict[panel_manufacturer][panel_model]["P"]
    wsParam.range("B15").value = panel_dict[panel_manufacturer][panel_model]["Voc"]
    wsParam.range("B16").value = panel_dict[panel_manufacturer][panel_model]["Isc"]
    #Inverter Information
    inv_type = job_dict["jobComponents"]["invType"]
    invmanufacturer= job_dict["jobComponents"]["invManufacturer"]
    invmodel= job_dict["jobComponents"]["invModel"]
    wsParam.range("B19").value = inv_dict[inv_type][invmanufacturer][invmodel]["Manufacturer"]
    wsParam.range("B20").value = inv_dict[inv_type][invmanufacturer][invmodel]["Model"]#full model name
    wsParam.range("B21").value = inv_dict[inv_type][invmanufacturer][invmodel]["P"]
    wsParam.range("B22").value = job_dict["setupEnphase"]["string1L1"]
    wsParam.range("B23").value = job_dict["setupEnphase"]["string1L2"]
    wsParam.range("B24").value = job_dict["setupEnphase"]["string1L3"]
    wsParam.range("B25").value = job_dict["setupEnphase"]["string2L1"]
    wsParam.range("B26").value = job_dict["setupEnphase"]["string2L2"]
    wsParam.range("B27").value = job_dict["setupEnphase"]["string2L3"]
    wsParam.range("B28").value = job_dict["jobExtra"]["monitoring"]
    #Vrise Information
    wsParam.range("B31").value = job_dict["jobVrise"]["lenService"]
    wsParam.range("B32").value = job_dict["jobVrise"]["lenConsumer"]
    wsParam.range("B33").value = job_dict["jobVrise"]["lenMsb"]
    wsParam.range("B34").value = job_dict["jobVrise"]["cableSize"]
    wsParam.range("B35").value = job_dict["jobVrise"]["maxCurrent"]

    #Extra Information
    wsParam.range("B42").value = job_dict["jobExtra"]["existingArray"]
    wsParam.range("B43").value = job_dict["jobExtra"]["blockDiagram"]
    wsParam.range("B44").value = job_dict["jobExtra"]["notes"]
    wsParam.range("B36").value = job_dict["setupEnphase"]["micro_phases"]
    wsParam.range("B37").value = job_dict["jobVrise"]["notes"]

    run_macro_setup = wbSld.app.macro('Setup.Setup')
    run_macro_print = wbSld.app.macro('printer.Printer')

    try:
        run_macro_setup()
        run_macro_print(vrise_print_loc,sld_print_loc)
    except:
        error=tk.messagebox.showerror(title="Unexpected Error",message="Sorry, an unexpected error occured",icon="error")

    wbSld.save()
    wbSld.close()
    xl_app.kill()

    original = constants.EXCEL_LOC+"/DesignTemplate.xlsm"
    target = user_prefs["Paths"]["outputSld"]+"/DesignTemplate.xlsm"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design VRC.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design VRC.pdf"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design SLD.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design SLD.pdf"
    shutil.move(original,target)


def print_gateway(job_dict,panel_dict,inv_dict):
    shutil.copy(template_tesla, duplicate_name)

    xl_app = xw.App(add_book=False,visible=False)
    wbSld = xl_app.books.open(duplicate_name)
    wsParam = wbSld.sheets["Param"]
    #Client Information
    wsParam.range("B2").value = job_dict["jobInfo"]["jobNumber"]
    wsParam.range("B3").value = job_dict["jobInfo"]["clientName"]
    wsParam.range("B4").value = job_dict["jobInfo"]["siteName"]
    wsParam.range("B5").value = job_dict["jobInfo"]["numMsbPhases"]
    #Panel Information
    panel_model = job_dict["jobComponents"]["panelModel"]
    panel_manufacturer = job_dict["jobComponents"]["panelManufacturer"]
    wsParam.range("B11").value = panel_model
    wsParam.range("B12").value = panel_dict[panel_manufacturer][panel_model]["model"]
    wsParam.range("B13").value = job_dict["jobComponents"]["panelNumber"]
    wsParam.range("B14").value = panel_dict[panel_manufacturer][panel_model]["P"]
    wsParam.range("B15").value = panel_dict[panel_manufacturer][panel_model]["Voc"]
    wsParam.range("B16").value = panel_dict[panel_manufacturer][panel_model]["Isc"]
    #Inverter Information
    inv_type = job_dict["jobComponents"]["invType"]
    invmanufacturer= job_dict["jobComponents"]["invManufacturer"]
    invmodel= job_dict["jobComponents"]["invModel"]
    wsParam.range("B19").value = inv_dict[inv_type][invmanufacturer][invmodel]["Manufacturer"]
    wsParam.range("B20").value = inv_dict[inv_type][invmanufacturer][invmodel]["Model"]#full model name
    wsParam.range("B21").value = inv_dict[inv_type][invmanufacturer][invmodel]["P"]
    wsParam.range("B22").value = job_dict["setupEnphase"]["string1L1"]
    wsParam.range("B23").value = job_dict["setupEnphase"]["string1L2"]
    wsParam.range("B24").value = job_dict["setupEnphase"]["string1L3"]
    wsParam.range("B25").value = job_dict["jobExtra"]["monitoring"]
    #Vrise Information
    wsParam.range("B28").value = job_dict["jobVrise"]["lenService"]
    wsParam.range("B29").value = job_dict["jobVrise"]["lenConsumer"]
    wsParam.range("B30").value = job_dict["jobVrise"]["lenMsb"]
    wsParam.range("B31").value = job_dict["jobVrise"]["cableSize"]
    wsParam.range("B32").value = job_dict["jobVrise"]["maxCurrent"]
    wsParam.range("B33").value = job_dict["jobSetup"]["phases"]
    wsParam.range("B34").value = job_dict["jobVrise"]["notes"]

    #For the string inverters
    if job_dict["jobComponents"]["invType"] == "String":
        wsParam.range("E16").value = inv_dict[inv_type][invmanufacturer][invmodel]["Manufacturer"]
        wsParam.range("E17").value = inv_dict[inv_type][invmanufacturer][invmodel]["Model"]#full model name
        wsParam.range("E18").value = inv_dict[inv_type][invmanufacturer][invmodel]["Phases"]
        wsParam.range("E19").value = inv_dict[inv_type][invmanufacturer][invmodel]["IOutMax"]
        wsParam.range("E20").value = inv_dict[inv_type][invmanufacturer][invmodel]["P"]
        wsParam.range("E21").value = job_dict["jobSetup"]["mpptA1"]
        wsParam.range("E22").value = job_dict["jobSetup"]["mpptA2"]
        wsParam.range("E23").value = job_dict["jobSetup"]["mpptB1"]
        wsParam.range("E24").value = job_dict["jobSetup"]["mpptB2"]


    #Extra Information
    wsParam.range("B36").value = job_dict["jobExtra"]["existingArray"]
    wsParam.range("B37").value = job_dict["jobExtra"]["blockDiagram"]
    wsParam.range("B38").value = job_dict["jobExtra"]["notes"]

    if job_dict["jobComponents"]["invType"] == "Micro":
        run_macro_setup = wbSld.app.macro('Setup.Setup_ENP')
    elif job_dict["jobSetup"]["mpptB1"] == "":
        run_macro_setup = wbSld.app.macro('Setup.Setup_1Mppt')
    else:
        run_macro_setup = wbSld.app.macro('Setup.Setup_2Mppt')

    run_macro_setup()

    if job_dict["jobComponents"]["invType"] == "Micro":
        run_macro_print = wbSld.app.macro('printer.Printer_ENP')
    elif job_dict["jobSetup"]["mpptB1"] == "":
        run_macro_print = wbSld.app.macro('printer.Printer_1Mppt')
    else:
        run_macro_print = wbSld.app.macro('printer.Printer_2Mppt')
    run_macro_print(vrise_print_loc,sld_print_loc)

    wbSld.save()
    wbSld.close()
    xl_app.kill()

    original = constants.EXCEL_LOC+"/DesignTemplate.xlsm"
    target = user_prefs["Paths"]["outputSld"]+"/DesignTemplate.xlsm"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design VRC.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design VRC.pdf"
    shutil.move(original,target)
    original = constants.EXCEL_LOC+"/Design SLD.pdf"
    target = user_prefs["Paths"]["outputSld"]+"/Design SLD.pdf"
    shutil.move(original,target)
