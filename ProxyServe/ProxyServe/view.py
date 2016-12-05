from django.http import HttpResponse
from ipware.ip import get_trusted_ip

def hello(request):
	ip = get_trusted_ip(request, trusted_proxies=['23.91.45.15'])
	if ip is not None:
		print("we got user's real IP address from a known proxy")
	else:
		print("request wasn't from a unknown proxy. Not a trusted IP.")

	msg=request.META
	if request.META.has_key('HTTP_X_FORWARDED_FOR'):
		ip =  request.META['HTTP_X_FORWARDED_FOR']
	else:
		ip = request.META['REMOTE_ADDR']
	print ip
	print msg

	return HttpResponse("hello")
