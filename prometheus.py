import requests
import sys
from colorama import Fore,Style,init
init(autoreset=True)

logo = """
   )
  ((\  
  ===        ___ ___                     __  __              
 /_|_\     ---- / _ \_______  __ _  ___ / /_/ /  ___ __ _____
   |     ----- / ___/ __/ _ \/  ' \/ -_) __/ _ \/ -_) // (_-<
  \|/  _______/_/  /_/  \___/_/_/_/\__/\__/_//_/\__/\_,_/___/.co
"""

def initialize():
  print(Fore.LIGHTRED_EX+logo,end='')
  print(Style.DIM+"\n ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n",
      Style.DIM+"● ",
      Style.BRIGHT+"create by mehranSP @ Mon Jul 1 2019\n",
      Style.DIM+"● ",
      Style.BRIGHT+"Email :",
      Style.DIM+"mehran.safaripour@gmail.com\n",
      Style.DIM+"● ",
      Style.BRIGHT+"Github :",
      Style.DIM+"mygithub\n",
      Style.DIM+"● ",
      Style.BRIGHT+"Desceription :",
      Style.DIM+"prometheus is an micro sequeity framework\n",
      Style.DIM+"● ",
      Style.DIM+"to scan ports and search vulnerability.\n",
      Style.DIM+"●\n",
      Fore.RED+"● ",
      Style.NORMAL+Fore.LIGHTYELLOW_EX+"*NOTE:",
      Style.DIM+"for more help press",
      Style.NORMAL+"h\n",
      )


def whois_lookup(website):
  try:
    req = "https://api.hackertarget.com/whois/?q="+website
    res = requests.get(req)
    if res.text == "error check your api query":
      print(Fore.LIGHTYELLOW_EX+"* Warning:",Fore.WHITE+"try again ...")
    elif res.text == "error input invalid - enter IP or Hostname":
      print(Fore.LIGHTYELLOW_EX+"* Error!:",Fore.WHITE+"please insert valid IP or Hostname")
    elif res.status_code == 200:
      print(Fore.RED+">>> ",Fore.WHITE+website)
      print(res.text)
    else:
      print(Fore.LIGHTYELLOW_EX+"* Error!:",Fore.WHITE+"something wrong ...")
  except:
    print(Fore.LIGHTYELLOW_EX+"* Error!:",Fore.WHITE+"something wrong !!")


if __name__ == "__main__":
  initialize()
  while(True):
    curser = input(Fore.RED+"prometheus"+Fore.WHITE+"@"+Style.NORMAL+Fore.LIGHTGREEN_EX+"~"+Fore.WHITE+": ")
    if curser == "whois":
      website = input(Fore.RED+"prometheus"+Fore.WHITE+"@"+Style.NORMAL+Fore.LIGHTGREEN_EX+"whois"+Fore.WHITE+": ")
      whois_lookup(website)
    elif curser == "exit":
      sys.exit()
    else:
      print(Fore.LIGHTYELLOW_EX+"* Warning:",Fore.WHITE+"invalid input. press h for help.")