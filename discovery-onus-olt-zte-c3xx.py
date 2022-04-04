#!/usr/bin/env python3

from puresnmp import walk
import sys

# Variaveis
OID = '.1.3.6.1.4.1.3902.1082.500.10.2.3.3.1.2'
IP = '192.168.20.22'
COM = 'uKV9efW2rxD9j'
params = sys.argv

# Print inicio
print("[")

# Laço para cada index encontrado no snmpwalk
for row in walk(IP, COM, OID):
    # Oid completa
    oidfull = (row[0])
    # Pega o index
    indexport = (oidfull[15])
    indexonu = (oidfull[16])
    # Pega nome da ONU
    onuname = (row[1])
    # Converte o index para inteiro
    indexportint = int(indexport)
    indexonuint = int(indexonu)
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
    print(f'\t\t"{"{#GPON_NAME}"}": "{rack}/{slot}/{port}",')
    print(f'\t\t"{"{#ONU_INDEX}"}": "{indexonu}",')
    print(f'\t\t"{"{#ONU_NAME}"}": "{onuname}"')
    print("\t},\n")

print("\t\t{}")

# Print final
print("]")
