import requests

def request_to_site(url):
    headers = {
        'accept': '*/*',
         'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    try:
        request = requests.get(url, headers=headers)
        return request.text
    except requests.exceptions.ConnectionError:
        print('Проверьте интернет соедиение')
        exit(1)