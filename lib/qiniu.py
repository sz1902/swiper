from qiniu import Auth, put_file, etag
import qiniu.config

from common import keys
from swiper import config

access_key = config.QN_ACCESS_KEY
secret_key = config.QN_SECRET_KEY
bucket_name = config.QN_BUCKET_NAME


def upload_to_qiniu(filepath, uid):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间

    # 上传后保存的文件名
    key = keys.AVATAR_KEY % uid
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    ret, info = put_file(token, key, filepath)
    # print(info)
    # print(ret)
    if info.status_code == 200:
        # 上传成功
        return True
    return False
