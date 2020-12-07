from django.shortcuts import render
from .models import *
from django.views import View
from django.http.response import JsonResponse


class IndexView(View):

    def get(self,request):
        return render(request=request,template_name="index.html")


class IndexViewChart(View):

    def get(self, request):
        context = {}
        if request.COOKIES['isGist'] == 'true':
            client_and_amount = {}
            clients_and_amounts = []
            for client in Client.objects.all():
                client_and_amount['client'] = client.first_name+' '+client.last_name
                amount = 0
                for pay in PayInfo.objects.filter(payer_id=client):
                    amount += pay.amount
                client_and_amount['amount'] = amount
                clients_and_amounts.append(client_and_amount)
                client_and_amount = {}
            context['clients_and_amount'] = clients_and_amounts
        else:
            payinfos = []
            for payinfo in PayInfo.objects.all().order_by('pay_date'):
                amount = payinfo.amount
                date = payinfo.pay_date.date()
                payinfos.append({'amount':amount,'date':date})
            context['payinfos'] = payinfos
        return JsonResponse(data=context, status=200)

# Create your views here.
