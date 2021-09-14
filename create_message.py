from pathlib import Path
import numpy as np
import plotly.express as px


def plot(x, y):
    fig = px.line(x=x, y=y)
    fig.write_image("image.png")
    return


def main():
    message = "sample message"
    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)

    x = np.arange(-np.pi, np.pi)
    y = np.cos(x)
    plot(x, y)
    return


if __name__ == "__main__":
    main()
