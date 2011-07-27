import countershape
from countershape import markup
from countershape.doc import *

this.markup = markup.Markdown( extras=["code-friendly"] )

pages = [
            Page(
                "install.md",
                title="Install",
                pageTitle = "Installation"
            ),           

            Page(
                "client.md",
                title="Client",
                pageTitle = "Client Use"
            ),           

            Page(
                "server.md",
                title="Server",
                pageTitle = "Server Configuration"
            ),
			
            Page(
                "gitweb.md",
                title="Gitweb",
                pageTitle = "Gitweb Interface"
            ),
						
        ]
        
