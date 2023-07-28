import requests
APY_KEY = "99f3c07488fa2f5f9151aa97a7ef6b27"
cidade = "buri"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={APY_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ªC")
