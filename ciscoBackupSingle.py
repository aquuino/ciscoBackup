###############################################################################################################
# Language     :  PowerShell 6.1
# Filename     :  ciscoBackupSingle.ps1
# Author       :  matthew-git-hub (https://github.com/Matthew-git-hub)
# Description  :  Backs up a single Cisco Device
# Repository   :  https://github.com/Matthew-git-hub/ciscoBackup
###############################################################################################################

import sys
import time
import paramiko
import os
import cmd
import datetime

#Set Date

timestr = time.strftime("%Y%m%d")

#Authentication Variables

host = 'SANITIZED'
user = 'SANITIZED'
loginPass = 'SANITIZED'
port = "22"
#enable = "cisco"

#session start
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=loginPass)

#ssh shell
channel = client.invoke_shell()
time.sleep(2)

#enter enable secret
#chan.send('en\n')
#chan.send(secret +'\n')
#time.sleep(1)

#terminal lenght for no paging 
channel.send('term len 0\n')
time.sleep(1)

#Show config and write output
channel.send('sh run\n')
time.sleep(30)
output = channel.recv(999999)

#Show Running Config and Print to a file
print (config)
filename = str(host) + "-" + str(timestr) + "_.txt"
file = open(filename, 'a')
file.write(config)
f.close

#Close SSH 
print "Closing SSH session with: " + (host)
client.close