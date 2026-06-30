#!/usr/bin/env python3
"""Daily SEO content for bio-generator site."""
import os, sys, json, random
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
POSTS_DIR = BASE_DIR / "_posts"
POSTS_DIR.mkdir(parents=True, exist_ok=True)

ARTICLES = [
    {
        "title": "200+ Best Instagram Bios for 2026: Stand Out & Get Followers",
        "slug": "best-instagram-bios-2026",
        "tags": ["Instagram", "Bio", "Social Media"],
        "body": [
            "## Why Your Instagram Bio Matters More Than Ever",
            "Your Instagram bio is the first thing people see when they visit your profile. With Instagram's algorithm favoring engagement, a compelling bio can be the difference between a follow and a scroll-past.",
            "## Key Elements of a Great Bio",
            "• A clear value proposition: What do you offer?<br>• Personality: Be authentic, not corporate<br>• A call-to-action: Link, subscribe, shop<br>• Keywords: Help people find you in search<br>• Emojis: Use them strategically (not excessively)",
            "## Bio Ideas by Category",
            "### For Creators",
            "🎨 Turning ideas into art • DM for collabs • {keyword}",
            "### For Business",
            "💼 Helping brands grow • Strategy × Creativity • {keyword}",
            "### For Lifestyle",
            "🌍 Travel • Food • Coffee • Living my best life • {keyword}",
            "## Free Tool to Generate More",
            "Need more options? Use our <a href='../index.html'>free Instagram bio generator</a> — pick your style and get instant bios tailored to your brand.",
        ],
    },
    {
        "title": "LinkedIn Bio Examples That Get You Hired in 2026",
        "slug": "linkedin-bio-examples-2026",
        "tags": ["LinkedIn", "Career", "Professional"],
        "body": [
            "## Why Your LinkedIn Bio Matters",
            "Recruiters spend an average of 7 seconds scanning your LinkedIn profile. Your headline and summary need to make an instant impact.",
            "## The Formula for a Winning Bio",
            "1. Headline: Job title + value proposition + keywords<br>2. Summary: Problem you solve + how you solve it + proof<br>3. Call-to-action: Connect, message, or visit your portfolio<br>4. Skills: Include relevant keywords for search",
            "## Headline Examples",
            "### Marketing Professional",
            "📊 Digital Marketing Strategist | Helping brands 10x their ROI | {keyword}",
            "### Software Engineer",
            "👨‍💻 Full-Stack Developer | React • Python • Cloud | Building products users love",
            "### Sales Professional",
            "🤝 B2B Sales Leader | Consistently exceeding quotas | {keyword}",
            "## Generate Your Perfect Bio",
            "Use our <a href='../index.html'>free LinkedIn bio generator</a> to create a professional headline and summary in seconds.",
        ],
    },
    {
        "title": "Twitter/X Bio Ideas: Make Your Profile Stand Out",
        "slug": "twitter-bio-ideas-2026",
        "tags": ["Twitter", "X", "Social Media"],
        "body": [
            "## The Art of the Twitter Bio",
            "With only 160 characters, your Twitter bio needs to work harder than any other platform. Every word counts.",
            "## What Works on Twitter",
            "• Be specific: 'I write about tech' vs 'I write about AI startups and indie hacking'<br>• Show personality: Twitter rewards authentic voices<br>• Include keywords: Help people find you in search<br>• Link strategically: Your best content or landing page",
            "## Template: The Problem Solver",
            "Helping {audience} achieve {result} without {pain point} • {keyword}",
            "## Template: The Curator",
            "Curating the best {topic} content • {keyword} • Sharing what I learn",
            "## Template: The Builder",
            "Building {project} • {keyword} • Documenting the journey in public",
            "## Create Yours Now",
            "Try our <a href='../index.html'>free Twitter bio generator</a> to experiment with different styles instantly.",
        ],
    },
    {
        "title": "TikTok Bio Tips: Grow Your Following Faster",
        "slug": "tiktok-bio-tips-2026",
        "tags": ["TikTok", "Growth", "Social Media"],
        "body": [
            "## Why TikTok Bios Are Different",
            "TikTok users decide to follow in seconds. Your bio needs to communicate your value instantly and match the platform's energetic, authentic vibe.",
            "## TikTok Bio Best Practices",
            "• Keep it short: 2-3 lines max<br>• Use emojis: TikTok is an emoji-native platform<br>• Tell them what to expect: Daily tips, funny sketches, etc.<br>• Include a CTA: Follow for more, link in bio<br>• Update regularly: Keep content fresh",
            "## Bio Ideas That Work",
            "### Educational Content",
            "📚 Learning {topic} so you don't have to • New tips daily • {keyword}",
            "### Comedy / Entertainment",
            "😂 Making you laugh one video at a time • {keyword} • Follow for daily serotonin",
            "### Lifestyle / Vlog",
            "☀️ Living my best life • {keyword} • Join the journey ✨",
            "## Level Up Your TikTok Game",
            "Use our <a href='../index.html'>free bio generator</a> to create platform-optimized bios for TikTok, Instagram, LinkedIn, and Twitter.",
        ],
    },
    {
        "title": "150+ Aesthetic Instagram Bios: Copy & Paste",
        "slug": "aesthetic-instagram-bios",
        "tags": ["Instagram", "Aesthetic", "Bios"],
        "body": [
            "## The Power of Aesthetic Bios",
            "Aesthetic bios create an immediate emotional connection with your audience. They signal taste, personality, and intentionality.",
            "## Minimalist Aesthetic",
            "less but better • {keyword} • quality over quantity",
            "## Nature Lover",
            "🌿 wild & free • finding beauty in the ordinary • {keyword}",
            "## Creative Soul",
            "🎨 making the world more beautiful • one post at a time • {keyword}",
            "## Dreamer",
            "☁️ chasing sunsets & big dreams • {keyword} • living in the moment",
            "## Why aesthetics matter",
            "A cohesive aesthetic across your bio, feed, and stories signals quality and builds trust. It tells visitors: 'This profile is curated. Follow for more of this.'",
            "## Generate Your Aesthetic Bio",
            "Can't find the right words? Try our <a href='../index.html'>free bio generator</a> with multiple aesthetic styles to match your vibe.",
        ],
    },
]

