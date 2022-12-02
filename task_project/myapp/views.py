from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):
	users=User.objects.all()
	return render(request,'index.html')

def adduser(request):
	if request.method=="POST":
		User.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			gender=request.POST['gender'],
			subject=request.POST['subject'],
			city=request.POST['city'],
			address=request.POST['address']
			)
		msg="Data added is Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'adduser.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
				email=request.POST['email'],
				city=request.POST['city']
				)
			request.session['email']=user.email
			users=User.objects.all()
			return render(request,'index.html',{'users':users})
		except Exception as e:
			print(e)
			msg="Email Or City Is Incorrect"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,"login.html")

def logout(request):
	try:
		del request.session['email']
		return render(request,"index.html")
	except:
		return render(request,"index.html")

def edit(request,pk):
	user=User.objects.get(pk=pk)
	if request.method=="POST":
		user.name=request.POST['name']
		user.email=request.POST['email']
		user.gender=request.POST['gender']
		user.subject=request.POST['subject']
		user.city=request.POST['city']
		user.address=request.POST['address']
		user.save()
		msg="User Updated Successfully"
		users=User.objects.all()
		return render(request,'index.html',{'users':users,'msg':msg})
	else:
		return render(request,'edit.html',{'user':user})

def delete(request,pk):
	user=User.objects.get(pk=pk)
	user.delete()
	msg="User Deleted Successfully"
	users=User.objects.all()
	return render(request,'index.html',{'users':users,'msg':msg})
