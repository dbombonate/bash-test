#!/usr/bin/python3
import os.path

os.chdir("/tmp")

comment = str()
ipString = list()

file = open("output_1.txt", "r")
content = file.readlines()
file.close()

output = open("output_2.txt", "w")

def has_ip(string):
  ip = string.split('.')
  return True if len(ip)>1 else False

for x in content:
  contentSplit = x.split(' ')
  contentSplit = list(filter(None, contentSplit))
  ip = has_ip(contentSplit[0])
  if ip is False:
    comment = x
  else:
    ipString.append(x)

for y in ipString:
  contentIp = y.split(' ')
  contentIp = list(filter(None, contentIp))
  dataIpHostname = "{ip:<18}{hostname:<15}".format(ip = contentIp[0], hostname = contentIp[1])
  contentIp = '   '.join(contentIp[2:])
  output.write(dataIpHostname + contentIp)

output.write(comment)

output.close()