from django.shortcuts import render
import requests

def passthrough(request):
    print("hi")
    inresponse = requests.request(
        request.method,
        request.build_absolute_uri(),
        headers=request.META,
        data = request.body)

    outresponse = HttpResponse(
        content = response.content,
        content_type = response.headers["content-type"],
        status = response.status_code,
        reason = response.reason,
        )
    for itempair in inresponse.iteritems():
        outresponse[itempair[0]] = itempair[1]

    return outresponse
