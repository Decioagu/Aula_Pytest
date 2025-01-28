# função testada
def email_valido(email):
    return "@" in email and "." in email

# função testada
def dividir(a,b):
    if b == 0:
        return None
    return a / b