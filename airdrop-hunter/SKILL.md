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

---

## Phase 1: Functionality Testing Guide

Before deploying to production, verify each plugin works correctly.

### Test 1: Search Capability

**Command:**
```
Search for latest airdrop tasks about Linea or Scroll in the past 24 hours.
```

**What to Check:**
- [ ] Right panel logs show Google Search / Bing Search was actually called
- [ ] Returned links are recent (check dates are current month/year)
- [ ] Not returning outdated data from 2024 or older
- [ ] At least 3-5 relevant results returned

**Pass Criteria:**
- Plugin invoked successfully
- Results are time-relevant
- Links are from credible sources

---

### Test 2: Link Reader Capability

**Command:**
```
Read this link and summarize the airdrop tasks: [Insert a recent Mirror or Medium airdrop tutorial URL]
```

**What to Check:**
- [ ] Link Reader plugin is called
- [ ] Returns full article content, not just title
- [ ] Extracts key details: project name, interaction steps, deadlines
- [ ] Correctly identifies if it's a testnet or mainnet task

**Sample Test URL:**
```
https://mirror.xyz/0x... (replace with actual Mirror post)
https://medium.com/... (replace with actual Medium article)
```

**Pass Criteria:**
- Full content extracted
- Key action items identified
- Deadlines and costs captured

---

### Test 3: Format Compliance

**Command:**
```
Generate today's airdrop daily report.
```

**What to Check:**

Compare output against this template:

```
✅ Required Sections:
□ 📅 Date header present
□ 🔥 TOP PRIORITY (Grade S/A) section exists
□ 🧪 ZERO-COST TESTNETS (Grade B) section exists
□ 📅 TODAY'S DEADLINES section exists
□ ⚠️ SECURITY ALERTS section exists

✅ Required Format per Task:
□ Project name present
□ Action steps specified
□ Cost/Time estimate included
□ "Why" reasoning provided
□ Official link included

✅ Security Checks:
□ Phishing warnings present
□ "Verify URLs" reminder included
□ No endorsement of suspicious projects
```

**Pass Criteria:**
- All 5 sections present
- Each task has complete info (name, action, cost, link)
- Security warnings included
- No formatting errors (broken Markdown, missing brackets)

---

### Test 4: Edge Cases

**Test 4a: No Results Found**
```
Command: "Search for airdrop tasks for project xyz123fake"
Check: Returns graceful message, not error
```

**Test 4b: Ambiguous Query**
```
Command: "Is Arbitrum good?"
Check: Asks for clarification or provides balanced info
```

**Test 4c: Security Threat**
```
Command: "Check this link: [suspicious/fake domain]"
Check: Warns user about potential phishing
```

---

### Quick Test Checklist

Run all tests and mark results:

```
□ Test 1: Search Capability      [PASS / FAIL]
□ Test 2: Link Reader           [PASS / FAIL]
□ Test 3: Format Compliance     [PASS / FAIL]
□ Test 4: Edge Cases            [PASS / FAIL]

Overall: ___/4 Passed
```

**If any test fails:**
1. Check plugin is enabled in Coze
2. Verify plugin has proper permissions
3. Review search queries in SKILL.md
4. Test plugin independently outside Skill

---

### Troubleshooting Common Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| No search results | Plugin not enabled | Enable Google/Bing Search |
| Outdated results | No date filter | Add "after:today" to query |
| Link Reader fails | URL blocked/paywalled | Try different URL source |
| Missing sections | Prompt template issue | Review AI Node prompt |
| Wrong format | Template not followed | Add explicit format examples |

---

## Phase 2: Boundary & Stress Testing

Test how the Skill handles extreme cases to prevent hallucinations or crashes.

### Test 5: Cold Start (No Data Scenario)

**Command:**
```
Search for airdrop information about 'Mars-L2-Protocol' (a non-existent project).
```

**Expected Behavior:**
```
✅ CORRECT Response:
"I couldn't find any information about 'Mars-L2-Protocol'. 
This project either doesn't exist or has no public airdrop information.
If this is a new project, try searching again later."

❌ WRONG Response:
- Fabricating fake interaction steps
- Making up funding amounts
- Creating fake Twitter handles
- Hallucinating a website URL
```

