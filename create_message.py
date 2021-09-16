from pathlib import Path
import random
import numpy as np
import pandas as pd
import plotly.express as px


def normal_distribution(x):
    mean = 0
    std = 1
    y = (1 / (2 * np.pi * std * 2) ** 0.5) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
    return y


def plot(df, title=None):
    fig = px.scatter(df, title=title)
    fig.update_yaxes(title_text="y")
    fig.write_image("image.png")
    return


def create_dict_message_candidate():
    dict_message_candidate = {
        "y=cos(x)": np.cos,
        "y=sin(x)": np.sin,
        "y=tan(x)": np.tan,
        "y=標準正規分布(x)": normal_distribution,
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
    h = np.random.chisquare(1)  # 自由度１のχ二乗分布、0以上で0付近が多い
    diffferential_message = f"({fundmental_message[:-1]}+h) - {fundmental_message})/h"

    message = f"{fundmental_message}, {diffferential_message}, {h=}"

    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)

    x = np.arange(-2 * np.pi, 2 * np.pi, step=0.06)
    y = func(x)

    x_plus_h = x + h
    dy_dx = (func(x_plus_h) - func(x)) / h

    df = pd.DataFrame(
        data={fundmental_message: y, diffferential_message: dy_dx},
        index=x,
    )
    df.index.name = "x"
    plot(df, title=message)
    return


if __name__ == "__main__":
    main()
