from django.conf.urls import patterns, url, include

from django.contrib import admin

from chess.views import ChessView, MoveView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ChessView.as_view(template_name='chess.html'), name='chess'),
    url(r'^move$', MoveView.as_view(template_name='chess.html'), name='move'),
    
    (r'^admin/', include(admin.site.urls)),
)
