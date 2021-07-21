from django.urls import path
from . import views  # noticeboard의 views를 임포트한다
# URL은 view와 template을 이어주는 역할을 하고, 이 부분을 만들어 주는 작업을
# URLconf라고 한다.path()함수 이용
app_name = 'noticeboard' #일종의 도메인 생성
urlpatterns = [
    path('', views.main, name='main'),
    path('corona',views.corona, name='corona'),
    path('correlation_tmp',views.correlation_tmp, name='correlation_tmp'),
    path('tmp',views.tmp, name='tmp'),
    path('pm10',views.pm10,name='pm10'),
    path('pm25',views.pm25,name='pm25'),
    path('correlation_dust10',views.correlation_dust10,name='correlation_dust10'),
    path('correlation_dust25',views.correlation_dust25,name='correlation_dust25'),
    path('dust10_yearly',views.dust10_yearly,name='dust10_yearly'),
    path('dust25_yearly',views.dust25_yearly,name='dust25_yearly'),
]