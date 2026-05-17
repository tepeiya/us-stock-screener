// ========================================
// 美股选股器 v2.0 - 核心数据模型
// 数据同步自对话版选股器
// ========================================

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

// ---- 13F最新持仓数据（模拟数据，代表季报方向）----
// 来源：13F季度13D/G filings

const HEDGE_FUND_13F = {
  warren_buffett: {name:'Buffett',fund:'Berkshire Hathaway',portfolio_value:'$368B',
    top_buys:[{ticker:'CVX',amount:'+$320M'},{ticker:'OXY',amount:'+$280M'},{ticker:'AXP',amount:'+$156M'}],
    top_sells:[{ticker:'AAPL',amount:'-$1.2B'}],last_updated:'2026-Q1'},
  jim_simons: {name:'Simons (Renaissance)',fund:'Renaissance Technologies',portfolio_value:'$63.9B',
    top_buys:[{ticker:'AAPL',amount:'+$781M'},{ticker:'NVDA',amount:'+$278M'},{ticker:'AVGO',amount:'+$245M'},{ticker:'JPM',amount:'+$202M'}],
    top_sells:[{ticker:'NFLX',amount:'-$673M'},{ticker:'COST',amount:'-$578M'},{ticker:'PLTR',amount:'-$542M'},{ticker:'MSFT',amount:'-$329M'}],
    last_updated:'2026-Q1'},
  ray_dalio: {name:'Ray Dalio',fund:'Bridgewater',portfolio_value:'$97B',
    top_buys:[{ticker:'NVDA',amount:'+$412M'},{ticker:'GOOGL',amount:'+$356M'},{ticker:'AMZN',amount:'+$298M'},{ticker:'COST',amount:'+$215M'}],
    top_sells:[{ticker:'KO',amount:'-$185M'}],last_updated:'2026-Q1'},
  ken_griffin: {name:'Ken Griffin',fund:'Citadel Advisors',portfolio_value:'$62B',
    top_buys:[{ticker:'NVDA',amount:'+$850M'},{ticker:'AVGO',amount:'+$620M'},{ticker:'MSFT',amount:'+$510M'},{ticker:'AMZN',amount:'+$420M'}],
    top_sells:[{ticker:'AAPL',amount:'-$380M'}],last_updated:'2026-Q1'},
  chase_coleman: {name:'Chase Coleman',fund:'Tiger Global',portfolio_value:'$36B',
    top_buys:[{ticker:'META',amount:'+$480M'},{ticker:'NVDA',amount:'+$320M'},{ticker:'MSFT',amount:'+$280M'}],
    top_sells:[{ticker:'SE',amount:'-$195M'}],last_updated:'2026-Q1'},
  steve_cohen: {name:'Steve Cohen',fund:'Point72',portfolio_value:'$34B',
    top_buys:[{ticker:'NVDA',amount:'+$350M'},{ticker:'AVGO',amount:'+$280M'},{ticker:'PLTR',amount:'+$145M'}],
    top_sells:[{ticker:'AAPL',amount:'-$120M'}],last_updated:'2026-Q1'},
  bill_ackman: {name:'Bill Ackman',fund:'Pershing Square',portfolio_value:'$16B',
    top_buys:[{ticker:'GOOGL',amount:'+$520M'}],
    top_sells:[],last_updated:'2026-Q1'},
  daniel_loeb: {name:'Daniel Loeb',fund:'Third Point',portfolio_value:'$18B',
    top_buys:[{ticker:'GOOGL',amount:'+$210M'},{ticker:'AMZN',amount:'+$175M'},{ticker:'NOW',amount:'+$88M'}],
    top_sells:[],last_updated:'2026-Q1'},
  howard_marks: {name:'Howard Marks',fund:'Oaktree Capital',portfolio_value:'$192B',
    top_buys:[{ticker:'CSCO',amount:'+$135M'}],
    top_sells:[],last_updated:'2026-Q1'},
  david_einhorn: {name:'David Einhorn',fund:'Greenlight Capital',portfolio_value:'$3.5B',
    top_buys:[{ticker:'GOOGL',amount:'+$85M'},{ticker:'AMZN',amount:'+$62M'},{ticker:'META',amount:'+$48M'}],
    top_sells:[],last_updated:'2026-Q1'},
  david_tepper: {name:'David Tepper',fund:'Appaloosa',portfolio_value:'$6.5B',
    top_buys:[{ticker:'AMZN',amount:'+$165M'},{ticker:'META',amount:'+$120M'},{ticker:'NVDA',amount:'+$98M'}],
    top_sells:[],last_updated:'2026-Q1'},
  nelson_peltz: {name:'Nelson Peltz',fund:'Trian',portfolio_value:'$8.5B',
    top_buys:[{ticker:'PG',amount:'+$95M'},{ticker:'JPM',amount:'+$72M'}],
    top_sells:[],last_updated:'2026-Q1'}
};

