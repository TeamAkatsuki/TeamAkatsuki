class Dict_mod:
    def __init__(self,ip_str):
        self.ip_str = ip_str
    def sale_dict(ip_str):
        ip_list = ip_str.split(",")
        all_dic = {}
        for i in range(len(ip_list)):
            if i % 2 == 0:
                if not ip_list[i] in all_dic:
                    all_dic[ip_list[i]] = int(ip_list[i + 1])
                else:
                    all_dic[ip_list[i]] += int(ip_list[i + 1])
        return all_dic
