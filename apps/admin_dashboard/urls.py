from django.conf.urls import url

from apps.admin_dashboard import views

urlpatterns = [
    url(r'^$', views.CategoryDashBoardView.as_view()),
    url(r'^cat_summary', views.category_summary),
]
