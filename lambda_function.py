import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class TestColumns:
    column1: str = None
    column2: str = None
    column3: str = None

def exec_function(event):
    column_list = TestColumns()
    column_list.column1 = "hoge"
    column_list.column2 = "huga"
    column_list.column3 = "hogehuga"

    print(column_list)
    column_list_json = column_list.to_json(indent=4)
    print(column_list_json)

def lambda_handler(event, context):
    exec_function(event)