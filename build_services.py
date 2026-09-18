import os
def ensure_dir(p): os.makedirs(p, exist_ok=True)
import os
import json
from generator import (
    BASE_DIR, SITE_NAME, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    render_head, render_header, render_footer
)

FAQS = [
    {
        "q": "What is the difference between a beauty salon and a beauty parlour?",
        "a": "The terms salon and parlour are often used interchangeably, but there is a distinct contrast. A salon usually offers a comprehensive, high-end range of services related to skin and hair care, advanced treatments, and relaxation in a luxury ambiance. A parlour traditionally focuses on specific routine treatments or basic beauty maintenance."
    },
    {
        "q": "What is a beauty parlour also known as?",
        "a": "A beauty parlour is commonly known as a beauty salon, hair salon, beauty lounge, or styling studio. 'Beauty salon' is the modern and internationally recognized term, whereas 'beauty parlour' is a more traditional term."
    },
    {
        "q": "How to start a parlour at home?",
        "a": "Starting a parlour requires addressing legal certifications and proper licenses, securing adequate equipment and sanitary accessories, determining specific services (waxing, facials, haircuts), creating a marketing identity, and maintaining a hygienic, customer-friendly environment."
    },
    {
        "q": "Is Hair Spa good for Hair?",
        "a": "Yes, a professional hair spa is exceptionally beneficial. It deeply nourishes the hair and scalp, stimulates healthy blood circulation, and repairs damaged hair fibers, leaving hair significantly softer, stronger, and shinier. Regular hair spa therapy also alleviates mental stress. We strongly advise scheduling a session at least once a month at LivArt Salon Kakkanad, where our stylists tailor treatment creams specifically to your scalp condition."
    },
    {
        "q": "What beauty service is most popular?",
        "a": "The popularity of beauty services depends on modern trends and seasonal needs. Highly demanded services include advanced skin facials (Hydra Facial, De-Tan), hair rejuvenation treatments (Keratin, Hair Botox, L'Oreal Hair Spa), precision haircuts, and bridal makeup artistry."
    },
    {
        "q": "Why are salon services important?",
        "a": "Personal grooming is essential for both men and women. In addition to enhancing aesthetic appearance, professional salon treatments maintain scalp and skin hygiene, restore cellular moisture, relieve physical stress, and dramatically boost self-confidence and body language."
    },
    {
        "q": "What is beauty parlour management?",
        "a": "Beauty parlour management involves the organized administration of salon operations, client scheduling, staff training, safety and hygiene compliance, inventory control, and marketing to ensure outstanding customer satisfaction."
    },
    {
        "q": "How to select the best Hairstyle that suits me?",
        "a": "Choosing the ideal hairstyle depends on facial structure, jawline, hair density, texture, and daily lifestyle. At LivArt Salon Kakkanad, our master stylists provide personalized consultations before every haircut, recommending cuts and coloring tones that enhance your natural facial contours."
    },
    {
        "q": "What is the brief description of the salon?",
        "a": "A salon is a destination for relaxation, wellness, and aesthetic beauty providing expert hair styling, coloring, facials, manicures, pedicures, and makeup application, leaving patrons revitalized, confident, and refreshed."
    },
    {
        "q": "What does a salon business do?",
        "a": "A salon business delivers professional grooming and therapeutic personal care services for hair, skin, and nails, combining high-grade cosmetic formulations with certified techniques to elevate clients' appearance and well-being."
    },
    {
        "q": "What all beauty services does Livart Salon Provide?",
        "a": "LivArt Salon Kakkanad offers hair styling, balayage, global colouring, keratin treatments, hair botox, permanent blow dry, hair straightening, deluxe manicure & pedicure, Hydra facials, de-tan whitening combos, waxing, threading, lash extensions, and signature bridal & groom packages."
    },
    {
        "q": "What is a parlour service?",
        "a": "A parlour service refers to professional cosmetic treatments—such as hair shaping, scalp massage, waxing, skin exfoliation, and nail maintenance—rendered in a dedicated beauty studio."
    },
    {
        "q": "What beauty services are most requested in Kakkanad & Kochi?",
        "a": "In Kakkanad and Kochi, clients frequently seek humidity-shield hair treatments (Hair Botox, Keratin), L'Oreal Hair Spa for scalp relaxation, De-Tan whitening facials to combat tropical sun exposure, and customized wedding bridal makeup."
    }
]

