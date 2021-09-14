from pathlib import Path
import numpy as np
import plotly.express as px


def plot(x, y, title=None):
    fig = px.line(x=x, y=y, title=title)
    fig.write_image("image.png")
    return


def main():
    message = "y = cos(x)"
    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)

    x = np.arange(-np.pi, np.pi, step=0.2)
    y = np.cos(x)
    plot(x, y, title=message)
    return


if __name__ == "__main__":
    main()
