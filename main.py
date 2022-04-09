from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk
import os
import logging
from tags_bookmarks.tags_bookmarks import tags, bookmarks, count_bookmarks_list, bookmarks_add_del  # импортируем модуль блупринт (и FLASK переменные)

# logging.basicConfig(filename="basic.log")

SYSTEM_SCRIPT_DIR = os.path.abspath(
    os.path.dirname(__file__))  # получаем абсолютный путь к директории исполняемого файла
print(SYSTEM_SCRIPT_DIR)

post_link = str(SYSTEM_SCRIPT_DIR) + "/data/posts.json"
comments_link = str(SYSTEM_SCRIPT_DIR) + '/data/comments.json'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # чтобы JSON правильно кодировал русские буквы



# ЗАДАНИЕ СО ЗВЕЗДОЧКОЙ
app.register_blueprint(tags, url_prefix='/tag/<tag>')  # Шаг *1 – Реализуйте переход по тегам
app.register_blueprint(bookmarks, url_prefix='/bookmarks')  # просмотр закладок
app.register_blueprint(bookmarks_add_del, url_prefix='/bookmarks_add_del/<postid>') # Шаг *2 – добавление или удаление посты в закладки.





# ОСНОВНОЕ ЗАДАНИЕ

@app.route('/', methods=['GET', 'POST'])  # главная страница, выводящая список всех постов (шаблон post.html)
def all_posts_page():
    posts_list = get_posts_all(post_link)  # функция возвращает список словарей всех постов
    logging.info('главная страница, index.html, функция возвращает список словарей всех постов')
    return render_template('index.html',
                           posts_list=posts_list,
                           count_bookmarks_list=count_bookmarks_list)


@app.route('/user-feed/<username>', methods=['GET', 'POST'])  # Шаг 4 – Реализуйте вывод по пользователю
def user_feed(username):
    user_posts = get_posts_by_user(username)
    logging.info(f'вывод всех постов пользователя {username}, user-feed.html')
    return render_template('user-feed.html',
                           user_posts=user_posts,
                           username=username)


@app.route('/post/<postid>', methods=['GET', 'POST'])  # Шаг 2 – реализуйте просмотр поста
def post_id(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    comments_count = len(comments)
    logging.info(f'вывод конкретного поста по его {postid}, post.html')
    return render_template('post.html',
                           post=post,
                           comments=comments,
                           comments_count=comments_count)


@app.route('/search/', methods=['GET', 'POST'])  # Шаг 3 – реализуйте поиск
def post_text_search():
    s = request.args.get('s')  # получение аргумента 's'
    post_search = search_for_posts(s)
    post_search_count = len(post_search)
    logging.info(f'выводим все посты, где встречается "{s}", search.html')
    return render_template('search.html',
                           post_search=post_search,
                           post_search_count=post_search_count)


@app.route('/api/posts/', methods=['GET'])  # возвращает полный список постов в виде json списка
def get_all_posts_json():
    data = get_posts_all(post_link)  # функция возвращает список словарей всех постов
    # data = request.json
    logging.info(f'выводим весь JSON файл с постами')
    return jsonify(data)


@app.route('/api/postid/', methods=['GET'])  # возвращает конкретный пост в виде словаря
def get_postid_json():
    postid = request.args.get('postid')  # получение аргумента 'postid'
    post = get_post_by_pk(postid)
    logging.info(f'выводим конкретный пост в виде словаря по его postid "{postid}", search.html')
    return jsonify(post)




if __name__ == '__main__':
    app.run(debug=True)