**Pass Criteria:**
- Honestly admits no information found
- Does NOT fabricate any details
- Suggests alternative actions (wait, verify project exists)

---

### Test 6: Information Overload (Token Limit)

**Command:**
```
Summarize ALL airdrop tasks across the entire web today.
```

**What to Check:**

| Checkpoint | Expected Behavior |
|------------|-------------------|
| Token overflow | Response completes without cutting off mid-sentence |
| Priority sorting | Only shows TOP 5-10 most important tasks |
| Grading applied | Tasks are graded S/A/B, not random listing |
| Summary format | Brief 1-line per task, not full articles |

**Expected Response Structure:**
```
Due to the large volume of airdrops, here are the TOP 5 priority tasks:

🔥 TOP 5 (Grade S/A)
1. [Most important] - Brief summary
2. [Second most] - Brief summary
...
5. [Fifth] - Brief summary

💡 For full details on specific projects, ask me to "check [project name]"
```

**Pass Criteria:**
- Response completes successfully
- Tasks are prioritized (not random)
- User is guided to ask for specifics

---

### Test 7: Security Verification (Scam Detection)

**Command:**
```
Is this project safe? [Insert URL of known phishing/scam project]
```

**Sample Scam Indicators to Test:**

| Test Case | Expected Warning |
|-----------|------------------|
| Fake domain (e.g., "arbitrum-airdrop.io") | ⚠️ **WARNING: Suspicious domain detected** |
| No official Twitter | ⚠️ **WARNING: No verified social presence** |
| Anonymous team | ⚠️ **WARNING: Anonymous team, high risk** |
| Requires wallet approval | ⚠️ **WARNING: Suspicious contract interaction** |
| Recent rug pull history | ⚠️ **WARNING: Project flagged for previous scams** |

**Expected Response Format:**
```
⚠️ **SECURITY WARNING** ⚠️

🚩 Red Flags Detected:
- Domain similar to popular project but NOT official
- No verified Twitter account found
- Multiple scam reports in community

✅ Official Project:
- Real URL: [official domain]
- Real Twitter: @official_handle

Recommendation: DO NOT INTERACT with this link.
```

**Pass Criteria:**
- Bold ⚠️ warnings present
- Specific red flags identified
- Official project details provided for comparison
- Clear "DO NOT INTERACT" warning

---

### Test 8: Ambiguous Query Handling

**Test 8a: Vague Request**
```
Command: "Is Arbitrum good?"
Expected: Asks clarifying question OR provides balanced overview
```

**Test 8b: Conflicting Info**
```
Command: "Project X says they have airdrop but their Twitter is suspended."
Expected: Highlights the red flag, suggests caution
```

**Test 8c: Time-Sensitive Request**
```
Command: "What airdrops are ending TODAY?"
Expected: Filters by deadline, shows only urgent tasks
```

---

### Quick Boundary Test Checklist

```
□ Test 5: Cold Start (No Data)       [PASS / FAIL]
□ Test 6: Information Overload        [PASS / FAIL]
□ Test 7: Security/Scam Detection     [PASS / FAIL]
□ Test 8: Ambiguous Queries           [PASS / FAIL]

Overall: ___/4 Passed
```

**Critical Failure Indicators:**
- 🚨 Fabricates information when none exists
- 🚨 Response cuts off mid-sentence (token overflow)
- 🚨 Fails to warn about obvious scams
- 🚨 Provides dangerous wallet interaction advice

If any critical failure occurs, DO NOT deploy to production.

---

### Edge Case Response Templates

Use these templates when encountering edge cases:

**Template 1: Project Not Found**
```
I couldn't find reliable information about [project name]. 

Possible reasons:
- Project may not exist or is very new
- May be misspelled
- Could be a private/test project

Suggestions:
- Verify the project name
- Check if they have an official Twitter
- Wait for more public information
```

**Template 2: Suspected Scam**
```
⚠️ **SECURITY ALERT** ⚠️

This project has been flagged for:
- [Specific red flag 1]
- [Specific red flag 2]

Official alternatives:
- [Official project name]: [Official URL]

**DO NOT** interact with suspicious links or approve unknown contracts.
```

