// ========================================
// 美股选股器 - 核心数据模型
// ========================================

// ---- 30个社交热度源 ----
const SOURCES = {
  macro: [
    { name: 'Liz Ann Sonders', handle: '@LizAnnSonders', title: '嘉信首席策略师' },
    { name: 'Mohamed El-Erian', handle: '@elerianm', title: 'PIMCO前CEO' },
    { name: 'Barry Ritholtz', handle: '@ritholtz', title: 'Ritholtz财富CEO' },
    { name: 'Jeff Gundlach', handle: '@TruthGundlach', title: '债券之王' },
    { name: 'David Rosenberg', handle: '@EconguyRosie', title: 'Rosenberg Research' },
  ],
  trading: [
    { name: 'Brian Shannon', handle: '@alphatrends', title: 'VWAP大师' },
    { name: 'Peter Brandt', handle: '@PeterLBrandt', title: '40年图表交易员' },
    { name: 'Nathan Michaud', handle: '@InvestorsLive', title: '日内交易' },
    { name: 'Tom Lee', handle: '@fundstrat', title: 'Fundstrat创始人' },
  ],
  deep: [
    { name: 'Morgan Housel', handle: '@morganhousel', title: '金钱心理学作者' },
    { name: '10-K Diver', handle: '@10kdiver', title: '基本面拆解' },
    { name: 'Brian Feroldi', handle: '@BrianFeroldi', title: '财报教学' },
    { name: 'Byrne Hobart', handle: '@ByrneHobart', title: '金融+科技深入' },
  ],
  whales: [
    { name: 'Bill Ackman', handle: '@BillAckman', title: 'Pershing Square' },
    { name: 'Ray Dalio', handle: '@RayDalio', title: 'Bridgewater' },
    { name: 'David Einhorn', handle: '@DavidEinhorn', title: 'Greenlight Capital' },
    { name: 'Howard Marks', handle: '@HowardCMarks', title: 'Oaktree Capital' },
    { name: 'Carl Icahn', handle: '@Carl_C_Icahn', title: 'Icahn Enterprises' },
  ],
  kol: [
    { name: 'Joseph Wang', handle: '@josephwang', title: '美联储分析' },
    { name: '美股OK哥', handle: '@artinmemes', title: '实战交易' },
    { name: 'Lyn Alden', handle: '@LynAldenContact', title: '宏观底层' },
    { name: 'Jim Bianco', handle: '@biancoresearch', title: '利率/债市' },
    { name: '投资TALK君', handle: '@TJ_Research', title: '宏观+美股+AI' },
    { name: 'Nico投资有道', handle: '@tychozzz', title: '长期投资' },
  ],
  news: [
    { name: 'DeItaone', handle: '@DeItaone', title: 'Bloomberg消息流' },
    { name: 'Unusual Whales', handle: '@unusual_whales', title: '期权异动' },
    { name: 'ZeroHedge', handle: '@ZeroHedge', title: '金融数据挖掘' },
    { name: 'WSJ Markets', handle: '@WSJmarkets', title: '华尔街日报' },
    { name: 'SoberLook', handle: '@SoberLook', title: '宏观信贷深度' },
    { name: 'LiveSquawk', handle: '@LiveSquawk', title: '央行/经济数据' },
  ]
};

// ---- 股票数据模型 ----
/*
  ticker:   代码
  name:     公司名
  sector:   板块
  cap:      市值分类
  price:    当前价
  change:   涨跌幅(%)
  tech:     技术分(1-5)
  fund:     基本面分(1-5)
  heat:     社交热度(0-10)
  catalyst: 催化剂分(0-5)
  comp:     综合分(0-5)
  position: 仓位建议
  description: 催化剂描述
  risk:     风险提示
  stars:    星级
  industry: 行业细分
*/

