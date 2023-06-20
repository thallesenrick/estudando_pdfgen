from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (Flowable, Paragraph,
                                SimpleDocTemplate, Spacer)
from reportlab.lib.colors import Color, magenta

class MCLine(Flowable):
    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def __repr__(self):
        return "Line(w=%s)" % self.width

    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)


def create_pdf():
    story = []
    doc = SimpleDocTemplate("hello.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    spacer = Spacer(0, 0.25 * inch)

    styles.add(ParagraphStyle(
        name='teste',
        textColor=magenta
    ))

    ptext = '<span>%s</span>' % "Section #1"
    story.append(Paragraph(ptext, styles["teste"]))
    story.append(spacer)

    line = MCLine(500)
    story.append(line)
    story.append(spacer)

    ptext = '<span>%s</span>' % "Section #2"
    story.append(Paragraph(ptext, styles["Heading1"]))

    doc.build(story)


if __name__ == "__main__":
    create_pdf()
