def get_pdf_info(txt_string,job_dict):#gets information from the quote file

    #find the client name
    client_name=txt_string.find("Contact:")#finds the position in bytes from beginning of text file
    end_of_line_name = txt_string.find("\n",client_name)
    job_dict["jobInfo"]["clientName"]=txt_string[client_name+9:end_of_line_name]
    #find the address
    site_name=txt_string.find("Address:")#finds the position in bytes from beginning of text file
    end_of_line_address = txt_string.find("\n",site_name)
    job_dict["jobInfo"]["siteName"]=txt_string[site_name+9:end_of_line_address]

    #finding all other job info
    system_summary=txt_string.find("System summary:")#finds the position in bytes from beginning of text file
    end_of_line1 = txt_string.find("\n",system_summary)
    system_part_1 = txt_string[system_summary+16:end_of_line1]
    #finding panel number
    end_panel_number=system_part_1.find("x")
    job_dict["jobComponents"]["panelNumber"]=system_part_1[0:end_panel_number]

    #after_panel_number= system_part_1[end_panel_number:end_of_line1]
    #find the panels used
    #after_panel_name=txt_string.find(" Watt")#finds the position in bytes from beginning of text file
    #job_dict["jobInfo"]["siteName"]=system_part_1[0:end_panel_number]
    #after_panel_number= system_part_1[end_panel_number:end_of_line1]
    # end_of_previous_line = txt_string.find("\n",panel_name-6)
    # txt_file.seek(end_of_previous_line+1) #seek points the text file reader to postion
    # job_dict["jobComponents"]["panelNumber"]= txt_file.read(2)#panel number will be 1 or 2 digits
    # lg_place = txt_string.find("LG",end_of_previous_line)
    # try:
    #     txt_file.seek(lg_place)
    #     panel_name = txt_file.read(6)
    # except:
    #     panel_name=""
    #
    # job_dict["jobComponents"]["panelModel"]= panel_name#can improve
    # job_dict["jobComponents"]["panelManufacturer"] = "LG Electronics"
