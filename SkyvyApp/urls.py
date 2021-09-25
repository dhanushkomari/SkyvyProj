from django.urls import path
from . import views

##########################################
app_name = 'SkyvyApp'

urlpatterns = [
    path('bot/<str:id>', views.bot_details, name = 'bot-details'),
    path('update/<str:id>', views.bot_update, name = 'bot-update')
]
