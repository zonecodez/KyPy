import requests
def main():

    response = requests.get('https://httpbin.org/ip')

    return print('Your IP is {0}'.format(response.json()['origin']))


main()