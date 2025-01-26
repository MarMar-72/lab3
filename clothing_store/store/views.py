from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

def preferences(request):
    preferred_style = request.COOKIES.get('preferred_style', 'Не выбрано')
    preferred_size = request.COOKIES.get('preferred_size', 'Не выбрано')

    if request.method == 'POST':
        style = request.POST.get('style')
        size = request.POST.get('size')
        response = HttpResponseRedirect('/')
        response.set_cookie('preferred_style', style, max_age=3600 * 24 * 30)
        response.set_cookie('preferred_size', size, max_age=3600 * 24 * 30)
        return response

    return render(request, 'store/form.html', {
        'preferred_style': preferred_style,
        'preferred_size': preferred_size,
    })