import urllib.request, json, sys
url='http://127.0.0.1:8000/health'
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        data=json.load(r)
        print(data)
except Exception as e:
    print('Start the app first with: uvicorn app.main:app --reload')
    print(e)
    sys.exit(1)
