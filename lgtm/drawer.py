from PIL import Image, ImageDraw, ImageFont

# 画像全体に対するメッセージ病が可能エリアの比率
MAX_RATIO = 0.8

# フォント関連の定数
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

# フォントの格納先のパスは実行環境に合わせて変更
FONT_NAME = '/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)

# アウトプット関連の定義
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'

#---

def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    # メッセージを描画できる領域のサイズをタプルの要素ごとに計算
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # 1 ポイントずつ小さくしながら最適なフォトサイズを求める
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)

        # 描画に必要なサイズ
        text_width, text_height = draw.textsize(
            message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height

        # 幅、高さともに領域内に収まる値を採用
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2,
                        (image_height - text_height) / 2)
            # メッセージの描画
            draw.text(position, message,
                      fill=FONT_COLOR_WHITE, font=font)
            break

    # 画像の保存
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
