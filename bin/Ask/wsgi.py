
##gunicorn -b 127.0.0.1:8081 wsgi:app

import cgi

form = b'''
    <html>
    <head>
    <title>Hello User!</title>
    </head>
    <body>
    <p>Hello,word :)
    </br>
    <form method="post">
    <label>Post</label>
    <input type="text" name="name">
    <input type="submit" value="Go">
    </form>
    </br>
    <form method="get">
    <label>Get</label>
    <input type="text" name="name">
    <input type="submit" value="Go">
    </form>

    </body>
    </html>
    '''

def app(environ, start_response):
    html = form
    
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        html = b'Post ' + post['name'].value + '!'
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

    if environ['REQUEST_METHOD'] == 'GET':
        get_env = environ.copy()
        get_env['QUERY_STRING'] = ''
        get = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=get_env,
                                keep_blank_values=True
                                )
        html = b'Get ' + get['name'].value + '!'
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
