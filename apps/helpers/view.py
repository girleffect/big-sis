from django.shortcuts import redirect
from django.views.decorators.http import require_GET

@require_GET
def data_switch(request):
    if 'moya' in request.session:
        del request.session['moya']
    else:   
        request.session['moya'] = True
    
    if 'origin_path' in request.GET:
        return redirect(request.GET['origin_path'])
    else:
        return redirect('/')
 