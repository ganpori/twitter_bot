from pathlib import Path


def main():
    message = "sample message"
    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)
    return


if __name__ == "__main__":
    main()
