from playwright.sync_api import sync_playwright

def start_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return p, browser, context, page