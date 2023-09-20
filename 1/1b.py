import pandas as pd

# Ler os dados do arquivo CSV
data = pd.read_csv('dados.csv')  # Substitua 'seuarquivo.csv' pelo nome do seu arquivo de dados

# Função para mapear os dados
def mapper(row):
    user_id = row['user_id']
    movie_id = row['movie_id']
    rating = row['rating']
    return user_id, (movie_id, rating)

# Aplicar o mapeamento aos dados
mapped_data = data.apply(mapper, axis=1)

# Agrupar os dados pelo user_id e listar os filmes e ratings
grouped_data = mapped_data.groupby('user_id')[1].apply(list)

# Exibir os resultados
for user_id, movies_ratings in grouped_data.iteritems():
    print(f'User {user_id}:')
    for movie_id, rating in movies_ratings:
        print(f'  Movie {movie_id}: Rating {rating}')
