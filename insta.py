import requests,random,string,json,os,time
try: 
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet

try: 
    import instaloader as l
except:
    os.system("pip install instaloader")
    import instaloader as l


red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
white = "\033[1m\033[37m"

L=l.Instaloader()
def logo(name):
    banner = pyfiglet.figlet_format(name, font="slant")
    print(f"{green}_______________________________")
    print(f"\033[1m\033[31m{banner}\033[0m") 
    print(f"{yellow}Code Dev: @AnkuCode\n")
    print(f"{yellow}Telegram: @AnkuCode\n")
    print(f"{green}_______________________________")


logo("AnkuCode")


def fetch_uid(username):
    x=l.Profile.from_username(L.context,username)
    uid=x.userid
    return uid


def year(uid):

    try: 
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (33254029834, 2020),  
            (43254029834, 2021), 
            (51254029834, 2022),  
            (57254029834, 2023),  
            (62254029834, 2024), 
            (66254029834, 2025),  
        ]
        for x,y in ranges:
            if uid<=x:
                return y
            
    except Exception as e:
        return e
    

def eizon_python():
    
    user_id=fetch_uid(username)
    yearr=year(user_id)
    data = {
        'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
        'variables': json.dumps({
            'id': user_id,
            'render_surface': 'PROFILE'
        }),
        'doc_id': '25618261841150840'
    }

    headers = {
        'X-FB-LSD': data['lsd'],
        'Content-Type': 'application/x-www-form-urlencoded'  
    }

    try:
        response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
        response.raise_for_status()
        response_json = response.json()
        print(f'{green}Loading Info Please wait...')

        user_data = response_json.get('data', {}).get('user', {})

        for i,j in user_data.items():
            print(f"{cyan}{i} : {green}{j}{white}")
        print(f'{cyan}Year of creation: {green}{yearr}{white}')

    except requests.exceptions.RequestException as e:
        print(f"{red}Request error:{white}{e}{white}")
    except json.JSONDecodeError:
        print(f"{red}Response could not be decoded as JSON.")
    except Exception as e:
        print(f"{red}Unexpected error:{white}{e}{white}")



while True:
    print(f"{magenta} Welcome to Insta Metadata fetcher: ".center(40))
    print(f"{yellow}Please Enter Your username (without @):")
    username=input(f'----> {green} ')
    eizon_python()
    choose=input(f"Do You wnat to conitnue? y/n\n---> {green}")
    if choose.lower()=='n':
        print(f"{yellow}Thanks for using tool By @AnkuCode")
        break
    else:
        os.system('clear||cls')
        continue


