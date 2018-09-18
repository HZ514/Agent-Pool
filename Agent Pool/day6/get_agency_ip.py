import requests
import json
import random


url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=1a79df9043914308bd4e3168ca5f1376&count=10&expiryDate=0&format=1&newLine=2'

def get_ip():
    # 获取网页内容
    data_str = requests.get(url).text
    # print(type(data_str))
    # 获取的内容时json数据，将其转换成python数据类型
    data_dict = json.loads(data_str)
    # 获取其中一个ip字典
    data_ong_dict = random.choice(data_dict['msg'])
    # 获取ip
    # print(data_ong_dict['port'])
    # print(data_ong_dict['ip'])
    ip_str = ':'.join((data_ong_dict['ip'], data_ong_dict['port']))
    # print(ip_str)
    return ip_str





def main():
    get_ip()


if __name__ == '__main__':
    main()