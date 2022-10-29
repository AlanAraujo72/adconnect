import io
import pandas as pd
import sys
#import pyad.aduser
#import pyad.adcontainer
from pyad import *
#from pyad import adquery

#import pyad.adquery

#with io.open("data.csv", "r", encoding="utf-8") as f1:
 #   data = f1.read()
 #   f1.close()
#file_row = data.split("\n")
file_row = pd.read_csv("data.csv", delimiter=";")
#ou=pyad.adcontainer.ADContainer.from_dn("OU=STI,OU=ST,OU=Usuarios,OU=AAPADM,OU=Usr e Cmp W2000,OU=Objetos do STJ,DC=STJ,DC=GOV,DC=BR")

q = adquery.ADQuery()

q.execute_query(
    attributes=["userprincipalName","givenName","sn","distinguishedName"],
    where_clause = "objectClass = 'user'",
    base_dn="caminho ou"
)

pyad.set_defaults(ldap_server="servidor",
username="user", password="senha")

emails = pd.Series(file_row['Email'])
for raw in q.get_results():

    distinto = raw["distinguishedName"]
    given = raw["givenName"]
    sn = raw["sn"]
    upn = raw["userprincipalName"]
    print(" processando " + upn)

    for row in file_row[1:]:
        attributes = row.split(";")

        if len(attributes) > 4:
            displayname = attributes[0]
            title = attributes[1]
            company = attributes[2]
            officephone = attributes[3]
            email = attributes[4]
            usuario = {'displayname': displayname, 'telephoneNumber': officephone,'title': title, 'department': company }
            emaltest = "adfadfasdfasf"
            if upn == emaltest:
               objeto = pyad.adobject.ADObject.from_dn(distinto)
               #mostra = objeto.get_attribute('telephoneNumber')
               input("ATUALIZADO - - - " + displayname + " *** telefone: " + officephone + " ***  Cargo: " + title + " ***  Empresa:  " + company)
               #objeto.update_attribute(attribute='telephoneNumber', newvalue=officephone)
               #objeto.update_attribute(attribute='title', newvalue=title)
               #objeto.update_attribute(attribute='company', newvalue=company)
               objeto.update_attributes(usuario)
        else:
            print(len(attributes))
            print(attributes[0])
            input("Lista zerou")


    pass
pass
