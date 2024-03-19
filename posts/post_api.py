from fastapi import APIRouter, UploadFile, Body
from database.postservice import *

from posts import PublicPostValidator, EditPostValidator

post_router = APIRouter(prefix='/posts', tags=['Работа с постами'])


# Загружаем наши посты DOWNLOAD
@post_router.post('/public_post')
async def publish_post(data: PublicPostValidator):
    result = add_new_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден Брат'}


# Запрос на удаление поста
@post_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нету такого поста'}


# Запрос на получении всех постов
@post_router.get('/all')
async def get_all():
    result = get_all_posts_db()

    return {'message': result}


# Запрос для добавления фото к посту
@post_router.post('/add-photo')
async def add_photo(post_id: int, photo_path: UploadFile = None):
    with open(f'media/{photo_path.filename}', 'wb') as file:
        user_photo = await photo_path.read()
        file.write(user_photo)

    result = upload_post_photo_db(post_id, f'media/{photo_path.file}')

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка! при загрузки изображения'}


# Изменить текст определенного публикацию
@post_router.put('/edit')
async def edit_post(data: EditPostValidator):
    result = edit_post_text_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка при изменении!'}


# Получить определенного поста
@post_router.get('/get-post')
async def get_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нету такого поста!'}


# Запрос на получении всех фотографий
@post_router.get('/all-photos')
async def all_photos():
    result = all_photos_db()
    return result

# Остальные функции вы сами я верю в вас!!!
# Посмотрите в postservice.py!
# Вам 15 минут!!
