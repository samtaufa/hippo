import countershape
from countershape import Page, Directory, PythonModule, markup
from countershape.doc import *

this.layout = countershape.Layout("_layout.html")
this.markup = markup.Markdown( extras=["code-friendly"] )

ns.docTitle = "hippo"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "aldo@corte.si"
ns.copyright = "Aldo Cortesi 2011"
ns.head = countershape.template.Template(None, "<h1> @!docTitle!@ - @!this.title!@ </h1>")

this.stdHeaders = [
    model.UrlTo("media/css/reset-fonts-grids-base.css"),
    model.UrlTo("media/css/docstyle-default.css"),
    model.UrlTo("media/css/docstyle-customised.css"),
    model.UrlTo("media/css/syntax.css"),
]
this.metadata = {
    "robots":"all",
    "keywords":"countershape,website generator,website compiler",
    "description":"Countershape website generator",
    "copyright":"(c) Copyright Nullcube 2007"
}

ns.sidebar = countershape.widgets.SiblingPageIndex(
            '/index.html',
            exclude=['countershape']
          )

ns.license = file("../LICENSE").read()
ns.index_contents = file("../README.md").read()

pages = [
    Page("index.md", 
        title="Overview",
        pageTitle="Hippo: an Overview"
        ),
    Page("intro.md", 
        title="Introduction",
        pageTitle="Hippo: a quick Introduction"
        ),
	
    Directory("intro"),
        
    Page("admin.md", "administrivia"),
    PythonModule( src="../libhippo", name= "Source", title="Source")
]
