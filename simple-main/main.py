import django
import whitenoise
import waitress

import sys

def main():
    print("Hello from uv-test!")
    print("System path")
    for x in sys.path:
        print(x)

if __name__ == "__main__":
    main()
