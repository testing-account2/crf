import sys
sys.path
#sys.path.append(" ")

import PyPDF2, traceback

src = 'acrf.pdf'
 
input1 = PyPDF2.PdfFileReader(open(src, "rb"))
nPages = input1.getNumPages()

for i in range(nPages) :
        page0 = input1.getPage(i)
        try :
            for annot in page0['/Annots'] :
                print (annot.getObject())       # (1)
                print ('')
        except : 
        # there are no annotations on this page
            pass
    
print(npages) 
