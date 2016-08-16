"""
    By: Derek Santos
    Only on Mac/Linux 
"""
import subprocess
import time

Access_Token = "Access-Token: Something"

#defining functions
def Automated(substring):
    Pushing_Out = ""
    Message = ""

    print (substring)#Error Checking...

    if substring == "This should work!":
        Message = "Now This Works!"

    elif substring == "Cat":
        Message = "Sorry No Cat!"

    elif substring == "Thank you!":
        Message = "You're Welcome!"

    elif substring == "humble bundle":
        Message = "Sorry No Bundle!"

    if Message != "":
        Pushing_Out = "curl --header \'" + Access_Token + "\' --header 'Content-Type: application/json' --data-binary '{\"body\":\"" + Message + "\",\"title\":\"Raspberrypi\",\"type\":\"note\"}' --request POST https://api.pushbullet.com/v2/pushes"
        subprocess.call(Pushing_Out,shell=True)



#main



while(True):

    time.sleep(5)

    #getting Pushes
    file = open("pushes.json","w")

    Grabbing_Pushes = ["curl","--header", Access_Token,"--data", "active=true", "--data", "limit=1","--get", "https://api.pushbullet.com/v2/pushes"]

    subprocess.call(Grabbing_Pushes, stdout= file)
    subprocess.call(["cat pushes.json | python3 -m json.tool > new"], shell=True)
    subprocess.call(["mv new pushes.json"], shell=True)

    file.close()

    #using Pushes
    with open("pushes.json","r") as file_read:
        for line in file_read:

            start = line.find("body")
            while(start != -1):
                substring = line[21:]
                size = len(substring) - 3
                substring = substring[:size]
                substring = substring.replace("\\n","\n" )
                Automated(substring)
                start = -1
