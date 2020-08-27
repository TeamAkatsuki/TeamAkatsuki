from team_akatsuki.py01_fruitshop.fruitshop_class_kimgh_200805.dict_mod import Dict_mod
from team_akatsuki.py01_fruitshop.fruitshop_class_kimgh_200805.save_mod import Save_mod
import os


def sale_str(p_dir):
    all_str = ''
    with os.scandir(p_dir) as entries:
        for entry in entries:
            file_name = entry.name
            with open("{}\\{}".format(p_dir, file_name), 'r', encoding='utf8') as file:
                line1 = file.readline()
                line2 = file.readline() + ','
                all_str += line2
    return all_str[:-1]


sale = sale_str('sale_box')
sale_dict = Dict_mod.sale_dict(sale)
Save_mod.save_mod(sale_dict)