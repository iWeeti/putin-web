from django.shortcuts import render
from blog.models import Announcement
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host='localhost')
	cur = conn.cursor()
	cur.execute('select * from profiles where id=464910064965386283;')
	record = cur.fetchone()
	context = {
		'ann': ann[0:5],
		'record': str(record)
	}
	return render(request, 'putin/home.html', context)