// ---- 股票数据模型 ----
// 新增字段:
//   exit_signals: 退场信号
//   earnings_date: 下次财报日期
//   hedge_fund_buys: 大佬增持列表
//   option_flow: 期权异动信号

const STOCK_DATABASE = {

  nvda: {
    ticker: 'NVDA', name: 'NVIDIA', sector: '科技', industry: '半导体',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 9, catalyst: 5, comp: 4.8,
    position: 'core',
    description: 'Blackwell量产+中美AI峰会+13F增持',
    risk: 'PE 48中等偏高',
    earnings_date: '2026-05-28',
    earnings_beat: 'Q1超预期+12%',
    hedge_fund_buys: ["Bridgewater", "Citadel", "Renaissance"],
    option_flow: '大单Call 5/28行权价$240',
    exit: {"stop": -15, "rsi_sell": 85, "ma_violation": "SMA50", "status": "持有"}
  },

  csco: {
    ticker: 'CSCO', name: 'Cisco', sector: '科技', industry: '通信设备',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 8, catalyst: 5, comp: 4.7,
    position: 'watch',
    description: 'NVIDIA战略入股+AI-RAN转型+财报暴打预期',
    risk: '单日+15%超买，建议回调后介入',
    earnings_date: '2026-08-12',
    earnings_beat: 'Q3超预期+15%',
    hedge_fund_buys: ["Oaktree"],
    option_flow: '大单Call 6月$120',
    exit: {"stop": -10, "rsi_sell": 90, "ma_violation": "SMA20", "status": "超买预警"}
  },

  avgo: {
    ticker: 'AVGO', name: 'Broadcom', sector: '科技', industry: '半导体',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 8, catalyst: 5, comp: 4.7,
    position: 'core',
    description: 'AI定制芯片+AISC需求爆发+VMware整合',
    risk: 'PE 85较高',
    earnings_date: '2026-06-04',
    earnings_beat: 'Q1超预期+9%',
    hedge_fund_buys: ["Citadel", "Point72", "Renaissance"],
    option_flow: '深价外Call 7月$450累计3000张',
    exit: {"stop": -12, "rsi_sell": 82, "ma_violation": "SMA50", "status": "持有"}
  },

  meta: {
    ticker: 'META', name: 'Meta', sector: '科技', industry: '互联网',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 8, catalyst: 4, comp: 4.5,
    position: 'core',
    description: 'AI广告+开源Llama生态+Q2指引强劲',
    risk: '反垄断监管风险',
    earnings_date: '2026-07-29',
    earnings_beat: 'Q1超预期+11%',
    hedge_fund_buys: ["Bridgewater", "Greenlight"],
    option_flow: 'Call价差6月$620/$650',
    exit: {"stop": -18, "rsi_sell": 85, "ma_violation": "SMA50", "status": "持有"}
  },

  msft: {
    ticker: 'MSFT', name: 'Microsoft', sector: '科技', industry: '软件',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 9, catalyst: 4, comp: 4.5,
    position: 'core',
    description: 'Azure+AI Copilot+机构重仓持股',
    risk: '走势稳健但短期波动较小',
    earnings_date: '2026-07-22',
    earnings_beat: 'Q3超预期+8%',
    hedge_fund_buys: ["Bridgewater", "Citadel", "Renaissance"],
    option_flow: '累计Call仓位高',
    exit: {"stop": -15, "rsi_sell": 80, "ma_violation": "SMA50", "status": "持有"}
  },

  now: {
    ticker: 'NOW', name: 'ServiceNow', sector: '科技', industry: '软件',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 5, heat: 7, catalyst: 5, comp: 4.4,
    position: 'watch',
    description: 'AI Agent工作流+Q1超预期',
    risk: '估值偏高',
    earnings_date: '2026-07-23',
    earnings_beat: 'Q1超预期+10%',
    hedge_fund_buys: [],
    option_flow: '温和Call',
    exit: {"stop": -15, "rsi_sell": 85, "ma_violation": "SMA50", "status": "持有"}
  },

  pltr: {
    ticker: 'PLTR', name: 'Palantir', sector: '科技', industry: '软件',
    cap: 'Large', price: 0, change: 0,
    tech: 4, fund: 4, heat: 8, catalyst: 5, comp: 4.3,
    position: 'watch',
    description: 'AIP政府订单+企业AI应用落地',
    risk: 'PE极高',
    earnings_date: '2026-05-06',
    earnings_beat: 'Q1超预期+18%',
    hedge_fund_buys: ["Citadel", "Point72"],
    option_flow: '大单Call 6月$140',
    exit: {"stop": -20, "rsi_sell": 88, "ma_violation": "SMA20", "status": "持有"}
  },

  cost: {
    ticker: 'COST', name: 'Costco', sector: '消费防御', industry: '零售',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 7, catalyst: 4, comp: 4.3,
    position: 'watch',
    description: '会员制零售+成长防御双属性',
    risk: '股息率偏低0.57%',
    earnings_date: '2026-05-29',
    earnings_beat: 'Q2超预期+7%',
    hedge_fund_buys: ["Bridgewater", "Berkshire"],
    option_flow: '温和看涨',
    exit: {"stop": -12, "rsi_sell": 78, "ma_violation": "SMA50", "status": "持有"}
  },

  mrvl: {
    ticker: 'MRVL', name: 'Marvell Tech', sector: '科技', industry: '半导体',
    cap: 'Large', price: 0, change: 0,
    tech: 4, fund: 4, heat: 7, catalyst: 5, comp: 4.2,
    position: 'watch',
    description: '定制AI芯片(AISC)新爆款',
    risk: '体量较小',
    earnings_date: '2026-05-29',
    earnings_beat: '待定',
    hedge_fund_buys: [],
    option_flow: '温和看涨',
    exit: {"stop": -20, "rsi_sell": 85, "ma_violation": "SMA50", "status": "持有"}
  },

  orcl: {
    ticker: 'ORCL', name: 'Oracle', sector: '科技', industry: '软件',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 4, heat: 7, catalyst: 4, comp: 4.2,
    position: 'watch',
    description: '云基建+AI订单大增+4.7%',
    risk: '毛利率承压',
    earnings_date: '2026-06-10',
    earnings_beat: 'Q3超预期+6%',
    hedge_fund_buys: ["Bridgewater"],
    option_flow: '温和看涨',
    exit: {"stop": -15, "rsi_sell": 82, "ma_violation": "SMA50", "status": "持有"}
  },

  wmt: {
    ticker: 'WMT', name: 'Walmart', sector: '消费防御', industry: '零售',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 6, catalyst: 4, comp: 4.2,
    position: 'watch',
    description: '电商转型+AI供应链优化',
    risk: '零售竞争激烈',
    earnings_date: '2026-05-21',
    earnings_beat: '待公布',
    hedge_fund_buys: ["Berkshire"],
    option_flow: '温和看涨',
    exit: {"stop": -12, "rsi_sell": 78, "ma_violation": "SMA50", "status": "持有"}
  },

  amat: {
    ticker: 'AMAT', name: 'Applied Materials', sector: '科技', industry: '半导体设备',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 4, heat: 7, catalyst: 4, comp: 4.1,
    position: 'watch',
    description: 'AI投资扩产，设备龙头受益',
    risk: '周期敏感 | 数据非实时',
    earnings_date: '2026-05-15',
    earnings_beat: '今日盘后财报',
    hedge_fund_buys: [],
    option_flow: '末日期权博弈',
    exit: {"stop": -15, "rsi_sell": 80, "ma_violation": "SMA50", "status": "财报窗口期"}
  },

  anet: {
    ticker: 'ANET', name: 'Arista Networks', sector: '科技', industry: '通信设备',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 5, heat: 6, catalyst: 4, comp: 4.1,
    position: 'watch',
    description: '数据中心网络冠军',
    risk: 'CSCO竞争加剧',
    earnings_date: '2026-05-01',
    earnings_beat: 'Q1超预期+7%',
    hedge_fund_buys: ["Bridgewater"],
    option_flow: '温和看涨',
    exit: {"stop": -15, "rsi_sell": 82, "ma_violation": "SMA50", "status": "持有"}
  },

  googl: {
    ticker: 'GOOGL', name: 'Alphabet', sector: '科技', industry: '互联网',
    cap: 'Mega', price: 0, change: 0,
    tech: 5, fund: 5, heat: 7, catalyst: 3, comp: 4.0,
    position: 'watch',
    description: 'Gemini+Google Cloud AI',
    risk: '反垄断压制',
    earnings_date: '2026-07-23',
    earnings_beat: 'Q1超预期+8%',
    hedge_fund_buys: ["Pershing Square", "Bridgewater", "Greenlight"],
    option_flow: 'Call堆积',
    exit: {"stop": -15, "rsi_sell": 80, "ma_violation": "SMA50", "status": "持有"}
  },

  amzn: {
    ticker: 'AMZN', name: 'Amazon', sector: '科技', industry: '电商/云',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 5, heat: 7, catalyst: 3, comp: 3.9,
    position: 'light',
    description: 'AWS AI需求+成本优化',
    risk: '今日回调-0.7%',
    earnings_date: '2026-07-30',
    earnings_beat: 'Q1超预期+6%',
    hedge_fund_buys: ["Bridgewater", "Greenlight"],
    option_flow: '温和看涨',
    exit: {"stop": -15, "rsi_sell": 80, "ma_violation": "SMA20", "status": "持有"}
  },

  pg: {
    ticker: 'PG', name: 'Procter & Gamble', sector: '消费防御', industry: '消费品',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 5, heat: 5, catalyst: 3, comp: 3.9,
    position: 'light',
    description: '消费刚需+涨价传导+股息3.0%',
    risk: '增长慢',
    earnings_date: '2026-07-23',
    earnings_beat: 'Q3超预期+4%',
    hedge_fund_buys: ["Berkshire"],
    option_flow: '低波动',
    exit: {"stop": -10, "rsi_sell": 75, "ma_violation": "SMA20", "status": "持有"}
  },

  mu: {
    ticker: 'MU', name: 'Micron', sector: '科技', industry: '半导体',
    cap: 'Large', price: 0, change: 0,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.8,
    position: 'light',
    description: 'HBM3E高增长+存储周期上行',
    risk: '今日-2.2%',
    earnings_date: '2026-06-25',
    earnings_beat: '预计超预期',
    hedge_fund_buys: ["Bridgewater"],
    option_flow: 'Put/Call均衡',
    exit: {"stop": -20, "rsi_sell": 78, "ma_violation": "SMA20", "status": "持有"}
  },

  amd: {
    ticker: 'AMD', name: 'AMD', sector: '科技', industry: '半导体',
    cap: 'Large', price: 0, change: 0,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.8,
    position: 'light',
    description: 'MI300追赶NVDA',
    risk: '与NVDA差距拉大',
    earnings_date: '2026-07-29',
    earnings_beat: 'Q1符合预期',
    hedge_fund_buys: ["Citadel"],
    option_flow: '温和看涨',
    exit: {"stop": -15, "rsi_sell": 82, "ma_violation": "SMA20", "status": "持有"}
  },

  ko: {
    ticker: 'KO', name: 'Coca-Cola', sector: '消费防御', industry: '饮料',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 5, heat: 6, catalyst: 3, comp: 3.8,
    position: 'light',
    description: '全球品牌+股息王者+股息2.6%',
    risk: '增长慢',
    earnings_date: '2026-07-22',
    earnings_beat: 'Q1超预期+3%',
    hedge_fund_buys: ["Berkshire"],
    option_flow: '低波动',
    exit: {"stop": -10, "rsi_sell": 75, "ma_violation": "SMA20", "status": "持有"}
  },

  xom: {
    ticker: 'XOM', name: 'ExxonMobil', sector: '能源', industry: '油气',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 4, heat: 6, catalyst: 4, comp: 3.7,
    position: 'light',
    description: '油价高位+回购强劲+股息2.7%',
    risk: '油价波动',
    earnings_date: '2026-08-01',
    earnings_beat: 'Q1超预期+12%',
    hedge_fund_buys: ["Berkshire"],
    option_flow: '温和看涨',
    exit: {"stop": -20, "rsi_sell": 78, "ma_violation": "SMA20", "status": "持有"}
  },

  gs: {
    ticker: 'GS', name: 'Goldman Sachs', sector: '金融', industry: '投行',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 4, heat: 5, catalyst: 4, comp: 3.6,
    position: 'light',
    description: '投行复苏+AI布局',
    risk: '波动大',
    earnings_date: '2026-07-15',
    earnings_beat: 'Q1超预期+10%',
    hedge_fund_buys: ["Citadel"],
    option_flow: '温和',
    exit: {"stop": -15, "rsi_sell": 80, "ma_violation": "SMA20", "status": "持有"}
  },

  cvx: {
    ticker: 'CVX', name: 'Chevron', sector: '能源', industry: '油气',
    cap: 'Mega', price: 0, change: 0,
    tech: 4, fund: 4, heat: 5, catalyst: 3, comp: 3.5,
    position: 'light',
    description: '能源整合+股东回报+股息3.8%',
    risk: '油价波动',
    earnings_date: '2026-08-01',
    earnings_beat: 'Q1超预期+7%',
    hedge_fund_buys: ["Berkshire"],
    option_flow: '温和',
    exit: {"stop": -20, "rsi_sell": 78, "ma_violation": "SMA20", "status": "持有"}
  },

  jpm: {
    ticker: 'JPM', name: 'JPMorgan Chase', sector: '金融', industry: '银行',
    cap: 'Mega', price: 0, change: 0,
    tech: 3, fund: 5, heat: 6, catalyst: 3, comp: 3.3,
    position: 'light',
    description: '全能银行+AI应用',
    risk: '短期均线走弱',
    earnings_date: '2026-07-14',
    earnings_beat: 'Q1超预期+8%',
    hedge_fund_buys: ["Berkshire", "Renaissance"],
    option_flow: '温和',
    exit: {"stop": -15, "rsi_sell": 78, "ma_violation": "SMA20", "status": "持有"}
  },

// ---- AI超级周期 新增标的 ----
  be: {
    ticker: 'BE', name: 'Bloom Energy', sector: '科技', industry: '电力/燃料电池',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 4, heat: 8, catalyst: 5, comp: 4.3,
    position: 'watch',
    description: 'AI电力层瓶颈+Oracle 2.8GW大单+扭亏为盈',
    risk: '1年涨1292%/PB 85极高/今日-9%回调',
    earnings_date: '',
    earnings_beat: '',
    hedge_fund_buys: [],
    option_flow: '回调关注',
    exit: {"stop": -25, "rsi_sell": 82, "ma_violation": "SMA50", "status": "持有"}
  },

  vrt: {
    ticker: 'VRT', name: 'Vertiv', sector: '科技', industry: '液冷散热',
    cap: 'Large', price: 0, change: 0,
    tech: 5, fund: 5, heat: 8, catalyst: 5, comp: 4.5,
    position: 'watch',
    description: '液冷龙头+AI 1kW+/chip散热刚需+刚入S&P 500',
    risk: 'PE 93较高/Forward PE 43/1年涨252%',
    earnings_date: '',
    earnings_beat: '',
    hedge_fund_buys: [],
    option_flow: '回调至SMA50关注',
    exit: {"stop": -20, "rsi_sell": 82, "ma_violation": "SMA50", "status": "持有"}
  },
};

