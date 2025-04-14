import math
from datetime import datetime

import numpy as np
import pandas as pd

from app.utils import no_type_hints


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(say_hello("world"))


if __name__ == "__main__":
    main()

    df = pd.DataFrame()
    sqrt_five = math.sqrt(5)

    some_date = datetime.now()
    some_array = np.array([1, 2, 3, 4, 5])

    delimited_string = no_type_hints("Hello, world!")
