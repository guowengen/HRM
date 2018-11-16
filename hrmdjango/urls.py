from django.conf.urls import url

import xadmin
from hrm.views import staffsubmit

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^staffsubmit/$',staffsubmit,name='staffsubmit'),
    url(r'^$', xadmin.site.urls)
]
