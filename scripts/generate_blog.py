#!/usr/bin/env python3
"""
MoreBuildtech - Daily SEO Blog Generator
Powered by Google Gemini (FREE)
Roz 10 AM IST pe automatically chalta hai
"""

import google.generativeai as genai
import json, os, re
from datetime import datetime
from pathlib import Path

SITE_URL = "https://morebuildtech.in"
BLOG_DIR = Path("blog")
WA_LINK  = "https://wa.me/918237408633?text=Hello!%20I%20read%20your%20blog%20and%20want%20a%20free%20consultation."

TOPICS = [
    {"topic":"Modern Living Room Interior Design Ideas for Mumbai Homes 2025",       "kw":"living room interior design Mumbai",       "cat":"Interior Design"},
    {"topic":"False Ceiling Designs: Types, Cost & Best Options for Indian Homes",   "kw":"false ceiling design India",              "cat":"Interior Design"},
    {"topic":"Modular Kitchen Design Ideas for Small Flats in Mumbai",               "kw":"modular kitchen design Mumbai",           "cat":"Kitchen Design"},
    {"topic":"Complete House Construction Cost Guide for Maharashtra 2025",           "kw":"house construction cost Maharashtra",     "cat":"Construction"},
    {"topic":"Vastu Shastra Tips for New Home Construction in India",                "kw":"vastu shastra home construction",         "cat":"Vastu"},
    {"topic":"Best Flooring Options for Indian Homes: Tiles vs Marble vs Vinyl",    "kw":"best flooring options Indian homes",      "cat":"Flooring"},
    {"topic":"Bedroom Interior Design: Luxury Look on Any Budget",                   "kw":"bedroom interior design India",           "cat":"Interior Design"},
    {"topic":"RCC vs Steel Structure: Which is Better for Your Home in India?",     "kw":"RCC vs steel structure India",            "cat":"Construction"},
    {"topic":"Interior Design Colour Combinations for Indian Homes 2025",           "kw":"interior colour combination India",       "cat":"Interior Design"},
    {"topic":"Bathroom Interior Design: Modern Ideas for Indian Homes",             "kw":"bathroom interior design India",          "cat":"Interior Design"},
    {"topic":"Commercial Office Interior Design Trends in Mumbai 2025",             "kw":"office interior design Mumbai",           "cat":"Commercial"},
    {"topic":"Home Renovation Tips: Complete Transformation Guide India",           "kw":"home renovation tips India",             "cat":"Renovation"},
    {"topic":"Waterproofing Solutions for Terrace and Bathrooms in India",          "kw":"waterproofing solutions India",           "cat":"Construction"},
    {"topic":"Wooden Furniture vs Modular Furniture: Best for Indian Homes?",      "kw":"wooden vs modular furniture India",       "cat":"Furniture"},
    {"topic":"How to Choose the Right Interior Designer in Mumbai",                 "kw":"interior designer Mumbai",               "cat":"Interior Design"},
    {"topic":"Kitchen Vastu: Direction, Tips and Design for a Happy Home",          "kw":"kitchen vastu tips India",               "cat":"Vastu"},
    {"topic":"Smart Home Automation Ideas for Modern Indian Homes 2025",            "kw":"smart home automation India",            "cat":"Smart Homes"},
    {"topic":"Building Material Prices in Maharashtra 2025: Complete Guide",        "kw":"building material prices Maharashtra",    "cat":"Construction"},
    {"topic":"Master Bedroom Design with Wardrobe and Lighting Ideas",              "kw":"master bedroom wardrobe design India",    "cat":"Interior Design"},
    {"topic":"Terrace Garden Design Ideas for Mumbai Apartments",                   "kw":"terrace garden design Mumbai",           "cat":"Landscaping"},
    {"topic":"How Long Does Home Construction Take? Complete Timeline",             "kw":"home construction timeline India",        "cat":"Construction"},
    {"topic":"Pooja Room Interior Design: Vastu-Friendly Ideas India",             "kw":"pooja room interior design vastu",        "cat":"Interior Design"},
    {"topic":"Wall Painting vs Wallpaper: Which is Better for Indian Homes?",      "kw":"wall painting vs wallpaper India",        "cat":"Interior Design"},
    {"topic":"Shop Interior Design Ideas to Attract More Customers India",         "kw":"shop interior design India",             "cat":"Commercial"},
    {"topic":"Foundation Types in Construction: Which is Best for Your Plot?",     "kw":"foundation types construction India",    "cat":"Construction"},
    {"topic":"Home Interior Budget Planning: Room-by-Room Cost Breakdown",         "kw":"home interior budget India",             "cat":"Interior Design"},
    {"topic":"Window Designs for Indian Homes: Style, Ventilation & Vastu",        "kw":"window design Indian homes",             "cat":"Architecture"},
    {"topic":"Exterior Home Design: Paint Colors & Elevation Ideas India",         "kw":"exterior home design India",             "cat":"Architecture"},
]

