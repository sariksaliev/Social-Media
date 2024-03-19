from database.models import PostComment

from datetime import datetime
from database import get_db


# Опубликовать комментарий
def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())

    new_comment = PostComment(post_id=post_id,
                              comment_text=comment_text, user_id=user_id,
                              publish_date=datetime.now())
    if new_comment:
        db.add(new_comment)
        db.commit()

        return 'Комментарий успешно добавлен'
    else:
        return 'Нету такого поста (('


# Удаления комментарий
def delete_comment_db(post_id, comment_id):
    db = next(get_db())
    # Если ошибка то Капзда Шоху
    exact_comment = db.query(PostComment).filter_by(post_id=post_id, comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удален'
    else:
        return 'Такого коммента нету'


# Изменить определенную комментарию
def change_comment_db(post_id, comment_id, change_text):
    pass


# Вам 15 минут попробуйте сделать!

# Получить все комменты определенного поста
def get_post_comments_db(post_id):
    db = next(get_db())

    post_comments = db.query(PostComment).filter_by(post_id=post_id).all()

    if post_comments:
        return post_comments
    else:
        return 'Нету брат извините(('
