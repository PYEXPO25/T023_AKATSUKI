from django.shortcuts import render,redirect
from .models import bill_Data


# def bills(request):
#     if request.method == 'POST':
#         rent = request.POST('rent')
#         electricity = request.POST('electricity')
#         water = request.POST('water')
#         food = request.POST('food')
#         parking = request.POST('parking')

#         room_bill_data = bill_Data(rent=rent, electricity=electricity,water=water,food=food,parking=parking)
#         room_bill_data.save()

    

#     return render(request,'blog/bills.html')