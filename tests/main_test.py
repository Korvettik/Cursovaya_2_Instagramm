
from main import app



def test_get_all_posts_json():  # тест проверяет все посты, что
    response = app.test_client().get('/api/posts/')  #не поднимая сервер перехватываем поток данных, который генерится на этот адрес /
    #1) возвращается список,
    assert type(response.json) in [list], 'JSON должен быть списком словарей'

    #2) у элементов есть нужные ключи
    keys_list = sorted(['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'tag', 'pk'])  # проверочный список ключей
    #print(response.json[0].keys())
    for i in range(len(response.json)):
        assert keys_list == sorted(response.json[i].keys()), f'Ключи в JSON файле cловаря-поста {i+1} не верные'



def test_get_postid_json():  # тест проверяет конкретный пост, что
    response = app.test_client().get('/api/postid/?postid=2')  #пускай будет тестовым пост с 2 ID
    # 1) возвращается список,
    assert type(response.json) in [dict], 'JSON должен быть словарем'

    #2) у элементов есть нужные ключи
    keys_list = sorted(['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'tag', 'pk'])
    assert keys_list == sorted(response.json.keys()), f'Ключи в JSON файле cловаря-поста "2" не верные'