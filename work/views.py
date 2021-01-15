import os

from django.http import HttpResponse

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