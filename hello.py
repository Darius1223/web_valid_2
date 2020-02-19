def app(env, start_response):
	data = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	start_response("200 OK", [("Content-type", "text/plain")])
	return data
