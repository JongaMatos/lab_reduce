# Importação de bibliotecas necessárias
import pandas as pd

# Leitura do arquivo com informações de usuários e filmes
data = pd.read_csv('dados.csv')

# Estrutura de dados para armazenar filmes e suas avaliações por usuário
user_ratings = {}

# Iteração pelos registros do arquivo
for _, row in data.iterrows():
    user_id = row['user_id']
    movie = row['movie_id']
    rating = row['rating']
    
    # Verificar se o usuário já existe no dicionário
    if user_id in user_ratings:
        user_ratings[user_id].append((movie, rating))
    else:
        user_ratings[user_id] = [(movie, rating)]

# Exibição dos filmes e suas avaliações por usuário
for user_id, ratings in user_ratings.items():
    print(f"Usuário {user_id}:")
    for movie, rating in ratings:
        print(f"Filme: {movie}, Rating: {rating}")