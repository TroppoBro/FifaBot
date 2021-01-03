import random
import time
import requests
import os

from webbot import Browser


def login(driver):
    # file = open('C:/Users/GAMER/Desktop/BotFifa1.0/cookies.txt', 'r')
    driver.go_to('https://accounts.ea.com/')
    time.sleep(2)  # chargement de la page
    driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1502230733.1607072051'})
    driver.add_cookie({'name': '_gat', 'value': '1'})
    driver.add_cookie({'name': '_gid', 'value': 'GA1.2.280040679.1609624487'})
    driver.add_cookie({'name': '_nx_mpcid', 'value': '6ab000e3-966f-4968-afde-7af1f8f882d3'})
    driver.add_cookie({'name': 'ak_bmsc',
                       'value': '1DE2B53E1C94AE314878002285ACBF555F65B5355C4900001A18F25F87F64136~pl0RQ16B0qed/hgmN8IDQqDyzG8UDwrAxv4L6T246G8WWGDaWNoVxBClmqhjCpjrexSgngAuUsXoUZuh3nHARiYgbN+11Fp7SAVANOTFsKpNBvgpUgnqogImwAWiysfHr0YKNPsiT9M7tuN/kEK3LcX92fwjzM//8ReaEAT+VgS72+q4Quv+SIuyXnFPv12VLJl9RMaZwiy0faP0NgP3JLRcEy1/jYJub4g+n/hGgOmeAtOGPMWw2cF5KXBU+CtYZBzaUMbLx2tDlEmicQu44y4D1TSOvpGi9Q5MeoCs1Xiyw='})
    driver.add_cookie({'name': 'bm_sv',
                       'value': '8FB5D238281796F4736AFAFBA2FAD8A8~5+SUZ5edX3Xr2bXJrSzOOIooyjtmNZBIQOGrx1DMoeu1L8f7vw4WMqUBDZ5kxUqj+k0kw7/uqcv7TRuqizMQpZZrMMYQKUlQHktYoL6CKoP42XUPEXg95a9WQiE9WuiEMOu6dLajxxByAgg+VETELA=='})
    driver.add_cookie({'name': 'ealocale', 'value': 'it-it'})
    time.sleep(1)

    driver.go_to('https://signin.ea.com/')
    time.sleep(2)  # chargement de la page
    driver.add_cookie({'name': 'webun', 'value': 'sam4nzd@gmail.com'})
    driver.add_cookie({'name': 'isPhone', 'value': 'false'})
    driver.add_cookie({'name': 'isPogo', 'value': 'false'})
    driver.add_cookie({'name': 'JSESSIONID', 'value': '3BD293E4C24E491982799AE83F3EBB34.prdaccounts-80'})
    time.sleep(1)  # chargement de la page

    time.sleep(2)  # chargement de la page
    driver.go_to('https://accounts.ea.com/')
    driver.add_cookie({'name': 'PLAY_LANG', 'value': 'en'})
    driver.add_cookie({'name': 'remid',
                       'value': 'TUU6QlU0V3pBaGhlNTNxaDhYVW1pZVRTZ29uZTFwVzdDNllxcW95VDRRQjoxMjI4MjU5NDY.2jHjiPveX9l9KnVDSQKoymxCQiTmOHmgfAeQluN5'})
    driver.add_cookie({'name': 'sid',
                       'value': 'U3VURW5STVh3T2toQXBVRXdYdk5Vd0E1azJFbFQ2NEkzcnRsT0plSXRYSWJZZkZKRmd4UndtM2pJYkxPNA.HNVAKWFTRQcwM0vq8aZqW9tcp4TNUmMtC4T8J17DjGo'})
    # driver.add_cookie({'name': file.readline().replace('\n', ''), 'value': file.readline().replace('\n', '')})
    time.sleep(1)  # chargement de la page
    # file.close()

    time.sleep(1)
    driver.go_to('https://www.ea.com/fifa/ultimate-team/web-app/')
    # loading
    time.sleep(10)
    driver.click('Login')
    # loading
    time.sleep(3)

    # login
    driver.type('Enricosnitch418', into='Password', id='passwordFieldId')
    time.sleep(2)
    driver.click('Log In')
    # end login

    # in companion app
    ready = 'n'
    while ready != 'y':
        ready = input("Are you ready? (driver App Home) [y/n] ")


