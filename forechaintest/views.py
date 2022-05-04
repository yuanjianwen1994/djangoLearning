from django.db.models import Sum, Avg
from django.forms import model_to_dict
from django.shortcuts import render
from .models import BlockchainUser, Contract, Nft, Token, Transaction
from django.http import HttpResponse, JsonResponse


# Create your views here.
def get_price(request):
    # 获取最新的500条数据
    result = Transaction.objects.extra(select={'day': 'date(time)'}).values('day').order_by('day').annotate(
        sum=Sum('token_price'))
    print(type(result))
    result = result.values()
    print(type(result))

    return JsonResponse(result)
