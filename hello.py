def app(env, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/html')]
  body = env['QUERY_STRING'].replace('&', '\n')
  start_response(status, headers)
  return [body]
