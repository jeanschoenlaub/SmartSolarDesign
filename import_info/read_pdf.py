def get_pdf_info(txt_string,job_dict,panel_dict,inv_dict):#gets information from the quote file

    #find the client name
    client_name=txt_string.find("Contact:")#finds the position in bytes from beginning of text file
    end_of_line_name = txt_string.find("\n",client_name)
    job_dict["jobInfo"]["clientName"]=txt_string[client_name+9:end_of_line_name]
    #find the address
    site_name=txt_string.find("Address:")#finds the position in bytes from beginning of text file
    end_of_line_address = txt_string.find("\n",site_name)
    job_dict["jobInfo"]["siteName"]=txt_string[site_name+9:end_of_line_address]

    #finding all other job info
    system_summary =  txt_string.find("System summary:")#finds the position in bytes from beginning of text file
    end_of_line1 = txt_string.find("\n",system_summary)
    end_of_line2 = txt_string.find("\n",end_of_line1+1)
    system_summary_string = txt_string[system_summary+16:end_of_line2]

    #finding panel number
    end_panel_number= system_summary_string.find("x")
    job_dict["jobComponents"]["panelNumber"]=system_summary_string[0:end_panel_number]
    #find the panels used
    end_panel_name= system_summary_string.find(" ",end_panel_number+2)#finds the position in bytes from beginning of text file
    pdf_panel_model = system_summary_string[end_panel_number+2:end_panel_name]
    for panel_manu_keys in panel_dict.keys():
        for panel_model_keys in panel_dict[panel_manu_keys].keys():
            for panel_model_watt_keys in panel_dict[panel_manu_keys][panel_model_keys].keys():
                if pdf_panel_model == panel_dict[panel_manu_keys][panel_model_keys][panel_model_watt_keys]["panelSerial"]:
                    job_dict["jobComponents"]["panelManufacturer"]= panel_manu_keys
                    job_dict["jobComponents"]["panelModel"]= panel_model_keys
                    job_dict["jobComponents"]["panelSerial"]= panel_model_watt_keys
    #Ffinding the inverter used
    end_panel_part=system_summary_string.find("x",end_panel_name)
    end_of_inverter_serial = system_summary_string.find(" ",end_panel_part+2)
    pdf_inv_model = system_summary_string[end_panel_part+2:end_of_inverter_serial]
    for inv_type_keys in inv_dict.keys():
        for inv_manu_keys in inv_dict[inv_type_keys].keys():
            for inv_model_keys in inv_dict[inv_type_keys][inv_manu_keys].keys():
                for inv_model_size_keys in inv_dict[inv_type_keys][inv_manu_keys][inv_model_keys].keys():
                    length_of_inv_model_in_dict = len(inv_dict[inv_type_keys][inv_manu_keys][inv_model_keys][inv_model_size_keys]["Model"])
                    adjusted_pdf_inv_model = pdf_inv_model[0:length_of_inv_model_in_dict]
                    if adjusted_pdf_inv_model == inv_dict[inv_type_keys][inv_manu_keys][inv_model_keys][inv_model_size_keys]["Model"]:
                        job_dict["jobComponents"]["invType"]= inv_type_keys
                        job_dict["jobComponents"]["invManufacturer"]= inv_manu_keys
                        job_dict["jobComponents"]["invModel"]= inv_model_keys
                        job_dict["jobComponents"]["invSerial"]= inv_model_size_keys


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
