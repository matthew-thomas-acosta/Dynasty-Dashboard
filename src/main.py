from src.Data import setup_main as setup
from src.Data import json_writer as jsn


if __name__ == '__main__':
    setup.collect_data()
    jsn.connect(jsn.path)

