# Quick Test Checklist - 5 Minutes

## 🚀 Quick Smoke Test (Essential Tests)

### 1. Upload & Setup (1 minute)
- [ ] Upload `web3-glossary-translator.skill` to Coze
- [ ] Add Google Search or Bing Search plugin
- [ ] Verify skill appears in skill library

### 2. Basic Functionality (2 minutes)

**Test 1: Classic Term**
```
Input: "What is HODL?"
```
Check:
- [ ] Shows all 7 dimensions
- [ ] Plain language definition is clear
- [ ] Meme origin is present
- [ ] Sentiment shows 🟢 Bullish
- [ ] Risk level shows ⚠️⚠️
- [ ] Veteran advice is actionable

**Test 2: Web Search**
```
Input: "What is $SLOP?"
```
Check:
- [ ] Triggers web search (or says "too new")
- [ ] Shows timestamp if found
- [ ] Risk level higher than normal

**Test 3: Comparison**
```
Input: "What is the difference between Diamond Hands and Paper Hands?"
```
Check:
- [ ] Explains both terms
- [ ] Contrasts them clearly

### 3. Persona Check (1 minute)

**Test 4: Humor Style**
```
Input: "Explain FOMO"
```
Check:
- [ ] Uses jokes or witty language
- [ ] Blunt but helpful tone
- [ ] Sounds like experienced trader

**Test 5: Risk Warning**
```
Input: "What is Rug Pull?"
```
Check:
- [ ] Shows ⚠️⚠️⚠️⚠️⚠️ High Risk
- [ ] Strong warnings present
- [ ] Specific advice to avoid scams

### 4. Edge Cases (1 minute)

**Test 6: Unknown Term**
```
Input: "What is xyz123abc?"
```
Check:
- [ ] Gracefully handles unknown term
- [ ] Doesn't crash or give generic error

**Test 7: Quick Commands**
Test all 5 preset questions:
- [ ] "What is WAGMI?"
- [ ] "Explain why everyone is posting LFG?"
- [ ] "What does Rug Pull mean in meme coin space?"
- [ ] "What is FOMO? I feel like I'm always missing opportunities"
- [ ] "Explain Diamond Hands vs Paper Hands difference"

---

## ✅ Success Criteria

If all tests pass, the skill is ready for production:
- [ ] All 7 dimensions present
- [ ] Web search works
- [ ] Persona is intact
- [ ] Risk warnings are appropriate
- [ ] Edge cases handled gracefully
- [ ] All quick commands work

---

## 🐛 If Tests Fail

### Common Issues & Fixes

**Issue 1: Missing Dimensions**
- Check SKILL.md formatting
- Verify all sections are present
- Check for markdown errors

**Issue 2: Web Search Not Working**
- Verify search plugin is added
- Check plugin is enabled
- Test plugin separately

**Issue 3: Persona Not Showing**
- Check SKILL.md persona section
- Verify examples are present
- Check language style

**Issue 4: Risk Warnings Missing**
- Check Risk Level section in SKILL.md
- Verify ⚠️ symbols are present
- Check formatting

---

## 📊 Test Results Template

```
Test Date: ____________
Tester: ____________

Results:
- Test 1 (HODL): [PASS/FAIL]
- Test 2 (Web Search): [PASS/FAIL]
- Test 3 (Comparison): [PASS/FAIL]
- Test 4 (Persona): [PASS/FAIL]
- Test 5 (Risk Warning): [PASS/FAIL]
- Test 6 (Unknown Term): [PASS/FAIL]
- Test 7 (Quick Commands): [PASS/FAIL]

Total: ___/7 Passed

Issues Found:
1. ________________
2. ________________
3. ________________

Status: [READY/NEEDS FIX]
```

---

## 🎯 After Testing

1. Document any bugs found
2. Fix issues in SKILL.md
3. Repackage skill: `package_skill web3-glossary-translator`
4. Re-upload and test again
5. Repeat until all tests pass

---

## 📝 Notes

- Test with real Coze environment
- Use different users for testing
- Test on different devices/browsers
- Test search functionality thoroughly
- Verify all 15 classic terms work
