import pyfiglet
from termcolor import colored
CRED = '\033[91m'
CEND = '\033[0m'
import requests,base64,json
url = "https://www.hackthebox.eu/api/invite/generate"
print(CRED+pyfiglet.figlet_format('HTB Invite Code Generator')+CEND)
num = int(input('Enter the number of invite codes: '))
invites=[]
for i in range(0,num):
        head = {'User-Agent': ''}
        out = requests.post(url,headers=head)
        info = json.loads(out.text)
        result = info['data']['code']
        decodedBytes =(base64.b64decode(result))
        decodedStr = str(decodedBytes, "utf-8")
        invites.append(decodedStr)
count=1
for i in invites:
        print(f'[-]Invite code {count}:',i)
        count+=1
