# login_check('PUT','GET','POST')
from django.http import JsonResponse
import jwt
from user.models import UserProfile

KEY = '584023982'
def login_check(*methods):
    def _login_check(func):
        def wrapper(request,*args,**kwargs):
            # 通过request检查token
            # 校验不通过，return JsonResponse()
            # user 查询出来
            token = request.META.get('HTTP_AUTHORIZATION')
            if request.method not in methods:
                return func(request,*args,**kwargs)
            if not token:
                result = {'code':107,'error':'Please login'}
                return JsonResponse(result)
            try:
                res = jwt.decode(token,KEY,algorithm=['HS256'])
            except jwt.ExpiredSignatureError:
                # token过期了
                result = {'code':108,'error':'Please login'}
                return JsonResponse(result)
            except Exception as e:
                result = {'code':109,'error':'Please login'}
                return JsonResponse(result)
            username = res['username']
            try:
                user = UserProfile.objects.get(username=username)
            except:
                user = None
            if not user:
                result = {'code':110,'error':'no user'}
                return JsonResponse(result)
            # 将查询成功的user赋值给request
            request.user = user
            return func(request,*args,**kwargs)
        return wrapper
    return _login_check