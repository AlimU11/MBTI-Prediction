from pydantic import BaseSettings


class Config(BaseSettings):
    class Page(BaseSettings):
        name: str
        link: str
        icon: str

    pages: list[Page] = [
        Page(name='Index', icon='flask', link='/'),
        Page(name='Types', icon='book', link='/types'),
    ]

    # TODO add api secrets variables


config = Config()
