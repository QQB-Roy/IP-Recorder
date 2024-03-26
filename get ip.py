import time,requests

while True:
   
    t=time.strftime("%D    %H:%M:%S")
    html = "http://127.0.0.1"
    myip = "http://myip.ipip.net/"
    htmlr=requests.get(html)
    myipr=requests.get(myip)
    web=htmlr.text
    ip=myipr.text


    print(t)
    print(ip)
    #print(web)
    time.sleep(1)


    f = open('ip.ini','a')
    f.write(t + ip + '\n')
        
