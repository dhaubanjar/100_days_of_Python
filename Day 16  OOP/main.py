from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

table = PrettyTable()
table.add_column("United States of America", ["Texas", "Colorado", "Kansas", "California"])
table.add_column("Mexico", ["Guadalajara", "Cancun", "Bhaktapur", "Kathmandu"])
table.align = "l"
tab = ColorTable(theme=Themes.OCEAN)
print(tab)
print(table)