const STOCK_DATABASE = {
  // ---- 科技/半导体 ----
  nvda: {
    ticker: 'NVDA', name: 'NVIDIA', sector: '科技', industry: '半导体',
    cap: 'Mega', price: 234.87, change: 4.00,
    tech: 5, fund: 5, heat: 9, catalyst: 5, comp: 4.8,
    position: 'core',
    description: 'Blackwell量产+中美AI峰会+13F持仓增持',
    risk: 'PE 48中等偏高'
  },
  csco: {
    ticker: 'CSCO', name: 'Cisco', sector: '科技', industry: '通信设备',
    cap: 'Mega', price: 117.31, change: 15.16,
    tech: 5, fund: 5, heat: 8, catalyst: 5, comp: 4.7,
    position: 'core',
    description: 'NVIDIA战略入股+AI-RAN转型+财报暴打预期',
    risk: '单日+15%超买，建议回调后介入'
  },
  avgo: {
    ticker: 'AVGO', name: 'Broadcom', sector: '科技', industry: '半导体',
    cap: 'Mega', price: 436.09, change: 2.10,
    tech: 5, fund: 5, heat: 8, catalyst: 5, comp: 4.7,
    position: 'core',
    description: 'AI定制芯片+AISC需求爆发+VMware整合',
    risk: 'PE 85较高'
  },
  meta: {
    ticker: 'META', name: 'Meta', sector: '科技', industry: '互联网',
    cap: 'Mega', price: 622.39, change: 0.79,
    tech: 5, fund: 5, heat: 8, catalyst: 4, comp: 4.5,
    position: 'core',
    description: 'AI广告+开源Llama生态+Q2指引强劲',
    risk: '反垄断监管风险'
  },
  msft: {
    ticker: 'MSFT', name: 'Microsoft', sector: '科技', industry: '软件',
    cap: 'Mega', price: 409.01, change: 0.94,
    tech: 5, fund: 5, heat: 9, catalyst: 4, comp: 4.5,
    position: 'core',
    description: 'Azure+AI Copilot+机构重仓持股',
    risk: '走势稳健但短期波动较小'
  },
  now: {
    ticker: 'NOW', name: 'ServiceNow', sector: '科技', industry: '软件',
    cap: 'Large', price: 1080.00, change: 1.20,
    tech: 5, fund: 5, heat: 7, catalyst: 5, comp: 4.4,
    position: 'watch',
    description: 'AI Agent工作流+Q1超预期',
    risk: '估值偏高'
  },
  pltr: {
    ticker: 'PLTR', name: 'Palantir', sector: '科技', industry: '软件',
    cap: 'Large', price: 133.28, change: 2.48,
    tech: 4, fund: 4, heat: 8, catalyst: 5, comp: 4.3,
    position: 'watch',
    description: 'AIP政府订单+企业AI应用落地',
    risk: 'PE极高'
  },
  mrvl: {
    ticker: 'MRVL', name: 'Marvell Tech', sector: '科技', industry: '半导体',
    cap: 'Large', price: 85.00, change: 3.10,
    tech: 4, fund: 4, heat: 7, catalyst: 5, comp: 4.2,
    position: 'watch',
    description: '定制AI芯片(AISC)新爆款',
    risk: '体量较小'
  },
  orcl: {
    ticker: 'ORCL', name: 'Oracle', sector: '科技', industry: '软件',
    cap: 'Large', price: 198.75, change: 4.70,
    tech: 5, fund: 4, heat: 7, catalyst: 4, comp: 4.2,
    position: 'watch',
    description: '云基建+AI订单大增+4.7%',
    risk: '毛利率承压'
  },
  amat: {
    ticker: 'AMAT', name: 'Applied Materials', sector: '科技', industry: '半导体设备',
    cap: 'Large', price: 444.74, change: 1.90,
    tech: 5, fund: 4, heat: 7, catalyst: 4, comp: 4.1,
    position: 'watch',
    description: 'AI投资扩产，设备龙头受益',
    risk: '周期敏感'
  },
  anet: {
    ticker: 'ANET', name: 'Arista Networks', sector: '科技', industry: '通信设备',
    cap: 'Large', price: 110.00, change: 1.10,
    tech: 5, fund: 5, heat: 6, catalyst: 4, comp: 4.1,
    position: 'watch',
    description: '数据中心网络冠军',
    risk: 'CSCO竞争加剧'
  },
  googl: {
    ticker: 'GOOGL', name: 'Alphabet', sector: '科技', industry: '互联网',
    cap: 'Mega', price: 401.70, change: -0.23,
    tech: 5, fund: 5, heat: 7, catalyst: 3, comp: 4.0,
    position: 'watch',
    description: 'Gemini+Google Cloud AI',
    risk: '反垄断压制'
  },
  amzn: {
    ticker: 'AMZN', name: 'Amazon', sector: '科技', industry: '电商/云',
    cap: 'Mega', price: 268.36, change: -0.66,
    tech: 4, fund: 5, heat: 7, catalyst: 3, comp: 3.9,
    position: 'light',
    description: 'AWS AI需求+成本优化',
    risk: '今日回调-0.7%'
  },
  mu: {
    ticker: 'MU', name: 'Micron', sector: '科技', industry: '半导体',
    cap: 'Large', price: 786.30, change: -2.16,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.8,
    position: 'light',
    description: 'HBM3E高增长+存储周期上行',
    risk: '今日-2.2%'
  },
  amd: {
    ticker: 'AMD', name: 'AMD', sector: '科技', industry: '半导体',
    cap: 'Large', price: 449.14, change: 0.82,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.8,
    position: 'light',
    description: 'MI300追赶NVDA',
    risk: '与NVDA差距拉大'
  },

  // ---- 消费防御 ----
  cost: {
    ticker: 'COST', name: 'Costco', sector: '消费防御', industry: '零售',
    cap: 'Mega', price: 1034.74, change: 0.16,
    tech: 5, fund: 5, heat: 7, catalyst: 4, comp: 4.3,
    position: 'watch',
    description: '会员制零售+成长防御双属性',
    risk: '股息率偏低0.57%'
  },
  wmt: {
    ticker: 'WMT', name: 'Walmart', sector: '消费防御', industry: '零售',
    cap: 'Mega', price: 132.12, change: 0.50,
    tech: 5, fund: 5, heat: 6, catalyst: 4, comp: 4.2,
    position: 'watch',
    description: '电商转型+AI供应链优化',
    risk: '零售竞争激烈'
  },
  pg: {
    ticker: 'PG', name: 'Procter & Gamble', sector: '消费防御', industry: '消费品',
    cap: 'Mega', price: 143.71, change: 1.02,
    tech: 4, fund: 5, heat: 5, catalyst: 3, comp: 3.9,
    position: 'light',
    description: '消费刚需+涨价传导+股息3.0%',
    risk: '增长慢'
  },
  ko: {
    ticker: 'KO', name: 'Coca-Cola', sector: '消费防御', industry: '饮料',
    cap: 'Mega', price: 80.89, change: 0.79,
    tech: 4, fund: 5, heat: 6, catalyst: 3, comp: 3.8,
    position: 'light',
    description: '全球品牌+股息王者+股息2.6%',
    risk: '增长慢'
  },

  // ---- 金融 ----
  jpm: {
    ticker: 'JPM', name: 'JPMorgan Chase', sector: '金融', industry: '银行',
    cap: 'Mega', price: 302.78, change: 0.84,
    tech: 3, fund: 5, heat: 6, catalyst: 3, comp: 3.3,
    position: 'light',
    description: '全能银行+AI应用',
    risk: '短期均线走弱'
  },
  gs: {
    ticker: 'GS', name: 'Goldman Sachs', sector: '金融', industry: '投行',
    cap: 'Mega', price: 580.00, change: 0.50,
    tech: 4, fund: 4, heat: 5, catalyst: 4, comp: 3.6,
    position: 'light',
    description: '投行复苏+AI布局',
    risk: '波动大'
  },

  // ---- 能源 ----
  xom: {
    ticker: 'XOM', name: 'ExxonMobil', sector: '能源', industry: '油气',
    cap: 'Mega', price: 152.19, change: 0.41,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.7,
    position: 'light',
    description: '油价高位+回购强劲+股息2.7%',
    risk: '油价波动'
  },
  cvx: {
    ticker: 'CVX', name: 'Chevron', sector: '能源', industry: '油气',
    cap: 'Mega', price: 186.28, change: 0.15,
    tech: 4, fund: 4, heat: 5, catalyst: 3, comp: 3.5,
    position: 'light',
    description: '能源整合+股东回报+股息3.8%',
    risk: '油价波动'
  },
};

