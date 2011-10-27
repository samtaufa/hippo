import countershape
from countershape import markup
from countershape.doc import *

this.markup = markup.Markdown( extras=["code-friendly"] )

pages = [
            Page(
                "dependencies.md",
                title="Dependencies",
                pageTitle = "Install Dependencies"
            ),
            
            Page(
                "hippo.md",
                title="Hippo",
                pageTitle = "Install Hippo"
            ),
    ]
        
