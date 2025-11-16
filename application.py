from playwright.sync_api import sync_playwright
import pandas as pd

BASE_URL = "https://appexchange.salesforce.com"

def get_links(page, number_show):
    links = []
    href_list = page("a.card-target").evaluate_all(
        "els => els.map(e => e.href)"
    )
    for href in href_list:
        if href not in links:
            links.append(href)
    for _ in range(number_show):
        show_more = page.get_by_role("button", name="Show More")
        show_more.click()
        page.wait_for_timeout(2000)
        href_list = page("a.card-target").evaluate_all(
            "els => els.map(e => e.href)"
        )
    return links
def open_links(page, links):
    results = []

    for url in links:
        page.goto(url, timeout=90000)
        page.wait_for_timeout(2000)
        title = page.get_by_role("heading").first.inner_text().strip()
        rating = ""
        if page("ax-star-rating").count() > 0:
            rating = page("ax-star-rating").first.get_attribute("value")
        reviews = page("a:has-text('Reviews')").first.inner_text().strip().split()[0]
        texts = page('[data-testid="pricing-summary-headline"]').all_text_contents()
        price = texts[0].strip() if texts else ""
        results.append({
            "url": url,
            "title": title,
            "rating": rating,
            "reviews": reviews,
            "price": price
        })
    return results
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(BASE_URL, timeout=90000)
    page.wait_for_timeout(2000)

    search = page("Search AppExchange")
    search.click()
    search.fill("web")
    search.press("Enter")
    page.wait_for_timeout(4000)
    
    links = get_links(page, 3)
    links=links[:5]
    results = open_links(page, links)
    browser.close()
df=pd.DataFrame(results)
df.to_excel("application.xlsx")
print(df)
