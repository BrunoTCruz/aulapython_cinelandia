import pandas as pd

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios':[1000, 2000, 3000, 4000]
}

Expect = {
    'cargo_desejado': ["assistente", "analista", "gerente", "diretor"],
    'salarios_almejado':[5000, 10000, 15000, 20000]
}

dados_bi = pd.DataFrame(dados)
Expect_bi = pd.DataFrame(Expect) 
print(dados_bi)
print(Expect_bi)

