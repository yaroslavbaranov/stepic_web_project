# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                   encoding="utf8")]

from cgi import parse_qs


def application(environ, start_response):
    queryString = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = ''
    print(queryString)
    for key, value in queryString.items():
        for element in value:
            body += key + '='
            body += element + '\r\n'

    print(body)

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, response_headers)

    return [body]