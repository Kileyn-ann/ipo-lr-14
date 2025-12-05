class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_contour_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.CONTOUR)
        return self

    def add_centered_text(self, text="Вариант 3"):
        if self.image:
            draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.load_default()
        except:
            font = None

        width, height = self.image.size

        # Используем font.getsize() если доступно, иначе draw.textbbox
        if hasattr(font, 'getsize'):
            
            text_width, text_height = font.getsize(text)
        else:
            # Предпочтительно использовать textbbox
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            position = ((width - text_width) / 2, (height - text_height) / 2)

            draw.text(position, text, fill="white", font=font)
        return self

