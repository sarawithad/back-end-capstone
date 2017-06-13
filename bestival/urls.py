from django.conf.urls import url, include
from rest_framework import routers
from APIbestival import views


router = routers.DefaultRouter()
#All routs for API resources
router.register(r'festivals', views.FestivalViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'dates', views.
    DateViewSet)
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
