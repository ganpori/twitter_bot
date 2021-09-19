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
    fig.write_html("graph.html")
    fig.write_image("image.png")
    return


def generate_polynomial_values(max_degree=3, max_coefficient=9):
    degree = random.randint(0, max_degree)
    list_coefficient = [
        random.randint(-max_coefficient, max_coefficient) for _ in range(degree + 1)
    ]  # +1は0次の項
    return list_coefficient


def func_polynomial(list_coefficient):
    def _func_polynomial(x):
        value = 0
        for i, coefficient in enumerate(list_coefficient):
            value += coefficient * x ** i
        return value

    return _func_polynomial


def generate_str_polynomial(list_coefficient):
    str_polynomial = ""
    for i, coefficient in enumerate(list_coefficient):
        if coefficient > 0:
            str_coefficient = f"+{coefficient}"
        elif coefficient == 0:
            continue
        elif coefficient == -1:  # -1の1を表示しないようにする
            str_coefficient = "-"
        else:  # -1以外の負の場合。そのまま表示。
            str_coefficient = str(coefficient)
        str_polynomial = f"{str_coefficient}x^{i}{str_polynomial}"

    if coefficient >= 0:
        str_polynomial = str_polynomial[1:]  # 最後の+だけ除去する
    str_polynomial = str_polynomial[:-3]  # x^0を削除
    return str_polynomial


def create_dict_message_candidate():
    list_coefficient = generate_polynomial_values()
    str_polynomial = generate_str_polynomial(list_coefficient)
    dict_message_candidate = {
        "cos(x)": np.cos,
        "sin(x)": np.sin,
        "StandardNormalDistribution(x)": normal_distribution,
        str_polynomial: func_polynomial(list_coefficient),  # カリー化して部分適用した関数を与える
        "e^x": np.exp,
    }
    return dict_message_candidate


def select_dict_message(dict_message_candidate):
    temp = list(dict_message_candidate.keys())
    random.shuffle(temp)
    key = temp[0]

    return key, dict_message_candidate[key]


def calc_diff(func, x, h):
    x_plus_h = x + h
    dy_dx = (func(x_plus_h) - func(x)) / h
    return dy_dx


def main():
    dict_message_candidate = create_dict_message_candidate()
    fundmental_message, func = select_dict_message(dict_message_candidate)
    h1 = np.random.chisquare(1)  # 自由度１のχ二乗分布、0以上で0付近が多い
    h2 = np.random.chisquare(1)  # 自由度１のχ二乗分布
    diffferential_message = f"(f(x+h)-f(x))/h"
    message = f"f(x)={fundmental_message}, {diffferential_message}, {h1=:.4f},{h2=:.4f}, http://18.222.32.112/graph/graph.html"
    path_message_txt = Path("message.txt")
    with path_message_txt.open("w") as f:
        f.write(message)

    x = np.arange(-2 * np.pi, 2 * np.pi, step=0.06)
    y = func(x)
    dy_dx1 = calc_diff(func=func, x=x, h=h1)
    dy_dx2 = calc_diff(func=func, x=x, h=h2)

    df = pd.DataFrame(
        data={
            fundmental_message: y,
            "(f(x+h1)-f(x))/h1": dy_dx1,
            "(f(x+h2)-f(x))/h2": dy_dx2,
        },
        index=x,
    )
    df.index.name = "x"
    plot(df, title=message)
    return


if __name__ == "__main__":
    main()
