from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis, XValueAxis
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import Color, magenta, red, black, lightgrey, steelblue, grey, HexColor, yellow, lavender, \
    orange, limegreen, khaki, beige, palegreen
from reportlab.lib.colors import green, pink
from reportlab.lib import pdfencrypt
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Flowable, Table, TableStyle, Image, DocAssign, \
    DocWhile, DocPara, DocExec, DocIf, XPreformatted, BaseDocTemplate, PageTemplate, Frame, PageBreak
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus.tableofcontents import TableOfContents, delta
from reportlab.pdfbase.pdfmetrics import registerFont
from criando_flowable import MCLine
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
import pprint

"""
2.2 Mais sobre o Canvas

pagesize = paisagem ou retrato(tamanho da folha)
bottomup = altera os sistemas de coordenadas
pageCompression = determina se o fluxo de operações de PDF para cada página é compactado. Por padrão 
                  os arquivos não são compactados, mas se o tamanho da saida for importante (=1)
verbosity = determina quanta informação será printada. Por padrão é 0, mas se colocarmos 1 ao gerar pdf, 
            será informado com uma mensagem.
encrypt = determina se e como o documento é criptografado
exemplo: 
def create_document():
     c = canvas.Canvas("hello.pdf", pagesize=landscape(A4), bottomup=0,
                       pageCompression=0, verbosity=1, encrypt=None)
     hello(c)
     c.showPage()
     c.save()
"""

