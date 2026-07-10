import camelot
import pandas as pd

# Extract tables (lattice for gridlines, stream for whitespace)
tables = camelot.read_pdf('example.pdf', flavor='lattice')

# Convert first table to DataFrame
df = tables[0].df
df = pd.DataFrame(df)