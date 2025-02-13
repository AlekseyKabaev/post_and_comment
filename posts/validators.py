from rest_framework.exceptions import ValidationError


def title_validator(value):
    """Проверка заголовка на запрещенные слова."""
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(f'Запрещенное слово: {word}')
