
import json
import os

SYSTEM_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
post_link = str(SYSTEM_SCRIPT_DIR)+"/data/posts.json"
comments_link = str(SYSTEM_SCRIPT_DIR)+'/data/comments.json'


def get_posts_all(file_link):
    """Возвращает посты (список словарей)"""
    with open(file_link, 'r', encoding='utf-8') as json_file:
        posts_list = json.load(json_file)
        return posts_list


def get_comments_all(file_link):
    """Возвращает комментарии (список словарей)"""
    with open(file_link, 'r', encoding='utf-8') as json_file:
        comments_list = json.load(json_file)
        return comments_list


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    if type(user_name) not in [str]:
        raise TypeError('Имя пользователя должно быть строкой')
    posts_list = get_posts_all(post_link)
    user_posts = []
    for post in posts_list:
        if post['poster_name'] == user_name:
            user_posts.append(post)
    return user_posts


def get_posts_by_tag(tag):
    """Возвращает посты c определенным ТЕГОМ"""
    if type(tag) not in [str]:
        raise TypeError('Тег должнен быть строкой')
    posts_list = get_posts_all(post_link)
    tag_posts = []
    for post in posts_list:
        if post['tag'] == tag:
            tag_posts.append(post)
    return tag_posts


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    if str(post_id).isalpha():
        raise TypeError('ID поста должно быть цифрой')
    comments_list = get_comments_all(comments_link)
    comments_for_post_id = []
    for comment in comments_list:
        if comment['post_id'] == int(post_id):
            comments_for_post_id.append(comment)
    return comments_for_post_id


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    if type(query) not in [str]:
        raise TypeError(
            'Поисковый запрос должен быть строкой')
    posts_list = get_posts_all(post_link)
    posts_with_query = []
    for post in posts_list:
        if query.lower() in post['content'].lower():
            posts_with_query.append(post)
    return posts_with_query


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    if not pk.isdigit():
        raise TypeError('PK-идентификатор поста должен быть цифрой')
    posts_list = get_posts_all(post_link)
    for post in posts_list:
        if post['pk'] == int(pk):
            return post
