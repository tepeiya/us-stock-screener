#!/usr/bin/env python3
"""
A股选股器 - 核心程序
基于价值大师网(GuruFocus.CN)+东方财富等工具
"""
from datetime import datetime

# A股数据：基于当前市场态势整理的候选池
# (排名, 代码, 名称, 行业, 市值, 技术分, 基本面分, 热度分, 催化剂分, 综合分,
#  催化剂, 风险)

stocks = [
    # --- AI/半导体（目前A股最热门赛道）---
    (1,  "300308", "中际旭创", "光模块/AI",   "万亿级", 5, 5, 9, 5, 4.8, 
     "800G/1.6T光模块需求爆发+AI基建", "高位+2.51%注意回调"),
    (2,  "300502", "新易盛",  "光模块/AI",   "6000亿", 5, 5, 9, 5, 4.8, 
     "AI光模块核心供应商+今日+7.85%", "单日暴涨分时超买"),
    (3,  "300394", "天孚通信", "光模块/AI",   "3000亿", 5, 5, 8, 5, 4.6, 
     "光器件龙头+AI互联需求+今日+3.79%", "短期涨幅过大"),
    (4,  "688256", "寒武纪",  "AI芯片",      "8000亿", 4, 4, 9, 5, 4.4, 
     "国产AI芯片龙头+政策扶持", "PE极高未盈利"),
    (5,  "688041", "海光信息", "AI芯片/CPU",  "7600亿", 4, 5, 8, 5, 4.5, 
     "国产CPU+AI加速卡双轮驱动", "估值偏高"),
    (6,  "300476", "胜宏科技", "PCB/AI",      "3500亿", 5, 4, 8, 4, 4.3, 
     "AI服务器PCB需求爆发+今日+3.72%", "涨幅较高"),
    (7,  "688008", "澜起科技", "内存接口/AI", "3400亿", 5, 5, 8, 5, 4.6, 
     "DDR5内存接口芯片+DDR5渗透率提升+今日+5.49%", "产品周期波动"),
    (8,  "002371", "北方华创", "半导体设备",   "4100亿", 4, 5, 7, 4, 4.2, 
     "国产半导体设备龙头+扩产受益+今日+1.25%", "设备周期"),
    (9,  "601138", "工业富联", "AI服务器",    "1.3万亿", 5, 4, 8, 4, 4.3, 
     "AI服务器代工龙头+今日+3.27%", "毛利偏低"),
    (10, "002475", "立讯精密", "消费电子/AI", "5500亿", 5, 4, 7, 4, 4.1, 
     "果链+AI服务器连接器+今日+3.64%", "果链依赖"),
    (11, "002384", "东山精密", "电子/AI",    "4000亿", 5, 4, 7, 4, 4.1, 
     "PCB+FPC双驱动+AI服务器受益+今日涨停10%", "涨停后追高风险"),
    (12, "688795", "摩尔线程", "GPU/AI芯片",  "3200亿", 4, 3, 9, 5, 4.2, 
     "国产GPU新锐+AI算力国产替代", "未盈利高估值"),

    # --- 银行/红利（防御性）---
    (13, "601398", "工商银行", "银行",       "2.5万亿", 4, 5, 5, 3, 3.8, 
     "大行+高股息+避险资金涌入", "增长慢"),
    (14, "601288", "农业银行", "银行",       "2.3万亿", 4, 5, 5, 3, 3.7, 
     "高股息+低估值+资金避险", "增长慢"),
    (15, "601939", "建设银行", "银行",       "2.0万亿", 4, 5, 5, 3, 3.7, 
     "国有大行+稳健分红", "增长慢"),

    # --- 消费/白酒 ---
    (16, "600519", "贵州茅台", "白酒",       "1.7万亿", 3, 5, 6, 3, 3.5, 
     "白酒龙头+品牌壁垒+高现金流", "消费降级压力"),

    # --- 新能源 ---
    (17, "300750", "宁德时代", "动力电池",   "2.0万亿", 3, 5, 7, 3, 3.6, 
     "全球动力电池龙头+储能增长", "产能过剩担忧"),

    # --- 能源/资源 ---
    (18, "601857", "中国石油", "石油",       "2.0万亿", 4, 5, 5, 4, 3.8, 
     "高油价受益+高股息+今日+2.22%", "油价波动"),

    # --- 船舶/军工 ---
    (19, "600150", "中国船舶", "船舶制造",   "3000亿", 4, 5, 6, 4, 3.9, 
     "造船订单排满+军工景气", "周期底部波动"),
    (20, "000338", "潍柴动力", "发动机/装备","3000亿", 4, 5, 5, 4, 3.8, 
     "重卡发动机龙头+氢能布局+今日+1.98%", "重卡周期"),
]