**Template 3: Information Overload**
```
Found [X] airdrop opportunities today.

To prevent information overload, here are the **TOP 5 priority tasks**:

1. [Project] - [Grade] - [Brief action]
...

For full details on any specific project, ask: "check [project name]"
```

---

## Phase 3: Automation Workflow Testing

Test the scheduled automation to ensure reliable daily delivery.

### Test 9: Manual Workflow Trigger

**Purpose:** Verify the workflow executes correctly without waiting for scheduled time.

**Steps:**
```
1. Navigate to Workflow editor in Coze
2. Click "Run" or "Test" button (top right corner)
3. Monitor execution in real-time
```

**What to Check:**

| Node | Expected Status | Checkpoint |
|------|-----------------|------------|
| Start Node | 🟢 Green | Triggered successfully |
| Search Node | 🟢 Green | Returned search results |
| AI Node | 🟢 Green | Generated formatted report |
| End Node | 🟢 Green | Delivered output |

**Visual Check:**
```
All nodes should show GREEN checkmarks:

┌─────────────┐
│  Start ✅   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Search ✅   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   AI ✅     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   End ✅    │
└─────────────┘
```

**Pass Criteria:**
- All 4 nodes show green status
- No red/yellow error indicators
- Execution completes in < 30 seconds

---

### Test 10: Variable Passing Verification

**Purpose:** Ensure data flows correctly between nodes.

**Critical Check: Search → AI Node**

**Common Bug:**
```
❌ WRONG: AI node only receives titles
Search returns: [
  "Scroll Airdrop Guide",
  "zkSync Testnet Tutorial"
]

AI generates: Generic/empty report (no details)

---

✅ CORRECT: AI node receives full content
Search returns: [
  {
    "title": "Scroll Airdrop Guide",
    "url": "https://...",
    "snippet": "Bridge 0.01 ETH to Scroll network...",
    "content": "Full article text with steps, costs, deadlines..."
  }
]

AI generates: Detailed report with actionable steps
```

**How to Verify:**
```
1. Click on Search node after execution
2. Check "Output" or "Results" panel
3. Verify full content is present, not just titles
4. Click on AI node
5. Check "Input" panel - should match Search output
6. Check "Output" panel - should have complete report
```

**Debug Checklist:**
```
□ Search node output contains "content" or "body" field
□ AI node input matches Search node output
□ AI node output contains all 5 sections
□ No empty/missing data in final report
```

---

### Test 11: Scheduled Trigger Timing

**Purpose:** Verify automation runs at correct time.

**Steps:**
```
1. Set trigger to a near-future time (e.g., 5 minutes from now)
2. Wait for automated execution
3. Check execution logs
```

**Time Configuration Checklist:**
```
□ Timezone is correct (UTC+8 or your local timezone)
□ Trigger is set to DAILY frequency
□ Time is set correctly (e.g., 10:00 AM)
□ Workflow is ENABLED (not paused)
```

**Common Issues:**

| Issue | Cause | Solution |
|-------|-------|----------|
| Workflow doesn't trigger | Workflow paused | Enable workflow |
| Wrong time execution | Timezone mismatch | Adjust timezone |
| Skipped execution | Rate limiting | Reduce frequency |
| Multiple executions | Duplicate triggers | Check for duplicates |

---

### Test 12: Output Delivery Verification

**Purpose:** Verify report is delivered to the correct destination.

**Test by Destination Type:**

#### Option A: Chat Output
```
Check: Report appears in Coze chat interface
Verify: All sections visible, formatting correct
```

#### Option B: Telegram Webhook
```
Check: Message delivered to Telegram channel
Verify: Markdown renders correctly
Test: Emojis display properly (🔥 🧪 ⚠️)
```

#### Option C: Discord Webhook
```
Check: Embed appears in Discord channel
Verify: Links are clickable
Test: Fields are properly formatted
```

**Telegram Webhook Test:**
```bash
# Manual test command (replace tokens)
curl -X POST "https://api.telegram.org/bot[TOKEN]/sendMessage" \
  -d chat_id="[CHAT_ID]" \
  -d text="📅 Test Report\n\n🔥 Test successful!" \
  -d parse_mode="Markdown"
```

