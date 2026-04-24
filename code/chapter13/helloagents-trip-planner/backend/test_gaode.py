import requests


def test_amap_weather(api_key, city="110000"):  # 110000 是北京的 adcode
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={api_key}"
    response = requests.get(url)
    print("高德官方返回的原始数据：")
    print(response.json())


# 把这里替换成你的高德 Key！
my_key = "4aa0453521bc32c34bc1693379ecb42e"
test_amap_weather(my_key)