import os
from dotenv import load_dotenv

load_dotenv()


secret_key = os.getenv("SECRET_KEY")


def main():
    print(secret_key)


if __name__ == "__main__":
    main()
