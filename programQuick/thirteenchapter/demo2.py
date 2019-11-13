import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# 1
print(pdfReader.decrypt('rosebud'))

# True
print(pdfReader.isEncrypted)

# {'/CropBox': [0, 0, 612, 792], '/Parent': IndirectObject(4, 0),
# '/Type': '/Page', '/Contents': [IndirectObject(946, 0),
# IndirectObject(947, 0), IndirectObject(948, 0), IndirectObject(949, 0),
# IndirectObject(950, 0), IndirectObject(951, 0), IndirectObject(952, 0),
# IndirectObject(953, 0)], '/Resources': {'/ExtGState':
# {'/GS0': IndirectObject(954, 0)}, '/XObject': {'/Im0': IndirectObject(955, 0)},
# '/ColorSpace': {'/CS1': IndirectObject(956, 0), '/CS2': IndirectObject(956, 0),
# '/CS0': IndirectObject(6, 0)}, '/Font': {'/TT2': IndirectObject(957, 0),
# '/TT1': IndirectObject(958, 0), '/TT0': IndirectObject(959, 0),
# '/TT5': IndirectObject(960, 0), '/TT4': IndirectObject(961, 0),
# '/TT3': IndirectObject(962, 0)}}, '/MediaBox': [0, 0, 612, 792],
# '/StructParents': 0, '/Rotate': 0}
print(pdfReader.getPage(0))
