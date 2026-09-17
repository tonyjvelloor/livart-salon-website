import os
import json

from generator import (
    BASE_DIR, SITE_NAME, SITE_TAGLINE, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    INSTAGRAM_HANDLE, INSTAGRAM_URL, FACEBOOK_URL, LOGO_URL,
    ACADEMY_PHONE, ACADEMY_PHONE_TEL,
    render_head, render_header, render_footer
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# -------------------------------------------------------------
# 1. HOMEPAGE GENERATION
# -------------------------------------------------------------
def build_homepage():
    extra_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "url": BASE_URL,
        "name": SITE_NAME,
        "description": "Premier Destination Hair & Makeup Studio in Kakkanad, Kochi curated by World Class Stylists."
    }
    
    html = render_head(
        title="LivArt Salon & Make-up Studio | Best Beauty Parlour in Kakkanad, Kochi",
        description="LivArt Salon Kakkanad offers bespoke hair styling, bridal makeup, L'Oreal hair colouring & luxury skincare by Stephy Sebastian. Book your experience.",
        canonical_path="/",
        extra_schema=extra_schema
    )
    
    html += render_header(active_slug="home")
    
    html += f"""
<main class="flex-grow">
  <!-- HERO SANCTUARY -->
  <section class="relative w-full bg-obsidian-deep text-alabaster-cream pt-16 pb-20 overflow-hidden">
    <div class="absolute -top-32 -left-32 w-96 h-96 rounded-full bg-champagne-gold/10 blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 -right-48 w-[500px] h-[500px] rounded-full bg-warm-bronze/10 blur-3xl pointer-events-none"></div>
    
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Micro-Badge Row -->
      <div class="flex flex-wrap items-center gap-2 mb-6">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-obsidian-surface rounded-full text-champagne-gold text-[11px] font-bold tracking-widest uppercase border border-champagne-gold/20">
          <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
          4.9 Google Rated Sanctuary • Kakkanad, Kochi
        </span>
        <span class="hidden sm:inline text-muted-slate">•</span>
        <span class="text-metallic-gold-light text-xs tracking-wider">Bespoke Atelier for Haute Couture Hair, Makeup & Aesthetics</span>
      </div>

      <!-- Hero Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Left Column -->
        <div class="lg:col-span-7 flex flex-col items-start">
          <p class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase mb-2 font-semibold">
            Discover Kakkanad’s Premier Destination Salon
          </p>
          <h1 class="font-serif-luxury text-4xl sm:text-5xl lg:text-6xl text-alabaster-cream leading-[1.15] mb-6 font-normal">
            The Art of Radiant Hair <br class="hidden sm:inline" />
            <span class="italic text-gold-gradient">and Flawless Glamour.</span>
          </h1>
          <p class="text-base sm:text-lg text-gray-300 max-w-xl mb-6 leading-relaxed">
            LivArt Salon & Make Up Studio curates bespoke beauty rituals led by world-class stylists. Experience transformative hair coloring, radiant skincare therapies, and unforgettable bridal aesthetics crafted in an atmosphere of serene luxury.
          </p>

          <!-- Founder Quote -->
          <div class="bg-obsidian-surface/90 border-l-2 border-champagne-gold p-4 sm:p-5 rounded-r-xl mb-8 max-w-xl shadow-lg">
            <p class="font-serif-luxury text-base sm:text-lg text-alabaster-cream italic">
              “We strive for outstanding professionalism and top quality in everything we do.”
            </p>
            <span class="block mt-2 font-label-caps text-[11px] text-champagne-gold tracking-widest uppercase">
              — Stephy Sebastian, Founder & Creative Director
            </span>
          </div>

          <!-- CTAs -->
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3.5 w-full sm:w-auto">
            <button data-open-booking class="inline-flex items-center justify-center gap-2 bg-champagne-gold hover:bg-metallic-gold-light active:scale-95 text-obsidian-deep px-7 py-3.5 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase shadow-xl transition-all min-h-[44px]">
              <span>Book Your Experience</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </button>
            <a href="services/index.html" class="inline-flex items-center justify-center gap-2 bg-obsidian-surface hover:bg-white/10 active:scale-95 text-alabaster-cream px-7 py-3.5 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase border border-white/10 transition-all min-h-[44px]">
              <span>Explore Services</span>
              <span class="material-symbols-outlined text-[16px]">menu_book</span>
            </a>
          </div>

          <!-- Trust Badges -->
          <div class="grid grid-cols-3 gap-6 pt-10 mt-6 border-t border-white/10 w-full max-w-xl">
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">10+</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Years Mastery</span>
            </div>
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">100%</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Pure Formulations</span>
            </div>
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">4,800+</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Transformations</span>
            </div>
          </div>
        </div>

        <!-- Right Column: Visual Showcase Slideshow -->
        <div class="lg:col-span-5 relative" id="hero-showcase-container">
          <div class="relative w-full aspect-[4/5] rounded-2xl overflow-hidden shadow-2xl bg-obsidian-surface border border-white/10 group select-none">
            
            <!-- Slide 1: Muslim Nikah Bride -->
            <div class="hero-slide active" data-index="0" data-tag="Nikah Ceremony" data-title="Bespoke Muslim Bridal Couture">
              <img src="assets/images/instagram/DTc2O2fCFZI.jpg" alt="Haute Couture Muslim Nikah Bride Artistry by Stephy Sebastian" class="w-full h-full object-cover" fetchpriority="high" />
            </div>

            <!-- Slide 2: Reception Glamour -->
            <div class="hero-slide" data-index="1" data-tag="Cocktail & Party" data-title="Red Carpet Evening Glamour">
              <img src="assets/images/instagram/DX6qGl_SKf1.jpg" alt="Red Carpet Reception Glamour at LivArt Salon Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            </div>

            <!-- Slide 3: Hindu Muhurtham Bride -->
            <div class="hero-slide" data-index="2" data-tag="Sacred Muhurtham" data-title="Traditional South Indian Radiance">
              <img src="assets/images/instagram/DULWym5CHa0.jpg" alt="Traditional Hindu Muhurtham Bride by Stephy Sebastian" class="w-full h-full object-cover" loading="lazy" />
            </div>

            <!-- Slide 4: Christian Bride -->
            <div class="hero-slide" data-index="3" data-tag="Church Ceremony" data-title="Porcelain Christian Bridal Grace">
              <img src="assets/images/instagram/DYuASLuK_le.jpg" alt="Christian Bridal Gown and Veil Styling LivArt Salon" class="w-full h-full object-cover" loading="lazy" />
            </div>

            <!-- Slide 5: Hair Styling & Blowout -->
            <div class="hero-slide" data-index="4" data-tag="Couture Balayage" data-title="Glossy Balayage & Salon Waves">
              <img src="assets/images/instagram/C5pwjmOidQU.jpg" alt="L'Oreal Glossy Balayage Hair Colouring and Styling at LivArt Salon Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            </div>

            <!-- Subtle Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-black/20 pointer-events-none z-[3]"></div>

            <!-- Slide Navigation Chevrons (Prev / Next) -->
            <button id="hero-slide-prev" aria-label="Previous Slide" class="absolute left-3 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-obsidian-deep/70 hover:bg-champagne-gold hover:text-obsidian-deep text-alabaster-cream flex items-center justify-center backdrop-blur-sm border border-white/15 opacity-0 group-hover:opacity-100 transition-all duration-300 z-[5]">
              <span class="material-symbols-outlined text-[18px]">chevron_left</span>
            </button>
            <button id="hero-slide-next" aria-label="Next Slide" class="absolute right-3 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-obsidian-deep/70 hover:bg-champagne-gold hover:text-obsidian-deep text-alabaster-cream flex items-center justify-center backdrop-blur-sm border border-white/15 opacity-0 group-hover:opacity-100 transition-all duration-300 z-[5]">
              <span class="material-symbols-outlined text-[18px]">chevron_right</span>
            </button>

            <!-- Slide Progress Indicators (Dots) -->
            <div class="absolute top-4 right-4 flex items-center gap-1.5 z-[5] bg-obsidian-deep/60 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/10">
              <button class="hero-dot w-4 h-2 rounded-full transition-all bg-champagne-gold" data-index="0" aria-label="Slide 1"></button>
              <button class="hero-dot w-2 h-2 rounded-full transition-all bg-white/40 hover:bg-white/70" data-index="1" aria-label="Slide 2"></button>
              <button class="hero-dot w-2 h-2 rounded-full transition-all bg-white/40 hover:bg-white/70" data-index="2" aria-label="Slide 3"></button>
              <button class="hero-dot w-2 h-2 rounded-full transition-all bg-white/40 hover:bg-white/70" data-index="3" aria-label="Slide 4"></button>
              <button class="hero-dot w-2 h-2 rounded-full transition-all bg-white/40 hover:bg-white/70" data-index="4" aria-label="Slide 5"></button>
            </div>

            <!-- Bottom Glassmorphic Caption Card -->
            <div class="absolute bottom-6 left-6 right-6 p-4 bg-obsidian-deep/90 backdrop-blur-md rounded-xl border border-white/10 flex items-center justify-between z-[4] shadow-xl">
              <div class="overflow-hidden pr-2">
                <span id="hero-slider-tag" class="font-label-caps text-[10px] text-champagne-gold tracking-widest uppercase block transition-all duration-300">Nikah Ceremony</span>
                <span id="hero-slider-title" class="font-serif-luxury text-base text-alabaster-cream font-bold truncate block transition-all duration-300">Bespoke Muslim Bridal Couture</span>
              </div>
              <div class="flex items-center gap-2.5 shrink-0">
                <span id="hero-slider-counter" class="text-[11px] font-bold text-metallic-gold-light tracking-wider font-mono">1/5</span>
                <div class="w-9 h-9 rounded-full bg-champagne-gold text-obsidian-deep flex items-center justify-center shadow-md">
                  <span class="material-symbols-outlined text-[18px]">spa</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Floating Badge -->
          <div class="absolute -top-5 -left-5 hidden sm:flex items-center gap-2 bg-obsidian-surface/95 backdrop-blur-md p-3.5 rounded-xl shadow-xl border border-champagne-gold/30 z-[6]">
            <span class="material-symbols-outlined text-champagne-gold text-[22px]" style="font-variation-settings: 'FILL' 1;">verified</span>
            <div class="flex flex-col pr-1">
              <span class="text-[10px] font-bold text-metallic-gold-light uppercase tracking-wider">Certified Masters</span>
              <span class="text-xs text-gray-300">Curated by World Class Stylists</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SPECIAL 1-YEAR 20% OFF MEMBERSHIP BANNER -->
  <section class="w-full bg-gold-gradient text-obsidian-deep py-4 shadow-inner">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-11 h-11 rounded-full bg-obsidian-deep text-champagne-gold flex items-center justify-center shrink-0 shadow-md">
          <span class="material-symbols-outlined text-[24px]">card_membership</span>
        </div>
        <div>
          <h2 class="font-serif-luxury text-xl font-bold leading-tight">
            Complimentary 1-Year LivArt Privilege Membership
          </h2>
          <p class="text-xs sm:text-sm text-black/80 font-medium">
            Avail any salon service worth <strong>Rs. 1,000</strong> and receive an exclusive <strong>1-Year Membership Card</strong> with <strong>20% discount</strong> on all future services!
          </p>
        </div>
      </div>
      <button data-open-booking data-service="1-Year 20% Membership Offer" class="shrink-0 bg-obsidian-deep hover:bg-obsidian-surface text-alabaster-cream px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all shadow-md">
        Claim Membership
      </button>
    </div>
  </section>

  <!-- HOT DEALS FROM LIVART -->
  <section class="w-full py-20 bg-surface-bright" id="hot-deals">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-semibold block mb-1">
            Exclusive Limited Offerings
          </span>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-obsidian-deep font-bold">
            Hot Deals from LivArt Kakkanad
          </h2>
        </div>
        <p class="text-sm text-muted-slate max-w-md">
          Indulge in our most sought-after salon rituals at promotional atelier pricing. Handcrafted using premium L'Oreal & Cheryl's professional formulations.
        </p>
      </div>

      <!-- Hot Deals Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Deal 1: De-Tan + Skin Miracle (Featured) -->
        <div class="lg:col-span-2 bg-surface-container-low rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-black/5 flex flex-col md:flex-row">
          <div class="md:w-1/2 relative min-h-[260px] bg-obsidian-deep">
            <img src="assets/images/offers/offer-poster1.webp" alt="De-Tan and Skin Miracle Whitening Facial Combo LivArt Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            <span class="absolute top-4 left-4 bg-obsidian-deep/90 text-champagne-gold px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase border border-champagne-gold/30">
              Most Requested
            </span>
          </div>
          <div class="md:w-1/2 p-6 sm:p-8 flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-1.5 text-warm-bronze mb-2">
                <span class="material-symbols-outlined text-[16px]">schedule</span>
                <span class="text-[11px] font-bold uppercase tracking-wider">75 Min Signature Ritual</span>
              </div>
              <h3 class="font-serif-luxury text-2xl text-obsidian-deep font-bold mb-2">
                De-Tan + Skin Miracle Whitening Facial Combo!
              </h3>
              <p class="text-sm text-muted-slate mb-4 leading-relaxed">
                Our signature brightening facial ritual eradicates stubborn sun tanning, infuses cellular hydration, and revitalizes natural collagen. Includes free 1-Year 20% privilege membership card!
              </p>
            </div>
            <div>
              <div class="flex items-baseline gap-2 mb-4">
                <span class="text-xs uppercase text-muted-slate font-medium">From</span>
                <span class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Rs. 2,499</span>
                <span class="text-xs text-warm-bronze font-semibold">+ 20% Membership Perk</span>
              </div>
              <button data-open-booking data-service="De-Tan + Skin Miracle Whitening Combo (Rs. 2499)" class="w-full inline-flex items-center justify-center bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
                Book Offer Now
              </button>
            </div>
          </div>
        </div>

        <!-- Deal 2: Hair Botox -->
        <div class="bg-surface-container-low rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-black/5 flex flex-col justify-between p-6 sm:p-7">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="bg-champagne-gold/15 text-warm-bronze px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider">
                Anti-Frizz Therapy
              </span>
              <span class="material-symbols-outlined text-champagne-gold">auto_awesome</span>
            </div>
            <div class="w-full h-48 rounded-xl overflow-hidden mb-4 bg-obsidian-deep">
              <img src="assets/images/offers/offer-poster2.webp" alt="Hair Botox Treatment LivArt Salon Kochi" class="w-full h-full object-cover" loading="lazy" />
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">
              Hair Botox Treatment
            </h3>
            <p class="text-xs text-muted-slate mb-4 leading-relaxed">
              Intensive deep-conditioning formula that fills hair fiber gaps, eliminates humidity frizz, and restores silky mirror-like luminosity.
            </p>
          </div>
          <div>
            <div class="flex items-baseline gap-1.5 mb-4">
              <span class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Rs. 5,999</span>
              <span class="text-[11px] text-warm-bronze font-bold uppercase">Only</span>
            </div>
            <button data-open-booking data-service="Hair Botox Treatment (Rs. 5999)" class="w-full inline-flex items-center justify-center bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              Book Hair Botox
            </button>
          </div>
        </div>

        <!-- Deal 3: Hair Colouring -->
        <div class="bg-surface-container-low rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-black/5 flex flex-col justify-between p-6 sm:p-7">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="bg-champagne-gold/15 text-warm-bronze px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider">
                Couture Color
              </span>
              <span class="material-symbols-outlined text-champagne-gold">palette</span>
            </div>
            <div class="w-full h-48 rounded-xl overflow-hidden mb-4 bg-obsidian-deep">
              <img src="assets/images/offers/offer-poster3.webp" alt="Hair Colouring Artistry LivArt Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">
              Hair Colouring Artistry
            </h3>
            <p class="text-xs text-muted-slate mb-4 leading-relaxed">
              From seamless multidimensional balayage to rich global tinting, customized by senior colorists with premium L'Oreal formulations.
            </p>
          </div>
          <div>
            <div class="flex items-baseline gap-1.5 mb-4">
              <span class="text-xs uppercase text-muted-slate">From</span>
              <span class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Rs. 5,999</span>
            </div>
            <button data-open-booking data-service="Hair Colouring Artistry (From Rs. 5999)" class="w-full inline-flex items-center justify-center bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              Book Hair Colour
            </button>
          </div>
        </div>

        <!-- Deal 4: Permanent Blow Dry -->
        <div class="bg-surface-container-low rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-black/5 flex flex-col justify-between p-6 sm:p-7">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="bg-champagne-gold/15 text-warm-bronze px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider">
                Long-Lasting
              </span>
              <span class="material-symbols-outlined text-champagne-gold">air</span>
            </div>
            <div class="w-full h-48 rounded-xl overflow-hidden mb-4 bg-obsidian-deep">
              <img src="assets/images/instagram/Db7rJBtuj4B.jpg" alt="Amala Shaji Permanent Blow Dry at LivArt Salon Kochi" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">
              Permanent Blow Dry
            </h3>
            <p class="text-xs text-muted-slate mb-4 leading-relaxed">
              Wake up with runway-ready bouncy, effortless volume every single morning without heat styling tools for months.
            </p>
          </div>
          <div>
            <div class="flex items-baseline gap-1.5 mb-4">
              <span class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Rs. 5,999</span>
              <span class="text-[11px] text-warm-bronze font-bold uppercase">Special Rate</span>
            </div>
            <button data-open-booking data-service="Permanent Blow Dry (Rs. 5999)" class="w-full inline-flex items-center justify-center bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              Book Blow Dry
            </button>
          </div>
        </div>

        <!-- Deal 5: Hair Spa Special -->
        <div class="bg-surface-container-low rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-black/5 flex flex-col justify-between p-6 sm:p-7">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="bg-champagne-gold text-obsidian-deep px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider">
                33% Seasonal Off
              </span>
              <span class="material-symbols-outlined text-champagne-gold">water_drop</span>
            </div>
            <div class="w-full h-48 rounded-xl overflow-hidden mb-4 bg-obsidian-deep">
              <img src="assets/images/instagram/DEXOFvGTyDZ.jpg" alt="Actress Amala Rose Kurian L'Oreal Hair Spa at LivArt Salon Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">
              Revitalizing Hair Spa
            </h3>
            <p class="text-xs text-muted-slate mb-4 leading-relaxed">
              Intensive steam infusion and scalp acupressure massage targeting dryness, scalp tension, and root rejuvenation.
            </p>
          </div>
          <div>
            <div class="flex items-baseline gap-2 mb-4">
              <span class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Rs. 1,200</span>
              <span class="text-sm line-through text-muted-slate">Rs. 1,800</span>
            </div>
            <button data-open-booking data-service="Revitalizing Hair Spa (Rs. 1200)" class="w-full inline-flex items-center justify-center bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              Book Hair Spa
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- INSTAGRAM REELS & VIDEO COMMUNITY SHOWCASE -->
  <section class="w-full py-16 sm:py-20 bg-obsidian-deep text-alabaster-cream" id="instagram-showcase">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-12 gap-4">
        <div>
          <div class="flex items-center gap-2 text-champagne-gold mb-2">
            <span class="material-symbols-outlined text-[20px]">photo_camera</span>
            <span class="font-label-caps text-xs tracking-[0.2em] uppercase font-bold">Live Atelier Creations</span>
          </div>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-alabaster-cream font-bold">
            Follow the Artistry on Instagram
          </h2>
        </div>
        <div class="flex items-center gap-4">
          <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto justify-center inline-flex items-center gap-2 bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:opacity-95 active:scale-95 text-white px-5 py-3 sm:py-2.5 rounded-lg text-xs font-bold tracking-wider uppercase transition-all shadow-md min-h-[44px] sm:min-h-[auto]">
            <span>Follow {INSTAGRAM_HANDLE}</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
        </div>
      </div>

      <!-- Touch-Friendly Category Filter Tabs (Swipeable on Mobile) -->
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar touch-scroll py-2 px-1 -mx-4 px-4 sm:mx-0 sm:justify-center mb-8">
        <button onclick="filterReelsCategory('all', 'instagram-feed-grid')" data-category="all" class="reel-filter-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-champagne-gold text-obsidian-deep min-h-[40px] shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px]">auto_awesome</span>
          <span>All 48 Curated Reels</span>
        </button>
        <button onclick="filterReelsCategory('celebrity', 'instagram-feed-grid')" data-category="celebrity" class="reel-filter-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[40px] flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px]">star</span>
          <span>Celebrity Visits (21)</span>
        </button>
        <button onclick="filterReelsCategory('bridal', 'instagram-feed-grid')" data-category="bridal" class="reel-filter-btn shrink-0 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all bg-obsidian-surface text-gray-300 border border-white/10 hover:border-champagne-gold min-h-[40px] flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px]">favorite</span>
          <span>Bridal Works (27)</span>
        </button>
      </div>

      <!-- Instagram Grid Container -->
      <div id="instagram-feed-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-6 gap-4 sm:gap-6">
        <!-- Injected via assets/js/instagram-feed.js -->
      </div>
    </div>
  </section>

  <!-- WHO WE ARE / FOUNDER STORY -->
  <section class="w-full py-20 bg-ivory-surface">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Images Left -->
        <div class="lg:col-span-6 grid grid-cols-2 gap-4">
          <div class="aspect-[3/4] rounded-2xl overflow-hidden shadow-lg mt-6 bg-obsidian-deep">
            <img src="assets/images/instagram/CpsA0o_OSo5.jpg" alt="Master Hair Styling & Runway Waves by LivArt Senior Stylist Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="aspect-[3/4] rounded-2xl overflow-hidden shadow-lg -mt-6 bg-obsidian-deep">
            <img src="assets/images/instagram/DX6qGl_SKf1.jpg" alt="Red Carpet Reception Glamour & Hair Design at LivArt Atelier" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="col-span-2 aspect-[16/9] rounded-2xl overflow-hidden shadow-lg bg-obsidian-deep">
            <img src="assets/images/instagram/DULWym5CHa0.jpg" alt="Master Bridal Makeup & Saree Draping by Stephy Sebastian LivArt Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
        </div>

        <!-- Content Right -->
        <div class="lg:col-span-6 flex flex-col items-start">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-semibold mb-2">
            Atelier Identity • Kakkanad, Kochi
          </span>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-obsidian-deep font-bold mb-6">
            Who We Are
          </h2>
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            LivArt Hair and Makeup Studio is a destination salon in Kakkanad that offers top-of-the-line hair, makeup & skin services, with a focus on cutting-edge techniques and an unmatched level of customer service.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Having gained invaluable experience working with industry giants for over a decade, our founder <strong>Stephy Sebastian</strong> specializes in creating looks that will make you feel on top of the world.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-6">
            Our team of experienced stylists is passionate about their craft and is always ready to help you find your perfect style, whether it’s for everyday wear or a special occasion. We provide customized services that cater to all skin and hair types, ensuring your personal style will always reflect who you truly are!
          </p>

          <div class="grid grid-cols-2 gap-4 w-full bg-surface-container p-4 rounded-xl mb-8">
            <div>
              <span class="font-label-caps text-[10px] text-warm-bronze uppercase tracking-widest font-bold block mb-1">Philosophy</span>
              <p class="text-xs text-gray-700">Beauty as a lifestyle, celebrating personal grace, inner well-being, and genuine radiance.</p>
            </div>
            <div>
              <span class="font-label-caps text-[10px] text-warm-bronze uppercase tracking-widest font-bold block mb-1">Kochi Sanctuary</span>
              <p class="text-xs text-gray-700">Anchorage Business Center, Seaport-Airport Road, Kakkanad.</p>
            </div>
          </div>

          <div class="flex items-center gap-4">
            <a href="about-us/index.html" class="inline-flex items-center gap-2 bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
              <span>Read Full Story</span>
              <span class="material-symbols-outlined text-[16px]">north_east</span>
            </a>
            <button data-open-booking class="inline-flex items-center gap-2 border border-obsidian-deep/20 hover:bg-black/5 px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              <span>Consult Stylists</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4 PILLARS OF LIVART -->
  <section class="w-full py-20 bg-obsidian-deep text-alabaster-cream">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl mb-16">
        <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
          The Atelier Standard
        </span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-alabaster-cream font-bold mb-4">
          Why LivArt is Kakkanad’s Preferred Choice
        </h2>
        <p class="text-base text-gray-300 leading-relaxed">
          At LivArt Salon, we believe beauty is a lifestyle. We are dedicated to helping you express your unique individuality through flawless technique, serene hospitality, and remarkable transformations.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-obsidian-surface p-6 rounded-2xl border border-white/5 flex flex-col justify-between hover:border-champagne-gold/40 transition-all">
          <div>
            <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-champagne-gold flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-[24px]">workspace_premium</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2">Expert Artists & Stylists</h3>
            <p class="text-xs text-muted-slate leading-relaxed">
              Our team has extensive working experience with advanced techniques and premium products, creating a look that perfectly reflects your personal style.
            </p>
          </div>
          <span class="pt-6 text-champagne-gold font-label-caps text-[10px] tracking-widest uppercase font-bold">• Global Standards</span>
        </div>

        <div class="bg-obsidian-surface p-6 rounded-2xl border border-white/5 flex flex-col justify-between hover:border-champagne-gold/40 transition-all">
          <div>
            <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-champagne-gold flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-[24px]">weekend</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2">Unmatched Comfort</h3>
            <p class="text-xs text-muted-slate leading-relaxed">
              We go beyond haircuts and makeup to offer a relaxing, luxurious experience where you can lounge, unwind, and indulge in attentive care.
            </p>
          </div>
          <span class="pt-6 text-champagne-gold font-label-caps text-[10px] tracking-widest uppercase font-bold">• Pure Sanctuary</span>
        </div>

        <div class="bg-obsidian-surface p-6 rounded-2xl border border-white/5 flex flex-col justify-between hover:border-champagne-gold/40 transition-all">
          <div>
            <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-champagne-gold flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-[24px]">sanitizer</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2">Radiant Formulations</h3>
            <p class="text-xs text-muted-slate leading-relaxed">
              We exclusively use top-quality skin and hair products that nourish and freshen up your looks while promoting long-term biological hair health.
            </p>
          </div>
          <span class="pt-6 text-champagne-gold font-label-caps text-[10px] tracking-widest uppercase font-bold">• Certified Products</span>
        </div>

        <div class="bg-obsidian-surface p-6 rounded-2xl border border-white/5 flex flex-col justify-between hover:border-champagne-gold/40 transition-all">
          <div>
            <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-champagne-gold flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-[24px]">psychology_alt</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2">Empowered Confidence</h3>
            <p class="text-xs text-muted-slate leading-relaxed">
              We follow a client-centric approach and actively seek your input throughout every session so you leave feeling positive, empowered, and confident.
            </p>
          </div>
          <span class="pt-6 text-champagne-gold font-label-caps text-[10px] tracking-widest uppercase font-bold">• Inner Well-Being</span>
        </div>
      </div>
    </div>
  </section>

  <!-- FOUNDER SPOTLIGHT: STEPHY SEBASTIAN -->
  <section class="w-full py-20 bg-surface-container-low" id="founder-spotlight">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-surface-container-lowest rounded-3xl overflow-hidden shadow-md p-6 sm:p-10 lg:p-12 border border-black/5 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-5 relative">
          <div class="w-full aspect-[4/5] rounded-2xl overflow-hidden shadow-xl bg-obsidian-deep">
            <img src="assets/images/brand/stephy-sebastian.webp" alt="Stephy Sebastian - Founder of LivArt Salon & LivArt Beauty Academy Kakkanad" class="w-full h-full object-cover" loading="lazy" />
          </div>
          <div class="absolute -bottom-4 -right-4 bg-obsidian-deep text-alabaster-cream p-4 rounded-xl shadow-xl hidden sm:block border border-champagne-gold/20">
            <span class="font-label-caps text-[10px] text-champagne-gold tracking-widest uppercase font-bold block">Founder • Director</span>
            <span class="font-serif-luxury text-sm font-bold">10+ Years of Artistry</span>
          </div>
        </div>

        <div class="lg:col-span-7 flex flex-col items-start">
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-semibold">
              Visionary Behind LivArt
            </span>
            <span class="text-muted-slate text-xs">•</span>
            <span class="text-[11px] font-semibold text-champagne-gold bg-obsidian-deep px-2.5 py-0.5 rounded-full">Former National Educator L'Oréal & Wella</span>
          </div>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-obsidian-deep font-bold mb-2">
            Stephy Sebastian
          </h2>
          <span class="font-serif-luxury text-lg text-warm-bronze mb-4 font-semibold">
            Founder, Creative Director & Master Cosmetology Mentor
          </span>
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            Stephy Sebastian is the visionary force driving LivArt Hair & Makeup Studio and <a href="https://livart.co.in/" target="_blank" rel="noopener noreferrer" class="text-warm-bronze font-semibold hover:underline">LivArt Beauty Academy</a> in Kakkanad, Kochi. Her artistic journey began in Kuttanadu, Alappuzha, where she observed her mother grooming village brides with unmatched warmth and devotion.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Before turning her creative passion into a lifetime calling, Stephy served for <strong>5 years as a professional healthcare nurse</strong>. That medical foundation instilled the hospital-grade sterilization, scientific skin analysis, and deep client empathy that defines LivArt today. She subsequently headed technical education at a national level for <strong>L'Oréal Professionnel and Wella</strong>, training hundreds of elite stylists across India.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-6">
            In 2021, she established <strong>LivArt Beauty Academy (<a href="https://livart.co.in/" target="_blank" rel="noopener noreferrer" class="underline text-obsidian-deep font-semibold">livart.co.in</a>)</strong>, affiliated with the <strong>B&WSSC (Beauty and Wellness Sector Skill Council of India)</strong>, to mentor aspiring cosmetologists with authentic salon floor apprenticeship.
          </p>
          
          <div class="grid grid-cols-3 gap-4 w-full py-4 mb-6 border-y border-black/5">
            <div>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep block">10+ Yrs</span>
              <span class="text-[11px] text-muted-slate uppercase">Mastery</span>
            </div>
            <div>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep block">5,000+</span>
              <span class="text-[11px] text-muted-slate uppercase">Clients Transformed</span>
            </div>
            <div>
              <span class="font-serif-luxury text-xl font-bold text-obsidian-deep block">B&WSSC</span>
              <span class="text-[11px] text-muted-slate uppercase">Govt. Accredited</span>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-3">
            <button data-open-booking data-service="Personal Consultation with Founder Stephy Sebastian" class="inline-flex items-center gap-2 bg-obsidian-deep hover:bg-champagne-gold text-alabaster-cream hover:text-obsidian-deep px-5 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
              <span>Consult with Stephy</span>
              <span class="material-symbols-outlined text-[16px]">calendar_month</span>
            </button>
            <a href="academy/index.html" class="inline-flex items-center gap-2 bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-5 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
              <span>LivArt Beauty Academy</span>
              <span class="material-symbols-outlined text-[16px]">school</span>
            </a>
            <a href="https://livart.co.in/founder-makeup-academy/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs text-muted-slate hover:text-obsidian-deep font-semibold px-3 py-2 border border-black/10 rounded-lg transition-colors">
              <span>Founder Story on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LIVART BEAUTY ACADEMY SHOWCASE (livart.co.in) -->
  <section class="w-full py-20 bg-obsidian-deep text-alabaster-cream relative overflow-hidden" id="academy-showcase">
    <div class="absolute -top-32 right-0 w-96 h-96 rounded-full bg-champagne-gold/10 blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-0 -left-48 w-96 h-96 rounded-full bg-warm-bronze/10 blur-3xl pointer-events-none"></div>

    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Section Header -->
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-14">
        <div class="max-w-2xl">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-3 py-1 bg-champagne-gold text-obsidian-deep rounded-full text-[10px] font-bold tracking-widest uppercase">
              Govt. Affiliated Academy
            </span>
            <span class="text-metallic-gold-light text-xs font-medium">B&WSSC Accredited Beautician Courses</span>
          </div>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl lg:text-5xl text-alabaster-cream font-normal">
            LivArt Beauty Academy <br />
            <span class="italic text-gold-gradient">Turn Your Passion into a Global Career</span>
          </h2>
          <p class="text-sm sm:text-base text-gray-300 mt-4 leading-relaxed">
            Curated by Master Stylist Stephy Sebastian. Unlike conventional schools, LivArt Academy students train on the active salon floor of LivArt Kakkanad with real clients, international cosmetic brands, and government-approved certifications.
          </p>
        </div>
        <div class="flex flex-wrap items-center gap-3">
          <a href="academy/index.html" class="bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-lg flex items-center gap-2">
            <span>Explore Academy Hub</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
          <a href="https://livart.co.in/" target="_blank" rel="noopener noreferrer" class="border border-white/20 hover:border-champagne-gold text-white hover:text-champagne-gold px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all flex items-center gap-2">
            <span>Visit livart.co.in</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
        </div>
      </div>

      <!-- Course Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        <!-- Course 1 -->
        <div class="bg-obsidian-surface rounded-2xl p-6 border border-white/10 flex flex-col justify-between hover:border-champagne-gold/50 transition-all group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/10 px-2.5 py-1 rounded-full">Comprehensive</span>
              <span class="text-xs text-muted-slate font-mono">Diploma</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2 group-hover:text-champagne-gold transition-colors">
              Diploma in Cosmetology
            </h3>
            <p class="text-xs text-muted-slate leading-relaxed mb-4">
              All-inclusive master curriculum covering advanced hair styling, clinical skincare aesthetics, bridal makeup, chemical texturing, and salon management.
            </p>
            <ul class="text-xs text-gray-300 space-y-2 mb-6 border-t border-white/5 pt-4">
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Govt. B&WSSC Approved</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Live Salon Apprenticeship</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>100% Placement Assistance</span>
              </li>
            </ul>
          </div>
          <a href="https://livart.co.in/certification-course-in-cosmetology/" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 rounded-lg border border-champagne-gold/30 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold text-xs font-bold tracking-wider uppercase text-center transition-all flex items-center justify-center gap-1.5">
            <span>Syllabus on livart.co.in</span>
            <span class="material-symbols-outlined text-[14px]">open_in_new</span>
          </a>
        </div>

        <!-- Course 2 -->
        <div class="bg-obsidian-surface rounded-2xl p-6 border border-white/10 flex flex-col justify-between hover:border-champagne-gold/50 transition-all group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/10 px-2.5 py-1 rounded-full">Bridal Masterclass</span>
              <span class="text-xs text-muted-slate font-mono">2 Months</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2 group-hover:text-champagne-gold transition-colors">
              Professional Bridal Makeup
            </h3>
            <p class="text-xs text-muted-slate leading-relaxed mb-4">
              Intensive training in 4K HD makeup, airbrush techniques, traditional Kerala, Christian, and contemporary Muslim bridal aesthetics, and couture saree draping.
            </p>
            <ul class="text-xs text-gray-300 space-y-2 mb-6 border-t border-white/5 pt-4">
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Stephy Sebastian Mentorship</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Portfolio Photo Shoots</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Airbrush Kit Familiarization</span>
              </li>
            </ul>
          </div>
          <a href="https://livart.co.in/bridal-makeup-course/" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 rounded-lg border border-champagne-gold/30 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold text-xs font-bold tracking-wider uppercase text-center transition-all flex items-center justify-center gap-1.5">
            <span>Syllabus on livart.co.in</span>
            <span class="material-symbols-outlined text-[14px]">open_in_new</span>
          </a>
        </div>

        <!-- Course 3 -->
        <div class="bg-obsidian-surface rounded-2xl p-6 border border-white/10 flex flex-col justify-between hover:border-champagne-gold/50 transition-all group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/10 px-2.5 py-1 rounded-full">Hair Science</span>
              <span class="text-xs text-muted-slate font-mono">4 Months</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2 group-hover:text-champagne-gold transition-colors">
              Hair Styling & Haircuts
            </h3>
            <p class="text-xs text-muted-slate leading-relaxed mb-4">
              Master geometric precision cuts, balayage, ombre, global coloring, hair botox, nanoplastia, and advanced chemical straightening protocols.
            </p>
            <ul class="text-xs text-gray-300 space-y-2 mb-6 border-t border-white/5 pt-4">
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>L'Oréal & Wella Standards</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Precision Sectioning & Angles</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Chemical & Texture Science</span>
              </li>
            </ul>
          </div>
          <a href="https://livart.co.in/hair-styling-course/" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 rounded-lg border border-champagne-gold/30 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold text-xs font-bold tracking-wider uppercase text-center transition-all flex items-center justify-center gap-1.5">
            <span>Syllabus on livart.co.in</span>
            <span class="material-symbols-outlined text-[14px]">open_in_new</span>
          </a>
        </div>

        <!-- Course 4 -->
        <div class="bg-obsidian-surface rounded-2xl p-6 border border-white/10 flex flex-col justify-between hover:border-champagne-gold/50 transition-all group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/10 px-2.5 py-1 rounded-full">Dermal Aesthetics</span>
              <span class="text-xs text-muted-slate font-mono">4 Months</span>
            </div>
            <h3 class="font-serif-luxury text-xl font-bold text-alabaster-cream mb-2 group-hover:text-champagne-gold transition-colors">
              Skin Care & Aesthetics
            </h3>
            <p class="text-xs text-muted-slate leading-relaxed mb-4">
              Learn medical-grade Hydra Facials, ultrasonic peeling, galvanic skin treatments, acne management, and de-tan therapies using Cheryl's Cosmeceuticals.
            </p>
            <ul class="text-xs text-gray-300 space-y-2 mb-6 border-t border-white/5 pt-4">
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Clinical Hygiene Protocols</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Hydra Vacuum Machine Handling</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[14px] text-champagne-gold">check_circle</span>
                <span>Skin Type Diagnostic Science</span>
              </li>
            </ul>
          </div>
          <a href="https://livart.co.in/skin-care-course/" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 rounded-lg border border-champagne-gold/30 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold text-xs font-bold tracking-wider uppercase text-center transition-all flex items-center justify-center gap-1.5">
            <span>Syllabus on livart.co.in</span>
            <span class="material-symbols-outlined text-[14px]">open_in_new</span>
          </a>
        </div>
      </div>

      <!-- Bottom Academy Banner -->
      <div class="bg-gradient-to-r from-obsidian-surface to-obsidian-deep p-6 sm:p-8 rounded-2xl border border-champagne-gold/20 flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 rounded-xl bg-champagne-gold/20 text-champagne-gold flex items-center justify-center shrink-0">
            <span class="material-symbols-outlined text-[26px]">workspace_premium</span>
          </div>
          <div>
            <h4 class="font-serif-luxury text-lg font-bold text-white">Admissions Open for Next Batch in Kakkanad, Kochi</h4>
            <p class="text-xs text-gray-300 mt-0.5">Government B&WSSC Certification • High demand across Gulf countries (UAE, Qatar, Oman) & India.</p>
          </div>
        </div>
        <div class="flex items-center gap-3 shrink-0">
          <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20am%20interested%20in%20beautician%20and%20cosmetology%20courses" target="_blank" rel="noopener noreferrer" class="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">chat</span>
            <span>WhatsApp Admissions</span>
          </a>
          <a href="tel:{ACADEMY_PHONE_TEL}" class="border border-white/20 hover:border-champagne-gold text-white hover:text-champagne-gold px-4 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[15px] text-champagne-gold">call</span>
            <span>Call 096332 11151</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- VERIFIED GOOGLE CLIENT REVIEWS -->
  <section class="w-full py-20 bg-surface-bright" id="reviews">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <div class="flex items-center gap-1 mb-2 text-champagne-gold">
            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="text-xs text-obsidian-deep font-bold uppercase tracking-wider ml-1">4.9 / 5.0 Google Reviews</span>
          </div>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-obsidian-deep font-bold">
            What Our Patrons Say
          </h2>
        </div>
        <p class="text-sm text-muted-slate max-w-sm">
          Hear directly from Kakkanad patrons and brides whose special milestones were elevated by LivArt's attentive touch.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-surface-container-low p-8 rounded-2xl shadow-sm border border-black/5 flex flex-col justify-between">
          <div>
            <div class="text-champagne-gold mb-3">
              <span class="material-symbols-outlined text-[32px]">format_quote</span>
            </div>
            <p class="text-sm text-gray-700 leading-relaxed italic mb-6">
              “Stephy and her team at LivArt Kakkanad made my wedding day unforgettable. The bridal makeup stayed pristine through tears and 10 hours of celebrations. Truly world-class styling!”
            </p>
          </div>
          <div class="pt-4 border-t border-black/5">
            <span class="font-serif-luxury text-base font-bold text-obsidian-deep block">Ananya R. Nair</span>
            <span class="text-xs text-muted-slate">Bridal Package Client • Infopark, Kakkanad</span>
          </div>
        </div>

        <div class="bg-surface-container-low p-8 rounded-2xl shadow-sm border border-black/5 flex flex-col justify-between">
          <div>
            <div class="text-champagne-gold mb-3">
              <span class="material-symbols-outlined text-[32px]">format_quote</span>
            </div>
            <p class="text-sm text-gray-700 leading-relaxed italic mb-6">
              “The Hair Botox and De-Tan Facial combo is unmatched value. My frizzy humidity hair feels like liquid silk. The salon space is serene, clean, and smells heavenly.”
            </p>
          </div>
          <div class="pt-4 border-t border-black/5">
            <span class="font-serif-luxury text-base font-bold text-obsidian-deep block">Dr. Priya Menon</span>
            <span class="text-xs text-muted-slate">Verified Reviewer • Kochi</span>
          </div>
        </div>

        <div class="bg-surface-container-low p-8 rounded-2xl shadow-sm border border-black/5 flex flex-col justify-between">
          <div>
            <div class="text-champagne-gold mb-3">
              <span class="material-symbols-outlined text-[32px]">format_quote</span>
            </div>
            <p class="text-sm text-gray-700 leading-relaxed italic mb-6">
              “Took their permanent blow dry service and got the 1-year free membership card. Courteous staff who listen to what you want without rushing. 10/10 recommend LivArt!”
            </p>
          </div>
          <div class="pt-4 border-t border-black/5">
            <span class="font-serif-luxury text-base font-bold text-obsidian-deep block">Sarah Thomas</span>
            <span class="text-xs text-muted-slate">Premium Member • Kakkanad</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LOCATION & CONTACT EMBED -->
  <section class="w-full py-20 bg-ivory-surface">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        <div class="lg:col-span-7 bg-obsidian-deep text-alabaster-cream p-8 sm:p-10 rounded-3xl shadow-xl">
          <span class="font-label-caps text-xs text-champagne-gold tracking-widest uppercase font-bold block mb-2">
            Visit Our Kakkanad Atelier
          </span>
          <h3 class="font-serif-luxury text-3xl font-bold text-alabaster-cream mb-6">
            Anchorage Business Center Sanctuary
          </h3>
          
          <div class="space-y-6 text-sm text-gray-300">
            <div class="flex items-start gap-4">
              <span class="material-symbols-outlined text-champagne-gold text-[24px] mt-0.5">location_on</span>
              <div>
                <p class="text-white font-medium mb-1">LivArt Salon & Make-up Studio</p>
                <p class="leading-relaxed">{ADDRESS}</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <span class="material-symbols-outlined text-champagne-gold text-[24px] mt-0.5">call</span>
              <div>
                <a href="tel:{PHONE_TEL}" class="text-white hover:text-champagne-gold text-lg font-bold block">{PHONE}</a>
                <span class="text-xs text-muted-slate">Direct Appointments & WhatsApp Consultations</span>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <span class="material-symbols-outlined text-champagne-gold text-[24px] mt-0.5">schedule</span>
              <div>
                <p class="text-white font-medium">{HOURS}</p>
                <span class="text-xs text-muted-slate">Open 7 days a week for your beauty convenience</span>
              </div>
            </div>
          </div>

          <div class="mt-8 pt-8 border-t border-white/10 flex flex-wrap gap-4">
            <button data-open-booking class="bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all">
              Book Appointment
            </button>
            <a href="https://maps.google.com/?q=LivArt+Salon+Kakkanad" target="_blank" rel="noopener noreferrer" class="border border-white/20 hover:bg-white/10 text-white px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all flex items-center gap-1.5">
              <span>Open Google Maps</span>
              <span class="material-symbols-outlined text-[16px]">directions</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5 h-[420px] rounded-3xl overflow-hidden shadow-xl border border-black/5 bg-surface-container">
          <iframe 
            src="https://maps.google.com/maps?q=Livart%20Salon%20-%20Best%20Beauty%20Parlour%20in%20Kakkanad&t=m&z=14&output=embed&iwloc=near" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy" 
            title="LivArt Salon Kakkanad Google Maps Location"
            aria-label="LivArt Salon Kakkanad Google Maps Location">
          </iframe>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer()
    
    with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
        f.write(html)
    print("✓ index.html built")

if __name__ == "__main__":
    build_homepage()
