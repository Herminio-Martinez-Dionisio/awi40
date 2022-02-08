import json

texto ='''{
  "error": {
    "code": 400,
    "message": "EMAIL_NOT_FOUND",
    "errors": [
      {
        "message": "EMAIL_NOT_FOUND",
        "domain": "global",
        "reason": "invalid"
      }
    ]
  }
}'''

formato = json.loads(texto)
error = formato['error']
print(error['message']) 