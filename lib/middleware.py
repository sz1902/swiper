from django.utils.deprecation import MiddlewareMixin

from user.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 给每一个request加上一个user
        # print('auth middleware ....')
        URL_WHITE_LIST = [
            '/api/user/submit/phone/',
            '/api/user/submit/vcode/'
        ]
        if request.path in URL_WHITE_LIST:
            return

        uid = request.session.get('uid')
        request.user = User.objects.get(id=uid)
