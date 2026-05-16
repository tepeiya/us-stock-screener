#!/usr/bin/env python3
"""
ARK交易数据同步脚本
从 /var/minis/shared/ark-trades/ 读取最新ARK交易日报
自动解析表格，更新到 screener-data.js 的 ARK_DATA 字段
然后提交推送 git
"""
import re, os, subprocess
from datetime import datetime

WORKSPACE = '/var/minis/workspace'
ARK_DIR = '/var/minis/shared/ark-trades'

def parse_trade_row(row):
    """解析一行ARK交易表格"""
    # 格式: | ARKK | 🔴 Sell | TSMA | $12.6M | $338.00 | 37,278 | 5.76% | 📉 减仓 |
    row = row.strip()
    if not row.startswith('|') or '基金' in row or '---' in row:
        return None
    
    parts = [p.strip() for p in row.split('|')]
    parts = [p for p in parts if p]  # 去掉空字符串
    
    if len(parts) < 6:
        return None
    
    fund = parts[0] if len(parts) > 0 else ''
    action = parts[1] if len(parts) > 1 else ''
    ticker = parts[2] if len(parts) > 2 else ''
    amount = parts[3] if len(parts) > 3 else ''
    price = parts[4] if len(parts) > 4 else ''
    shares = parts[5] if len(parts) > 5 else ''
    pct = parts[6] if len(parts) > 6 else ''
    status = parts[7] if len(parts) > 7 else ''
    
    # 标准化基金名
    fund = fund.replace('**', '').strip()
    # 标准化操作
    is_buy = 'Buy' in action or 'buy' in action
    action_type = 'buy' if is_buy else 'sell'
    # 提取ticker
    ticker = ticker.replace('**', '').strip()
    # 提取交易金额
    amount = amount.replace('**', '').strip()
    price = price.replace('**', '').strip()
    shares = shares.replace('**', '').strip().replace(',', '')
    pct = pct.replace('**', '').strip()
    status = status.replace('**', '').strip()
    
    if not ticker or not amount:
        return None
    
    return {
        'fund': fund,
        'type': action_type,
        'ticker': ticker,
        'amount': amount,
        'price': price,
        'shares': shares,
        'pct': pct,
        'status': status
    }

def parse_ark_file(filepath):
    """解析ARK交易日报文件，返回结构化数据"""
    with open(filepath) as f:
        content = f.read()
    
    # 提取更新时间
    update_match = re.search(r'> 更新时间: (.+?)<', content)
    last_updated = update_match.group(1).strip() if update_match else datetime.now().strftime('%Y-%m-%d %H:%M')
    
    # 按日期分割
    date_blocks = re.split(r'### 📅 ', content)
    
    result = []
    for block in date_blocks[1:]:  # 跳过第一个非日期块
        lines = block.split('\n')
        date_str = lines[0].strip() if lines else ''
        
        # 找到表格行（跳过表头和空行）
        trades = []
        for line in lines:
            if line.startswith('|') and '基金' not in line and '---' not in line and '：' not in line and '标识' not in line:
                trade = parse_trade_row(line)
                if trade:
                    trades.append(trade)
        
        if date_str and trades:
            day_data = {'date': date_str, 'buys': [], 'sells': []}
            for t in trades:
                if t['type'] == 'buy':
                    day_data['buys'].append(t)
                else:
                    day_data['sells'].append(t)
            # 只保留有交易的日期
            if day_data['buys'] or day_data['sells']:
                result.append(day_data)
    
    return last_updated, result[:7]  # 最多保留7天

