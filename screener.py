#!/usr/bin/env python3
"""
选股器主程序 - 技术+基本面综合筛选
后续可通过修改参数来适配不同场景
"""
import json, sys, subprocess, urllib.parse

class StockScreener:
    """选股器核心"""
    
    FILTER_TECH = [
        "sh_curvol_o200000",    # 成交量 > 20万（放宽方便测试）
        "sh_price_o10",         # 股价 > $10
        "ta_sma20_pa",          # 股价 > SMA20
        "ta_sma50_pa",          # 股价 > SMA50  
        "ta_sma200_pa",         # 股价 > SMA200
        "ta_perf_dup",          # 近期涨幅为正
        "ta_rsi_os50",          # RSI > 50（强势区）
    ]
    
    FILTER_FUND = [
        "fa_pe_profitable",     # PE 为正
        "fa_epsyoy_pos",        # EPS同比正增长
        "fa_salesyoy_pos",      # 营收同比正增长
        "fa_curratio_o1",       # 流动比率 > 1
    ]
    
    FILTER_MARKET_CAP = {
        "mega": "cap_mega",     # > $2000亿
        "large": "cap_large",   # $100亿-$2000亿
        "mid": "cap_mid",       # $20亿-$100亿
        "small": "cap_small",   # $3亿-$20亿
    }

    def build_url(self, extra_filters=None, view='111', sort='price'):
        """构建Finviz筛选URL"""
        filters = self.FILTER_TECH + self.FILTER_FUND
        if extra_filters:
            filters += extra_filters
        
        f_str = ','.join(filters)
        url = f"https://finviz.com/screener.ashx?v={view}&f={f_str}&ft=4&o={sort}"
        return url, filters

    def describe_filters(self, filters):
        """解释当前筛选条件"""
        descriptions = {
            "sh_curvol_o200000": "成交量 > 20万",
            "sh_price_o10": "股价 > $10",
            "ta_sma20_pa": "股价在SMA20之上",
            "ta_sma50_pa": "股价在SMA50之上",
            "ta_sma200_pa": "股价在SMA200之上",
            "ta_perf_dup": "近期涨幅为正",
            "ta_rsi_os50": "RSI > 50（强势区）",
            "fa_pe_profitable": "PE为正（盈利）",
            "fa_epsyoy_pos": "EPS同比增长",
            "fa_salesyoy_pos": "营收同比增长",
            "fa_curratio_o1": "流动比率 > 1",
        }
        return "\n".join([f"  ✓ {descriptions.get(f, f)}" for f in filters if f in descriptions])

# 预设筛选场景
SCENARIOS = {
    "default": {
        "name": "标准多头选股",
        "filters": [],
        "desc": "均线多头 + 基本面健康 + 流动性充足"
    },
    "ai_semiconductor": {
        "name": "AI/半导体",
        "filters": ["sec_technology", "ind_semiconductors"],
        "desc": "科技板块半导体行业"
    },
    "consumer_defensive": {
        "name": "消费防御",
        "filters": ["sec_consumer_defensive"],
        "desc": "防御性消费板块"
    },
    "high_dividend": {
        "name": "高股息",
        "filters": ["fa_div_o1"],
        "desc": "有股息 + 均线多头"
    },
    "financial": {
        "name": "金融龙头",
        "filters": ["sec_financial"],
        "desc": "金融板块多头排列"
    },
}

if __name__ == "__main__":
    screener = StockScreener()
    
    scenario = sys.argv[1] if len(sys.argv) > 1 else "default"
    
    if scenario == "list":
        for k, v in SCENARIOS.items():
            print(f"  {k:25s} → {v['name']}")
        sys.exit(0)
    
    if scenario not in SCENARIOS:
        print(f"未知场景: {scenario}")
        print("可选场景:")
        for k in SCENARIOS:
            print(f"  {k}")
        sys.exit(1)
    
    s = SCENARIOS[scenario]
    url, filters = screener.build_url(s["filters"])
    
    print(f"📊 选股场景：{s['name']}")
    print(f"📝 描述：{s['desc']}")
    print(f"\n🔍 筛选条件：")
    print(screener.describe_filters(filters))
    print(f"\n🔗 Finviz Screener URL：")
    print(url)
    print(f"\n💡 操作提示：")
    print(f"   打开上述URL查看完整结果")
