from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'Error': "El usuario ya existe"}, status=400)
            
            user = User.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({'Success': "Usuario registrado", 'user_id': user.id}, status=201)
        except Exception as e:
            print("Error "+str(e))
            return JsonResponse({'Error': "Error en el registro"}, status=400)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)

# Función para login de usuario
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'Success': "Usuario autenticado"}, status=200)
            else:
                return JsonResponse({'Error': "Credenciales incorrectas"}, status=401)
        except Exception as e:
            print("Error "+str(e))
            return JsonResponse({'Error': "Error en el login"}, status=400)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)

# Función para logout de usuario
@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        try:
            logout(request)
            return JsonResponse({'Success': "Usuario desconectado"}, status=200)
        except Exception as e:
            print("Error "+str(e))
            return JsonResponse({'Error': "Error en el logout"}, status=400)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)
    
def user(request,id):
    try:
        if request.method != 'GET':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'Error': "Usuario no encontrado"}, status=404)
        
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

def deleteUser(request,id):
    try:
        if request.method != 'DELETE':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse('User deleted')
    except Exception as e:
        print("Error "+e)
        return JsonResponse({"Error":"error deñ servicio"}, status=400)

@csrf_exempt
def user_verification(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return JsonResponse({
                'status': 'success',
                'username': request.user.username,
                'email': request.user.email,
            })
        else:
            return JsonResponse({'status': 'error', 'message': 'No autenticado'}, status=401)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)

    