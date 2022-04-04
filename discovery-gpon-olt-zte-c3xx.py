#!/usr/bin/env python3

from puresnmp import walk
import sys

# Variaveis
OID = '.1.3.6.1.4.1.3902.1082.500.1.2.4.5.1.1'
params = sys.argv

# Print inicio
print("[")

# Laço para cada index encontrado no snmpwalk
for row in walk(params[1],params[2], OID):
    # Oid completa
    oidfull = (row[0])
    # Pega o index
    indexport = (oidfull[15])
    # Converte o index para inteiro
    indexportint = int(indexport)
    # Convert o index para binario
    binario = format(indexportint, "b")
    # Separa por bits e converte para decimal
    rack = int(binario[5:13], 2)
    slot = int(binario[13:21], 2)
    port = int(binario[21:29], 2)

    # Print em formato json
    print("\t")
    print("\t{\n")
    print(f'\t\t"{"{#GPON_INDEX}"}": "{indexport}",')
    print(f'\t\t"{"{#GPON_NAME}"}": "{rack}/{slot}/{port}"')
    print("\t},\n")

print("\t{\n")
print(f'\t\t"{"{#TESTE}"}": "OK"')
print("\t}\n")

# Print ultima quebra de linha e adiciona um ]
print("]")
