import json

from django.conf import settings
from django.http import HttpResponse


def render_json(code=0, data=None):
    json_data = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        # 人性化的方式显示json字符串
        content = json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        # 压缩json
        content = json.dumps(json_data, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(content=content)
