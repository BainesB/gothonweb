import web

render = web.template.render('templates/')

urls = ( 
	'/(.*)', 'index'
)

class index:
		
	def GET(self,name):
		
		return render.index(name) # this is what u are working on.
		
if __name__ == "__main__":

	app = web.application(urls, globals())
	app.run()
	