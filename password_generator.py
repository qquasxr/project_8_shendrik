import random
import string

def generate_password(n):
    # Алфавит: только маленькие буквы
    chars = string.ascii_lowercase
    password = ''.join(random.choice(chars) for _ in range(n))
    return password

if __name__ == "__main__":
    length = 10
    pwd = generate_password(length)
    print(f"Случайный пароль: {pwd}")