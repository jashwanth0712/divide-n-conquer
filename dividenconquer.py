import webbrowser
d={
   "dataset1.csv":"bafybeigdyzkgh3lvgnqhjws4h37djirgo7d5mg4v2h2ustoqc775tqouna",
    "dataset2.csv":"bafybeic5vbddejok5m3avq5zru242qstzxwrv2acwcs4yogsb4giciepo4"
}
Logo="""
  ____    _           _       _
 |  _ \  (_) __   __ (_)   __| |   ___           _ __             ___    ___    _ __     __ _   _   _    ___   _ __ 
 | | | | | | \ \ / / | |  / _` |  / _ \  _____  | '_ \   _____   / __|  / _ \  | '_ \   / _` | | | | |  / _ \ | '__|
 | |_| | | |  \ V /  | | | (_| | |  __/ |_____| | | | | |_____| | (__  | (_) | | | | | | (_| | | |_| | |  __/ | |   
 |____/  |_|   \_/   |_|  \__,_|  \___|         |_| |_|          \___|  \___/  |_| |_|  \__, |  \__,_|  \___| |_|   
                                                                                           |_|
"""
def download_first():
    print(Logo)
    file_name="dataset1.csv"
    link="https://"+d[file_name]+".ipfs.w3s.link/"+file_name
    webbrowser.open(link)

def download_next():
    print("Downloading next")
    file_name="dataset2.csv"
    link="https://"+d[file_name]+".ipfs.w3s.link/"+file_name
    webbrowser.open(link)