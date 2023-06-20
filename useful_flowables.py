def hello(c):
    c.drawString(10, 10, 'k')


def create_document():
    story = []
    doc = SimpleDocTemplate('hello.pdf')

    stylesheet = getSampleStyleSheet()
    normalstyle = stylesheet['Code']
    text = '''                                                                                  
    class XPreformatted(Paragraph):                                                             
        def __init__(self, text, style, bulletText = None, frags=None, caseSensitive=1):        
            self.caseSensitive = caseSensitive                                                  
            if maximumLineLength and text:                                                      
                text = self.stopLine(text, maximumLineLength, splitCharacters)                  
            cleaner = lambda text, dedent=dedent: ''.join(_dedenter(text or '',dedent))         
            self._setup(text, style, bulletText, frags, cleaner)                                
    '''

    t = Preformatted(text, normalstyle, maxLineLength=60, newLineChars='> ')

    story.append(t)
    doc.build(story)


def create_document2():
    story = []
    doc = SimpleDocTemplate('hello.pdf')

    stylesheet = getSampleStyleSheet()
    normalstyle = stylesheet['Code']
    text = '''                                                                                    
    This is a non rearranging form of the <b>Paragraph</b> class;                                 
    <b><font color=red>XML</font></b> tags are allowed in <i>text</i> and have the same           

       meanings as for the <b>Paragraph</b> class.                                                
    As for <b>Preformatted</b>, if dedent is non zero <font color="red" size="+1">dedent</font>   

       common leading spaces will be removed from the                                             
    front of each line.                                                                           
    You can have &amp;amp; style entities as well for &amp; &lt; &gt; and &quot;                  
    '''

    t = XPreformatted(text, normalstyle, dedent=4)

    story.append(t)
    doc.build(story)


def create_document3():
    story = []
    doc = SimpleDocTemplate('hello.pdf')
    im = Image("JPG-Alta-Qualidade.jpg", width=2 * inch, height=2 * inch)
    im.hAlign = 'CENTER'
    story.append(im)
    doc.build(story)


if __name__ == '__main__':
    create_document()
