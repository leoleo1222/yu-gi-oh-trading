import asyncio
import pandas as pd
from pyppeteer import launch

async def scrape(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    data = []
    elements = await page.querySelectorAll('.card_unit')
    for element in elements:
        rarity = await page.evaluate('(element) => element.className.split(" ")[1]', element)
        rarity = rarity.replace("rarity_", "")
        name_element = await element.querySelector('.name')
        name = await page.evaluate('(element) => element.textContent', name_element)
        price_element = await element.querySelector('.price_box .price')
        price = await page.evaluate('(element) => element.textContent', price_element)
        # Extract only digits from price string
        price = int(''.join(filter(str.isdigit, price))) * 0.06
        data.append({'Rarity': rarity, 'Name': name.strip(), 'Price': price})

    await browser.close()

    return pd.DataFrame(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # 1111 [PHHY] PHOTON HYPERNOVA
    df1 = loop.run_until_complete(scrape('https://yuyu-tei.jp/game_ygo/sell/sell_price.php?ver=phhy'))
    # 1112 [CYAC] CYBERSTORM ACCESS
    df2 = loop.run_until_complete(scrape('https://yuyu-tei.jp/game_ygo/sell/sell_price.php?ver=cyac'))
    # Concatenate the two dataframes vertically
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Print the merged dataframe
    print(merged_df)

    # Save the merged dataframe as a JSON file
    merged_df.to_json('merged_data.json', orient='records')

    