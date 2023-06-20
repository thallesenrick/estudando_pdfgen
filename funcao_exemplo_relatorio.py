def hello(c):
    c.drawString(0, 0, '')


def grades():
    c.setFillColor(lightgrey)
    c.setStrokeColor(lightgrey)

    c.rect(30, 130, 530, 30, fill=True, stroke=1)
    c.rect(30, 160, 530, 40, fill=False, stroke=1)
    c.rect(30, 200, 530, 40, fill=False, stroke=1)

    c.rect(30, 240, 530, 30, fill=True, stroke=1)
    c.rect(30, 270, 530, 40, fill=False, stroke=1)
    c.rect(30, 310, 530, 40, fill=False, stroke=1)

    c.rect(30, 350, 530, 30, fill=True, stroke=1)
    c.rect(30, 370, 530, 50, fill=False, stroke=1)

    c.rect(30, 420, 530, 30, fill=True, stroke=1)
    c.rect(30, 450, 530, 40, fill=False, stroke=1)
    c.rect(30, 490, 530, 40, fill=False, stroke=1)
    c.rect(30, 530, 530, 40, fill=False, stroke=1)

    c.rect(30, 570, 530, 30, fill=True, stroke=1)
    c.rect(30, 600, 530, 40, fill=False, stroke=1)
    c.rect(30, 640, 530, 40, fill=False, stroke=1)
    c.rect(30, 680, 530, 40, fill=False, stroke=1)

    c.line(290, 720, 290, 130)


def cabecalhos():
    grades()
    c.setFont('Helvetica', 17)
    c.setFillColor(black)
    c.drawString(200, 30, 'Checklist de Manuntenção')
    c.drawString(214, 50, 'Preventiva - INTGEST')
    c.drawString(217, 70, 'Sunrise (21/09/2022)')
    c.drawString(40, 150, 'Empresa Responsável')
    c.drawString(40, 260, 'Cliente')
    c.drawString(40, 370, 'Local')
    c.drawString(40, 440, 'Informações do Serviço')
    c.drawString(40, 590, 'Ativo')

    c.setFont('Helvetica', 10)
    c.setFillColor(grey)
    c.drawString(30, 110, 'Por: Thalles Enrick (thallesenrick39@gmail.com)')
    c.drawString(463, 110, 'Em: 21/07/2022 08:30')
    c.drawString(190, 782, 'Intgest - Inteligencia e Gestao Tecnologica Ltda ')


def textos_bold():
    cabecalhos()
    c.setFont('Helvetica-Bold', 12)
    c.setFillColor(black)
    c.drawString(40, 177, 'Nome:')
    c.drawString(300, 177, 'Telefone / Celular:')
    c.drawString(40, 217, 'CPF / CNPJ:')
    c.drawString(300, 217, 'Endereço:')

    c.drawString(40, 287, 'Nome:')
    c.drawString(300, 287, 'CPF / CNPJ:')
    c.drawString(40, 327, 'Endereço:')
    c.drawString(300, 327, 'URL de abertura de chamados:')

    c.drawString(40, 397, 'Nome:')
    c.drawString(300, 397, 'Endereço:')

    c.drawString(40, 467, 'Horário planejado:')
    c.drawString(300, 467, 'Horário realizado:')
    c.drawString(40, 507, 'Tempo de execução:')
    c.drawString(300, 507, 'Tempo de inicio de atendimento:')
    c.drawString(40, 547, 'Tempo de finalização de atendimento:')
    c.drawString(300, 547, 'Responsável:')

    c.drawString(40, 617, 'Nome:')
    c.drawString(300, 617, 'Local do ativo:')
    c.drawString(40, 657, 'Marca:')
    c.drawString(300, 657, 'Modelo:')
    c.drawString(40, 697, 'Patrimônio / Número de Série:')


def textos():
    textos_bold()
    c.setFont('Helvetica', 12)
    c.drawString(40, 192, 'INTGEST')
    c.drawString(300, 192, '88 9 9712-2527')
    c.drawString(40, 232, '29.856.088/0001-20')
    c.drawString(300, 232, 'Av. Rua Moreira Pinto, N° 03, sala 01 - Centro ')

    c.drawString(40, 302, 'Prefeitura Municipal de Piquet Carneiro')
    c.drawString(300, 302, '07.738.057/0001-31')
    c.drawString(40, 342, 'Praça Mariano Aires - Centro')
    c.setFillColor(steelblue)
    c.drawString(300, 342, 'https://intgest.com.br/')

    c.setFillColor(black)
    c.drawString(40, 412, 'Andar Térreo - Sala 3')
    c.drawString(300, 412, 'Praça Mariano Aires - Centro')

    c.drawString(40, 482, '23/09/2022 08:00 - 23/09/22 10:00')
    c.drawString(300, 482, '23/09/2022 08:30 - 23/09/22 10:30')
    c.drawString(40, 522, 'Em torno de 2 horas')
    c.drawString(300, 522, '1 hora, 4 minutos e 39 segundos')
    c.drawString(40, 562, '1 hora, 2 minutos e 42 segundos')
    c.drawString(300, 562, 'Thalles Enrick André Maciel')

    c.drawString(40, 632, 'Intel Core i5 8GB HD 500GB Windows 10')
    c.drawString(300, 632, 'Andar Térreo - Sala 3')
    c.drawString(40, 672, 'Intel')
    c.drawString(300, 672, 'Desktop')
    c.drawString(40, 712, '05/001')

    hello(c)
    c.showPage()
    c.save()


if __name__ == '__main__':
    c = canvas.Canvas("hello.pdf", bottomup=0)
    textos()
