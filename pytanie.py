#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# test pytanie - przykładowy skrypt

powitanie = raw_input("Wpisz swoje powitanie dla świata: ")
if len(powitanie) > 0 and powitanie.isalpha():
    slowo = powitanie.upper()
    print "Użytkownik przemówił: %s " %(slowo)
elif powitanie != powitanie.isalpha():
    print "Witasz się podając cyfry?"
else:
    print "Nic nie wpisałeś, nie chcesz się przywitać?"

