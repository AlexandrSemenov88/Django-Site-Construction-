
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homeProject, name="homeProject"),
    path("companiesProject", views.companiesProject, name="companiesProject"),
    path("servisProject", views.servisProject, name="servisProject"),
    path("production", views.production, name="production"),
    path("metalworking", views.metalworking, name="metalworking"),
    path("designing", views.designing, name="designing"),
    path("mounting", views.mounting, name="mounting"),
    path("productsProject", views.productsProject, name="productsProject"),
    path("wireframes", views.wireframes, name="wireframes"),
    path("cstraightWalled", views.straightWalled, name="straightWalled"),
    path("arched", views.arched, name="arched"),
    path("combined", views.combined, name="combined"),
    path("constructions", views.constructions, name="constructions"),
    path("screwPiles", views.screwPiles, name="screwPiles"),
    path("architecturalForms", views.architecturalForms, name="architecturalForms"),
    path("newsProject", views.newsProject, name="newsProject"),
    path("objectsProject", views.objectsProject, name="objectsProject"),
    path("contactsProject", views.contactsProject, name="contactsProject"),

]
