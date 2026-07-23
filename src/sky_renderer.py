from PIL import Image, ImageDraw
from sky_engine import get_sky_position
import random

def create_sky_image():

    width = 1200
    height = 800

    # Create sky gradient
    image = Image.new(
        "RGB",
        (width, height)
    )

    pixels = image.load()

    for y in range(height):

        ratio = y / height

        # Sky colours
        r = int(15 + ratio * 100)
        g = int(30 + ratio * 70)
        b = int(90 + ratio * 80)

        for x in range(width):
            pixels[x, y] = (r, g, b)


    draw = ImageDraw.Draw(image)


    # Horizon
    horizon = height * 0.75

    draw.line(
        (0, horizon, width, horizon),
        fill=(120,120,140),
        width=2
    )

    # Generate stars ⭐

    random.seed(42)

    for i in range(250):

        x = random.randint(0, width)

        # Keep stars mostly above horizon
        y = random.randint(0, int(horizon))

        brightness = random.randint(120, 255)

        size = random.choice([1, 1, 2, 2, 3])

        draw.ellipse(
        (x-size, y-size, x+size, y+size),
        fill=(brightness, brightness, brightness)
        )


    # Real Moon position

    sky = get_sky_position()

    moon_altitude = sky["moon_altitude"]
    moon_azimuth = sky["moon_azimuth"]

    print("Renderer Moon altitude:", moon_altitude)
    print("Renderer Moon azimuth:", moon_azimuth)


    # Convert sky coordinates to image coordinates

    x = (moon_azimuth / 360) * width

    y = height - ((moon_altitude + 90) / 180) * height


    if moon_altitude > 0:

    # Moon glow layers

        draw.ellipse(
        (x-60, y-60, x+60, y+60),
        fill=(180, 180, 200)
        )

        draw.ellipse(
        (x-40, y-40, x+40, y+40),
        fill=(220, 220, 230)
        )

        draw.ellipse(
        (x-20, y-20, x+20, y+20),
        fill="white"
     )

    else:
        print("Moon is below horizon")


    # Save image

    image.save(
        "assets/skycanvas_test.png"
    )

    print("🌌 Sky image created!")


if __name__ == "__main__":
    create_sky_image()