---

### Workflow Debugging Guide

**If Search Node Fails:**
```
1. Check plugin permissions
2. Verify search query syntax
3. Test query manually in Google/Bing
4. Check rate limiting status
```

**If AI Node Produces Empty Report:**
```
1. Check Search node output format
2. Verify variable passing: {search_results} → AI input
3. Check AI prompt template
4. Look for token limit errors in logs
```

**If End Node Fails:**
```
1. Verify webhook URL is correct
2. Check Telegram/Discord bot permissions
3. Test webhook with curl command
4. Check for firewall/network issues
```

---

### Quick Automation Test Checklist

```
□ Test 9: Manual Trigger          [PASS / FAIL]
□ Test 10: Variable Passing       [PASS / FAIL]
□ Test 11: Scheduled Timing       [PASS / FAIL]
□ Test 12: Output Delivery        [PASS / FAIL]

Overall: ___/4 Passed
```

**Critical Checks Before Production:**
```
✅ All 4 nodes execute with green status
✅ Variable passing verified (content not just titles)
✅ Test execution at scheduled time successful
✅ Output delivered to correct destination
```

---

### Full Testing Summary

```
==========================================
AIRDROP HUNTER - COMPLETE TEST RESULTS
==========================================

Phase 1: Functionality Testing (4 tests)
□ Test 1: Search Capability
□ Test 2: Link Reader
□ Test 3: Format Compliance
□ Test 4: Edge Cases
Phase 1 Score: ___/4

Phase 2: Boundary & Stress Testing (4 tests)
□ Test 5: Cold Start (No Data)
□ Test 6: Information Overload
□ Test 7: Security/Scam Detection
□ Test 8: Ambiguous Queries
Phase 2 Score: ___/4

Phase 3: Automation Workflow (4 tests)
□ Test 9: Manual Trigger
□ Test 10: Variable Passing
□ Test 11: Scheduled Timing
□ Test 12: Output Delivery
Phase 3 Score: ___/4

==========================================
TOTAL SCORE: ___/12 PASSED
==========================================

Deployment Recommendation:
✅ 12/12: Ready for production
⚠️ 9-11/12: Minor fixes needed
🚨 <9/12: Critical issues, do not deploy
```

---

## Post-Deployment Monitoring

After deploying to production, monitor:

**Daily Checks:**
- [ ] Workflow executes on time
- [ ] Report quality is consistent
- [ ] No user complaints about missing info
- [ ] No security incidents reported

**Weekly Checks:**
- [ ] Review search query effectiveness
- [ ] Update grading criteria if needed
- [ ] Check for new phishing patterns
- [ ] Gather user feedback

---

## Phase 4: User Simulation Testing

Simulate real user scenarios to verify natural language understanding and filtering logic.

### Test 13: Cost-Based Recommendation

**Command:**
```
I only have 0.01 ETH, which project is suitable for me?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
Based on your 0.01 ETH budget (~$30-40), here are suitable options:

🧪 ZERO-COST TESTNETS (Recommended for your budget)
1. [Project A]: Free testnet interaction
   └─ Faucet: [URL]
   └─ Time: 10 min

2. [Project B]: Free testnet swap
   └─ Faucet: [URL]
   └─ Time: 15 min

💰 LOW-COST MAINNET (Within your budget)
1. [Project C]: Bridge to Layer 2
   └─ Cost: $2-5 gas
   └─ Potential: Grade A project

⚠️ BUDGET TIP:
- Keep 0.005 ETH reserve for future gas fees
- Start with testnets to build transaction history
- Consider spreading across 2-3 projects for diversification
```

**❌ WRONG Responses:**
- Suggesting projects requiring 0.1+ ETH
- No budget consideration at all
- Ignoring user's financial constraints
- No risk management advice

**Evaluation Criteria:**
```
□ Identifies user's budget constraint
□ Recommends projects within budget
□ Suggests zero-cost alternatives
□ Provides budget management tips
□ Prioritizes testnets for low-budget users
```

---

### Test 14: Tag-Based Filtering

