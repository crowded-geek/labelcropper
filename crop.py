#!/usr/bin/env python

import sys

if __name__ == '__main__' and sys.argv[1][-3:].upper() == 'PDF':
  
  original = sys.argv[1]
  
  target = original[:-4] + '.top.cropped.pdf'
  target2 = original[:-4] + '.bottom.cropped.pdf'
  
  left     = 177
  top      = 25
  right    = 177
  bottom   = 475
  
  left2 = 0
  top2 = 372
  right2 = 0
  bottom2 = 0

  from pyPdf import PdfFileWriter, PdfFileReader
  pdf = PdfFileReader(file(original, 'rb'))
  out = PdfFileWriter()
  for page in pdf.pages:
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
    out.addPage(page)    
  ous = file(target, 'wb')
  out.write(ous)
  ous.close()

  pdf2 = PdfFileReader(file(original, 'rb'))
  out2 = PdfFileWriter()
  for page in pdf2.pages:
      page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right2, page.mediaBox.getUpperRight_y() - top2)
      page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x() + left2, page.mediaBox.getLowerLeft_y() + bottom2)
      out2.addPage(page)
  ous2 = file(target2, 'wb')
  out2.write(ous2)
  ous2.close()

else:
  print 'EXAMPLE: crop.py original.pdf'