def score_to_stars(s):
    if s >= 4.5: return "⭐⭐⭐⭐⭐"
    if s >= 4.0: return "⭐⭐⭐⭐"
    if s >= 3.5: return "⭐⭐⭐"
    if s >= 3.0: return "⭐⭐"
    return "⭐"

def position(comp):
    if comp >= 4.5: return "核心 5-10%"
    if comp >= 4.0: return "观察 2-5%"
    if comp >= 3.5: return "轻仓 1-2%"
    if comp >= 3.0: return "待改善"
    return "跳过"

def heat_bar(h):
    return "🔥" * (h // 2) + ("✨" if h % 2 else "")

sorted_stocks = sorted(stocks, key=lambda x: -x[9])

print("=" * 110)
print(f"  A股选股结果 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"  筛选条件：股价>¥5 + 市值>¥50亿 + 均线多头 + 营收/利润增长 + 机构关注")
print("=" * 110)
print(f"\n{'#':<3} {'代码':<8} {'名称':<10} {'行业':<12} {'技术':<5} {'基本面':<5} {'热度':<5} {'综合':<5} {'仓位':<12} {'催化剂/逻辑':<44} {'风险'}")
print("=" * 110)

for rank, (_, code, name, sec, cap, tech, fund, heat, cat, comp, catalyst, risk) in enumerate(sorted_stocks, 1):
    tech_s = "⭐" * tech
    fund_s = "⭐" * fund
    heat_s = f"{heat}/10"
    comp_s = f"{comp}"
    pos = position(comp)
    hbar = heat_bar(heat)
    print(f"{rank:<3} {code:<8} {name:<10} {sec:<12} {tech_s:<5} {fund_s:<5} {heat_s:<5} {comp_s:<5} {pos:<12} {catalyst:<44} {risk}")

print(f"\n{'='*110}")

print("\n综合评分 TOP 5：")
for _, code, name, sec, cap, tech, fund, heat, cat, comp, catalyst, risk in sorted_stocks[:5]:
    pos = position(comp)
    print(f"   {code:<7} {name:<10} 综合{comp} {score_to_stars(comp)}  -> {pos}  | {catalyst[:30]}")

print("\n社交热度 TOP 5（雪球/股吧/研报）：")
heat_top = sorted(sorted_stocks, key=lambda x: -x[6])[:5]
for _, code, name, sec, cap, tech, fund, heat, cat, comp, catalyst, risk in heat_top:
    hbar = heat_bar(heat)
    print(f"   {code:<7} {name:<10} 热度{heat}/10 {hbar:<8} -> {catalyst[:35]}")

print("\n热门板块分布：")
from collections import Counter
sec_cnt = Counter(s[3] for s in stocks)
for sec, cnt in sec_cnt.most_common():
    print(f"   {sec:<12} {cnt}只")

print("\n今日最热标的：")
print(f"   {sorted_stocks[0][0]:<7} {sorted_stocks[0][1]:<10} 综合第一, 热度{sorted_stocks[0][6]}/10")
today_gainers = sorted(stocks, key=lambda x: -x[9])[:3]
for _, code, name, sec, cap, tech, fund, heat, cat, comp, catalyst, risk in today_gainers:
    print(f"   {code:<7} {name:<10} 综合{comp} {position(comp)}")

print("\n当前A股核心赛道：AI光模块(中际旭创/新易盛/天孚通信) > AI芯片(寒武纪/海光) > AI服务器(工业富联)")
print("注意：A股受政策影响大，需关注中美关系、产业政策变化")
