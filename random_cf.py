import requests
import random
from bs4 import BeautifulSoup

levels = []
name = []
round = []
level = 6
user_level = []
user_round = []
user_problem = []

def fill_level(lev):
    for i in range(len(name)):
        if int(levels[i]) == lev:
            user_level.append(lev)
            user_round.append(round[i])
            user_problem.append(name[i])
    return len(user_level)

result = requests.get("https://a2oj.com/signin?url=%2F")
pars = { "url": "/",
"Username": "",
"Password": ""
 }

with requests.Session() as s:
    url = "https://a2oj.com/signincode"
    s.post(url,pars)
    t = s.get("https://a2oj.com/category?ID=410")
    src = BeautifulSoup(t.content)
    for trs in src.find_all('tr'):
        buffer=[]
        index=-1
        for tc in trs.find_all('td'):
            # print tc.text
            buffer.append(tc.text)
            index+=1
            if buffer[index] == "No":
                levels.append(buffer[index-1])
                name.append(buffer[index-6])
                round.append(buffer[index-2])
n = len(name)
#list size 3 times the expected length
for i in range(2*n/3):
    name.pop()
    levels.pop()
    round.pop()
#fill arrays with the given level of difficulty
while fill_level(level) == 0:
    level+=1
k = len(user_level)
rand_prob_num = random.randint(0,k) #generate random problem number for the given level
print user_problem[rand_prob_num]
print user_round[rand_prob_num]
