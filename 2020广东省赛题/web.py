import urllib
num = 1
f = open("flag.txt","wb")
while num < 254:
    try:
        ip = str(num)
        print(ip)
        url="http://172.16."+ip+".250/flag.txt" 
        flag = urllib.urlopen(url).read()
        f.write("172.16."+ip+".10  :  ")
        f.write(flag)
        f.write("\n")
        print(flag)
        num = num + 1
    except:
        num =num + 1
f.close()