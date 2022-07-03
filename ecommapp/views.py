from django.shortcuts import render
from .forms import signupform,VerifyForm
from django.shortcuts import redirect
from .import verify
from .decorators import verification_required 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product

@login_required(login_url='/login/')
@verification_required                 #adding extra decorators so that every user get verified 
def index(request):
    return render(request,'ecommapp/index.html')

def register(request):    #view for signupform and saving the data that user is sending while registering
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            verify.send(form.cleaned_data.get('phone'))   #after cleaning the form sending code 
            return redirect('index')
    else:
        form=signupform()
    context={'form':form} 
    return render(request,'ecommapp/register.html',context)

def verify_code(request):   #verifying the code which is sent to user's mobile no 
    form=VerifyForm()
    if request.method=='POST':
        form=VerifyForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                print(request.user.is_verified)
                request.user.save()
                return redirect('index')
        else:
            return HttpResponse('incorrect code ')
    else:
        form=VerifyForm()
    context={'form':form}
    return render(request,'ecommapp/verify.html',context)

def product_list(request):   #getting all the phone which is in the database 
    products=Product.objects.filter(available=True)     #query set to get phone which are available
    context={'products':products}                       #to show the output on the html page 
    return render(request,'ecommapp/store.html',context)

def product_deatail(request,id):   #getting specific phone which user has clicked 
    product=get_object_or_404(Product,id=id,available=True)     
    context={'product':product}
    return render(request,'ecommapp/product.html',context)

