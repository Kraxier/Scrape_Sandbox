# Goal for Playwright 
r'''
Creating a Milestone for Playwright 

Goal: Implement all the Core and Fundamentals in Playwright while creating a mini project in 
quotetoscrape.com

1. Javascript Website {Done}
2. Delayed Javascript Website {Done}
3. Infinite Scrolling {Done}
    V2 Human Behaviour Infinite Scrolling 
4. Form Interaction and Login 
    {
        https://quotes.toscrape.com/login
        https://quotes.toscrape.com/search.aspx
        }
5. Messy HTML & Advanced Selectors
    Endpoints: Tableful
'''

# Documents Learning Basics to Advance
# For Each of the Endpoint should be the Documentation of Learning 
    # Selenium Based is a Structured Path 
    # Hybrid Approach is the Hybrid Path for Implementation and for Concepts Studying 
# Let's take a Stepback from Everything and Organize the Learning Stuff of Things 






# Goal Create a Project 
r'''
Implement 
    1. CSV a Basic Pipeline Integration 
    2. Retry Logic 
    3. User Agent Rotation + Window Size 
    4. Human Like Interaction 
    5. Performance Monitoring 
    6. Behavioural Patterns 

'''





# Research in Phone User Agent + Behavioural Pattern + Fingerprinting 
# I'm Going to Delay the Proxy Rotation so 1 - 2 Request per Things man 
# Careful in User Agent Implementations Stuff 

r'''
from fake_useragent import UserAgent
ua = UserAgent()

# Random UA
print(ua.random)  
# e.g., "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Chrome/131.0.0.0 Safari/537.36"

# Browser-specific UA
print(ua.chrome, ua.firefox, ua.edge)


💡 Pro Tips Practicals for User Agents 
1. Rotate UAs every 3–5 requests to mimic natural traffic ( Rotation Frequency ).
2. Match UAs to IP geolocation (e.g., don’t use a French UA with a Japanese IP).
3. Combine with headers like Accept-Language and Sec-CH-UA 9.
4. Test UAs against httpbin.org/headers to verify 3.

⚠️ Avoid outdated UAs (e.g., Chrome v60) – they signal bots. Use libraries with auto-updates to stay current. For advanced anti-blocking, pair with residential proxies and behavior emulation.


------------------------------------------------------------------------
🎯 The 80/20 Pareto Principle for Human Behavior in Playwright Python
Focus on these 4 core behaviors that deliver 80% of human-like results with 20% effort:

Scrolling > Mouse Movement > Action Timing > Typing and Error 

1. Variable Action Timing (35% impact)
* Humans never operate at machine precision. Implement:

2. Organic Mouse Movements (30% impact)
Avoid straight-line pointer motions:

3. Natural Scrolling (25% impact)
The #1 most detectable behavior:

4. Behavioral Patterns (10% impact)
Mimic human interaction quirks:

Behavior	Key Parameters	Ideal Range
Scrolling	speed_factor	0.8-1.5x
Mouse Movement	steps	3-8 steps
Delays	think time	2.5-8.0s
Errors	Mistake probability	3-7%

📈 When to Go Beyond 80/20
Upgrade when you encounter:

Cloudflare challenges

"Please verify you're human" captchas

Behavioral biometric systems (e.g., PerimeterX)


'''