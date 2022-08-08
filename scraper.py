from colorama import Fore

def main():
    from http.server import HTTPServer, CGIHTTPRequestHandler
    server_address = ("", 8000)
    httpb = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpb.serve_forever()

if __name__ == '__main__':
    main()
else:
    print(Fore.RED + 'ERROR this file is not a lib!')