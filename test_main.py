from main import add_numbers, get_greeting


def test_add_numbers_positive():
	assert add_numbers(2, 3) == 5


def test_add_numbers_negative():
	assert add_numbers(-1, -5) == -6


def test_add_numbers_floats():
	assert add_numbers(1.5, 2.5) == 4.0


def test_get_greeting_standard():
	assert get_greeting("World") == "Hello, World!"
	assert get_greeting("Alice") == "Hello, Alice!"


def test_get_greeting_empty():
	assert get_greeting("") == "Hello, Guest!"
	assert get_greeting("   ") == "Hello, Guest!"
