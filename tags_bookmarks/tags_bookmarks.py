from flask import Blueprint, render_template
from werkzeug.utils import redirect

from utils import get_posts_by_tag, get_posts_all
import json
import os

SYSTEM_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
file_link = str(SYSTEM_SCRIPT_DIR) + "/../data/posts.json"


tags = Blueprint('tags', __name__, template_folder='templates', static_folder='static')
bookmarks = Blueprint('bookmarks', __name__, template_folder='templates', static_folder='static')
bookmarks_add_del = Blueprint('bookmarks_add_del', __name__, template_folder='templates', static_folder='static')


@tags.route('/', methods=['GET', 'POST'])  # Шаг *1 – Реализуйте переход по тегам
def posts_tag(tag):
    tag_posts = get_posts_by_tag(tag)
    return render_template('tag.html',
                           tag_posts=tag_posts,
                           tag=tag)


# СТРАННО РАБОТАЕТ
@bookmarks_add_del.route('/', methods=['GET', 'POST'])  # Шаг 2 – добавление или удаление посты в закладки.
def bookmarks_add_and_del(post_id):
    post_id = int(post_id)
    bookmarks_list = posts_bookmarks()  # получаем список словарей - постов bookmarks
    #формируем список индексов постов файла bookmarks.json
    bookmarks_pk_list = []
    for bookmarks_pk in bookmarks_list:
        bookmarks_pk_list.append(bookmarks_pk['pk'])
        print("[DEBUG]" + "glow-0")
    posts_all = get_posts_all(file_link)  # получаем список вообще всех постов
    # формируем список индексов постов  posts.json
    posts_pk_list = []
    for posts_pk in posts_all:
        posts_pk_list.append(posts_pk['pk'])
        print("[DEBUG]" + "glow-1")
    if post_id in bookmarks_pk_list:  # удаление поста
        for post in bookmarks_list:
            if post['pk'] == post_id:
                bookmarks_list.remove(post)
                print("[DEBUG]" + "glow-2")
                print(f"[DEBUG] bookmarks_pk_list after remove: {bookmarks_pk_list}")
    else:    #добавление поста
        for post in posts_all:
            if post['pk'] == post_id:
                bookmarks_list.append(post)
                print("[DEBUG]" + "glow-3")
    with open('./tags_bookmarks/bookmarks.json', 'w',
              encoding='utf-8') as json_file:
        json.dump(bookmarks_list, json_file, indent=3, ensure_ascii=False)
        print("[DEBUG]" + "glow-4")
    print('bookmarks_add_del сработала')
    return redirect("/", code=302)


def posts_bookmarks():
    """Функция возвращает JSON список словарей из файла"""
    with open('./tags_bookmarks/bookmarks.json', 'r', encoding='utf-8') as json_file:
        bookmarks_list = json.load(json_file)
        print("[DEBUG]"+"glow-5")
        return bookmarks_list


bookmarks_list = posts_bookmarks()
count_bookmarks_list = len(bookmarks_list)  # подсчет количества закладок


@bookmarks.route('/', methods=['GET', 'POST'])  # Шаг 3 – выведите закладки
def get_posts_bookmarks():
    return render_template('bookmarks.html',
                           bookmarks_list=bookmarks_list)
