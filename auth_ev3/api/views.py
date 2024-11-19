from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario  # Importa tu modelo personalizado
from django.shortcuts import redirect

# Crear un usuario con el modelo personalizado
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            # Imprime el cuerpo de la solicitud para inspección
            print("Body recibido:", request.body)
            print("Encabezados:", request.headers)

            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            # Validación adicional de campos
            if not username or not password or not email:
                print("Datos faltantes en el registro.")
                return JsonResponse({'Error': "Faltan campos obligatorios"}, status=400)

            if Usuario.objects.filter(username=username).exists():
                return JsonResponse({'Error': "El usuario ya existe"}, status=400)

            user = Usuario.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'Success': "Usuario registrado", 'user_id': user.id}, status=201)
        
        except json.JSONDecodeError:
            print("Error: Formato JSON no válido en la solicitud.")
            return JsonResponse({'Error': "Formato JSON no válido"}, status=400)
        
        except Exception as e:
            print("Error inesperado:", str(e))
            return JsonResponse({'Error': "Error en el registro"}, status=400)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)
# Función para login de usuario
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            # Recibir los datos enviados en formato JSON
            data = json.loads(request.body)
            email = data.get('email')  # El email será utilizado como el campo username
            password = data.get('password')

            # Autenticamos al usuario usando el email como 'username'
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)  # Iniciar sesión
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
            return redirect('/')
            ##return JsonResponse({'Success': "Usuario desconectado"}, status=200)
        except Exception as e:
            print("Error "+str(e))
            return JsonResponse({'Error': "Error en el logout"}, status=400)
    else:
        return JsonResponse({'Error': "Método no permitido"}, status=405)

# Obtener información del usuario
def user(request, id):
    try:
        if request.method != 'GET' and request.method !='delete':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        if request.method == 'DELETE':
            user = Usuario.objects.get(id=id)
            user.delete()
            return JsonResponse({'Success': "Usuario eliminado"}, status=201)
        try:
            user = Usuario.objects.get(id=id)
            return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})
        except Usuario.DoesNotExist:
            return JsonResponse({'Error': "Usuario no encontrado"}, status=404)
    except Exception as e:
        print("Error "+str(e))
        return JsonResponse({'Error': "error del servicio"}, status=400)

# Obtener todos los usuarios
def users(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'Error': "Metodo no permitido"}, status=405)
        users = Usuario.objects.all()  # Cambiar a Usuario
        users_list = []
        for user in users:
            users_list.append({'id': user.id, 'username': user.username, 'email': user.email})
        return JsonResponse(users_list, safe=False)
        
    except Exception as e:
        print("Error "+str(e))
        return JsonResponse({'Error': "error del servicio"}, status=400)

# Verificación del estado de autenticación del usuario
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
