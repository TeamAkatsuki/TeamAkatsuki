class Save_mod:
    def __init__(self,ip_dic):
        self.ip_dic = ip_dic
    def save_mod(ip_dic):
        with open("sale_file.csv", 'w', encoding='utf8') as sale_file:
            for i in ip_dic:
                sale_file.write("{},{}\n".format(i, ip_dic[i]))