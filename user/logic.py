import os

from common import keys

from swiper import settings
from lib.qiniu import upload_to_qiniu


def handler_upload_file(avatar, uid):
    filename = keys.AVATAR_KEY % uid
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, mode='wb+') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    flag = upload_to_qiniu(filepath, uid)
    return flag

