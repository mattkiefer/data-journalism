# async allows python to wait for pages to load before proceeding
import asyncio
# playwright has a dedicated async api
from playwright.async_api import async_playwright

# configs
igb_url = "https://igb.illinois.gov/sports-wagering/sports-reports.html"
output_dir = 'igb_csv_downloads'


async def download_igb_reports():
    """
    get the main page,
    loop through every month,
    downloading reports
    """
    async with async_playwright() as p:
        # opening the browser so we can see it work
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # navigate to igb sports page
        print("navigating to",igb_url)
        await page.goto(igb_url)
    
        # select the iframe
        frame_element = page.frame_locator("iframe[src*='igbapps.illinois.gov']")
        
        # get all years from the dropdown
        year_start_selector = "select[id$='SearchStartYear']"
        year_end_selector = "select[id$='SearchEndYear']"
        
        years = await frame_element.locator(year_start_selector).locator("option").all_text_contents()

        # loop through years
        for year in years:
            print(year)
            await frame_element.locator(year_start_selector).select_option(label=year)
            await frame_element.locator(year_end_selector).select_option(label=year)
            
            # get all months for the selected year
            month_start_selector = "select[id$='SearchStartMonth']"
            month_end_selector = "select[id$='SearchEndMonth']"
            months = await frame_element.locator(month_start_selector).locator("option").all_text_contents()
            
            # now loop thru months
            for month in months:
                print(f"downloading: {month} {year}...")
                await frame_element.locator(month_start_selector).select_option(label=month)
                await frame_element.locator(month_end_selector).select_option(label=month)

                
                # toggle the csv radio button
                try:
                    async with page.expect_download(timeout=1000) as download_info:
                        # locate csv button
                        await frame_element.locator("input[id='ViewCSV']").check()
                        # locate search button
                        await frame_element.locator("input[id='ButtonSearch']").click()
                        # check for errors
                        if await frame_element.locator("div.error").count():
                            print('error', year, month)
                            continue
                    download = await download_info.value
                    
                    # Save with a descriptive name
                    safe_month = month.replace(" ", "_")
                    file_path = output_dir + '/' + f"sports_report_{year}_{safe_month}.csv"
                    await download.save_as(file_path)
                    print(f"saved to: {file_path}")
                
                except Exception as e:
                    print(f"failed to download {month} {year}: {e}")

        await browser.close()


# run the function when you run the file
if __name__ == "__main__":
    asyncio.run(download_igb_reports())

