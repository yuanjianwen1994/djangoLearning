from django.db.models import Sum, Avg
from django.forms import model_to_dict
from django.shortcuts import render
from .models import BlockchainUser, Contract, Nft, Token, Transaction
from django.http import HttpResponse
from django.core import serializers
import json
from datetime import date, datetime


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y/%m/%d')
        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.
def get_price(request):
    # 获取最新的500条数据
    result = Transaction.objects.extra(select={'day': 'date(time)'}).values('day').order_by('day').annotate(
        sum=Sum('token_price'))
    result_ = json.dumps(list(result), ensure_ascii=False, cls=ComplexEncoder)

    return HttpResponse(result_)