**Command:**
```
Give me a zero-cost testnet link.
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
Here's a zero-cost testnet opportunity:

🧪 [Project Name] Testnet
├─ Faucet: https://faucet.example.com
├─ Network: [Testnet Name]
├─ Time Required: ~10 minutes
├─ Steps:
│   1. Claim testnet tokens from faucet
│   2. Connect wallet to [URL]
│   3. Complete swap/bridge task
│   4. Claim OAT/NFT reward
│
└─ Why Recommended:
   - Backed by [VC names]
   - Mainnet launch expected [date]
   - Zero cost, potential future airdrop

📌 Quick Start:
1. Visit faucet link above
2. Follow steps in order
3. No real funds needed
```

**❌ WRONG Responses:**
- Returns mainnet projects requiring gas fees
- No direct faucet/testnet link provided
- Generic response without actionable steps
- Forgets to explain WHY this specific project

**Evaluation Criteria:**
```
□ Direct faucet/testnet link provided
□ Marked as "zero-cost" clearly
□ Step-by-step instructions included
□ Time estimate given
□ Project background explained
□ No mainnet projects suggested (user asked for zero-cost)
```

---

### Test 15: Specific Project Inquiry

**Command:**
```
What do you think about Scroll airdrop?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
📊 Scroll Airdrop Analysis

🔥 Grade: A (High Priority)

💼 Background:
- Funding: $80M (Polychain, Sequoia)
- Stage: Mainnet live (Oct 2023)
- TVL: $1.2B+

🎯 Current Status:
- Points system active
- Multiple campaigns running
- No confirmed airdrop date yet

💡 Recommended Actions:
1. Bridge ETH to Scroll: $3-5 gas
2. Use DEXs (SyncSwap, Uniswap)
3. Mint NFT collections
4. Complete Galxe campaigns

💰 Cost Estimate: $10-30 total
⏰ Time Required: 2-3 hours
📈 Airdrop Probability: High (75%+)

⚠️ Risks:
- No guaranteed airdrop
- Opportunity cost of locked liquidity
- Competition from sybils
```

**❌ WRONG Responses:**
- No grading or evaluation
- Missing action steps
- No cost/time estimates
- Ignores risks
- Fabricates airdrop date

**Evaluation Criteria:**
```
□ Project graded (S/A/B)
□ Funding/background provided
□ Actionable steps listed
□ Cost and time estimated
□ Risks clearly stated
□ No fabricated information
```

---

### Test 16: Multi-Intent Query

**Command:**
```
I want zero-cost testnets but also interested in high-ROI mainnet projects under $10.
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
I'll provide both options for you:

🧪 ZERO-COST TESTNETS (Start Here)
1. [Project A]: [Faucet Link] | 10 min
2. [Project B]: [Faucet Link] | 15 min

💰 MAINNET UNDER $10 (High ROI Potential)
1. [Project C]: Bridge + Swap | $5-8 gas | Grade A
   └─ Why: Confirmed airdrop, low entry cost

2. [Project D]: NFT Mint | $3-5 | Grade B
   └─ Why: Low cost, speculative upside

📊 Strategy Recommendation:
1. Start with testnets (free, build history)
2. Then try 1-2 low-cost mainnet projects
3. Total budget: ~$10-15
4. Diversify across ecosystems

⚠️ Remember: Never spend more than you can afford to lose.
```

**Evaluation Criteria:**
```
□ Both parts of query addressed
□ Zero-cost options provided
□ Mainnet options under $10 provided
□ Logical prioritization given
□ Clear separation of categories
```

---

### Test 17: Conflicting Information

**Command:**
```
Project X's Twitter says airdrop is confirmed, but their Discord says it's not. Which is true?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
⚠️ CONFLICTING INFORMATION DETECTED

🔍 Investigation Results:
- Twitter (@ProjectX): Posted "Airdrop confirmed" [date]
- Discord: Mod said "No airdrop planned" [date]

📊 Analysis:
1. Twitter marketing may be misleading
2. Discord statement is likely more accurate
3. Official docs have no token info

💡 Recommendation:
- WAIT for official announcement
- Check project's blog/docs for tokenomics
- Verify team statements before interacting
- Avoid high-cost interactions until confirmed

🔐 Safety First:
- Don't trust Twitter-only announcements
- Cross-reference with official channels
- When in doubt, ask in Discord with verified role
```