def slugify(t):
    t = t.lower()
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    return re.sub(r'\s+', '-', t.strip())

def get_topic():
    return TOPICS[datetime.now().timetuple().tm_yday % len(TOPICS)]

def ai_generate(t):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    prompt = f"""You are an SEO expert writing for MoreBuildtech, a premium interior & construction company in Mumbai, India.

Write a complete SEO blog post:
TOPIC: {t['topic']}
PRIMARY KEYWORD: {t['kw']}
CATEGORY: {t['cat']}
DATE: {datetime.now().strftime('%B %d, %Y')}

SEO RULES:
- Title: 50-60 chars, must include keyword
- Meta description: 150-160 chars with CTA
- Intro: keyword in first 100 words
- 5-6 H2 subheadings (long-tail keyword phrases)
- H3 under each H2 where needed
- 1200-1500 words total
- Keyword density 1-2%
- Mention Mumbai/Maharashtra naturally
- Include costs in INR where relevant
- 4 FAQ items at end
- End with MoreBuildtech free consultation CTA

Return ONLY valid JSON, no markdown fences, no extra text:
{{
  "title": "SEO title 50-60 chars",
  "meta": "meta description 150-160 chars",
  "slug": "url-slug",
  "reading_time": "X min read",
  "excerpt": "2-sentence excerpt for blog listing",
  "tags": ["tag1","tag2","tag3","tag4","tag5"],
  "html": "<article>full blog content with h2,h3,p,ul,strong tags</article>",
  "faq": [
    {{"q":"Question 1?","a":"Answer in 2-3 sentences."}},
    {{"q":"Question 2?","a":"Answer in 2-3 sentences."}},
    {{"q":"Question 3?","a":"Answer in 2-3 sentences."}},
    {{"q":"Question 4?","a":"Answer in 2-3 sentences."}}
  ]
}}"""

    response = model.generate_content(prompt)
    raw = response.text.strip()
    raw = re.sub(r'^```json\s*', '', raw)
    raw = re.sub(r'^```\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    return json.loads(raw)

def make_blog_page(d, t):
    date  = datetime.now().strftime("%B %d, %Y")
    iso   = datetime.now().strftime("%Y-%m-%d")
    slug  = d["slug"]
    url   = f"{SITE_URL}/blog/{slug}.html"
    tags  = " ".join(f'<span class="b-tag">{x}</span>' for x in d.get("tags", []))
    faqs  = "".join(
        f'<div class="faq-item"><div class="faq-q">{x["q"]}</div><div class="faq-a">{x["a"]}</div></div>'
        for x in d.get("faq", [])
    )

    faq_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type":"Question","name":x["q"],"acceptedAnswer":{"@type":"Answer","text":x["a"]}}
            for x in d.get("faq", [])
        ]
    })
    art_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": d["title"],
        "datePublished": iso,
        "author": {"@type":"Organization","name":"MoreBuildtech Expert Team"},
        "publisher": {"@type":"Organization","name":"MoreBuildtech","url":SITE_URL},
        "description": d["meta"],
        "url": url
    })
    bc_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type":"ListItem","position":1,"name":"Home","item":SITE_URL},
            {"@type":"ListItem","position":2,"name":"Blog","item":f"{SITE_URL}/blog"},
            {"@type":"ListItem","position":3,"name":d["title"],"item":url}
        ]
    })

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{d['title']} | MoreBuildtech</title>
<meta name="description" content="{d['meta']}"/>
<meta name="keywords" content="{t['kw']}, {', '.join(d.get('tags',[]))}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{url}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{d['title']}"/>
<meta property="og:description" content="{d['meta']}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:site_name" content="MoreBuildtech"/>
<meta property="article:published_time" content="{iso}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{d['title']}"/>
<meta name="twitter:description" content="{d['meta']}"/>
<script type="application/ld+json">{art_schema}</script>
<script type="application/ld+json">{faq_schema}</script>
<script type="application/ld+json">{bc_schema}</script>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet"/>
<style>
:root{{--black:#080808;--deep:#0d0d0d;--panel:#111111;--gold:#c9a84c;--gold2:#e8c97a;--white:#f8f4ee;--grey:#888;--glass:rgba(255,255,255,0.04);--glass-border:rgba(201,168,76,0.2);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--black);color:var(--white);font-family:'Montserrat',sans-serif;font-weight:300;overflow-x:hidden;}}
::-webkit-scrollbar{{width:3px;}}
::-webkit-scrollbar-track{{background:var(--black);}}
::-webkit-scrollbar-thumb{{background:var(--gold);border-radius:2px;}}
nav{{position:sticky;top:0;z-index:1000;background:rgba(8,8,8,0.95);backdrop-filter:blur(20px);display:flex;align-items:center;justify-content:space-between;padding:20px 60px;border-bottom:1px solid var(--glass-border);}}
.logo{{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:600;letter-spacing:4px;color:var(--white);text-transform:uppercase;text-decoration:none;}}
.logo span{{color:var(--gold);}}
.nav-links{{display:flex;gap:32px;list-style:none;}}
.nav-links a{{font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:rgba(248,244,238,0.6);text-decoration:none;transition:color 0.3s;}}
.nav-links a:hover{{color:var(--gold);}}
.nav-cta{{border:1px solid var(--gold)!important;color:var(--gold)!important;padding:8px 22px;}}
.nav-cta:hover{{background:var(--gold)!important;color:var(--black)!important;}}
.breadcrumb{{background:var(--panel);padding:12px 60px;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:var(--grey);border-bottom:1px solid var(--glass-border);}}
.breadcrumb a{{color:var(--grey);text-decoration:none;transition:color 0.3s;}}
.breadcrumb a:hover{{color:var(--gold);}}
.breadcrumb span{{margin:0 8px;color:var(--gold);}}
.blog-hero{{background:var(--deep);padding:64px 60px 48px;border-bottom:1px solid var(--glass-border);position:relative;overflow:hidden;}}
.blog-hero::before{{content:'';position:absolute;top:-100px;right:-100px;width:500px;height:500px;background:radial-gradient(circle,rgba(201,168,76,0.08) 0%,transparent 65%);pointer-events:none;}}
.b-cat{{display:inline-block;border:1px solid var(--gold);color:var(--gold);font-size:0.6rem;letter-spacing:3px;text-transform:uppercase;padding:5px 16px;margin-bottom:20px;}}
.blog-hero h1{{font-family:'Cormorant Garamond',serif;font-size:clamp(1.8rem,4vw,3.2rem);font-weight:400;line-height:1.25;color:var(--white);max-width:800px;margin-bottom:24px;}}
.blog-meta{{display:flex;flex-wrap:wrap;gap:24px;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:var(--grey);}}
.blog-meta span::before{{content:'— ';color:var(--gold);}}
.blog-body{{max-width:820px;margin:0 auto;padding:56px 24px 80px;}}
article h2{{font-family:'Cormorant Garamond',serif;font-size:1.9rem;font-weight:400;color:var(--white);margin:52px 0 16px;padding-bottom:12px;border-bottom:1px solid var(--glass-border);position:relative;}}
article h2::after{{content:'';position:absolute;bottom:-1px;left:0;width:40px;height:1px;background:var(--gold);}}
article h3{{font-size:0.95rem;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin:32px 0 12px;}}
article p{{margin-bottom:20px;font-size:0.95rem;line-height:1.95;color:rgba(248,244,238,0.75);}}
article ul,article ol{{margin:12px 0 20px 24px;}}
article li{{margin-bottom:10px;font-size:0.9rem;line-height:1.8;color:rgba(248,244,238,0.7);}}
article strong{{color:var(--white);font-weight:500;}}
article a{{color:var(--gold);text-decoration:none;border-bottom:1px solid rgba(201,168,76,0.3);}}
.tags-row{{display:flex;flex-wrap:wrap;gap:8px;margin:40px 0;}}
.b-tag{{background:transparent;border:1px solid rgba(201,168,76,0.25);color:var(--grey);font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;padding:5px 14px;}}
.faq-section{{background:var(--panel);border:1px solid var(--glass-border);padding:40px;margin:48px 0;}}
.faq-section h2{{font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:400;color:var(--white);margin-bottom:32px;}}
.faq-item{{border-bottom:1px solid var(--glass-border);padding:20px 0;}}
.faq-item:last-child{{border-bottom:none;}}
.faq-q{{font-size:0.85rem;font-weight:500;letter-spacing:1px;color:var(--gold);margin-bottom:10px;}}
.faq-a{{font-size:0.88rem;line-height:1.85;color:rgba(248,244,238,0.65);}}
.cta-box{{background:linear-gradient(135deg,rgba(201,168,76,0.08),rgba(201,168,76,0.03));border:1px solid var(--glass-border);padding:48px;text-align:center;margin:48px 0;position:relative;overflow:hidden;}}
.cta-box::before{{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(201,168,76,0.1) 0%,transparent 65%);}}
.cta-tag{{font-size:0.6rem;letter-spacing:4px;text-transform:uppercase;color:var(--gold);margin-bottom:16px;}}
.cta-box h3{{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:400;color:var(--white);margin-bottom:12px;}}
.cta-box p{{font-size:0.85rem;color:var(--grey);margin-bottom:28px;line-height:1.8;}}
.btn-gold{{display:inline-block;background:linear-gradient(135deg,var(--gold),var(--gold2));color:var(--black);padding:14px 40px;font-family:'Montserrat',sans-serif;font-size:0.65rem;letter-spacing:4px;text-transform:uppercase;text-decoration:none;font-weight:600;transition:transform 0.3s,box-shadow 0.3s;}}
.btn-gold:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(201,168,76,0.35);border-bottom:none;}}
footer{{background:var(--deep);border-top:1px solid var(--glass-border);padding:32px 60px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;}}
.footer-logo{{font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;letter-spacing:4px;text-transform:uppercase;color:var(--white);}}
.footer-logo span{{color:var(--gold);}}
footer p{{font-size:0.65rem;letter-spacing:1px;color:var(--grey);}}
footer a{{color:var(--gold);text-decoration:none;}}
.wa-float{{position:fixed;bottom:32px;right:32px;z-index:9999;}}
.wa-btn{{width:56px;height:56px;background:linear-gradient(135deg,#25D366,#128C7E);border-radius:50%;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:0 6px 24px rgba(37,211,102,0.4);transition:transform 0.3s;}}
.wa-btn:hover{{transform:scale(1.1);}}
.wa-btn svg{{width:26px;height:26px;fill:#fff;}}
@media(max-width:768px){{nav{{padding:16px 20px;}}.breadcrumb{{padding:10px 20px;}}.blog-hero{{padding:40px 20px 32px;}}.blog-meta{{gap:12px;}}footer{{padding:24px;flex-direction:column;text-align:center;}}}}
</style>
</head>
<body>
<nav>
  <a class="logo" href="{SITE_URL}">MORE<span>BUILD</span>TECH</a>
  <ul class="nav-links">
    <li><a href="{SITE_URL}/#services">Services</a></li>
    <li><a href="{SITE_URL}/blog">Blog</a></li>
    <li><a href="{SITE_URL}/#process">Process</a></li>
    <li><a class="nav-cta" href="{WA_LINK}">Get Quote</a></li>
  </ul>
</nav>
<div class="breadcrumb">
  <a href="{SITE_URL}">Home</a><span>›</span>
  <a href="{SITE_URL}/blog">Blog</a><span>›</span>
  {t['cat']}
</div>
<div class="blog-hero">
  <div class="b-cat">{t['cat']}</div>
  <h1>{d['title']}</h1>
  <div class="blog-meta">
    <span>{date}</span>
    <span>{d.get('reading_time','6 min read')}</span>
    <span>MoreBuildtech Expert Team</span>
    <span>Mumbai, Maharashtra</span>
  </div>
</div>
<div class="blog-body">
  {d['html']}
  <div class="tags-row">{tags}</div>
  <div class="faq-section">
    <h2>Frequently Asked Questions</h2>
    {faqs}
  </div>
  <div class="cta-box">
    <div class="cta-tag">Free Consultation</div>
    <h3>Ready to Build Your Dream Space?</h3>
    <p>Mumbai's trusted interior & construction experts — 7+ years, 50+ projects, 98% satisfaction.<br/>
    Get a free consultation today and let's bring your vision to life.</p>
    <a class="btn-gold" href="{WA_LINK}">WhatsApp Us Now</a>
  </div>
</div>
<footer>
  <div class="footer-logo">MORE<span>BUILD</span>TECH</div>
  <p>© {datetime.now().year} MoreBuildtech. Premium Interior & Construction, Mumbai.</p>
  <p><a href="{SITE_URL}/blog">All Blogs</a> &nbsp;|&nbsp; <a href="{SITE_URL}">Home</a></p>
</footer>
<div class="wa-float">
  <a class="wa-btn" href="{WA_LINK}" target="_blank" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>
</div>
</body>
</html>"""

def make_index(posts):
    cards = ""
    for p in sorted(posts, key=lambda x: x["date_iso"], reverse=True)[:50]:
        cards += f"""
<article class="b-card">
  <div class="b-cat-badge">{p['cat']}</div>
  <h2 class="b-card-title"><a href="{SITE_URL}/blog/{p['slug']}.html">{p['title']}</a></h2>
  <p class="b-card-excerpt">{p['excerpt']}</p>
  <div class="b-card-footer">
    <span>{p['date']}</span>
    <a href="{SITE_URL}/blog/{p['slug']}.html">Read More →</a>
  </div>
</article>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Interior & Construction Blog | MoreBuildtech Mumbai</title>
<meta name="description" content="Expert interior design and construction tips for Indian homes. Vastu, renovation, modular kitchen, false ceiling guides by MoreBuildtech Mumbai."/>
<link rel="canonical" href="{SITE_URL}/blog"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet"/>
<style>
:root{{--black:#080808;--deep:#0d0d0d;--panel:#111111;--gold:#c9a84c;--gold2:#e8c97a;--white:#f8f4ee;--grey:#888;--glass-border:rgba(201,168,76,0.2);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--black);color:var(--white);font-family:'Montserrat',sans-serif;font-weight:300;}}
::-webkit-scrollbar{{width:3px;}}::-webkit-scrollbar-thumb{{background:var(--gold);}}
nav{{position:sticky;top:0;z-index:100;background:rgba(8,8,8,0.95);backdrop-filter:blur(20px);display:flex;align-items:center;justify-content:space-between;padding:20px 60px;border-bottom:1px solid var(--glass-border);}}
.logo{{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:600;letter-spacing:4px;color:var(--white);text-transform:uppercase;text-decoration:none;}}
.logo span{{color:var(--gold);}}
.nav-links{{display:flex;gap:32px;list-style:none;}}
.nav-links a{{font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:rgba(248,244,238,0.6);text-decoration:none;transition:color 0.3s;}}
.nav-links a:hover{{color:var(--gold);}}
.nav-cta{{border:1px solid var(--gold)!important;color:var(--gold)!important;padding:8px 22px;}}
.blog-hero{{background:var(--deep);padding:72px 60px;text-align:center;border-bottom:1px solid var(--glass-border);position:relative;overflow:hidden;}}
.blog-hero::before{{content:'';position:absolute;top:-150px;left:50%;transform:translateX(-50%);width:600px;height:600px;background:radial-gradient(circle,rgba(201,168,76,0.07) 0%,transparent 65%);pointer-events:none;}}
.hero-tag{{font-size:0.6rem;letter-spacing:5px;text-transform:uppercase;color:var(--gold);margin-bottom:20px;display:flex;align-items:center;justify-content:center;gap:14px;}}
.hero-tag::before,.hero-tag::after{{content:'';width:30px;height:1px;background:var(--gold);}}
.blog-hero h1{{font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,5vw,4rem);font-weight:300;color:var(--white);margin-bottom:16px;}}
.blog-hero p{{font-size:0.85rem;color:var(--grey);letter-spacing:1px;}}
.grid{{max-width:1200px;margin:64px auto;padding:0 40px;display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1px;background:var(--glass-border);border:1px solid var(--glass-border);}}
.b-card{{background:var(--black);padding:36px;transition:background 0.3s;}}
.b-card:hover{{background:var(--panel);}}
.b-cat-badge{{display:inline-block;border:1px solid rgba(201,168,76,0.3);color:var(--gold);font-size:0.55rem;letter-spacing:3px;text-transform:uppercase;padding:4px 12px;margin-bottom:16px;}}
.b-card-title{{font-family:'Cormorant Garamond',serif;font-size:1.35rem;font-weight:400;line-height:1.4;margin-bottom:12px;}}
.b-card-title a{{color:var(--white);text-decoration:none;transition:color 0.3s;}}
.b-card-title a:hover{{color:var(--gold);}}
.b-card-excerpt{{font-size:0.8rem;line-height:1.8;color:var(--grey);margin-bottom:20px;}}
.b-card-footer{{display:flex;justify-content:space-between;align-items:center;font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--grey);border-top:1px solid var(--glass-border);padding-top:16px;}}
.b-card-footer a{{color:var(--gold);text-decoration:none;}}
footer{{background:var(--deep);border-top:1px solid var(--glass-border);padding:32px 60px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;margin-top:64px;}}
.footer-logo{{font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;letter-spacing:4px;text-transform:uppercase;}}
.footer-logo span{{color:var(--gold);}}
footer p{{font-size:0.65rem;letter-spacing:1px;color:var(--grey);}}
footer a{{color:var(--gold);text-decoration:none;}}
@media(max-width:768px){{nav{{padding:16px 20px;}}.blog-hero{{padding:48px 20px;}}.grid{{padding:0;margin:32px 0;}}.b-card{{padding:24px;}}footer{{padding:24px;flex-direction:column;text-align:center;}}}}
</style>
</head>
<body>
<nav>
  <a class="logo" href="{SITE_URL}">MORE<span>BUILD</span>TECH</a>
  <ul class="nav-links">
    <li><a href="{SITE_URL}/#services">Services</a></li>
    <li><a href="{SITE_URL}/blog">Blog</a></li>
    <li><a class="nav-cta" href="{WA_LINK}">Get Quote</a></li>
  </ul>
</nav>
<div class="blog-hero">
  <div class="hero-tag">Expert Knowledge</div>
  <h1>Interior & Construction Blog</h1>
  <p>Design ideas, construction guides & expert tips for Indian homes — by MoreBuildtech, Mumbai</p>
</div>
<div class="grid">{cards}</div>
<footer>
  <div class="footer-logo">MORE<span>BUILD</span>TECH</div>
  <p>© {datetime.now().year} MoreBuildtech — Premium Interior & Construction, Mumbai</p>
  <p><a href="{SITE_URL}">Home</a> &nbsp;|&nbsp; <a href="{WA_LINK}">WhatsApp</a></p>
</footer>
</body>
</html>"""

def load_registry():
    f = BLOG_DIR / "_registry.json"
    return json.loads(f.read_text()) if f.exists() else []

def save_registry(posts):
    BLOG_DIR.mkdir(exist_ok=True)
    (BLOG_DIR / "_registry.json").write_text(json.dumps(posts, indent=2, ensure_ascii=False))

def main():
    print(f"MoreBuildtech Blog — {datetime.now().strftime('%d %b %Y %H:%M')}")
    t = get_topic()
    print(f"Topic: {t['topic']}")

    d = ai_generate(t)
    slug = slugify(d.get("slug", t["topic"]))
    BLOG_DIR.mkdir(exist_ok=True)
    (BLOG_DIR / f"{slug}.html").write_text(make_blog_page(d, t), encoding="utf-8")
    print(f"Created: blog/{slug}.html")

    posts = load_registry()
    if not any(p["slug"] == slug for p in posts):
        posts.append({
            "slug": slug,
            "title": d["title"],
            "excerpt": d.get("excerpt", ""),
            "cat": t["cat"],
            "date": datetime.now().strftime("%b %d, %Y"),
            "date_iso": datetime.now().strftime("%Y-%m-%d")
        })
        save_registry(posts)

    (BLOG_DIR / "index.html").write_text(make_index(posts), encoding="utf-8")
    print(f"Blog index updated — {len(posts)} posts total")
    print(f"Live at: {SITE_URL}/blog/{slug}.html")

if __name__ == "__main__":
    main()
 
