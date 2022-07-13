import requests
import json

def core_login():
    core_url = "https://core.api.wallpostsoftware.com/api/v2/auth/login"
    core_header = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'

    }
    core_login_data = {
        'accountno': '120843',
        'apptype': 'WEB',
        'username': 'giby',
        'password': 'Smit@123',
        'environment': 'Development',
        'deviceuid': 'qwerty12341234',

    }

    core_session = requests.Session()
    core_session.get(core_url, headers=core_header)

    req_res = core_session.post(core_url, data=core_login_data, headers=core_header)
    # extracting authorization token for cookie token

    # response_text = req_res.text
    json_con = json.loads(req_res.text)
    token = json_con['data']['token']
    sskey = 'PHPSESSID=' + str(token)
    dicts = {'Cookie': sskey}
    core_header.update(dicts)
    print(core_header)

    payload = {}
    holiday_url = "https://wallpostsoftware.com/wp/index.php?r=wp/holidays"
    count = core_session.get(holiday_url, headers=core_header, cookies=core_session.cookies)
    print(count.text)


def direct_login():
    #url_w = "https://wallpostsoftware.com/wp"
    headers = {
        "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
        #"Accept-Encoding": "gzip, deflate, br",
        #'Host': 'wallpostsoftware.com',
        #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer":"https://wallpostsoftware.com/wp/index.php?r=site/wPlogin",
    }

    """
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length": '103',
        
    """

    login_link = "https://wallpostsoftware.com/wp/index.php?r=site/wPlogin"

    login_data = {
        "LoginForm[accountno]": "120843",
        "LoginForm[username]": "giby",
        "LoginForm[password]": "Smit@123",
    }

    """
    with requests.Session() as s:
        s.get(url_w, headers=headers)
        cookie = s.cookies
        resp = s.post(login_link, headers=headers, data=login_data)
        print(resp.cookies)
        print(resp.text)
    """

    session = requests.Session()
    #requests.get(login_link, headers=headers)
    req = session.post(login_link, data=login_data, headers=headers,allow_redirects=True)

    sec_link = "https://wallpostsoftware.com/wp/index.php?r=hr/position/getPositionList"
    getse = session.get(sec_link, data=login_data, headers=headers, allow_redirects=True)
    print(getse.json())
    print(getse.cookies)


direct_login()
