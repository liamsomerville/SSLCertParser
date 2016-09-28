# SSLCertParser
A really basic Python SSL Certificate Parser

Provides an output like this:
```
==============================
Certificate Details for:  www.google.com 
==============================

==========
Issuer
==========  
Country: US
Organisation: Google Inc
Common Name: Google Internet Authority G2


==========
Subject
==========  
Country: US
State: California
Localaity: Mountain View
Organisation: Google Inc
Common Name: google.com


====================
Certificate stats
====================
Valid From: Sep 14 08:28:51 2016 GMT
Valid Until: Dec  7 08:19:00 2016 GMT
Serial: 07F3282B0622AF20
SHA1 Fingerprint=11:EB:76:5A:33:8D:7E:58:A8:2D:76:CD:C1:5E:5E:6E:B8:DF:19:09


==========
Public Key
==========
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAj6wWR9EZh2eBotYuN3CB
0eefIgWRjlDBQRMcuADPFBPxYIuZl0cXIhjejQeDvlMm31qDpdrgONAWIZbxsZ6B
yPRiYJTcgow6VTa0WIcwuHpOzAotKeT+AxFnyG+wrCKUvB6el9eYaCFaBz0d+hL8
7QcJ/MIay9bwGQYG67hSQK4M6/Ayx2R6HHopfAKoQBhOEi//aAp337tzhRCcMzq2
+rJk43e4AD8oAjP5BttGFa4Ngs8dDVM5iqcDyBxrG866UvTc25E00uGqqzDkXxNh
RiGdor89LojqZGY6m0Bdel4Aqh0fVghuHTFxIhmPSXnJoienUN5AOkX8Her6M5JJ
xwIDAQAB
-----END PUBLIC KEY-----

==========
Certificate Validity
==========
Hostname www.google.com does match certificate
```