def generate_ark_js(last_updated, recent_days):
    """生成ARK_DATA的JavaScript代码块"""
    
    def trade_to_js(t):
        return f"{{fund: '{t['fund']}', ticker: '{t['ticker']}', amount: '{t['amount']}', price: '{t['price']}', shares: '{t['shares']}', pct: '{t['pct']}'}}"
    
    days_js = []
    for day in recent_days:
        buys = f"[{','.join(trade_to_js(t) for t in day['buys'])}]" if day['buys'] else '[]'
        sells = f"[{','.join(trade_to_js(t) for t in day['sells'])}]" if day['sells'] else '[]'
        days_js.append(f"{{date: '{day['date']}', buys: {buys}, sells: {sells}}}")
    
    js = f"""
const ARK_DATA = {{
  lastUpdated: '{last_updated}',
  recentDays: [
    {','.join(days_js)}
  ]
}};
"""
    return js.strip()

def update_js_file(ark_js_block):
    """替换 screener-data.js 中的 ARK_DATA 部分"""
    js_path = os.path.join(WORKSPACE, 'screener-data.js')
    
    with open(js_path) as f:
        content = f.read()
    
    # 找到 ARK_DATA 的起始和结束位置
    start_marker = 'const ARK_DATA'
    end_marker = '\n// ---- 工具函数 ----'
    
    # 如果没有ARK_DATA，追加到文件末尾
    if start_marker not in content:
        # 在函数定义之前插入
        func_marker = 'function daysUntil'
        insert_pos = content.find(func_marker)
        if insert_pos > 0:
            # 找到func_marker前的空行
            content = content[:insert_pos] + ark_js_block + '\n\n' + content[insert_pos:]
        else:
            content += '\n\n' + ark_js_block
        print("  → 新增 ARK_DATA 块")
    else:
        # 替换现有ARK_DATA块
        start = content.find(start_marker)
        end = content.find(end_marker, start)
        if end > start:
            content = content[:start] + ark_js_block + '\n\n' + content[end:]
            print("  → 替换 ARK_DATA 块")
    
    with open(js_path, 'w') as f:
        f.write(content)
    
    print(f"  → screener-data.js 更新完成")

def git_push():
    """提交并推送git"""
    os.chdir(WORKSPACE)
    
    # git add
    subprocess.run(['git', 'add', 'screener-data.js'], capture_output=True)
    
    # git commit
    date_str = datetime.now().strftime('%Y-%m-%d')
    result = subprocess.run(
        ['git', 'commit', '-m', f'chore: 更新ARK交易数据 {date_str}'],
        capture_output=True, text=True
    )
    print(f"  → {result.stdout.strip()}")
    if result.stderr:
        print(f"  → {result.stderr.strip()}")
    
    # 没有变更就退出
    if 'nothing to commit' in result.stdout or 'nothing to commit' in result.stderr:
        print("  → 数据无变化，跳过推送")
        return
    
    # git push
    push = subprocess.run(['git', 'push'], capture_output=True, text=True)
    print(f"  → {push.stdout.strip()}")
    if push.stderr:
        # 只显示最后几行
        lines = push.stderr.strip().split('\n')
        for l in lines[-3:]:
            print(f"  → {l.strip()}")

def main():
    print(f"🔄 ARK数据同步 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # 找到最新的ARK文件
    ark_files = sorted([f for f in os.listdir(ARK_DIR) if f.startswith('ARK交易日报')])
    if not ark_files:
        print("❌ 未找到ARK交易日报文件")
        return
    
    latest_file = os.path.join(ARK_DIR, ark_files[-1])
    print(f"📂 读取: {ark_files[-1]}")
    
    # 解析
    last_updated, recent_days = parse_ark_file(latest_file)
    print(f"📊 解析完成: {len(recent_days)}天交易数据")
    print(f"  更新时间: {last_updated}")
    
    for day in recent_days:
        buy_count = len(day['buys'])
        sell_count = len(day['sells'])
        print(f"  {day['date']}: 🟢{buy_count}笔买入 🔴{sell_count}笔卖出")
    
    # 生成JS
    ark_js = generate_ark_js(last_updated, recent_days)
    
    # 更新文件
    update_js_file(ark_js)
    
    # 推送到GitHub
    print("📤 推送到GitHub...")
    git_push()
    
    print("✅ 完成!")

if __name__ == '__main__':
    main()
