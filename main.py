import random
import time
import requests
import os

from webbot import Browser


def login(driver):
    #file = open('C:/Users/GAMER/Desktop/BotFifa1.0/cookies.txt', 'r')
    driver.go_to('https://accounts.ea.com/')
    time.sleep(2)  # chargement de la page
    driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1394686556.1568073046'})
    driver.add_cookie({'name': '_gat', 'value': '1'})
    driver.add_cookie({'name': '_gid', 'value': 'GA1.2.1959508212.1609598163'})
    driver.add_cookie({'name': '_nx_mpcid', 'value': 'a94b28cb-6a8b-4e49-8252-1d2097cace3c'})
    driver.add_cookie({'name': 'ak_bmsc', 'value': '5FF96DB52481E6F4A976F7C08CF9DF140212F057A5650000C284F05F2C514E77~plUbvedLCGATTkQ0/AwtSyaPiPSHCOEomhoCbu0EKsH6eoGpslVY46c2X2reaS0An5s/yLGZCEnAzKIdNpQl6Q5T+oEFo7SoftyoxoqNguLNSJnVLfcthOtjD3yh0EkVdh/Nuh9f6aLOy1JvTmd7WEVaCkyxM2Hc5sn1yYZdLPeyS1PQjqteAiOwSv0Nj9peSt+oJiTnjVewmsL1EUyI1S7QjzDyrEwjM0EvhsKFGyX7BxaBKAPnf2wZn+oVvo1Wvv'})
    driver.add_cookie({'name': 'bm_sv', 'value': 'F0EA4EAF1812F09628A88095D8CC64F8~seE/F6Mba7d6GyaGuqiWqSfqEL0SNS7tlrOJG2BvBbooELAPvDhowxzoDLN+SuEQfvngSREBJfDTwDxDyM98OqD5qgJ3TgHBIBe7RvetelB847LrAS3Eq/Cc07eOaFx4sJRCv9VpazIYngcf1IcFGA=='})
    driver.add_cookie({'name': 'ealocale', 'value': 'it-it'})
    time.sleep(1)

    driver.go_to('https://signin.ea.com/')
    time.sleep(2)  # chargement de la page
    driver.add_cookie({'name': 'webun', 'value': 'enrimuraro@gmail.com'})
    driver.add_cookie({'name': 'isPhone', 'value': 'false'})
    driver.add_cookie({'name': 'isPogo', 'value': 'false'})
    driver.add_cookie({'name': 'JSESSIONID', 'value': 'B8C54F6BB740D58BC2D5A2D7105F2CB5.prdaccounts-60'})
    time.sleep(1)  # chargement de la page

    time.sleep(5)  # chargement de la page
    driver.go_to('https://accounts.ea.com/')
    driver.add_cookie({'name': 'PLAY_LANG', 'value': 'en'})
    driver.add_cookie({'name': 'remid', 'value': 'TUU6Z0NQNDFrNkJRZG1qeFR2Y1hVRXJrbTQyc3c1RGhmMVh5R2NBSGpTUTowMTAyMDA1NDE.Eqfdq9FJPblXubzm3jLhp6aj2vylqlct3SrVdCMd'})
    driver.add_cookie({'name': 'sid', 'value': 'UzFmWUN3ejlIY1EyTGluVXd4TjhuQVpGMnJkSlg1OW5LUUlIRFNtVmFMZFROZzQ1M1ZvbWU3bU9oV0I2dQ.UeRSfDFTOTGw9z4yT_EXFD9Oa0HEG07lVsN4YRsPBnY'})
    #driver.add_cookie({'name': file.readline().replace('\n', ''), 'value': file.readline().replace('\n', '')})
    time.sleep(1)  # chargement de la page
    #file.close()

    time.sleep(1)
    driver.go_to('https://www.ea.com/fifa/ultimate-team/web-app/')
    # loading
    time.sleep(5)
    driver.click('Login')
    # loading
    time.sleep(3)

    # login
    driver.type('PASSWORD', into='Password', id='passwordFieldId')
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
    player_name = input("Who you want to buy? ")
    if player_name != 'no':
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
    price_to_buy = int(input("How much do you want to buy? "))
    driver.type(price_to_buy, classname="numericInput", number=4)

    # count
    count = 150
    min_price = '0' + str(count)
    driver.type(min_price, classname="numericInput", number=1)
    time.sleep(1.2)

    # numbers of research
    stop = int(input('How many searches do you want to do? '))

    # price to resell
    # price = input('For how much do you want to resell it? ')

    # start of research
    attemp = 0
    while stop != 0:

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
                        driver.click('Send to Transfer List')
                        # driver.type(price, classname="numericInput filled", number=2)
                        # driver.type(str((int(price)-100)), classname="numericInput filled", number=1)
                        # driver.click('List for Transfer')
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

    # end of research

    # finish
    driver.click('Home')
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
    buy_player(web)
    start = input('Do you wish to continue? [y/n]: ')

