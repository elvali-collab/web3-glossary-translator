# Web3 Slang Translator - Test Plan

## Test Environment Setup

### Prerequisites
- Coze account with skill uploaded
- Google Search or Bing Search plugin enabled
- Test environment ready

---

## Test Categories

### 1. Functional Testing

#### 1.1 Basic Term Translation
**Test Cases:**
- [ ] Test classic term: "What is HODL?"
  - Expected: 7-dimensional output with all sections
  - Verify: Plain language definition, meme origin, sentiment, scenario, risk level, veteran advice

- [ ] Test classic term: "Explain FOMO"
  - Expected: Complete translation with Bearish sentiment
  - Verify: Risk level ⚠️⚠️⚠️⚠️⚠️

- [ ] Test classic term: "What does WAGMI mean?"
  - Expected: Bullish sentiment, community belief context

#### 1.2 Web Search Functionality
**Test Cases:**
- [ ] Test new term (not in knowledge base): "What is $SLOP?"
  - Expected: Triggers web search, returns latest meaning
  - Verify: Search timestamp included

- [ ] Test trending term: "Explain $GOAT token"
  - Expected: Real-time search, multiple sources if available
  - Verify: Note about timeliness ("As of [date]")

- [ ] Test very new term: "What is [brand new meme coin]?"
  - Expected: Either finds meaning or honest "too new" response

#### 1.3 7-Dimensional Output Validation
**Test Cases:**
- [ ] Verify all 7 dimensions present for "What is REKT?"
  - ✓ Term Name
  - ✓ Plain Language Definition
  - ✓ Meme Origin Story
  - ✓ Sentiment Analysis
  - ✓ Scenario Simulation
  - ✓ Risk Level (1-5 warnings)
  - ✓ Veteran Advice

#### 1.4 Edge Cases
**Test Cases:**
- [ ] Test non-crypto term: "What is blockchain?"
  - Expected: Basic explanation or redirect to crypto context

- [ ] Test typo: "What is HODLING?"
  - Expected: Recognizes as HODL variant

- [ ] Test multiple terms: "Explain Diamond Hands vs Paper Hands"
  - Expected: Compares both terms

- [ ] Test empty input: ""
  - Expected: Prompt for term or show examples

- [ ] Test very long query: Long paragraph asking about term
  - Expected: Extracts main term and translates

---

### 2. Persona Testing

#### 2.1 Veteran Leek Persona
**Test Cases:**
- [ ] Verify humor style: Check if explanations are witty/blunt
- [ ] Verify professionalism: Humor doesn't compromise accuracy
- [ ] Verify tone: Sharp but well-intentioned
- [ ] Check examples:
  - Does it use jokes to explain concepts?
  - Does it sound like experienced crypto trader?
  - Is it condescending but helpful?

---

### 3. Risk Assessment Testing

#### 3.1 Risk Level Accuracy
**Test Cases:**
- [ ] Low risk terms (Gas Fee): Should be ⚠️
- [ ] Medium risk terms (HODL): Should be ⚠️⚠️
- [ ] High risk terms (Rug Pull): Should be ⚠️⚠️⚠️⚠️⚠️
- [ ] Verify risk explanations are objective

#### 3.2 Safety Warnings
**Test Cases:**
- [ ] Does high-risk term include strong warnings?
- [ ] Are warnings specific, not generic?
- [ ] Does it mention potential losses?

---

### 4. Scenario Simulation Testing

#### 4.1 Real-World Context
**Test Cases:**
- [ ] Verify X/Twitter format is realistic
- [ ] Verify Discord format is realistic
- [ ] Check if usernames are believable
- [ ] Check if dialogue sounds authentic

---

### 5. Error Handling Testing

#### 5.1 Search Failures
**Test Cases:**
- [ ] Simulate search plugin failure
- [ ] Test with no internet connection
- [ ] Test with rate limiting
- [ ] Expected: Graceful error message

#### 5.2 Invalid Inputs
**Test Cases:**
- [ ] Test with special characters: "What is @#$%?"
- [ ] Test with very long strings
- [ ] Test with code snippets
- [ ] Test with non-English input

---

### 6. Performance Testing

#### 6.1 Response Time
**Test Cases:**
- [ ] Classic term response time < 5 seconds
- [ ] Search-enabled term response time < 15 seconds
- [ ] Multiple queries in succession

#### 6.2 Resource Usage
**Test Cases:**
- [ ] Memory usage within limits
- [ ] No memory leaks
- [ ] Concurrent request handling

---

### 7. Integration Testing

#### 7.1 Plugin Integration
**Test Cases:**
- [ ] Google Search plugin working correctly
- [ ] Bing Search plugin working correctly
- [ ] Search results properly formatted

