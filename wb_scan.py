import requests
import subprocess
import json

test_article = "211690467"
vol = test_article[:4]
part = test_article[:6]

urls = [
    "https://wb.ru",
    "https://www.wildberries.ru",
    "https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm=" + test_article,
    "https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm=" + test_article,
    "https://catalog.wb.ru/catalog/electronic/catalog?appType=1&curr=rub&dest=-1257786&spp=30&nm=" + test_article,
    "https://catalog.wb.ru/catalog/electronic2/catalog?appType=1&curr=rub&dest=-1257786&spp=30&nm=" + test_article,
    "https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1257786&spp=30&query=" + test_article,
    "https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1257786&spp=30&query=" + test_article,
    "https://product-order.wb.ru/api/v1/order?nm=" + test_article,
    "https://product-reviews.wb.ru/api/v1/reviews?nm=" + test_article,
    "https://product-questions.wb.ru/api/v1/questions?nm=" + test_article,
    "https://feedbacks.wb.ru/api/v1/feedbacks?nm=" + test_article,
    "https://static.wb.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://static-basket-01.wb.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-01.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-02.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-03.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-04.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-05.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-06.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-07.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-08.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-09.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-10.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-11.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-12.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-13.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-14.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-15.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-16.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-17.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-18.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-19.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-20.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-21.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-22.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-23.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json",
    "https://basket-24.wbbasket.ru/vol" + vol + "/part" + part + "/" + test_article + "/info/ru/card.json"
]

for i in range(1, 25):
    urls.append(f"https://basket-{i:02d}.wbbasket.ru/vol{vol}/part{part}/{test_article}/info/ru/card.json")

working_urls = []

for url in urls:
    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            text = r.text.lower()
            if "products" in text or "priceu" in text:
                print(f"[РАБОТАЕТ] requests: {url}")
                working_urls.append(url)
    except:
        pass

    try:
        result = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url], capture_output=True, text=True, timeout=5)
        if result.stdout == "200":
            result2 = subprocess.run(["curl", "-s", url], capture_output=True, text=True, timeout=5)
            text = result2.stdout.lower()
            if "products" in text or "priceu" in text:
                print(f"[РАБОТАЕТ] curl: {url}")
                if url not in working_urls:
                    working_urls.append(url)
    except:
        pass

print("\n=== ИТОГОВЫЙ РЕЗУЛЬТАТ ===")
print(f"Найдено рабочих URL: {len(working_urls)}")
for u in working_urls:
    print(u)
