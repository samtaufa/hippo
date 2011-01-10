import countershape
from countershape import Page, Directory, PythonModule, markup
import countershape.grok


this.layout = countershape.Layout("_layout.html")
this.markup = markup.Markdown()
ns.docTitle = "hippo"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "aldo@corte.si"
ns.copyright = "Aldo Cortesi 2011"
ns.head = countershape.template.Template(None, "<h1> @!docTitle!@ - @!this.title!@ </h1>")
ns.sidebar = countershape.widgets.SiblingPageIndex(
            '/index.html',
            exclude=['countershape']
          )

ns.license = file("../LICENSE").read()
ns.index_contents = file("../README").read()

pages = [
    Page("index.html", "introduction"),
    Page("admin.html", "administrivia")
]
