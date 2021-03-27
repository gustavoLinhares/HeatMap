import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "soe.heatmap@gmail.com"
toaddr = "misas.andrade@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "HeatMap SOE - Report"

body = "Caro Cliente\n\nSegue em anexo o seu relatório HeatMap de hoje. \n\nQualquer dúvida, por favor entre em contato com o setor técnico.\n\nAtt., \nEquipe SOE-HeatMap Solutions."

msg.attach(MIMEText(body, 'plain'))
filename = "REPORT.pdf"
attachment = open("/Users/Cliente/Documents/generatePDF/REPORT.pdf", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "projetosoe2021")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
