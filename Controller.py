import web


urls = (
    '/', 'index'
)

render = web.template.render('Views/Templates/', base="MainLayout")
app = web.application(urls, globals())


class index:
    def GET(self):
        return render.Home()


if __name__ == '__main__':
    app.run()
