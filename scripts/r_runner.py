
# Запуск R-скриптов

import subprocess


def build_graphs():

    subprocess.run(
        [
            "Rscript",
            "r_scripts/plots.R"
        ],
        check=True
    )

    return True

