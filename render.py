import pandas as pd
import requests

USERNAME = "PhiladelphiaController"

if __name__ == "__main__":

    # load the raw data
    data = pd.read_csv("data.csv", header=None, names=["date", "name", "title", "link"])

    # read the template files
    out = open("template.md", "r").read().rstrip()

    lines = []
    for i, row in data.iterrows():
        line = "| "
        slug = row["name"]

        # Date
        line += f"{row['date']} | "

        # Github
        line += f"[{slug}](https://www.github.com/{USERNAME}/{slug})"
        line += "| "

        # Report titles
        line += f"[{row['title']}]({row['link']}) |"

        lines.append(line)

    with open("README.md", "w") as ff:
        ff.write(out + "\n" + "\n".join(lines))

