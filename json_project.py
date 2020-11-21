import json


with open(r"E:\projetSIG\4.json","r") as f:
    source=f.read()
with open(r"E:\projetSIG\4.1 (1).json","r") as f1:
    source1=f1.read()

with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'w') as f:
            f.write("Secteur (Libellé, Id_secteur):\n- Emploi,1\n")
            data=json.loads(source)
            f.write("Thèmes du secteur (Libellé, Id_theme):\n ")
            for i in data["themes"]:
                f.write("-"+i["libelle"]+","+str(i["id"])+"\n")
            f.write("Indicateurs du secteur(Libellé, Id_theme, Id_indicateur):\n")
            for i in data["indicateurs"]:
                f.write("-"+i["libelle"]+","+i["idS"]+"\n")
            f.write("Fichiers json associés au secteur et ses indicateurs:\n- secteur :                  http://bds.hcp.ma/assets/data/4.json\n- indicateur 1 : http://bds.hcp.ma/assets/data/4.1.json\n- indicateur 2 : http://bds.hcp.ma/assets/data/4.2.json\n- indicateur 3 : http://bds.hcp.ma/assets/data/4.3.json\n- indicateur 4 : http://bds.hcp.ma/assets/data/4.4.json\n- indicateur 5 : http://bds.hcp.ma/assets/data/4.5.json\n- indicateur 6 : http://bds.hcp.ma/assets/data/4.6.json\n- indicateur 7 : http://bds.hcp.ma/assets/data/4.7.json\n- indicateur 8 : http://bds.hcp.ma/assets/data/4.8.json\n- indicateur 9 : http://bds.hcp.ma/assets/data/4.9.json\n- indicateur 10 : http://bds.hcp.ma/assets/data/4.10.json\n- indicateur 11 : http://bds.hcp.ma/assets/data/4.11.json\n- indicateur 12 : http://bds.hcp.ma/assets/data/4.12.json\n- indicateur 13 : http://bds.hcp.ma/assets/data/4.13.json\n- indicateur 14 : http://bds.hcp.ma/assets/data/4.14.json\n- indicateur 15 : http://bds.hcp.ma/assets/data/4.15.json\n- indicateur 16 : http://bds.hcp.ma/assets/data/4.16.json\n- indicateur 17 : http://bds.hcp.ma/assets/data/4.17.json\n- indicateur 18 : http://bds.hcp.ma/assets/data/4.18.json\n- indicateur 19 : http://bds.hcp.ma/assets/data/4.19.json\n- indicateur 20 : http://bds.hcp.ma/assets/data/4.20.json\n- indicateur 21 : http://bds.hcp.ma/assets/data/4.21.json\n- indicateur 22 : http://bds.hcp.ma/assets/data/4.22.json\n- indicateur 23 : http://bds.hcp.ma/assets/data/4.23.json\n- indicateur 24 : http://bds.hcp.ma/assets/data/4.24.json\n- indicateur 25 : http://bds.hcp.ma/assets/data/4.25.json\n- indicateur 26 : http://bds.hcp.ma/assets/data/4.26.json\n- indicateur 27 : http://bds.hcp.ma/assets/data/4.27.json\n- indicateur 28 : http://bds.hcp.ma/assets/data/4.28.json\n- indicateur 29 : http://bds.hcp.ma/assets/data/4.29.json\n- indicateur 30 : http://bds.hcp.ma/assets/data/4.30.json\n- indicateur 31 : http://bds.hcp.ma/assets/data/4.31.json\n- indicateur 32 : http://bds.hcp.ma/assets/data/4.32.json\n- indicateur 33 : http://bds.hcp.ma/assets/data/4.33.json\n- indicateur 34 : http://bds.hcp.ma/assets/data/4.34.json\n- indicateur 35 : http://bds.hcp.ma/assets/data/4.35.json\n- indicateur 36 : http://bds.hcp.ma/assets/data/4.36.json\n- indicateur 37 : http://bds.hcp.ma/assets/data/4.37.json\n- indicateur 38 : http://bds.hcp.ma/assets/data/4.38.json\n- indicateur 39 : http://bds.hcp.ma/assets/data/4.39.json\n- indicateur 40 : http://bds.hcp.ma/assets/data/4.40.json\n")
            f.write("Données de l'indicateur1.1: Puissance totale installee au Maroc\n")
            f.write("Année;Valeur\n")
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    data1=json.loads(source1)
    H=data1["levels"][0]
    for h in H["serie"]["data"]:
        f.write((h["annee"])+";"+str(h["valeur"])+"\n")

