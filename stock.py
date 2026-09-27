import os

def run_stock_tracker():
    print("📈 Welcome to the Simple Stock Tracker 📈\n")

    # 1. Hardcoded dictionary defining stock prices (2026 baseline values)
    STOCK_PRICES = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "MSFT": 420.00,
        "GOOGL": 175.00,
        "AMZN": 185.00
    }

    # Display available stock prices to the user
    print("Current Available Stocks and Market Prices:")
    for ticker, price in STOCK_PRICES.items():
        print(f"  • {ticker}: ${price:.2f}")
    print("-" * 45)

    portfolio = {}
    
    # 2. User Input Loop
    while True:
        ticker_input = input("Enter stock ticker symbol (or type 'done' to calculate): ").strip().upper()
        
        if ticker_input == 'DONE':
            break
            
        if ticker_input not in STOCK_PRICES:
            print(f"❌ '{ticker_input}' is not in our database. Please choose from: {', '.join(STOCK_PRICES.keys())}\n")
            continue

        # Get and validate the quantity input
        try:
            quantity = float(input(f"How many shares of {ticker_input} do you own?: "))
            if quantity < 0:
                print("❌ Quantity cannot be negative. Please try again.\n")
                continue
        except ValueError:
            print("❌ Invalid number. Please enter a valid number for shares.\n")
            continue

        # Add or update shares in the user's portfolio
        portfolio[ticker_input] = portfolio.get(ticker_input, 0) + quantity
        print(f"✅ Added {quantity} shares of {ticker_input} to calculation.\n")

    if not portfolio:
        print("\n👋 Portfolio is empty. Exiting tracker.")
        return

    # 3. Arithmetic: Calculate Holdings and Total Investment Value
    print("\n📊 --- YOUR INVESTMENT BREAKDOWN --- 📊")
    total_investment = 0.0
    report_lines = ["--- STOCK PORTFOLIO REPORT ---\n"]

    for ticker, quantity in portfolio.items():
        price = STOCK_PRICES[ticker]
        holding_value = quantity * price
        total_investment += holding_value
        
        breakdown_str = f"{ticker}: {quantity} shares @ ${price:.2f} = ${holding_value:.2f}"
        print(breakdown_str)
        report_lines.append(breakdown_str + "\n")

    summary_str = f"\n💰 Total Portfolio Value: ${total_investment:.2f}"
    print(summary_str)
    report_lines.append(summary_str)

    # 4. File Handling: Save Results to a Text File
    output_filename = "portfolio_summary.txt"
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.writelines(report_lines)
        print(f"\n💾 Success! Your report has been saved locally to '{output_filename}'.")
    except Exception as e:
        print(f"\n❌ Failed to save file: {e}")

# Run the tracker application
if __name__ == "__main__":
    run_stock_tracker()
