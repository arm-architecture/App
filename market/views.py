from market.db_connection import DatabBaseConnection 
from django.shortcuts import render

def greeting(request):
     return render(request, 'greeting.html')

def baseHTML(request):
     return render(request, 'base.html')

def getItems(request):
     db_connection = DatabBaseConnection()
     db_connection.get_connection()
     items = db_connection.fetchall("SELECT * FROM productos;")
     
     return render(request, 'items.html', context={'items': items})
