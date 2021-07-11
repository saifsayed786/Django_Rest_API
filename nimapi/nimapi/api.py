from rest_framework import routers
from client import views as myapp_views  
from apipackage import views 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'client',myapp_views.ClientViewset)
router.register(r'project',myapp_views.ProjectViewset)
 