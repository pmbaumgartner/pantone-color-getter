import pandas as pd
import colorsys
from pathlib import Path 
import json

df = pd.read_csv("data.csv", header=None, names=["hex", "year", "color", "pantone"])

def hex_2_rgb(hex):
    h = hex.lstrip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def hex_to_rgb_str(hex):
    rgb = hex_2_rgb(hex)
    return "rgb" + str(rgb)


def rgb_to_hsl(r, g, b):
    p = tuple((i / 255 for i in (r, g, b)))
    h, l, s = colorsys.rgb_to_hls(*p)
    return h,s,l


def hex_to_hsl(hex):
    rgb = hex_2_rgb(hex)
    hsl = rgb_to_hsl(*rgb)
    return hsl

def hex_to_hsl_str(hex):
    h, s, l = hex_to_hsl(hex)
    return f"hsl({round(h*360)}, {round(s*100)}%, {round(l*100)}%)"

df["rgb"] = df["hex"].apply(hex_to_rgb_str)
df["hsl"] = df["hex"].apply(hex_to_hsl_str)

df = df[["year", "color", "pantone", "hex", "rgb", "hsl"]].sort_values("year", ascending=False)
Path("docs/colors.json").write_text(json.dumps(df.to_dict(orient="records"), indent=4))
