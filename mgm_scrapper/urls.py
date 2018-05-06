from django.urls import path

from . import views

app_name = 'mgm_scrapper'

urlpatterns = [
	path('', views.Index.as_view(), name='index'),
  path('dayquery/', views.day_query, name='day-query'),
  path('mgmdayhistory/<int:year>/<int:month>/<int:day>', views.MgmDataView.as_view(),
  name='mgm-day-history'),
  path('mgmdata/', views.MgmDataView.as_view(), name='mgm-data'),
  path('savedata/', views.save_data, name='save-data'),
]
