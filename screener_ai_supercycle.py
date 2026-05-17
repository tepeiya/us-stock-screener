#!/usr/bin/env python3
"""
AI超级周期 · 10层架构选股评估
添加第1/2/5/6/7/9层的缺失标的
"""
from datetime import datetime

# 新6只标的评分
new_stocks = [
    # 1-电力
    ("BE",  "Bloom Energy",      "电力/燃料电池", "Large", 5, 4, 8, 5, 4.3, "watch", 
     "AI数据中心100-500MW瓶颈+Oracle签2.8GW+扭亏为盈", 
     "1年涨1292%/PE为负/PB 85/今日-9%回调"),
    # 2-基板
    ("AXTI", "AXT Inc",          "半导体基板",    "Small", 3, 3, 4, 4, 3.1, "light",
     "InP/GaAs晶圆供应商+CPO/1.6T驱动", 
     "微盘$200M/流动性差/周期股"),
    # 5-光子
    ("AAOI", "Applied Optoelectronics", "光子器件", "Small", 4, 3, 5, 5, 3.4, "light",
     "纯光子器件+400G→800G→1.6T量价齐升",
     "小盘$500M/竞争激烈/波动大"),
    # 6-光学
    ("LITE", "Lumentum",         "光网络",       "Large", 4, 4, 6, 5, 3.9, "watch",
     "光网络互联龙头+800G→1.6T全网替换",
     "PE 50+ /并购整合风险"),
    # 7-散热
    ("VRT",  "Vertiv",           "液冷散热",     "Large", 5, 5, 8, 5, 4.5, "watch",
     "液冷龙头+1kW+/chip散热刚需+刚入S&P 500",
     "PE 93/Forward PE 43/1年涨252%"),
    # 9-数据中心
    ("NBIS", "Nebius Group",     "AI原生数据中心", "Large", 4, 3, 5, 5, 3.6, "light",
     "AI原生数据中心+Yandex背景+GPU密度领先",
     "刚上市不久/盈利不确定"),
]

pos_label = {"core":"🏛️核心5-10%","watch":"👀观察2-5%","light":"⚡轻仓1-2%","skip":"⏭️跳过"}

print("="*110)
print(f"  AI超级周期 · 10层缺失标的评估 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("="*110)
print(f"\n{'层':<10} {'Ticker':<9} {'公司':<18} {'市值':<8} {'技术':<5} {'基本面':<5} {'热度':<5} {'综合':<5} {'仓位':<12} {'逻辑':<44}")
print("="*110)

layers = ["1-电力","2-基板","3-芯片","4-内存","5-光子","6-光学","7-散热","8-网络","9-数据中心","10-云"]
existing = {
    "3-芯片": ("NVDA", 4.8, "🏛️核心"),
    "4-内存": ("MU", 3.8, "⚡轻仓"),
    "8-网络": ("ANET", 4.1, "👀观察"),
    "10-云": ("GOOGL", 4.0, "👀观察"),
}

for s in new_stocks:
    t, n, ind, size, tl, fl, h, cl, comp, pos, desc, risk = s
    print(f"  {s[0]:<6} {t:<9} {n:<18} {size:<8} {'⭐'*tl:<5} {'⭐'*fl:<5} {h}/10{'🔥'*(h//2):<5} {comp:<5} {pos_label[pos]:<12} {desc:<44}")

# 已覆盖
print(f"\n{'='*110}")
print("\n📋 10层完整覆盖状态：")
print(f"\n{'层':<10} {'Ticker':<9} {'公司':<20} {'评分':<6} {'仓位':<12} {'判断'}")
print("-"*70)

all_layers = []
for l in layers:
    found = False
    for s in new_stocks:
        if l.startswith(s[0][0]):
            all_layers.append((l, s[1], s[2], s[9], pos_label[s[10]], s[12]))
            found = True
            break
    if l in existing:
        t, c, p = existing[l]
        name = {"NVDA":"NVIDIA","MU":"Micron","ANET":"Arista","GOOGL":"Alphabet"}[t]
        all_layers.append((l, t, name, c, p, "已在选股器中"))
        
for l, t, n, c, p, desc in all_layers:
    print(f"  {l:<10} {t:<9} {n:<20} {c:<6} {p:<12} {desc}")

print(f"\n{'='*110}")
print("\n🏆 新标的中最值得关注的：")
print(f"   🥇 VRT (4.5) → Vertiv 液冷龙头, AI散热刚需, 刚入S&P 500, ROC 21%, 基本面优秀")
print(f"   🥈 BE  (4.3) → Bloom Energy, 电力层瓶颈, Oracle 2.8GW大单, 扭亏为盈")  
print(f"   🥉 LITE (3.9) → Lumentum, 光网络替换周期, 800G→1.6T驱动")

print(f"\n💡 建议：")
print(f"   1. VRT 基本面最硬(ROE 45%/ROIC 21%/收入增29%), 如果回调到SMA50可考虑建仓")
print(f"   2. BE 位置偏高(1年12倍), 等回调至$200附近更有安全边际")
print(f"   3. 其余4只(AXTI/AAOI/LITE/NBIS)可作为观察, 仓位不宜重")
print(f"   4. 你的10层框架逻辑自洽, 但底层标的(BE/AXTI/AAOI)波动远大于顶层(NVDA/GOOGL)")
