import time
timestamp =time.strftime('%H:%M:%S')
#print(timestamp)
timestamp = time.strftime('%H')
# print(timestamp)
timestamp = time.strftime('%M')
# print(timestamp)
timestamp = time.strftime('%S')
# print(timestamp)

checker = int(time.strftime('%H'))
if(checker<12):
    print("😊😊😊😊😊😊😊😊😊😊😊Good Morning😊😊😊😊😊😊😊😊😊😊😊😊")
    

elif(12< checker <18):
     print("😊😊😊😊😊😊😊😊😊😊😊😊Good Afternoon😊😊😊😊😊😊😊😊😊😊😊😊")

elif(18< checker <21):
     print("😊😊😊😊😊😊😊😊😊😊😊😊Good Evening😊😊😊😊😊😊😊😊😊😊😊😊")

print()
print()
print(">>>>>>>>>>>>>>>Welcome To Our Project<<<<<<<<<<<<<<<<<<<<<<")
print()
print()
print("This Program Is Able To Do Many Operations On Pdf")
print()
print()
print("^^^^^^^^^^^^^^^^^^Hit Enter To Continue^^^^^^^^^^^^^^^^^^^")
EnterHitter = input()

print("Please Select The Operation No You Want To Perform On Pdf's ")
print()
print()
print()
print("Options Are\n1.Merge PDF\n2.Protect PDF With Password\n3.Convert PDF To Word\n4.Convert PDF To Images\n5.Change Page No In A PDF\n6.Delete Page In PDF\n7.Reverse The PDF\n8.Rotate PDF\n9.Split Each Page Of PDF Into New PDF ")
print()
print('These Are The Operations Available')
operation_No = int(input("Enter The Operation No You Want To Perform :"))

match(operation_No):
    case 1:
        from glob import glob
        from pikepdf import Pdf
        print("Note : This Operation Work Only When PDF Files Are Available In This Folder\n\n\n\n       >>It Will Merge All PDF Present In Ths Folder<<")
        print()
        print()
        nameofpdf = input('Enter The Name For Final Merged PDF :')
        new_pdf = Pdf.new()

        for files in glob("*.pdf"):
            old_pdf = Pdf.open(files)
            new_pdf.pages.extend(old_pdf.pages)

            new_pdf.save(f"{nameofpdf}.pdf")
        
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 2:
        import pikepdf

        print("Note : This Operation Will Protect Your PDF With Password\n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")

        path = input("Please Paste The Relative Path Of PDF You Want To Protect Here : 👉👉👉")
        password = input("Enter The Password You Want To Set 🔏:")
        nameofpdf = input('Enter The Name For Protected PDF :')
        old_pdf = pikepdf.Pdf.open(f"{path}")

        no_extract = pikepdf.Permissions(extract=False)

        old_pdf.save(f"{nameofpdf}.pdf",encryption=pikepdf.Encryption(user=password,owner="Yash Maske",allow=no_extract))

        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 3:
        from pdf2docx import Converter
        print("Note : This Operation Will Convert Your PDF Into Word File \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF You Want To Convert Here : 👉👉👉")
        nameofdoc = input('Enter The Name For Word File :')
        old_pdf = path
        new_doc = f"{nameofdoc}.docx"

        obj = Converter(old_pdf)
        obj.convert(new_doc)
        obj.close()
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 4:
        from pdf2image import convert_from_path
        print("Note : This Operation Will Convert Your PDF Into Images \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF You Want To Convert Here : 👉👉👉")
        name = input("Enter The Name For Image :")
        old_pdf = convert_from_path(path,poppler_path=r"C:\Programs\Python\Mini Project Shreya Bedre\Release-24.02.0-0\poppler-24.02.0\Library\bin")
       
        for i in range(len(old_pdf)):
            old_pdf[i].save(f"{name}{i}.jpg","JPEG")
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 5:
        import pikepdf
        print("Note : This Operation Will Change The Page No In Provided PDF \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF Here : 👉👉👉 ")
        old_pdf = pikepdf.Pdf.open(path)
        oldNo = int(input("Enter The Current Page Number : "))
        newNo = int(input("Enter The Page No You Want To Set For The Page You Entered Above :"))
        nameofpdf = input('Enter The Name For New Updated PDF :')

        # old_pdf.pages[oldNo-1] = old_pdf.pages[newNo-1]
        pagetemp = old_pdf.pages[oldNo-1]
        old_pdf.pages[oldNo-1] = old_pdf.pages[newNo-1]
        old_pdf.pages[newNo-1] = pagetemp
        

        old_pdf.save(f"{nameofpdf}.pdf")
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 6:
        import pikepdf
        print("Note : This Operation Will Delete The Entered Page Number Page In The PDF Provied \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF Here : 👉👉👉 ")
        old_pdf = pikepdf.Pdf.open(path)
        RangeStaart = int(input("Enter The Page No From Which You Want To Delete The Page :"))
        RangeEnd = int(input("Enter The Page No Upto  Which You Want To Delete The Page :"))
        nameofpdf = input('Enter The Name For New Updated PDF :')

        del old_pdf.pages[RangeStaart-1:RangeEnd-1]
        

        old_pdf.save(f"{nameofpdf}.pdf")
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
        
    case 7:
        import pikepdf
        print("Note : This Operation Will Reverse The Pages Order In PDF Provided \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF Here : 👉👉👉 ")
        nameofpdf = input('Enter The Name For New Updated PDF :')
        old_pdf = pikepdf.Pdf.open(path)

        old_pdf.pages.reverse()
        
        old_pdf.save(f"{nameofpdf}.pdf")
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 8:
        import pikepdf
        print("Note : This Operation Will Rotate The Pages Of PDF Provided By The Angle You Entered \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF Here : 👉👉👉 ")
        Angle = int(input("Enter The Angle In Degree By Which You Want To Rotate The PDF : "))
        nameofpdf = input('Enter The Name For New Updated PDF :')
        old_pdf = pikepdf.Pdf.open(path)

        #print(pdf_my.pages)
        for i in old_pdf.pages:
            i.rotate(Angle,True)
        old_pdf.save(f"{nameofpdf}.pdf")
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    case 9:
        import pikepdf
        print("Note : This Operation Will Split Each And Every Page Of The PDF Provided Into A New PDF \n\n\n\n       >>It Requires The Relative Path Of The PDF<<\n\n\n")
        path = input("Please Paste The Relative Path Of PDF Here : 👉👉👉 ")
        nameofpdf = input('Enter The Name For New Updated PDF :')
        old_pdf = pikepdf.Pdf.open(path)

        for n,pag_cnt in enumerate(old_pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(pag_cnt)
            name = nameofpdf + str(n+1) + ".pdf"
            new_pdf.save(name)
        print("←←←←←←←←←Your Operation Is Successfull→→→→→→→→→→")
    