const SECTOR_PERFORMANCE = [
  { name: '科技', week: '+4.59%', month: '+14.90%', quarter: '+22.77%', ytd: '+19.63%', change: '+1.79%', rank: 1 },
  { name: '通信服务', week: '-0.06%', month: '+6.00%', quarter: '+12.76%', ytd: '+9.03%', change: '-0.14%', rank: 2 },
  { name: '消费防御', week: '+1.62%', month: '+4.96%', quarter: '-3.49%', ytd: '+11.09%', change: '+0.67%', rank: 3 },
  { name: '能源', week: '+2.98%', month: '+3.27%', quarter: '+11.69%', ytd: '+31.29%', change: '+0.72%', rank: 4 },
  { name: '工业', week: '+0.61%', month: '+2.25%', quarter: '+2.19%', ytd: '+15.06%', change: '+0.72%', rank: 5 },
  { name: '金融', week: '-0.32%', month: '-1.15%', quarter: '-1.15%', ytd: '-3.21%', change: '+0.51%', rank: 9 },
  { name: '医疗', week: '+1.03%', month: '-1.35%', quarter: '-4.85%', ytd: '-3.67%', change: '-0.13%', rank: 10 },
];

// ---- 经济日历 ----

const ECONOMIC_CALENDAR = [
  { date: '2026-05-15', event: '密歇根消费者信心指数', impact: '中' },
  { date: '2026-05-20', event: 'FOMC会议纪要', impact: '高' },
  { date: '2026-05-21', event: 'WMT财报', impact: '中' },
  { date: '2026-05-28', event: 'NVDA财报', impact: '高' },
  { date: '2026-05-29', event: 'MRVL/COST财报', impact: '中' },
  { date: '2026-06-04', event: 'AVGO财报', impact: '高' },
  { date: '2026-06-10', event: 'CPI通胀数据 / ORCL财报', impact: '高' },
  { date: '2026-06-11', event: 'PPI生产者物价', impact: '中' },
  { date: '2026-06-17', event: 'FOMC利率决议', impact: '极高' },
  { date: '2026-06-25', event: 'MU财报', impact: '中' },
  { date: '2026-07-14', event: 'JPM财报', impact: '中' },
  { date: '2026-07-22', event: 'MSFT/KO财报', impact: '高' },
  { date: '2026-07-29', event: 'META/AMD财报', impact: '高' },
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

function exitColor(status) {
  const colors = {
    '持有': '#3fb950',
    '超买预警': '#f97316',
    '财报窗口期': '#bc8cff',
    '考虑减仓': '#d29922',
    '考虑离场': '#f85149'
  };
  return colors[status] || '#8b949e';
}

function exitIcon(status) {
  const icons = {
    '持有': '✅',
    '超买预警': '⚠️',
    '财报窗口期': '📅',
    '考虑减仓': '📉',
    '考虑离场': '🚨'
  };
  return icons[status] || '❓';
}

function daysUntil(dateStr) {
  if (!dateStr) return -1;
  const today = new Date();
  const target = new Date(dateStr);
  const diff = Math.ceil((target - today) / (1000 * 60 * 60 * 24));
  return diff;
}

// ========================================
// ARK每日交易数据
// 来源: /var/minis/shared/ark-trades/
// 自动读取最新交易日报中的结构化数据
// ========================================

const ARK_DATA = {
  // 每日交易摘要 (YYYY-MM-DD -> 交易列表)
  // 由工具自动更新，前端展示
  lastUpdated: '2026-05-16 16:18',
  
  // 最近5天交易汇总
  recentDays: [
    {
      date: '2026-05-15',
      buys: [
        {fund: 'ARKK', ticker: 'NTRA', amount: '$1.4M', price: '$186', shares: '7,526', pct: '1.69%'},
      ],
      sells: [
        {fund: 'ARKK', ticker: 'TER', amount: '$12.6M', price: '$338', shares: '37,278', pct: '5.76%'},
        {fund: 'ARKK', ticker: 'TSM', amount: '$18.5M', price: '$404', shares: '45,792', pct: '10.85%'},
        {fund: 'ARKK', ticker: 'TWST', amount: '$816.3K', price: '$49', shares: '16,659', pct: '0.26%'},
        {fund: 'ARKW', ticker: 'AMD', amount: '$5.8M', price: '$424', shares: '13,679', pct: '2.75%'},
        {fund: 'ARKW', ticker: 'TSM', amount: '$5.8M', price: '$404', shares: '14,356', pct: '9.88%'},
        {fund: 'ARKG', ticker: 'TWST', amount: '$59.4K', price: '$49', shares: '1,212', pct: '0.06%'},
        {fund: 'ARKG', ticker: 'CDNA', amount: '$132.2K', price: '$20', shares: '6,610', pct: '0.36%'},
      ]
    },
    {
      date: '2026-05-14',
      sells: [
        {fund: 'ARKK', ticker: 'TWST', amount: '$564.1K', price: '$49', shares: '11,512', pct: '0.28%'},
        {fund: 'ARKK', ticker: 'TSM', amount: '$11.6M', price: '$404', shares: '28,712', pct: '10.22%'},
        {fund: 'ARKK', ticker: 'TER', amount: '$8.1M', price: '$338', shares: '23,964', pct: '5.56%'},
        {fund: 'ARKW', ticker: 'TSM', amount: '$4.9M', price: '$404', shares: '12,128', pct: '9.15%'},
        {fund: 'ARKW', ticker: 'AMD', amount: '$5.1M', price: '$424', shares: '12,028', pct: '2.71%'},
        {fund: 'ARKG', ticker: 'TWST', amount: '$67.2K', price: '$49', shares: '1,371', pct: '0.07%'},
        {fund: 'ARKG', ticker: 'ADPT', amount: '$465.0K', price: '$13', shares: '35,769', pct: '1.79%'},
        {fund: 'ARKG', ticker: 'CDNA', amount: '$282.6K', price: '$20', shares: '14,130', pct: '0.75%'},
      ]
    },
    {
      date: '2026-05-13',
      buys: [
        {fund: 'ARKK', ticker: 'NTRA', amount: '$1.4M', price: '$186', shares: '7,526', pct: '1.69%'},
        {fund: 'ARKG', ticker: 'NTRA', amount: '$2.1M', price: '$186', shares: '11,290', pct: '4.44%'},
      ],
      sells: [
        {fund: 'ARKK', ticker: 'TWST', amount: '$236.4K', price: '$49', shares: '4,824', pct: '0.14%'},
        {fund: 'ARKG', ticker: 'ADPT', amount: '$166.9K', price: '$13', shares: '12,838', pct: '0.63%'},
        {fund: 'ARKG', ticker: 'TWST', amount: '$568.4K', price: '$49', shares: '11,600', pct: '0.58%'},
        {fund: 'ARKG', ticker: 'CDNA', amount: '$353.9K', price: '$20', shares: '17,695', pct: '0.90%'},
      ]
    },
    {
      date: '2026-05-12',
      buys: [
        {fund: 'ARKK', ticker: 'NTLA', amount: '$590.4K', price: '$14', shares: '42,171', pct: '0.38%'},
        {fund: 'ARKK', ticker: 'NTRA', amount: '$690.9K', price: '$186', shares: '3,714', pct: '0.89%'},
      ],
      sells: [
        {fund: 'ARKK', ticker: 'TWST', amount: '$2.9M', price: '$49', shares: '59,183', pct: '1.61%'},
      ]
    },
  ]
};