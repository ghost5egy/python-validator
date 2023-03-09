import requests, os, sys, json
from hashlib import md5
from tkinter import messagebox

def validator():
    usermac = md5(getmachinemac().encode()).hexdigest()
    url = 'pastebin-url'
    req = requests.get(url)
    if usermac in req.text:
        return False
    ip = requests.get('https://api.ipify.org').text
    messagebox.showinfo(title=None, message="This is PC not allowed Contact Admin")
    if os.name == 'nt':
        pcname = os.getenv('COMPUTERNAME')
    else:
        pcname = os.uname()[1]
    senddiscord('discord-url', "Allow this pc :\n" + usermac + "\nIP : " + ip + "\nPC Name : " + pcname)
    return True

def senddiscord(webhookurl, msg):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        payload = {"content": msg}
        result = requests.post(webhookurl, headers=headers, data=json.dumps(payload))
        try:
                result.raise_for_status()
        except requests.exceptions.HTTPError as e:
                print(e)
        else:
                print("Discord: sent with code {}.".format(result.status_code))
def getmachinemac():
    osname = sys.platform.lower()
    if 'win' in osname:
        command = "wmic bios get serialnumber"
    return os.popen(command).read().replace("\n","").replace("    ","").replace(" ","").replace("SerialNumber","")

if __name__ == "__main__":
    if validator():
        exit()
