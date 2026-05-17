#!/usr/bin/env python3
"""
可持续能源/AI电力概念股 - 选股器评估
"""
from datetime import datetime

stocks = [
    ("PLUG", "Plug Power",     "氢燃料电池",   "$5.27B", "Mid",   2, 1, 7, 3, 2.5, "light", "绿氢AI备用电源+Q1亏损收窄", "未盈利/-128% ROE/Short Float 25.8%/目标价$3.49低于股价"),
    ("FLNC", "Fluence Energy",  "电池储能",     "$3.5B",  "Mid",   3, 2, 5, 3, 2.8, "skip",  "电网级储能+AI数据中心",     "估值偏高/竞争激烈"),
    ("ARRY", "Array Tech",      "太阳能跟踪",   "$1.5B",  "Small", 3, 2, 4, 3, 2.6, "skip",  "太阳能跟踪系统",           "小型股流动性差"),
    ("SHLS", "Shoals Tech",     "光伏电气",     "$1.7B",  "Small", 3, 2, 3, 2, 2.4, "skip",  "光伏BOS组件",              "小型股"),
    ("RUN",  "Sunnova",         "分布式光伏",   "$1.8B",  "Small", 3, 1, 4, 3, 2.3, "skip",  "户用光伏+储能",             "未盈利/高负债"),
    ("CSIQ", "Canadian Solar",  "光伏组件",     "$1.2B",  "Small", 3, 3, 5, 3, 2.9, "skip",  "光伏+储能双业务",           "贸易战风险"),
    ("BEP",  "Brookfield Renewable", "清洁能源运营商","$10.5B","Large",4, 4, 5, 4, 3.7, "light", "全球水电/风/光/核+$BE合作", "PE为负/刚扭亏"),
    ("CWEN", "Clearway Energy", "风光储",       "$6.5B",  "Large", 4, 3, 4, 3, 3.3, "light", "10+GW风光储直供数据中心",   "负债率较高"),
    ("JKS",  "JinkoSolar",      "光伏制造",     "$1.1B",  "Small", 3, 2, 4, 2, 2.5, "skip",  "全球最大组件商之一",        "产能过剩/贸易壁垒"),
    ("DQ",   "Daqo New Energy", "多晶硅",       "$1.3B",  "Small", 3, 2, 3, 2, 2.4, "skip",  "多晶硅原料",               "周期底部不确定"),
    ("HASI", "Hannon Armstrong", "清洁能源融资", "$2.5B",  "Mid",   4, 3, 4, 3, 3.2, "light", "为风光储项目融资",          "利率敏感"),
    ("EOSE", "Eos Energy",      "长时锌电池",   "$1.2B",  "Small", 2, 1, 5, 3, 2.2, "skip",  "锌电池长时储能",            "未盈利/融资风险"),
    ("ENPH", "Enphase Energy",  "微型逆变器",   "$7.2B",  "Large", 4, 4, 6, 3, 3.6, "light", "微型逆变器龙头(超跌$53)",   "需求恢复不确定"),
]

pos_label = {"core":"🏛️核心5-10%","watch":"👀观察2-5%","light":"⚡轻仓1-2%","skip":"⏭️跳过"}

print("="*110)
print(f"  可持续能源/AI电力概念股 · 选股器评估 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"  核心逻辑: AI数据中心电力需求爆发 → 清洁能源+储能受益")
print("="*110)
print(f"\n{'#':<3} {'Ticker':<9} {'公司':<20} {'市值':<10} {'技术':<5} {'基本面':<5} {'热度':<5} {'综合':<5} {'仓位':<12} {'逻辑':<36} {'风险'}")
print("="*110)

for i, (t, n, ind, cap, size, tl, fl, h, cl, comp, pos, desc, risk) in enumerate(stocks, 1):
    print(f"{i:<3} {t:<9} {n:<20} {size:<10} {'⭐'*tl:<5} {'⭐'*fl:<5} {h}/10{'🔥'*(h//2):<5} {comp:<5} {pos_label[pos]:<12} {desc:<36} {risk}")

print(f"\n{'='*110}")

print("\n🏆 推荐排序（综合+质量）：")
recommended = sorted([s for s in stocks if s[10] != 'skip'], key=lambda x: -x[9])
for s in recommended:
    print(f"   {s[0]:<9} {s[1]:<20} 综合{s[9]} {pos_label[s[10]]}  {s[12]:<30}")

print("\n📊 板块整体评估：")
print(f"   • 这些股票多数是小型/微型市值（$1-10B），波动大、流动性差")
print(f"   • 多数未盈利（PLUG/BEP/EOSE/FUNC等都是负数PE）")
print(f"   • 基本面合格的只有：BEP(CWEN)/HASI/ENPH——有收入+相对合理估值")
print(f"   • 热度最高的：PLUG(7/10) > ENPH(6/10) > BEP(5/10)")
print(f"\n💡 策略建议：")
print(f"   1. 这个主题方向（AI×电力）是对的，但标的质量参差不齐")
print(f"   2. 质量优先：BEP(Brookfield) > CWEN > HASI > ENPH")
print(f"   3. 投机博弈：PLUG(做多情绪强但基本面差,需严格止损)")
print(f"   4. ENPH $53→$300的反弹逻辑最扎实(曾经是$340的股票)")
print(f"   5. 注意：该推文目标价过于激进（PLUG $30=8x, BEP $200=6x）")
print(f"\n⚠️ 风险提示：")
print(f"   • 清洁能源板块在利率高位承压，降息才是真正催化剂")
print(f"   • PLUG Short Float 25.8%, 轧空风险双向")
print(f"   • ENPH从$340跌到$53跌幅83%, 反弹需要时间")
