from collections import defaultdict
from functools import reduce

# Leitura do arquivo com informações de usuários e filmes
data = pd.read_csv('dados.csv')

# Função Map: Mapear os dados para o formato (user_id, [(movie, rating)])
def mapper(row):
    user_id = row['user_id']
    movie = row['movie']
    rating = row['rating']
    return user_id, [(movie, rating)]

# Função Reduce: Agrupar os filmes e suas avaliações por usuário
def reducer(user_id, ratings_list):
    return user_id, reduce(lambda x, y: x + y, ratings_list)

# Mapear os dados
mapped_data = data.apply(mapper, axis=1)

# Agrupar os dados usando Reduce
user_ratings = defaultdict(list)
for user_id, ratings_list in mapped_data:
    user_ratings[user_id].append(ratings_list)

# Exibição dos filmes e suas avaliações por usuário
for user_id, ratings in user_ratings.items():
    print(f"Usuário {user_id}:")
    for movie, rating in ratings:
        print(f"Filme: {movie}, Rating: {rating}")
