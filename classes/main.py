from PIL import Image, ImageFilter, ImageDraw, ImageFont
if __name__ == "__main__":
    # Путь к изображению
    image_path = "images.jpg" 
    save_path = "processed_image.jpg"

    # Создаём обработчик
    handler = ImageHandler(image_path)
    handler.load_image()

    # Создаём миниатюру
    thumbnail = handler.create_thumbnail()
    # сохраняем миниатюру
    thumbnail.save("thumbnail.jpg")

    # Обработка исходного изображения
    processor = ImageProcessor(handler.get_image())
    processor.apply_contour_filter().add_centered_text()

    # Сохраняем результат
    processor.image.save("filtered_text_image.jpg")
