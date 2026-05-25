# MoreBuildtech — Blog Automation Setup

## GitHub pe kya upload karna hai?

Is ZIP mein ye sab files hain — sab ek saath upload karo:

```
✅ index.html                    ← Aapki existing website
✅ google62979d125a092d95.html   ← Google verification file
✅ .github/workflows/daily-blog.yml  ← Scheduler (10 AM daily)
✅ scripts/generate_blog.py      ← AI blog generator
✅ blog/                         ← Blog folder (auto-fill hoga)
```

## Setup Steps (30 minutes)

### 1. GitHub
- github.com pe free account banao
- New repo: `morebuildtech-website` (Public)
- Is ZIP ki saari files upload karo

### 2. Anthropic API Key (Free credits!)
- console.anthropic.com pe signup karo
- API Keys → Create Key → copy karo

### 3. GitHub Secret
- Repo → Settings → Secrets → Actions
- New secret: `ANTHROPIC_API_KEY` = apni key

### 4. Netlify Deploy (Free)
- netlify.com pe signup
- Add new site → GitHub → apni repo
- Deploy → `morebuildtech.in` domain add karo

## Done! Roz 10 AM pe automatic blog live ho jayega.

Blog URL: https://morebuildtech.in/blog
Cost: ~Rs.3-5 per blog post only
