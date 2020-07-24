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

  x = open(original, 'rb')
  pdf = PdfFileReader(x)
  out = PdfFileWriter()
  for page in pdf.pages:
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
    out.addPage(page)    
  ous = open("H:\\test folder\\kop\\"+target, 'wb')
  out.write(ous)
  ous.close()
  x.close()

  # A List containing the system printers
  all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
  # Ask the user to select a printer
  # printer_num = int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
  # set the default printer
  time.sleep(3)
  win32print.SetDefaultPrinter(all_printers[1])
  time.sleep(2)
  win32api.ShellExecute(0, "print", "H:\\test folder\\kop\\"+target, None,  ".",  0)

  x = open(original, 'rb')
  pdf2 = PdfFileReader(x)
  out2 = PdfFileWriter()
  for page in pdf2.pages:
      page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right2, page.mediaBox.getUpperRight_y() - top2)
      page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x() + left2, page.mediaBox.getLowerLeft_y() + bottom2)
      out2.addPage(page)
  ous2 = open("H:\\test folder\\kjop\\"+target2, 'wb')
  out2.write(ous2)
  ous2.close()
  x.close()
  
  # A List containing the system printers
  all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
  # Ask the user to select a printer
  # printer_num =int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
  # set the default printer
  time.sleep(2)
  win32print.SetDefaultPrinter(all_printers[9])
  time.sleep(2)
  win32api.ShellExecute(0, "print", "H:\\test folder\\kjop\\"+target2, None,  ".",  0)
  time.sleep(3)
  os.system("move *.pdf parent")
else:
  print('EXAMPLE: crop.py original.pdf')
