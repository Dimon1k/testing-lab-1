def add_numbers(a, b):
	"""Return the sum of two numbers."""
	return a + b


def get_greeting(name: str) -> str:
	"""Return a formatted greeting string."""
	if not name or not name.strip():
		return "Hello, Guest!"
	return f"Hello, {name.strip()}!"


def main():
	print(get_greeting("World"))
	print(f"2 + 3 = {add_numbers(2, 3)}")


if __name__ == "__main__":
	main()
