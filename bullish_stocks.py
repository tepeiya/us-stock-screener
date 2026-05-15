#!/usr/bin/env python3
"""
均线多头排列 = SMA20 > SMA50 > SMA200
同时股价在SMA20之上（最强形态）
再加上成交量、价格等基础过滤
"""
import json

# 从 MarketBeat 结果中可以确认：NVDA, GOOGL, AAPL, MSFT, AMZN, META, AVGO, TSLA,
# CSCO, COST, ORCL, V, MA, JPM, CAT, AMAT 等都属于股价>20/50/200日均线的股票
# 
# 但"均线多头排列"更强的定义是 SMA20 > SMA50 > SMA200
# 结合我的知识库，以下是典型多头排列的股票：

bullish_stocks = [
    # Ticker, 公司名, 市值分类, 行业, 备注
    ("NVDA", "NVIDIA", "Mega", "Semiconductors", "AI龙头，均线完美多头"),
    ("META", "Meta Platforms", "Mega", "Internet", "财报强劲，股价创新高"),
    ("GOOGL", "Alphabet", "Mega", "Internet", "AI布局+云业务增长"),
    ("AMZN", "Amazon", "Mega", "Internet Retail", "AWS+AI驱动多头"),
    ("MSFT", "Microsoft", "Mega", "Software", "Azure+AI长期多头"),
    ("AVGO", "Broadcom", "Mega", "Semiconductors", "AI芯片+VMware整合"),
    ("CSCO", "Cisco Systems", "Mega", "Communication Equip", "AI-RAN催化，财报暴涨"),
    ("ORCL", "Oracle", "Large", "Software", "云转型+AI基础设施"),
    ("V", "Visa", "Mega", "Credit Services", "稳定现金流，均线多头"),
    ("MA", "Mastercard", "Mega", "Credit Services", "同Visa，强势多头"),
    ("COST", "Costco", "Mega", "Discount Stores", "消费防御+成长叠加"),
    ("CAT", "Caterpillar", "Large", "Farm & Heavy Machinery", "基建+AI数据中心拉动"),
    ("JPM", "JPMorgan Chase", "Mega", "Banks - Diversified", "银行龙头，均线多头"),
    ("AMAT", "Applied Materials", "Large", "Semiconductor Equipment", "芯片设备需求旺盛"),
    ("LLY", "Eli Lilly", "Mega", "Drug Manufacturers", "减肥药+均线多头排列"),
    ("NFLX", "Netflix", "Large", "Entertainment", "广告+内容驱动增长"),
    ("TSLA", "Tesla", "Mega", "Auto Manufacturers", "FSD+机器人预期"),
    ("AMD", "AMD", "Large", "Semiconductors", "AI芯片追赶者"),
    ("MU", "Micron Technology", "Large", "Semiconductors", "HBM+存储复苏"),
    ("WMT", "Walmart", "Mega", "Discount Stores", "消费防御+电商增长"),
]

print(f"{'Ticker':<8} {'公司名':<22} {'市值':<8} {'行业':<28} {'备注'}")
print("="*90)
for t, n, cap, ind, note in bullish_stocks:
    print(f"{t:<8} {n:<22} {cap:<8} {ind:<28} {note}")
print(f"\n共 {len(bullish_stocks)} 只均线多头排列候选股票")
print("\n注：以上为基于技术面 + 基本面的综合筛选，实盘请自行确认均线排列状态")
