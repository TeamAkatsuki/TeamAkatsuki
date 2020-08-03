import os

report_data = []

def dir_list(pram_string):
    with os.scandir(param_string) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            t_list = transform_data("{0}\\{1}".format(param_string, file_name))