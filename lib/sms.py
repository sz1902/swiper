""" 发送短信的模块 """
import random

import requests

from django.core.cache import cache

from swiper import config
from common import keys


def gen_vcode(size=4):
    start = 10 ** (size - 1)
    end = 10 ** size - 1
    return str(random.randint(start, end))


def send_sms(phone):
    params = config.YZX_PARAMS.copy()
    params['mobile'] = phone
    vcode = gen_vcode()
    # 加入缓存
    key = keys.VCODE_KEY % phone
    cache.set(key, vcode, 180)
    params['param'] = vcode

    response = requests.post(config.YZX_URL, json=params)

    if response.status_code ==  200:
        resp_json = response.json()
        print(resp_json)
        if resp_json['code'] == '000000':
            return True, resp_json['msg']
        else:
            return False, resp_json['msg']
    else:
        return False, '发送短信异常'


