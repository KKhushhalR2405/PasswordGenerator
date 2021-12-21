from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
# Create your views here.

# Local functions

def generate_password(length,ptype):
    length = int(length)
    
    if ptype == 'alphanumeric':
        sample1 = list('abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sample2 = list('1234567890')
        length1 = length//2
        length2 = length - length1
        pass1 = random.sample(sample1,length1)
        pass2 = random.sample(sample2,length2)
        pass1.extend(pass2)
        password = ''.join(random.sample(pass1,length))

    elif ptype == 'alphabetic':
        sample = list('abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        password = ''.join(random.sample(sample,length))
        
    else:
        sample = list('12345678901234567890')
        password = ''.join(random.sample(sample,length))

    return password

# View Functions
def index(request):
    return render(request,'index.html')

def generate(request):
    if request.method == 'GET':
        return redirect('index')
    else:
        length = request.POST['length']
        ptype = request.POST['gridRadios']
        password = generate_password(length,ptype)
        content = {
            'password': password,
        }
        return render(request,'generate.html',context = content)