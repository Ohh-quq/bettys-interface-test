import re
import test_swagger_manage


get_list = []
post_list = []
multi_list = []
list_all = test_swagger_manage.re_File()     # 获取正则分割后的list


def allocate_list():   # 将get/post和多种请求方式的接口分别存入不同的列表
    for i in range(0, len(list_all)):
        result_get = ("\"get\"" in list_all[i]) & ("\"post\"" not in list_all[i])
        result_post = ("\"post\"" in list_all[i]) & ("\"get\"" not in list_all[i])
        if result_get:
        #print(list[i])
            get_list.append(format(list_all[i]))           # 存get接口
        elif result_post:
            post_list.append(format(list_all[i]))           # 存post接口
        else:
            multi_list.append(format(list_all[i]))          # 存多种请求方式的接口


def getpath(components):
    pattern = re.compile('/.*?(?=\")')
    #self.path = pattern.search(get_list[1])
    path = pattern.findall(components)
    print(path[0])


allocate_list()
getpath(get_list[1])






