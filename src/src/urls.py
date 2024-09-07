
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.ViewsetsGuest)
router.register('movies', views.ViewsetsMovie)
router.register('reservations', views.ViewsetsReservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/fbv/', views.FBV_List),
    path('rest/pk/<int:pk>',views.FBV_PK),
    path('rest/',include(router.urls)),
   # path('making_reservation/',views.making_reservation),

]
