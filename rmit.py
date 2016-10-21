import browsercookie
import requests
import time
import json

ts = int(time.time() * 1000)
ts_str = str(ts)
cookie_str = ""

url = "https://my.rmit.edu.au/service/myexamtimetable?time="+ts_str

fake_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Host":"my.rmit.edu.au",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Referer": "https://my.rmit.edu.au/portal/myExam-timetable/",
}

cj = browsercookie.chrome()


for cookies in cj:
    if "rmit.edu.au" in cookies.domain:
        cookie_str += str(cookies.name + "=" + cookies.value + "; ")
        #print("Added fake cookie:  " + cookies.name + "=" + cookies.value + "; ")

cookie_str = cookie_str[:-2] # remove the last two "; " symbols

fake_header["Cookie"] = cookie_str

r = requests.get(url, headers=fake_header)

#print(str(r.content))

jsondata = json.loads(str(r.text))

print("Your ID:" + jsondata["userId"] + "\n\n")

for timetable in jsondata["timetable"]:
    print("Campus code:" + timetable["campusCode"])
    print("Course code:" + timetable["courseCode"])
    print("Course title: " + timetable["courseTitle"])
    print("Desk number: " + timetable["deskNumber"])
    print("Duration: " + timetable["duration"])
    print("Exam date:" + timetable["examDate"])
    print("\n\n")