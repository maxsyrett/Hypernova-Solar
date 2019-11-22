import logging
from datetime import *

logging.basicConfig(filename='Hud.log', filemode='a+', format='%(asctime)s - %(message)s', datefmt='%b/%d/%y %H:%M:%S')


def log(speed, charge, temp1, temp2):
    logRow = 'Speed: ' + speed + ' Charge: ' + charge + ' Temp1: ' + temp1 + ' Temp2: ' + temp2 + ' '
    logging.error('%s', logRow)


def clearLine():
    with open('Hud.Log', 'r') as x:
        data = x.read().splitlines(True)
    with open('Hud.log', 'w') as z:
        z.writelines(data[1:])


def getHudInfo():
    info = []
    f = open('Hud.log', 'r')
    f1 = f.readlines()
    line = f1[-1].split(' ')
    info.append(line[4] + ' MPH')
    info.append(line[6] + '%')
    info.append(line[8] + u'\u00b0F')
    info.append(line[10] + u'\u00b0F')

    for dLine in f1:
        top = dLine.split('-')
        now = datetime.strptime(top[0], '%b/%d/%y %H:%M:%S ')
        if now < datetime.now() - timedelta(hours=1):
            clearLine()
        else:
            break
    return info


for i in range(2):
    log('60', '100', '90', '92')