with open(r"E:\projetSIG\4.2.json","r") as f1:
    source2=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.2: Puissance installee par l O.N.E\n")
    data2=json.loads(source2)
    for k in range(4):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data2["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))

with open(r"E:\projetSIG\4.3.json","r") as f1:
    source3=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.3: Longueur des lignes de transport d’electricite\n")
    S=[]
    data3=json.loads(source3)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,7):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data3["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.4.json","r") as f1:
    source4=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.4: Longueur des lignes de transport d'electricite a  haute tension\n")
    data4=json.loads(source4)
    f.write("Année;Valeur\n")
    J=data4["levels"][0]
    for h in J["serie"]["data"]:
        f.write((h["annee"])+";"+str(h["valeur"])+"\n")

with open(r"E:\projetSIG\4.5.json","r") as f1:
    source5=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.5: Voltage Haute et moyenne tension\n")
    data5=json.loads(source5)
    f.write("Année;Valeur\n")
    J=data5["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.6.json","r") as f1:
    source6=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.6: Consommation par les petites distributions isolees\n")
    data6=json.loads(source6)
    f.write("Année;Valeur\n")
    J=data6["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.7.json","r") as f1:
    source7=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.7: Consommation par les industriels autoproducteurs\n")
    data7=json.loads(source5)
    f.write("Année;Valeur\n")
    J=data7["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.8.json","r") as f1:
    source8=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.8: Production nette d'electricite (O.N.E + AUTOPRODUCTEURS)\n")
    data8=json.loads(source8)
    f.write("Année;Valeur\n")
    J=data8["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.9.json","r") as f1:
    source9=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.9: Production nette des services de distribution\n")
    data9=json.loads(source9)
    f.write("Année;Valeur\n")
    J=data9["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))

with open(r"E:\projetSIG\4.10.json","r") as f1:
    source10=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.10: Production concessionnelle \n")
    data10=json.loads(source9)
    f.write("Année;Valeur\n")
    J=data10["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))

with open(r"E:\projetSIG\4.11.json","r") as f1:
    source11=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.11: Production total de l'O.N.E. \n")
    data11=json.loads(source11)
    f.write("Année;Valeur\n")
    J=data11["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))

with open(r"E:\projetSIG\4.12.json","r") as f1:
    source12=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.12: Production des apports des tiers\n")
    data12=json.loads(source12)
    f.write("Année;Valeur\n")
    J=data12["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.13.json","r") as f1:
    source13=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.13: Production du parc aolien de L'O.N.E.\n")
    data13=json.loads(source13)
    f.write("Année;Valeur\n")
    J=data13["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.14.json","r") as f1:
    source14=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.14: Production nette des petites distributions isolÃ©es\n")
    data14=json.loads(source14)
    f.write("Année;Valeur\n")
    J=data14["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.15.json","r") as f1:
    source15=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.15: Production nette des autoproducteurs \n")
    data15=json.loads(source15)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,4):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data15["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.16.json","r") as f1:
    source16=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.16: Production nette thermique de L'O.N.E \n")
    data16=json.loads(source16)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,14):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data16["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.17.json","r") as f1:
    source17=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.17: Consommation de l'energie electrique (Haute et moyenne tension) \n")
    data17=json.loads(source17)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,37):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data17["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.18.json","r") as f1:
    source18=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.18: Consommation de l'energie electrique (Base Tension) \n")
    data18=json.loads(source18)
    for k in range(7):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data18["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.19.json","r") as f1:
    source19=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.19: Puissance installee par les principaux autoproducteurs \n")
    data19=json.loads(source19)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,7):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data19["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.20.json","r") as f1:
    source20=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.20: Cote de retenue \n")
    data20=json.loads(source20)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,14):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data20["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.21.json","r") as f1:
    source21=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.21: Coefficient de remplissage \n")
    data21=json.loads(source21)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,14):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data21["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.22.json","r") as f1:
    source22=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.22: Volume de reserve \n")
    data22=json.loads(source22)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(1,14):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data22["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.23.json","r") as f1:
    source23=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.23: Nombre d'abonnes d'electricite \n")
    data23=json.loads(source23)
    for k in range(7):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data23["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))


with open(r"E:\projetSIG\4.24.json","r") as f1:
    source24=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur1.24: Personnel de l'O.N.E. \n")
    data24=json.loads(source24)
    f.write("-rang 1\n"+ " "+ "\n")
    for k in range(6):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data24["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.25.json","r") as f1:
    source25=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.1: Exportation des produits pÃ©troliers\n")
    data25=json.loads(source25)
    f.write("Année;Valeur\n")
    J=data25["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.26.json","r") as f1:
    source26=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.2: Exportation des huiles de base\n")
    data26=json.loads(source26)
    f.write("Année;Valeur\n")
    J=data26["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.27.json","r") as f1:
    source27=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.3: Consommation de produits pÃ©troliers Ã©nergÃ©tiques \n")
    data27=json.loads(source27)
    for k in range(11):
        f.write("-rang" + str(k+1) +":\n")
        f.write("Année;Valeur\n")
        H=data27["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.28.json","r") as f1:
    source28=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.4: Consommation de produits pÃ©troliers\n")
    data28=json.loads(source28)
    f.write("Année;Valeur\n")
    J=data28["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.29.json","r") as f1:
    source29=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.5: Consommation de produits pÃ©troliers non Ã©nergÃ©tiques\n")
    data29=json.loads(source29)
    f.write("Année;Valeur\n")
    J=data29["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.30.json","r") as f1:
    source30=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.6: Consommation des bitumes\n")
    data30=json.loads(source30)
    f.write("Année;Valeur\n")
    J=data30["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))




with open(r"E:\projetSIG\4.31.json","r") as f1:
    source31=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.7: Consommation des huiles et graisses\n")
    data31=json.loads(source31)
    f.write("Année;Valeur\n")
    J=data31["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))




with open(r"E:\projetSIG\4.32.json","r") as f1:
    source32=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur2.8: Exportation de Naphta\n")
    data32=json.loads(source32)
    f.write("Année;Valeur\n")
    J=data32["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))







with open(r"E:\projetSIG\4.34.json","r") as f1:
    source34=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.1: Ventes locales de charbon\n")
    data34=json.loads(source34)
    for k in range(4):
        f.write("Année;Valeur\n")
        H=data34["levels"][k]
        for h in H["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))




with open(r"E:\projetSIG\4.35.json","r") as f1:
    source35=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.2: Stocks de charbon\n")
    data35=json.loads(source35)
    f.write("Année;Valeur\n")
    J=data35["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))




with open(r"E:\projetSIG\4.36.json","r") as f1:
    source36=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.3: Ventes totales de charbon (y compris les exportations)\n")
    data36=json.loads(source36)
    f.write("Année;Valeur\n")
    J=data36["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.37.json","r") as f1:
    source37=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.4: Production nette de charbon\n")
    data37=json.loads(source37)
    f.write("Année;Valeur\n")
    J=data37["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.38.json","r") as f1:
    source38=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.5: Nombre d'heures de travail dans les Charbonnages du Maroc\n")
    data38=json.loads(source38)
    f.write("Année;Valeur\n")
    J=data38["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))




with open(r"E:\projetSIG\4.39.json","r") as f1:
    source39=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.6: Nombre d'employÃ©s des Charbonnages du Maroc\n")
    data39=json.loads(source39)
    f.write("Année;Valeur\n")
    J=data39["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))



with open(r"E:\projetSIG\4.40.json","r") as f1:
    source40=f1.read()
with open(r"E:\projetSIG\fichierTEXTElivrable.txt",'a') as f:
    f.write("Données de l'indicateur3.7: Exportation de charbon\n")
    data40=json.loads(source40)
    f.write("Année;Valeur\n")
    J=data40["levels"][0]
    for h in J["serie"]["data"]:
            if h["valeur"] == None:
                h["valeur"]="-"
            f.write(((h["annee"])+";"+str(h["valeur"])+"\n"))





























