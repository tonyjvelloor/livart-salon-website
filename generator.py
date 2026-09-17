import os
import json

BASE_DIR = "/Users/tonyvelloor/.gemini/antigravity/scratch/livart-salon-website"

# Core Configuration
SITE_NAME = "LivArt Salon & Make-Up Studio"
SITE_TAGLINE = "Premier Destination Hair & Makeup Atelier in Kakkanad, Kochi"
BASE_URL = "https://livartsalon.com"
PHONE = "+91 70120 59591"
PHONE_TEL = "+917012059591"
EMAIL = "info@livart.co.in"
ADDRESS = "2nd Floor, Anchorage Business Center, Seaport – Airport Road, NGO Quarters – Mavelipuram Rd, Kakkanad, Kochi, Kerala 682030"
HOURS = "Monday – Saturday: 9:30 AM – 8:30 PM | Sunday: 10:00 AM – 7:30 PM"
INSTAGRAM_HANDLE = "@Livart_salon"
INSTAGRAM_URL = "https://www.instagram.com/Livart_salon/"
FACEBOOK_URL = "https://www.facebook.com/livartsalon/"
LOGO_URL = "https://livartsalon.com/wp-content/uploads/2022/10/logo1.jpg"

ACADEMY_URL = "https://livart.co.in"
ACADEMY_FOUNDER_URL = "https://livart.co.in/founder-makeup-academy/"
PRESS_FEATURE_URL = "https://businessperiscope.com/stephy-sebastian-founder-of-livart-beauty-academy/"

LOCAL_BUSINESS_SCHEMA = {
    "@context": "https://schema.org",
    "@type": ["HairSalon", "BeautySalon", "HealthAndBeautyBusiness"],
    "name": "LivArt Salon & Make-Up Studio",
    "image": LOGO_URL,
    "@id": "https://livartsalon.com/#salon",
    "url": "https://livartsalon.com",
    "telephone": PHONE,
    "email": EMAIL,
    "priceRange": "₹₹",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "2nd floor, Anchorage business center, Seaport - Airport Road, NGO Quarters - Mavelipuram Rd",
        "addressLocality": "Kakkanad, Kochi",
        "addressRegion": "Kerala",
        "postalCode": "682030",
        "addressCountry": "IN"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 10.021406,
        "longitude": 76.342732
    },
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:30",
            "closes": "20:30"
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Sunday",
            "opens": "10:00",
            "closes": "19:30"
        }
    ],
    "sameAs": [
        INSTAGRAM_URL,
        FACEBOOK_URL,
        ACADEMY_URL,
        ACADEMY_FOUNDER_URL,
        PRESS_FEATURE_URL
    ],
    "founder": {
        "@type": "Person",
        "name": "Stephy Sebastian",
        "jobTitle": ["Founder & Creative Director", "Celebrity Hair & Makeup Artist", "Master Cosmetology Educator"],
        "url": ACADEMY_FOUNDER_URL,
        "image": "https://livartsalon.com/wp-content/uploads/2024/02/Stephy-Sebastian.webp",
        "description": "Stephy Sebastian is a celebrated celebrity hair stylist, bridal makeup artist, former national educator for L'Oréal Professionnel and Wella, and founder of LivArt Hair & Makeup Studio and LivArt Beauty Academy.",
        "sameAs": [
            ACADEMY_FOUNDER_URL,
            PRESS_FEATURE_URL,
            INSTAGRAM_URL,
            FACEBOOK_URL
        ],
        "knowsAbout": [
            "Haute Couture Hair Styling",
            "HD Bridal Makeup Artistry",
            "Cosmetology & Aesthetic Education",
            "Balayage & Advanced Hair Color Correction",
            "Hair Botox & Keratin Rejuvenation",
            "Clinical Skincare Aesthetics"
        ]
    },
    "subOrganization": {
        "@type": "EducationalOrganization",
        "name": "LivArt Beauty Academy",
        "url": ACADEMY_URL,
        "description": "Government-affiliated beauty and cosmetology academy accredited with B&WSSC (Beauty & Wellness Sector Skill Council of India), offering professional diplomas in cosmetology, bridal makeup, hair styling, and aesthetic skincare.",
        "sameAs": [
            ACADEMY_URL,
            PRESS_FEATURE_URL
        ]
    },
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "480"
    }
}

