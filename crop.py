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
  import win32print, win32api

  pdf = PdfFileReader(open(original, 'rb'))
  out = PdfFileWriter()
  for page in pdf.pages:
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
    page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
    out.addPage(page)    
  ous = open(target, 'wb')
  out.write(ous)
  ous.close()

  printdefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS} # Doesn't work with PRINTER_ACCESS_USE
  handle = win32print.OpenPrinter("TSC TTP-244 Pro", printdefaults)
  level = 2
  attributes = win32print.GetPrinter(handle, level)
  attributes['pDevMode'].Duplex = 3   #flip over
  win32print.SetPrinter(handle, level, attributes, 0)
  win32print.GetPrinter(handle, level)['pDevMode'].Duplex
  win32api.ShellExecute(0,'print',target,'.','.',0)

  pdf2 = PdfFileReader(open(original, 'rb'))
  out2 = PdfFileWriter()
  for page in pdf2.pages:
      page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right2, page.mediaBox.getUpperRight_y() - top2)
      page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x() + left2, page.mediaBox.getLowerLeft_y() + bottom2)
      out2.addPage(page)
  ous2 = open(target2, 'wb')
  out2.write(ous2)
  ous2.close()

  printdefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS} # Doesn't work with PRINTER_ACCESS_USE
  handle = win32print.OpenPrinter("EPSON L3150 Series", printdefaults)
  level = 2
  attributes = win32print.GetPrinter(handle, level)
  attributes['pDevMode'].Duplex = 3   #flip over
  win32print.SetPrinter(handle, level, attributes, 0)
  win32print.GetPrinter(handle, level)['pDevMode'].Duplex
  win32api.ShellExecute(0,'print',target2,'.','.',0)

else:
  print('EXAMPLE: crop.py original.pdf')
