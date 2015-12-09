from werkzeug.wrappers import Request, Response, Headers
import requests

@Request.application
def application(request):

    serverresponse = requests.request(request.method,request.url,headers = dict(request.headers.items()))

    print len(serverresponse.content)

    clientresponse = Response(serverresponse.content)
    clientresponse.headers = Headers(serverresponse.headers.items())

    print len(clientresponse.data)

    return clientresponse

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
