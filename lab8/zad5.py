import networkx as nx

krawedzie = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E')]
lista_s={}
#lista sąsiedztwa zakładając graf kierowany   na początku myślałem że jest niekierowany i caly ten kod w cudzysłowie był do tego
def lista_sasiedztwa():
    for x, y in krawedzie:
        if not x in lista_s.keys():
                lista_s[x]=[]
                lista_s[x].append(y)
                '''if not y in lista_s.keys():
                    lista_s[y]=[]
                    lista_s[y].append(x)
                elif y in lista_s.keys():
                    lista_s[y].append(x)'''
        elif x in lista_s.keys():
            lista_s[x].append(y)
            '''if not y in lista_s.keys():
                lista_s[y]=[]
                lista_s[y].append(x)
            elif y in lista_s.keys():
                lista_s[y].append(x)'''

lista_sasiedztwa()
print(lista_s)

#macierz sąsiedzctwa
graf = nx.DiGraph()
graf.add_edges_from(krawedzie)

macierz = nx.to_numpy_array(graf)
print(macierz)

