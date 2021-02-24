import sys
import databases.constants as constants
import os

def get_txtfile_info(job_number,job_dict):#gets information from the quote file

    prefixed = [filename for filename in os.listdir(constants.GDRIVE) if filename.startswith(str(job_number))]
    file_name=str(prefixed[0])
    txt_file = open(constants.GDRIVE+"/"+file_name+"/1. Quote/quote.txt", "r")
    txt_string=txt_file.read()

    #find the job number
    job_number=txt_string.find("Job:")#finds the position in bytes from beginning of text file
    end_of_line = txt_string.find("\n",job_number)
    txt_file.seek(job_number+5) #seek points the text file reader to postion, 5 is the lenght of string "Job: "
    job_dict["jobInfo"]["jobNumber"] = txt_file.read(end_of_line-job_number-5)

    #find the site name
    site_name=txt_string.find("Site:")#finds the position in bytes from beginning of text file
    end_of_line1 = txt_string.find("\n",site_name)
    end_of_line2 = txt_string.find("\n",end_of_line1)
    txt_file.seek(site_name+6) #seek points the text file reader to postion,6 is the lenght of string "Site: "
    part1= txt_file.read(end_of_line1-site_name-6)
    part2= txt_file.read(end_of_line2-end_of_line1)
    if part2 != "":
        complete_address = part1 + ", " + part2
    else:
        complete_address = part1
    job_dict["jobInfo"]["siteName"]=complete_address


    #find the client name
    client_name=txt_string.find("Client:")#finds the position in bytes from beginning of text file
    end_of_line = txt_string.find("\n",client_name)
    txt_file.seek(client_name+8) #seek points the text file reader to postion,9 is the lenght of string "Client: "
    #job_dict["jobInfo"]["clientName"]=txt_file.read(end_of_line-client_name-7)

    #find the panels used
    panel_name=txt_string.find("LG")#finds the position in bytes from beginning of text file
    end_of_previous_line = txt_string.find("\n",panel_name-6)
    txt_file.seek(end_of_previous_line+1) #seek points the text file reader to postion
    job_dict["jobComponents"]["panelNumber"]= txt_file.read(2)#panel number will be 1 or 2 digits
    lg_place = txt_string.find("LG",end_of_previous_line)
    try:
        txt_file.seek(lg_place)
        panel_name = txt_file.read(6)
    except:
        panel_name=""
    if panel_name == "LG370S":
        panel_name = "LG370M"#the way it is references in the panel_dict
    elif panel_name == "LG365S":
        panel_name = "LG365M"#the way it is references in the panel_dict
    job_dict["jobComponents"]["panelModel"]= panel_name#can improve
    job_dict["jobComponents"]["panelManufacturer"] = "LG Electronics"

    txt_file.close()
