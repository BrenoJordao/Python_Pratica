#   PRIMEIRA VEZ USANDO A BIBLIOTECA RICH
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect

print('ola [red]mundo[/] :earth_americas:')
print('ola, [bold blue on yellow]Jordan[/] :vulcan_salute: :sauropod: :t-rex: :six::seven:')

caixa = Panel('[red]apenas testando[/]', title='MIM DÊ PAPAI', style='blue', width=3)
print(caixa)

tabela = Table(title='tabela de preços')
tabela.add_column('Nome', justify='center', style='red')
tabela.add_column('Preço', justify='center', style='blue')
tabela.add_row('coco', 'R$5,50')
tabela.add_row('chocolate', 'R$7,90')

print(tabela)

inspect(print)
