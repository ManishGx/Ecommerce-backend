from django.http import JsonResponse

# Create your views here.
def home(request):
  data = {
    'message':'Welocome to the E-commerce store!'
  }
  return JsonResponse(data)