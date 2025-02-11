from generate_public import generate_public
from generate_page import generate_page


def main():
    generate_public("static", "public")
    generate_page("content", "template.html", "public")


if __name__ == "__main__":
    main()
