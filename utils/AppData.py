import json
from dataclasses import dataclass

from .Model import Model


@dataclass
class Person:
    name: str
    url: str
    image_url: str


@dataclass
class KeyValue:
    name: str
    description: str


@dataclass
class Type:
    name: str
    description: str
    strengths: list[KeyValue]
    weaknesses: list[KeyValue]
    ideal_partners: list[KeyValue]
    careers: list[str]
    interests: list[str]
    famous_persons: list[str]


class AppData:
    def __init__(self):
        self.model = Model()
        self.pred_type: str = ''  # TODO: make pseudo private
        self.pred_proba: list[float] = [0.5, 0.5, 0.5, 0.5]

        self.types: list[str] = []

        with open('data/personalities_description.json', 'r', encoding='utf8') as f:
            description = json.load(f)

            for type_name, type_description in description.items():
                self.types.append(type_name)
                setattr(
                    self,
                    type_name,
                    Type(
                        name=type_name,
                        description=type_description['description'],
                        strengths=[
                            KeyValue(strength, description)
                            for strength, description in type_description['strengths'].items()
                        ],
                        weaknesses=[
                            KeyValue(weakness, description)
                            for weakness, description in type_description['weaknesses'].items()
                        ],
                        ideal_partners=[
                            KeyValue(ideal_partner, description)
                            for ideal_partner, description in type_description['ideal_partners'].items()
                        ],
                        careers=type_description['careers'],
                        interests=type_description['interests'],
                        famous_persons=[
                            Person(person, urls['url'], urls['image_url'])
                            for person, urls in zip(
                                type_description['famous_persons'].keys(),
                                type_description['famous_persons'].values(),
                            )
                        ],
                    ),
                )

    @property
    def type(self) -> Type:
        return getattr(self, self.pred_type)

    @property
    def proba(self) -> list[float]:
        return self.pred_proba

    @type.setter
    def type(self, value: str):
        self.pred_type = value

    @proba.setter
    def proba(self, value: list[float]):
        self.pred_proba = value


app_data = AppData()
