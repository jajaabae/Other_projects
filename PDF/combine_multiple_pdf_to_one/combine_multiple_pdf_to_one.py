import os
from m.settings import Settings
from pyPdf import PdfFileWriter, PdfFileReader

def print_content(path):
    for e in os.listdir(path):
        print e

def example_from_www():
    # Loading the pyPdf Library
    #from pyPdf import PdfFileWriter, PdfFileReader

    # Creating a routine that appends files to the output file
    #def append_pdf(input,output):
    #    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

    # Creating an object where pdf pages are appended to
    output = PdfFileWriter()

    # Appending two pdf-pages from two different files
    append_pdf(PdfFileReader(open("SamplePage1.pdf","rb")),output)
    append_pdf(PdfFileReader(open("SamplePage2.pdf","rb")),output)

    # Writing all the collected pages to a file
    output.write(open("CombinedPages.pdf","wb"))

def combining_PDFs(fip_list, out_path):
    def append_pdf(input,output):
        [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

    output = PdfFileWriter()
    for f in fip_list:
        print f
        append_pdf(PdfFileReader(open(f,"rb")),output)
    out_name = out_path+'/'+"CombinedPages.pdf"
    output.write(open(out_name,"wb"))

def main():
    path = os.getcwd()
    settings = Settings(path)
    work_path = settings.work_path.replace('\\','/')
    #print_content(work_path)
    if settings.specify_files == 'True':
        files = settings.files
        files_list = files.split('; ')
    else:
        files_list = [f for f in os.listdir(work_path) if f[-4:].lower()=='.pdf']
    fip_list = [work_path+'/'+f for f in files_list]
    combining_PDFs(fip_list, work_path)

if __name__ == '__main__':
    main()
