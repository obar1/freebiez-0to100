def main() -> None:
    friends: dict[str, str | int] = {
        "mario": 10,
        "alea": 12,
        "sandra": 15,
        "???": "-inf"
    }

    def has_w(w: str | int):
        return True if str(w).isnumeric() else False

    for name, w in friends.items():
        print(f"{name.upper()} ... {has_w(w)} ... {w}")


main()
