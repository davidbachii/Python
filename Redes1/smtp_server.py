# -*- coding: utf-8 -*-

import sys
import smtpd
import asyncore

ALLOWED_EMAIL = "ar1@gpar1.es"

class AR1SMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):

        print ("> Correo recibido de: {}".format(mailfrom.decode(())))
        if ALLOWED_EMAIL in rcpttos:
            addr = str(peer[0])
            port = str(peer[1])
            strmail = ""
            for mail in rcpttos:
                strmail+=mail
                strmail+=","

            strdata = data.replace('\n',' ').replace('\r','')

            with open("./mails.txt","a") as f:
                f.write(addr+"|"+
                        port+"|"+
                        mailfrom+"|"+
                        strmail+"|"+
                        strdata+"\n"
                        )
        else:
            print ("> Enviado a dirección de correo erronea: {}".format(rcpttos.decode()))

if __name__ == "__main__":
    print ("Servidor SMTP iniciado...")
    try:
        server = smtpd.DebuggingServer((sys.argv[1], int(sys.argv[2])), None)
        asyncore.loop()
    except KeyboardInterrupt:
        print ("Servidor SMTP finalizado.")
        exit(0)
