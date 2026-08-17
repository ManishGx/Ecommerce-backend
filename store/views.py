from django.http import JsonResponse

# Create your views here.
def home():
  data = {
    'message':'Welocome to the E-commerce store!'
  }
  return JsonResponse(data)