import streamlit as st




st.write ("V2.2 Making Home Page...20250127")

st.html('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinPal – Invest Smarter, Stress Less</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .tagline {
            text-align: center;
            font-size: 1.5em;
            color: #3498db;
            margin-bottom: 30px;
            font-weight: bold;
        }
        p {
            margin-bottom: 15px;
        }
        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
        .cta {
            text-align: center;
            margin-top: 30px;
        }
        .cta a {
            background-color: #3498db;
            color: #fff;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
        }
        .cta a:hover {
            background-color: #2980b9;
        }
        .image-container {
            text-align: center;
            margin: 20px 0;
        }
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to FinPal</h1>
        <div class="tagline">Invest Smarter, Stress Less.</div>
        
        <!-- Image Section -->
        <div class="image-container">
            <img src="https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/blog/finance/difference-between-money-finance-funds-717X404.jpg" alt="FinPal Portfolio Management">
        </div>

        <p>Managing your money shouldn’t be complicated. At <span class="highlight">FinPal</span>, we help you take control of your financial future with smart, effortless portfolio management.</p>
        <p>Think of your investments as a garden. Over time, some plants (stocks, bonds, etc.) grow faster than others, throwing your garden out of balance. <span class="highlight">Portfolio rebalancing</span> is like tending to your garden—it ensures everything grows in harmony, aligning with your goals and risk tolerance.</p>
        <p>Why does this matter?</p>
        <ul>
            <li><span class="highlight">Stay on Track</span>: Markets change, and so do your investments. Rebalancing keeps your portfolio aligned with your plan.</li>
            <li><span class="highlight">Manage Risk</span>: Prevent one investment from dominating your portfolio and increasing risk.</li>
            <li><span class="highlight">Achieve Your Goals</span>: Whether it’s retirement, a dream home, or your child’s education, rebalancing keeps your money working for you.</li>
        </ul>
        <p>With <span class="highlight">FinPal</span>, portfolio management is simple. Our tools monitor your investments, alert you when adjustments are needed, and guide you every step of the way—no expertise required.</p>
        <p><span class="highlight">Your future is too important to leave to chance.</span> Let <span class="highlight">FinPal</span> help you grow your wealth wisely.</p>
        <div class="cta">
            <a href="#signup">Get Started Today</a>
        </div>
    </div>
</body>
</html>
''')