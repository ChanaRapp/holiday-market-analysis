# Jewish Holidays and US Stock Market Trade Volume: A Longitudinal Look

A semester project building on *The Impact of Jewish Holidays on US Market*, a thesis by Robert Aeder. Where that work asks whether Jewish holidays affect US market trade volume, this project asks whether the size of that effect has **changed over time**, and whether those changes track shifts in Jewish religiosity.

## Hypothesis

Two trends are commonly observed in the American Jewish community:

- Some Jews are becoming more religious, increasingly observing the three Pilgrimage Festivals (Passover, Shavuot, Sukkot).
- Many less-religious Jews are becoming even less connected, no longer observing Yom Kippur.

If these trends affect who is trading, then over many years:

- The **drop** in trade volume on **Yom Kippur** should shrink slightly.
- The **drop** in trade volume on the **Pilgrimage Festivals** should grow slightly.

If this holds, changing religiosity among Jews may measurably affect the stock market, and/or the stock market may serve as a valid indicator of trends in the Jewish community.

## Data Sources

| Source | Coverage | Outcome |
|---|---|---|
| [Stooq](https://stooq.com) | Per-ticker daily volume, back to the 1960s | Volume figures appeared inconsistent and inaccurate when checked against volumes reported in the news. Results not significant. |
| Cboe market data | Starting 2009 | More consistent, but accuracy could not be verified and the range was short. Results not significant. |
| Bloomberg Terminal (via the YU library) | Nasdaq from 2001, NYSE from 2003 | Considered the most reliable. **Results confirmed the hypothesis.** |
| [`theworld.com/~reinhold/jewishholidays.txt`](http://theworld.com/~reinhold/jewishholidays.txt) and [Hebcal](https://www.hebcal.com) | Jewish holiday dates, past 65 years | Used to build a complete list of holiday dates. |

## Methodology

1. **Holiday dates.** Combined the Reinhold text file and Hebcal data into one comprehensive list, then reformatted it uniformly and filtered it down to **Yom Kippur and the Pilgrimage Festivals** only.
2. **Combining volume data.** For each market data source, used a `find` command to merge the many split files into a single text file:
   - *Stooq:* every stock market (excluding ETFs) combined with each ticker's individual subfile.
   - *Cboe:* all years combined.
   - *Bloomberg:* Nasdaq and NYSE combined.
3. **Daily totals.** Built a file of each date followed by its total trade volume, summing across all tickers/exchanges for that day.
4. **Holiday comparison.** For each holiday date with available data, extracted:
   - the date,
   - the trade volume on that day,
   - the average daily trade volume over the **month before** and the **month after**, computed by looping through all dates and accumulating those from the surrounding month in separate variables,
   - the holiday name.
5. **Plotting.** Graphed each holiday as one point on a scatter plot:
   - **x-axis:** year
   - **y-axis:** log of (holiday volume ÷ average volume of the surrounding months). The log is used to emphasize the results.
   - **Yom Kippur** in black, **Pilgrimage Festivals** in cyan.
   - A line of best fit for each group, to identify any correlation.

### Methodological Decisions

- **Baseline window.** I first compared each holiday to the same weekday one week earlier, then to an average of the same weekday one week before and two weeks after (to avoid second days of Yom Tov). Both approaches were too easily skewed by current events. Averaging the **entire month before and after** produced fewer outliers, since more data dampens the effect of news-driven spikes and drops.
- **2020 exclusion.** Even with the broader window, the March to June 2020 holidays were consistent outliers, which is understandable given the market volatility at the start of the Covid-19 pandemic. **2020 was removed from the Pilgrimage Festival data.**

## Results
<img width="1999" height="676" alt="image" src="https://github.com/user-attachments/assets/8138f8e1-085d-4982-8a09-e7b5e8a1651e" />

The Stooq and Cboe results were not significant. The **Bloomberg data confirmed the hypothesis**:

- In 2002, the Yom Kippur trend line starts below zero (about **-0.1**), indicating a drop in volume. The Pilgrimage Festival line starts near **zero**, indicating no drop.
- From 2002 to 2025, the Yom Kippur ratio **increased**, meaning the drop in volume got smaller. This suggests fewer Jewish traders observing Yom Kippur.
- Over the same period, the Pilgrimage Festival ratio **decreased**, meaning the drop in volume got larger. This suggests more Jewish traders observing the Pilgrimage Festivals.

## Limitations

These findings are suggestive, not conclusive:

- The span of years covered is limited, and so is the data used.
- The Yom Kippur data is especially limited, because the holiday frequently falls on a Saturday or Sunday, when the market is closed.

## Future Work

- Run the same study on a stock market in a country with a small or nonexistent Jewish population, as a control.
- Repeat the analysis across more years, including future ones.
- Compare the results against data documenting trends in Jewish religiosity in America.

## Repository Contents

<!--
- `scripts/` : data combining and processing scripts
- `plots/` : generated graphs
-->

## Notes on Data

<!-- The raw market data is not included in this repository because the files are too large and I do not have permission to redistribute all of it. Holiday dates and the data sources listed above can be used to reproduce the dataset. -->

## Acknowledgments

- Robert Aeder, *The Impact of Jewish Holidays on US Market* (the thesis this project builds on)
- Hebcal and Reinhold's Jewish holiday date lists
- Stooq, Cboe, and Bloomberg for market data
- The YU library, for Bloomberg Terminal access
