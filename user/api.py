from django.core.cache import cache

from lib.sms import send_sms
from common import errors, keys
from lib.http import  render_json
from user.models import User


def submit_phone(request):
    """提交手机号码"""
    phone = request.POST.get('phone')

    # 给这个手机号码发短信
    flag, msg = send_sms(phone)
    if not flag:
        return render_json(code=errors.SMS_ERROR, data=msg)
    return render_json()


def submit_vcode(request):
    """提交验证码, 完成登录或者注册"""
    vcode = request.POST.get('vcode')
    phone = request.POST.get('phone')

    # 从缓存中取出vcode
    key = keys.VCODE_KEY % phone
    cached_vcode = cache.get(key)
    print(cached_vcode)
    if vcode == cached_vcode:
        # 验证码正确,可以登录或者注册
        # try:
        #     user = User.objects.get(phonenum=phone)
        # except User.DoesNotExist:
        #     # 说明是注册
        #     # 创建用户
        #     user = User.objects.create(phonenum=phone, nickname=phone)

        user, created = User.objects.get_or_create(phonenum=phone,
                        defaults={'nickname': phone})
        print(created)
        # 写入session
        request.session['uid'] = user.id

        # 登录或注册成功之后,需要把用户信息返回给前端
        return render_json(data=user.to_dict())
    else:
        return render_json(code=errors.VCODE_ERROR, data='验证码错误')





