import os
from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  try:
    browser = p.chromium.connect_over_cdp('http://localhost:9220')
  except:
    os.system("xvfb-run -a chromium-browser --remote-debugging-port=9220 --no-sandbox --disable-gpu &")
    while True:
      try:
        browser = p.chromium.connect_over_cdp('http://localhost:9220')
        break
      except:
        sleep(1)
  print("starting")
  page = browser.new_page()
  page.goto("https://wizzair.com/en-gb#/booking/select-flight/WAW/MAD/2022-10-17/null/1/0/0/null")
  print("waiting")
  page.click("button >> text=Allow all", timeout=0)
  # input()
  try:
    print("format 1")
    price = page.locator('[data-test="current-price"]').first.inner_text().replace("‎", "")
  except:
    print("format 2")
    price = page.locator('[data-test="fare-type-button"] span').first.inner_text().replace("‎", "")
  open("result.txt", "w").write(price)
  print("done")