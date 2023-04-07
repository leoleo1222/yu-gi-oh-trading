# Yu-Gi-Oh!
Price analysis for trading card games:


## - Feature1: Assuming there's a list of dataframes (like 100 boosters in total) to merge:
```python
    # Define a list of dataframes to merge
    df_list = [df1, df2, df3, ..., df100]
    # Concatenate the dataframes vertically using a loop
    merged_df = pd.DataFrame()
    for df in df_list:
    merged_df = pd.concat([merged_df, df], ignore_index=True)
```

## - Feature2: Implement a search function -> calling Yuyutei's url 

    (e.g. https://yuyu-tei.jp/game_ygo/sell/sell_price.php?name=HERO) and return the result as a dataframe

