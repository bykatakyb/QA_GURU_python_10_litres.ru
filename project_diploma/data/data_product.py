import dataclasses


@dataclasses.dataclass
class Product:
    name: str
    writer: str
    url: str
    price: str


item1 = Product(name='',
                writer='',
                url='',
                price='')
item2 = Product(name='',
                writer='',
                url='',
                price='')
item3 = Product(name='',
                writer='',
                url='',
                price='')