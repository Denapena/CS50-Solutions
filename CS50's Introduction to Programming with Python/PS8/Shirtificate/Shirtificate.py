from fpdf import FPDF

name = input("Your name and surname: ")

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(0, 0, 0)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

    def background(self):
        self.image("shirtificate.png", x=10, y=30, w=190)

pdf = PDF()
pdf.add_page()
pdf.background()

pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(255, 255, 255)

pdf.text(x=70, y=120, txt=name+" took CS50")

pdf.output("shirtificate.pdf")
