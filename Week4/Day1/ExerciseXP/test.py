import pandas as pd

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)
print(df.head())

print(df.describe())

print(df.info())

print(df.sort_values(by='Price', ascending=True))

print(df.sort_values(by='Copies Sold', ascending=False))

filtered_genre = df[df['Genre'] == 'Classic']
print(filtered_genre)

by_author= df.groupby('Author')['Copies Sold'].sum().reset_index
print(by_author)