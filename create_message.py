from pathlib import Path
import random
import numpy as np
import pandas as pd
import plotly.express as px


def plot(df, title=None):
    fig = px.line(df, title=title)
    fig.write_image("image.png")
    return


def create_dict_message_candidate():
    dict_message_candidate = {
        "y=cos(x)": np.cos,
        "y=sin(x)": np.sin,
        "y=tan(x)": np.tan,
    }
    return dict_message_candidate


def select_dict_message(dict_message_candidate):
    temp = list(dict_message_candidate.keys())
    random.shuffle(temp)
    key = temp[0]

    return key, dict_message_candidate[key]


def main():
    dict_message_candidate = create_dict_message_candidate()
    fundmental_message, func = select_dict_message(dict_message_candidate)
    h = 0.01
    diffferential_message = fundmental_message[:-1] + "+h)/h"

    message = f"{fundmental_message}, {diffferential_message}, {h=}"

    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)

    x = np.arange(-2 * np.pi, 2 * np.pi, step=0.02)
    y = func(x)

    x_plus_h = x + h
    dy_dx = (func(x_plus_h) - func(x)) / h

    df = pd.DataFrame(
        data={fundmental_message: y, diffferential_message: dy_dx},
        index=x,
    )
    plot(df, title=message)
    return


if __name__ == "__main__":
    main()
