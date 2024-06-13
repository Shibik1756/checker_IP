import requests


def check_list(ip_list: list):
    try:
        for ip in ip_list:
            response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
            result = dict(IP=ip,
                          Status=response.get("status"),
                          Message=response.get("message"),
                          Continent=response.get("continent"),
                          Continent_code=response.get("continentCode"),
                          Country=response.get("country"),
                          Country_Code=response.get("countryCode"),
                          Region=response.get("region"),
                          Region_name=response.get("regionName"),
                          City=response.get("city"),
                          District=response.get("district"),
                          ZIP=response.get("zip"),
                          Isp=response.get("isp"),
                          Org=response.get("org"),
                          As_data=response.get("as"),
                          As_name=response.get("asname"),
                          Reverse=response.get("reverse"),
                          Mobile=response.get("mobile"),
                          Proxy=response.get("proxy"),
                          Hosting=response.get("hosting"),
                          Query=response.get("query")
                          )

        for k, v in result.items():
            print(k, v)

    except BaseException:
        print("No connection")

        
def sort_arg(message: str):
    """В функцию передается один IP адрес. В случае передачи нескольких IP
    адресов, между ними ставится разделитель <,> или символ пробела < >."""
    ip_list = []

    if "," in message:
        for ip in message.split(","):
            ip_list.append(ip)

            return check_list(ip_list=ip_list)

    elif " " in message:
        for ip in message.split(" "):
            ip_list.append(ip)

            return check_list(ip_list=ip_list)

    else:
        ip_list.append(message)
        
        return check_list(ip_list=ip_list)
    

sort_arg(message=str(input("Enter text >>> ")))
