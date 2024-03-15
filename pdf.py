from fpdf import FPDF
import datetime
import json
from types import SimpleNamespace


with open('all_artcles.json', encoding="utf8") as file: 
    data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))



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
        # self.ln(20)

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
# pdf.cell(100, 30, 'Information scheet about data', 1, 1,'C')
# pdf.ln(20)
i=4
pdf.cell(0, 10, f'ID: {data[i].FileName} ', 0, 1)
pdf.cell(0, 10, f'Title: {data[i].PrimaryTitle} ', 0, 1)
pdf.cell(0, 10, f'Authors: {data[i].Autors} ', 0, 1)
pdf.cell(0, 10, f'DOI: {data[i].DOI} ', 0, 1, link=f"{data[i].DOI}")
pdf.cell(0, 10, f'PublicationYear: {data[i].PublicationYear} ', 0, 1)
pdf.cell(0, 10, f'Type: {data[i].Type} ', 0, 1)

pdf.cell(0, 40, f'Figure {data[i].Graphs[0].Isotherms[0].FigureNumber} ', 0, 1)
pdf.image('oryginal_images/Data5_f2_1.jpg', 10, 100, 70 )
pdf.image('synthesized_graphs/Data5_f2_1.jpg', 100, 100, 100)

pdf.cell(0, 160, f'Figure {data[i].Graphs[1].Isotherms[0].FigureNumber} ', 0, 1)
pdf.image('oryginal_images/Data5_f2_2.jpg', 10, 200, 70 )
pdf.image('synthesized_graphs/Data5_f2_2.jpg', 100, 200, 100)

pdf.add_page()

pdf.cell(0, 20, f'Figure {data[i].Graphs[2].Isotherms[0].FigureNumber} ', 0, 1)
pdf.image('oryginal_images/Data5_f5_1.jpg', 10, 30, 70 )
pdf.image('synthesized_graphs/Data5_f5_1.jpg', 100, 30, 100)

pdf.cell(0, 170, f'Figure {data[i].Graphs[3].Isotherms[0].FigureNumber} ', 0, 1)
pdf.image('oryginal_images/Data5_f5_2.jpg', 10, 120, 70 )
pdf.image('synthesized_graphs/Data5_f2_2.jpg', 100, 120, 100)

pdf.add_page()

pdf.image('myDemo.jpg', 10, 50, 60)

pdf.output('tuto2.pdf', 'F')