def credits(driver):
    coins = driver.driver.find_element_by_class_name('view-navbar-currency-coins').text
    a_coins = int((coins.replace(',', '')).replace(' ', ''))
    print('credits : ', a_coins)


def market_value(player_name):
    r = requests.get()
    # TO DO
    # Crea dizionario con i vari tipi di carta su fifa e futbin e associa i tipi uguali
    # apri una nuova tab con il nome del giocatore. Chiedi prima se vuole il prezzo da futbin
    # cerca il giocatore su https://www.futbin.com/21/players su questa barra id="players_search"
    # usa questo dropdwon class="dropdown-menu dropdown-menu2 general_dd" per cercare la versione (dal dizionario)
    # <a class="dropdown-item dropdown-item-rt static-filter".text per trovare il tipo e poi fare .click
    # fino a qua apre la pagina del giocatore
    # dopo si può prendere il prezzo e usarlo in altri modi tipo autovendita a quel prezzo o scriverlo in console
    # data-player-resource cerca nella pagina futbin del giocatore per trovare l'ID univoco
    # vai a questo link https://www.futbin.com/21/playerPrices?player=ID_UNIVOCO
    # Prendi il prezzo da quella pagina guardando dal francese


def buy_player(driver):
    # transfers page
    if driver.exists('Transfers'):
        driver.click('Transfers')
        time.sleep(0.7)

    # transfer market
    if driver.exists('SEARCH THE TRANSFER MARKET'):
        driver.click('SEARCH THE TRANSFER MARKET')
        time.sleep(0.2)

    # search player
    letter = 0
    player_name = input("Who you want to buy? "
                        "(Write 'any' if you won't insert the name) "
                        "Insert: ")
    # print(market_value(player_name))
    if player_name != 'no' or 'none' or 'no one' or 'any':
        time.sleep(1.5)
        driver.type(player_name[0].replace('-', ' '), into='Type Player Name', clear=False)
        while letter < len(player_name):
            time.sleep(0.1)
            driver.type(player_name[letter].replace('-', ' '), into='Type Player Name', clear=False)
            letter = letter + 1
        letter = 0
        time.sleep(1)
        driver.click(classname="btn-text", number=8)

    # price
    price_to_buy = int(input("For how much do you want to buy? "))
    time.sleep(0.2)
    driver.type(price_to_buy, classname="numericInput", number=4)

    # count
    count = 150
    min_price = '0' + str(count)
    driver.type(min_price, classname="numericInput", number=1)
    time.sleep(1.2)

    # numbers of research
    stop = int(input('How many searches do you want to do? '))

    # Selection between transfer list and sell it now
    selection = int(input('1 if you want to sell it new 0 if you want to send it to transfer list [0/1] '))

    if selection:
        # price to resell
        price = input('For how much do you want to resell it? ')

    # start of research
    attemp = 0
    while stop != 0:

        try:
            driver.click('Search')

            # buy
            time.sleep(0.2)
            if driver.exists('Buy Now'):
                try:
                    driver.click('Buy Now')

                    if driver.exists('OK'):
                        driver.click('OK')
                        print(f'This is the {attemp} attemp')
                        print('Find!')
                        time.sleep(2)

                        if driver.exists('Send to Transfer List'):
                            if selection == 1:
                                time.sleep(1)
                                driver.click('List on Transfer Market')
                                time.sleep(0.5)
                                if driver.exists(classname="numericInput"):
                                    driver.click(classname="numericInput", number=2)
                                    driver.type(price, classname="numericInput", number=2, clear=False)
                                    driver.click(classname="numericInput", number=1)
                                    driver.type(str((int(price) - 100)), classname="numericInput", number=1,
                                                clear=False)
                                time.sleep(2)
                                driver.click('List for Transfer')
                                print(f'You have list {player_name}!')
                            else:
                                driver.click('Send to Transfer List')
                                print(f'You got {player_name}!')
                        else:
                            print('Miss! :(')
                except:
                    pass

            # repeat
            stop = stop - 1
            time.sleep(0.2)
            driver.click(classname='ut-navigation-button-control')
            time.sleep(random.randint(1, 3))
            attemp = attemp + 1
            # count
            if count + 100 >= price_to_buy or count == 700:
                count = 150
                driver.type('000', classname="numericInput", number=1)
            else:
                count = count + 50
                min_price = '0' + str(count)
                driver.type(min_price, classname="numericInput", number=1)
                time.sleep(1.2)
            if not driver.exists('Search'):
                stop = 0
        except:
            if driver.exists('Home'):
                driver.click('Home')
                time.sleep(0.7)
            print('Interrupted')

    # end of research

    # finish
    driver.click('Home')
    print('FINISH')


