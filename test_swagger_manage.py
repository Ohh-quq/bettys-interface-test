# enconding:utf-8
import json
import re
import pytest
import requests
import coo_setting
import test_swagger_manage
import csv


# 获取swagger文档

swagger_json = requests.get(coo_setting.swagger_url)

# 转utf-8
#print(swagger_json.content)
swagger_utf8 = swagger_json.content.decode().strip('\n')
# print(swagger_utf8)

# 将未经处理的swagger内容写入docx.txt
def WriteDoc(file_name):
    with open("docx.txt", "w", encoding='utf-8') as f:
        f.write(file_name)
        f.close()

# WriteDoc(swagger_utf8)

# WriteDoc_swagger = WriteDoc(swagger_utf8)
# 对docx.txt传入进行处理，并将处理后的内容写入re_file

def re_File():
    pattern = re.compile('"/.*?[:false]}},')
    with open("docx.txt","r",encoding='utf-8') as f:
        content = f.read()
        patterns = pattern.findall(content)
        print(patterns)

# 将正则匹配的内容写入到[]中
        '''for index in range(0,len(patterns)):
            with open(file="re_file.txt", mode='a',encoding='utf-8') as file:
                file.write(patterns[index])
                file.close'''





WriteDoc(swagger_utf8)
#re_File()

