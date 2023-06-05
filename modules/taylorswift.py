import requests


class Taylor_newspaper:
    def subscribe(self, email_address):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.taylorswift.com/',
            'Content-type': 'application/x-www-form-urlencoded',
            'cache-control': 'no-cache',
            'Origin': 'https://www.taylorswift.com',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
        }

        data = f'g=WLqdaH&email={email_address.upper()}&$country=United%20States&$fields=$source&$source=Modal'

        response = requests.post('https://manage.kmail-lists.com/ajax/subscriptions/subscribe', headers=headers, data=data)
        print(response.text)

if __name__ == '__main__':
    Taylor_newspaper().subscribe("d838246554@mymaily.lol")
