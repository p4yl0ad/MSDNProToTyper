######################################################################
#                       Inspiration from                             #
#              Ben Heimerdinger and Sebastian Feldmann               #
#                       PIC Your Malware!                            #
#                                                                    #
#                     Author: p4yl0ad/p.load                         #
#                         MSDNProToTyper.py                          #
#                  Something i wrote while drunk                     #
#                    wedoalittlebitoftoolingkek                      #
######################################################################

"""
Example:
C:\python.exe C:\Automated_Builder\MSDNProToTyper.py -u https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress
FARPROC GetProcAddress(
  HMODULE hModule,
  LPCSTR  lpProcName
);
"""

"""
C:\python.exe C:\Automated_Builder\MSDNProToTyper.py -f .\apis.txt
FARPROC GetProcAddress(
  HMODULE hModule,
  LPCSTR  lpProcName
);

LPVOID VirtualAllocEx(
  HANDLE hProcess,
  LPVOID lpAddress,
  SIZE_T dwSize,
  DWORD  flAllocationType,
  DWORD  flProtect
);
[...SNIP...]
"""
import requests, argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def main():
    parser = argparse.ArgumentParser(description="Grab Function Prototypes from MSDN docs")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", type=str, help="Url to fetch funcprot from")
    group.add_argument("-f", "--file", type=str, help="Url file to fetch funcprots from")
    args = parser.parse_args()
    

    if args.url:
        request(args.url)

    if args.file:
        fromfile(args.file)

def fromfile(filename):
    try:
        with open(filename, "r") as file:
            data = file.read().splitlines()
            for linenum,url in enumerate(data):
                request(url)
                
    except Exception as e:
        print("Nani?: ", e)

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False
    
def request(url):
    print(url)
    if not is_url(url):
        print("Pass a valid url you cuck")
        
        # do something here
        raise SystemExit
          
    page = requests.get(url)
    if page.status_code == 200:
        parse(page.content)
    
def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.find_all('pre')[0].get_text())
    
    
if __name__ == "__main__":
    main()
