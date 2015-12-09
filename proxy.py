from werkzeug.wrappers import Request, Response, Headers
import requests
import gzip
import StringIO

def compress(content):

    filebuff = StringIO.StringIO()

    with gzip.GzipFile(mode='wb', fileobj=filebuff) as zipfile:
        zipfile.write(content)

    return filebuff.getvalue()


@Request.application
def application(request):

    serverresponse = requests.request(request.method,request.url,headers = dict(request.headers.items()))

    responsecontent = serverresponse.content

    if serverresponse.headers.get("content-encoding") == "gzip":
        responsecontent = compress(responsecontent)

    clientresponse = Response(responsecontent)
    clientresponse.headers = Headers(serverresponse.headers.items())

    return clientresponse

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
