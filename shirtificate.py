from fpdf import FPDF

pdf = FPDF()
name = input("Name: ")
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.set_font("helvetica", "", 48)
pdf.cell(text="CS50 Shirtificate", center=True)

pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", "", 24)
pdf.image("shirtificate.png", 10, 48, 190, 190)
pdf.cell(h=200, text=f"{name} took CS50", center=True)

pdf.output("shirtificate.pdf")
