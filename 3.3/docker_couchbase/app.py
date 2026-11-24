import subprocess,os,json,time,secrets,threading,base64,urllib.request,urllib.parse
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
STATE={'ready':False,'stage':'Starting Couchbase Server'}
PASSWORD=secrets.token_hex(24)
def request(path,form=None,auth=False):
 data=urllib.parse.urlencode(form).encode() if form is not None else None
 headers={}
 if auth:headers['Authorization']='Basic '+base64.b64encode(('student:'+PASSWORD).encode()).decode()
 req=urllib.request.Request('http://127.0.0.1:8091'+path,data=data,headers=headers)
 with urllib.request.urlopen(req,timeout=20) as r:
  value=r.read().decode()
  try:return json.loads(value)
  except ValueError:return value
def initialise():
 try:
  subprocess.Popen(['/entrypoint.sh','couchbase-server'])
  for n in range(180):
   try:request('/pools');break
   except Exception:time.sleep(2)
  else:raise RuntimeError('Couchbase REST API did not start')
  STATE['stage']='Initialising real Couchbase data service'
  request('/node/controller/setupServices',{'services':'kv'})
  request('/pools/default',{'memoryQuota':256})
  request('/settings/web',{'username':'student','password':PASSWORD,'port':8091})
  request('/pools/default/buckets',{'name':'practice','bucketType':'couchbase','ramQuotaMB':128,'replicaNumber':0,'flushEnabled':0},True)
  value={'student':'Maxim Kuznetsov','group':'IKBO-15-25','message':'Document stored in a real Couchbase bucket'}
  for n in range(90):
   try:
    request('/pools/default/buckets/practice/docs/demo',{'value':json.dumps(value),'flags':0},True)
    saved=request('/pools/default/buckets/practice/docs/demo',auth=True)
    STATE.update(ready=True,stage='Document written and read from Couchbase Server',document=saved)
    print('PASS: document written and read from actual Couchbase Server',flush=True);return
   except Exception as e:
    if n==89:raise
    time.sleep(2)
 except Exception as e:
  STATE.update(stage='Startup failed: '+str(e));print(STATE['stage'],flush=True)
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path=='/api':body=json.dumps(STATE,ensure_ascii=False,default=str);kind='application/json; charset=utf-8'
  else:body='<!doctype html><meta charset="utf-8"><h1>Couchbase Server — практика 3.3</h1><p>Кузнецов М.Д., ИКБО-15-25</p><p>'+STATE['stage']+'</p><pre>'+json.dumps(STATE.get('document',{}),ensure_ascii=False,indent=2)+'</pre><p><a href="/api">Результат проверки в JSON</a></p>';kind='text/html; charset=utf-8'
  data=body.encode();self.send_response(200 if STATE['ready'] else 503);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
threading.Thread(target=initialise,daemon=True).start()
ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','10000'))),Handler).serve_forever()
