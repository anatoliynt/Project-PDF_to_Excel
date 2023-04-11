import tabula
import pandas as pd

pdf_one_file = "E:\Python\Project\PDF_to_Excel\original_files" \
               "\\bad_file.pdf"

tabula_pdf = tabula.read_pdf(pdf_one_file, pages='all')

csv_tabula = tabula.convert_into("E:\Python\Project\PDF_to_Excel"
                                 "\original_files\\bad_file.pdf", "out.csv",
                                 output_format="csv", pages='all', lattice=":")

new_pad = pd.DataFrame(csv_tabula)

print(new_pad)
