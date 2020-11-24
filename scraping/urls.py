from django.contrib import admin
from django.urls import path
from .Trust_views import *
from .facebook_views import *
from .google_view import *
from .feefo_views import *
from .youtube_views import *

urlpatterns = [
    path('trust_search/',trust_search,name="trust_search"),
    path('trust_counter/',trust_counter,name='trust_counter'),
    path('trust_clear/',trust_clear,name='trust_clear'),

    path('facebook_search/',facebook_search,name="facebook_search"),
    path('facebook_counter/',facebook_counter,name='facebook_counter'),
    path('facebook_clear/',facebook_clear,name='facebook_clear'),

    path('youtube_search/',youtube_search,name="youtube_search"),
    path('youtube_counter/',youtube_counter,name='youtube_counter'),
    path('youtube_clear/',youtube_clear,name='youtube_clear'),

    path('google_search/',google_search,name="google_search"),
    path('google_counter/',google_counter,name='google_counter'),
    path('google_clear/',google_clear,name='google_clear'),

    path('feefo_search/',feefo_search,name="feefo_search"),
    path('feefo_counter/',feefo_counter,name='feefo_counter'),
    path('feefo_clear/',feefo_clear,name='feefo_clear'),
]
