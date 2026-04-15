beneficiario = input()
codigo = input()
monto_base = int(input())

monto_final = monto_base + 25000

letra = codigo[0]

if "A" <= letra <= "L":
    recargo_letra = 25000
    monto_final += recargo_letra
elif letra == "U":
    recargo_letra = 100000 
    monto_final += recargo_letra
elif "M" <= letra <= "Z":
    recargo_letra = 40000
    monto_final += recargo_letra

# H10.20   H10.2
if len(codigo) > 5:
    texto_porcentaje = codigo[4] + codigo[5]
    porcentaje = int(texto_porcentaje)
else:
    porcentaje = int(codigo[4])

monto_final += (monto_final * porcentaje / 100)

nombres_capitulos = (
    "Ciertas enfermedades infecciosas y parasitarias", 
    "Tumores [neoplasias]",
    "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad",
    "Enfermedades endocrinas, nutricionales y metabólicas",
    "Trastornos mentales y del comportamiento",
    "Enfermedades del sistema nervioso",
    "Enfermedades del ojo y sus anexos",
    "Enfermedades del oído y de la apófisis mastoides",
    "Enfermedades del sistema circulatorio",
    "Enfermedades del sistema respiratorio",
    "Enfermedades del sistema digestivo",
    "Enfermedades de la piel y del tejido subcutáneo",
    "Enfermedades del sistema osteomuscular y del tejido conjuntivo",
    "Enfermedades del sistema genitourinario",
    "Embarazo, parto y puerperio",
    "Ciertas afecciones originadas en el período perinatal",
    "Malformaciones congénitas, deformidades y anomalías cromosómicas",
    "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte",
    "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas",
    "Causas externas de morbilidad y de mortalidad",
    "Factores que influyen en el estado de salud y contacto con los servicios de salud",
    "Códigos para propósitos especiales"
)

texto_bloque = codigo[1] + codigo[2]
bloque = int(texto_bloque)

if letra == "A" or letra == "B":
    capitulo = nombres_capitulos[0]
elif letra == "C":
    capitulo = nombres_capitulos[1]
elif letra == "D":
    if bloque <= 48:
        capitulo = nombres_capitulos[1]
    else:
        capitulo = nombres_capitulos[2]
elif letra == "E":
    capitulo = nombres_capitulos[3]
elif letra == "F":
    capitulo = nombres_capitulos[4]
elif letra == "G":
    capitulo = nombres_capitulos[5]
elif letra == "H":
    if bloque <= 59:
        capitulo = nombres_capitulos[6]
    else:
        capitulo = nombres_capitulos[7]
elif letra == "I":
    capitulo = nombres_capitulos[8]
elif letra == "J":
    capitulo = nombres_capitulos[9]
elif letra == "K":
    capitulo = nombres_capitulos[10]
elif letra == "L":
    capitulo = nombres_capitulos[11]
elif letra == "M":
    capitulo = nombres_capitulos[12]
elif letra == "N":
    capitulo = nombres_capitulos[13]
elif letra == "O":
    capitulo = nombres_capitulos[14]
elif letra == "P":
    capitulo = nombres_capitulos[15]
elif letra == "Q":
    capitulo = nombres_capitulos[16]
elif letra == "R":
    capitulo = nombres_capitulos[17]
elif letra == "S" or letra == "T":
    capitulo = nombres_capitulos[18]
elif "V" <= letra <= "Y":
    capitulo = nombres_capitulos[19]
elif letra == "Z":
    capitulo = nombres_capitulos[20]
elif letra == "U":
    capitulo = nombres_capitulos[21]
    
print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final) 
# (1) Ciertas enfermedades infecciosas y parasitarias (C00–D48)
# (2) Tumores [neoplasias] (A00–B99)
# (3)Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad (D50–D89)
# (4) Enfermedades endocrinas, nutricionales y metabólicas (E00–E90)
# (5) Trastornos mentales y del comportamiento (F00–F99)
# (6) Enfermedades del sistema nervioso (G00–G99)
# (7) Enfermedades del ojo y sus anexos (H00–H59)
# (8) Enfermedades del oído y de la apófisis mastoides (H60–H95)
# (9) Enfermedades del sistema circulatorio (I00–I99)
# (10) Enfermedades del sistema respiratorio (J00–J99)
# (11) Enfermedades del sistema digestivo (K00–K93)
# (12) Enfermedades de la piel y del tejido subcutáneo (L00-L99)
# (13) Enfermedades del sistema osteomuscular y del tejido conjuntivo (M00-M99)
# (14) Enfermedades del sistema genitourinario (N00-N99)
# (15) Embarazo, parto y puerperio (O00–O99)
# (16) Ciertas afecciones originadas en el período perinatal (P00–P96)
# (17) Malformaciones congénitas, deformidades y anomalías cromosómicas (Q00–Q99)
# (18) Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte (R00–R99)
# (19) Traumatismos, envenenamientos y algunas otras consecuencias de causas externas (S00–T98)
# (20) Causas externas de morbilidad y de mortalidad (V01–Y98)
# (21) Factores que influyen en el estado de salud y contacto con los servicios de salud (Z00–Z99)
# (22) Códigos para propósitos especiales (U00–U99)