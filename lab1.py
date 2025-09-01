"""Simple program to multiply two numbers entered by the user."""


def multiply(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2


if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = multiply(first_number, second_number)
    print(f"{first_number} * {second_number} = {result}")
