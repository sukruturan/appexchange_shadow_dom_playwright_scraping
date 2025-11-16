# Salesforce AppExchange Scraper (Playwright + Shadow DOM) — Demo Version

This repository contains a **demo version** of the Salesforce AppExchange scraper built with **Playwright**.  
The scraper was recently **updated and improved**, especially for handling the complex **shadow DOM** structure used on AppExchange listings.

### ✔ What was fixed & improved
- Correct extraction of **price** (including “Starting at” values inside shadow DOM)
- Correct extraction of **review count** (e.g., “317 Reviews” → **317**)
- More stable selectors for:
  - Title
  - Rating
  - Reviews
  - Pricing
- Cleaner, simplified demo code (full version available upon request)

### ✔ About this demo
This repository shows:
- Example Playwright code  
- Shadow DOM traversal  
- Listing information extraction  
- Limited sample scraping (not the full production script)

The **full version** includes advanced features such as:
- Pagination  
- Multiple category crawling  
- Error handling & retries  
- Proxy/User-Agent rotation  
- Export to CSV/Excel  
- Full dataset extraction  

➡️ The full version is not included here for safety and privacy reasons,  
but can be delivered privately if needed.

---

## 📹 Demo Video (Scraper Running Live)

You can watch the scraper working here:  
👉 **[Demo Video Link](YOUR_VIDEO_LINK_HERE)**

---

## 📄 How it works
The script uses:
- `sync_playwright`
- Shadow DOM-safe locators
- Text extraction from dynamic components

Example extracted fields:
