import requests, os, time, threading, ctypes, json
from colorama import Fore, init
init()

config = json.load(open('config.json','r'))
cookie = config['cookie']

bought = 0
total = 0

def commandTitle():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Bought/Total: {bought}/{total}')

threading.Thread(target=commandTitle).start()

def askInput():
    strings = f"""{Fore.WHITE}[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] {Fore.LIGHTCYAN_EX}All
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Head
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Face
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}4{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Neck
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}5{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Shoulder
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}6{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Front
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}7{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Back
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}8{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Waist
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}9{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Gear
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}10{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Hair
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}11{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Heads
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}12{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Faces

    """
    print(strings)
    choice = int(input(f'Choice: '))

    if choice == 1:
        items = allAccessories()
    elif choice == 2:
        items = headAccessories()
    elif choice == 3:
        items = faceAccessories()
    elif choice == 4:
        items = neckAccessories()
    elif choice == 5:
        items = shoulderAccessories()
    elif choice == 6:
        items = frontAccessories()
    elif choice == 7:
        items = backAccessories()
    elif choice == 8:
        items = waistAccessories()
    elif choice == 9:
        items = gearAccessories()
    elif choice == 10:
        items = hairAccessories()
    elif choice == 11:
        items = headsAccessories()
    elif choice == 12:
        items = facesAccessories()
    purchaseItems(items)

def allAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=Accessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: break
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=BodyParts&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=BodyParts&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def headAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=HeadAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def faceAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=FaceAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def neckAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=NeckAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def shoulderAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=ShoulderAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def frontAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=FrontAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def backAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=BackAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def waistAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=WaistAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def gearAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=Accessories&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=GearAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def hairAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=BodyParts&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=HairAccessories&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def headsAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=BodyParts&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=Heads&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def facesAccessories():
    items = []
    cursor = ''
    while True:
        r = requests.get(f'https://catalog.roblox.com/v1/search/items?category=BodyParts&creatorTargetId=1&limit=60&maxPrice=0&minPrice=0&subcategory=Faces&cursor={cursor}', cookies={'.ROBLOSECURITY': cookie}).json()
        if 'data' in r:
            for x in r['data']:
                items.append(x['id'])
            if r['nextPageCursor'] == None: return items
            cursor = r['nextPageCursor']
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
            time.sleep(30)

def purchaseItems(items):
    global bought, total
    total += len(items)
    for item in items:
        while True:
            try:
                r = requests.get(f'https://api.roblox.com/marketplace/productinfo?assetId={item}').json()
                if 'ProductId' in r:
                    productId = r['ProductId']
                    itemName = r['Name']

                    while True:

                        csrfToken = requests.post(
                            'https://auth.roblox.com/v2/login',
                            cookies = {'.ROBLOSECURITY': cookie}
                            ).headers['X-CSRF-TOKEN']

                        buy = requests.post(
                            f'https://economy.roblox.com/v1/purchases/products/{productId}',
                            json = {"expectedCurrency":1,"expectedPrice":0,"expectedSellerId":1},
                            cookies = {'.ROBLOSECURITY': cookie},
                            headers = {'X-CSRF-TOKEN': csrfToken}
                            )

                        if buy.status_code == 200:
                            print(f'{Fore.GREEN}Successfully {Fore.WHITE}purchased item > {Fore.GREEN}{itemName}')
                            bought += 1
                            break

                        else:
                            print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 1 minute')
                            time.sleep(30)
                    break

                else:
                    print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
                    time.sleep(30)
            except:
                print(f'{Fore.WHITE}[{Fore.YELLOW}Error{Fore.WHITE}] Ratelimited, retrying in 30 seconds')
                time.sleep(30)
                pass


askInput()


#itemsToBuy = headAccessories()
