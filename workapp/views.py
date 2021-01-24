import os

from django.http import HttpResponse
from django.shortcuts import render

from model.juese import dizhao
from work.gld import order
from .tasks import yibu, runworktask,clicktesttask,test1,testcheckpoint

def runwork(request):
    # runworktask('任务-开始')
    # runworktask('剧情1幽暗密林')
    # runworktask('任务-再访林纳斯')
    # runworktask('剧情2幽暗密林')
    # runworktask('剧情1猛毒雷鸣废墟')
    # runworktask('剧情1冰霜幽暗密林')
    # runworktask('任务-再访林纳斯')
    # runworktask('剧情1格拉卡')
    runworktask('格兰迪')



    return HttpResponse(str('ok'))

def testcheckpointView(request):
    aa = testcheckpoint()
    return HttpResponse(str('ok'))

def runyibu(request):
    result = yibu.delay()
    return HttpResponse(str(result))

def clicktest(request):
    result = clicktesttask.delay('10,100')
    return HttpResponse(str(result))

def MpasSetowner(request):
    return render(request, "test.html")



dz = dizhao()

def click(request):
    point = request.POST.get('zb')
    dz.mouse_click(point)
    rs = '单击' + str(point)
    print(rs)
    return HttpResponse(str(rs))

def attack(request):
    dz.daguai()
    print('打怪')
    return HttpResponse('打怪')

def attackboos(request):
    dz.attack_boss()
    print('攻击boos')
    return HttpResponse('攻击boos')

def move(request):
    zb = request.POST.get('zb')
    dz.moveTo(zb)
    rs = '移动到' + str(zb)
    print(rs)
    return HttpResponse(str(rs))

def door(request):
    zb = request.POST.get('zb')
    dz.guomen(zb)
    print('过门')
    return HttpResponse('过门')

def run(request):
    order()
    return HttpResponse('run')




