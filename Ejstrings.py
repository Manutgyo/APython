str = "X-DSPAM-Confidence:0.8475"
colon = str.find(":")
numero = str[colon+1:]
numero = float(numero)
print(numero)

text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(":")
numero = text[colon+1:]
numero = float(numero.strip())
print(numero)

x = 'From marquard@uct.ac.za'
q_ubicacion = x.find("q")
print(q_ubicacion)
print(x[q_ubicacion])
uct_ubicacion = x.find("uct")
punto_ubicacion= x.find(".", uct_ubicacion)
print(uct_ubicacion, punto_ubicacion)
print(x[uct_ubicacion: punto_ubicacion])


