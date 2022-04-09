import pytest
import os

from utils import get_posts_all, get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk, post_link
from json import JSONDecodeError  #только чтобы видеть эту ошибку при перехвате

SYSTEM_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__)) # получаем абсолютный путь к директории исполняемого файла
test_post_link = str(SYSTEM_SCRIPT_DIR)+"/../tests/test_posts.json"  # формируем новый путь к тестовому кривому JSON файлу
test_comments_link = str(SYSTEM_SCRIPT_DIR)+"/../tests/test_comments.json"  # формируем новый путь к тестовому кривому JSON файлу

# поднимается ошибка на заранее кривом (пустом) файле
def test_get_posts_all_JSONDecodeError():
    with pytest.raises(JSONDecodeError):
        get_posts_all(test_post_link)

# поднимается ошибка на заранее кривом (пустом) файле
def test_get_comments_all_JSONDecodeError():
    with pytest.raises(JSONDecodeError):
        get_comments_all(test_comments_link)






def test_get_posts_by_user():
    user_posts = get_posts_by_user('hank')
    for post in user_posts:
        assert post['poster_name'] == 'hank', 'либо имя hank не содержится, либо функция не работает'

def test_get_posts_by_user_TypeError():
    with pytest.raises(TypeError):
        get_posts_by_user(123)







def test_get_comments_by_post_id_TypeError():
    with pytest.raises(TypeError):
        get_comments_by_post_id('abc')





def test_search_for_posts():
    with pytest.raises(TypeError):
        search_for_posts(123)





def test_get_post_by_pk_TypeError():
    with pytest.raises(TypeError):
        get_post_by_pk('abc')