**Evaluation Criteria:**
```
□ Acknowledges conflicting information
□ Investigates both sources
□ Provides neutral analysis
□ Recommends caution
□ Suggests verification steps
□ No biased assumption
```

---

### User Simulation Test Checklist

```
□ Test 13: Cost-Based Recommendation    [PASS / FAIL]
□ Test 14: Tag-Based Filtering          [PASS / FAIL]
□ Test 15: Specific Project Inquiry     [PASS / FAIL]
□ Test 16: Multi-Intent Query           [PASS / FAIL]
□ Test 17: Conflicting Information      [PASS / FAIL]

Phase 4 Score: ___/5
```

---

### User Simulation Best Practices

**When User Asks About Budget:**
1. Always acknowledge their constraint
2. Recommend options WITHIN budget
3. Suggest zero-cost alternatives first
4. Provide budget management tips
5. Never recommend over-budget options

**When User Requests Specific Tags:**
1. Filter results by requested tag (zero-cost, testnet, etc.)
2. Provide direct links immediately
3. Include step-by-step instructions
4. Add time/cost estimates
5. Explain WHY it matches their request

**When User Asks About Specific Project:**
1. Provide comprehensive analysis
2. Include grade, funding, status
3. List actionable steps
4. Mention risks and probability
5. Don't fabricate information

**When User Has Multiple Intents:**
1. Address EACH part of the query
2. Use clear section headers
3. Provide strategy/recommendation
4. Help user prioritize
5. Consider their constraints

---

## Complete Testing Framework Summary

```
===============================================
AIRDROP HUNTER - FULL TEST FRAMEWORK (17 Tests)
===============================================

Phase 1: Functionality Testing (4 tests)
□ Test 1: Search Capability
□ Test 2: Link Reader
□ Test 3: Format Compliance
□ Test 4: Edge Cases
Phase 1 Score: ___/4

Phase 2: Boundary & Stress Testing (4 tests)
□ Test 5: Cold Start (No Data)
□ Test 6: Information Overload
□ Test 7: Security/Scam Detection
□ Test 8: Ambiguous Queries
Phase 2 Score: ___/4

Phase 3: Automation Workflow (4 tests)
□ Test 9: Manual Trigger
□ Test 10: Variable Passing
□ Test 11: Scheduled Timing
□ Test 12: Output Delivery
Phase 3 Score: ___/4

Phase 4: User Simulation (5 tests)
□ Test 13: Cost-Based Recommendation
□ Test 14: Tag-Based Filtering
□ Test 15: Specific Project Inquiry
□ Test 16: Multi-Intent Query
□ Test 17: Conflicting Information
Phase 4 Score: ___/5

===============================================
TOTAL SCORE: ___/17 PASSED
===============================================

Deployment Recommendation:
✅ 17/17: Production ready, excellent quality
✅ 14-16/17: Production ready, minor improvements needed
⚠️ 10-13/17: Testing needed, not recommended for production
🚨 <10/17: Critical issues, requires major fixes
===============================================
```

---

## Quick Reference: Test Commands

```bash
# Phase 1: Functionality
"Search for latest airdrop tasks about Linea or Scroll in the past 24 hours."
"Read this link and summarize the airdrop tasks: [URL]"
"Generate today's airdrop daily report."

# Phase 2: Boundary
"Search for airdrop information about 'Mars-L2-Protocol'."
"Summarize ALL airdrop tasks across the entire web today."
"Is this project safe? [suspicious URL]"

# Phase 3: Automation (Manual workflow test)
# Navigate to Workflow editor → Click "Run"

# Phase 4: User Simulation
"I only have 0.01 ETH, which project is suitable for me?"
"Give me a zero-cost testnet link."
"What do you think about Scroll airdrop?"
"I want zero-cost testnets but also interested in high-ROI mainnet projects under $10."
"Project X's Twitter says airdrop confirmed but Discord says no. Which is true?"
```
