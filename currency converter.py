import requests

def convert_curr():
    init_currency = input("Enter the initial currency : ").upper()
    target_currency = input("Enter the target currency : ").upper()

    while True:
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("The amount needs to be numeric")
            continue

        if amount <= 0:
            print("Amount needs to be greater than 0")
        else:
            break

    url = f"https://api.apilayer.com/currency_data/convert?to={target_currency}&from={init_currency}&amount={amount}"

    headers = {
        "apikey": "nKjNMgRNohXayH48QeEX36xAL9lDvwRe"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print("Details:", response.text)
        return

    result = response.json()
    print(f"\n{amount} {init_currency} = {result['result']} {target_currency}")

if __name__ == '__main__':
    convert_curr()