import requests
from termcolor import colored


def check_list(ip_list: list):
    """Функция принимает в список адресов, проверяет на валидность, взаимодействует с 
    API сервиса ip-api.com и печатает результат. Если Status==fail, печатает предупреждение
    и продолжает работу дальше по валидным адресам."""

    if "" in ip_list:
        print(colored("ERROR: Empty request", "red"))

    else:
        try:
            for ip in ip_list:
                response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
                result = dict(IP=colored(ip, "green"),
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
                              Reverse=response.get("reverse")
                              )

                for k, v in result.items():
                    if result["Status"] == "fail":
                        invalid_ip = ip
                        print(colored(f"WARNING: Invalid IP - {invalid_ip}", "red"))

                        break
                    
                    else:
                        
                        print(k, v)

        except requests.ConnectionError:
            print(colored("ERROR: No connection", "red"))

        
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
            
    elif "," or " " not in message:
        ip_list.append(message)

        return check_list(ip_list=ip_list)

    else:
        print("Input Error, try again!")

        return sort_arg(message=str(input("Enter text >>> ")))
    

sort_arg(message=str(input("Enter text >>> ")))
