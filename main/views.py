
from django.shortcuts import HttpResponse, render

def homeProject(request):   # Главная
    return render(request, "main/homeProject.html")

def companiesProject(request):     # О компании
    return render(request, "main/companiesProject.html")

def servisProject(request): # Услуги
    return render(request, "main/servisProject.html")

def production(request): # Изготовление металоконструкций
    return render(request, "main/production.html")

def metalworking(request): # Металлообработка
    return  render(request, "main/metalworking.html")

def designing(request): # Проектирование
    return render(request, "main/designing.html")

def mounting(request): # Монтаж
    return render(request, "main/mounting.html")

def productsProject(request): # Наша продукция
    return render(request, "main/productsProject.html")

def wireframes(request): # Каркасы
    return render(request, "main/wireframes.html")

def straightWalled(request): # Прямостенные
    return render(request, "main/straightWalled.html")

def arched(request): # Арочные
    return  render(request, "main/arched.html")

def combined(request): # Комбинированные
    return render(request, "main/combined.html")

def constructions(request): # Конструкции
    return render(request, "main/constructions.html")

def screwPiles(request): # Винтовые сваи
    return render(request, "main/screwPiles.html")

def architecturalForms(request): # Архитектурные формы
    return  render(request, "main/architecturalForms.html")

def newsProject(request): # Новости
    return render(request, "main/newsProject.html")

def objectsProject(request): # Наши объекты
    return render(request, "main/objectsProject.html")

def contactsProject(request): # Контакты
    return render(request, "main/contactsProject.html")