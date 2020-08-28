from tkinter import *
import requests

class MyWindow(Tk):
	def __init__(self):
		Tk.__init__(self)

		self.title("Weather Application")
		self.resizable(False, False)
		self.iconbitmap('img/icon.ico')

		self.width = "500"
		self.height = "500"

		self.canvas = Canvas(self, height=self.height, width=self.width)
		self.canvas.pack()

		self.upper_frame = Frame(self)
		self.upper_frame.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9, anchor="nw")

		self.uBACKGROUND_IMAGE = PhotoImage(file="img/frame1_background.png")
		self.uBACKGROUND_OBJECT = Label(self.upper_frame, image=self.uBACKGROUND_IMAGE)
		self.uBACKGROUND_OBJECT.place(relheight=1,relwidth=1)

		self.entry = Entry(self.upper_frame, font="Arial 15", bd=5)
		self.entry.place(relx=0.05,rely=0.05,relheight=0.1,relwidth=0.9)

		self.button = Button(self.upper_frame, text="Get Weather", font="Arial 20", command=lambda: self.getWeather(self.entry.get()))
		self.button.place(relx=0.25,rely=0.2, relheight=0.1, relwidth=0.5)

		self.lower_frame = Frame(self, bg="#ffffff")
		self.lower_frame.place(relx=0.15,rely=0.4,relwidth=0.7, relheight=0.45)

		self.label = Label(self.lower_frame, font='Courier 15', anchor='nw', justify='left')
		self.label.place(relwidth=1, relheight=1)


	def formatWeather(self, r):

		try:
			global icon_image
			icon_image = PhotoImage(file="img/" + r['weather'][0]['icon'] + ".png")
			icon_object = Label(self.lower_frame, image=icon_image)
			icon_object.place(rely=0, relx=0.85, relheight=0.15,relwidth=0.15)

			city = r["name"]
			country = r["sys"]['country']
			description = r["weather"][0]["description"]
			temp = r["main"]["temp"]
			humidity = r['main']['humidity']
			pressure = r['main']['pressure']
			windspeed = r['wind']['speed']
			timezone = r['timezone'] / 3600
			fianl_string = 'City: %s\nCountry: %s\nWeather: %s\nTemperature(°C): %s\nHumidity: %s\nPressure: %s\nWind Speed: %s\nTimezone(hrs): %s' % (city, country, description, temp, humidity, pressure, windspeed, timezone)
		except KeyError:
			fianl_string = 'An Error Occured: \n'+ str(r['message'])
		return fianl_string

	def getWeather(self, city):
		weather_key = "[ENTER API KEY HERE]"
		url = "https://api.openweathermap.org/data/2.5/weather"
		params = {"APPID":weather_key, "q":city, "units":"metric"}
		response = requests.get(url, params).json()
		print(response)
		self.label['text'] = self.formatWeather(response)



if __name__ == '__main__':
	app = MyWindow()
	app.mainloop()
