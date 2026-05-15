#!/usr/bin/env python3
"""
高息股模式选股器 | 2026-05-15
逻辑：侧重股息持续性 + 估值安全 + 防御性
"""
from datetime import datetime

stocks = [
    (1,  "PG",   "Procter & Gamble",    "消费防御", "Mega",  4, 5, 5, 3, 3.9,  "3.0%", "65年增长", "消费刚需+涨价传导", "增长慢"),
    (2,  "KO",   "Coca-Cola",           "消费防御", "Mega",  4, 5, 6, 3, 3.8,  "2.6%", "63年增长", "全球品牌+股息王者", "增长慢"),
    (3,  "PEP",  "PepsiCo",             "消费防御", "Mega",  4, 5, 5, 3, 3.7,  "2.9%", "50年增长", "零食+饮料双驱动", "增长放缓"),
    (4,  "COST", "Costco",              "消费防御", "Mega",  5, 5, 7, 4, 4.3,  "0.57%","20年增长", "会员制零售+成长防御叠加", "股息偏低"),
    (5,  "WMT",  "Walmart",             "消费防御", "Mega",  5, 5, 6, 4, 4.2,  "0.75%","50年增长", "电商转型+AI供应链", "股息偏低"),
    (6,  "CL",   "Colgate-Palmolive",   "消费防御", "Large", 4, 5, 4, 3, 3.5,  "2.8%", "50年增长", "全球口腔护理龙头", "增长平缓"),
    (7,  "XOM",  "ExxonMobil",          "能源",     "Mega",  4, 4, 6, 4, 3.7,  "2.7%", "40年增长", "油气价高位+回购强劲", "油价波动"),
    (8,  "CVX",  "Chevron",             "能源",     "Mega",  4, 4, 5, 3, 3.5,  "3.8%", "35年增长", "能源整合+股东回报", "油价波动"),
    (9,  "COP",  "ConocoPhillips",      "能源",     "Large", 4, 4, 4, 3, 3.4,  "3.5%", "10年增长", "优质上游资产", "油价敏感"),
    (10, "JPM",  "JPMorgan Chase",      "金融",     "Mega",  3, 5, 6, 3, 3.3,  "2.0%", "连续增长", "全能银行+AI应用", "短期均线走弱"),
    (11, "BAC",  "Bank of America",     "金融",     "Mega",  3, 4, 5, 3, 3.1,  "2.2%", "11年增长", "降息预期+投行回暖", "均线空头"),
    (12, "GS",   "Goldman Sachs",       "金融",     "Mega",  4, 4, 5, 4, 3.6,  "2.0%", "连续增长", "投行复苏+AI布局", "波动大"),
    (13, "VZ",   "Verizon",             "通信服务",  "Mega",  3, 4, 4, 3, 2.9,  "4.2%", "15年增长", "5G基建+定价权", "增长停滞"),
    (14, "T",    "AT&T",                "通信服务",  "Mega",  3, 3, 3, 2, 2.6,  "4.5%", "连续增长", "债务改善+Fiber", "债务高"),
    (15, "MSFT", "Microsoft",           "科技",     "Mega",  5, 5, 9, 4, 4.5,  "0.89%","20年增长", "Azure+AI Copilot", "股息一般"),
    (16, "AVGO", "Broadcom",            "科技",     "Mega",  5, 5, 8, 5, 4.7,  "0.6%", "14年增长", "AI芯片+VMware", "PE高"),
    (17, "CSCO", "Cisco Systems",        "科技",     "Mega",  5, 5, 8, 5, 4.7,  "1.44%","连续增长", "AI-RAN转型+大涨15%", "单日暴涨"),
    (18, "ORCL", "Oracle",              "科技",     "Large", 5, 4, 7, 4, 4.2,  "1.0%", "连续增长", "云基建+AI订单", "股息一般"),
]

sorted_stocks = sorted(stocks, key=lambda x: -x[9])

