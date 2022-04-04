import requests
import schedule

def greeting():
    todos_dict={
        '08:00':"Привет",
        '13:00':"Забрать что нибудь",
        '18:00':"уйти домой"

    }

    # print("Добрый день Роман")
    # for k,s in todos_dict.items():
    #     print(f"{k}:{s}")


    response = requests.get(url = "http://yobit.net/api/3/ticker/btc_usd")
    data = response.json()
    bts_price = f"BTC: {round(data.get('btc_usd').get('last'),2)}$\n"

    print(bts_price)


def main():
    # greeting()
    # schedule.every(4).seconds.do(greeting) #Запуск через каждые 4 секунды
    schedule.every().day.at('17:26').do(greeting)

    while True:
        schedule.run_pending()

if __name__ =="__main__":
    main()

