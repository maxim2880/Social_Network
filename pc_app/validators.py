from rest_framework import serializers
import re


class PasswordValidator:
    def __call__(self, value):
        pattern = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')
        if not pattern.match(value):
            raise serializers.ValidationError(
                'Пароль не менее 8 символов, должен содержать цифры, строчные и заглавные латинские буквы'
            )
        return value


class EmailValidator:
    def __call__(self, value):
        # pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@mail.ru|@yandex.ru')
        domen = value[value.find("@") + 1:]
        if not (domen == "mail.ru" or domen == "yandex.ru"):
            raise serializers.ValidationError(
                'Разрешенные домены mail.ru, yandex.ru'
            )
        return value


class AgeValidator:
    def __call__(self, value):
        if value.age < 18:
            raise serializers.ValidationError('Посты могут создавать люди, достигшие 18 лет.')

        return value


class ForbiddenWordsValidator:
    def __call__(self, value):
        if "ерунда" in value or "гупость" in value or "чепуха" in value:
            raise serializers.ValidationError(
                'Употребление слов ерунда, глупость, чепуха запрещено!'
            )
        return value
