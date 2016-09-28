#!/usr/bin/python

import sys
import ssl
import OpenSSL
import subprocess

__author__ = "Liam Somerville - www.liamsomerville.com"

hostname="www.google.com"
cert = ssl.get_server_certificate((hostname, 443))

#write the certificate to file - its in pem format just now 
#so we will need to play with it a bit first 
fo = open("cert.pem", "w")
line = fo.write(cert)
fo.close()

#Lets start parsing the cert and making it human readable
output = subprocess.check_output([ "openssl", "x509",  "-in", "cert.pem" , "-issuer", "-noout", "-subject", "-checkhost", hostname, "-dates", "-serial", "-fingerprint", "-pubkey"])
output = output.replace("/L=", "\nLocalaity: ")
output = output.replace("/O=", "\nOrganisation: ")
output = output.replace("/C=", "\nCountry: ")
output = output.replace("/ST=", "\nState: ")
output = output.replace("/CN=", "\nCommon Name: ")
output = output.replace("/OU=", "\nOrganizational Unit:")
output = output.replace("issuer=" ,"==========\nIssuer\n========== ")
output = output.replace("subject=" ,"\n\n==========\nSubject\n========== ")
output = output.replace("notBefore=", "\n\n====================\nCertificate stats\n====================\nValid From: ")
output = output.replace("notAfter=", "Valid Until: ")
output = output.replace("serial=", "Serial: ")
output = output.replace("-----BEGIN PUBLIC KEY-----","\n\n==========\nPublic Key\n==========\n-----BEGIN PUBLIC KEY-----")
output = output.replace("Hostname","\n==========\nCertificate Validity\n==========\nHostname")

#Print the results
print "==============================\nCertificate Details for: ", hostname, "\n==============================\n"
print output


