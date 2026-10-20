import pandas as pd
import re
from datetime import datetime

dLenght = 63
hederLenght = 5
dLenghtR = dLenght-hederLenght
weekLenght = 5
dWidth = 6

today = datetime.now().strftime('%d.%m.%Y')
todayDay = datetime.now().isoweekday()

weekDays = {
    1: "PONIEDZIAŁEK",
    2: "WTOREK",
    3: "ŚRODA",
    4: "CZWARTEK",
    5: "PIĄTEK",
    6: "SOBOTA",
    7: "NIEDZIELA"
}

today = f'{weekDays[todayDay]} {today}'

df = pd.read_excel('plan.xlsx', header=None)
for l in range(16): # LINE
    for d in range(weekLenght): # DAY
        day = df.iat[4+(l*dLenght), 2+(d*dWidth)]
        if day == today and todayDay <= 5:
            print(day+'\n\n')
            for j in range(dLenghtR): #ROW
                for i in range(2): #COLUMN
                    val = df.iat[(9+j+(l*dLenght)), (2+i+(d*dWidth))]
                    if pd.notna(val):
                        val = [el.strip() for el in re.split(r'\s{2,}', str(val))]
                        val = ' '.join(val)
                        print(val+'\n')
