#!/bin/python3
import os 
import sys
import socket
import time
from colorama import Fore, Style
import platform
import ipaddress 

type_platform = platform.system()
if  type_platform == "Linux":
   os.system("clear")
else:
   os.system('cls')
print("="*50)
print("Fastscan 1.1v")
print(f"Local Time is : {time.ctime()}".strip())
print("="*50)
try :
   var1 = sys.argv[1]
   var2 = sys.argv[2]
   
except :
   print("[+]You forget argemnt use " , Fore.RED+"-h -")
   exit(0)
def func_help(): # function all what it do just print help if someome need
   return Style.BRIGHT+"""
   -a   : Scan all port 65535
   -f   : Scan only famous port
   -p   : Chose  port manuly -p 5000
   -h - : See help
   -d - : See Descrption toole
   -D   : Descver hosts exomple fastscan -D 192.168.1.0/24
   exmple : fastscan -a 192.168.1.1  or fastscan -p 5000 192.168.1.1
   """

def func_description():# This function it calld wine someone ned descrption for tool  
   return Fore.RED+"""Fastscan is toole it can help you to scan port port if you noot have any toole in your computer .
i create this toole becouse some time wine i get the revers shell i didnt found toole like nmap 
inside thes victem box to see what auther ip found. 
"""

def func_conction(host , port): # This func to try conction and scaning port
   try:
      create_connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
         statues_resolte = create_connection.connect_ex((f"{host}",port))
         create_connection.settimeout(1)
         create_connection.close()
      except socket.gaierror:
         print(Fore.RED+"Error value")
         exit(0)
      return statues_resolte
   except KeyboardInterrupt:
      print("\nbye")
      exit(0)

def func_all_import(host , port):
   try:
      for value in range(0 , port):
         status_func =   func_conction(host , value) # her we see status  the connction if statu = 0 than connction seccess if equle any auther value then connction filed
         if  status_func == 0 :
            try:
               print(Fore.BLUE+"PORT OPEN :", Fore.GREEN+f"{value}" ,Fore.YELLOW+f"{socket.getservbyport(value)}")#{socket.getservbyport(value)}")
            except OSError:
               print(Fore.BLUE+"PORT OPEN : ", Fore.GREEN+f"{value}"  ,Fore.YELLOW+'Unkown Service')
         else:
            pass
   except NameError :
      print("Error Value ")


all_port = 65535
def scan_all_port(host , port):
   func_all_import(host , port)

def fast_scan(host):
   famous_port = [22,21,20,50,80,139,445,443,3306,53,67,69,110,119,123,135,139,143,161,389,989,3389]
   for value in famous_port:
      # func_conction(host , value)
      status_func =   func_conction(host , value) 

      if  status_func == 0 :
         print(Fore.BLUE+"PORT OPEN :", Fore.GREEN+f"{value}" ,Fore.YELLOW+f"{socket.getservbyport(value)}")
      else:
         pass
  
def chose_port_scan(host , port):
   func_all_import(host , port)

def descover_hosts_ip(ip_sabnet):
   try:
      if type_platform == "Linux":
         parameter = "-c"
      else:
         parameter = "-n"

      ip = ipaddress.ip_network(ip_sabnet)
      for i in ip:
         exit_code = os.system(f"ping {parameter} 1 -w2 {i} > /dev/null 2>&1")
         if exit_code == 0 :
            print(Fore.BLUE+"IP Found :" ,Fore.YELLOW+f"{i}")
         else:
            pass
   except ValueError :
      print("Error You forget add something ")
      exit(0)

def func_condtions():   
   if var1 == "-a" :
      print(scan_all_port(var2 , all_port))
   elif var1 == "-f":
      print(fast_scan(var2))
   elif var1 == "-d" :
      print(func_description())
   elif var1 == "-h" :
      print(func_help())
   elif var1 == "-p" :
      print(chose_port_scan(str(sys.argv[3]),  int(var2)))
   elif var1 == "-D" :
      print(descover_hosts_ip(var2))
   else:
      print("Sorry we don`t have this chose " ,Fore.RED+f"{var1}" )
func_condtions()