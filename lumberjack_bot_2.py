from PIL import ImageGrab
import pyautogui
import time
from pynput import keyboard


class Coordinates:
	replay_btn = (0, 0)
	left_btn = (0, 0)
	right_btn = (0, 0)

	game_over_tree = (0, 0)
	left_branch = (0, 0)
	right_branch = (0, 0)


class CoordinatesSmall(Coordinates):
	replay_btn = (950, 925)
	left_btn = (875, 925)
	right_btn = (1045, 925)

	game_over_tree = (-1, -1)
	left_branch = (900, 633)
	right_branch = (1018, 633)


class CoordinatesBig(Coordinates):
	replay_btn = (1910, 1930)
	left_btn = (1800, 1930)
	right_btn = (2050, 1930)

	game_over_tree = (1925, 1350)
	left_branch = (1832, 1490)
	right_branch = (2010, 1490)


def restart_game(coordinates: Coordinates):
	pyautogui.click(coordinates.replay_btn)
	time.sleep(0.2)
	pyautogui.click(coordinates.replay_btn)


game_over = False


def is_branch(coord):
	global c
	threshold = 500
	pixel = pyautogui.pixel(coord[0], coord[1])
	p_sum = pixel[0]\
			+ pixel[1] \
			+ pixel[2]
	if coord != c.game_over_tree:
		print("checking {0}. p_sum: [{1}], {2}".format("left" if coord == c.left_branch else "right", p_sum, "is branch" if p_sum < threshold else "not branch"))
	if p_sum < threshold:
		return True
	return False


def play(coords: Coordinates):
	button_side = coords.right_btn
	key = 'left'
	while not game_over:
		old_key = key
		if is_branch(coords.right_branch):
			key = 'left'
		if is_branch(coords.left_branch):
			key = 'right'
		if not is_branch(coords.game_over_tree):
			return
		print(key)
		# if key != old_key:
		# time.sleep(0.1)
		pyautogui.press(key)


def on_press(key):
	global game_over
	global c

	if str(key) == "'q'":
		print(is_branch(c.left_branch))
	if str(key) == "'w'":
		print(is_branch(c.right_branch))
	if str(key) == "'z'":
		pyautogui.moveTo(c.left_branch)
	if str(key) == "'c'":
		pyautogui.moveTo(c.right_branch)
	if str(key) == "'v'":
		pyautogui.moveTo(c.game_over_tree)
		is_branch(c.game_over_tree)

	if str(key) == "'e'":
		is_branch(c.left_branch)
		pyautogui.press('left')
	if str(key) == "'r'":
		is_branch(c.right_branch)
		pyautogui.press('right')
	if key == keyboard.Key.esc:
		game_over = True


listener = keyboard.Listener(on_press=on_press)
listener.start()

# c = CoordinatesSmall()
c = CoordinatesBig()
print(pyautogui.size())
pyautogui.PAUSE = 0.15

restart_game(c)
play(c)
# while not game_over:
# 	pass
