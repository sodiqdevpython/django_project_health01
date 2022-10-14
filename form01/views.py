from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .form import Userform
from .models import User
# Create your views here.

def home(request):
    form = Userform()
    context = {'form':form}
    return render(request,'form01.html',context)

@require_POST
def form01(request):
    ovr = 0
    lst = []
    form = Userform(request.POST)
    pol=(request.POST.get('pol'))
    if pol =='Мужской':
        for i in range(1,13,1):
            if type(request.POST.get('lst'+str(i)))==str:
                ovr+=1
                lst.append(request.POST.get('lst'+str(i)))
        if len(lst)>=4:
            result=('Очень высокий риск')
        elif 'I' in lst and float(request.POST.get('t29'))>=6.1 and len(lst)<4:
            result=('Высокий риск')
        elif len(lst)==0 and request.POST.get('inlineRadioOptions8')=='нет':
            result=('Низкий риск')
        elif len(lst)==2:
            result=('Умеренный риск')
        else:
            result=('Высокий риск')
    else:
        for i in range(1,13,1):
            if type(request.POST.get('lst'+str(i)))==str:
                ovr+=1
                lst.append(request.POST.get('lst'+str(i)))
        if len(lst)>=4:
            result=('Очень высокий риск')
        elif 'I' in lst and float(request.POST.get('t29'))>=5.1 and len(lst)<4:
            result=('Высокий риск')
        elif len(lst)==0 and request.POST.get('inlineRadioOptions8')=='нет':
            result=('Низкий риск')
        elif len(lst)==2:
            result=('Умеренный риск')
        else:
            result=('Высокий риск')
    f01 = request.POST.get('t12')
    f02 = request.POST.get('t13')
    f03 = request.POST.get('t10')
    f04 = request.POST.get('t11')
    f1 = round(int(f01)/int(f02),2)
    
    f2 = round((int(f04)/(int(f03)**2)),4)
    f3 = f2*10000
    if f3>=19 and f3<=24.9:
        imt = 'Норма'
    elif f3>=25 and f3<=29.9:
        imt = 'Предожирение'
    elif f3>=30 and f3<=34.9:
        imt = 'Первая степень ожирения'
    elif f3>=35 and f3<=39.9:
        imt = 'Вторая степень'
    elif f3>=40 and f3<=44.9:
        imt = 'Третья степень'
    elif f3>=45:
        imt = 'Четвертая степень'
    else:
        imt = 'Не соответствует требованию'
    
    kreatf = float(request.POST.get('t32'))

    if pol =='Мужской' and kreatf<=80:
        skf = 141 * (0.993**int(request.POST['data_rojdeniya']))*((kreatf/88.4)/0.9)**(-0.412)
    elif pol == 'Мужской' and kreatf>80:
        skf = 141 * (0.993**int(request.POST['data_rojdeniya']))*((kreatf/88.4)/0.9)**(-1.210)
    elif pol == 'Женский' and kreatf<=80:
        skf = 144 * (0.993**int(request.POST['data_rojdeniya']))*((kreatf/88.4)/0.7)**(-0.328)
    else:
        skf = 144 * (0.993**int(request.POST['data_rojdeniya']))*((kreatf/88.4)/0.7)**(-1.210)
    t34 = float(request.POST.get('t34'))
    t36 = float(request.POST.get('t36'))
    ka = t34-t36
    context = {
        'result':result,
        'f1':f1,
        'f2':f2,
        'imt':imt,
        'skf':round(skf,2),
        'ka': round(ka,3)
    }
    if form.is_valid() and (pol=='Мужской' or pol=='Женский'):
        new_fio = User(fio=request.POST['fio'],data_rojdeniya=request.POST['data_rojdeniya'],pol=(request.POST.get('pol')),resultn=result)
        new_fio.save()
        return render(request, 'result.html', context)
    else:
        return redirect('form01.html')