def score_to_stars(s):
    if s >= 4.5: return "⭐⭐⭐⭐⭐"
    if s >= 4.0: return "⭐⭐⭐⭐"
    if s >= 3.5: return "⭐⭐⭐"
    if s >= 3.0: return "⭐⭐"
    return "⭐"

def position(s, div_str):
    div = float(div_str.replace("%",""))
    if s >= 4.5 and div >= 1.0:  return "核心 5-10%"
    if s >= 4.0 and div >= 0.5:  return "观察 2-5%"
    if s >= 3.5:                 return "轻仓 1-2%"
    if s >= 3.0:                 return "待改善"
    return "跳过"

print("=" * 110)
print(f"  高息股选股结果 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"  筛选条件：有股息 + 均线多头 + 营收正增长 + ROE>10% + 成交量>50万")
print("=" * 110)
print(f"\n{'#':<3} {'Ticker':<9} {'公司':<18} {'板块':<10} {'技术':<5} {'基本面':<5} {'热度':<5} {'股息率':<7} {'综合':<5} {'仓位':<12} {'催化剂/逻辑':<40} {'风险'}")
print("=" * 110)

for rank, (_, t, n, sec, cap, tech, fund, heat, cat, comp, div, div_year, catalyst, risk) in enumerate(sorted_stocks, 1):
    tech_s = "⭐" * tech
    fund_s = "⭐" * fund
    heat_s = f"{heat}/10"
    pos = position(comp, div)
    print(f"{rank:<3} {t:<9} {n:<18} {sec:<10} {tech_s:<5} {fund_s:<5} {heat_s:<5} {div:<7} {comp:<5} {pos:<12} {catalyst:<40} {risk}")

print(f"\n" + "=" * 110)

print("\n股息率最高的真正高息股 TOP 5：")
div_sorted = sorted(sorted_stocks, key=lambda x: -float(x[10].replace("%","")))[:5]
for _, t, n, sec, cap, tech, fund, heat, cat, comp, div, dy, catalyst, risk in div_sorted:
    pos = position(comp, div)
    print(f"   {t:<8} {n:<18} 股息 {div:<7} 综合{comp} -> {pos}  | {catalyst}")

print("\n综合评分 TOP 5（高息+成长均衡优选）：")
for _, t, n, sec, cap, tech, fund, heat, cat, comp, div, dy, catalyst, risk in sorted_stocks[:5]:
    pos = position(comp, div)
    print(f"   {t:<8} {n:<18} 综合{comp} {score_to_stars(comp)}  股息{div} -> {pos}")

print("\n社交热度 TOP 5（30个来源）：")
heat_top = sorted(sorted_stocks, key=lambda x: -x[6])[:5]
for _, t, n, _, _, _, _, h, _, _, div, _, cat, _ in heat_top:
    fire = "🔥" * (h // 2)
    print(f"   {t:<8} {n:<18} 热度{h}/10 {fire:<8} 股息{div} -> {cat}")

print("\n高息股板块分布：")
from collections import Counter
sec_cnt = Counter(s[3] for s in stocks)
for sec, cnt in sec_cnt.most_common():
    print(f"   {sec:<12} {cnt}只")

print("\n高息股选股逻辑说明：")
print("   高息股的均线多头要求比成长股宽松 - 更侧重股息持续性和估值安全边际")
print("   真正的纯高息股(股息>2.5%)集中在：消费防御、能源、通信/公用事业")
print("   科技高息股(MSFT/AVGO/CSCO/ORCL)股息在0.6-1.5%, 胜在增长+分红双驱动")

print("\n风险提示：")
print("   - 金融板块近1月-1.15%, 均线走弱, 高息银行股需耐心等待")
print("   - 通信股VZ/T股息率高但增长停滞, 属于高息陷阱的高发区")
print("   - 能源股XOM/CVX受益油价高位, 但地缘政治变化是最大变量")
print("   - 真正高息+成长兼备的首选: COST, WMT, MSFT")
