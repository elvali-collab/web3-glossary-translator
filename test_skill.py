#!/usr/bin/env python3
"""
Web3 Slang Translator - Quick Test Script

This script performs automated testing of the skill.
Run this after uploading the skill to Coze.
"""

import json
import time
from typing import List, Dict, Any

class SkillTester:
    """Test runner for Web3 Slang Translator Skill"""
    
    def __init__(self):
        self.test_results = []
        self.passed = 0
        self.failed = 0
    
    def test_dimensional_output(self, term: str, expected_sentiment: str = None):
        """
        Test if output contains all 7 required dimensions
        
        Args:
            term: The crypto term to test
            expected_sentiment: Expected sentiment (Bullish/Bearish/Neutral)
        """
        required_dimensions = [
            "Term Name",
            "Plain Language Definition",
            "Meme Origin Story",
            "Sentiment Analysis",
            "Scenario Simulation",
            "Risk Level",
            "Veteran Advice"
        ]
        
        print(f"\n{'='*60}")
        print(f"Testing: {term}")
        print(f"{'='*60}")
        
        # Note: Replace this with actual Coze API call
        # For now, this is a template
        response = self.mock_skill_call(term)
        
        # Check all dimensions
        missing_dimensions = []
        for dimension in required_dimensions:
            if dimension not in response:
                missing_dimensions.append(dimension)
        
        # Check sentiment if specified
        sentiment_correct = True
        if expected_sentiment:
            if expected_sentiment not in response.get("Sentiment Analysis", ""):
                sentiment_correct = False
        
        # Determine test result
        test_passed = len(missing_dimensions) == 0 and sentiment_correct
        
        result = {
            "term": term,
            "passed": test_passed,
            "missing_dimensions": missing_dimensions,
            "sentiment_correct": sentiment_correct,
            "response": response
        }
        
        self.test_results.append(result)
        
        if test_passed:
            self.passed += 1
            print(f"✅ PASSED: All dimensions present")
        else:
            self.failed += 1
            print(f"❌ FAILED:")
            if missing_dimensions:
                print(f"   Missing dimensions: {missing_dimensions}")
            if not sentiment_correct:
                print(f"   Expected sentiment: {expected_sentiment}")
    
    def mock_skill_call(self, term: str) -> Dict[str, Any]:
        """
        Mock skill call for testing purposes
        
        In production, replace this with actual Coze API call:
        
        import requests
        response = requests.post(
            "YOUR_COZE_BOT_ENDPOINT",
            json={"query": f"What is {term}?"}
        )
        return response.json()
        """
        
        # Mock responses for classic terms
        mock_responses = {
            "HODL": {
                "Term Name": "HODL (Hold On for Dear Life)",
                "Plain Language Definition": "Holding on for dear life—refusing to sell...",
                "Meme Origin Story": "In December 2013, Bitcoin crashed...",
                "Sentiment Analysis": "🟢 Bullish",
                "Scenario Simulation": "@crypto_newbie: 'Should I sell?'...",
                "Risk Level": "⚠️⚠️ Medium-Low Risk",
                "Veteran Advice": "HODL only if fundamentals haven't changed..."
            },
            "FOMO": {
                "Term Name": "FOMO (Fear Of Missing Out)",
                "Plain Language Definition": "Fear of missing out...",
                "Meme Origin Story": "Originally a psychology concept...",
                "Sentiment Analysis": "🔴 Bearish",
                "Scenario Simulation": "@degen_trader: 'This project 10x'd...'...'",
                "Risk Level": "⚠️⚠️⚠️⚠️⚠️ High Risk",
                "Veteran Advice": "FOMO is the #1 killer of profits..."
            }
        }
        
        return mock_responses.get(term, {})
    
    def run_all_tests(self):
        """Run all test cases"""
        
        print("\n" + "="*60)
        print("Web3 Slang Translator - Test Suite")
        print("="*60)
        
        # Test classic terms
        test_cases = [
            ("HODL", "Bullish"),
            ("FOMO", "Bearish"),
            ("FUD", "Bearish"),
            ("WAGMI", "Bullish"),
            ("REKT", "Bearish"),
        ]
        
        for term, sentiment in test_cases:
            self.test_dimensional_output(term, sentiment)
            time.sleep(0.5)  # Rate limiting
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary"""
        
        print("\n" + "="*60)
        print("Test Summary")
        print("="*60)
        print(f"Total Tests: {self.passed + self.failed}")
        print(f"✅ Passed: {self.passed}")
        print(f"❌ Failed: {self.failed}")
        print(f"Success Rate: {(self.passed / (self.passed + self.failed)) * 100:.1f}%")
        print("="*60)
        
        if self.failed > 0:
            print("\nFailed Tests:")
            for result in self.test_results:
                if not result['passed']:
                    print(f"  - {result['term']}")
                    if result['missing_dimensions']:
                        print(f"    Missing: {result['missing_dimensions']}")
        
        print("\n" + "="*60)
        if self.failed == 0:
            print("🎉 All tests passed! Skill is ready for production.")
        else:
            print("⚠️ Some tests failed. Please review and fix issues.")
        print("="*60 + "\n")


def main():
    """Main test runner"""
    
    tester = SkillTester()
    tester.run_all_tests()
    
    # Additional manual tests
    print("\n" + "="*60)
    print("Manual Test Checklist")
    print("="*60)
    print("\nPlease manually verify:")
    print("1. [ ] Web search works for new terms")
    print("2. [ ] Persona is humorous and blunt")
    print("3. [ ] Risk warnings are appropriate")
    print("4. [ ] All 5 quick commands work")
    print("5. [ ] Edge cases handled gracefully")
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
