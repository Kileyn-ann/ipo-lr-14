class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self

    def resize_image(self, max_width=200, max_height=200):
        if self.image:
            # сохраняем пропорции, подгоняя к максимальным размерам
            self.image.thumbnail((max_width, max_height))
        return self

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)

    def get_image(self):
        return self.image

    def create_thumbnail(self):
        """Создание уменьшенной версии изображения (макс 200x200)"""
        if self.image:
            thumb = self.image.copy()
            thumb.thumbnail((200, 200))
            return thumb
        return None
