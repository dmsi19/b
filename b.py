import json, requests, time

while True:
    username = input ("[+] Enter User : ")
    print ("")
    r = requests.get(f"https://exolyt.com/api/users/{username}/basic").text

    resp = json.loads(r)
    print("[+] Possible Email : " + resp["nickName"] + "@gmail.com")


    
else:
    print ("Error")
