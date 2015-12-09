from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from models import Post, Comment

def main(request, id=''):
	postlist = Post.objects.filter(deleted=0)
	return render_to_response('index.html',{'postlist' : postlist}
		,context_instance=RequestContext(request)
		)

def addPost(request, id=''):
	if request.method == 'POST':
		title = request.POST['title']
		post = request.POST['post']
		user = request.user
		post_obj = Post(title=title, user=user, postContent=post)
		post_obj.save()
		postlist = Post.objects.filter(deleted=0)
		return render_to_response('index.html',{'postlist' : postlist}
		,context_instance=RequestContext(request)
		)
	else:
		postlist = Post.objects.filter(deleted=0)
		return render_to_response('addnew.html',{'postlist' : postlist}
		,context_instance=RequestContext(request)
		)

def viewPost(request, id=''):

	post = Post.objects.get(id=id)
	return render_to_response('viewPost.html',{'post':post},
		context_instance=RequestContext(request))

def editPost(request, id=''):
	if request.method == 'POST':
		try:
			post = Post.objects.get(id=id)
		except Exception:
			return HttpResponseRedirect('/main/')
		editedPost = request.POST['post']
		user = request.user
		post.postContent = editedPost
		post.save()
		postlist = Post.objects.filter(deleted=0)
		return render_to_response('index.html',{'postlist' : postlist}
		,context_instance=RequestContext(request)
		)
	else:
		postlist = Post.objects.filter(deleted=0)
		return render_to_response('editPost.html',{'postlist' : postlist}
		,context_instance=RequestContext(request)
		)

def deletePost(request, id=''):
	try:
		post = Post.objects.get(id=id)
	except Exception:
		raise Http404
	if post:
		post.delete()
		return HttpResponseRedirect('/main/')
	postlist = Post.objects.filter(deleted=0)
	return render_to_response('index.html',{'postlist' : postlist}
	,context_instance=RequestContext(request))

def upvote(request, id=''):
	post = Post.objects.get(id=id)
	post.rankingPoints+= 1
	post.save()
	return HttpResponseRedirect('/main/')

def downvote(request,id=''):
	post = Post.objects.get(id=id)
	post.rankingPoints-= 1
	post.save()
	return HttpResponseRedirect('/main/')

#will replace postContent like todo2