def md_to_html(text):
    lines = text.split("\n")
    out = []
    in_list = False; lt = None
    for line in lines:
        s = line.strip()
        if not s:
            if in_list: out.append(f"</{lt}>"); in_list = False; lt = None
            continue
        if s.startswith("### "):
            if in_list: out.append(f"</{lt}>"); in_list = False; lt = None
            out.append(f"<h3>{s[4:]}</h3>")
        elif s.startswith("## "):
            if in_list: out.append(f"</{lt}>"); in_list = False; lt = None
            out.append(f"<h2>{s[3:]}</h2>")
        elif s.startswith("• ") or s.startswith("- "):
            t = s.lstrip("•- ")
            if not in_list or lt != "ul": 
                if in_list: out.append(f"</{lt}>")
                out.append("<ul>"); in_list = True; lt = "ul"
            out.append(f"<li>{t}</li>")
        elif s[0].isdigit() and ". " in s[:4]:
            t = s.split(". ", 1)[1]
            if not in_list or lt != "ol":
                if in_list: out.append(f"</{lt}>")
                out.append("<ol>"); in_list = True; lt = "ol"
            out.append(f"<li>{t}</li>")
        else:
            if in_list: out.append(f"</{lt}>"); in_list = False; lt = None
            out.append(f"<p>{s}</p>")
    if in_list: out.append(f"</{lt}>")
    return "\n".join(out)

for art in ARTICLES:
    desc = art["body"][1][:160] if len(art["body"]) > 1 else ""
    body_html = md_to_html("\n".join(art["body"]))
    tags = " ".join(f'<span class="tag">{t}</span>' for t in art["tags"])
    today = datetime.now().strftime("%Y-%m-%d")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width">
<title>{art['title']}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://slashman413.github.io/bio-generator/_posts/{art['slug']}.html">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0f172a;color:#e2e8f0;max-width:720px;margin:auto;padding:20px;line-height:1.8;font-size:16px}}
h1{{margin:30px 0 10px;font-size:1.8rem}}
h2{{color:#60a5fa;margin:25px 0 10px;font-size:1.3rem;border-bottom:1px solid #1e293b;padding-bottom:5px}}
h3{{color:#93c5fd;margin:20px 0 8px;font-size:1.1rem}}
p{{margin:12px 0}}
ul,ol{{margin:10px 0 10px 24px}}
li{{margin:5px 0}}
.tag{{display:inline-block;background:#1e293b;color:#38bdf8;padding:2px 10px;border-radius:12px;font-size:.8rem;margin-right:5px}}
a{{color:#3b82f6}}
.date{{color:#64748b;font-size:.85rem;margin-bottom:20px}}
.cta{{background:linear-gradient(135deg,#1e293b,#334155);border:1px solid #475569;border-radius:12px;padding:20px;text-align:center;margin:25px 0}}
.cta a{{display:inline-block;background:#3b82f6;color:white;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:8px}}
.cta a:hover{{background:#2563eb}}
.back{{color:#64748b;text-decoration:none;font-size:.9rem;display:block;margin:20px 0}}
.back:hover{{color:#3b82f6}}
footer{{text-align:center;color:#475569;padding:30px 0;font-size:.85rem}}
</style>
</head>
<body>
<a href="../index.html" class="back">&larr; Back to Generator</a>
<h1>{art['title']}</h1>
<div class="date">{today}</div>
<div>{tags}</div>
{body_html}
<div class="cta">
<strong>✨ Generate your perfect bio now</strong><br>
<a href="../index.html">Try the Free Bio Generator →</a>
</div>
<footer>
<p><a href="https://github.com/slashman413/bio-generator">GitHub</a></p>
</footer>
</body>
</html>"""
    (POSTS_DIR / f"{today}-{art['slug']}.html").write_text(html, encoding="utf-8")
    print(f"  ✅ {art['slug']}.html")
print(f"✅ Generated {len(ARTICLES)} SEO articles")
