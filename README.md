# MSDNProToTyper
Grab Function Prototypes from MSDN url's

```
C:\python.exe C:\Automated_Builder\function_prototyper.py -h
usage: function_prototyper.py [-h] (-u URL | -f FILE)

Grab Function Prototypes from MSDN docs

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url to fetch funcprot from
  -f FILE, --file FILE  Url file to fetch funcprots from
```


```
C:\python.exe C:\Automated_Builder\MSDNProToTyper.py -u https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress
FARPROC GetProcAddress(
  HMODULE hModule,
  LPCSTR  lpProcName
);
```

```
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
```