def sell_player(driver):
    if driver.exists('Transfers'):
        driver.click('Transfers')
        time.sleep(0.7)

    # transfer market
    if driver.exists('TRANSFER LIST'):
        driver.click('TRANSFER LIST')
        time.sleep(0.7)

    choice = 0

    while driver.exists(classname='ut-navigation-button-control') and driver.exists('List on Transfer Market'):

        # clear sold
        if driver.exists('Clear Sold'):
            driver.click('Clear Sold')
            time.sleep(0.2)

        # relist
        if driver.exists('Re-List All'):
            driver.click('Re-List All')
            time.sleep(0.6)
            if driver.exists('Yes'):
                driver.click('Yes')
                time.sleep(0.4)

        # click on 'List on Transfer Market'
        if driver.exists('List on Transfer Market'):
            driver.click('List on Transfer Market')
            time.sleep(0.5)

            # set the price
            if choice == 0 or choice == 1:

                same = 'y'
                if choice == 1:
                    same = input("Do you want change the price? [y/n] ")

                if same != 'n':
                    start_price = input("'Start price'? ")
                    buy_now_price = input("'Buy now price'? ")

                if choice == 0:
                    choice = int(input("""1. Set the price for each
2. Same price for every player
"""))

            # sell
            if driver.exists(classname="numericInput"):
                web.click(classname="numericInput", number=2)
                driver.type(buy_now_price, classname="numericInput", number=2, clear=False)
                web.click(classname="numericInput", number=1)
                driver.type(start_price, classname="numericInput", number=1, clear=False)
                driver.click('List for Transfer')

        time.sleep(0.5)

    print('FINISH')
# main

"""
r = requests.post('https://signin.ea.com/p/driver2/login?execution=e2026505167s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.ea.com%252Flogin_check%26state%3D0d7f7e80-f710-4ab3-81c2-4aabfe633d68%26client_id%3DEADOTCOM-driver-SERVER')
print(r.content)
if r.status_code == 200:
    file = open('C:/Users/GAMER/Desktop/BotFifa1.0/cookies.txt', 'w')
    if os.path.getsize('C:/Users/GAMER/Desktop/BotFifa1.0/cookies.txt') == 0:
        print("ciao")
        file.write("_ga"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["_ga"]+'\n')
        file.write("_gat"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["_gat"]+'\n')
        file.write("_gid"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["_gid"]+'\n')
        file.write("_nx_mpcid"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["_nx_mpcid"]+'\n')
        file.write("ak_bmsc"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["ak_bmsc"]+'\n')
        file.write("bm_sv"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["bm_sv"]+'\n')
        file.write("ealocale"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["ealocale"]+'\n')
        file.write("webun"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["webun"] + '\n')
        file.write("isPhone"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["isPhone"] + '\n')
        file.write("isPogo"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["isPogo"] + '\n')
        file.write("PLAY_LANG"+'\n' "en" + '\n')
        file.write("remid"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["remid"] + '\n')
        file.write("sid"+'\n' + requests.utils.dict_from_cookiejar(r.cookies)["sid"] + '\n')
        file.close()
"""

web = Browser("--disable-dev-shm-usage")

# login
login(web)

# buy players
start = 'y'

while start == 'y':
    credits(web)
    decision = input("""1. Buy players
2. Sell players
3. Bid players
""")

    if decision == '1':
        buy_player(web)

    if decision == '2':
        sell_player(web)

    if decision == '3':
        print('Future...')

    start = input('Do you wish to continue? [y/n]: ')
