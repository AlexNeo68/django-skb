from typing import Any
from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):
    
    print('initial')
    
    def middleware(request: HttpRequest):
        print('before middleware')
        request.user_agent = request.META['HTTP_USER_AGENT']

        response = get_response(request)
        print('after middleware')
        return response
    
    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.request_count = 0
        self.response_count = 0
        self.exception_count = 0

    def __call__(self, request: HttpRequest) -> Any:
        self.request_count += 1 
        print('request_count', self.request_count)
        response = self.get_response(request)
        self.response_count += 1 
        print('response_count', self.response_count)
        return response
        
    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exception_count += 1
        print("got", self.exception_count, 'so far')
