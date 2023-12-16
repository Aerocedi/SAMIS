from django.shortcuts import render, redirect

# samis/views.py
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import numpy as np
import cv2
import subprocess
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

#@csrf_exempt
#def samis_drone_frame(request):
   # if request.method == 'POST':
    #    frame_data = request.POST.get('frame')
     #   frame = base64.b64decode(frame_data)
      #  frame = np.frombuffer(frame, dtype=np.uint8)
       # frame = cv2.imdecode(frame, flags=1)

        # Process the frame as needed
        # ...

        #return StreamingHttpResponse(frame, content_type="image/jpeg")

# views.py


@csrf_exempt
@require_http_methods(["POST"])  # Ensure that this can only be called via POST request
def run_command(request):
    try:
        # Replace 'your_python_script.py' with your Python script
        output = subprocess.check_output(['python3', 'control.py'], text=True)
        return JsonResponse({'status': 'success', 'output': output})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})



@csrf_exempt
def samis_drone_frame(request):
    if request.method == 'POST':
        frame = request.FILES['frame'].read()
        return StreamingHttpResponse(frame, content_type="image/jpeg")



def login(request):

    return render(request, 'samis/login.html')



def dashboard(request):

    return render(request, 'samis/dashboard.html')

def engine(request):

    if request.method=="POST":
        ans=request.POST.get('task')
        print(ans)
        if ans=="NewEngineRecord":
            return render(request, 'samis/engine.html')
        else:
            return redirect('dash')
    else:
            return render(request, 'samis/dashboard.html')


