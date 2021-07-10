import tornado.ioloop
import tornado.web
import os
from io import StringIO

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        uri = self.request.uri.replace("/", "")
        dyn_sites, sites = os.listdir("sites/html"), os.listdir("sites/html")
        dyn_sites.remove('index.html')
        dyn_sites.remove('404.html')

        if uri == "":
            uri = "index.html"


        html_inject = []
        for dyn_uri in dyn_sites:
            html_inject.append(f'<a href="{dyn_uri}">{dyn_uri.replace(".html", "")}</a>')


        if len(dyn_sites) > 0 and uri == "index.html":
            with open('sites/html/index.html', 'r') as file:
                index_html = StringIO(file.read())
                file.close()
            html = index_html.getvalue().splitlines()

            strio_out = StringIO()
            for line in html:
                out = ""
                for l in (ele for ele in reversed(html_inject)):
                    out += l + "\n"
                line=line.replace("<!--here-->", out)
                strio_out.write(line)

            self.write(strio_out.getvalue())
            strio_out.close()
            return
        else:
            if uri in sites:
                self.render(f"sites/html/{uri}")
            else:   #if site not found
                self.render("sites/html/404.html")



def main():
    return tornado.web.Application(static_path="sites/css",
    default_handler_class=indexHandler)

if __name__ == "__main__":
    app = main()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
