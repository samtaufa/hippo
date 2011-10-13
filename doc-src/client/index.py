import countershape
from countershape import markup
from countershape.doc import *

this.markup = markup.Markdown( extras=["code-friendly"] )
this.titlePrefix = ns.titlePrefix + " Client - "

pages = [
		Page(
			"workflow.md",
			title="Workflow",
			pageTitle = "Basic Workflow"
		),           						

		Page(
			"shortcuts.md",
			title="Shortcuts",
			pageTitle = "Connectivity Shortcuts"
		),           						

		Page(
			"bastion.md",
			title="Bastion",
			pageTitle = "Bastion Passthrough"
		),           						
		
		Page(
			"git.md",
			title="GIT",
			pageTitle = "GIT is the Core"
		),           						
		
		Page(
			"restore.md",
			title="Restore",
			pageTitle = "Restore"
		),           						
			
	]
        
