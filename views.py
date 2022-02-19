from django.shortcuts import render
import requests
from urllib.request import urlopen
import json
from scan.models import Accounts

ethereum_token = 'D2R66WU1RBHPPDIGVET25491BTQBNAA97J'


def index(request):
    accounts = Accounts.objects.all()
    list_acc = []


    for i in range(5):
        address = ""
        length = 0

        if i == 0:
            length = 20
        elif i == 1:
            length = 40
        elif i == 2:
            length = 60
        elif i == 3:
            length = 80
        else:
            length = 100

        for j in range(length-20, length):
            if j == 19:
                address += accounts[j].address
            else:
                address += accounts[j].address + ","
        coin_api = 'https://api.etherscan.io/api?module=account&action=balancemulti&address=' + address + '&tag=latest&apikey=' + ethereum_token



        result = requests.get(url=coin_api)
        for i in (result.json())['result']:
            list_acc.append(i)


    for i in list_acc:
        acc = Accounts.objects.get(address=i['account'])
        acc.balance = i['balance']
        print(acc)
        acc.save()



    context = {
        "data" : list_acc
    }


    return render(request, 'chartapp/index.html', {"list_acc": list_acc} )
