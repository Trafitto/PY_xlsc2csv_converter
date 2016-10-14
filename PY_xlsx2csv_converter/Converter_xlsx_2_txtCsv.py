import xlrd
import csv
print"start process"
riga=''
fileName='FILENAME'
sheetName='Sheet1'
wb = xlrd.open_workbook(fileName+'.xlsx')
sh = wb.sheet_by_name(sheetName)
your_csv_file = open(fileName+'.csv', 'wb')
wr = csv.writer(your_csv_file)
for rownum in xrange(sh.nrows):
      for columnum in xrange(sh.ncols):
        riga+=(unicode(sh.cell_value(rownum,columnum)).encode('utf-8'))
      wr.writerow(riga)
      riga=''



your_csv_file.close()
print "end"
