from util import http_get
from db import UPDATE


def main() -> None:
    response = http_get("https://www.sec.gov/include/ticker.txt")

    for line in response.text.splitlines():
        data = line.split("\t")
        UPDATE.cik(
            symbol=data[0],
            cik=int(data[1])
        )


if __name__ == "__main__":  
    main()