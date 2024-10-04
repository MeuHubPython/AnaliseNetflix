import pandas as pd

df = pd.read_csv(
    "netflix_titles.csv", encoding="UTF-8"
)  # Lendo o arquivo netflix_titles.csv com encoding ISO-8859-1

print("\nColunas presentes no dataset: ", end="")
for columns in df.columns:
    print(f"{columns}, ", end="", flush=True)

print("\n\n")

quantity_films = len(
    df[df["type"] == "Movie"]
)  # Atribuindo a quantidade de filmes contidos no dataset para a variável quantity_films
quantity_series = len(
    df[df["type"] == "TV Show"]
)  # Atribuindo a quantidade de séries contidas no dataset para a variável quantity_series
print(  # imprimindo na tela a quantidade de filmes e séries contidas no dataset e o total de produções
    f"\n\nQuantidade de Filmes: {quantity_films} | Quantidade de Séries: {quantity_series} | Total (Filmes + Séries): {quantity_films + quantity_series}"
)

print("\n\n")

most_common_directors = (
    df["director"].value_counts().head(5)
)  # Procurando na coluna diretores os nomes mais comuns e armazenando os 5 primeiros em most_common_directors, juntamente com o seu número de produções.
print("\nOs 5 diretores que mais produziram séries e filmes:")
print(f"|{'Posição':^10} | {'Diretor':^25} | {'Produções':^10}|")
print("-" * 53)
counter = 1
for director, number in most_common_directors.items():
    print(
        f"|{counter:^10} | {director:^25} | {number:^10}|"
    )  # Imprimindo na tela o nome do diretor e sua quantidade de produções em formato de tabela no terminal.
    counter += 1

print("\n\n")


# Diretores que atuaram em suas próprias produções:
def director_as_actor(row):
    if pd.isna(row["cast"]) or pd.isna(row["director"]):
        return False
    actors = row["cast"].split(", ")
    return row["director"] in actors


result = df[
    df.apply(director_as_actor, axis=1)
]  # Aplicando a função director_as_actor em cada linha do dataset.

print(
    "\nDiretores que atuaram em suas próprias produções e títulos das respectivas produções: \n"
)
print(f"|{'Diretor':^25} | {'Produção':^80}|")
print("-" * 110)
for (
    row
) in (
    result.itertuples()
):  # Imprimindo na tela o nome do diretor e sua quantidade de produções em formato de tabela no terminal.
    print(f"|{row.director:^25} | {row.title:^80}|")

print("\n\n")

# INSIGHTS ADICIONAIS
print("\n#INSIGHTS ADICIONAIS: ")


# INSIGHT 1: Em qual ano houve a maior quantidade de producoes? A quantidade de produções aumentou ou diminuiu com o tempo?

print(
    f"\nINSIGHT 1:\n - Ano com mais lançamento de produções: {df['release_year'].value_counts().head(1).index[0]}, com {df['release_year'].value_counts().head(1).values[0]} produções"
)
print(
    "\n - Analizando o total de lançamentos por ano, percebemos uma queda no número de lançamentos com o passar dos anos.\n"
)
print(f"|{'Ano':^10} | {'Produções':^10}|\n" + ("-" * 25))
for year, productions in (
    df["release_year"].value_counts().head(6).items()
):  # Imprimindo na tela os 6 anos com mais produções.
    print(f"|{year:^10} | {productions:^10}|")

print("\n\n")
# INSIGHT 2: Em que país houve mais produções? Quais são os países que mais produziram na plataforma?
print(
    f"\nINSIGHT 2:\n - País com mais contribuições de produções: {df['country'].value_counts().head(1).index[0]}, com {df['country'].value_counts().head(1).values[0]} produções"
)
print(
    "\n - Os 5 países que mais produziram conteúdo para a palataforma:"
)  # Imprimindo na tela os 5 paises que mais produziram
print(f"\n|{'País':^25} | {'Produções':^10}|\n" + ("-" * 40))
for country, productions in df["country"].value_counts().head(5).items():
    print(f"|{country:^25} | {productions:^10}|")
