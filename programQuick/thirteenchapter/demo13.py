import docx
from docx.shared import Inches,Cm

doc = docx.Document()
doc.add_picture('zophie.png', width=Inches(1), height=Cm(4))
