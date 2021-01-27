import random
avaliacoes = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}
def DE(user1,user2):
    si={}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]: si[item] = 1

    if len(si)== 0: return 0
    soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item], 2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    return 1/(1+(soma**0.5))
def getS(user):
    S=[(DE(user, outro), outro)
                  for outro in avaliacoes if outro != user]
    S.sort()
    return S
def maisS(nome):
    filmes=list(avaliacoes['Ana'].keys())
    f1=random.choice(filmes)
    f2=random.choice(filmes)
    while f2 == f1:
        f1=random.choice(filmes)
        f2=random.choice(filmes)
    fv1=float(input("De uma nota para {} exemplo 4.5 ou 3.0->".format(f1)))
    fv2=float(input("De uma nota para {} exemplo 4.5 ou 3.0->".format(f2)))
    avaliacoes[nome]={f1:fv1,f2:fv2}
    S=getS(nome)
    comb=list(S[0])
    if comb[0] == 0:
        print("[-] Nenhum filme [-]")
    else:
        print("[+] Filmes recomendados para vc {} [+]".format(nome))
        filmes_comb=list(avaliacoes[comb[1]].keys())
        print(filmes_comb)
maisS('Gustavo')
        
