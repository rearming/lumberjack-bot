from pynput import keyboard
# from pynput import mouse
import time
import pyscreenshot as image_grab
from tkinter import *

left_rect = None
right_rect = None

pos1 = (0, 0)
pos2 = (0, 0)
radius = 100

left_image = None
right_image = None


# def keyboard_control():
# 	controller = keyboard.Controller()
# 	controller.press(keyboard.Key.caps_lock)
# 	time.sleep(1)
# 	controller.press(keyboard.Key.caps_lock)


def on_left_mouse(event):
	global pos1, left_rect
	print("left mouse pressed, {0} {1}".format(event.x, event.y))
	pos1 = (event.x, event.y)
	if left_rect is not None:
		canvas.delete(left_rect)
	left_rect = canvas.create_rectangle(pos1[0] - radius, pos1[1] - radius, pos1[0] + radius, pos1[1] + radius,
										outline='blue')


def on_rigth_mouse(event):
	global pos2, right_rect
	print("right mouse pressed, {0} {1}".format(event.x, event.y))
	pos2 = (event.x, event.y)
	if right_rect is not None:
		canvas.delete(right_rect)
	right_rect = canvas.create_rectangle(pos2[0] - radius, pos2[1] - radius, pos2[0] + radius, pos2[1] + radius,
										 outline='red')


def on_enter(event):
	global left_image, right_image
	left_image = grab(pos1[0] - radius, pos1[1] - radius, pos1[0] + radius, pos1[1] + radius)
	right_image = grab(pos2[0] - radius, pos2[1] - radius, pos2[0] + radius, pos2[1] + radius)


def on_space(event):
	global left_image, right_image
	if left_image is not None and right_image is not None:
		left_image.show()
		right_image.show()


def on_escape(event):
	print("Exit!")
	global root
	root.quit()


def on_left_arrow(event):
	global controller
	print("left arrow!")
	controller.press(keyboard.Key.left)


def grab(x1, y1, x2, y2):
	if x1 + x2 + y1 + y2 == 0:
		print("Some of areas aren't selected!")
		return None
	im = image_grab.grab(bbox=(x1, y1, x2, y2))
	return im


controller = keyboard.Controller()

root = Tk()
root.bind('<Return>', on_enter)
root.bind('<Key-Escape>', on_escape)
root.bind('<Key-space>', on_space)
root.bind('<Key-Left>', on_left_arrow)

root.bind('<Button-1>', on_left_mouse)
root.bind('<Button-3>', on_rigth_mouse)

root.attributes('-alpha', 0.2)
root.attributes('-fullscreen', True)

print("width: {0}, height: {1}", root.winfo_screenwidth(), root.winfo_screenheight())
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()
root.mainloop()

# пофиксить координаты image_grab
# после установки окон бота можно запускать через n секунд по sleep'у
