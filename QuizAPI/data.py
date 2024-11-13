import requests

paramater={
    "amount":10,
    "type":"boolean",
}
question_datas=requests.get(url="https://opentdb.com/api.php",params=paramater)
question_datas.raise_for_status()
question_data=question_datas.json()["results"]

