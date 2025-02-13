from rest_framework.exceptions import ValidationError


def password_validator(value):
    """Проверка пароля: минимум 8 символов и цифры."""
    if len(value) < 8:
        raise ValidationError('Пароль должен содержать минимум 8 символов.')
    if not any(i.isdigit() for i in value):
        raise ValidationError('Пароль должен содержать хотя бы одну цифру.')


def email_validator(value):
    """Проверка домена email: только mail.ru и yandex.ru."""
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f"Домен {domain} не разрешен.")
