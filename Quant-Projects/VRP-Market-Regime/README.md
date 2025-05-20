Variance Risk Premium (VRP) Strategy & Market Regime Classification
This project explores the Variance Risk Premium (VRP) using historical data from NIFTY 50 and India VIX. The idea was inspired by the research paper "Variance Risk Premium" by Carr and Wu (2009).

🔍 What This Project Covers
Understanding and calculating VRP using market index and VIX

Exploring how VRP behaves over time

Testing whether VRP can classify market regimes (risk-on vs. risk-off)

Performing basic backtests using VRP-based trading signals

Monte Carlo simulation to test performance robustness

⚠️ This project applies VRP to the underlying index (NIFTY) directly — not options — due to lack of historical option chain data.

📁 Files Included
VRP_Strategy.ipynb: Main Jupyter notebook with full code and visualizations

Nifty 50 Historical Data.csv: NIFTY price data

India VIX Historical Data.csv: India VIX data

⚙️ Requirements
Python 3.x

pandas

numpy

matplotlib

yfinance (if fetching live data)

📊 Key Plots
VRP over time (2015–2025)

VIX vs. NIFTY comparison

Distribution of VRP

Strategy performance vs. NIFTY returns

Monte Carlo return distribution

📌 Conclusion
While VRP was helpful in identifying volatility mispricing and fear in the market, it did not produce a robust trading signal when applied to the index directly. However, the insights can still be useful for regime detection or building option strategies.

🔗 Related Resources
Research Paper: [Carr and Wu (2009)](https://engineering.nyu.edu/sites/default/files/2019-01/CarrReviewofFinStudiesMarch2009-a.pdf)

AQR Whitepaper: [Understanding the Volatility Risk Premium](https://www.aqr.com/-/media/AQR/Documents/Whitepapers/Understanding-the-Volatility-Risk-Premium.pdf)

🤝 Connect With Me
If you're into quant research or just want to discuss cool ideas:
📬 [LinkedIn](https://www.linkedin.com/in/roshan-zambare-304905253/)

Feel free to connect or collaborate!
