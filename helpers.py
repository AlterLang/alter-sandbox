import os
def clone() -> None:
    if os.path.exists("./alterlang-source") is False:
        os.system("git clone https://www.github.com/Atharv-Attri/alterlang-source.git")

