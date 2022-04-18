from django.shortcuts import render

# Create your views here.
def home(request):
 return
render(request,'home.html',context={'sepal_length':3,'sepal_width':2,'petal_le
ngth':2,'petal_width':2,'class':"Iris Setosa"},)
