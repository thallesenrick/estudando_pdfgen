def hello(c):
    c.drawString(10, 10, 'k')


def create_document():
    styles = getSampleStyleSheet()
    F = 1
    styles.add(ParagraphStyle(
        name='teste',
        alignment=1,
        allowOrphans=0,
        allowWidows=1,
        backColor=yellow,
        borderColor=black,
        borderPadding=0,
        borderRadius=None,
        borderWidth=1,
        bulletFontName='Helvetica',
        bulletFontSize=10,
        bulletIndent=0,
        embeddedHyphenation=1,
        endDots=None,
        firstLineIndent=0,
        fontName='Helvetica',
        fontSize=10,
        hyphenationLang='en_GB',
        justifyBreaks=0,
        justifyLastLine=0,
        leading=12,
        leftIndent=36,
        linkUnderline=0,
        rightIndent=24,
        spaceAfter=0,
        spaceBefore=0,
        spaceShrinkage=0.05,
        splitLongWords=2,
        strikeColor=None,
        strikeGap=1,
        strikeOffset=0.25 * F,
        textColor=Color(0, 0, 0, 1),
        textTransform=None,
        underlineColor=None,
        underlineGap=1,
        underlineOffset=-0.125 * F,
        uriWasteReduce=0.3,
        wordWrap=None,
    ))

    styleN = styles['Normal']
    styleH = styles['Heading1']
    styleP = styles['Heading2']
    styleK = styles['Code']
    styleG = styles['Heading6']

    story = []
    story.append(Paragraph('''You are hereby charged that on the
                           28th day of May, 1970, you did willfully''',
                           styles['teste']))

    story.append(Paragraph('''You are hereby charged that on the
                           28th day of May, 1970, you did willfully''',
                           styleH))

    story.append(Paragraph('''You are hereby charged that on the
                               28th day of May, 1970, you did willfully''',
                           styleN))

    story.append(Paragraph('''You are hereby charged that on the
                                   28th day of May, 1970, you did willfully''',
                           styleP))

    story.append(Paragraph('''You are hereby charged that on the
                                       28th day of May, 1970, you did willfully''',
                           styleK))

    story.append(Paragraph('''You are hereby charged that on the
                                       28th day of May, 1970, you did willfully''',
                           styleG))

    doc = SimpleDocTemplate('hello.pdf')
    doc.build(story)


if __name__ == '__main__':
    # c = canvas.Canvas("hello.pdf", bottomup=0)

    create_document()