from PIL import Image, ImageDraw
from sky_engine import get_sky_position


def create_sky_image():

    width = 1200
    height = 800

    image = Image.new(
        "RGB",
        (width, height),
        "black"
    )

    draw = ImageDraw.Draw(image)

    # Horizon
    horizon = height * 0.75

    draw.line(
        (0, horizon, width, horizon),
        fill="white",
        width=2
    )

    # Example stars
    stars = [
        (200, 150),
        (450, 100),
        (800, 180),
        (1000, 250)
    ]

    for x, y in stars:
        draw.ellipse(
            (x-3, y-3, x+3, y+3),
            fill="white"
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

    draw.ellipse(
    (x-20, y-20, x+20, y+20),
    fill="white"
    )

    image.save(
        "assets/skycanvas_test.png"
    )

    print("🌌 Sky image created!")


if __name__ == "__main__":
    create_sky_image()