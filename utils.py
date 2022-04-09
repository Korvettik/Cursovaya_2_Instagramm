
import json
import os

SYSTEM_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # получаем абсолютный путь к директории исполняемого файла

post_link = str(SYSTEM_SCRIPT_DIR)+"/data/posts.json"
comments_link = str(SYSTEM_SCRIPT_DIR)+'/data/comments.json'



def get_posts_all(file_link):
    """– возвращает посты (список словарей)"""

    with open(file_link, 'r', encoding='utf-8') as json_file:
        posts_list = json.load(json_file)
        return posts_list  # фактически это список словарей из прочтенного json файла


def get_comments_all(file_link):
    """– возвращает комментарии (список словарей)"""
    with open(file_link, 'r', encoding='utf-8') as json_file:
        comments_list = json.load(json_file)
        return comments_list  # фактически это список словарей из прочтенного json файла


def get_posts_by_user(user_name):
    """– возвращает посты определенного пользователя"""
    if type(user_name) not in [str]:
        raise TypeError('Имя пользователя должно быть строкой')
    posts_list = get_posts_all(post_link)  # получим список всех словарей-постов
    user_posts = []  # пустой список постов, если вдруг их у юзера будет несколько
    for post in posts_list:
        if post['poster_name'] == user_name:
            user_posts.append(post)
    return user_posts  # это список словарей



def get_posts_by_tag(tag):
    """– возвращает посты c определенным ТЕГОМ"""
    if type(tag) not in [str]:
        raise TypeError('Тег должнен быть строкой')
    posts_list = get_posts_all(post_link)  # получим список всех словарей-постов
    tag_posts = []  # пустой список постов
    for post in posts_list:
        if post['tag'] == tag:
            tag_posts.append(post)
    return tag_posts  # это список словарей


def get_comments_by_post_id(post_id):
    """– возвращает комментарии определенного поста"""
    if str(post_id).isalpha():
        raise TypeError('ID поста должно быть цифрой')
    comments_list = get_comments_all(comments_link)
    comments_for_post_id = []
    for comment in comments_list:
        if comment['post_id'] == int(post_id):
            comments_for_post_id.append(comment)
    return comments_for_post_id  # это список словарей комментариев к конкретному посту


def search_for_posts(query):
    """– возвращает список постов по ключевому слову"""
    if type(query) not in [str]:
        raise TypeError(
            'Поисковый запрос должен быть строкой')  # если руками вбивать в форму, то там и так будет строка
    posts_list = get_posts_all(post_link)  # получим список всех словарей-постов
    posts_with_query = []  # пустой список постов, если вдруг ключевое слово query будет в нескольких
    for post in posts_list:
        if query.lower() in post['content'].lower():
            posts_with_query.append(post)
    return posts_with_query  # это список словарей постов с ключевым словом


def get_post_by_pk(pk):
    """– возвращает один пост по его идентификатору"""
    if not pk.isdigit():
        raise TypeError('PK-идентификатор поста должен быть цифрой')
    posts_list = get_posts_all(post_link)  # получим список всех словарей-постов
    for post in posts_list:
        if post['pk'] == int(pk):
            return post  # это конкретный словарь-пост
