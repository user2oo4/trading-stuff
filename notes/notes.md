# Chapter 2: Where can we find good strategies?

## How to find strategies
- Simpler strategies may work better than complicated papers
- Most ready-made strategies do not withstand careful backtesting
- However, you can modify basic strategy and make it profitable
=> Try multiple variations of a basic strategy
![alt text](table-2-1.png)

## How to identify a strategy that suits you
- Working hours: High automation will help with this
- Programming skills
- Trading capital
- ![alt text](table-2-2.png)
- Goal
  - The more regular the profits and income, the shorter the holding period should be
  - Maximize the Sharpe ratio

## A taste for plausible strategies and their pitfalls

### Some definitions
- Futures: These are agreements between two parties to exchange a specific asset (like a commodity, currency, or stock index) at a fixed price on a future date
- Long: Expect profit -> buy = make profit
- Short: Expect deficit -> sell = make profit
- Excess Returns = Portfolio returns - Benchmark returns
- Benchmark returns: The market index to which the securities you are trading belong.

### Number of quick checks before backtesting/trading to save time and money
- Comparison with benchmark, how consistent are returns?

**Information Ratio (Sharpe ratio)**
- Use when assessing a long-only strategy
- Information Ratio = Avg. Excess Returns / Std Dev. Excess Returns
- Sharpe ratio: special case of information ratio (suitable for dollar-neutral strategy (long = short)) => benchmark to use is always the risk-free rate.
- Higher sharpe ratio -> more profits (allows to trade at a higher leverage, it's the leveraged return that matters in the end)
- How to figure out the sharpe ratio of a strategy:
  - Email the author
  - Educated guess:
    - If a strategy trades only a few times a year, Sharpe ratio are likely not high
    - Deep (>10%) or length (4+ months) drawdowns -> unlikely to have high Sharpe ratio.
    - Drawdown: ![alt text](figure-2-1.png)
    - Values
      - <1: Not suitable as a stand-alone strat
      - 2: profitable every month
      - 3: profitable almost everyday 

### Drawdown
- Definition
  - Time t
  - global max - current value
  - Max drawdown: Max (global max (at time t) - value (time t))
  - Max drawdown duration: Longest it has taken for the equity curve to recover losses
- How deep and long of a drawdown can you tolerate without shutting down the strategy?

### Transaction costs and its affect on the strategy



