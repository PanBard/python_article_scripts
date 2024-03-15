# from fpdf import FPDF

# name = "elo"

# pdf = FPDF()

# pdf.add_page()
# pdf.set_font('Times','B',12)
# pdf.cell(40,10,f"no siema {name}")
# pdf.output("test.pdf",'F')

from fpdf import FPDF
import datetime
class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('graphs/Data1_f1.jpg', 10, 8, 33,link="https://google.com")
        # Arial bold 15
        self.set_font('Times', 'B', 12)
        # Move to the right
        # self.cell(80)
        # Title
        # self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        # Page number
        self.cell(-50, 20, 'Generated ' + str(datetime.datetime.now()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
# pdf.cell(80)
pdf.cell(100, 30, 'Information scheet about data', 1, 1,'C')
pdf.ln(20)
pdf.cell(1,1,'rr')
for i in range(1, 10):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto2.pdf', 'F')