"""
2.3 - Operações de desenho

c.translate(inch, inch) = Para mover a origem para cima e para a esquerda 
c.setFont = Definir a fonte e tamanho 
c.setStrokeColorRGB(x,x,x) e c.setFillColor(x,x,x) = escolher algumas cores
c.line(x, x, x, x) = desenhar algumas linhas
c.rect(x, x, x, x) = desenhar retangulos
c.rotate(x) = gira o texto
exemplo: def create_document():
    c = canvas.Canvas("hello.pdf", bottomup=0)
    c.translate(inch, inch)
    c.setFont("Helvetica", 14)
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.setFillColorRGB(1, 0, 1)
    c.line(0, 0, 0, 1.7*inch)
    c.line(0, 0, 1*inch, 0)
    c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=1)
    c.rotate(90)
    c.setFillColorRGB(0, 0, 0.77)
    c.drawString(0.3*inch, -inch, "hello World")
    hello(c)
    c.showPage()
    c.save()
    
2.4 - As ferramentas: As operações de "desenho"

Métodos para linhas
    canvas.line(x1,y1, x2, y2)
    canvas.lines(linelist)
    
Métodos para formas
    canvas.grid(xlist, ylist)
    canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
    canvas.arc(x1,y1,x2,y2)
    canvas.rect(x, y, width, height, stroke=1, fill=0)
    canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)
    canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0)
    canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)
    canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0) 
exemplo: def create_document():
    c.arc(100, 100, 30, 30)
    c.circle(100, 100, 30, stroke=1, fill=0)
    
Métodos para desenhar string
    canvas.drawString(x, y, text)
    canvas.drawRightString(x, y, text)
    canvas.drawCentredString(x, y, text)
    
Métodos para objetos de caminho
    path= canvas.beginPath()
    canvas.drawPath(path, stroke=1, fill=0, fillMode=None)
    canvas.clipPath(path, stroke=1, fill=0, fillMode=None)
    
Métodos para objetos de texto
    textobject.setTextOrigin(x,y)
    textobject.setTextTransform(a,b,c,d,e,f)
    textobject.moveCursor(dx, dy) 
    (x,y) = textobject.getCursor()
    x = textobject.getX(); y = textobject.getY()
    textobject.setFont(psfontname, size, leading = None)
    textobject.textOut(text)
    textobject.textLine(text='')
    textobject.textLines(stuff, trim=1)

Métodos para imagem
    c.drawInlineImage('Rosa-sp-10.jpg', 0, 0, width=None, height=None)
 
2.5 - A caixa de ferramentas: as operações de "mudança de estado"
Esta seção lista brevemente as maneiras de alternar as ferramentas usadas pelo programa para pintar 
informações em uma página usando a interface de tela. 

MUDANDO CORES =
    canvas.setFillColorCMYK(c, m, y, k)
    canvas.setStrikeColorCMYK(c, m, y, k)
    canvas.setFillColorRGB(r, g, b) -> setFillColorRGB(139, 0, 0)
    canvas.setStrokeColorRGB(r, g, b)
    canvas.setFillColor(acolor)
    canvas.setStrokeColor(acolor)
    canvas.setFillGray(gray)
    canvas.setStrokeGray(gray) 

MUDANDO FONTES = 
    canvas.setFont(psfontname, size, leading = None)

MUDANDO ESTILO GRÁFICOS DA LINHA
    canvas.setLineWidth(width)
    canvas.setLineCap(mode)
    canvas.setLineJoin(mode)
    canvas.setMiterLimit(limit)
    canvas.setDash(self, array=[], phase=0)

MUDANDO GEOMETRIA =
    canvas.setPageSize(pair)
    canvas.transform(a,b,c,d,e,f):
    canvas.translate(dx, dy)
    canvas.scale(x, y)
    canvas.rotate(theta)
    canvas.skew(alpha, beta) 

CONTROLE DE ESTADO = 
Muitas vezes é importante salvar a fonte atual, transformação gráfica, estilos de linha e outros 
estados gráficos para restaurá-los mais tarde. Nenhum estado é preservado entre as páginas.
    canvas.saveState()
    canvas.restoreState()

2.7 - Coordenadas
    c = canvas.Canvas("hello.pdf", bottomup=0)
    c.setStrokeColor(pink)
    c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(black)
    c.setFont("Times-Roman", 20)
    c.drawString(60, 220, "(0, 0) The Origin")
    c.drawString(2.5*inch, 2*inch, "(2.5,1) in inches")
    c.drawString(4*inch, 0.4*inch, "(4, 2.5)")
    c.setFillColor(red)
    c.rect(0.3*inch, 0.8*inch, 0.3*inch, fill=1, height=30)
    c.setFillColor(green)
    c.circle(4.5 * inch, 2.9 * inch, 0.2 * inch, fill=1)
    hello(c)
    c.showPage()
    c.save()

Movendo a origem: o metodo de tradução
    c.translate(2.3*cm, 0.3*cm)

Alterando a escala
    c.scale(0.75, 0.75)  
    
Espelhando imagens
    c.translate(5.5*inch, 0)
    c.scale(-1, 1)

2.8 - Cores

RGB Color Transparency
    red50transparent = Color(100, 0, 0, alpha=0.4)
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(125, 800, 'sólido')
    c.setFillColor(blue)
    c.rect(125, 650, 100, 100, fill=True, stroke=False)
    c.setFillColor(red)
    c.rect(200, 700, 100, 100, fill=True, stroke=False)
    c.setFillColor(black)
    c.drawString(325, 800, 'transparente')
    c.setFillColor(blue)
    c.rect(325, 650, 100, 100, fill=True, stroke=False)
    c.setFillColor(red50transparent)
    c.rect(400, 700, 100, 100, fill=True, stroke=False)
    c.setFillColor(black)
    c.drawString(200, 600, 'Figura 2-8: Exemplo com o Alpha')
    
IMPRIMINDO POR CIMA DE OUTRAS CORES    
     for i in range(4):
        for color in (pink, green, brown):
            c.setFillColor(color)
            c.rect(x, 600, dx, 3*inch, stroke=0, fill=1)
            x += dx
    c.setFillColor(white)
    c.setStrokeColor(white)
    c.setFont('Helvetica-Bold', 85)
    c.drawCentredString(4.25*inch, 675, "SPUMONI")
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(230, 575, 'Figura 2-11: Pintando sobre as cores')
    

DIFERENTES FONTES E TAMANHOS
c.setFont("Times-Roman", 20)
    c.setFillColor(red)
    c.drawCentredString(4.2*inch, 11*inch, "Font size examples")
    c.setFillColor(magenta)
    size = 7
    y = 10.7*inch
    x = 2.9*inch
    lyrics = [""]  
    for line in lyrics:
        c.setFont("Helvetica", size)
        c.drawRightString(x, y, "%s points " % size)
        c.drawString(x, y, line)
        y = y - size * 1.2
        size += 1.5
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(190, 450, 'Figura 2-13: Textos em diferentes fontes e tamanhos')
    
MOVENDO O CURSO DE TEXTO / MOVENDO O CURSOR NA HORIZONTAL / ALTERANDO O ESPAÇAMENTO ENTRE 
CARACTERES, ESPAÇOS E LINHAS

c.saveState()
    textobject = c.beginText()
    textobject.setTextOrigin(130, 800)
    textobject.setFont("Helvetica-Oblique", 14)
    ??????? = ?
    lyrics = [""]
    for line in lyrics:
        textobject.set???????(????????)
        textobject.textLine("%s: %s" % (????????, line))
        leading += 2.5
    textobject.setFillColorCMYK(0.6, 0.0, 0.0, 0)
    textobject.textLines("")
    c.drawText(textobject)
    c.restoreState()
--------------------------------------------------------------------------------------------------
FUNÇÔES DESENHO DE ESTRELAS
def create_document(c, title="Title Here", aka="Comment here.",
                    xcenter=None, ycenter=None, nvertices=5):
    from math import pi, cos, sin
    radius = inch / 1.5
    if xcenter is None:
        xcenter = 2.75 * inch
    if ycenter is None:
        ycenter = 10.5 * inch
    c.drawCentredString(xcenter, ycenter + 1.4 * radius, title)
    c.drawCentredString(xcenter, ycenter - 1.4 * radius, aka)
    p = c.beginPath()
    p.moveTo(xcenter, ycenter + radius)
    angle = (2 * pi) * 2 / 5.0
    startangle = pi / 2
    for vertex in range(nvertices - 1):
        nextangle = angle * (vertex + 1) + startangle
        x = xcenter + radius * cos(nextangle)
        y = ycenter + radius * sin(nextangle)
        p.lineTo(x, y)
    if nvertices == 5:
        p.close()
    c.drawPath(p)

def joins(c: canvas.Canvas):
    c.setDash(6, 3)
    create_document(c, "Traços simples", "6 point on, 3 off", xcenter=2*inch)
    c.setDash(1, 2)
    create_document(c, "Pontos", "One on, two off", xcenter=4 * inch)
    c.setDash([1, 1, 3, 3, 1, 4, 4, 1], 0)
    create_document(c, "Padrão complexo", "[1, 1, 3, 3, 1, 4, 4, 1]", xcenter=6 * inch)
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(190, 650, 'Figura 2-24: Alguns padrões de traço')
    hello(c)
    c.showPage()
    c.save()

if __name__ == '__main__':
    c = canvas.Canvas("hello.pdf")
    joins(c)

--------------------------------------------------------------------------------------------------------
Capitulo 4
4.2 - Destinos e links - adicionar marcadores de página
    c.drawCentredString(560, 782, "1")
    c.bookmarkPage('page1')
    c.addOutlineEntry("pagina 1", 'page1')
    c.showPage()
    c.drawCentredString(560, 782, "2")
    c.bookmarkPage('page2')
    c.addOutlineEntry("pagina 2", 'page2')
   

"""


def pdf_graficos_linhas():
    c = Drawing(400, 200)
    data = [
        (13, 5, 20, 22, 37, 45, 19, 4),
        (5, 20, 46, 38, 23, 21, 6, 14)]

    lc = HorizontalLineChart()

    lc.x = 50
    lc.y = 50
    lc.height = 125
    lc.width = 300
    
    lc.data = data
    lc.joinedLines = 1
    catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 60
    lc.valueAxis.valueStep = 15
    lc.lines[0].strokeWidth = 2.9
    lc.lines[0].strokeColor = beige
    lc.lines[1].strokeWidth = 1.5

    c.add(lc)
    renderPDF.drawToFile(c, 'hello.pdf')


if __name__ == '__main__':
    pdf_graficos_linhas()
