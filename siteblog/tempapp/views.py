from django.http import HttpResponse
from django.template import loader
from .models import Temp
from django.shortcuts import render
from .forms import TempForm

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")




# def index(request):
#     latest_temp_list = Temp.objects.order_by('-temp_date')[:100]
#     # output = ', '.join([q.value for q in latest_temp_list])
#     text = ''
#     for q in latest_temp_list:
#         print(q.temp_date, q.value)
#         text+= str(q.temp_date) + '  ' + str(q.value) + ' ' +'\n\r'+ '\n'
#
#     output = text
#     return HttpResponse(output)

# def index(request):
#     latest_temp_list = Temp.objects.order_by('-temp_date')[:100]
#     template = loader.get_template('tempapp/index.html')
#     context = {
#         'latest_temp_list': latest_temp_list,
#     }
#     return HttpResponse(template.render(context, request))

# def create(request):
#     form = TempForm()
#
#     data = {
#         'form': form
#     }
#
#     return render(request, 'tempapp/index.html', data)

def index(request):
    if request.method == 'POST':
        print(request)
        form = TempForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверна'
            print(error)

    latest_temp_list = Temp.objects.order_by('-temp_date')[:100]
    template = loader.get_template('tempapp/index.html')

    form = TempForm()
    data = {
        'form': form,
        'latest_temp_list': latest_temp_list,
    }

    return HttpResponse(template.render(data, request))