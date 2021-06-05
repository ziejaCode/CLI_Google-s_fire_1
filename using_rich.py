from rich.console import Console
from rich import print
from rich.markdown import Markdown

console = Console()

console.print("cos")

console.log()

# Test/Color
console.print('Hello world', style='bold red')
console.print("[u]Hello[/u] [bold cyan]wordls[bold /cyan]")

print('test [bold magenta]rich[/bold magenta]')

console.print("I :heart: coding :smiley:")

# markdown
with open("RD.docx") as md:
    markdown = Markdown(md.read())
    console.print(markdown)




