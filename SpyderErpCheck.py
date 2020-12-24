# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:18:10 2020

@author: laguna
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt


USEREMAIL = '****.*****'
PASSWORD = '*********'
LOGIN_URL = 'http://192.168.***.***/erp/login.php?login'
QUERY_STRING = ['&week_offset=-1','']

payload = {
    'name': USEREMAIL,
    'pwd': PASSWORD,
}

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


#登入
session_requests = requests.session()
result = session_requests.post(LOGIN_URL, data = payload)

#組人員日報陣列
engineers = []
engineers.append(('杜Ｏ文','http://192.168.123.211/erp/daily.php?id=32'))
engineers.append(('涂Ｏ維','http://192.168.123.211/erp/daily.php?id=72'))
engineers.append(('張Ｏ源','http://192.168.123.211/erp/daily.php?id=77'))
engineers.append(('戴Ｏ政','http://192.168.123.211/erp/daily.php?id=86'))
engineers.append(('陳Ｏ翔','http://192.168.123.211/erp/daily.php?id=100'))
engineers.append(('姚Ｏ霖','http://192.168.123.211/erp/daily.php?id=113'))
engineers.append(('翁Ｏ愷','http://192.168.123.211/erp/daily.php?id=126'))
engineers.append(('陳Ｏ澔','http://192.168.123.211/erp/daily.php?id=128'))
engineers.append(('林Ｏ廷','http://192.168.123.211/erp/daily.php?id=130'))

txts = []
today = dt.now()

for engineer in engineers:
    txts.append('<br/>' + engineer[0] + '-')
    noPassList = []
    for qs in QUERY_STRING:
        URL = engineer[1] + qs
        result = session_requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")
        trs = soup.find_all("tr",class_="text-center table table-active")
        for tr in trs:
            tds = tr.select("td")
            dateStrList = str(tds[0]).replace("<td>","").replace("</td>","").split("-")
            month = month_string_to_number(dateStrList[1])
            day = int(dateStrList[0])
            if month<=today.month and day<=today.day:                
                dayOfTheWeek = str(tds[1]).replace("<td>","").replace("</td>","")
                if dayOfTheWeek !='六' and dayOfTheWeek !='日':
                    noPassList.append(str(month) + "/" + str(day) + '(' + dayOfTheWeek + ')')
                    #txts.append('<br/>' + str(tds[0]).replace("<td>","").replace("</td>","") + ' ' + dayOfTheWeek + " 未填寫日報")
                    #Ok = False      
    if len(noPassList) == 0:
        txts.append("已正常填寫日報")
    else:
        txts.append("- " + str(len(noPassList)) + " 日未填寫日報，[")
        for i in range(len(noPassList)):
            if i > 0:
                txts.append(',' + noPassList[i])
            else :
                txts.append(noPassList[i])
        txts.append(']')
    
f = open('D:/ERP_CHECK.htm','w',encoding="utf-8")
f.write('\ufeff')#BOM
f.writelines(txts)
f.close()