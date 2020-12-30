from django.utils.deprecation import MiddlewareMixin

class MwM1(MiddlewareMixin):
    # 1.处理请求前方法
    def process_request(self,request):
        print('每次请求前都会调用request——11111')
        pass



    # 2.处理请求后方法
    def process_response(self,request,response):
        print('每次响应前都会调用response——11111')
        return response


class MwM2(MiddlewareMixin):
    # 1.处理请求前方法
    def process_request(self,request):
        print('每次请求前都会调用request——22222')
        pass



    # 2.处理请求后方法
    def process_response(self,request,response):
        print('每次响应前都会调用response——22222')
        return response