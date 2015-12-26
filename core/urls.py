from django.conf.urls import include, url
from core import views

urlpatterns = [
	url(r'^$',views.main, name = 'main'),
	url(r'^add/',views.addPost, name='add'),
	url(r'^view/(?P<id>\d+)/$',views.viewPost, name='view'),
	url(r'^edit/(?P<id>\d+)/$',views.editPost, name='edit'),
	url(r'^delete/(?P<id>\d+)/$',views.deletePost, name='delete'),
	url(r'^upvote/(?P<id>\d+)/$',views.upvote, name='upvote'),
	url(r'^downvote/(?P<id>\d+)/$',views.downvote, name='downvote'),
	url(r'^test/',views.test, name='test'),

	]