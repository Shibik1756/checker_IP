import requests
from termcolor import colored


def displayData(ip_list: list):
    """Checks the correctness of the data entered by the user and prints the result"""

    if "" in ip_list:
        print(colored("ERROR: Empty request", "red"))

    else:
        try:
            for ip in ip_list:
                response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
                result = dict(IP=colored(ip, "green"),
                              Status=response.get("status"),
                              Country=response.get("country"),
                              Country_Code=response.get("countryCode"),
                              Region=response.get("region"),
                              Region_name=response.get("regionName"),
                              City=response.get("city"),
                              Isp=response.get("isp"),
                              Org=response.get("org"),
                              As_data=response.get("as"),
                              As_name=response.get("asname"),
                              Reverse=response.get("reverse"),
                              Hosting=response.get("hosting"),
                              Proxy=response.get("proxy")
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
    """The function takes user parameters and passes them to displayData()"""
    
    ip_list = []

    if "," in message:
        for ip in message.split(","):
            ip_list.append(ip)

        return displayData(ip_list=ip_list)

    elif " " in message:
        for ip in message.split(" "):
            ip_list.append(ip)
        
        return displayData(ip_list=ip_list)
            
    elif "," or " " not in message:
        ip_list.append(message)

        return displayData(ip_list=ip_list)

    else:
        print("Input Error, try again!")

        return sort_arg(message=str(input("Enter text >>> ")))
