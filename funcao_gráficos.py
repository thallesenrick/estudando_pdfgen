def pdf_graficos_torta():
    c = Drawing(400, 200)
    pc = Pie()
    pc.x = 150
    pc.y = 50
    pc.data = [1, 2, 3, 4, 5, 6, 7, 8]
    pc.labels = ['l', 'b', 'g', 't', 'q', 'i', 'a', '+']
    pc.width = 120
    pc.height = 120
    pc.startAngle = 90
    pc.slices.strokeWidth = 0.5
    pc.slices[3].popout = 10
    pc.slices[3].strokeWidth = 0.5
    pc.slices[3].strokeDashArray = [1, 1]
    pc.slices[3].labelRadius = 1.2
    pc.slices[3].fontColor = red
    c.add(pc, '')
    renderPDF.drawToFile(c, 'hello.pdf')


def pdf_graficos_editando_labels():
    c = Drawing(200, 100)
    c.add(Circle(100, 90, 5, fillColor=green))

    lab = Label()
    lab.setOrigin(100, 90)
    lab.boxAnchor = 'ne'
    lab.angle = 45
    lab.dx = 0
    lab.dy = -20
    lab.boxStrokeColor = green
    lab.setText('''Some 
Multi-Line
Label''')
    c.add(lab)
    renderPDF.drawToFile(c, 'hello.pdf')


def pdf_graficos_eixos():
    c = Drawing(400, 200)

    data = [(10, 20, 30, 40), (15, 22, 37, 42)]

    x_axis = XCategoryAxis()
    x_axis.setPosition(50, 50, 300)
    x_axis.configure(data)
    x_axis.categoryNames = ['Piquet Carneiro', 'Quixadá', 'Senador Pompeu', 'Fortaleza']
    # 'n', 'e', 'w', 's', 'ne', 'nw', 'se', 'sw'.
    x_axis.labels.boxAnchor = 'n'
    x_axis.labels[3].dy = -15
    x_axis.labels[3].angle = 25
    x_axis.labels[3].fontName = 'Times-Bold'

    y_axis = YValueAxis()
    y_axis.setPosition(50, 50, 125)
    y_axis.configure(data)

    c.add(x_axis)
    c.add(y_axis)
    renderPDF.drawToFile(c, 'hello.pdf')


def pdf_graficos_barras():
    c = Drawing(600, 600)

    data = [
        (13, 5, 20, 22, 37, 98, 19, 4),
    ]

    names = ["Cat %s" % i for i in range(1, len(data[0])+1)]

    bc = HorizontalBarChart()
    bc.x = 100
    bc.y = 350
    bc.height = 200
    bc.width = 400
    bc.data = data
    bc.strokeColor = colors.white
    bc.groupSpacing = 10
    bc.barSpacing = 0
    bc.categoryAxis.style = 'parallel'
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 100
    bc.valueAxis.valueStep = 10
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = -10
    bc.categoryAxis.labels.fontName = 'Helvetica'
    bc.categoryAxis.categoryNames = names
    bc.bars[(0, 0)].fillColor = red
    bc.bars[(0, 1)].fillColor = orange
    bc.bars[(0, 2)].fillColor = yellow
    bc.bars[(0, 3)].fillColor = green
    bc.bars[(0, 4)].fillColor = steelblue
    bc.bars[(0, 5)].fillColor = pink
    bc.bars[(0, 6)].fillColor = colors.purple
    bc.bars[(0, 7)].fillColor = colors.lavender

    c.add(bc)
    renderPDF.drawToFile(c, 'hello.pdf')


if __name__ == '__main__':
    pdf_graficos()