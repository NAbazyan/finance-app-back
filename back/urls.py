from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.bills.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/goals/', include('apps.goals.urls')),
    path('api/expenses/', include('apps.expenses.urls')),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/transactions/', include('apps.transactions.urls'))
]
