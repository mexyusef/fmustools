from PIL import Image, ImageDraw

from typing import List, Tuple
from enum import Enum
import io, os, random

from django import http
from django.utils.cache import add_never_cache_headers, patch_cache_control

def random_hex() -> str:
	def h(): return random.randint(0, 255)
	return '#%02X%02X%02X' % (h(), h(), h())

def random_hexs(amount: int) -> List[str]:
	return [random_hex() for _ in range(amount)]

def random_color_range() -> List[str]:
	return random_hexs(random.randint(1, 20))

class DrawType(Enum):
	ELLIPSE = 0
	RECTANGLE = 1

class Shape:
	x: int
	y: int
	color: str
	line_width: int

	def __init__(self, x: int, y: int, color: str, line_width: int = 1) -> None:
		(self.x, self.y, self.color, self.line_width) = (x, y, color, line_width)

	def draw(self, image_draw: ImageDraw, xy: Tuple[Tuple[int, int], Tuple[int, int]], draw_type: DrawType = DrawType.ELLIPSE) -> None:
		if draw_type == DrawType.ELLIPSE:
			image_draw.ellipse(xy=xy, outline=self.color, width=self.line_width)

		if draw_type == DrawType.RECTANGLE:
			image_draw.rectangle(xy=xy, outline=self.color, width=self.line_width)

class Circle(Shape):
	radius: float

	def __init__(self, x: int, y: int, color: str, radius: float, line_width: int = 1) -> None:
		super().__init__(x, y, color, line_width=line_width)
		self.radius = radius

	def draw(self, image_draw: ImageDraw) -> None:
		return super().draw(image_draw=image_draw, xy=(
			(self.x - self.radius, self.y - self.radius),
			(self.x + self.radius, self.y + self.radius)
		), draw_type=DrawType.ELLIPSE)

	def __str__(self) -> str:
		return super().__str__() + f': Radius: {self.radius}, Pos: ({self.x}, {self.y}), Line Width: {self.line_width}'

class Square(Shape):
	width: int
	height: int

	def __init__(self, x: int, y: int, color: str, width: int, height: int, line_width: int = 1) -> None:
		super().__init__(x, y, color, line_width=line_width)
		(self.width, self.height) = (width, height)

	def draw(self, image_draw: ImageDraw) -> None:
		return super().draw(image_draw, xy=(
			(self.x - self.width, self.y - self.height),
			(self.x + self.width, self.y + self.height)
		), draw_type=DrawType.RECTANGLE)

	def __str__(self) -> str:
		return super().__str__() + f': Width: {self.width}, Height: {self.height}, Pos: ({self.x}, {self.y}), Line Width: {self.line_width}'

def image_art(request, seed=None, width=600, height=600):
	if not seed:
		seed = request.GET.get("seed") or "random"

	if seed != "random":
		random.seed(seed)

	bytes_io = io.BytesIO()

	image = Image.new('RGBA', (width, height), random_hex())
	image_draw = ImageDraw.Draw(im=image)

	for hexes in random_hexs(random.randint(3, 6)):
		square = Square(
			x=width/2,
			y=height/2,
			width=random.randint(0, width),
			height=random.randint(0, height),
			color=hexes,
			line_width=random.randint(5, 15),
		)
		square.draw(image_draw=image_draw)

	for hexes in random_hexs(random.randint(3, 6)):
		circle = Circle(
			x=width/2,
			y=height/2,
			radius=random.randint(0, width),
			color=hexes,
			line_width=random.randint(5, 15),
		)
		circle.draw(image_draw=image_draw)

	# image.save(f'img_{random.randint(0, 100000000000000000)}.png')
	# https://stackoverflow.com/questions/646286/how-to-write-png-image-to-string-with-the-pil
	image.save(bytes_io, 'PNG')
	# image.show()

	response = http.HttpResponse(bytes_io.getvalue())
	response["content-type"] = "image/png"
	if seed == "random":
		add_never_cache_headers(response)
	else:
		patch_cache_control(response, max_age=60, public=True)

	return response

def image_art_save(filepath, width=600, height=600):

	image = Image.new('RGBA', (width, height), random_hex())
	image_draw = ImageDraw.Draw(im=image)

	for hexes in random_hexs(random.randint(3, 6)):
		square = Square(
			x=width/2,
			y=height/2,
			width=random.randint(0, width),
			height=random.randint(0, height),
			color=hexes,
			line_width=random.randint(5, 15),
		)
		square.draw(image_draw=image_draw)

	for hexes in random_hexs(random.randint(3, 6)):
		circle = Circle(
			x=width/2,
			y=height/2,
			radius=random.randint(0, width),
			color=hexes,
			line_width=random.randint(5, 15),
		)
		circle.draw(image_draw=image_draw)

	image.save(filepath)
	# https://stackoverflow.com/questions/646286/how-to-write-png-image-to-string-with-the-pil
	# image.save(bytes_io, 'PNG')
	# image.show()
	return filepath
