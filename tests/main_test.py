import pytest
from main import app


def test_get_all_posts_json():  # тест проверяет все посты, что 1) возвращается список, 2) у элементов есть нужные ключи
    response = app.test_client.get('/api/posts/')  #не поднимая сервер перехватываем поток данных, который генерится на этот адрес /
    #1)....

    #2)....
    keys_list = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']  # проверочный список ключей
    for post in response.json():
        print(post.keys())
        for i in range(len(post.keys())):
            assert post.keys[i] == keys_list[i], f'Неверный ключ {keys_list[i]}'



def test_get_postid_json():  # тест проверяет конкретный пост, что 1) возвращается список, 2) у элементов есть нужные ключи
    # 1)....

    # 2)....
    pass