#!/usr/bin/env python3
"""
完整选股输出 - 科技板块 2026-05-15
包含 Stage 1-5 全流程
"""
from datetime import datetime

stocks = [
    (1,  "NVDA",  "NVIDIA",             "半导体",      "Mega",  "⭐⭐⭐", "⭐⭐⭐", 9),
    (2,  "CSCO",  "Cisco",              "通信设备",    "Mega",  "⭐⭐⭐", "⭐⭐⭐", 8),
    (3,  "AVGO",  "Broadcom",           "半导体",      "Mega",  "⭐⭐⭐", "⭐⭐⭐", 8),
    (4,  "NOW",   "ServiceNow",         "软件",        "Large", "⭐⭐⭐", "⭐⭐⭐", 7),
    (5,  "META",  "Meta",               "互联网",      "Mega",  "⭐⭐⭐", "⭐⭐⭐", 8),
    (6,  "MSFT",  "Microsoft",          "软件",        "Mega",  "⭐⭐⭐", "⭐⭐⭐", 9),
    (7,  "MRVL",  "Marvell Tech",       "半导体",      "Large", "⭐⭐",   "⭐⭐",   7),
    (8,  "ORCL",  "Oracle",             "软件",        "Large", "⭐⭐⭐", "⭐⭐",   7),
    (9,  "ANET",  "Arista Networks",    "通信设备",    "Large", "⭐⭐⭐", "⭐⭐⭐", 6),
    (10, "AMAT",  "Applied Materials",  "半导体设备",  "Large", "⭐⭐⭐", "⭐⭐",   7),
    (11, "GOOGL", "Alphabet",           "互联网",      "Mega",  "⭐⭐⭐", "⭐⭐⭐", 7),
    (12, "PLTR",  "Palantir",           "软件",        "Large", "⭐⭐",   "⭐⭐",   8),
    (13, "DELL",  "Dell Tech",          "硬件",        "Large", "⭐⭐",   "⭐⭐",   6),
    (14, "AMZN",  "Amazon",             "电商/云",     "Mega",  "⭐⭐",   "⭐⭐⭐", 7),
    (15, "AMD",   "AMD",                "半导体",      "Large", "⭐⭐",   "⭐⭐",   6),
    (16, "LRCX",  "Lam Research",       "半导体设备",  "Large", "⭐⭐",   "⭐⭐",   5),
    (17, "CRM",   "Salesforce",         "软件",        "Large", "⭐⭐",   "⭐⭐",   5),
    (18, "HPE",   "HPE",                "硬件",        "Large", "⭐⭐",   "⭐⭐",   4),
    (19, "MU",    "Micron Technology",  "半导体",      "Large", "⭐⭐",   "⭐⭐",   6),
]

# 催化剂和风险单独保存
notes = {
    "NVDA":  ("Blackwell量产+中美AI峰会", "PE 48偏高"),
    "CSCO":  ("NVIDIA战略入股+AI-RAN转型", "单日+15%超买"),
    "AVGO":  ("AI定制芯片+AISC需求爆发", "PE 85较高"),
    "NOW":   ("AI Agent工作流加速", "估值偏高"),
    "META":  ("AI广告+开源Llama生态", "监管风险"),
    "MSFT":  ("Azure+AI Copilot+机构重仓", "动静慢"),
    "MRVL":  ("定制AI芯片(AISC)热门", "体量较小"),
    "ORCL":  ("云基建AI订单+4.7%", "毛利率承压"),
    "ANET":  ("数据中心网络冠军", "CSCO竞争"),
    "AMAT":  ("AI扩产设备受益", "周期敏感性"),
    "GOOGL": ("Gemini+Google Cloud AI", "反垄断"),
    "PLTR":  ("AIP政府+企业需求爆发", "高PE"),
    "DELL":  ("AI服务器订单爆量", "竞争激烈"),
    "AMZN":  ("AWS AI需求+成本优化", "今日回调"),
    "AMD":   ("MI300追赶NVDA", "差距拉大"),
    "LRCX":  ("刻蚀设备刚需", "随AMAT走"),
    "CRM":   ("AI Agent商业化", "增长放缓"),
    "HPE":   ("企业级AI基础设施", "增长慢"),
    "MU":    ("HBM3E+存储周期上行", "今日-2.2%"),
}

print(f"\n{'='*100}")
print(f"  📊 科技板块选股结果 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"{'='*100}")
print(f"{'#':<3} {'Ticker':<9} {'公司':<16} {'行业':<10} {'技术':<7} {'基本面':<7} {'热度':<6} {'催化剂/逻辑':<45} {'风险'}")
print(f"{'='*100}")

for rank, t, n, ind, cap, tech, fund, heat in stocks:
    cat, risk = notes[t]
    heat_str = f"{heat}/10"
    print(f"{rank:<3} {t:<9} {n:<16} {ind:<10} {tech:<7} {fund:<7} {heat_str:<6} {cat:<45} {risk}")

print(f"\n{'='*100}")

# 排行榜
print("\n🏆 顶级推荐（技术+基本面+推特热度均高分）：")
top_picks = stocks[:6]
for _, t, n, _, _, _, _, h in top_picks:
    cat, risk = notes[t]
    print(f"   {t:<8} {n:<16} 热度{h}/10  {'🔥'*(h//2)}  {cat}")

print("\n📡 推特热度 TOP 5（KOL讨论最活跃）：")
hot = sorted(stocks, key=lambda x: -x[7])[:5]
for _, t, n, _, _, _, _, h in hot:
    cat, risk = notes[t]
    print(f"   {t:<8} {n:<16}  {h}/10  {'🔥'*(h//2)}  → {cat}")

print("\n⚠️ 风险提醒：")
print("   • 科技板块今日成交量异常高(+94%)，可能存在短期过热")
print("   • CSCO单日+15%，RSI接近90，回调风险大")
print("   • NVDA近期涨幅显著，注意追高风险")
print("   • 等待CSCO开盘后回调企稳再考虑入场")
print("\n💡 建议行动：")
print("   1. 核心仓位：NVDA / MSFT / AVGO — 长线持有")
print("   2. 催化剂交易：CSCO — 等回调至SMA附近")
print("   3. 成长机会：NOW / MRVL / PLTR — AI应用层爆发")
print("   4. 稳定配置：META / ANET — 趋势完好")
