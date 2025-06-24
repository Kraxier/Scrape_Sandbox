# Guide on Learning Things 
r'''
Phase 1: Fundamentals (Week 1)
Understanding Websites

    Static vs. Dynamic websites (Prerequisite_1.md)
    JavaScript vs. Dynamic websites (Pre_javascript_Dynamics_Comparison.md)
    Tools for JS-heavy sites (Pre_Tools_for_JS_Dy.md)

Tool Selection
    Playwright vs. Selenium comparison (Pre_Selenium_vs_Playwright.md)
    Why Playwright? (Performance, stealth features)

Playwright Basics
    Sync vs. Async concepts (Play_1_test_1_concept.py)

Phase 2: Core Skills (Week 2)
    1. Content Retrieval
        * text_content() vs inner_text()
        * Locator strategies (Play_1_test_1_concept.py)

    2. Dynamic Content Handling
        * Explicit waiting strategies (explicit_waiting_1.py)
        * JS-delayed content patterns (concept_delayed.py)
        * Practical: Quotes.toscrape JS-delayed

    3. State Management
        * .is_visible(), .is_enabled() checks
        * Verification patterns (verify_check_1.py)

Phase 3: Advanced Techniques (Week 3)
    1. Concurrency Models
        Sync vs. Async implementations (Play_3_browser_context_pages.py)
        Multi-tab vs. Multi-browser strategies

    2. Resource Management
        Browser contexts and sessions (browser_context.py)
        Scaling decisions (Decision Tree)

    3. Anti-Detection
        User-agent rotation
        Request throttling
        Proxy configuration

Phase 4: Optimization (Week 4)
    1. JavaScript Framework Patterns
        React/Angular/Vue specific challenges (Play_4_Concept.py)
        Shadow DOM handling

    2. Performance Optimization
        Concurrency control (browser_context.py)
        Resource monitoring
        Hybrid approaches (API + browser)

    3. Error Handling & Verification
        Robust verification checks:

Phase 5: Scaling (Ongoing)
    1. Architecture Patterns
        Isolated contexts
        Session management
        Queue-based systems

    2. Monitoring & Adaptation
        Success rate tracking
        Dynamic scaling (should_scale_up() logic)
        Anti-blocking rotation

'''