import requests
import tkinter as tk

# срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    city = city_entry.get() # получаем данные от пользователя
    api_key = '81dc4a9445dc14778db518ee34a55fc0'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' # JSON данные

# отправляем запрос по URL
    response = requests.get(url)
    data = response.json()

# выводим данные о погоде
    weather_data = f'Город: {data["name"]}\nТемпература: {round(data["main"]["temp"] - 273)}°C\nПогода: {data["weather"][0]["description"]}'
    weather_label.config(text=weather_data)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Прогноз погоды")
root.geometry("700x500")
root.configure(background='darkseagreen')

city_label = tk.Label(root, text="Введите город:", bg='darkseagreen', font=('Inter', 30), padx=10, pady=50)
city_label.pack()

city_entry = tk.Entry(root, bg='ivory2', font=('Inter', 20))
city_entry.pack()

get_weather_button = tk.Button(root, text="Узнать погоду", bg='ivory2', font=('Inter', 15), padx=10, pady=10, command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", bg='darkseagreen', font=('Inter', 12), padx=10, pady=50)
weather_label.pack()

root.mainloop()