// ---- 板块表现 ----
const SECTOR_PERFORMANCE = [
  { name: '科技', week: '+4.59%', month: '+14.90%', quarter: '+22.77%', ytd: '+19.63%', change: '+1.79%', rank: 1 },
  { name: '通信服务', week: '-0.06%', month: '+6.00%', quarter: '+12.76%', ytd: '+9.03%', change: '-0.14%', rank: 2 },
  { name: '消费防御', week: '+1.62%', month: '+4.96%', quarter: '-3.49%', ytd: '+11.09%', change: '+0.67%', rank: 3 },
  { name: '能源', week: '+2.98%', month: '+3.27%', quarter: '+11.69%', ytd: '+31.29%', change: '+0.72%', rank: 4 },
  { name: '工业', week: '+0.61%', month: '+2.25%', quarter: '+2.19%', ytd: '+15.06%', change: '+0.72%', rank: 5 },
  { name: '金融', week: '-0.32%', month: '-1.15%', quarter: '-1.15%', ytd: '-3.21%', change: '+0.51%', rank: 9 },
  { name: '医疗', week: '+1.03%', month: '-1.35%', quarter: '-4.85%', ytd: '-3.67%', change: '-0.13%', rank: 10 },
];

// ---- 工具函数 ----
function stars(n) {
  return '⭐'.repeat(n);
}

function fires(n) {
  const full = Math.floor(n / 2);
  const half = n % 2;
  return '🔥'.repeat(full) + (half ? '✨' : '');
}

function positionLabel(pos) {
  const labels = {
    core: '核心仓位 5-10%',
    watch: '观察仓位 2-5%',
    light: '轻仓试探 1-2%',
    skip: '跳过'
  };
  return labels[pos] || pos;
}

function formatChange(val) {
  const sign = val >= 0 ? '+' : '';
  return `<span class="change-${val >= 0 ? 'up' : 'down'}">${sign}${val.toFixed(2)}%</span>`;
}

function scoreColor(score) {
  if (score >= 4.5) return '#3fb950';
  if (score >= 4.0) return '#58a6ff';
  if (score >= 3.5) return '#d29922';
  return '#f85149';
}
