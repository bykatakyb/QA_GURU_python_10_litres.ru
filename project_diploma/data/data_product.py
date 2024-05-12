import dataclasses


@dataclasses.dataclass
class Product:
    title: str
    writer: str
    url: str
    price: str


product = Product(title='Мартин Иден',
                  writer='Джек Лондон',
                  url='audiobook/dzhek-london/martin-iden-603635/',
                  price='253 ₽')

product2 = Product(title='Дом, в котором…',
                   writer='Мариам Петросян',
                   url='book/mariam-petrosyan/dom-v-kotorom-6714012/',
                   price='349 ₽')

product3 = Product(title='Разговоры с друзьями',
                   writer='Салли Руни',
                   url='book/salli-runi/razgovory-s-druzyami-63415002/',
                   price='329 ₽')
