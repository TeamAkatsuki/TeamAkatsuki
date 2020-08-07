import os

class fruitshop():

    def __init__(self):
        pass

    def start_fruitshop(self,start_str):
        self.first_list = []
        self.start_str = start_str
        self.split_list = self.start_str.split(",")
        for a in range(int(len(self.split_list)/2)):
            self.first_list.append([self.split_list[a*2],int(self.split_list[a*2+1])])

        self.first_list = fruitshop.joongbok_fruitshop(self,self.first_list)
        return self.first_list

    def joongbok_fruitshop(self,target_list):
        self.target_list = target_list
        self.empty_list = []
        for a in range(len(self.target_list)):
            dupl_check = False
            for b in range(len(self.empty_list)):
                if self.target_list[a][0] == self.empty_list[b][0]:
                    dupl_check = True
                    break
            if dupl_check == True:
                self.empty_list[b][1] += self.target_list[a][1]
            else:
                self.empty_list.append(self.target_list[a])

        return self.empty_list

class loaddata():

    def fileload(self):
        name_list =[]
        with os.scandir("savefile") as load_list:
            for load_filename in load_list:
                name_list.append(load_filename.name)

        return name_list
    def dataload(self,select , filelist):
        self.select = int(select)
        self.filelist = filelist
        with open("savefile\\%s"%self.filelist[self.select-1], "r") as f:
            self.read_data = f.read()
        return self.read_data

    def save(self, savefile , savefile_name):
        self.final_save = []
        for b in range(len(savefile)):
            self.final_save.append(savefile[b][0])
            self.final_save.append(str(savefile[b][1]))
        self.join_str = ",".join(self.final_save)
        with open("savefile\\%s.txt"%savefile_name, "w") as f:
            f.write(self.join_str)

        pass
data = loaddata()
fruitshop_data = fruitshop()

while True:
    filelist = data.fileload()
    t =1
    for a in filelist:
        print("{0}. {1}".format(t,a))
        t += 1
    select = input(
"""불러올 파일을 선택해주세요 :"""
    )
    if select == "q":
        print("종료합니다")
        break
    save_str = data.dataload(select,filelist)
    final_list = fruitshop_data.start_fruitshop(save_str)

    print(final_list)
    select = input(
'''1. 저장하기
2. 나가기'''
    )
    if select == "1":
        savefile_name = input(
"""저장할 파일의 이름을 입력하세요"""
        )
        data.save(final_list,savefile_name)
        print("저장성공")
        continue
    elif select == "2":
        continue





