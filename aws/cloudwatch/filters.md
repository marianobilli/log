# Filter events for https and http
```
{ $.event.tls.sni = "*" ||  $.event.http.hostname = "*" }
```
