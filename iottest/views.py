from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def keyboard(request):

	return JsonResponse({
	'type' : 'buttons',
  	'buttons': ['카메라','온도','습도']
})

@csrf_exempt

def anser(request):
	  json_str=((request.body).decode('utf-8'))
	  recieved_json_data=json.loads(json_str)
	  iot_name=received_json_data['content']
	  today_date=datetime.date.today().strftime("% dnjf  %d  dlf ")

	  return JsonResponse({

	  'message': {
	  						'text': today_dat + 'dml' + iot_name + 'wndtldlqslek. '
	  }
	  })
