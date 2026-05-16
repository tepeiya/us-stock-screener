// ========================================
// 美股选股器 v2.0 - 核心数据模型
// 数据同步自对话版选股器
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
