import countershape
from countershape import markup
from countershape.doc import *

this.markup = markup.Markdown( extras=["code-friendly"] )
this.titlePrefix = ns.titlePrefix + " Server - "

pages = [
            Page(
                "repository.md",
                title="Repository",
                pageTitle = "Repository"
            ),           						
        ]
        
