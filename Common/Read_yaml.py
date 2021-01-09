import yaml,os
class Common_funcs():
    def get_datas(self,path:str)-> list:
        # 打开文件
        current_path = os.getcwd().split("lagou05")[0]
        #print(current_path)
        with open(current_path+"\\lagou05"+path) as f:
            datas = yaml.safe_load(f)
            #print(datas)
            # 获取文件中key为datas的数据
            # data_all = datas["datas"]
            add_datas = datas["datas"]["add"]
            # 获取文件中key为myids的数据
            add_ids = datas["myids"]["add"]
            # 获取文件中key为datas的数据
            div_datas = datas["datas"]["div"]
            # 获取文件中key为myids的数据
            div_ids = datas["myids"]["div"]
            # 获取文件中key为datas的数据
            mul_datas = datas["datas"]["mul"]
            # 获取文件中key为myids的数据
            mul_ids = datas["myids"]["mul"]
            # 获取文件中key为datas的数据
            sub_datas = datas["datas"]["sub"]
            # 获取文件中key为myids的数据
            sub_ids = datas["myids"]["sub"]
            #print(add_ids,add_datas)
            #print(data_all)
            f.close()
            return [add_datas,add_ids,div_datas,div_ids,mul_datas,mul_ids,sub_datas,sub_ids]
