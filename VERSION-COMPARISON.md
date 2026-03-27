# Web3 黑话翻译官 - 版本说明

本项目提供两个版本的 Skill，分别适配不同的 AI 平台。

## 版本对比

### Coze 版本
- **目录**：`web3-glossary-translator/`
- **入口文件**：`SKILL.md`
- **打包文件**：`web3-glossary-translator.skill`
- **特点**：
  - 完整的 YAML 前言区（name、description）
  - 详细的操作步骤和资源索引
  - 包含"快捷指令"章节
  - 已集成联网搜索能力
  - 适用于 Coze 平台

### Claude 版本
- **目录**：`claude-web3-glossary-translator/`
- **入口文件**：`CLAUDE.md`
- **参考文件**：`REFERENCES.md`、`README.md`
- **特点**：
  - 适配 Claude 项目结构
  - README.md 提供快速概览
  - CLAUDE.md 包含完整的人设和翻译框架
  - REFERENCES.md 提供经典术语示例库
  - 适用于 Claude 本地环境

## 核心功能（两个版本相同）

### 翻译框架（7 个维度）
1. **词条名称**：术语的英文原文
2. **大白话定义**：用最接地气的语言解释
3. **圈内梗来源**：追溯起源故事
4. **情绪识别**：Bullish/Bearish/Neutral
5. **场景模拟**：X/Twitter、Discord 真实用法
6. **危险程度**：⚠️⚠️⚠️⚠️⚠️ 风险等级
7. **老手建议**：具体可操作的实战忠告

### 核心人设
- 混迹币圈多年的"老韭菜"
- 幽默毒舌但专业有用
- 直白有用，表面嘲讽实则善意
- 文化洞察，不仅解释字面意思

### 经典术语库（15 个示例）
1. HODL - 信仰持有
2. FOMO - 错失恐惧
3. FUD - 恐慌散布
4. TO THE MOON - 暴涨预期
5. DYOR - 自行研究
6. WAGMI - 我们都会成功
7. REKT - 惨重亏损
8. DIAMOND HANDS - 钻石手
9. PAPER HANDS - 纸手
10. RUG PULL - 撤梯跑路
11. GAS FEE - 矿工费
12. DEGEN - 赌徒
13. APE IN - 无脑冲
14. BAGHOLDER - 接盘侠
15. WHALE - 巨鲸

## 使用建议

### Coze 平台
1. 使用 `web3-glossary-translator.skill` 文件
2. 在 Plugins 部分添加 Google Search 或 Bing Search 插件
3. 在 Variable & Settings 中设置预设问题作为 Start Message
4. 当遇到新术语时，自动触发联网搜索

### Claude 本地环境
1. 将 `claude-web3-glossary-translator/` 目录放置在 Claude 项目中
2. Claude 会自动读取 `CLAUDE.md` 中的指导
3. 参考 `REFERENCES.md` 中的经典术语示例
4. Claude 原生支持联网搜索，无需额外配置

## 更新日志

### v1.0 (2024-03-27)
- 创建初始版本
- 实现 7 维度翻译框架
- 提供 15 个经典术语示例
- 添加联网搜索能力（Coze 版本）
- 添加快捷指令功能（Coze 版本）
- 创建 Claude 适配版本
