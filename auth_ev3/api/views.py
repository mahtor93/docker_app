from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
def user(request):
    try:
        user_id = request.GET['id']
        user = User.objects.get(id=user_id)

        if user is None:
            return JsonResponse({'Error': "Usario no encontrado"}, status=404)
        
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})
    except Exception as e:
            print("Error "+e)
            return JsonResponse({'Error': "error del servicio"}, status=400)

def users(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        users = User.objects.all()
        users_list = []
        for user in users:
            users_list.append({'id': user.id, 'username': user.username, 'email': user.email})
        return JsonResponse(users_list, safe=False)
        
    except Exception as e:
        print("Error "+e)
        return JsonResponse({'Error': "error del servicio"}, status=400)

def deleteUser(request):
    try:
        if request.method != 'DELETE        ':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        user_id = request.GET['id']
        user = User.objects.get(id=user_id)
        user.delete()

        if user is None:
            return JsonResponse({'Error': "Usario no encontrado"}, status=404)
        return JsonResponse('User deleted')
    except Exception as e:
        print("Error "+e)
        return JsonResponse({"Error":"error deñ servicio"}, status=400)
    