from PIL import Image
import numpy as np

def shift_pixels(image_path, output_path):
    
    img = Image.open(image_path)
    pixels = np.array(img)

    if len(pixels.shape) == 3:
        height, width, channels = pixels.shape
    elif len(pixels.shape) == 2:
        height, width = pixels.shape
        channels = 1
    else:
        raise ValueError("Gambar ndak didukung bosqu")

    for row in range(height):
        if row % 2 == 0:
            pixels[row] = np.roll(pixels[row], 1, axis=0)
        else:
            pixels[row] = np.roll(pixels[row], -10, axis=0)

    shifted_img = Image.fromarray(pixels)

    shifted_img.save(output_path)
    print(f"Gambar telah disimpan sebagai {output_path}")

shift_pixels('gemastik_5.png', 'corrected_gemastik_51.png')
