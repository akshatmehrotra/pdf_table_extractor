import camelot

# PDF file to extract tables from
file = "foo.pdf"
tables = camelot.read_pdf(file)
# extract all the tables in the PDF file
tables = camelot.read_pdf(file)
# number of tables extracted
print("Total tables extracted:", tables.n)
