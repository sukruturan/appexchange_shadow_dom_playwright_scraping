from playwright.sync_api import sync_playwright
import pandas as pd

BASE_URL = "https://appexchange.salesforce.com"

def get_links(page, number_show):
    links = []

    # İlk linkleri al
    href_list = page.locator("a.card-target").evaluate_all(
        "els => els.map(e => e.href)"
    )
    for href in href_list:
        if href not in links:
            links.append(href)

    # Show More tıklama
    for _ in range(number_show):
        show_more = page.get_by_role("button", name="Show More")

        if not show_more.is_visible() or show_more.is_disabled():
            break

        show_more.click()
        page.wait_for_timeout(2000)

        # yeni gelen linkler
        href_list = page.locator("a.card-target").evaluate_all(
            "els => els.map(e => e.href)"
        )
        for href in href_list:
            if href not in links:
                links.append(href)

    return links

def open_links(page, links):
    results = []

    for url in links:
        page.goto(url, timeout=90000)
        page.wait_for_timeout(2000)

        # --- Title ---
        title = page.get_by_role("heading").first.inner_text().strip()

        # --- Rating ---
        rating = ""
        if page.locator("ax-star-rating").count() > 0:
            rating = page.locator("ax-star-rating").first.get_attribute("value")

        # --- Reviews ---
        reviews = page.locator("a:has-text('Reviews')").first.inner_text().strip().split()[0]

        # --- Price ---
        texts = page.locator('[data-testid="pricing-summary-headline"]').all_text_contents()
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

    search = page.get_by_placeholder("Search AppExchange")
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