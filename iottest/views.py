from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json,datetime 

# Create your views here.

def keyboard(request):

	return JsonResponse({
	'type' : 'buttons',
  	'buttons': ['카메라','온도','습도']
})


@csrf_exempt

def answer(request):
	  json_str=((request.body).decode('utf-8'))
	  recieved_json_data=json.loads(json_str)
	  iot_name=recieved_json_data['content']
	  today_date=datetime.date.today().strftime("%m 월 %d 일")

	  return JsonResponse({

	  'message': {
	   'text': today_date + '의' + iot_name + '입니다.'
	  },

	'keyboard':{
		'type':'buttons',
		'buttons':['카메라','온도','습도']
	}
	  })
