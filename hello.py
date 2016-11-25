def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),)]

# def app(environ, start_responce):
#     status = '200 OK'
#     headers = [('Content-Type', 'text/plain')]
#     body = '\r\n'.join(env['QUERY_STRING'].split('&'))
#     start_responce(status, headers)
#     return body