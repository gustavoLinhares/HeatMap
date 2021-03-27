from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 #A4 210X297 (mm)
import os

pastaPDF = os.path.dirname(__file__)

def mp(mm):
    return mm/0.352777

def criarPDF():
    try:
        cnv=canvas.Canvas(pastaPDF+"\\REPORT.pdf", pagesize=A4)
        cnv.drawImage(pastaPDF+"\\Loja_HeatMap.png", mp(20), mp(200))
        cnv.drawString(mp(95),mp(280),"HeatMap Report")
        cnv.drawString(mp(20),mp(270),"Mapa de Calor do fluxo de clientes de sua loja:")
        cnv.drawString(mp(20),mp(190),"Quantidade de clientes hoje: ")
        cnv.drawString(mp(20),mp(180),"Média de permanência na loja: ")
        cnv.drawString(mp(20),mp(170),"Setor mais visitado:  / Tempo médio: ")
        cnv.drawString(mp(20),mp(160),"Setor menos visitado:  / Tempo médio: ")
        cnv.drawString(mp(20),mp(20),"Atualizado em 23/03/2021 (Terça-Feira) - 23:52.")

        cnv.circle(mp(100),mp(100),mp(25)) #Cria circulo

        cnv.save()
        print("PDF CRIADO!")
    except:
         print("ERRO AO CRIAR O ARQUIVO PDF")

criarPDF()
