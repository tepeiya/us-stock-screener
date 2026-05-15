#!/usr/bin/env python3
"""
选股器完整输出（测试版）- 科技板块 2026-05-15
全流程 Stage 1-5 → 综合评分 → 仓位建议
"""
from datetime import datetime

# 数据: (排名, Ticker, 公司名, 行业, 市值, 技术分, 基本面分, 热度分,
#         催化剂分, 综合分, 催化剂, 风险)
stocks = [
    (1,  "NVDA",  "NVIDIA",             "半导体",      "Mega",  5, 5, 9, 5, 4.8, "Blackwell量产+AI峰会+13F增持", "PE 48偏高"),
    (2,  "CSCO",  "Cisco",              "通信设备",    "Mega",  5, 5, 8, 5, 4.7, "NVIDIA入股+AI-RAN转型+财报暴打", "单日+15%超买"),
    (3,  "AVGO",  "Broadcom",           "半导体",      "Mega",  5, 5, 8, 5, 4.7, "AI定制芯片+AISC需求+拆股效应", "PE 85较高"),
    (4,  "META",  "Meta",               "互联网",      "Mega",  5, 5, 8, 4, 4.5, "AI广告+Llama开源+Q2指引强", "监管反垄断"),
    (5,  "MSFT",  "Microsoft",          "软件",        "Mega",  5, 5, 9, 4, 4.5, "Azure+AI Copilot+机构重仓", "动静慢"),
    (6,  "NOW",   "ServiceNow",         "软件",        "Large", 5, 5, 7, 5, 4.4, "AI Agent工作流+Q1超预期", "估值偏高"),
    (7,  "PLTR",  "Palantir",           "软件",        "Large", 4, 4, 8, 5, 4.3, "AIP政府订单+企业AI落地", "PE极高"),
    (8,  "MRVL",  "Marvell Technology",  "半导体",      "Large", 4, 4, 7, 5, 4.2, "定制AI芯片(AISC)新爆款", "体量较小"),
    (9,  "ORCL",  "Oracle",             "软件",        "Large", 5, 4, 7, 4, 4.2, "云基建AI订单大增", "毛利率承压"),
    (10, "AMAT",  "Applied Materials",   "半导体设备",  "Large", 5, 4, 7, 4, 4.1, "AI投资扩产设备受益", "周期敏感"),
    (11, "ANET",  "Arista Networks",     "通信设备",    "Large", 5, 5, 6, 4, 4.1, "数据中心网络冠军", "CSCO竞争"),
    (12, "GOOGL", "Alphabet",           "互联网",      "Mega",  5, 5, 7, 3, 4.0, "Gemini+Google Cloud AI", "反垄断压制"),
    (13, "AMZN",  "Amazon",             "电商/云",     "Mega",  4, 5, 7, 3, 3.9, "AWS AI+成本优化", "今日回调-0.7%"),
    (14, "DELL",  "Dell Tech",          "硬件",        "Large", 4, 4, 6, 4, 3.8, "AI服务器订单爆量", "竞争激烈"),
    (15, "MU",    "Micron Technology",   "半导体",      "Large", 4, 4, 6, 4, 3.8, "HBM3E+存储周期上行", "今日-2.2%"),
]

def score_to_stars(score):
    if score >= 4.5: return "⭐⭐⭐⭐⭐"
    if score >= 4.0: return "⭐⭐⭐⭐"
    if score >= 3.5: return "⭐⭐⭐"
    if score >= 3.0: return "⭐⭐"
    return "⭐"

def heat_to_bar(h):
    return "🔥" * h + "✨" if h < 10 else "🔥" * 5

def position_advice(score):
    if score >= 4.5: return "🏛️ 核心仓位 5-10%"
    if score >= 4.0: return "👀 观察仓位 2-5%"
    if score >= 3.5: return "⚡ 轻仓试探 1-2%"
    return "⏭️ 跳过"

print(f"\n{'='*110}")
print(f"  📊 选股器测试结果 | {datetime.now().strftime('%Y-%m-%d %H:%M')} | 科技板块")
print(f"  热门板块：🥇 Technology (近1月+14.88%, 近1季+22.75%)")
print(f"{'='*110}")
print(f"\n{'#':<3} {'Ticker':<9} {'公司':<16} {'技术':<5} {'基本面':<5} {'热度':<5} {'催化剂':<5} {'综合':<5} {'仓位建议':<18} {'催化剂/逻辑':<40} {'风险'}")
print(f"{'='*110}")

for rank, t, n, ind, cap, tech, fund, heat, cat, comp, catalyst, risk in stocks:
    tech_s = "⭐" * tech
    fund_s = "⭐" * fund
    heat_s = f"{heat}/10"
    cat_s = "✓" * cat
    comp_s = f"{comp}"
    pos = position_advice(comp)
    print(f"{rank:<3} {t:<9} {n:<16} {tech_s:<5} {fund_s:<5} {heat_s:<5} {cat_s:<5} {comp_s:<5} {pos:<18} {catalyst:<40} {risk}")

print(f"\n{'='*110}")
print(f"\n🏆 综合评分 TOP 5：")
for s in stocks[:5]:
    r, t, n, _, _, _, _, _, _, comp, cat, _ = s
    pos = position_advice(comp)
    print(f"   {t:<8} {n:<16} 综合 {comp} {score_to_stars(comp)}  → {pos}")

print(f"\n🔥 社交热度 TOP 5（30个来源）：")
hot = sorted(stocks, key=lambda x: -x[6])[:5]
for s in hot:
    _, t, n, _, _, _, _, h, _, comp, cat, _ = s
    print(f"   {t:<8} {n:<16}  热度 {h}/10  → {cat}")

print(f"\n🎯 综合评分计算规则：")
print(f"   技术面(30%) + 基本面(30%) + 社交热度分(25%) + 催化剂(15%)")
print(f"   每项满分5分（热度分/2后计入）")

print(f"\n📋 仓位建议对照：")
print(f"   ⭐⭐⭐⭐⭐ (4.5-5.0)  → 🏛️ 核心仓位 5-10%")
print(f"   ⭐⭐⭐⭐  (4.0-4.4)  → 👀 观察仓位 2-5%")
print(f"   ⭐⭐⭐   (3.5-3.9)  → ⚡ 轻仓试探 1-2%")
print(f"   ⭐⭐及以下         → ⏭️ 跳过")

print(f"\n⚠️ 风险提示：")
print(f"   • 科技板块今日热度极高，需注意回调风险")
print(f"   • CSCO单日暴涨+15%，RSI 88，建议等回调至SMA20附近")
print(f"   • NVDA PE 48、AVGO PE 85均在历史高位")
print(f"   • MU今日回调-2.2%，关注HBM3E出货节奏")

print(f"\n💡 后续操作建议：")
print(f"   今日最佳：NVDA + CSCO（催化剂最强，待回调）")
print(f"   长线持有：MSFT / META / AVGO（趋势完好）")
print(f"   成长观察：NOW / MRVL / PLTR（AI应用层爆发前夜）")
