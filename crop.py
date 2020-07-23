#!/usr/bin/env python

import sys

if __name__ == '__main__' and sys.argv[1][-3:].upper() == 'PDF':
  
  original = sys.argv[1]
  
  target = original[:-4] + '.top.cropped.pdf'
  target2 = original[:-4] + '.bottom.cropped.pdf'
  
  left     = 175
  top      = 25
  right    = 175
  bottom   = 475
  
  left2 = 0
  top2 = 372
  right2 = 0
  bottom2 = 0

  from PyPDF2 import PdfFileWriter, PdfFileReader
  import os
  import time
  import win32print, win32api, glob

  pdf = PdfFileReader(open(original, 'rb'))
  out = PdfFileWriter()
  for page in pdf.pages:
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
    out.addPage(page)    
  ous = open(target, 'wb')
  out.write(ous)
  ous.close()

  # A List containing the system printers
  all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
  # Ask the user to select a printer
  #printer_num = int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
  # set the default printer
  win32print.SetDefaultPrinter(all_printers[1])
  win32api.ShellExecute(0, "print", target, None,  ".",  0)

  pdf2 = PdfFileReader(open(original, 'rb'))
  out2 = PdfFileWriter()
  for page in pdf2.pages:
      page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right2, page.mediaBox.getUpperRight_y() - top2)
      page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x() + left2, page.mediaBox.getLowerLeft_y() + bottom2)
      out2.addPage(page)
  ous2 = open(target2, 'wb')
  out2.write(ous2)
  ous2.close()

  # A List containing the system printers
  all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
  # Ask the user to select a printer
  #printer_num = int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
  # set the default printer
  win32print.SetDefaultPrinter(all_printers[9])
  win32api.ShellExecute(0, "print", target2, None,  ".",  0)
 
else:
  print('EXAMPLE: crop.py original.pdf')
