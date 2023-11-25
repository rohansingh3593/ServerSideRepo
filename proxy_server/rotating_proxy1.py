import requests,os
import threading
import queue

q = queue.Queue()


valid_file = 'valid_proxiy_list'
os.remove(valid_file)


with open("proxy_list.txt", "r") as f:
    content1 = f.read().split("\n")
    # print(content1)
    for p in content1:
        if not 'Failed' in p:
            q.put(p)
        # with open("file.txt", "a") as secondfile:
        #     secondfile.write(p + '\n')


while not q.empty():
    proxy = q.get()
    with open("file.txt", "a") as secondfile:
        try:
            res = requests.get("http://ipinfo.io/json",proxies={"http": proxy,"https:": proxy})
        except:
            print(f'Failed {proxy}')
            secondfile.write(f'Failed {proxy}' + '\n')
            continue
        if res.status_code == 200:
            print(f'Sussessful {proxy}')
            print(f'Text {res.text}')
            secondfile.write(proxy + '\n')


# for _ in range(20):
#     threading.Thread(target=check_proxies).start()

with open(valid_file, "r") as f:
    content2 = f.read().split("\n")

print(content2)



