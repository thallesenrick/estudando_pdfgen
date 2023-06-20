def hello(c):
    c.drawString(10, 10, 'k')


def create_document():
    doc = SimpleDocTemplate('hello.pdf')
    elements = []

    data = [['Dom', 'Seg', 'Ter', 'Quar', 'Quin', 'Sex', 'Sab'],
            ['28', '29', '30', '31', '1', '2', '3'],
            ['4', '5', '6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15', '16', '17'],
            ['18', '19', '20', '21', '22', '23', '24'],
            ['25', '26', '27', '28', '29', '30', '1']]

    t = Table(data, 7 * [2 * cm], 6 * [2 * cm])

    tabla_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('BACKGROUND', (0, 1), (-4, -5), lightgrey),
        ('BACKGROUND', (-1, -1), (-1, -1), lightgrey),

        ('TEXTCOLOR', (0, 1), (0, -1), red),
        ('TEXTCOLOR', (0, 1), (-4, -5), grey),
        ('TEXTCOLOR', (-1, -1), (-1, -1), grey),

        ('INNERGRID', (0, 0), (-1, -1), 0.55, black),

        ('FONTSIZE', (0, 0), (-1, -1), 12, red),

        ('BOX', (0, 0), (-1, -1), 0.55, black),
    ])

    for row, values in enumerate(data):
        for column, value in enumerate(values):
            print(column, value)
            if value == '22':
                tabla_style.add('BACKGROUND', (column, row), (column, row), yellow)

    t.setStyle(tabla_style)
    elements.append(t)
    doc.build(elements)


def create_document2():
    doc = SimpleDocTemplate('hello.pdf')
    styles = getSampleStyleSheet()

    imagem = Image('logo.png')
    imagem.drawHeight = 3 * cm * imagem.drawHeight / imagem.drawWidth
    imagem.drawWidth = 3 * cm

    paragra = Paragraph('''<b>A pa<font color=red>r</font>a<i>graph</i></b>
        <super><font color=yellow>1</font></super>''', styles['BodyText'])
    paragr = Paragraph('''<para align=center spaceb=3>The <b>ReportLab Left
        <font color=red>Logo</font></b>
        Image</para>''', styles['BodyText'])

    elements = []
    data = [['A', 'B', 'C', paragra, 'D'],
            ['00', '01', '02', [imagem, paragr], '04'],
            ['10', '11', '12', [paragr, imagem], '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]

    t = Table(data, style=[('GRID', (1, 1), (-2, 2), 1, green),
                           ('BOX', (0, 0), (1, -1), 2, red),
                           ('LINEABOVE', (1, 2), (-2, 2), 1, steelblue),
                           ('LINEBEFORE', (2, 1), (2, -2), 1, magenta),
                           ('BACKGROUND', (0, 0), (0, 1), pink),
                           ('BACKGROUND', (1, 1), (1, 2), lavender),
                           ('BACKGROUND', (2, 2), (2, 3), orange),
                           ('BOX', (0, 0), (-1, -1), 1, black),
                           ('GRID', (0, 0), (-1, -1), 0.5, grey),
                           ('VALING', (0, 2), (0, 2), 'TOP'),
                           ('BACKGROUND', (0, 2), (0, 2), limegreen),
                           ('BACKGROUND', (3, 1), (3, 1), khaki),
                           ('ALING', (3, 1), (3, 1), 'CENTER'),
                           ('BACKGROUND', (3, 2), (3, 2), beige),
                           ('ALING', (3, 2), (3, 2), 'LEFT'),
                           ])

    t._argW[3] = 3.5 * cm
    t._argH[0] = 3.5 * cm

    elements.append(t)
    doc.build(elements)


def create_document3():
    doc = SimpleDocTemplate('hello.pdf')
    styles = getSampleStyleSheet()

    elements = []
    data = [['Top\nLeft', '', '02', '03', '04'],
            ['', '', '12', '13', '14'],
            ['20', '21', '22', 'Bottom\nRight', ''],
            ['30', '31', '32', '', '']]

    t = Table(data, style=[('GRID', (0, 0), (-1, -1), 0.5, grey),
                           ('BACKGROUND', (0, 0), (1, 1), palegreen),
                           ('SPAN', (0, 0), (1, 1)),
                           ('BACKGROUND', (-2, -2), (-1, -1), pink),
                           ('SPAN', (-2, -2), (-1, -1)),
                           ('ROUNDEDCORNERS', [10, 10, 10, 10])
                           ])

    elements.append(t)
    doc.build(elements)


if __name__ == '__main__':
    # c = canvas.Canvas("hello.pdf", bottomup=0)

    create_document()

