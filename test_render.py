import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:8080/index.html', wait_until='networkidle')
        
        # DOM check
        w = await page.evaluate("window.getComputedStyle(document.querySelector('.container')).maxWidth")
        cols = await page.evaluate("window.getComputedStyle(document.querySelector('.features-wrapper')).gridTemplateColumns")
        about_w = await page.evaluate("document.querySelector('.features-wrapper').getBoundingClientRect().width")
        
        print(f"Container max-width: {w}")
        print(f"Features wrapper width: {about_w}px")
        print(f"Grid columns (About Us): {cols}")
        
        cols2 = await page.evaluate("window.getComputedStyle(document.querySelector('.service-grid')).gridTemplateColumns")
        print(f"Grid columns (Services): {cols2}")
        
        await page.screenshot(path='full_screenshot.png', full_page=True)
        await browser.close()

asyncio.run(main())