def build_services_page():
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            } for item in FAQS
        ]
    }

    html = render_head(
        title="Best Salon & Beauty Parlour Services in Kakkanad, Kochi | LivArt",
        description="Complete salon service price menu at LivArt Kakkanad: Keratin smoothing, hair botox, bridal makeup, L'Oreal hair spa, Hydra facials & hair colouring near Infopark.",
        canonical_path="/services/",
        extra_schema=faq_schema,
        root_prefix="../"
    )

    html += render_header(active_slug="services", root_prefix="../")

    faq_items_html = ""
    for idx, item in enumerate(FAQS):
        faq_items_html += f"""
        <details class="faq-item group bg-surface-container-low rounded-xl p-5 border border-black/5 transition-all">
          <summary class="flex items-center justify-between cursor-pointer font-serif-luxury text-lg font-bold text-obsidian-deep list-none select-none">
            <span>{idx + 1}. {item['q']}</span>
            <span class="faq-icon material-symbols-outlined text-warm-bronze transition-transform duration-300">expand_more</span>
          </summary>
          <div class="mt-4 pt-4 border-t border-black/5 text-sm text-gray-700 leading-relaxed">
            {item['a']}
          </div>
        </details>
        """

    html += f"""
<main class="flex-grow">
  <!-- Page Hero Header -->
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
        Artisanal Beauty Sanctuary • Kakkanad, Kochi
      </span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">
        Best Salon & Beauty Parlour Services in Kakkanad, Kochi
      </h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Welcome to LivArt Salon, your premier destination for luxury hair design, rejuvenating treatments, and radiant skincare on Seaport-Airport Road. Curated by master stylists with international experience.
      </p>
    </div>
  </section>

  <!-- 5 Signature Services Grid -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl mb-12">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">
          Signature Treatments
        </span>
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">
          Our Most Demanded Rejuvenation Rituals
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Service 1: Keratin -->
        <div class="bg-surface-container-low rounded-2xl p-7 border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-2.5 py-1 rounded-full">Hair Smoothing</span>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep">From Rs. 5,000</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Livart Majestic Keratin Treatment</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-6">
              A luxurious and rejuvenating experience that transforms unruly hair into silky-smooth, frizz-free tresses that stay lustrous through humid Kerala weather.
            </p>
          </div>
          <div class="flex items-center justify-between pt-4 border-t border-black/5">
            <a href="livart-majestic-keratin-treatment/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze uppercase tracking-wider flex items-center gap-1">
              <span>View Details</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
            <button data-open-booking data-service="Livart Majestic Keratin Treatment (From Rs. 5000)" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-4 py-2 rounded-lg text-xs font-bold tracking-wider uppercase transition-all">
              Book
            </button>
          </div>
        </div>

        <!-- Service 2: Hair Straightening -->
        <div class="bg-surface-container-low rounded-2xl p-7 border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-2.5 py-1 rounded-full">Thermal Rebonding</span>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep">From Rs. 4,000</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Livart Hair Straightening</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-6">
              Experience the magic of permanent hair straightening, designed to deliver sleek, stylish, pin-straight manageability while safeguarding natural moisture.
            </p>
          </div>
          <div class="flex items-center justify-between pt-4 border-t border-black/5">
            <a href="livart-hair-straightening/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze uppercase tracking-wider flex items-center gap-1">
              <span>View Details</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
            <button data-open-booking data-service="Livart Permanent Hair Straightening (From Rs. 4000)" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-4 py-2 rounded-lg text-xs font-bold tracking-wider uppercase transition-all">
              Book
            </button>
          </div>
        </div>

        <!-- Service 3: Hair Colouring -->
        <div class="bg-surface-container-low rounded-2xl p-7 border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-2.5 py-1 rounded-full">Balayage & Tint</span>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep">From Rs. 3,000</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">L’Oreal Glossy Hair Colouring</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-6">
              Indulge in vibrant multidimensional shades. Skilled color masters formulate ammonia-free L'Oreal palettes from caramel balayage to rich mocha tones.
            </p>
          </div>
          <div class="flex items-center justify-between pt-4 border-t border-black/5">
            <a href="loreal-glossy-hair-colouring/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze uppercase tracking-wider flex items-center gap-1">
              <span>View Details</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
            <button data-open-booking data-service="L'Oreal Glossy Hair Colouring (From Rs. 3000)" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-4 py-2 rounded-lg text-xs font-bold tracking-wider uppercase transition-all">
              Book
            </button>
          </div>
        </div>

        <!-- Service 4: Hair Spa -->
        <div class="bg-surface-container-low rounded-2xl p-7 border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-2.5 py-1 rounded-full">Scalp Therapy</span>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep">From Rs. 1,500</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">L’Oreal Lustrous Hair Spa</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-6">
              Treat your hair to the ultimate nourishment. A deeply hydrating steam therapy and acupressure scalp massage that revitalizes follicles and restores shine.
            </p>
          </div>
          <div class="flex items-center justify-between pt-4 border-t border-black/5">
            <a href="loreal-lustrous-hair-spa/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze uppercase tracking-wider flex items-center gap-1">
              <span>View Details</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
            <button data-open-booking data-service="Revitalizing Hair Spa (Rs. 1200)" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-4 py-2 rounded-lg text-xs font-bold tracking-wider uppercase transition-all">
              Book
            </button>
          </div>
        </div>

        <!-- Service 5: Hydra Facial -->
        <div class="bg-surface-container-low rounded-2xl p-7 border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-2.5 py-1 rounded-full">Clinical Skincare</span>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep">Rs. 4,000</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Skin Miracle Hydra Facial</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-6">
              For radiant, glass-like skin: a deeply purifying vortex-infusion treatment extracting clogged impurities while saturating the dermis in hyaluronic serums.
            </p>
          </div>
          <div class="flex items-center justify-between pt-4 border-t border-black/5">
            <a href="skin-miracle-hydra-facial/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze uppercase tracking-wider flex items-center gap-1">
              <span>View Details</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
            <button data-open-booking data-service="Skin Miracle Hydra Facial (Rs. 4000)" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-4 py-2 rounded-lg text-xs font-bold tracking-wider uppercase transition-all">
              Book
            </button>
          </div>
        </div>

        <!-- Callout: View Full Menu -->
        <div class="bg-obsidian-deep text-alabaster-cream rounded-2xl p-7 border border-white/10 shadow-xl flex flex-col justify-between">
          <div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block mb-2">Complete Catalog</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-white mb-2">Looking for More Services?</h3>
            <p class="text-xs text-gray-300 leading-relaxed mb-6">
              Explore our dedicated sections for haircuts & styling, bridal couture packages, and clinical skincare rituals.
            </p>
          </div>
          <div class="flex flex-col gap-2">
            <a href="../hair-styling/index.html" class="text-xs text-metallic-gold-light hover:underline flex items-center justify-between py-1.5 border-b border-white/10">
              <span>Haircuts & Blowouts</span> <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
            </a>
            <a href="../make-up/index.html" class="text-xs text-metallic-gold-light hover:underline flex items-center justify-between py-1.5 border-b border-white/10">
              <span>Bridal & Groom Makeup</span> <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
            </a>
            <a href="../skin-care/index.html" class="text-xs text-metallic-gold-light hover:underline flex items-center justify-between py-1.5">
              <span>Skincare & Facials</span> <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- COMPLETE ATELIER SERVICE DIRECTORY & PRICE MENU (POWERED BY ZYLU) -->
  <section class="py-20 bg-obsidian-deep text-alabaster-cream" id="catalog">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-10">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-champagne-gold/10 border border-champagne-gold/30 text-champagne-gold text-[10px] font-bold uppercase tracking-widest mb-3">
          <span class="material-symbols-outlined text-[14px]">verified</span>
          <span>Official 2026 Atelier Rate Card • 234 Verified Services</span>
        </div>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
          Complete Salon Menu & Transparent Pricing
        </h2>
        <p class="text-sm sm:text-base text-gray-300 leading-relaxed">
          Browse our entire bespoke service catalog directly synced with our appointment desk. Instant online booking, clear durations, and exclusive privilege card discounts up to 25% OFF.
        </p>
      </div>

      <!-- Controls & Filter Dashboard -->
      <div class="bg-obsidian-surface rounded-3xl p-5 sm:p-7 border border-white/10 shadow-2xl mb-10">
        <!-- Top Row: Search Bar & Privilege Toggle -->
        <div class="flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-4 pb-6 border-b border-white/10">
          
          <!-- Search Bar -->
          <div class="relative flex-1">
            <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-champagne-gold text-[20px]">search</span>
            <input 
              id="services-search-input" 
              type="text" 
              oninput="window.onSearchServices(this.value)" 
              placeholder="Search by treatment (e.g. Hair Botox, Balayage, Hydra Facial, Beard, Layers)..." 
              class="w-full bg-black/40 border border-white/15 focus:border-champagne-gold rounded-xl pl-11 pr-10 py-3 text-sm text-white placeholder:text-gray-500 focus:outline-none transition-all"
            />
            <button onclick="window.resetServiceFilters()" class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white p-1 text-xs" title="Clear Search">
              ✕
            </button>
          </div>

          <!-- Member Pricing Toggle -->
          <div class="flex items-center justify-between sm:justify-end gap-3 bg-black/30 border border-white/10 rounded-2xl px-4 py-2.5 shrink-0">
            <div class="flex flex-col text-left">
              <span class="text-xs font-bold text-white flex items-center gap-1">
                <span class="material-symbols-outlined text-[15px] text-champagne-gold">card_membership</span>
                <span>Grand Privilege Card</span>
              </span>
              <span id="member-pricing-badge" class="text-[10px] text-champagne-gold font-medium">
                Show Privilege Rates (25% OFF)
              </span>
            </div>
            
            <button 
              id="member-pricing-toggle" 
              onclick="window.toggleMemberPricing()" 
              type="button" 
              class="relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent bg-gray-700 transition-colors duration-200 ease-in-out focus:outline-none" 
              role="switch" 
              aria-checked="false">
              <span class="toggle-dot pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out translate-x-0"></span>
            </button>
          </div>
        </div>

        <!-- Middle Row: Category Tabs (Horizontal scroll on mobile) -->
        <div class="pt-5 pb-3">
          <span class="text-[10px] font-bold uppercase tracking-widest text-gray-400 block mb-2.5">Filter by Service Category:</span>
          <div class="flex items-center gap-2 overflow-x-auto pb-2 touch-scroll no-scrollbar">
            <button onclick="window.setServiceTab('all')" data-tab="all" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-champagne-gold text-obsidian-deep min-h-[38px]">
              All Services (234)
            </button>
            <button onclick="window.setServiceTab('haircuts')" data-tab="haircuts" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Haircuts & Trims
            </button>
            <button onclick="window.setServiceTab('hair-color')" data-tab="hair-color" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Color & Balayage
            </button>
            <button onclick="window.setServiceTab('hair-treatments')" data-tab="hair-treatments" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Botox & Keratin
            </button>
            <button onclick="window.setServiceTab('hair-styling')" data-tab="hair-styling" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Styling & Blowout
            </button>
            <button onclick="window.setServiceTab('skincare-facials')" data-tab="skincare-facials" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Facials & Skincare
            </button>
            <button onclick="window.setServiceTab('bridal-makeup')" data-tab="bridal-makeup" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Bridal & Makeup
            </button>
            <button onclick="window.setServiceTab('manicure-pedicure')" data-tab="manicure-pedicure" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Mani, Pedi & Nails
            </button>
            <button onclick="window.setServiceTab('waxing-threading')" data-tab="waxing-threading" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Waxing & Threading
            </button>
            <button onclick="window.setServiceTab('mens-grooming')" data-tab="mens-grooming" class="service-tab-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[38px]">
              Beard & Men
            </button>
          </div>
        </div>

        <!-- Bottom Row: Gender Filters & Active Count -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pt-3 border-t border-white/10 text-xs">
          <div class="flex items-center gap-2">
            <span class="text-gray-400 font-medium">Guest:</span>
            <div class="inline-flex rounded-lg bg-black/40 p-0.5 border border-white/10">
              <button onclick="window.setServiceGender('all')" data-gender="all" class="service-gender-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-champagne-gold text-obsidian-deep transition-all">All</button>
              <button onclick="window.setServiceGender('Female')" data-gender="Female" class="service-gender-btn px-2.5 py-1 rounded-md text-[11px] font-medium text-gray-400 hover:text-white transition-all">Women</button>
              <button onclick="window.setServiceGender('Male')" data-gender="Male" class="service-gender-btn px-2.5 py-1 rounded-md text-[11px] font-medium text-gray-400 hover:text-white transition-all">Men</button>
              <button onclick="window.setServiceGender('Kids')" data-gender="Kids" class="service-gender-btn px-2.5 py-1 rounded-md text-[11px] font-medium text-gray-400 hover:text-white transition-all">Kids</button>
            </div>
          </div>

          <div class="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-end">
            <span id="services-count-display" class="text-gray-400 font-medium text-[11px]">
              Loading services...
            </span>
            <a href="https://store.zylu.co/livart-salon-kakkanad" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-[11px] font-bold text-champagne-gold hover:underline">
              <span>Direct Zylu Booking</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Services Grid (Populated via assets/js/services-catalog.js) -->
      <div id="services-catalog-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
        <!-- Injected via JS -->
      </div>

      <!-- Load More / Expand Bar -->
      <div id="services-load-more-container" class="mt-12 text-center w-full flex justify-center">
        <!-- Injected via JS -->
      </div>

      <!-- Zylu Online Booking Notice Banner -->
      <div class="mt-16 p-6 sm:p-8 bg-gradient-to-r from-obsidian-surface via-obsidian-deep to-obsidian-surface rounded-3xl border border-champagne-gold/30 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="flex items-center gap-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-champagne-gold/20 border border-champagne-gold/40 flex items-center justify-center shrink-0 text-champagne-gold">
            <span class="material-symbols-outlined text-[24px]">calendar_month</span>
          </div>
          <div>
            <h4 class="font-serif-luxury text-lg font-bold text-white mb-0.5">
              Live Real-Time Salon Scheduling via Zylu Store
            </h4>
            <p class="text-xs text-gray-300 leading-relaxed max-w-xl">
              Book your preferred stylist, pick exact time slots, and explore authentic real-time availability at our Anchorage Business Centre studio.
            </p>
          </div>
        </div>
        <div class="flex flex-wrap items-center gap-3 shrink-0 w-full md:w-auto justify-center">
          <a href="https://store.zylu.co/livart-salon-kakkanad" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto bg-champagne-gold hover:bg-white active:scale-95 text-obsidian-deep px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all shadow-md flex items-center justify-center gap-2">
            <span>Book on Zylu Store</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
          <a href="https://wa.me/917012059591?text=Hi%20LivArt%20Salon,%20I%20would%20like%20to%20inquire%20about%20your%20services" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-300 px-5 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center justify-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">chat</span>
            <span>WhatsApp Desk</span>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 13-QUESTION FAQ SECTION (HIGH-LEVERAGE SEO ASSET) -->
  <section class="py-20 bg-ivory-surface" id="faq">
    <div class="max-w-[1000px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-bold block mb-2">
          Knowledge Base & Client Guide
        </span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-obsidian-deep font-bold mb-4">
          Frequently Asked Questions (FAQ)
        </h2>
        <p class="text-sm text-gray-600 max-w-xl mx-auto">
          Everything you need to know about our salon treatments, hair spa therapy, hygiene standards, and beauty styling in Kakkanad, Kochi.
        </p>
      </div>

      <div class="space-y-4">
        {faq_items_html}
      </div>

      <div class="mt-12 p-8 bg-obsidian-deep text-alabaster-cream rounded-2xl text-center">
        <h3 class="font-serif-luxury text-2xl font-bold mb-2">Have a Custom Beauty or Bridal Inquiry?</h3>
        <p class="text-xs text-gray-300 max-w-lg mx-auto mb-6">
          Our styling director Stephy Sebastian and senior team offer individualized hair and skin consultations at our Kakkanad studio.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <button data-open-booking class="bg-champagne-gold text-obsidian-deep px-6 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider hover:bg-metallic-gold-light transition-all">
            Schedule Free Consultation
          </button>
          <a href="tel:{PHONE_TEL}" class="border border-white/20 text-white px-6 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider hover:bg-white/10 transition-all flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">call</span> Call {PHONE}
          </a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../", extra_scripts='<script src="../assets/js/services-catalog.js"></script>')

    with open(os.path.join(BASE_DIR, "services", "index.html"), "w") as f:
        f.write(html)
    print("✓ services/index.html built with 13 FAQs and FAQPage Schema")

# -------------------------------------------------------------
# 2. SUB-SERVICE RE-RANKING LANDING PAGES
# -------------------------------------------------------------
def build_sub_services():
    sub_pages = [
        {
            "slug": "loreal-lustrous-hair-spa",
            "title": "Hair Spa in Kakkanad | L'Oreal Scalp Therapy & Relaxo Massage | LivArt Salon",
            "desc": "Best hair spa in Kakkanad, Kochi. L'Oreal professional scalp therapy, steam deep-hydration & acupressure massage at LivArt Salon near Infopark from Rs. 1,200.",
            "heading": "L’Oreal Lustrous Hair Spa Scalp Therapy",
            "price": "From Rs. 1,500 (Offer: Rs. 1,200)",
            "category": "Scalp & Hair Health",
            "img": "../../assets/images/instagram/DEXOFvGTyDZ.jpg",
            "body": """
            <p class="text-base text-gray-700 leading-relaxed mb-4">
              Is your hair feeling brittle, lifeless, or stressed from Kochi’s tropical humidity and hard water? The <strong>L’Oreal Lustrous Hair Spa</strong> at LivArt Salon Kakkanad is engineered to provide intensive nourishment straight to your follicles, revitalizing dull strands and repairing deep environmental damage.
            </p>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">Why Choose LivArt's L'Oreal Hair Spa?</h3>
            <ul class="list-disc pl-5 space-y-2 text-sm text-gray-700 mb-6">
              <li><strong>Deep Cellular Moisture:</strong> Infuses concentrated botanical liposomes into the hair cuticle, sealing in long-lasting hydration.</li>
              <li><strong>Therapeutic Acupressure Scalp Massage:</strong> Stimulates micro-capillary blood circulation to boost natural hair growth and relieve mental fatigue.</li>
              <li><strong>Humidity Defense:</strong> Creates a protective lipid sheath preventing frizzy flyaways in coastal Kerala weather.</li>
              <li><strong>Stress Relief:</strong> A multi-sensory warm steam ritual accompanied by calming essential oils in our private salon lounge.</li>
            </ul>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">Recommended Frequency</h3>
            <p class="text-sm text-gray-700 leading-relaxed mb-4">
              We strongly advise scheduling a professional hair spa treatment at least once every 3 to 4 weeks. Our trained stylists diagnose your scalp condition—whether dry, sensitive, oily, or prone to dandruff—to customize your L'Oreal spa treatment cream.
            </p>
            """
        },
        {
            "slug": "livart-majestic-keratin-treatment",
            "title": "Keratin Treatment in Kakkanad, Kochi | Anti-Frizz Smoothing | LivArt Salon",
            "desc": "Eliminate frizzy hair with Livart Majestic Keratin Treatment in Kakkanad, Kochi. Formaldehyde-safe, mirror gloss and humidity-proof smoothness from Rs. 5,000.",
            "heading": "Livart Majestic Keratin Smoothing Treatment",
            "price": "From Rs. 5,000",
            "category": "Hair Smoothing & Restoration",
            "img": "../../assets/images/instagram/C5pwjmOidQU.jpg",
            "body": """
            <p class="text-base text-gray-700 leading-relaxed mb-4">
              The <strong>Livart Majestic Keratin Treatment</strong> is our flagship hair smoothing therapy, formulated to tame unruly textures, eliminate 95% of frizz, and give you effortless runway-sleek hair every single morning.
            </p>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">How the Majestic Keratin Works</h3>
            <p class="text-sm text-gray-700 leading-relaxed mb-4">
              Micro-keratin proteins are thermally sealed into compromised hair shafts, restoring structural elasticity and sealing the outer cuticle. The result is hair that feels feather-soft, highly reflective, and completely immune to frizz even on rainy or humid days.
            </p>
            <ul class="list-disc pl-5 space-y-2 text-sm text-gray-700 mb-6">
              <li>Lasts 4 to 6 months with sulfate-free aftercare.</li>
              <li>Reduces daily blow-drying and styling time by 70%.</li>
              <li>Safe on previously colored, highlighted, or chemically processed hair.</li>
            </ul>
            """
        },
        {
            "slug": "livart-hair-straightening",
            "title": "Permanent Hair Straightening & Rebonding in Kakkanad | LivArt Salon Kochi",
            "desc": "Permanent hair straightening and rebonding at LivArt Salon Kakkanad. Expert stylists and nourishing silk amino formulations for sleek hair from Rs. 4,000.",
            "heading": "Livart Permanent Hair Straightening & Rebonding",
            "price": "From Rs. 4,000",
            "category": "Thermal Rebonding",
            "img": "../../assets/images/instagram/Db7rJBtuj4B.jpg",
            "body": """
            <p class="text-base text-gray-700 leading-relaxed mb-4">
              For those seeking pin-straight, ultra-sleek, and impeccably aligned locks, <strong>Livart Hair Straightening</strong> delivers permanent, silky transformations that stay smooth permanently until natural roots grow out.
            </p>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">Precision Stylist Artistry</h3>
            <p class="text-sm text-gray-700 leading-relaxed mb-4">
              Straightening requires expert mastery to ensure hair bonds are softened and restructured without heat damage. At LivArt Kakkanad, our senior stylists perform thorough strand testing and use deeply nourishing neutralizers with silk amino acids to keep hair healthy and lustrous.
            </p>
            """
        },
        {
            "slug": "loreal-glossy-hair-colouring",
            "title": "Balayage & Hair Colouring Salon in Kakkanad, Kochi | L'Oreal | LivArt",
            "desc": "Top-rated hair colouring salon in Kakkanad. Seamless balayage, caramel highlights, and global hair colour with ammonia-free L'Oreal palettes from Rs. 3,000.",
            "heading": "L’Oreal Glossy Hair Colouring & Dimensional Balayage",
            "price": "From Rs. 3,000 (Balayage from Rs. 5,999)",
            "category": "Couture Hair Colouring",
            "img": "../../assets/images/instagram/DABMk4mtv8b.jpg",
            "body": """
            <p class="text-base text-gray-700 leading-relaxed mb-4">
              Transform your look with <strong>L’Oreal Glossy Hair Colouring</strong> at LivArt Kakkanad. Whether you desire subtle warm caramel babylights, dramatic honey-blonde balayage, or rich mocha global coverage, our certified colorists hand-paint dimensions tailored to your skin undertones.
            </p>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">Zero Ammonia, Maximum Gloss</h3>
            <p class="text-sm text-gray-700 leading-relaxed mb-4">
              We prioritize the long-term integrity of your hair. We utilize L'Oreal Inoa and Majirel lines enriched with protective Ionène G and Incell to ensure vibrant, fade-resistant color with a luminous, reflective mirror sheen.
            </p>
            """
        },
        {
            "slug": "skin-miracle-hydra-facial",
            "title": "Hydra Facial in Kakkanad, Kochi | Skin Miracle Dermal Aesthetics | LivArt",
            "desc": "Experience medical-grade Hydra Facial in Kakkanad at LivArt Salon. Painless vortex pore extraction, hyaluronic hydration, and bridal glass-skin glow for Rs. 4,000.",
            "heading": "Skin Miracle Hydra Facial Aesthetics",
            "price": "Rs. 4,000",
            "category": "Clinical Dermal Aesthetics",
            "img": "../../assets/images/instagram/DRXFRQCEgpm.jpg",
            "body": """
            <p class="text-base text-gray-700 leading-relaxed mb-4">
              The <strong>Skin Miracle Hydra Facial</strong> is an advanced clinical aesthetic treatment that cleanses, exfoliates, extracts impurities, and hydrates the skin simultaneously using vortex suction and specialized peptide serums.
            </p>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mt-6 mb-3">The 4-Step Hydra Radiance Process</h3>
            <ul class="list-disc pl-5 space-y-2 text-sm text-gray-700 mb-6">
              <li><strong>Step 1: Vortex Cleansing:</strong> Gently washes away sebum and environmental debris.</li>
              <li><strong>Step 2: Gentle Acid Peel:</strong> Loosens stubborn dead dermal cells without redness or irritation.</li>
              <li><strong>Step 3: Vacuum Extraction:</strong> Painlessly unclogs blackheads and deep pores.</li>
              <li><strong>Step 4: Hyaluronic Serum Infusion:</strong> Floods the skin with potent antioxidants, peptides, and deep moisture for an unmistakable bridal glow.</li>
            </ul>
            """
        }
    ]

    for p in sub_pages:
        dir_path = os.path.join(BASE_DIR, "services", p["slug"])
        ensure_dir(dir_path)

        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": "Services", "item": BASE_URL + "/services/"},
                {"@type": "ListItem", "position": 3, "name": p["heading"], "item": f"{BASE_URL}/services/{p['slug']}/"}
            ]
        }

        og_img = p["img"].replace("../../", f"{BASE_URL}/")
        html = render_head(
            title=p["title"],
            description=p["desc"],
            canonical_path=f"/services/{p['slug']}/",
            extra_schema=breadcrumb_schema,
            root_prefix="../../",
            og_image=og_img
        )
        html += render_header(active_slug="services", root_prefix="../../")

        html += f"""
