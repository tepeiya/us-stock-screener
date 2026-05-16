#!/usr/bin/env python3
"""
对话版选股器 - 完整输出
技术+基本面+社交热度+催化剂+退场+13F
"""
from datetime import datetime

stocks = [
    {"r":1,"t":"NVDA","n":"NVIDIA","ind":"半导体","sec":"科技","tl":5,"fl":5,"h":9,"cl":5,"c":4.8,"pos":"core",
     "desc":"Blackwell量产+中美AI峰会+13F增持","risk":"PE 48","stop":"$199.6","rsi":85,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater, Citadel, Renaissance","ed":"05-28","ed_d":13},
    {"r":2,"t":"CSCO","n":"Cisco","ind":"通信设备","sec":"科技","tl":5,"fl":5,"h":8,"cl":5,"c":4.7,"pos":"core",
     "desc":"NVIDIA入股+AI-RAN转型+财报暴打","risk":"超买","stop":"$105.6","rsi":90,"ma":"SMA20","sts":"超买预警",
     "funds":"Oaktree, NVIDIA","ed":"08-12","ed_d":89},
    {"r":3,"t":"AVGO","n":"Broadcom","ind":"半导体","sec":"科技","tl":5,"fl":5,"h":8,"cl":5,"c":4.7,"pos":"core",
     "desc":"AI定制芯片+AISC需求+VMware","risk":"PE 85","stop":"$383.8","rsi":82,"ma":"SMA50","sts":"持有",
     "funds":"Citadel, Point72","ed":"06-04","ed_d":20},
    {"r":4,"t":"META","n":"Meta","ind":"互联网","sec":"科技","tl":5,"fl":5,"h":8,"cl":4,"c":4.5,"pos":"core",
     "desc":"AI广告+Llama+Q2指引强","risk":"反垄断","stop":"$510.4","rsi":85,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater, Greenlight","ed":"07-29","ed_d":75},
    {"r":5,"t":"MSFT","n":"Microsoft","ind":"软件","sec":"科技","tl":5,"fl":5,"h":9,"cl":4,"c":4.5,"pos":"core",
     "desc":"Azure+AI Copilot+机构重仓","risk":"波动小","stop":"$347.7","rsi":80,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater, Citadel, Renaissance","ed":"07-22","ed_d":68},
    {"r":6,"t":"NOW","n":"ServiceNow","ind":"软件","sec":"科技","tl":5,"fl":5,"h":7,"cl":5,"c":4.4,"pos":"watch",
     "desc":"AI Agent+Q1超预期","risk":"估值偏高","stop":"$918.0","rsi":85,"ma":"SMA50","sts":"持有","funds":"-","ed":"07-23","ed_d":69},
    {"r":7,"t":"PLTR","n":"Palantir","ind":"软件","sec":"科技","tl":4,"fl":4,"h":8,"cl":5,"c":4.3,"pos":"watch",
     "desc":"AIP政府+企业AI","risk":"PE极高","stop":"$106.6","rsi":88,"ma":"SMA20","sts":"持有",
     "funds":"Citadel, Point72","ed":"已过","ed_d":-1},
    {"r":8,"t":"COST","n":"Costco","ind":"零售","sec":"消费防御","tl":5,"fl":5,"h":7,"cl":4,"c":4.3,"pos":"watch",
     "desc":"会员制+成长防御","risk":"股息0.6%","stop":"$910.6","rsi":78,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater, Berkshire","ed":"05-29","ed_d":14},
    {"r":9,"t":"MRVL","n":"Marvell Tech","ind":"半导体","sec":"科技","tl":4,"fl":4,"h":7,"cl":5,"c":4.2,"pos":"watch",
     "desc":"定制AI芯片(AISC)","risk":"体量小","stop":"$68.0","rsi":85,"ma":"SMA50","sts":"持有","funds":"-","ed":"05-29","ed_d":14},
    {"r":10,"t":"ORCL","n":"Oracle","ind":"软件","sec":"科技","tl":5,"fl":4,"h":7,"cl":4,"c":4.2,"pos":"watch",
     "desc":"云+AI订单+4.7%","risk":"毛利承压","stop":"$168.9","rsi":82,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater","ed":"06-10","ed_d":26},
    {"r":11,"t":"WMT","n":"Walmart","ind":"零售","sec":"消费防御","tl":5,"fl":5,"h":6,"cl":4,"c":4.2,"pos":"watch",
     "desc":"电商+AI供应链","risk":"竞争激烈","stop":"$116.3","rsi":78,"ma":"SMA50","sts":"持有",
     "funds":"Berkshire","ed":"05-21","ed_d":6},
    {"r":12,"t":"AMAT","n":"Applied Materials","ind":"半导体设备","sec":"科技","tl":5,"fl":4,"h":7,"cl":4,"c":4.1,"pos":"watch",
     "desc":"AI扩产设备受益","risk":"周期敏感","stop":"$378.0","rsi":80,"ma":"SMA50","sts":"财报窗口","funds":"-","ed":"05-15","ed_d":0},
    {"r":13,"t":"ANET","n":"Arista Networks","ind":"通信设备","sec":"科技","tl":5,"fl":5,"h":6,"cl":4,"c":4.1,"pos":"watch",
     "desc":"数据中心网络冠军","risk":"CSCO竞争","stop":"$93.5","rsi":82,"ma":"SMA50","sts":"持有",
     "funds":"Bridgewater","ed":"已过","ed_d":-1},
    {"r":14,"t":"GOOGL","n":"Alphabet","ind":"互联网","sec":"科技","tl":5,"fl":5,"h":7,"cl":3,"c":4.0,"pos":"watch",
     "desc":"Gemini+GoogleCloud","risk":"反垄断","stop":"$341.5","rsi":80,"ma":"SMA50","sts":"持有",
     "funds":"Pershing, Bridgewater, Greenlight","ed":"07-23","ed_d":69},
    {"r":15,"t":"AMZN","n":"Amazon","ind":"电商/云","sec":"科技","tl":4,"fl":5,"h":7,"cl":3,"c":3.9,"pos":"light",
     "desc":"AWS AI+成本优化","risk":"今日-0.7%","stop":"$228.1","rsi":80,"ma":"SMA20","sts":"持有",
     "funds":"Bridgewater, Greenlight","ed":"07-30","ed_d":76},
    {"r":16,"t":"PG","n":"P&G","ind":"消费品","sec":"消费防御","tl":4,"fl":5,"h":5,"cl":3,"c":3.9,"pos":"light",
     "desc":"刚需+股息3.0%","risk":"增长慢","stop":"$129.3","rsi":75,"ma":"SMA20","sts":"持有",
     "funds":"Berkshire","ed":"07-23","ed_d":69},
    {"r":17,"t":"MU","n":"Micron","ind":"半导体","sec":"科技","tl":4,"fl":4,"h":6,"cl":4,"c":3.8,"pos":"light",
     "desc":"HBM3E+存储上行","risk":"今日-2.2%","stop":"$629.0","rsi":78,"ma":"SMA20","sts":"持有",
     "funds":"Bridgewater","ed":"06-25","ed_d":41},
    {"r":18,"t":"AMD","n":"AMD","ind":"半导体","sec":"科技","tl":4,"fl":4,"h":6,"cl":4,"c":3.8,"pos":"light",
     "desc":"MI300追赶NVDA","risk":"差距拉大","stop":"$381.8","rsi":82,"ma":"SMA20","sts":"持有",
     "funds":"Citadel","ed":"07-29","ed_d":75},
    {"r":19,"t":"KO","n":"Coca-Cola","ind":"饮料","sec":"消费防御","tl":4,"fl":5,"h":6,"cl":3,"c":3.8,"pos":"light",
     "desc":"品牌+股息2.6%","risk":"增长慢","stop":"$72.8","rsi":75,"ma":"SMA20","sts":"持有",
     "funds":"Berkshire","ed":"07-22","ed_d":68},
    {"r":20,"t":"XOM","n":"ExxonMobil","ind":"油气","sec":"能源","tl":4,"fl":4,"h":6,"cl":4,"c":3.7,"pos":"light",
     "desc":"油价高位+股息2.7%","risk":"油价波动","stop":"$121.8","rsi":78,"ma":"SMA20","sts":"持有",
     "funds":"Berkshire","ed":"08-01","ed_d":78},
    {"r":21,"t":"GS","n":"Goldman Sachs","ind":"投行","sec":"金融","tl":4,"fl":4,"h":5,"cl":4,"c":3.6,"pos":"light",
     "desc":"投行复苏+AI","risk":"波动大","stop":"$493.0","rsi":80,"ma":"SMA20","sts":"持有",
     "funds":"Citadel","ed":"07-15","ed_d":61},
    {"r":22,"t":"CVX","n":"Chevron","ind":"油气","sec":"能源","tl":4,"fl":4,"h":5,"cl":3,"c":3.5,"pos":"light",
     "desc":"股东回报+股息3.8%","risk":"油价波动","stop":"$149.0","rsi":78,"ma":"SMA20","sts":"持有",
     "funds":"Berkshire","ed":"08-01","ed_d":78},
    {"r":23,"t":"JPM","n":"JPMorgan","ind":"银行","sec":"金融","tl":3,"fl":5,"h":6,"cl":3,"c":3.3,"pos":"light",
     "desc":"全能银行+AI","risk":"均线走弱","stop":"$257.4","rsi":78,"ma":"SMA20","sts":"持有",
     "funds":"Berkshire, Renaissance","ed":"07-14","ed_d":60},
]

stocks.sort(key=lambda s: -s["c"])

pos_lb = {"core":"🏛️核心5-10%","watch":"👀观察2-5%","light":"⚡轻仓1-2%","skip":"跳过"}
ex_icon = {"持有":"✅","超买预警":"⚠️","财报窗口":"📅","考虑离场":"🚨"}

def hb(v): return "🔥"*(v//2)+("✨" if v%2 else "")

print("="*110)
print(f"  对话选股结果 | {datetime.now().strftime('%Y-%m-%d %H:%M')} | 最热板块: 科技(🥇1月+14.9%)")
print("="*110)
print(f"{'#':<3} {'Ticker':<9} {'公司':<16} {'综合':<5} {'仓位':<14} {'🔥热度':<10} {'退场':<8} {'催化剂':<42}")
print("="*110)

for s in stocks:
    print(f"{s['r']:<3} {s['t']:<9} {s['n']:<16} {s['c']:<5} {pos_lb[s['pos']]:<14} {s['h']}/10{hb(s['h']):<7} {ex_icon.get(s['sts'],s['sts']):<8} {s['desc']:<42}")

print(f"\n{'='*110}")

print("\n🏆 综合评分 TOP 5：")
for s in stocks[:5]:
    print(f"   {s['t']:<9} {s['n']:<16} 综合{s['c']}  仓位{pos_lb[s['pos']]}  🔥{s['h']}/10  {s['desc']}")

print("\n🛡️ 退场预警：")
warn = [s for s in stocks if s["sts"] != "持有"]
for s in warn:
    print(f"   ⚠️ {s['t']:<9} {s['n']:<16} 状态:{s['sts']}  止损:{s['stop']}  RSI>{s['rsi']}  跌破{s['ma']}")

print("\n🏛️ 13F大佬共识（按出现次数）：")
from collections import Counter
fmap = Counter()
for s in stocks:
    for f in s["funds"].split(","):
        f = f.strip()
        if f and f != "-":
            fmap[f] += 1
for f, cnt in fmap.most_common():
    holders = [s['t'] for s in stocks if f in s['funds']]
    print(f"   {f:<20} {cnt}x  → {', '.join(holders)}")

print("\n📅 近期财报（30天内）：")
for s in stocks:
    d = s["ed_d"]
    if d >= 0 and d <= 30:
        dsp = "今天" if d == 0 else f"{d}天后"
        print(f"   📅 {s['t']:<9} {s['n']:<16} {s['ed']} ({dsp})")

print(f"\n💡 策略建议：")
print(f"   核心: NVDA + AVGO + MSFT（趋势完好、13F增持、热度高）")
print(f"   关注: CSCO超买⚠️, 等回调至SMA20附近再考虑入场")
print(f"   成长: NOW / MRVL（AI Agent/AISC 应用层爆发前夜）")
print(f"   防御: COST / WMT（消费稳健, 适合底仓）")
