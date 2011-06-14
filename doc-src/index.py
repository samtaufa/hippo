import countershape
from countershape import Page, Directory, PythonModule, markup

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
ns.index_contents = file("../README.md").read()

pages = [
    Page("index.md", 
        title="Introduction",
        pageTitle="Introduction to Hippo"
        ),
    Directory("intro"),
        
    Page("admin.md", "administrivia"),
    PythonModule( src="../libhippo", name= "Source", title="Source")
]
