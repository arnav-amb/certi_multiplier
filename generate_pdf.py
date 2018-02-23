import fpdf
names=open("names.txt","r")
x=names.read().split("\n")
# print x
for i in range(len(x)-2):
	name = x[i][:-1]
	filename=name+str(i)
	# print name
	pdffile = fpdf.FPDF()
	pdffile.compress = False
	pdffile.add_page(orientation = 'L')
	pdffile.add_font('boldfont','','bold4.otf',uni=True)
	pdffile.set_font('boldfont','',55,)
	pdffile.set_text_color(8,17,63)
	pdffile.image('certifoss.jpg',2,2,877/3,620/3)
	pdffile.ln(55)
	pdffile.cell(0,80.5,name,0,1,'C')
	try:
		pdffile.output('certipdfs/'+filename+'.pdf')
		print "made for " , name
	except:
		print "*******failed for ",name,"***********" 