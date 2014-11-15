from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from calc.models import Calc
from calc.serializers import CalcSerializer

class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSON.
  """
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def calc_list(request):
  """
  List all calcs, or create a new calc.
  """
  if request.method == 'GET':
    calcs = Calc.objects.all()
    serializer = CalcSerializer(calcs, many=True)
    return JSONResponse(serializer.data)


@csrf_exempt
def calc_detail(request, number):
  """
  Retrieve, update or delete a calc.
  """
  try:
    calc = Calc.objects.get(pk=number)
  except Calc.DoesNotExist:
    print "Does not exists so we create it %s" % number
    calc = Calc(number=int(number)) 
    calc.save()

  if request.method == 'GET':
    serializer = CalcSerializer(calc)
    return JSONResponse(serializer.data)

  elif request.method == 'PUT':
    #data = JSONParser().parse(request)
    data = CalcSerializer(calc).data
    serializer = CalcSerializer(calc, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    calc.delete()
    return HttpResponse(status=204)



