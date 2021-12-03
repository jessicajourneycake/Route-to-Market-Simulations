from django.urls import path
from .views import engage, home, qualify, design, propose, negotiate, closing, won, loss, simulations, simulation2

# simulation/
# simulation/summary

urlpatterns = [
    path('', home),
    path('dashboard/engage', engage),
    path('dashboard/qualify', qualify),
    path('dashboard/design', design),
    path('dashboard/propose', propose),
    path('dashboard/negotiate', negotiate),
    path('dashboard/closing', closing),
    path('dashboard/won', won),
    path('dashboard/loss', loss),
    path('simulation/stages', simulations),
    path('simulation/funnel', simulation2),

]
