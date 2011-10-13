import countershape
from countershape import Page, Directory, PythonModule, markup
from countershape.doc import *

this.layout = countershape.Layout("_layout.html")
this.markup = markup.Markdown( extras=["code-friendly"] )

ns.docTitle = "hippo"
ns.titlePrefix = "hippo "
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "aldo@corte.si"
ns.copyright = "Aldo Cortesi 2011"
ns.head = countershape.template.Template(None, "<h1> @!docTitle!@ - @!this._pageTitle!@ </h1>")

this.titlePrefix = ns.titlePrefix

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
        pageTitle="an Overview"
        ),
    Page("intro.md", 
        title="Introduction",
        pageTitle="a quick Introduction"
        ),
    Directory("intro"),
        
	Page(
		"client.md",
		title="Client",
		pageTitle = "Client Use"
	),           
    Directory("client"),

	Page(
		"server.md",
		title="Server",
		pageTitle = "Server Configuration"
	),
    Directory("server"),
	
	Page(
		"gitweb.md",
		title="Gitweb",
		pageTitle = "Gitweb Interface"
	),
    Page("admin.md", 
		title="administrivia",
		pageTitle = "About Us"
		),
    PythonModule( src="../libhippo", name= "Source", title="Source")
]
