from django.shortcuts import render
from django.shortcuts import render_to_response
from core.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/main/")
	else:
		form = UserCreationForm()
	return render(request, "register.html", {
		'form':form,
		})

def userpage(request, id=''):

	user = request.user
	postlist = Post.objects.filter(user=user)

	return render_to_response('userpage.html', {'postlist':postlist},
			 context_instance=RequestContext(request))

