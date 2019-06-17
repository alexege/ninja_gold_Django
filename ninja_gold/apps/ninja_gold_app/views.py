from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    
    if request.session.get('total') == None:
        request.session['total'] = 0

    if request.session.get('building') == None:
        request.session.buildilng = []

    if request.session.get('activities_list') == None:
        request.session['activities_list'] = []

    if request.session.get('activities') == None:
        request.session['actions'] = ""

    return render(request, "ninja_gold_app/index.html")

def process_money(request):

    request.session.building = request.POST["building"]

    if request.method == "POST":
        if request.session.building == 'farm':
            coins = random.randint(10, 21)
            request.session['total'] += coins
            message = 'Earned ' + str(coins) + ' golds from the ' + request.session.building + '! (' + str(datetime.now()) + ')'
        elif request.session.building == 'cave':
            coins = random.randint(5, 11)
            request.session['total'] += coins
            message = 'Earned ' + str(coins) + ' golds from the ' + request.session.building + '! (' + str(datetime.now()) + ')'
        elif request.session.building == 'house':
            coins = random.randint(2, 6)
            request.session['total'] += coins
            message = 'Earned ' + str(coins) + ' golds from the ' + request.session.building + '! (' + str(datetime.now()) + ')'
        elif request.session.building == 'casino':
            amount = random.randint(-50, 51)
            coins = amount
            request.session['total'] += coins
            if amount >= 0:
                message = 'Earned ' + str(coins) + ' golds from the ' + request.session.building + '! (' + str(datetime.now()) + ')'
            else:
                message = 'Lost ' + str(coins) + ' golds from the ' + request.session.building + '! (' + str(datetime.now()) + ')'

        print("coins: " + str(coins))
        print("total: " + str(request.session['total']))
        
        request.session['actions'] += message

        print(request.session['actions'])
        request.session['activities_list'].append(message)
        print(request.session['activities_list'])
        
        return redirect('/')

def reset(request):
    print("Reset total back to 0")
    request.session['activities_list'] = []
    request.session['past_activities'] = []
    request.session['total'] = 0
    return redirect('/')