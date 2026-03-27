---
name: airdrop-hunter
description: Daily Web3 airdrop interaction guide covering Grade S high-value tasks, zero-cost testnets, and trending opportunities aggregation; use when users ask for daily airdrop tasks or zero-cost opportunities
dependency:
  plugin:
    - web_search
    - link_reader
---

# Airdrop Task Daily

**Cut through the noise. Only the most valuable interactions.** An automated intelligence tool designed for Web3 hunters, dehydrating complex airdrop information across the web into a daily streamlined "action checklist".

---

## Prerequisites: Required Plugins

**⚠️ This Skill is blind without plugins.** Configure the following plugins in Coze Plugins page before using:

### Required Plugins

| Plugin | Purpose | Priority |
|--------|---------|----------|
| **Google Search** / **Bing Search** | Search web articles for airdrop news | 🔴 Required |
| **Link Reader** | Read details from long tweets or Medium articles | 🔴 Required |
| **Twitter/X Search** (if available) | Direct access to X for real-time alpha | 🟡 Optional |

### Why These Plugins Matter

1. **Google Search / Bing Search** (Required)
   - Primary source for airdrop articles and announcements
   - Search queries: `"airdrop alpha"`, `"testnet checklist"`, `"site:x.com airdrop"`
   - Without this: Cannot fetch any external airdrop information

2. **Link Reader** (Required)
   - When search finds a long tweet thread or Medium article
   - Extracts key details: funding amounts, deadlines, interaction steps
   - Without this: Cannot deep-dive into articles for actionable info

3. **Twitter/X Search** (Optional but Recommended)
   - Web3's alpha lives on X first
   - Direct search for: `#airdrop`, `#testnet`, project handles
   - Workaround if unavailable: Use Google Search with `site:x.com` prefix

### Plugin Configuration Checklist
```
□ Google Search OR Bing Search enabled
□ Link Reader enabled
□ (Optional) Twitter/X Search enabled if available
□ Test: Search "airdrop alpha today" to verify
```

---

## Advanced: Scheduled Automation (Daily Push)

To make this a true "daily report", configure Coze Workflow for automated daily delivery:

### Workflow Setup: Daily_Airdrop_Push

**Create a new workflow with the following nodes:**

```
┌─────────────────┐
│  Start Node     │ → Scheduled Trigger: Every day at 10:00 AM
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Search Node    │ → Auto-search daily keywords
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Node        │ → Aggregate into daily report format
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  End Node       │ → Output to chat or Telegram via Webhook
└─────────────────┘
```

### Node Configuration Details

#### 1. Start Node: Scheduled Trigger
```
Trigger Type: Scheduled
Schedule: Daily
Time: 10:00 AM (configurable to your timezone)
Timezone: UTC+8 (adjust as needed)
```

#### 2. Search Node: Multi-Query Search
```
Plugin: Google Search / Bing Search

Queries to execute:
1. "airdrop alpha" [current_date] crypto
2. "testnet checklist" latest
3. "galxe campaign" active OR live
4. site:x.com "airdrop" after:24h

Output: List of URLs and snippets
```

#### 3. AI Node: Report Generation
```
Prompt Template:
"You are the Airdrop Hunter agent. Based on the search results below, generate a daily airdrop report following this format:

📅 [DATE] Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
[Project]: [Action] | [Cost] | [Deadline]

🧪 ZERO-COST TESTNETS (Grade B)
[Project]: [Faucet] | [Time]

📅 TODAY'S DEADLINES
[Deadlines list]

⚠️ SECURITY ALERTS
[Warnings]

Search Results:
{search_results}"

Output: Formatted daily report
```

#### 4. End Node: Delivery Options
```
Option A: Direct Chat Output
- Output the report directly to the Coze chat interface
- Users can view in the conversation history

Option B: Telegram Push (via Webhook)
- Configure Telegram Bot API
- Webhook URL: https://api.telegram.org/bot[TOKEN]/sendMessage
- Payload:
  {
    "chat_id": "[CHANNEL_ID]",
    "text": "{daily_report}",
    "parse_mode": "Markdown"
  }

Option C: Discord Webhook
- Webhook URL: [Your Discord channel webhook]
- Format: Embed with fields for each section
```

### Workflow Test Checklist
```
□ Start node triggers at scheduled time
□ Search node returns relevant results
□ AI node generates properly formatted report
□ End node delivers to chosen destination
□ Verify report content quality
□ Check timezone is correct
```

### Alternative: Manual Trigger
If scheduled automation is not available, users can manually trigger:
```
User types: "daily report"
Skill executes: Full search → Generate report → Display
```

---

## Core Features

### 1. Network-Wide Scanning
Automatically track earliest airdrop signals from:
- **X (Twitter)**: KOLs, official project accounts, alpha groups
- **Mirror.xyz**: Project blogs and announcements
- **Galxe**: Campaign quests and OATs
- **Research Channels**: RootData, DefiLlama, Messari

### 2. Project Grading System
Dynamic scoring based on:
| Grade | Criteria | Action Priority |
|-------|----------|-----------------|
| **S** | Tier-1 VC backing (a16z, Paradigm), $50M+ funding, mainnet live with points system | MUST DO |
| **A** | Reputable VCs, $10M+ funding, confirmed token or imminent TGE | HIGH |
| **B** | Testnet stage, early potential, zero-cost interaction | SPECULATIVE |

See [references/evaluation-criteria.md](references/evaluation-criteria.md) for detailed grading criteria.

### 3. Minimalist Output
Cut all the fluff. Direct delivery of:
```
[Project] + [Action] + [Cost/Faucet Link]
```

### 4. Security Scanning
Auto-check interaction site safety:
- Verify official domains via Twitter bio
- Flag suspicious similar domains (e.g., "scroll-airdrop.io" vs "scroll.io")
- Contract verification on Etherscan/Arbiscan

