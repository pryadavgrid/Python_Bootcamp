import re


# Read File Line By Line
def read_log_file(file_path):
    try:
        file = open(file_path, "r")
        return True, file
    except Exception as e:
        return False, e


# Process Log File
def process_log(file):

    ip_count = {}
    endpoint_count = {}

    total_requests = 0
    total_success = 0
    total_client_error = 0
    total_server_error = 0

    ip_pattern = r"\d+\.\d+\.\d+\.\d+"

    for line in file:

        line = line.strip()
        if not line:
            continue

        total_requests += 1

        # Extract IP
        ip_match = re.search(ip_pattern, line)
        if ip_match:
            ip = ip_match.group()
            ip_count[ip] = ip_count.get(ip, 0) + 1

        parts = line.split()

        # Extract Endpoint safely
        if len(parts) > 5:
            endpoint = parts[5]
            endpoint_count[endpoint] = endpoint_count.get(endpoint, 0) + 1

        # Extract Status Code safely
        if len(parts) > 7:
            try:
                status_code = int(parts[-1])

                if status_code == 200:
                    total_success += 1
                elif 400 <= status_code < 500:
                    total_client_error += 1
                elif 500 <= status_code < 600:
                    total_server_error += 1

            except:
                continue

    file.close()

    return {
        "ip_count": ip_count,
        "endpoint_count": endpoint_count,
        "total_requests": total_requests,
        "total_success": total_success,
        "total_client_error": total_client_error,
        "total_server_error": total_server_error,
    }



# Show Log Statistics
def show_statistics(data):

    print("\n" + "-" * 10 + " Log Statistics " + "-" * 10)

    print(f"Total Requests       → {data['total_requests']}")
    print(f"Total Success (200)  → {data['total_success']}")
    print(f"Total Client Error   → {data['total_client_error']}")
    print(f"Total Server Error   → {data['total_server_error']}")

    print("-" * 40 + "\n")



# Show Top IPs
def show_top_ips(ip_dict, top_n):

    print("\n" + "-" * 10 + f" Top {top_n} IPs " + "-" * 10)

    sorted_ips = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)

    for index, (ip, count) in enumerate(sorted_ips[:top_n], start=1):
        print(f"{index}. {ip} → {count} requests")

    print("-" * 40 + "\n")



# Show Top Endpoints

def show_top_endpoints(endpoint_dict, top_n):

    print("\n" + "-" * 10 + f" Top {top_n} Endpoints " + "-" * 10)

    sorted_endpoints = sorted(endpoint_dict.items(), key=lambda x: x[1], reverse=True)

    for index, (endpoint, count) in enumerate(sorted_endpoints[:top_n], start=1):
        print(f"{index}. {endpoint} → {count} requests")

    print("-" * 40 + "\n")



# Main Menu
def main():

    file_path = "sample_log.txt"

    status, file = read_log_file(file_path)

    if not status:
        print("Error reading file:", file)
        return

    data = process_log(file)

    while True:

        print("1. Show Log Statistics")
        print("2. Show Top IPs")
        print("3. Show Top Endpoints")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input.\n")
            continue

        if choice == 1:
            show_statistics(data)

        elif choice == 2:
            top_n = int(input("How many top IPs you want: "))
            show_top_ips(data["ip_count"], top_n)

        elif choice == 3:
            top_n = int(input("How many top Endpoints you want: "))
            show_top_endpoints(data["endpoint_count"], top_n)

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()