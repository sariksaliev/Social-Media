from database.models import PostPhoto, UserPost
from database import get_db
from datetime import datetime


# Получить все публикации
def get_all_posts_db():
    db = next(get_db())
    all_post = db.query(UserPost).all()
    return all_post


# Получить определенную публикацию
def get_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Такой пост не найден(('


# Добавить публикацию
def add_new_post_db(user_id, post_text):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=datetime.now())
    db.add(new_post)
    db.commit()
    return f'Успешно добавлен {new_post.post_id}'


# Изменить текст к публикацию
def edit_post_text_db(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return 'Текст к публикации изменен!'
    else:
        return 'Пост не найден Брат(('


# Удалить публикацию
def delete_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return 'Post successfully deleted'
    else:
        return 'Post not found'


def add_like_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.likes += 1
        db.commit()
        return '+1 Like'
    else:
        return 'Post not found'


def unlike_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.likes -= 1
        db.commit()
        return '-1 Like'
    else:
        return 'Post not found'


# Загрузить фотографии к определенному посту
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())

    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()

        return 'Фото добавлен!'
    else:
        return 'Нету поста Брат('


# Удалить фотографию определенного поста
def delete_post_photo_db(post_id):
    db = next(get_db())

    new_photo = db.query(PostPhoto).filter_by(post_id=post_id).first()

    if new_photo:
        # Если не будет работать то Капзда Дильмуроду
        db.delete(new_photo.photo_path)
        db.commit()

        return 'Фото добавлен!'
    else:
        return 'Нету поста Брат('


# Запрос на получении всех фотографий
def all_photos_db():
    db = next(get_db())

    photos = db.query(PostPhoto).all()
    return photos