def render_head(title, description, canonical_path, extra_schema=None, root_prefix=""):
    schemas = [LOCAL_BUSINESS_SCHEMA]
    if extra_schema:
        schemas.append(extra_schema)

    schema_script = f'<script type="application/ld+json">{json.dumps(schemas, indent=2)}</script>'

    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{BASE_URL}{canonical_path}" />
  
  <!-- Open Graph -->
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{BASE_URL}{canonical_path}" />
  <meta property="og:site_name" content="{SITE_NAME}" />
  <meta property="og:image" content="{LOGO_URL}" />
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{LOGO_URL}" />

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "obsidian-deep": "#0F0F11",
            "obsidian-surface": "#18181B",
            "champagne-gold": "#C5A059",
            "warm-bronze": "#9E7B3B",
            "metallic-gold-light": "#E8D8A6",
            "alabaster-cream": "#FAF8F5",
            "ivory-surface": "#F3EFEA",
            "surface": "#FAF8F5",
            "surface-bright": "#FFFFFF",
            "surface-container": "#EFEEEB",
            "surface-container-low": "#F5F3F0",
            "surface-container-high": "#EAE8E5",
            "surface-container-lowest": "#FFFFFF",
            "muted-slate": "#71717A",
            "primary": "#775a19",
            "primary-container": "#c5a059",
            "on-primary": "#ffffff"
          }},
          fontFamily: {{
            "display-hero": ["Playfair Display", "Georgia", "serif"],
            "title-editorial": ["Playfair Display", "Georgia", "serif"],
            "headline-lg": ["Playfair Display", "Georgia", "serif"],
            "headline-md": ["Playfair Display", "Georgia", "serif"],
            "headline-sm": ["Playfair Display", "Georgia", "serif"],
            "body-lg": ["Plus Jakarta Sans", "sans-serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"],
            "body-sm": ["Plus Jakarta Sans", "sans-serif"],
            "label-caps": ["Plus Jakarta Sans", "sans-serif"]
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="{root_prefix}assets/css/style.css" />
  {schema_script}
</head>
<body class="bg-surface font-body-md text-[#1b1c1a] antialiased selection:bg-champagne-gold selection:text-obsidian-deep min-h-screen flex flex-col">
"""

def render_header(active_slug="", root_prefix=""):
    nav_links = [
        ("Home", f"{root_prefix}index.html", ""),
        ("Services", f"{root_prefix}services/index.html", "services"),
        ("Hair", f"{root_prefix}hair-styling/index.html", "hair-styling"),
        ("Makeup & Bridal", f"{root_prefix}make-up/index.html", "make-up"),
        ("Skincare", f"{root_prefix}skin-care/index.html", "skin-care"),
        ("Packages", f"{root_prefix}packages/index.html", "packages"),
        ("Instagram & Gallery", f"{root_prefix}gallery/index.html", "gallery"),
        ("Academy", f"{root_prefix}academy/index.html", "academy"),
        ("About & Founder", f"{root_prefix}about-us/index.html", "about-us"),
        ("Blog", f"{root_prefix}blog/index.html", "blog"),
        ("Contact", f"{root_prefix}contact-us/index.html", "contact-us")
    ]

    links_html = ""
    for label, url, slug in nav_links:
        is_active = (active_slug == slug) or (slug == "" and active_slug == "home")
        active_cls = "text-champagne-gold font-bold" if is_active else "text-muted-slate hover:text-obsidian-deep"
        badge = ""
        if slug == "academy":
            badge = '<span class="ml-1 text-[9px] uppercase tracking-widest bg-champagne-gold/20 text-warm-bronze font-bold px-1.5 py-0.5 rounded">Govt Affiliated</span>'
        links_html += f'<a href="{url}" class="font-body-sm text-[12.5px] tracking-wide transition-colors flex items-center {active_cls}">{label}{badge}</a>\n'

    drawer_links_html = ""
    for label, url, slug in nav_links:
        is_active = (active_slug == slug) or (slug == "" and active_slug == "home")
        active_cls = "text-champagne-gold font-bold bg-obsidian-surface/60" if is_active else "text-alabaster-cream hover:text-champagne-gold"
        badge = ""
        if slug == "academy":
            badge = '<span class="ml-2 text-[9px] bg-champagne-gold text-obsidian-deep font-bold px-1.5 py-0.5 rounded">B&WSSC</span>'
        drawer_links_html += f'<a href="{url}" class="flex items-center justify-between px-4 py-3 rounded-lg text-sm tracking-wider uppercase {active_cls} transition-colors"><span>{label}</span>{badge}</a>\n'

    return f"""
<!-- Luxury Top Announcement Ticker -->
<div class="bg-obsidian-deep text-metallic-gold-light py-2 px-4 text-center font-label-caps text-[11px] tracking-widest flex items-center justify-center gap-2 border-b border-white/5 relative z-50">
  <span class="inline-block w-2 h-2 rounded-full bg-champagne-gold animate-pulse"></span>
  <span>Exclusive Atelier Offer: De-Tan + Skin Miracle Whitening Combo <strong>Rs. 2,499</strong> | Beautician Courses Affiliated with B&WSSC at <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="underline text-champagne-gold hover:text-white">LivArt Academy (livart.co.in)</a> | Call <a href="tel:{PHONE_TEL}" class="underline hover:text-white">{PHONE}</a></span>
</div>

<!-- Main Sticky Header -->
<header class="sticky top-0 w-full z-40 bg-surface/95 backdrop-blur-xl border-b border-black/5 transition-all duration-300">
  <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
    <!-- Brand Logo & Identity -->
    <a href="{root_prefix}index.html" class="flex items-center gap-3 shrink-0">
      <img src="{LOGO_URL}" alt="LivArt Salon and Makeup Studio Kakkanad" class="h-10 w-auto object-contain" />
      <div class="flex flex-col">
        <span class="font-serif-luxury text-xl font-bold tracking-tight text-obsidian-deep">LivArt</span>
        <span class="text-[9px] uppercase tracking-[0.25em] text-warm-bronze font-semibold -mt-0.5">Salon & Makeup Studio</span>
      </div>
    </a>

    <!-- Desktop Navigation Menu -->
    <nav class="hidden xl:flex items-center gap-4 2xl:gap-5">
      {links_html}
    </nav>

    <!-- Header Actions -->
    <div class="flex items-center gap-2.5 shrink-0">
      <a href="tel:{PHONE_TEL}" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold text-obsidian-deep hover:text-warm-bronze transition-colors px-3 py-1.5 rounded-md border border-black/10">
        <span class="material-symbols-outlined text-[16px] text-champagne-gold">call</span>
        <span>{PHONE}</span>
      </a>
      <a href="https://wa.me/917012059591?text=Hi%20LivArt%20Salon,%20I%20would%20like%20to%20inquire%20about%20your%20services" target="_blank" rel="noopener noreferrer" class="hidden md:inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 hover:bg-emerald-100 transition-colors px-3 py-1.5 rounded-md border border-emerald-200">
        <span class="material-symbols-outlined text-[16px] text-emerald-600">chat</span>
        <span>WhatsApp</span>
      </a>
      <button data-open-booking class="bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep px-3.5 py-2 rounded-lg font-label-caps text-[11px] font-bold tracking-widest uppercase transition-all shadow-md">
        Book Appointment
      </button>
      
      <!-- Mobile Menu Button -->
      <button id="mobile-menu-btn" class="xl:hidden p-2 text-obsidian-deep hover:text-champagne-gold focus:outline-none" aria-label="Open Navigation Menu">
        <span class="material-symbols-outlined text-[28px]">menu</span>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Navigation Drawer -->
<div id="mobile-backdrop" class="fixed inset-0 bg-black/60 z-50 hidden modal-backdrop transition-opacity"></div>
<div id="mobile-drawer" class="fixed top-0 right-0 w-[300px] sm:w-[360px] h-full bg-obsidian-deep text-alabaster-cream z-50 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col justify-between p-6">
  <div>
    <div class="flex items-center justify-between pb-6 border-b border-white/10">
      <div class="flex items-center gap-2">
        <img src="{LOGO_URL}" alt="LivArt Salon" class="h-8 w-auto brightness-0 invert" />
        <span class="font-serif-luxury text-lg font-bold text-champagne-gold">LivArt</span>
      </div>
      <button id="mobile-menu-close" class="p-1 text-muted-slate hover:text-alabaster-cream" aria-label="Close Menu">
        <span class="material-symbols-outlined text-[24px]">close</span>
      </button>
    </div>
    <div class="py-4 flex flex-col gap-1 overflow-y-auto max-h-[60vh]">
      {drawer_links_html}
    </div>
  </div>
  
  <div class="pt-6 border-t border-white/10 flex flex-col gap-3">
    <a href="tel:{PHONE_TEL}" class="flex items-center justify-center gap-2 py-2.5 rounded-lg border border-champagne-gold/30 text-champagne-gold text-xs font-semibold tracking-wider uppercase">
      <span class="material-symbols-outlined text-[16px]">call</span> Call +91 70120 59591
    </a>
    <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-2.5 rounded-lg border border-white/20 text-white text-xs font-semibold tracking-wider uppercase hover:border-champagne-gold hover:text-champagne-gold transition-colors">
      <span class="material-symbols-outlined text-[16px]">school</span> LivArt Academy (livart.co.in) ↗
    </a>
    <button data-open-booking class="w-full bg-champagne-gold text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase hover:bg-metallic-gold-light transition-all">
      Book Appointment
    </button>
  </div>
</div>
"""

def render_footer(root_prefix=""):
    return f"""
<!-- Global Luxury Footer -->
<footer class="w-full bg-obsidian-deep text-alabaster-cream pt-16 pb-12 border-t border-white/5 mt-auto">
  <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-white/10">
      <!-- Col 1: Brand -->
      <div class="flex flex-col gap-4 lg:col-span-1">
        <a href="{root_prefix}index.html" class="flex items-center gap-3">
          <img src="{LOGO_URL}" alt="LivArt Salon" class="h-9 w-auto brightness-0 invert" />
          <div class="flex flex-col">
            <span class="font-serif-luxury text-xl font-bold text-alabaster-cream tracking-tight">LivArt</span>
            <span class="text-[9px] uppercase tracking-[0.25em] text-champagne-gold">Kakkanad Atelier</span>
          </div>
        </a>
        <p class="text-xs text-muted-slate leading-relaxed">
          Haute couture aesthetics and bespoke beauty rituals curated by master artists in Kakkanad, Kochi. Co-founded by Stephy Sebastian and Nipun Conso.
        </p>
        <div class="flex items-center gap-3 pt-2">
          <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" class="w-9 h-9 rounded-full bg-obsidian-surface flex items-center justify-center text-metallic-gold-light hover:bg-champagne-gold hover:text-obsidian-deep transition-all" aria-label="LivArt Instagram">
            <span class="material-symbols-outlined text-[18px]">photo_camera</span>
          </a>
          <a href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" class="w-9 h-9 rounded-full bg-obsidian-surface flex items-center justify-center text-metallic-gold-light hover:bg-champagne-gold hover:text-obsidian-deep transition-all" aria-label="LivArt Facebook">
            <span class="material-symbols-outlined text-[18px]">share</span>
          </a>
          <a href="https://wa.me/917012059591" target="_blank" rel="noopener noreferrer" class="w-9 h-9 rounded-full bg-obsidian-surface flex items-center justify-center text-metallic-gold-light hover:bg-emerald-600 hover:text-white transition-all" aria-label="LivArt WhatsApp">
            <span class="material-symbols-outlined text-[18px]">chat</span>
          </a>
        </div>
      </div>

      <!-- Col 2: Services -->
      <div class="flex flex-col gap-3">
        <span class="font-serif-luxury text-base text-metallic-gold-light tracking-wide">Signature Services</span>
        <ul class="flex flex-col gap-2 text-xs text-muted-slate">
          <li><a href="{root_prefix}services/loreal-lustrous-hair-spa/index.html" class="hover:text-champagne-gold transition-colors">L'Oreal Lustrous Hair Spa (From Rs. 1,500)</a></li>
          <li><a href="{root_prefix}services/livart-majestic-keratin-treatment/index.html" class="hover:text-champagne-gold transition-colors">Livart Majestic Keratin Treatment</a></li>
          <li><a href="{root_prefix}services/livart-hair-straightening/index.html" class="hover:text-champagne-gold transition-colors">Permanent Hair Straightening</a></li>
          <li><a href="{root_prefix}services/loreal-glossy-hair-colouring/index.html" class="hover:text-champagne-gold transition-colors">L'Oreal Glossy Hair Colouring & Balayage</a></li>
          <li><a href="{root_prefix}services/skin-miracle-hydra-facial/index.html" class="hover:text-champagne-gold transition-colors">Skin Miracle Hydra Facial (Rs. 4,000)</a></li>
          <li><a href="{root_prefix}make-up/index.html" class="hover:text-champagne-gold transition-colors">Bridal & Groom Couture Packages</a></li>
        </ul>
      </div>

      <!-- Col 3: LivArt Beauty Academy (Affiliated with B&WSSC) -->
      <div class="flex flex-col gap-3">
        <div class="flex items-center gap-1.5">
          <span class="font-serif-luxury text-base text-metallic-gold-light tracking-wide">LivArt Academy</span>
          <span class="text-[9px] bg-champagne-gold text-obsidian-deep font-bold px-1.5 py-0.5 rounded tracking-widest uppercase">Govt Affiliated</span>
        </div>
        <p class="text-xs text-muted-slate leading-relaxed">
          Kerala's premier beauty academy offering Government-approved B&WSSC certified cosmetology courses mentored by Stephy Sebastian.
        </p>
        <ul class="flex flex-col gap-2 text-xs text-muted-slate">
          <li><a href="{root_prefix}academy/index.html" class="text-champagne-gold hover:text-white transition-colors font-medium flex items-center gap-1">Academy Overview Hub ↗</a></li>
          <li><a href="{ACADEMY_URL}/certification-course-in-cosmetology/" target="_blank" rel="noopener noreferrer" class="hover:text-champagne-gold transition-colors">Diploma in Cosmetology (livart.co.in) ↗</a></li>
          <li><a href="{ACADEMY_URL}/bridal-makeup-course/" target="_blank" rel="noopener noreferrer" class="hover:text-champagne-gold transition-colors">Professional Bridal Makeup (livart.co.in) ↗</a></li>
          <li><a href="{ACADEMY_URL}/hair-styling-course/" target="_blank" rel="noopener noreferrer" class="hover:text-champagne-gold transition-colors">Hair Styling & Haircuts Course ↗</a></li>
          <li><a href="{ACADEMY_URL}/skin-care-course/" target="_blank" rel="noopener noreferrer" class="hover:text-champagne-gold transition-colors">Skin Care & Aesthetics Course ↗</a></li>
          <li><a href="{ACADEMY_FOUNDER_URL}" target="_blank" rel="noopener noreferrer" class="hover:text-champagne-gold transition-colors">Founder Stephy Sebastian Bio ↗</a></li>
        </ul>
      </div>

      <!-- Col 4: Studio Sanctuary & Hours -->
      <div class="flex flex-col gap-3">
        <span class="font-serif-luxury text-base text-metallic-gold-light tracking-wide">Sanctuary & Hours</span>
        <div class="text-xs text-muted-slate leading-relaxed">
          <p class="text-alabaster-cream font-medium mb-1">Anchorage Business Center</p>
          <p>2nd Floor, Seaport-Airport Road, NGO Quarters – Mavelipuram Rd, Kakkanad, Kochi, Kerala 682030</p>
        </div>
        <div class="text-xs text-muted-slate pt-2">
          <p><span class="text-alabaster-cream font-medium">Mon – Sat:</span> 9:30 AM – 8:30 PM</p>
          <p><span class="text-alabaster-cream font-medium">Sunday:</span> 10:00 AM – 7:30 PM</p>
        </div>
      </div>

      <!-- Col 5: Direct Concierge -->
      <div class="flex flex-col gap-3">
        <span class="font-serif-luxury text-base text-metallic-gold-light tracking-wide">Direct Concierge</span>
        <p class="text-xs text-muted-slate leading-relaxed">
          Pre-book appointments with founder Stephy Sebastian or senior styling masters.
        </p>
        <div class="flex flex-col gap-1.5 pt-1 text-xs">
          <a href="tel:{PHONE_TEL}" class="text-champagne-gold hover:text-metallic-gold-light transition-colors font-semibold flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">call</span> {PHONE}
          </a>
          <a href="mailto:{EMAIL}" class="text-muted-slate hover:text-alabaster-cream transition-colors flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">mail</span> {EMAIL}
          </a>
        </div>
        <button data-open-booking class="mt-2 inline-flex items-center justify-center bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep py-2 px-4 rounded-lg font-label-caps text-[11px] font-bold tracking-widest uppercase transition-all shadow-md">
          Reserve Treatment
        </button>
      </div>
    </div>

    <!-- Copyright & Legal -->
    <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-muted-slate">
      <p>© 2026 {SITE_NAME}, Kakkanad, Kochi. All rights reserved.</p>
      <div class="flex flex-wrap items-center gap-4 sm:gap-6 font-label-caps text-[10px] tracking-wider uppercase">
        <a href="{root_prefix}services/index.html" class="hover:text-champagne-gold">All Services</a>
        <a href="{root_prefix}packages/index.html" class="hover:text-champagne-gold">Packages</a>
        <a href="{root_prefix}academy/index.html" class="text-champagne-gold hover:underline">Beauty Academy</a>
        <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="text-metallic-gold-light hover:underline">livart.co.in ↗</a>
        <a href="{root_prefix}gallery/index.html" class="hover:text-champagne-gold">Instagram Feed</a>
        <a href="{root_prefix}blog/index.html" class="hover:text-champagne-gold">Beauty Journal</a>
        <a href="{root_prefix}contact-us/index.html" class="hover:text-champagne-gold">Locate Us</a>
      </div>
    </div>
  </div>
</footer>

<!-- Interactive Booking Modal Component -->
<div id="booking-modal" class="fixed inset-0 bg-black/70 z-50 hidden modal-backdrop flex items-center justify-center p-4">
  <div class="bg-surface-container-lowest text-[#1b1c1a] w-full max-w-xl rounded-2xl shadow-2xl p-6 sm:p-8 relative max-h-[90vh] overflow-y-auto border border-champagne-gold/20">
    <button id="booking-modal-close" class="absolute top-5 right-5 text-muted-slate hover:text-obsidian-deep" aria-label="Close Booking Dialog">
      <span class="material-symbols-outlined text-[24px]">close</span>
    </button>
    
    <div class="mb-5">
      <span class="font-label-caps text-[11px] text-warm-bronze uppercase tracking-[0.2em] font-semibold block mb-1">LivArt Concierge</span>
      <h3 class="font-serif-luxury text-2xl text-obsidian-deep font-bold">Reserve Your Treatment</h3>
      <p class="text-xs text-muted-slate mt-1">Direct confirmation via WhatsApp and immediate concierge call.</p>
    </div>

    <form id="reservation-form" class="flex flex-col gap-4">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Full Name</label>
          <input type="text" id="book-name" required placeholder="e.g. Maya Kurian" class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
        </div>
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Phone Number</label>
          <input type="tel" id="book-phone" required placeholder="+91 98765 43210" class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
        </div>
      </div>

      <div>
        <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Select Service or Offer</label>
        <select id="book-service" class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5">
          <option value="De-Tan + Skin Miracle Whitening Combo (Rs. 2499)">De-Tan + Skin Miracle Whitening Combo (Rs. 2499)</option>
          <option value="Hair Colouring Artistry (From Rs. 5999)">Hair Colouring Artistry (From Rs. 5999)</option>
          <option value="Hair Botox Treatment (Rs. 5999)">Hair Botox Treatment (Rs. 5999)</option>
          <option value="Permanent Blow Dry (Rs. 5999)">Permanent Blow Dry (Rs. 5999)</option>
          <option value="Revitalizing Hair Spa (Rs. 1200)">Revitalizing Hair Spa (Rs. 1200, Reg. 1800)</option>
          <option value="Livart Majestic Keratin Treatment (From Rs. 5000)">Livart Majestic Keratin Treatment (From Rs. 5000)</option>
          <option value="Livart Permanent Hair Straightening (From Rs. 4000)">Livart Permanent Hair Straightening (From Rs. 4000)</option>
          <option value="Skin Miracle Hydra Facial (Rs. 4000)">Skin Miracle Hydra Facial (Rs. 4000)</option>
          <option value="Bridal Couture Silver/Gold/Diamond Package">Bridal Couture Silver/Gold/Diamond Package</option>
          <option value="Groom Black Diamond Package">Groom Black Diamond Package</option>
          <option value="Personal Consultation with Founder Stephy Sebastian">Personal Consultation with Founder Stephy Sebastian</option>
        </select>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Preferred Date</label>
          <input type="date" id="book-date" required class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
        </div>
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Time Slot</label>
          <select id="book-time" class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5">
            <option>Morning: 10:00 AM – 1:00 PM</option>
            <option>Afternoon: 1:00 PM – 4:30 PM</option>
            <option>Evening: 4:30 PM – 7:30 PM</option>
          </select>
        </div>
      </div>

      <div>
        <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Special Hair / Skin Notes (Optional)</label>
        <textarea id="book-notes" rows="2" placeholder="Mention any specific styling preferences, hair length, or allergies..." class="w-full px-3.5 py-2 text-sm bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5"></textarea>
      </div>

      <button type="submit" class="w-full bg-champagne-gold hover:bg-obsidian-deep text-obsidian-deep hover:text-alabaster-cream py-3 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase transition-all shadow-md mt-1">
        Confirm via WhatsApp & Concierge
      </button>

      <div id="booking-confirmation-msg" class="hidden p-3 bg-emerald-50 border border-emerald-200 text-emerald-800 rounded-lg text-xs text-center font-medium">
        Connecting to WhatsApp desk with your selected service details. A stylist will verify immediately!
      </div>
    </form>
  </div>
</div>

<!-- Reel / Look Preview Modal -->
<div id="reel-modal" class="fixed inset-0 bg-black/80 z-50 hidden modal-backdrop flex items-center justify-center p-4">
  <div class="bg-obsidian-surface text-alabaster-cream w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden border border-white/10 relative">
    <button id="reel-modal-close" class="absolute top-4 right-4 z-20 text-white/70 hover:text-white bg-black/40 rounded-full p-1.5 backdrop-blur-md">
      <span class="material-symbols-outlined text-[22px]">close</span>
    </button>
    <div class="relative w-full aspect-[4/5] bg-black">
      <img id="modal-reel-img" src="" alt="Look Preview" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep via-transparent to-transparent"></div>
      <div class="absolute top-4 left-4">
        <span id="modal-reel-tag" class="px-2.5 py-1 bg-obsidian-deep/80 text-champagne-gold text-[10px] font-bold uppercase tracking-widest rounded-full border border-champagne-gold/30"></span>
      </div>
      <div class="absolute bottom-4 left-4 right-4">
        <div class="flex items-center gap-2 text-xs text-metallic-gold-light mb-1">
          <span class="font-bold">@Livart_salon</span>
          <span class="material-symbols-outlined text-[14px] text-sky-400" style="font-variation-settings: 'FILL' 1;">verified</span>
        </div>
        <h4 id="modal-reel-title" class="font-serif-luxury text-lg font-bold text-white mb-1"></h4>
        <p id="modal-reel-caption" class="text-xs text-gray-300 leading-relaxed mb-3 line-clamp-3"></p>
        <div class="flex items-center justify-between pt-2 border-t border-white/10">
          <span id="modal-reel-likes" class="text-xs text-gray-400"></span>
          <button id="modal-reel-service-btn" onclick="closeReelModal(); openBookingModal(this.getAttribute('data-service'));" class="bg-champagne-gold text-obsidian-deep hover:bg-metallic-gold-light px-4 py-1.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
            Book This Look
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="{root_prefix}assets/js/main.js"></script>
<script src="{root_prefix}assets/js/instagram-feed.js"></script>
</body>
</html>
"""

print("Helper templates defined")
