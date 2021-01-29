import web


urls = (
    '/', 'index'
)

render = web.template.render('Views/Templates/')
app = web.application(urls, globals())


class index:
    def GET(self):
        return render.home()


if __name__ == '__main__':
    app.run()
