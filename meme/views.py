from django.http import HttpResponse

def meme(request):
	return HttpResponse('{\"meme\": \"meme\"}')
