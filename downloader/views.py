from django.shortcuts import render
from .utils import get_reel_download_url
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
import requests

@csrf_exempt
def index(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get("reel_url", "").strip()
        
        # Check if URL is provided and looks like Instagram
        if url and "instagram.com" in url:
            video_url = get_reel_download_url(url)
            
            if video_url:
                context['download_url'] = video_url
            else:
                context['error'] = "Failed to fetch video. Ensure the account is public."
        else:
            context['error'] = "Please enter a valid Instagram Reel URL."
            
    return render(request, 'downloader/index.html', context)

def download_video(request):
    video_url = request.GET.get('url')
    if not video_url:
        return Http404("No video URL provided")
    
    try:
        # Fetch the video content from Instagram CDN
        response = requests.get(video_url, stream=True, timeout=15)
        response.raise_for_status()
        
        # Return the content as a downloadable file
        django_response = HttpResponse(response.content, content_type="video/mp4")
        django_response['Content-Disposition'] = 'attachment; filename="instagram_reel.mp4"'
        return django_response
    except Exception as e:
        return HttpResponse(f"Error downloading video: {str(e)}", status=500)