<main class="flex-grow">
  <!-- Breadcrumb Bar -->
  <div class="bg-surface-container py-3 border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-xs text-muted-slate flex items-center gap-2">
      <a href="../../index.html" class="hover:text-obsidian-deep">Home</a>
      <span>/</span>
      <a href="../index.html" class="hover:text-obsidian-deep">Services</a>
      <span>/</span>
      <span class="text-obsidian-deep font-semibold">{p['heading']}</span>
    </div>
  </div>

  <!-- Hero Header -->
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1100px] mx-auto px-4 sm:px-6 lg:px-8">
      <span class="text-xs font-bold uppercase tracking-widest text-champagne-gold block mb-2">{p['category']}</span>
      <h1 class="font-serif-luxury text-3xl sm:text-5xl font-bold text-alabaster-cream mb-4">{p['heading']}</h1>
      <div class="flex flex-wrap items-center gap-4 text-sm text-metallic-gold-light">
        <span class="font-serif-luxury text-xl font-bold text-champagne-gold">{p['price']}</span>
        <span>•</span>
        <span>Kakkanad, Kochi Studio</span>
        <span>•</span>
        <span>Certified Master Stylists</span>
      </div>
    </div>
  </section>

  <!-- Service Detail Body -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1100px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <!-- Content Left -->
        <div class="lg:col-span-8">
          <div class="rounded-2xl overflow-hidden shadow-lg mb-8 max-h-[420px] bg-obsidian-deep">
            <img src="{p['img']}" alt="{p['heading']} at LivArt Salon Kakkanad" class="w-full h-full object-cover" loading="lazy" />
          </div>

          <div class="prose max-w-none text-gray-800">
            {p['body']}
          </div>

          <!-- Bottom CTA Box -->
          <div class="mt-10 p-6 bg-gold-gradient rounded-2xl text-obsidian-deep flex flex-col sm:flex-row items-center justify-between gap-4 shadow-md">
            <div>
              <h4 class="font-serif-luxury text-xl font-bold mb-1">Ready for Your Transformation?</h4>
              <p class="text-xs font-medium text-black/80">Book with Stephy Sebastian and our senior stylists at Kakkanad.</p>
            </div>
            <button data-open-booking data-service="{p['heading']}" class="bg-obsidian-deep hover:bg-obsidian-surface text-alabaster-cream px-6 py-3 rounded-lg text-xs font-bold uppercase tracking-widest transition-all shrink-0">
              Book Appointment
            </button>
          </div>
        </div>

        <!-- Sidebar Right -->
        <div class="lg:col-span-4 flex flex-col gap-6">
          <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5 shadow-sm">
            <h3 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-4 pb-2 border-b border-black/5">Quick Reservation</h3>
            <p class="text-xs text-muted-slate mb-4">Direct WhatsApp & Concierge Desk with fast slot confirmation.</p>
            
            <button data-open-booking data-service="{p['heading']}" class="w-full bg-champagne-gold hover:bg-obsidian-deep text-obsidian-deep hover:text-white py-3 rounded-lg text-xs font-bold uppercase tracking-widest transition-all mb-3 shadow-sm">
              Reserve Online
            </button>
            <a href="tel:{PHONE_TEL}" class="w-full flex items-center justify-center gap-2 border border-black/10 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-obsidian-deep hover:bg-black/5 transition-all">
              <span class="material-symbols-outlined text-[16px]">call</span> Call {PHONE}
            </a>
          </div>

          <div class="bg-obsidian-deep text-alabaster-cream p-6 rounded-2xl shadow-xl">
            <span class="text-[10px] uppercase font-bold tracking-widest text-champagne-gold block mb-2">Location & Studio</span>
            <p class="text-xs font-medium text-white mb-2">Anchorage Business Center</p>
            <p class="text-xs text-muted-slate leading-relaxed mb-4">2nd Floor, Seaport-Airport Road, NGO Quarters – Mavelipuram Rd, Kakkanad, Kochi</p>
            <div class="text-xs text-muted-slate border-t border-white/10 pt-3">
              <p><strong class="text-white">Hours:</strong> Mon–Sat: 9:30 AM – 8:30 PM</p>
              <p>Sunday: 10:00 AM – 7:30 PM</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
"""
        html += render_footer(root_prefix="../../")

        with open(os.path.join(dir_path, "index.html"), "w") as f:
            f.write(html)
        print(f"✓ services/{p['slug']}/index.html built")

if __name__ == "__main__":
    build_services_page()
    build_sub_services()
