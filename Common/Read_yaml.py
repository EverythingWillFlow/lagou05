import yaml,os
class Common():
    def get_datas(self,path:str)-> list:
        # 打开文件
        current_path = os.getcwd().split("lagou05")[0]
        #print(current_path)
        with open(current_path+"\\lagou05"+path) as f:
            datas = yaml.safe_load(f)
            #print(datas)
            # 获取文件中key为datas的数据
            add_datas = datas["datas"]
            # 获取文件中key为myids的数据
            add_ids = datas["myids"]
            #print(add_ids,add_datas)
            f.close()
            return [add_datas,add_ids]