#### 7.2 Coze Platform Integration
**Test Cases:**
- [ ] Skill appears in skill library
- [ ] Start Messages configured correctly
- [ ] Quick commands working

---

### 8. User Experience Testing

#### 8.1 Newcomer-Friendly
**Test Cases:**
- [ ] Web2 user understands the explanation
- [ ] No crypto knowledge assumed
- [ ] Jargon-free plain language definitions
- [ ] Clear action items in advice

#### 8.2 Quick Commands
**Test Cases:**
- [ ] "What is WAGMI?" - Works correctly
- [ ] "Explain why everyone is posting LFG?" - Works correctly
- [ ] "What does Rug Pull mean in meme coin space?" - Works correctly
- [ ] "What is FOMO? I feel like I'm always missing opportunities" - Works correctly
- [ ] "Explain Diamond Hands vs Paper Hands difference" - Works correctly

---

### 9. Content Quality Testing

#### 9.1 Accuracy
**Test Cases:**
- [ ] Term definitions are factually correct
- [ ] Origin stories are accurate
- [ ] Sentiment analysis is reasonable
- [ ] Risk assessments are appropriate

#### 9.2 Completeness
**Test Cases:**
- [ ] All 7 dimensions present for every term
- [ ] No missing sections
- [ ] No placeholder text
- [ ] No incomplete sentences

#### 9.3 Consistency
**Test Cases:**
- [ ] Consistent formatting across all terms
- [ ] Consistent tone throughout
- [ ] Consistent risk level standards

---

### 10. Security Testing

#### 10.1 Input Validation
**Test Cases:**
- [ ] No SQL injection possible
- [ ] No XSS attacks possible
- [ ] No command injection possible

#### 10.2 Data Privacy
**Test Cases:**
- [ ] No sensitive data exposed
- [ ] No user data logged
- [ ] No API keys hardcoded

---

## Regression Testing Checklist

After any changes, verify:
- [ ] All classic terms still work (15 examples)
- [ ] Web search still triggers correctly
- [ ] 7-dimensional output still complete
- [ ] Persona still intact
- [ ] Risk levels still accurate
- [ ] No new bugs introduced

---

## Test Automation

### Automated Test Script (Python)

```python
import requests
import json

def test_skill(term):
    """Test the skill with a given term"""
    # Replace with actual Coze API endpoint
    url = "YOUR_COZE_BOT_ENDPOINT"
    payload = {
        "query": f"What is {term}?",
        "user_id": "test_user"
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    
    # Validate 7 dimensions
    required_sections = [
        "Term Name",
        "Plain Language Definition",
        "Meme Origin Story",
        "Sentiment Analysis",
        "Scenario Simulation",
        "Risk Level",
        "Veteran Advice"
    ]
    
    missing_sections = []
    for section in required_sections:
        if section not in result.get("response", ""):
            missing_sections.append(section)
    
    return {
        "term": term,
        "success": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "response": result
    }

# Test classic terms
classic_terms = ["HODL", "FOMO", "FUD", "WAGMI", "REKT"]
results = [test_skill(term) for term in classic_terms]

# Print results
for result in results:
    print(f"Term: {result['term']}")
    print(f"Success: {result['success']}")
    if not result['success']:
        print(f"Missing: {result['missing_sections']}")
    print("-" * 50)
```

---

## Manual Testing Checklist

### Quick Smoke Test (5 minutes)

1. [ ] Upload skill to Coze
2. [ ] Add search plugin
3. [ ] Test "What is HODL?" - Verify 7 dimensions
4. [ ] Test "What is $SLOP?" - Verify web search
5. [ ] Check persona style - Is it humorous and blunt?
6. [ ] Verify risk warnings are present

---

## Bug Reporting Template

```markdown
## Bug Report

**Test Case ID:** [ID from test plan]

**Description:**
[Clear description of the bug]

**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Result:**
[What should happen]

**Actual Result:**
[What actually happened]

**Environment:**
- Coze version: [version]
- Plugin: [Google Search / Bing Search]
- Input: [exact input used]

**Screenshots:**
[If applicable]

**Severity:** [Critical / High / Medium / Low]
```

---

## Success Criteria

The skill passes testing if:
- ✅ All 15 classic terms work correctly
- ✅ Web search triggers for new terms
- ✅ All 7 dimensions present for every output
- ✅ Persona is consistent and appropriate
- ✅ Risk assessments are accurate
- ✅ No security vulnerabilities
- ✅ Performance within acceptable limits
- ✅ User experience is smooth

---

## Next Steps After Testing

1. Document all bugs found
2. Prioritize bugs by severity
3. Fix critical bugs first
4. Re-test after fixes
5. Prepare for production deployment
