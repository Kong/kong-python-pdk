## Get started


```
$ docker-compose up
```

```
$ curl http://localhost:8000/any -i

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 522
Connection: keep-alive
x-hello-from-python: Python says hello to localhost:8000
x-python-pid: 1341
Date: Wed, 13 Mar 2024 08:46:23 GMT
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
X-Kong-Upstream-Latency: 1665
X-Kong-Proxy-Latency: 9
Via: kong/3.6.1
X-Kong-Request-Id: 5aa07d554fdc731e708b5e5d702b1525

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/8.4.0", 
    "X-Amzn-Trace-Id": "Root=1-65f167df-79ce3037161a30a142226f60", 
    "X-Forwarded-Host": "localhost", 
    "X-Forwarded-Path": "/any", 
    "X-Forwarded-Prefix": "/any", 
    "X-Kong-Request-Id": "5aa07d554fdc731e708b5e5d702b1525"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "192.168.65.1, 210.13.68.134", 
  "url": "https://localhost/anything"
}
```

From the response headers, the `x-hello-from-python`, `x-python-pid` are injected by py-hello plugin.
