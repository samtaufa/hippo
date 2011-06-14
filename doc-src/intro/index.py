import countershape
from countershape import markup
from countershape.doc import *

this.markup = markup.Markdown(extras=["code-friendly"])

pages = [
            Page(
                "install.md",
                title="Install",
                pageTitle = "Installation"
            ),           

            Page(
                "usage.md",
                title="Usage",
                pageTitle = "Usage"
            ),           

            Page(
                "config.md",
                title="Config",
                pageTitle = "Path Config"
            ),
        ]
        
