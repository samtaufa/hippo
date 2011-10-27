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

def Image(imagefile, title=None, basepath=None, klass=None, kaption=None):
        defaultpath="media/"

        if basepath is None:
            src = """src="%s" """ % model.UrlTo(imagefile)
        else:
            src = """src="%s" """ % model.UrlTo(os.path.join(defaultpath, imagefile))

        if title is None:
            title=""
        else:
            title=""" title="%s" """ % title
        
        image = """<img %s%s>""" % (src, title)
        
        if klass is None:
            klass =""
        else:
            klass=""" class="%s" """ % klass            
        
        if kaption is None:
            kaption = ""
        else:
            kaption ="""<p %s>
    %s 
</p>""" % (klass, kaption)

        url = image
        if not klass == "" or not kaption == "":
            url="""
<div %s>
    %s
    %s
</div>
""" % (klass, image, kaption)

        return url
            
ns.Image = Image

pages = [
    Page("index.md", 
        title="Overview",
        pageTitle="an Overview"
        ),
    Page("install.md", 
        title="Install",
        pageTitle="a quick Install"
        ),
    Directory("install"),
        
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
