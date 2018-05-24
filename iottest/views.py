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
	  today_date=datetime.date.today().strftime("%m월 %d일 %h시 %m분 ")

	  return JsonResponse({

	  'message': {

	   'text': today_date + '의' + iot_name + '입니다.' +get_result (iot_name)
	  },


	'keyboard': {
		'type':'buttons',
		'buttons':['카메라','온도','습도']
	 }
	  })


def temperature(temperature):
	global global_temperature
	global_temperature=100

def humidity(humidity):
	
	return "50"


def get_result(iot_name):
	if iot_name =='온도': 
		return "현재온도: %.2f" % global_temperature
	elif iot_name =='습도':
		return "현재습도" + humidity(humidity)
	else : 
		return "현재준비중입니다. "

      
   
