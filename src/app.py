from flask import Flask, json, request, Response
import requests
import socket

# Constants
HOST = '0.0.0.0'
PORT = 8080
BASE_PATH = '/python'
API_VERSION = '1.0.0'

api = Flask(__name__)

# Health check endpoint
@api.route('/health', methods=['GET'])
def get_health():
  return Response(json.dumps({
    "api": API_VERSION,
    "message": "Health OK!"
  }), mimetype='application/json')

# Network validation API
@api.route(BASE_PATH+'/network', methods=['GET'])
def get_network():
  message = 'DEFAULT'
  # try:
  #   another_service_dns = ''
  #   response = requests.get("http://"+another_service_dns+":8080/nodejs/info")
  #   address = socket.gethostbyname(another_service_dns)
  #   message = {
  #     "data": response.json(),
  #     "from": address
  #   }
  # except Exception as e:
  #   message = str(e)
  #   print(e)
  
  return Response(json.dumps({
    "api": API_VERSION,
    "message": message
  }), mimetype='application/json')

# Business APIs
# GET
@api.route(BASE_PATH+'/mock', methods=['GET'])
def get_mock():
  response = {
    "api": API_VERSION,
    "output": "GET Success!"
  }
  print(response)
  return Response(json.dumps(response), mimetype='application/json')

# POST
@api.route(BASE_PATH+'/mock', methods=['POST'])
def post_mock():
  body  = request.get_json()
  response = {
    "api": API_VERSION,
    "input": body,
    "output": "POST Success!"
  }
  print(response)
  return Response(json.dumps(response), mimetype='application/json')

# PUT
@api.route(BASE_PATH+'/mock', methods=['PUT'])
def put_mock():
  body  = request.get_json()
  response = {
    "api": API_VERSION,
    "input": body,
    "output": "PUT Success!"
  }
  print(response)
  return Response(json.dumps(response), mimetype='application/json')

# PATCH
@api.route(BASE_PATH+'/mock', methods=['PATCH'])
def patch_mock():
  body  = request.get_json()
  response = {
    "api": API_VERSION,
    "input": body,
    "output": "PATCH Success!"
  }
  print(response)
  return Response(json.dumps(response), mimetype='application/json')

# DELETE
@api.route(BASE_PATH+'/mock', methods=['DELETE'])
def delete_mock():
  body  = request.get_json()
  response = {
    "api": API_VERSION,
    "input": body,
    "output": "DELETE Success!"
  }
  print(response)
  return Response(json.dumps(response), mimetype='application/json')

if __name__ == '__main__':
    api.run(host=HOST, port=PORT)