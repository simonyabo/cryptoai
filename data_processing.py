import json
import ast
import os
import numpy as np


def read_in_data(filename=None):
    with open(filename, "r") as fp:
        bitcoin = json.load(fp)
    ast_bit = ast.literal_eval(bitcoin)
    print(len(ast_bit))
    return ast_bit


def extract_data(json_obj, filename):
    """
    Open, close, volume_traded
    :param filename:
    :param json_obj:
    :return:
    """
    filename = filename.split(".")[0]
    overall_coin_data = []
    for i in json_obj:
        close_price = i["price_close"]
        open_price = i["price_open"]
        vol_trade = i["volume_traded"]
        count = i["trades_count"]
        high = i["price_high"]
        low = i["price_low"]
        overall_coin_data.append([open_price, close_price, vol_trade, count, high, low])

    np.save("./np_coin_data/"+filename, np.array(overall_coin_data))


if __name__ in "__main__":
    direct = "./raw_coin_data/"
    for files in os.listdir(direct):
        bitcoin_data = read_in_data(os.path.join(direct, files))
        extract_data(bitcoin_data, files)
