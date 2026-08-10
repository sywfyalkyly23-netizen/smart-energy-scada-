import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Simulate iPhone 13 Pro Max viewport
        device = p.devices['iPhone 13 Pro Max']
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(**device)
        page = await context.new_page()

        print("Navigating to local Streamlit on Port 3000...")
        await page.goto("http://localhost:3000")

        # Wait for Streamlit loading to complete
        await page.wait_for_timeout(4000)

        # Take screenshot of home page
        print("Taking screenshot of Home tab...")
        await page.screenshot(path="verification_iphone_home.png")

        # Click on the Rooms tab ("🎛️ الغرف")
        print("Navigating to Rooms tab...")
        rooms_tab = page.locator('button:has-text("🎛️ الغرف")')
        if await rooms_tab.is_visible():
            await rooms_tab.click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path="verification_iphone_rooms.png")

            # Click on control deck of the first room
            print("Clicking into first room's controller...")
            enter_room_btn = page.locator('button:has-text("🔑 فتح لوحة تحكم")').first
            if await enter_room_btn.is_visible():
                await enter_room_btn.click()
                await page.wait_for_timeout(2000)
                await page.screenshot(path="verification_iphone_room_details.png")

        # Click on the AI tab ("💬 الذكاء")
        print("Navigating to AI Chatbot tab...")
        ai_tab = page.locator('button:has-text("💬 الذكاء")')
        if await ai_tab.is_visible():
            await ai_tab.click()
            await page.wait_for_timeout(2000)

            # Send an AI question
            print("Interacting with the AI chatbot input...")
            input_box = page.get_by_role("textbox")
            if await input_box.is_visible():
                await input_box.fill("ما هو هذا التطبيق وكيف يتم حماية الشبكة؟")
                await page.keyboard.press("Enter")
                await page.wait_for_timeout(3000)
                await page.screenshot(path="verification_iphone_ai.png")

        await browser.close()
        print("Verification complete! Saved screenshots.")

if __name__ == "__main__":
    asyncio.run(main())
