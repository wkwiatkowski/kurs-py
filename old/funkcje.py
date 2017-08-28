#!/usr/bin/env python


def times(x, y):
    return x * y

a = times(2, 4)
print a

#======================================================
def powitanie(imie, nazwisko, pozdrowienie):
    return imie + nazwisko + pozdrowienie

print powitanie("Heniek ", "Kowalski ", "Hello")

#======================================================
def przywitanie():
    print "Pozdrowienia z mojej funkcji"

przywitanie()

#======================================================
def przywitanie_imienne(imie, zyczenia):
    print "Witaj " + imie + ". Zycze Tobie " + zyczenia

przywitanie_imienne("Bolek", "Najlepszego")

