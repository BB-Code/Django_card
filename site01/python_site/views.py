from django.shortcuts import render
from python_site.models import Articles_info
from django.core.paginator import Paginator
# Create your views here.
def Index(request):
	limit = 10
	db_info = Articles_info.objects
	paginator = Paginator(db_info,limit)
	page = request.GET.get('page',1)
	info_list = paginator.page(page)
	context = {
    'info_list': info_list
	}
	return render(request,'index.html',context)

def search(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '请输入文章关键字'
		return render(request,'search.html',{'error_msg':error_msg})
	db_info = Articles_info.objects.filter(title__icontains=q)
	return render(request,'search.html',{'error_msg':error_msg,'db_info':db_info})