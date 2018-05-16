import requests
import json

CLIENT_ID = ""

URL_FOR_GETTING_TOKEN_AND_USER_ID = f"https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52"

ACCESS_TOKEN = ""
USER_ID = ""

URL_TEMPLATE = f"https://api.vk.com/method/friends.get?user_id=%s&v=5.52&access_token={ACCESS_TOKEN}"

IDS = [USER_ID, '', '']


def get_friends(url, user_id):
    url = url % user_id
    r = requests.get(url)
    return r


def get_friends_by_ids(url, users_id):
    res = []
    for id in users_id:
        res.append(set(json.loads(get_friends(url, id).text)['response']['items']))

    return res


def find_common_friends(friends):
    common = friends[0]
    for i in friends[1:]:
        common = common.intersection(i)
    return [f'http://vk.com/id{i}' for i in common]


friends = get_friends_by_ids(URL_TEMPLATE, IDS)


for i in find_common_friends(friends):
    print(i)