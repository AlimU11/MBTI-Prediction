from .StrEnum import StrEnum


class Colors(StrEnum):
    def opacity(self, opacity: float) -> str:
        return self.value.replace('(', 'a(').replace(')', f', {opacity})')

    @staticmethod
    def colorpalette() -> list[str]:
        return [Colors.blue, Colors.green, Colors.purple, Colors.red]

    @staticmethod
    def personality(name: str) -> str:
        personality_dict = {
            'ENFP': Colors.orange,
            'INFP': Colors.softblue,
            'ENTP': Colors.turquoise,
            'INTP': Colors.grey,
            'ESFJ': Colors.lightgrey,
            'ISFJ': Colors.teal,
            'ESTJ': Colors.neutral,
            'ISTJ': Colors.traditional_neutral,
            'ENFJ': Colors.deep_purple,
            'INFJ': Colors.pink,
            'ESTP': Colors.red,
            'ISTP': Colors.green,
            'ESFP': Colors.coral,
            'ISFP': Colors.light_silver,
            'ENTJ': Colors.brown,
            'INTJ': Colors.lightbrown,
        }

        return personality_dict[name]

    softblue = 'rgb(158, 185, 243)'
    turquoise = 'rgb(25, 210, 243)'
    lightgrey = 'rgb(204, 204, 204)'
    teal = 'rgb(102, 197, 204)'
    neutral = 'rgb(241, 226, 204)'
    traditional_neutral = 'rgb(247, 225, 160)'
    deep_purple = 'rgb(95, 70, 144)'
    coral = 'rgb(249, 123, 114)'
    light_silver = 'rgb(216, 216, 216)'
    brown = 'rgb(166, 118, 29)'
    lightbrown = 'rgb(229, 196, 148)'

    black = 'rgb(42, 63, 95)'
    white = 'rgb(255, 255, 255)'
    grey = 'rgb(153, 153, 153)'
    green = 'rgb(27, 158, 119)'
    blue = 'rgb(99, 110, 250)'
    pink = 'rgb(255, 102, 146)'
    yellow = 'rgb(254, 203, 82)'
    red = 'rgb(220, 57, 18)'
    purple = 'rgb(171, 99, 250)'
    orange = 'rgb(255, 161, 90)'

    transparent = 'rgba(0, 0, 0, 0)'
