import requests, json

def jsonifprime(complete_url):
	response = requests.get(complete_url)
	final_response = response.json()
	print(final_response)
	day_mentioned = final_response[date]
	if (day_mentioned % i) == 0:           #check if prime
		print(final_response)
	else:
		print("Date is not prime so no date")


if __name__ == "__main__":
	base_url =  "https://samples.openweathermap.org/data/2.5/weather?"
	api_key = input("Entre api_key: ")
	city_name = input("Entre City name: ")
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	jsonifprime(complete_url)
