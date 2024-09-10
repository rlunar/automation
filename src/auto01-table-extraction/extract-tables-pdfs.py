import camelot
import os
from rich.pretty import pprint

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Set the prefix to the current directory path
prefix = current_dir
pprint(f"The prefix is set to: {prefix}")

tables = camelot.read_pdf(f"{prefix}/foo.pdf", pages='1')
pprint(tables)

tables.export(f"{prefix}/foo.csv", f='csv', compress=True)
tables[0].to_csv(f"{prefix}/foo.csv")  # to a csv file
pprint(tables[0].df)  # to a df