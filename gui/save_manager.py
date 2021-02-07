import json
import databases.constants as constants

def save_user_pref(user_preferences):

    with open(constants.DATABASE_LOC+'user_prefs.txt') as json_save_file:
        data = json.load(json_save_file)

    data=user_preferences

    with open(constants.DATABASE_LOC+'user_prefs.txt', 'w') as json_save_file:
        json.dump(data, json_save_file, indent=4)

def load_user_pref():

    with open(constants.DATABASE_LOC+'user_prefs.txt') as json_save_file:
        data = json.load(json_save_file)

    return data

def save_job(job_dict):

    job_exist = 0

    job_number = job_dict["jobInfo"]["jobNumber"]

    with open(constants.DATABASE_LOC+'job_saves.txt') as json_save_file:
        data = json.load(json_save_file)

    counter=-1
    for job in data:
        counter = counter +1
        for info in job:
            if job_number == info: # existing job so we modify data
                job_exist = 1
                data[counter][info] = job_dict

    if job_exist == 0: # New job so add it to the save_list
        data.append({job_number:job_dict})

    with open(constants.DATABASE_LOC+'job_saves.txt', 'w') as json_save_file:
        json.dump(data, json_save_file, indent=4)

def load_job(job_number):
    with open(constants.DATABASE_LOC+'job_saves.txt') as json_save_file:
        data = json.load(json_save_file)

    for job in data:
        for info in job:
            if job_number == info: # existing job so we return the saved dict
                job_dict = job[info]
    return job_dict
