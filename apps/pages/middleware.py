class DatafreeMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
       
        #check GET parameter for Moya App (Android)
        moya_app_id = request.GET.get('x-binu-did', None)  
        #check domain for Moya App (iOS) 
        domain = request.META
        if (moya_app_id is not None):
            request.session['moya'] = True
        response = self.get_response(request)
        return response 