---

## Daily Report Template

```
📅 [DATE] Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
1. [Project Name]: [Action] | [Est. Cost] | [Deadline]
   └─ Why: [1-line reasoning]
   └─ Link: [official URL]

🧪 ZERO-COST TESTNETS (Grade B)
1. [Project Name]: [Faucet] | [Time Required]
   └─ Chain: [testnet name]

📅 TODAY'S DEADLINES
- [Project]: [Task] ends in [X hours]
- [Galxe Campaign]: Ends [date]

⚠️ SECURITY ALERTS
- Verify all URLs through official Twitter accounts
- Never share private keys or seed phrases
- [Current phishing warning if applicable]
```

---

## Operational Workflow

### Step 1: Multi-Source Search

**Search Strategy by Source:**

#### 1.1 Web Articles (Google Search / Bing Search)
```
Primary Queries:
- "airdrop alpha" [current month] [current year]
- "testnet checklist" crypto latest
- "galxe campaign" active
- "layer3 quest" current

Date-Restricted Queries (past 24-48 hours):
- "airdrop" after:today
- "testnet faucet" after:yesterday
```

#### 1.2 Twitter/X Search
```
If Twitter/X Search plugin is available:
- #airdrop #alpha
- #testnet #faucet
- from:[KOL_handle] airdrop

Workaround using Google Search:
- site:x.com "airdrop alpha"
- site:x.com "testnet checklist"
- site:x.com from:[handle] airdrop
```

#### 1.3 Deep-Dive Reading (Link Reader)
When search returns:
- Long tweet threads (>5 tweets) → Use Link Reader to extract key points
- Medium articles → Use Link Reader to get full content
- Mirror.xyz posts → Use Link Reader for complete text
- Project documentation → Use Link Reader for interaction guides

**Example Link Reader Usage:**
```
Search finds: "https://mirror.xyz/0x.../airdrop-guide"
Action: Call Link Reader to extract:
  - Funding amount
  - Interaction steps
  - Deadline
  - Cost estimate
```

### Step 2: Filter & Grade
For each opportunity found:
1. Check funding status (RootData, Crunchbase)
2. Verify community traction (Twitter followers, Discord activity)
3. Determine grade (S/A/B)
4. Estimate cost and time requirement

### Step 3: Security Verification
- Cross-check URLs with official Twitter bio
- Verify contract addresses on block explorer
- Search for scam reports in Twitter replies

### Step 4: Generate Report
Format output using the template above, sorted by priority.

---

## Search Query Templates

### Daily Scanning Queries
```bash
# High-value airdrops (S/A grade)
"airdrop alpha" [current_month] funded OR backed OR raised

# Testnet opportunities (B grade)
"testnet faucet" [current_month] free OR zero

# Campaigns and quests
"galxe campaign" active OR live
"layer3 quest" crypto

# Twitter alpha (if using Google Search workaround)
site:x.com "airdrop" "testnet" after:24h
site:x.com from:airdropalert
```

### Project-Specific Queries
```bash
# Check if project has airdrop confirmed
"[project_name]" airdrop token confirmed

# Check funding background
"[project_name]" funding raised series

# Check scam reports
"[project_name]" scam OR rug OR phishing
```

---

## How to Use

### Quick Commands
In Coze/Claw interface, simply type:

| Command | Action |
|---------|--------|
| `daily report` | Get latest 24-hour airdrop checklist |
| `any zero-cost?` | Filter for free testnet opportunities |
| `check [project]` | Get specific project airdrop status |
| `S-grade tasks` | Show only Grade S high-priority tasks |

### Usage Examples

**User**: `daily report`

**Agent Response**:
```
📅 March 27, 2026 Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
1. Scroll: Bridge 0.01 ETH to Scroll network | $2-5 gas | No deadline
   └─ Why: Polychain backed ($80M), mainnet live, points active
   └─ Link: https://scroll.io/bridge

2. zkSync Era: Mint NFT + Swap | $1-3 | Ongoing
   └─ Why: a16z backed ($458M), confirmed token
   └─ Link: https://era.zksync.io

🧪 ZERO-COST TESTNETS (Grade B)
1. Linea: Claim testnet ETH → Swap tokens | Free | 10 min
   └─ Faucet: https://faucet.goerli.linea.build
   └─ Why: ConsenSys backed, mainnet imminent

📅 TODAY'S DEADLINES
- zkSync Galxe Campaign: Ends in 6 hours
- Scroll OAT Claim: Ends March 28

⚠️ SECURITY ALERTS
- Phishing alert: "scrolls-airdrop.io" is NOT official
- Always verify: scroll.io (check Twitter @Scroll_ZKP)
```

---

## Resource Index

- **Grading Criteria**: [references/evaluation-criteria.md](references/evaluation-criteria.md)
- **Trusted Sources**: [references/trusted-sources.md](references/trusted-sources.md)

---

## Important Notes

### Before Listing Any Project
- [ ] Funding confirmed via RootData or Crunchbase
- [ ] Official Twitter exists and is active
- [ ] Website has valid SSL certificate
- [ ] Contract verified on block explorer
- [ ] No scam reports in community

### Red Flags (Never List)
- Anonymous team with no track record
- Domain similar to popular project
- Requires sending ETH to unknown address
- No official Twitter or website
- Urgent "act now" pressure tactics

### Disclaimer
This Skill provides information only, not financial advice. Always:
- Do your own research (DYOR)
- Never invest more than you can afford to lose
- Verify all information before interacting
- Use separate wallets for airdrop hunting

---

## Changelog

### v1.0.0
- Initial release
- Multi-source search capability
- S/A/B grading system
- Daily report template
- Security verification checks
