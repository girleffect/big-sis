from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@require_POST
def data_switch(request):
    if 'moya' in request.session:
        del request.session['moya']
    else:   
        request.session['moya'] = True
    
    if 'origin_path' in request.POST:
        return redirect(request.POST['origin_path'])
    else:
        return redirect('/')
 