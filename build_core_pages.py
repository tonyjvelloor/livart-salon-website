import os
import json
from generator import (
    BASE_DIR, SITE_NAME, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    INSTAGRAM_HANDLE, INSTAGRAM_URL, FACEBOOK_URL, LOGO_URL,
    ACADEMY_URL, ACADEMY_FOUNDER_URL, PRESS_FEATURE_URL,
    ACADEMY_PHONE, ACADEMY_PHONE_TEL,
    render_head, render_header, render_footer
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# -------------------------------------------------------------
# 1. ABOUT US PAGE (/about-us/)
# -------------------------------------------------------------
def build_about_page():
    ensure_dir(os.path.join(BASE_DIR, "about-us"))
    
    extra_schema = {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": "About LivArt Salon & Beauty Academy",
        "description": "Learn about LivArt Salon & Beauty Academy founded by Stephy Sebastian and Nipun Conso in Kakkanad, Kochi.",
        "mainEntity": {
            "@type": "Person",
            "name": "Stephy Sebastian",
            "jobTitle": ["Founder & Creative Director", "Celebrity Hair & Makeup Artist", "Master Beauty Educator"],
            "url": ACADEMY_FOUNDER_URL,
            "image": f"{BASE_URL}/assets/images/brand/stephy-sebastian.webp",
            "description": "Stephy Sebastian is a renowned hair stylist, bridal makeup artist, former national educator for L'Oréal Professionnel and Wella, and founder of LivArt Hair & Makeup Studio Kakkanad and LivArt Beauty Academy.",
            "sameAs": [
                ACADEMY_FOUNDER_URL,
                PRESS_FEATURE_URL,
                INSTAGRAM_URL,
                FACEBOOK_URL
            ]
        }
    }

    html = render_head(
        title="About Us & Founder Stephy Sebastian | LivArt Salon Kakkanad Kochi",
        description="Learn about LivArt Salon founded by Stephy Sebastian and Nipun Conso. Former nurse and L'Oréal national trainer curating world-class hair, bridal makeup, and beauty education in Kochi.",
        canonical_path="/about-us/",
        extra_schema=extra_schema,
        root_prefix="../"
    )
    html += render_header(active_slug="about-us", root_prefix="../")
    
    transformations = [
        {"name": "Amala Shaji", "badge": "Influencer Spotlight", "service": "Permanent Blow Dry & Volume Styling", "desc": "Bouncy, effortless runway volume and structural blowout by LivArt senior stylists.", "img": "../assets/images/instagram/Db7rJBtuj4B.jpg"},
        {"name": "Azmin Yasar", "badge": "Model & Anchor", "service": "Precision Haircut & Salon Finish", "desc": "Bespoke hair shaping and salon chair blowout tailored for camera readiness.", "img": "../assets/images/instagram/DbLJRauyFro.jpg"},
        {"name": "Actress Amala Rose Kurian", "badge": "Film & Television", "service": "Hair Botox Rejuvenation Therapy", "desc": "Anti-frizz capillary deep conditioning restoring mirror-like silkiness and strength.", "img": "../assets/images/instagram/DW1NAndDGuP.jpg"},
        {"name": "Anchor Shiju Abdul Rasheed", "badge": "News Anchor", "service": "Executive Precision Haircut & Grooming", "desc": "High-definition camera-ready precision haircut and beard contouring.", "img": "../assets/images/instagram/C7l9fP5P3u9.jpg"},
        {"name": "RJ Soorya", "badge": "Radio Personality", "service": "Couture Balayage & Colouring", "desc": "Multi-dimensional L'Oreal hand-painted balayage with zero ammonia damage.", "img": "../assets/images/instagram/DABMk4mtv8b.jpg"},
        {"name": "Anchor Meenakshi Sudheer", "badge": "TV Anchor", "service": "Deluxe Foot Reflexology & Pedicure Spa", "desc": "Relaxing dead-skin exfoliation, herbal soak, and therapeutic acupressure massage.", "img": "../assets/images/instagram/C88tG9iSEKp.jpg"},
        {"name": "Model Shaluz Boon", "badge": "Fashion Model", "service": "Runway Waves & Texture Styling", "desc": "Voluminous textured curls and movement styling for high-fashion photoshoots.", "img": "../assets/images/instagram/CpsA0o_OSo5.jpg"},
        {"name": "Distinguished Groom", "badge": "Groom Sanctuary", "service": "Black Diamond Groom Makeover", "desc": "Natural matte camera-ready complexion, beard grooming, and hair architecture.", "img": "../assets/images/instagram/DXb3cLlEsmy.jpg"}
    ]

    transformations_html = ""
    for t in transformations:
        transformations_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-lg transition-all flex flex-col justify-between">
          <div class="h-64 overflow-hidden bg-obsidian-deep relative">
            <img src="{t['img']}" alt="{t['name']} - {t['service']} at LivArt Salon Kakkanad" class="w-full h-full object-cover object-top hover:scale-105 transition-transform duration-500" loading="lazy" />
            <span class="absolute top-3 left-3 bg-obsidian-deep/80 text-champagne-gold px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider backdrop-blur-sm border border-champagne-gold/20">
              {t['badge']}
            </span>
          </div>
          <div class="p-5 flex flex-col justify-between flex-grow">
            <div>
              <h3 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-1">{t['name']}</h3>
              <p class="text-xs text-warm-bronze font-bold uppercase tracking-wider mb-2">{t['service']}</p>
              <p class="text-xs text-gray-600 leading-relaxed">{t['desc']}</p>
            </div>
          </div>
        </div>
        """

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Our Heritage & Craft</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">About LivArt Salon & Make-Up Studio</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Where passion meets mastery. Founded by Stephy Sebastian and Nipun Conso to establish Cochin's premier haute couture beauty studio and Government-affiliated academy.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-20">
        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden shadow-2xl bg-obsidian-deep border border-black/10 relative">
            <img src="../assets/images/brand/stephy-sebastian.webp" alt="Stephy Sebastian - Founder of LivArt Salon & LivArt Beauty Academy Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            <div class="absolute bottom-4 left-4 right-4 bg-obsidian-deep/85 backdrop-blur-md p-4 rounded-xl border border-white/10 text-alabaster-cream">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block">Founder Spotlight</span>
              <span class="font-serif-luxury text-sm font-bold">Stephy Sebastian • Former National Trainer L'Oréal & Wella</span>
            </div>
          </div>
        </div>
        <div class="lg:col-span-6">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-2">Our Genesis & Heritage</span>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl font-bold text-obsidian-deep mb-6">Built on Artistry, Healthcare Ethics & World-Class Standards</h2>
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            LivArt Hair and Makeup Studio was established by <strong>Stephy Sebastian</strong> and <strong>Nipun Conso</strong> as a premier destination sanctuary in Kakkanad, Kochi. What sets LivArt apart is Stephy's extraordinary foundation: she worked for <strong>5 years as a professional healthcare nurse</strong> before pursuing her lifelong calling in hair and makeup artistry.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Her mother, hailing from Kuttanadu in Alappuzha, used to groom young village brides with deep love and care, sparking Stephy's early aesthetic passion. Her medical background instilled hospital-grade hygiene, scientific skin diagnostics, and gentle empathy into every LivArt treatment.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Stephy went on to head training at a national level for global beauty titans <strong>L'Oréal Professionnel and Wella</strong>, mentoring hundreds of elite stylists across India. In 2021, she expanded that educational commitment by founding <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="text-warm-bronze font-bold hover:underline">LivArt Beauty Academy (livart.co.in)</a>, affiliated with the <strong>B&WSSC (Beauty & Wellness Sector Skill Council)</strong> of India.
          </p>
          <div class="flex flex-wrap items-center gap-3 pt-2 mb-4">
            <button data-open-booking class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
              Consult Our Team
            </button>
            <a href="../academy/index.html" class="bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-5 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px]">school</span>
              <span>Beauty Academy Hub</span>
            </a>
            <a href="{ACADEMY_FOUNDER_URL}" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-muted-slate hover:text-obsidian-deep px-3 py-2 border border-black/10 rounded-lg transition-colors flex items-center gap-1">
              <span>Read Bio on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Transformations Grid -->
      <div class="border-t border-black/5 pt-16">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">Celebrity & Client Transformations</span>
          <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">Master Artistry by the LivArt Team</h2>
          <p class="text-xs text-muted-slate mt-2">Celebrated media personalities, news anchors, and distinguished clients styled by our certified master artists in Kakkanad.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {transformations_html}
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "about-us", "index.html"), "w") as f:
        f.write(html)
    print("✓ about-us/index.html built")

# -------------------------------------------------------------
# 2. TEAMS PAGE (/teams/)
# -------------------------------------------------------------
def build_teams_page():
    ensure_dir(os.path.join(BASE_DIR, "teams"))
    
    extra_schema = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "name": "Meet Stephy Sebastian & Master Artists at LivArt",
        "mainEntity": {
            "@type": "Person",
            "name": "Stephy Sebastian",
            "jobTitle": ["Founder & Creative Director", "Celebrity Hair & Makeup Artist", "Master Cosmetology Educator"],
            "url": ACADEMY_FOUNDER_URL,
            "image": f"{BASE_URL}/assets/images/brand/stephy-sebastian.webp",
            "description": "Stephy Sebastian is a celebrated celebrity hair stylist, bridal makeup artist, former national educator for L'Oréal Professionnel and Wella, and founder of LivArt Hair & Makeup Studio and LivArt Beauty Academy.",
            "sameAs": [
                ACADEMY_FOUNDER_URL,
                PRESS_FEATURE_URL,
                INSTAGRAM_URL,
                FACEBOOK_URL
            ]
        }
    }

    html = render_head(
        title="Meet Stephy Sebastian & Master Artists | LivArt Salon Kakkanad",
        description="Get to know Stephy Sebastian, founder of LivArt Hair & Makeup Studio and LivArt Academy. Former nurse, L'Oréal national trainer, and celebrity stylist in Kochi.",
        canonical_path="/teams/",
        extra_schema=extra_schema,
        root_prefix="../"
    )
    html += render_header(active_slug="about-us", root_prefix="../")

    transformations = [
        {"name": "Amala Shaji", "badge": "Influencer Spotlight", "service": "Permanent Blow Dry & Volume Styling", "desc": "Bouncy, effortless runway volume and structural blowout by LivArt senior stylists.", "img": "../assets/images/instagram/Db7rJBtuj4B.jpg"},
        {"name": "Azmin Yasar", "badge": "Model & Anchor", "service": "Precision Haircut & Salon Finish", "desc": "Bespoke hair shaping and salon chair blowout tailored for camera readiness.", "img": "../assets/images/instagram/DbLJRauyFro.jpg"},
        {"name": "Actress Amala Rose Kurian", "badge": "Film & Television", "service": "Hair Botox Rejuvenation Therapy", "desc": "Anti-frizz capillary deep conditioning restoring mirror-like silkiness and strength.", "img": "../assets/images/instagram/DW1NAndDGuP.jpg"},
        {"name": "Anchor Shiju Abdul Rasheed", "badge": "News Anchor", "service": "Executive Precision Haircut & Grooming", "desc": "High-definition camera-ready precision haircut and beard contouring.", "img": "../assets/images/instagram/C7l9fP5P3u9.jpg"},
        {"name": "RJ Soorya", "badge": "Radio Personality", "service": "Couture Balayage & Colouring", "desc": "Multi-dimensional L'Oreal hand-painted balayage with zero ammonia damage.", "img": "../assets/images/instagram/DABMk4mtv8b.jpg"},
        {"name": "Anchor Meenakshi Sudheer", "badge": "TV Anchor", "service": "Deluxe Foot Reflexology & Pedicure Spa", "desc": "Relaxing dead-skin exfoliation, herbal soak, and therapeutic acupressure massage.", "img": "../assets/images/instagram/C88tG9iSEKp.jpg"},
        {"name": "Model Shaluz Boon", "badge": "Fashion Model", "service": "Runway Waves & Texture Styling", "desc": "Voluminous textured curls and movement styling for high-fashion photoshoots.", "img": "../assets/images/instagram/CpsA0o_OSo5.jpg"},
        {"name": "Distinguished Groom", "badge": "Groom Sanctuary", "service": "Black Diamond Groom Makeover", "desc": "Natural matte camera-ready complexion, beard grooming, and hair architecture.", "img": "../assets/images/instagram/DXb3cLlEsmy.jpg"}
    ]

    transformations_html = ""
    for t in transformations:
        transformations_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-lg transition-all flex flex-col justify-between">
          <div class="h-64 overflow-hidden bg-obsidian-deep relative">
            <img src="{t['img']}" alt="{t['name']} - {t['service']} at LivArt Salon Kakkanad" class="w-full h-full object-cover object-top hover:scale-105 transition-transform duration-500" loading="lazy" />
            <span class="absolute top-3 left-3 bg-obsidian-deep/80 text-champagne-gold px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider backdrop-blur-sm border border-champagne-gold/20">
              {t['badge']}
            </span>
          </div>
          <div class="p-5 flex flex-col justify-between flex-grow">
            <div>
              <h3 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-1">{t['name']}</h3>
              <p class="text-xs text-warm-bronze font-bold uppercase tracking-wider mb-2">{t['service']}</p>
              <p class="text-xs text-gray-600 leading-relaxed">{t['desc']}</p>
            </div>
          </div>
        </div>
        """

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Visionaries & Master Artists</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">The Creative Minds Behind LivArt</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Stephy Sebastian and our ensemble of master artists dedicated to bringing haute couture hair and makeup to Kakkanad, Kochi.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-[1100px] mx-auto bg-surface-container-low rounded-3xl p-8 sm:p-12 border border-black/5 shadow-md grid grid-cols-1 md:grid-cols-12 gap-10 items-center mb-16">
        <div class="md:col-span-5">
          <div class="rounded-2xl overflow-hidden shadow-xl bg-obsidian-deep">
            <img src="../assets/images/brand/stephy-sebastian.webp" alt="Stephy Sebastian - Founder of LivArt Salon & Beauty Academy" class="w-full h-full object-cover" loading="lazy" />
          </div>
        </div>
        <div class="md:col-span-7">
          <span class="text-xs font-bold uppercase tracking-widest text-warm-bronze block mb-1">Founder & Creative Director</span>
          <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-2">Stephy Sebastian</h2>
          <span class="text-xs font-semibold text-champagne-gold bg-obsidian-deep px-2.5 py-0.5 rounded-full inline-block mb-4">Former National Educator L'Oréal & Wella</span>
          
          <div class="prose text-sm text-gray-700 space-y-3 leading-relaxed">
            <p>
              Stephy serves as the visionary pillar of LivArt Hair and Makeup Studio, portraying the qualities of a true stylist curated from genuine passion and love for the artistry. As a former nurse of 5 years, Stephy served in demanding medical conditions that forged her unmatched resilience and compassion—traits that make her an inspiration to all who meet her.
            </p>
            <p>
              Her transition from healthcare to hair and makeup artistry was fueled by a lifelong commitment to pursuing what she loves most. Stephy completed her master education under the industry's finest mentors and headed national technical training for global cosmetic giants <strong>L'Oréal Professionnel and Wella</strong>.
            </p>
            <p>
              In 2021, she established the <strong>LivArt Beauty Academy (<a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="underline text-obsidian-deep font-semibold">livart.co.in</a>)</strong>, affiliated with the <strong>B&WSSC (Beauty and Wellness Sector Skill Council)</strong> of India, training hundreds of emerging beauty professionals with hands-on salon floor apprenticeship.
            </p>
            <p class="italic text-obsidian-deep font-serif-luxury text-base pt-2">
              “If your mind can think it, you can achieve it. If I can, you can too.”
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-black/5 flex flex-wrap gap-3">
            <button data-open-booking data-service="Personal Consultation with Founder Stephy Sebastian" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
              Book with Stephy
            </button>
            <a href="../academy/index.html" class="bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1">
              <span class="material-symbols-outlined text-[15px]">school</span>
              <span>Beauty Academy</span>
            </a>
            <a href="{PRESS_FEATURE_URL}" target="_blank" rel="noopener noreferrer" class="border border-black/10 hover:bg-black/5 px-4 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-obsidian-deep transition-all flex items-center gap-1.5">
              <span>Business Periscope Feature</span>
              <span class="material-symbols-outlined text-[15px]">open_in_new</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Transformations Grid -->
      <div class="border-t border-black/5 pt-16">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">Celebrity & Client Transformations</span>
          <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">Master Artistry by the LivArt Team</h2>
          <p class="text-xs text-muted-slate mt-2">Celebrated media personalities, news anchors, and distinguished clients styled by our certified master artists in Kakkanad.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {transformations_html}
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "teams", "index.html"), "w") as f:
        f.write(html)
    print("✓ teams/index.html built")

# -------------------------------------------------------------
# 3. HAIR STYLING PAGE (/hair-styling/)
# -------------------------------------------------------------
def build_hair_page():
    ensure_dir(os.path.join(BASE_DIR, "hair-styling"))
    html = render_head(
        title="Best Hair Salon in Kakkanad, Kochi | Haircuts, Balayage & Hair Botox | LivArt",
        description="Top-rated hair salon in Kakkanad on Seaport-Airport Road. Precision haircuts, L'Oreal hair spa, balayage hair colouring, keratin and hair botox by master stylists.",
        canonical_path="/hair-styling/",
        root_prefix="../"
    )
    html += render_header(active_slug="hair-styling", root_prefix="../")

    hair_services = [
        ("Relaxo Hot Oil Head Massage & Spa", "Soothe your senses with a revitalizing hot oil head massage and steam infusion. Formulated to stimulate scalp micro-circulation, nourish deep hair follicles, and relieve cranial tension.", "From Rs. 700 (Member Rs. 525)", "../assets/images/instagram/CpsA0o_OSo5.jpg"),
        ("L’Oreal Professional Hair Spa", "Deep steam infusion and therapeutic acupressure massage that repairs cuticle breakdown, cures dryness, and restores lustrous mirror-like gloss.", "From Rs. 800 (Member Rs. 600)", "../assets/images/instagram/DEXOFvGTyDZ.jpg"),
        ("Balayage & Dimensional Colouring", "Hand-painted dimensional hues tailored to your undertone. Seamless transitions, soft root melting, and zero ammonia damage with L'Oreal Majirel & Inoa.", "From Rs. 2,500", "../assets/images/instagram/C5pwjmOidQU.jpg"),
        ("Precision Haircuts & Blowouts", "Structural haircutting customized to your bone structure and hair density by senior stylists or Founder Stephy Sebastian, finished with our iconic runway bouncy blowout.", "From Rs. 400 (Gents) / Rs. 800 (Women)", "../assets/images/instagram/C6F_GKgtlHk.jpg"),
        ("Hair Botox Anti-Aging Treatment", "Fills structural keratin gaps in hair strands, eliminates 95% of humidity frizz, and revitalizes damaged ends without harsh chemicals.", "Rs. 5,999 (Member Rs. 4,499)", "../assets/images/instagram/DW1NAndDGuP.jpg"),
        ("Permanent Hair Straightening & Rebonding", "Thermal rebonding and permanent straightening for mirror-like silky pin-straight hair that endures through any Kerala humidity.", "From Rs. 5,000 (Member Rs. 3,750)", "../assets/images/instagram/Db7rJBtuj4B.jpg")
    ]

    services_html = ""
    for title, desc, price, img in hair_services:
        services_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div class="h-48 overflow-hidden bg-obsidian-deep">
            <img src="{img}" alt="{title} at LivArt Salon Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-6 flex flex-col justify-between flex-grow">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze">LivArt Hair Atelier</span>
                <span class="font-serif-luxury text-base font-bold text-obsidian-deep">{price}</span>
              </div>
              <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">{title}</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-6">{desc}</p>
            </div>
            <button data-open-booking data-service="{title}" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
              Book Service
            </button>
          </div>
        </div>
        """

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Couture Hair Craft</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Best Hair Salon in Kakkanad: Haircuts, Balayage & Botox</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Welcome to LivArt Hair Atelier Kakkanad. From dimensional caramel balayage to anti-frizz Hair Botox, keratin smoothing, and relaxing L'Oréal hair spa, experience master styling 5 minutes from Infopark Kochi.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        {services_html}
      </div>

      <!-- Complete Rate Card CTA -->
      <div class="p-8 sm:p-10 bg-obsidian-deep rounded-3xl border border-champagne-gold/30 text-center max-w-3xl mx-auto shadow-2xl text-alabaster-cream">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-champagne-gold/10 border border-champagne-gold/30 text-champagne-gold text-[10px] font-bold uppercase tracking-widest mb-3">
          <span class="material-symbols-outlined text-[14px]">menu_book</span>
          <span>Official 2026 Price Menu</span>
        </div>
        <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-white mb-2">Looking for Our Complete Hair Rate Card?</h3>
        <p class="text-xs sm:text-sm text-gray-300 leading-relaxed mb-6 max-w-xl mx-auto">
          Explore all haircuts, kids styling, Kerasmooth, Botox, creative director sessions with Stephy Sebastian, and privilege member rates on our master service menu.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="../services/index.html#catalog" class="bg-champagne-gold text-obsidian-deep px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest hover:bg-white transition-all shadow-md flex items-center gap-2 font-bold">
            <span>Browse All 234 Services & Prices</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
          <a href="https://store.zylu.co/livart-salon-kakkanad" target="_blank" rel="noopener noreferrer" class="border border-white/20 hover:bg-white/10 text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center gap-1.5">
            <span>Direct Zylu Booking</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "hair-styling", "index.html"), "w") as f:
        f.write(html)
    print("✓ hair-styling/index.html built")

# -------------------------------------------------------------
# 4. MAKE-UP & BRIDAL PAGE (/make-up/)
# -------------------------------------------------------------
def build_makeup_page():
    ensure_dir(os.path.join(BASE_DIR, "make-up"))
    html = render_head(
        title="Best Bridal Makeup Artist in Kakkanad, Kochi | HD & Airbrush Studio | LivArt",
        description="Award-winning bridal makeup artist in Kakkanad, Kochi by Stephy Sebastian. Christian, Hindu, and Muslim bridal packages, saree draping, HD airbrush & groom styling.",
        canonical_path="/make-up/",
        root_prefix="../"
    )
    html += render_header(active_slug="make-up", root_prefix="../")

    packages = [
        {
            "name": "Silver Bridal Package",
            "price": "Rs. 12,000",
            "tag": "Essential Radiance",
            "inclusions": [
                "Professional HD Bridal Makeup",
                "Traditional / Contemporary Bridal Hairdo",
                "Saree Draping & Dupatta Setting",
                "Basic Pre-Bridal Glow Facial",
                "Standard False Lash Application",
                "Complimentary Change of Accessories Assistance"
            ]
        },
        {
            "name": "Gold Bridal Package",
            "price": "Rs. 18,000",
            "tag": "Most Popular",
            "popular": True,
            "inclusions": [
                "Ultra HD / Airbrush Bridal Makeup by Senior Artist",
                "Intricate Bridal Hair Styling with Fresh Flowers / Extensions",
                "Designer Saree Draping & Silhouette Setting",
                "Skin Miracle Hydra Glow Facial (Pre-Wedding)",
                "Deluxe Manicure & Pedicure",
                "Premium Mink Lash Application",
                "Full Touch-Up Kit for the Ceremony"
            ]
        },
        {
            "name": "Diamond Bridal Couture Package",
            "price": "Rs. 25,000",
            "tag": "Haute Couture by Stephy Sebastian",
            "inclusions": [
                "Direct Makeup Artistry by Founder Stephy Sebastian",
                "High-Definition Waterproof Airbrush Makeup",
                "Full Pre-Wedding Trial Session Included",
                "Signature Skin Miracle Whitening & De-Tan Therapy",
                "L'Oreal Lustrous Hair Spa Scalp Rejuvenation",
                "Luxury Deluxe Pedicure, Manicure & Nail Gel Art",
                "Complete Saree Draping & Veil Pinning",
                "Dedicated On-Location Artist Support for 4 Hours"
            ]
        },
        {
            "name": "Black Diamond Groom Package",
            "price": "Rs. 7,500",
            "tag": "Distinguished Groom",
            "inclusions": [
                "Signature Groom Haircut, Precision Beard Design & Styling",
                "Instant De-Tan & Complexion Revitalization Facial",
                "Relaxo Hot Oil Scalp & Shoulder Massage",
                "Groom Natural Camera-Ready Matte Finish Makeup",
                "Deluxe Hand & Foot Grooming / Pedicure",
                "Styling Consultation & Groom Attire Setting"
            ]
        }
    ]

    pkgs_html = ""
    for p in packages:
        pop_border = "border-2 border-champagne-gold shadow-2xl relative" if p.get("popular") else "border border-black/5 shadow-sm"
        badge = f'<span class="absolute -top-3 left-1/2 -translate-x-1/2 bg-champagne-gold text-obsidian-deep px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest">{p["tag"]}</span>' if p.get("popular") else f'<span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze mb-1 block">{p["tag"]}</span>'
        
        inc_html = "".join([f'<li class="flex items-start gap-2 text-xs text-gray-700"><span class="material-symbols-outlined text-[16px] text-champagne-gold shrink-0">check_circle</span><span>{inc}</span></li>' for inc in p["inclusions"]])

        pkgs_html += f"""
        <div class="bg-surface-container-low rounded-3xl p-8 flex flex-col justify-between {pop_border}">
          <div>
            {badge}
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">{p['name']}</h3>
            <div class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-6">{p['price']}</div>
            <ul class="space-y-3 mb-8 border-t border-black/5 pt-6">
              {inc_html}
            </ul>
          </div>
          <button data-open-booking data-service="{p['name']}" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all">
            Reserve Package
          </button>
        </div>
        """

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Bespoke Bridal Sanctuary</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Best Bridal Makeup Artist & Makeover Studio in Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Curated by Stephy Sebastian. Flawless 4K Ultra-HD, airbrush waterproof bridal makeup, bespoke saree draping, and pre-bridal packages in Kakkanad, Kochi.
      </p>
    </div>
  </section>

  <!-- BRIDAL TRADITIONS SHOWCASE -->
  <section class="py-14 bg-ivory-surface border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">
          Atelier Bridal Masterpieces
        </span>
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">
          Four Traditions of Bridal Artistry
        </h2>
        <p class="text-xs text-muted-slate mt-2">
          From sacred rituals to modern cocktail celebrations, Stephy Sebastian curates timeless bridal aesthetics tailored to every community and cultural tradition.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- 1. Christian Bridal Couture -->
        <div class="group bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col">
          <div class="aspect-[3/4] overflow-hidden bg-obsidian-deep relative">
            <img src="../assets/images/instagram/DYuASLuK_le.jpg" alt="Christian Bridal Makeover by Stephy Sebastian LivArt Kakkanad" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/80 via-transparent to-transparent"></div>
            <div class="absolute bottom-3 left-3 right-3 text-alabaster-cream">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block">Church Ceremony</span>
              <h3 class="font-serif-luxury text-lg font-bold">Christian Bridal Couture</h3>
            </div>
          </div>
          <div class="p-4 flex-grow flex flex-col justify-between">
            <p class="text-xs text-gray-600 leading-relaxed mb-3">
              Porcelain dewy skin, romantic soft smoky eyes, and meticulous cathedral veil anchoring designed to photograph exquisitely in church illumination.
            </p>
            <span class="text-[11px] font-bold text-warm-bronze uppercase tracking-wider">Diamond & Gold Packages</span>
          </div>
        </div>

        <!-- 2. Traditional Hindu Muhurtham -->
        <div class="group bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col">
          <div class="aspect-[3/4] overflow-hidden bg-obsidian-deep relative">
            <img src="../assets/images/instagram/DULWym5CHa0.jpg" alt="Traditional Hindu Muhurtham Bridal Makeup & Saree Draping LivArt" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/80 via-transparent to-transparent"></div>
            <div class="absolute bottom-3 left-3 right-3 text-alabaster-cream">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block">Sacred Muhurtham</span>
              <h3 class="font-serif-luxury text-lg font-bold">Hindu Muhurtham Radiance</h3>
            </div>
          </div>
          <div class="p-4 flex-grow flex flex-col justify-between">
            <p class="text-xs text-gray-600 leading-relaxed mb-3">
              Traditional South Indian gold eye shimmer, fresh jasmine hair braiding, and immaculate silk Kanchipuram saree pleating.
            </p>
            <span class="text-[11px] font-bold text-warm-bronze uppercase tracking-wider">Diamond & Gold Packages</span>
          </div>
        </div>

        <!-- 3. Muslim Nikah Elegance -->
        <div class="group bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col">
          <div class="aspect-[3/4] overflow-hidden bg-obsidian-deep relative">
            <img src="../assets/images/instagram/DTc2O2fCFZI.jpg" alt="Muslim Nikah Bespoke Bridal Makeup LivArt Salon Kochi" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/80 via-transparent to-transparent"></div>
            <div class="absolute bottom-3 left-3 right-3 text-alabaster-cream">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block">Nikah Ceremony</span>
              <h3 class="font-serif-luxury text-lg font-bold">Muslim Nikah Elegance</h3>
            </div>
          </div>
          <div class="p-4 flex-grow flex flex-col justify-between">
            <p class="text-xs text-gray-600 leading-relaxed mb-3">
              Flawless waterproof airbrush base, dramatic winged liner, and regal tiara and dupatta setting for majestic Nikah poise.
            </p>
            <span class="text-[11px] font-bold text-warm-bronze uppercase tracking-wider">Diamond & Gold Packages</span>
          </div>
        </div>

        <!-- 4. Evening Reception Glamour -->
        <div class="group bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col">
          <div class="aspect-[3/4] overflow-hidden bg-obsidian-deep relative">
            <img src="../assets/images/instagram/DX6qGl_SKf1.jpg" alt="Red Carpet Reception Glamour Makeup LivArt Salon Kakkanad" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/80 via-transparent to-transparent"></div>
            <div class="absolute bottom-3 left-3 right-3 text-alabaster-cream">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block">Cocktail & Party</span>
              <h3 class="font-serif-luxury text-lg font-bold">Evening Reception Glam</h3>
            </div>
          </div>
          <div class="p-4 flex-grow flex flex-col justify-between">
            <p class="text-xs text-gray-600 leading-relaxed mb-3">
              Sculpted cheekbone contouring, high-impact evening eyes, and tousled Hollywood waves crafted to turn heads on the dance floor.
            </p>
            <span class="text-[11px] font-bold text-warm-bronze uppercase tracking-wider">Reception Glamour Package</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PACKAGES PRICING SECTION -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-xl mx-auto mb-12">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">Couture Offerings</span>
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">Signature Bridal & Groom Packages</h2>
        <p class="text-xs text-muted-slate mt-2">Comprehensive bridal and groom regimens combining skincare prep, hair artistry, and high-definition makeup.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {pkgs_html}
      </div>

      <div class="mt-16 p-8 bg-ivory-surface rounded-3xl border border-black/5 text-center max-w-3xl mx-auto mb-16">
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Planning a Destination Wedding in Kerala?</h3>
        <p class="text-xs text-gray-600 leading-relaxed mb-6">
          Stephy Sebastian and her senior bridal team travel for destination weddings across Kochi, Kumarakom, Munnar, and Kovalam. We customize group styling for bridesmaids and family members.
        </p>
        <button data-open-booking data-service="Destination Bridal Consultation" class="bg-champagne-gold text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold uppercase tracking-widest hover:bg-metallic-gold-light transition-all shadow-md">
          Request Destination Bridal Quote
        </button>
      </div>

      <!-- A La Carte Bridal & Makeup Rate Card (Direct from Zylu) -->
      <div class="p-8 sm:p-12 bg-obsidian-deep rounded-3xl border border-champagne-gold/30 shadow-2xl text-alabaster-cream">
        <div class="text-center max-w-2xl mx-auto mb-10">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-champagne-gold/10 border border-champagne-gold/30 text-champagne-gold text-[10px] font-bold uppercase tracking-widest mb-3">
            <span class="material-symbols-outlined text-[14px]">verified</span>
            <span>Official 2026 Atelier Rate Card • Zylu Verified</span>
          </div>
          <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-white mb-2">A La Carte Bridal & Event Makeup Menu</h3>
          <p class="text-xs sm:text-sm text-gray-300">
            Direct pricing for individual wedding functions, party makeovers, and professional saree draping.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
          <div class="bg-obsidian-surface p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-champagne-gold uppercase tracking-wider">Indoor Ceremony</span>
                <span class="text-xs font-bold text-emerald-400">Save ₹6,250 with Grand Card</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">HD Bridal Makeup (Indoor)</h4>
              <p class="text-xs text-gray-400 mb-4">4K camera-ready base, eye artistry, lash application & setting.</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹25,000</span>
              <span class="text-xs text-gray-400">Member: ₹18,750</span>
            </div>
          </div>

          <div class="bg-obsidian-surface p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-champagne-gold uppercase tracking-wider">Outdoor Venue</span>
                <span class="text-xs font-bold text-gray-400">Natural Daylight Prep</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">HD Bridal Makeup (Outdoor)</h4>
              <p class="text-xs text-gray-400 mb-4">Waterproof, sweat-resistant formulation for outdoor Kerala climates.</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹30,000</span>
              <span class="text-xs text-gray-400">Member: ₹22,500</span>
            </div>
          </div>

          <div class="bg-obsidian-surface p-5 rounded-2xl border border-champagne-gold/40 flex flex-col justify-between relative">
            <span class="absolute -top-2.5 right-4 bg-champagne-gold text-obsidian-deep text-[9px] font-bold uppercase px-2 py-0.5 rounded-full">Haute Couture</span>
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-champagne-gold uppercase tracking-wider">Airbrush Luxury</span>
                <span class="text-xs font-bold text-gray-400">Flawless 16hr Wear</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">Airbrush Bridal Makeup</h4>
              <p class="text-xs text-gray-400 mb-4">Micro-misted silicone-based pigment. Weightless and transfer-proof.</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹50,000</span>
              <span class="text-xs text-gray-400">Outdoor: ₹60,000</span>
            </div>
          </div>

          <div class="bg-obsidian-surface p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">Pre-Wedding Event</span>
                <span class="text-xs font-bold text-gray-400">Indoor / Outdoor</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">Engagement & Haldi Makeup</h4>
              <p class="text-xs text-gray-400 mb-4">Vibrant, luminous aesthetics crafted for engagement & Haldi celebrations.</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹15,000</span>
              <span class="text-xs text-gray-400">Outdoor: ₹20,000</span>
            </div>
          </div>

          <div class="bg-obsidian-surface p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">Guest & Party</span>
                <span class="text-xs font-bold text-gray-400">Event Glamour</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">Party & Minimal Makeup</h4>
              <p class="text-xs text-gray-400 mb-4">Red-carpet party glam or soft subtle dewy minimal makeup for bridesmaids.</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹2,500 – ₹5,000</span>
              <span class="text-xs text-gray-400">Groom: ₹5,000</span>
            </div>
          </div>

          <div class="bg-obsidian-surface p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">Draping Craft</span>
                <span class="text-xs font-bold text-gray-400">Precision Pleating</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-white mb-1">Saree Draping & Styling</h4>
              <p class="text-xs text-gray-400 mb-4">Pre-pleated draping (₹1,000), box folding (₹1,000), or on-client draping (₹1,500).</p>
            </div>
            <div class="flex items-baseline justify-between pt-3 border-t border-white/10">
              <span class="text-xl font-bold text-champagne-gold">₹1,000 – ₹1,500</span>
              <span class="text-xs text-gray-400">Member from: ₹750</span>
            </div>
          </div>
        </div>

        <div class="text-center pt-6 border-t border-white/10 flex flex-wrap items-center justify-center gap-4">
          <a href="../services/index.html#catalog" class="bg-champagne-gold text-obsidian-deep px-8 py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest hover:bg-white transition-all shadow-md flex items-center gap-2">
            <span>Browse Complete 234 Service Menu</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
          <button data-open-booking data-service="Hd Makeup (Indoor)" class="border border-white/20 hover:bg-white/10 text-white px-6 py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all">
            Book Bridal Consultation
          </button>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "make-up", "index.html"), "w") as f:
        f.write(html)
    print("✓ make-up/index.html built")

# -------------------------------------------------------------
# 5. SKIN CARE PAGE (/skin-care/) — 100% CLEAN OF SPAM
# -------------------------------------------------------------
def build_skincare_page():
    ensure_dir(os.path.join(BASE_DIR, "skin-care"))
    html = render_head(
        title="Best Skin Care Clinic & Beauty Parlour in Kakkanad | Hydra Facial & De-Tan | LivArt",
        description="Advanced Hydra facials, de-tan whitening treatments, Cheryl's pro facials, and luxury pedicures at LivArt Salon Kakkanad. Reveal radiant, healthy skin.",
        canonical_path="/skin-care/",
        root_prefix="../"
    )
    html += render_header(active_slug="skin-care", root_prefix="../")

    skin_services = [
        ("Skin Miracle Hydra Facial", "Our advanced vortex extraction and hyaluronic infusion facial that clears congestion and restores dewy glass-skin luminosity.", "Rs. 4,000 (Member Rs. 3,000)", "../assets/images/instagram/DRXFRQCEgpm.jpg"),
        ("De-Tan + Skin Miracle Combo", "Signature dual ritual that erases sun tanning, lightens pigment spots, and floods the dermis in brightening vitamins.", "From Rs. 2,499", "../assets/images/offers/offer-poster1.webp"),
        ("O3+ Whitening & Brightening Facial", "Clinical brightening formulation with high-potency Vitamin C and botanical actives to reverse tropical pigmentation and dullness.", "Rs. 3,000 (Member Rs. 2,250)", "../assets/images/instagram/DIYwMqNSFPo.jpg"),
        ("Deluxe Manicure & Pedicure Spa", "Deep dead-skin exfoliation, cuticle conditioning, relaxing foot reflexology massage, and precision nail shaping.", "From Rs. 1,000 (Member Rs. 750)", "../assets/images/instagram/C88tG9iSEKp.jpg"),
        ("Herbal Waxing & Threading", "Painless threading for brows and facial contours, alongside gentle honey and chocolate wax formulations that prevent irritation.", "From Rs. 100", "../assets/images/instagram/Da8Hb68SA5B.jpg"),
        ("Casmara Spanish Luxury Facials", "World-renowned Casmara algae peel-off masks, retinol renewal, and antioxidant purifying therapies from Spain.", "From Rs. 5,000", "../assets/images/instagram/DIoW2P5TF7G.jpg")
    ]

    services_html = ""
    for title, desc, price, img in skin_services:
        services_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div class="h-48 overflow-hidden bg-obsidian-deep">
            <img src="{img}" alt="{title} at LivArt Salon Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-6 flex flex-col justify-between flex-grow">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze">Clinical Skincare</span>
                <span class="font-serif-luxury text-base font-bold text-obsidian-deep">{price}</span>
              </div>
              <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">{title}</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-6">{desc}</p>
            </div>
            <button data-open-booking data-service="{title}" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
              Book Treatment
            </button>
          </div>
        </div>
        """

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Clinical Dermal Aesthetics</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Clinical Skincare, Hydra Facials & Beauty Parlour in Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Discover exceptional skincare services designed to enhance cellular health and reveal radiant luminosity. Medical-grade Hydra facials, de-tan whitening, Cheryl's cosmeceuticals, and deluxe pedicures 5 minutes from Infopark.
      </p>
    </div>
  </section>

  <!-- Loyalty Program Callout Banner (Official Club LivArt Tiers) -->
  <section class="w-full bg-gold-gradient py-6">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-obsidian-deep text-champagne-gold flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-[24px]">verified</span>
        </div>
        <div>
          <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep">Club LivArt Privilege Membership Cards</h3>
          <p class="text-xs text-black/80 font-medium">
            Join Club LivArt and enjoy <strong>up to 25% OFF</strong> all 234 salon treatments, hair spa, and clinical skincare for 1 full year. Grand, Premium, and Classic tiers available.
          </p>
        </div>
      </div>
      <a href="../packages/index.html#memberships" class="shrink-0 bg-obsidian-deep text-white hover:bg-obsidian-surface px-6 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
        Explore Privilege Cards
      </a>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        {services_html}
      </div>

      <!-- Complete Rate Card CTA -->
      <div class="p-8 sm:p-10 bg-obsidian-deep rounded-3xl border border-champagne-gold/30 text-center max-w-3xl mx-auto shadow-2xl text-alabaster-cream">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-champagne-gold/10 border border-champagne-gold/30 text-champagne-gold text-[10px] font-bold uppercase tracking-widest mb-3">
          <span class="material-symbols-outlined text-[14px]">menu_book</span>
          <span>Official 2026 Price Menu</span>
        </div>
        <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-white mb-2">Looking for Our Complete Skincare Rate Card?</h3>
        <p class="text-xs sm:text-sm text-gray-300 leading-relaxed mb-6 max-w-xl mx-auto">
          Explore all 234 treatments: Cheryl's pro facials, Casmara luxury algae treatments, Hydra Facial tiers, de-tan therapies, body waxing, and privilege rates.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="../services/index.html#catalog" class="bg-champagne-gold text-obsidian-deep px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest hover:bg-white transition-all shadow-md flex items-center gap-2 font-bold">
            <span>Browse All 234 Services & Prices</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
          <a href="https://store.zylu.co/livart-salon-kakkanad" target="_blank" rel="noopener noreferrer" class="border border-white/20 hover:bg-white/10 text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center gap-1.5">
            <span>Direct Zylu Booking</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "skin-care", "index.html"), "w") as f:
        f.write(html)
    print("✓ skin-care/index.html built (clean & sanitized)")

# -------------------------------------------------------------
# 6. PACKAGES PAGE (/packages/)
# -------------------------------------------------------------
def build_packages_page():
    ensure_dir(os.path.join(BASE_DIR, "packages"))
    html = render_head(
        title="Best Salon Packages & Offers in Kakkanad, Kochi | LivArt Salon",
        description="Explore exclusive beauty, hair, pre-bridal, and groom packages at LivArt Salon Kakkanad. Includes complimentary 1-Year 20% privilege membership card.",
        canonical_path="/packages/",
        root_prefix="../"
    )
    html += render_header(active_slug="packages", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Curated Value Rituals</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Best Salon Packages & Exclusive Offers in Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Transparent, all-inclusive luxury salon packages combining our highest-rated hair therapies, bridal glamour, and restorative facials on Seaport-Airport Road.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Combo Packages Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
        <!-- Package 1 -->
        <div class="bg-surface-container-low rounded-3xl p-8 border border-black/5 flex flex-col justify-between">
          <div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">Glow & Rejuvenate</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Radiance Duo Combo</h3>
            <div class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-4">Rs. 2,499 <span class="text-xs text-muted-slate line-through font-normal">Rs. 4,200</span></div>
            <p class="text-xs text-gray-600 mb-6">The perfect monthly reset for glowing skin and manageable hair.</p>
            <ul class="space-y-3 text-xs text-gray-700 border-t border-black/5 pt-6 mb-8">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Complete De-Tan Face & Neck Therapy</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Skin Miracle Whitening Facial</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Scalp Pressure Release Massage</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Free 1-Year 20% Privilege Card</li>
            </ul>
          </div>
          <button data-open-booking data-service="Radiance Duo Combo (Rs. 2499)" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all">
            Book Combo
          </button>
        </div>

        <!-- Package 2 -->
        <div class="bg-surface-container-low rounded-3xl p-8 border-2 border-champagne-gold shadow-2xl relative flex flex-col justify-between">
          <span class="absolute -top-3 left-1/2 -translate-x-1/2 bg-champagne-gold text-obsidian-deep px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest">Atelier Bestseller</span>
          <div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">Hair Silk Rebirth</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Total Hair Botox & Spa</h3>
            <div class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-4">Rs. 6,999 <span class="text-xs text-muted-slate line-through font-normal">Rs. 9,500</span></div>
            <p class="text-xs text-gray-600 mb-6">Complete frizz reversal and cuticle rebuilding for silky manageability.</p>
            <ul class="space-y-3 text-xs text-gray-700 border-t border-black/5 pt-6 mb-8">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Full Length Hair Botox Treatment</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> L'Oreal Steam Scalp Infusion Spa</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Haircut & Bouncy Blow Dry</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Free 1-Year 20% Privilege Card</li>
            </ul>
          </div>
          <button data-open-booking data-service="Total Hair Botox & Spa (Rs. 6999)" class="w-full bg-champagne-gold hover:bg-obsidian-deep text-obsidian-deep hover:text-white py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all">
            Book Hair Package
          </button>
        </div>

        <!-- Package 3 -->
        <div class="bg-surface-container-low rounded-3xl p-8 border border-black/5 flex flex-col justify-between">
          <div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">Bridal & Special Occasions</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Pre-Bridal Luxury Sanctum</h3>
            <div class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-4">Rs. 8,999 <span class="text-xs text-muted-slate line-through font-normal">Rs. 13,000</span></div>
            <p class="text-xs text-gray-600 mb-6">Designed to prepare brides and party hosts 1 to 2 weeks before the big date.</p>
            <ul class="space-y-3 text-xs text-gray-700 border-t border-black/5 pt-6 mb-8">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Skin Miracle Hydra Facial Aesthetics</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Full Arms, Legs & Back Herbal Waxing</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> Deluxe Spa Manicure & Pedicure</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check</span> L'Oreal Lustrous Hair Spa & Trim</li>
            </ul>
          </div>
          <button data-open-booking data-service="Pre-Bridal Luxury Sanctum (Rs. 8999)" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all">
            Book Pre-Bridal Sanctum
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- CLUB LIVART PRIVILEGE MEMBERSHIPS (OFFICIAL ZYLU TIERS) -->
  <section class="py-20 bg-obsidian-deep text-alabaster-cream border-t border-champagne-gold/20" id="memberships">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
          Exclusive Atelier Club
        </span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
          Club LivArt Privilege Cards
        </h2>
        <p class="text-sm sm:text-base text-gray-300 leading-relaxed">
          Unlock wholesale savings across all 234 salon treatments, styling sessions, and bridal rituals for a full 365 days. Synced seamlessly to your client profile in our Zylu system.
        </p>
      </div>

      <!-- Membership Tiers Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch mb-12">
        
        <!-- Tier 1: Classic 10% -->
        <div class="bg-obsidian-surface rounded-3xl p-8 border border-white/10 hover:border-white/20 shadow-xl flex flex-col justify-between transition-all">
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-gray-400 bg-white/5 px-3 py-1 rounded-full border border-white/10">Everyday Grooming</span>
              <span class="text-xs text-champagne-gold font-bold">1-Year Pass</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-white mb-2">Classic Privilege</h3>
            <div class="font-serif-luxury text-3xl sm:text-4xl font-bold text-white mb-4">
              ₹1,000 <span class="text-xs text-gray-400 font-normal">/ year</span>
            </div>
            <p class="text-xs text-gray-400 mb-6 leading-relaxed">
              Ideal for regular haircuts, beard shaping, blowouts, and monthly salon upkeep.
            </p>
            <ul class="space-y-3 text-xs text-gray-300 border-t border-white/10 pt-6 mb-8">
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span><strong>10% OFF</strong> all haircuts, beard & hair styling</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span><strong>10% OFF</strong> threading, waxing & cleanups</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span>Valid on all 234 treatments for 1 full year</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span>No minimum visits or restrictions</span>
              </li>
            </ul>
          </div>
          <button onclick="openBookingModal('Classic 10% Privilege Card (₹1,000/yr)')" class="w-full bg-white/10 hover:bg-white/20 active:scale-95 text-white py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all border border-white/20">
            Get Classic Card
          </button>
        </div>

        <!-- Tier 2: Grand 25% (Featured) -->
        <div class="bg-obsidian-surface rounded-3xl p-8 border-2 border-champagne-gold shadow-2xl relative flex flex-col justify-between transition-all transform lg:-translate-y-2">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-champagne-gold text-obsidian-deep px-4 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest shadow-lg flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">star</span>
            <span>Most Popular • Maximum Savings</span>
          </div>
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/20 px-3 py-1 rounded-full border border-champagne-gold/40">VIP Atelier Tier</span>
              <span class="text-xs text-champagne-gold font-bold">1-Year Pass</span>
            </div>
            <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-white mb-2">Grand Privilege</h3>
            <div class="font-serif-luxury text-3xl sm:text-4xl font-bold text-champagne-gold mb-4">
              ₹3,000 <span class="text-xs text-gray-400 font-normal">/ year</span>
            </div>
            <p class="text-xs text-gray-300 mb-6 leading-relaxed">
              Our highest tier VIP card. Pays for itself in a single bridal booking or chemical therapy.
            </p>
            <ul class="space-y-3 text-xs text-gray-200 border-t border-white/10 pt-6 mb-8">
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">verified</span>
                <span><strong>Save ₹6,250</strong> on HD Bridal (₹18,750 vs ₹25,000)</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">verified</span>
                <span><strong>Save ₹1,250</strong> on Smoothing/Rebonding (₹3,750 vs ₹5,000)</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">verified</span>
                <span><strong>Save ₹750</strong> on O3+ Whitening Facial (₹2,250 vs ₹3,000)</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">verified</span>
                <span><strong>Flat 25% OFF</strong> all 234 treatments for 365 days</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">verified</span>
                <span>Priority peak-weekend appointment scheduling</span>
              </li>
            </ul>
          </div>
          <button onclick="openBookingModal('Grand 25% Privilege Card (₹3,000/yr)')" class="w-full bg-champagne-gold hover:bg-white active:scale-95 text-obsidian-deep py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all shadow-xl font-bold">
            Get Grand 25% Card
          </button>
        </div>

        <!-- Tier 3: Premium 15% -->
        <div class="bg-obsidian-surface rounded-3xl p-8 border border-white/10 hover:border-white/20 shadow-xl flex flex-col justify-between transition-all">
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-gray-400 bg-white/5 px-3 py-1 rounded-full border border-white/10">Frequent Visitor</span>
              <span class="text-xs text-champagne-gold font-bold">1-Year Pass</span>
            </div>
            <h3 class="font-serif-luxury text-2xl font-bold text-white mb-2">Premium Privilege</h3>
            <div class="font-serif-luxury text-3xl sm:text-4xl font-bold text-white mb-4">
              ₹2,000 <span class="text-xs text-gray-400 font-normal">/ year</span>
            </div>
            <p class="text-xs text-gray-400 mb-6 leading-relaxed">
              Designed for clients who indulge monthly in revitalizing hair spa, coloring, and facials.
            </p>
            <ul class="space-y-3 text-xs text-gray-300 border-t border-white/10 pt-6 mb-8">
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span><strong>15% OFF</strong> all hair spa & scalp therapy</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span><strong>15% OFF</strong> hair colouring, balayage & highlights</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span><strong>15% OFF</strong> all clinical facials & aesthetics</span>
              </li>
              <li class="flex items-center gap-2.5">
                <span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span>
                <span>Valid across all 234 salon services for 1 year</span>
              </li>
            </ul>
          </div>
          <button onclick="openBookingModal('Premium 15% Privilege Card (₹2,000/yr)')" class="w-full bg-white/10 hover:bg-white/20 active:scale-95 text-white py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all border border-white/20">
            Get Premium Card
          </button>
        </div>

      </div>

      <!-- Quick Zylu Store Link Callout -->
      <div class="text-center">
        <p class="text-xs text-gray-400">
          Already a LivArt client? Check your active membership status and book online anytime at 
          <a href="https://store.zylu.co/livart-salon-kakkanad" target="_blank" rel="noopener noreferrer" class="text-champagne-gold hover:underline font-bold">store.zylu.co/livart-salon-kakkanad ↗</a>
        </p>
      </div>

    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "packages", "index.html"), "w") as f:
        f.write(html)
    print("✓ packages/index.html built")

# -------------------------------------------------------------
# 7. GALLERY & INSTAGRAM SHOWCASE (/gallery/)
# -------------------------------------------------------------
def build_gallery_page():
    ensure_dir(os.path.join(BASE_DIR, "gallery"))
    html = render_head(
        title="Gallery & Instagram Reels | LivArt Salon Kakkanad Kochi",
        description="Explore real client transformations, bridal looks, balayage colors, and Instagram reels from LivArt Salon & Makeup Studio Kakkanad (@Livart_salon).",
        canonical_path="/gallery/",
        root_prefix="../"
    )
    html += render_header(active_slug="gallery", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Visual Portfolio & Reels</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">LivArt Atelier Gallery</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Our camera captures what words cannot describe. Real brides, real hair transformations, and behind-the-scenes artistry from our Kakkanad studio.
      </p>
      <div class="mt-6 flex justify-center gap-4">
        <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white px-6 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider hover:opacity-90 transition-all shadow-lg">
          <span>Follow {INSTAGRAM_HANDLE} on Instagram</span>
          <span class="material-symbols-outlined text-[16px]">open_in_new</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Editorial Photography Showcase -->
  <section class="py-12 bg-ivory-surface border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">Curated Portfolio</span>
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">Editorial Bridal & Hair Masterpieces</h2>
        <p class="text-xs text-muted-slate mt-2">A high-definition glimpse into signature bridal traditions and hair color artistry handcrafted at LivArt.</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <!-- Photo 1: Muslim Bride -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/DTc2O2fCFZI.jpg" alt="Haute Couture Muslim Nikah Bride LivArt Kakkanad" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Nikah Bride</span>
            <span class="text-xs font-bold font-serif-luxury">Bespoke Bridal Elegance</span>
          </div>
        </div>
        <!-- Photo 2: Reception Glam -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/DX6qGl_SKf1.jpg" alt="Evening Reception Glamour LivArt Salon Kochi" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Reception Glam</span>
            <span class="text-xs font-bold font-serif-luxury">Red Carpet Shimmer</span>
          </div>
        </div>
        <!-- Photo 3: Hindu Bride -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/DULWym5CHa0.jpg" alt="Traditional Hindu Muhurtham Bride LivArt" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Muhurtham Bride</span>
            <span class="text-xs font-bold font-serif-luxury">Temple Gold Radiance</span>
          </div>
        </div>
        <!-- Photo 4: Christian Bride -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/DYuASLuK_le.jpg" alt="Christian Bridal Lace & Veil Styling LivArt" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Christian Bride</span>
            <span class="text-xs font-bold font-serif-luxury">Porcelain Lace Veil</span>
          </div>
        </div>
        <!-- Photo 5: Hair Styling -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/C5pwjmOidQU.jpg" alt="Couture Balayage and Hair Styling at LivArt Salon Kakkanad" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Couture Balayage</span>
            <span class="text-xs font-bold font-serif-luxury">L'Oreal Caramel Curls</span>
          </div>
        </div>
        <!-- Photo 6: Balayage -->
        <div class="group aspect-[3/4] rounded-2xl overflow-hidden shadow-md bg-obsidian-deep relative">
          <img src="../assets/images/instagram/Db7rJBtuj4B.jpg" alt="Precision Runway Blowout and Layered Cut Amala Shaji LivArt" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy" />
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-3 text-alabaster-cream">
            <span class="text-[9px] font-bold uppercase tracking-wider text-champagne-gold">Runway Blowout</span>
            <span class="text-xs font-bold font-serif-luxury">Precision Layered Finish</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Feed Section -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-8 text-center">
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-2">Featured Instagram Reels & Client Transformations</h2>
        <p class="text-xs text-muted-slate mb-6">Click any reel to watch, read styling details, and instantly book that exact look with our stylists.</p>
        
        <!-- Touch-Friendly Category Filter Tabs (Swipeable on Mobile) -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar touch-scroll py-2 px-1 -mx-4 px-4 sm:mx-0 sm:justify-center">
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
      </div>

      <div id="instagram-feed-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-6 gap-4 sm:gap-6">
        <!-- Populated via assets/js/instagram-feed.js -->
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "gallery", "index.html"), "w") as f:
        f.write(html)
    print("✓ gallery/index.html built")

# -------------------------------------------------------------
# 8. CONTACT US PAGE (/contact-us/)
# -------------------------------------------------------------
def build_contact_page():
    ensure_dir(os.path.join(BASE_DIR, "contact-us"))
    html = render_head(
        title="Salon Near Me in Kakkanad, Kochi | Contact, Location & Hours | LivArt Salon",
        description="Visit LivArt Salon at Anchorage Business Center, Seaport-Airport Road, Kakkanad. 5 mins from Infopark & SmartCity Kochi. Call +91 70120 59591 to book.",
        canonical_path="/contact-us/",
        root_prefix="../"
    )
    html += render_header(active_slug="contact-us", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Concierge & Studio</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Connect With LivArt Salon Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Come to us & get sharp. We are located on Seaport-Airport Road in Kakkanad, just 5 minutes from Infopark Phase 1 & 2 and SmartCity Kochi.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <!-- Form Left -->
        <div class="lg:col-span-7 bg-surface-container-low p-8 sm:p-10 rounded-3xl border border-black/5 shadow-sm">
          <h2 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-obsidian-deep mb-2">Send Us a Message</h2>
          <p class="text-xs text-muted-slate mb-6">Our concierge desk will respond within 15 minutes during operating hours.</p>

          <form id="reservation-form" class="flex flex-col gap-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Your Name</label>
                <input type="text" id="book-name" required placeholder="Maya Kurian" class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
              </div>
              <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Phone Number</label>
                <input type="tel" id="book-phone" required placeholder="+91 98765 43210" class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Select Service</label>
              <select id="book-service" class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5">
                <option value="De-Tan + Skin Miracle Whitening Combo (Rs. 2499)">De-Tan + Skin Miracle Whitening Combo (Rs. 2,499)</option>
                <option value="Hair Botox Treatment (Rs. 5999)">Anti-Frizz Hair Botox Rejuvenation (Rs. 5,999 | Member Rs. 4,499)</option>
                <option value="Permanent Blow Dry (Rs. 5999)">Permanent Blow Dry & Volume (Rs. 5,999)</option>
                <option value="Skin Miracle Hydra Facial (Rs. 4000)">Skin Miracle Hydra Facial (Rs. 4,000 | Member Rs. 3,000)</option>
                <option value="Livart Majestic Keratin Treatment (From Rs. 5000)">LivArt Majestic Keratin Smoothing (From Rs. 5,000 | Member Rs. 3,750)</option>
                <option value="Livart Permanent Hair Straightening (From Rs. 4000)">Permanent Hair Straightening / Rebonding (From Rs. 5,000 | Member Rs. 3,750)</option>
                <option value="Loreal Hair Spa For Men Short">L'Oreal / Matrix Hair Spa Scalp Therapy (From Rs. 700 | Member Rs. 525)</option>
                <option value="Hair Colouring Artistry (From Rs. 5999)">L'Oreal Hair Colouring & Balayage (From Rs. 2,500)</option>
                <option value="Women Layer Cut / Styling">Women Haircut & Runway Styling (From Rs. 800 | Member Rs. 600)</option>
                <option value="Gents Haircut & Grooming">Men's Precision Haircut & Beard (From Rs. 400 | Member Rs. 300)</option>
                <option value="O3+ Whitening Facial (Rs. 3000)">O3+ Whitening / Brightening Facial (Rs. 3,000 | Member Rs. 2,250)</option>
                <option value="Anti-Aging Facial (Rs. 4000)">Anti-Aging Collagen Facial (Rs. 4,000 | Member Rs. 3,000)</option>
                <option value="Casmara Luxury Facial Treatment">Casmara Spanish Luxury Facial (From Rs. 5,000)</option>
                <option value="Silver Bridal Package">Silver Bridal Package (Rs. 12,000)</option>
                <option value="Gold Bridal Package">Gold Bridal Package (Rs. 18,000)</option>
                <option value="Diamond Bridal Couture Package">Diamond Bridal Couture Package (Rs. 25,000)</option>
                <option value="Hd Makeup (Indoor)">Signature HD Bridal Artistry (Rs. 25,000 | Member Rs. 18,750)</option>
                <option value="Air Brush Makeup (Indoor)">Airbrush HD Bridal Luxury (Rs. 50,000)</option>
                <option value="Grand 25% Privilege Card (₹3,000/yr)">Club LivArt Grand 25% Privilege Card (₹3,000/yr)</option>
                <option value="Personal Consultation with Founder Stephy Sebastian">Personal Consultation with Founder Stephy Sebastian</option>
                <option value="LivArt Beauty Academy Beautician Courses Admission">LivArt Beauty Academy Beautician Courses Admission</option>
              </select>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Preferred Date</label>
                <input type="date" id="book-date" required class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5" />
              </div>
              <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Preferred Time Window</label>
                <select id="book-time" class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5">
                  <option>Morning: 10:00 AM – 1:00 PM</option>
                  <option>Afternoon: 1:00 PM – 4:30 PM</option>
                  <option>Evening: 4:30 PM – 7:30 PM</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-wider text-obsidian-deep mb-1">Notes / Preferences</label>
              <textarea id="book-notes" rows="3" placeholder="Tell us if you have any allergies or questions..." class="w-full px-3.5 py-2.5 text-sm bg-white rounded-lg focus:outline-none focus:ring-2 focus:ring-champagne-gold border border-black/5"></textarea>
            </div>

            <button type="submit" class="w-full bg-champagne-gold hover:bg-obsidian-deep text-obsidian-deep hover:text-white py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md mt-2">
              Send via WhatsApp & Desk
            </button>
            <div id="booking-confirmation-msg" class="hidden p-3 bg-emerald-50 border border-emerald-200 text-emerald-800 rounded-lg text-xs text-center font-medium">
              Thank you! Your inquiry is being sent directly to WhatsApp desk.
            </div>
          </form>
        </div>

        <!-- Info Right -->
        <div class="lg:col-span-5 flex flex-col gap-6">
          <div class="bg-obsidian-deep text-alabaster-cream p-8 rounded-3xl shadow-xl">
            <span class="text-xs font-bold uppercase tracking-widest text-champagne-gold block mb-2">Salon & Make-Up Studio</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-white mb-4">LivArt Kakkanad Studio</h3>
            <div class="space-y-4 text-xs text-gray-300">
              <p><strong class="text-white">Address:</strong><br />{ADDRESS}</p>
              <p><strong class="text-white">Salon Direct Phone:</strong><br /><a href="tel:{PHONE_TEL}" class="text-champagne-gold text-sm font-bold">{PHONE}</a></p>
              <p><strong class="text-white">Email:</strong><br /><a href="mailto:{EMAIL}" class="hover:underline">{EMAIL}</a></p>
              <p><strong class="text-white">Opening Hours:</strong><br />{HOURS}</p>
            </div>

            <div class="mt-6 pt-6 border-t border-white/10 flex gap-3">
              <a href="https://wa.me/917012059591" target="_blank" rel="noopener noreferrer" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[16px]">chat</span> WhatsApp Salon
              </a>
              <a href="tel:{PHONE_TEL}" class="flex-1 bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[16px]">call</span> Call Salon
              </a>
            </div>
          </div>

          <!-- Dedicated LivArt Beauty Academy Admissions -->
          <div class="bg-obsidian-surface border border-champagne-gold/30 text-alabaster-cream p-6 rounded-3xl shadow-xl">
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold bg-champagne-gold/15 px-2.5 py-1 rounded-full">Govt. Affiliated Academy</span>
              <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="text-xs text-champagne-gold hover:underline flex items-center gap-1">livart.co.in ↗</a>
            </div>
            <h4 class="font-serif-luxury text-xl font-bold text-white mb-2">LivArt Beauty Academy</h4>
            <p class="text-xs text-gray-300 mb-4 leading-relaxed">
              Course admissions, syllabus queries, and B&WSSC government certification inquiries:
            </p>
            <div class="space-y-2 text-xs text-gray-300 mb-4 bg-obsidian-deep/60 p-3 rounded-xl border border-white/5">
              <p><strong class="text-white">Direct Admissions Desk:</strong><br /><a href="tel:{ACADEMY_PHONE_TEL}" class="text-champagne-gold text-sm font-bold">{ACADEMY_PHONE}</a></p>
              <p><strong class="text-white">Academy Portal:</strong> <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="text-champagne-gold hover:underline">livart.co.in</a></p>
            </div>
            <div class="flex gap-3">
              <a href="https://wa.me/919633211151?text=Hello%20LivArt%20Beauty%20Academy,%20I%20would%20like%20to%20inquire%20about%20courses" target="_blank" rel="noopener noreferrer" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white py-2 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[15px]">chat</span> WhatsApp ({ACADEMY_PHONE})
              </a>
              <a href="tel:{ACADEMY_PHONE_TEL}" class="flex-1 border border-champagne-gold/40 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold py-2 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[15px]">call</span> Call Desk
              </a>
            </div>
          </div>

          <div class="h-64 rounded-3xl overflow-hidden shadow-lg border border-black/5 bg-surface-container">
            <iframe 
              src="https://maps.google.com/maps?q=Livart%20Salon%20-%20Best%20Beauty%20Parlour%20in%20Kakkanad&t=m&z=14&output=embed&iwloc=near" 
              width="100%" 
              height="100%" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              title="LivArt Salon Kakkanad Google Maps Location">
            </iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "contact-us", "index.html"), "w") as f:
        f.write(html)
    print("✓ contact-us/index.html built")

# -------------------------------------------------------------
# 9. LIVART BEAUTY ACADEMY PAGE (/academy/)
# -------------------------------------------------------------
def build_academy_page():
    ensure_dir(os.path.join(BASE_DIR, "academy"))

    extra_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "EducationalOrganization",
                "@id": f"{ACADEMY_URL}/#academy",
                "name": "LivArt Beauty Academy",
                "url": ACADEMY_URL,
                "logo": LOGO_URL,
                "description": "Government-approved beauty and cosmetology academy affiliated with B&WSSC (Beauty & Wellness Sector Skill Council of India), offering professional diplomas in cosmetology, bridal makeup, hair styling, and clinical skincare aesthetics.",
                "telephone": ACADEMY_PHONE,
                "email": EMAIL,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "2nd Floor, Anchorage Business Center, Seaport - Airport Road, NGO Quarters – Mavelipuram Rd",
                    "addressLocality": "Kakkanad, Kochi",
                    "addressRegion": "Kerala",
                    "postalCode": "682030",
                    "addressCountry": "IN"
                },
                "founder": {
                    "@type": "Person",
                    "name": "Stephy Sebastian",
                    "jobTitle": ["Founder & Creative Director", "Celebrity Hair & Makeup Artist", "Master Cosmetology Educator"],
                    "url": ACADEMY_FOUNDER_URL,
                    "sameAs": [
                        ACADEMY_FOUNDER_URL,
                        PRESS_FEATURE_URL,
                        INSTAGRAM_URL,
                        FACEBOOK_URL
                    ]
                },
                "sameAs": [
                    ACADEMY_URL,
                    PRESS_FEATURE_URL
                ]
            },
            {
                "@type": "Course",
                "name": "Diploma in Cosmetology (Comprehensive Hair, Skin & Makeup)",
                "description": "Comprehensive 6-month government-accredited beautician diploma covering hair designing, clinical aesthetics, HD bridal makeup, and salon management with live salon floor practice.",
                "provider": {
                    "@type": "EducationalOrganization",
                    "name": "LivArt Beauty Academy",
                    "sameAs": ACADEMY_URL
                },
                "url": f"{ACADEMY_URL}/certification-course-in-cosmetology/"
            },
            {
                "@type": "Course",
                "name": "Professional Bridal Makeup Course",
                "description": "Intensive 2-month bridal makeup certification covering 4K HD foundation, airbrush artistry, traditional and contemporary South Indian bridal looks, and couture saree draping.",
                "provider": {
                    "@type": "EducationalOrganization",
                    "name": "LivArt Beauty Academy",
                    "sameAs": ACADEMY_URL
                },
                "url": f"{ACADEMY_URL}/bridal-makeup-course/"
            },
            {
                "@type": "Course",
                "name": "Professional Hair Styling & Haircuts Course",
                "description": "Advanced 4-month hair styling and cutting program teaching geometric precision cuts, balayage coloring, keratin, hair botox, and nanoplastia.",
                "provider": {
                    "@type": "EducationalOrganization",
                    "name": "LivArt Beauty Academy",
                    "sameAs": ACADEMY_URL
                },
                "url": f"{ACADEMY_URL}/hair-styling-course/"
            },
            {
                "@type": "Course",
                "name": "Skin Care & Advanced Aesthetics Course",
                "description": "4-month clinical dermal aesthetics course training students in Hydra facials, chemical peels, ultrasonic skin treatments, and acne solutions.",
                "provider": {
                    "@type": "EducationalOrganization",
                    "name": "LivArt Beauty Academy",
                    "sameAs": ACADEMY_URL
                },
                "url": f"{ACADEMY_URL}/skin-care-course/"
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"},
                    {"@type": "ListItem", "position": 2, "name": "LivArt Beauty Academy", "item": BASE_URL + "/academy/"}
                ]
            }
        ]
    }

    html = render_head(
        title="Best Beautician Course & Makeup Academy in Kakkanad, Kochi | LivArt Academy",
        description="Join LivArt Beauty Academy in Kakkanad, Kochi. Govt B&WSSC accredited diploma courses in cosmetology, bridal makeup artistry, hair styling, and skincare aesthetics.",
        canonical_path="/academy/",
        extra_schema=extra_schema,
        root_prefix="../"
    )
    html += render_header(active_slug="academy", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <!-- Breadcrumb Navigation -->
  <div class="bg-surface-container py-3 border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-xs text-muted-slate flex items-center gap-2">
      <a href="../index.html" class="hover:text-obsidian-deep transition-colors">Home</a>
      <span>/</span>
      <span class="text-obsidian-deep font-semibold">LivArt Beauty Academy (Govt. Affiliated)</span>
    </div>
  </div>

  <!-- Hero Sanctuary -->
  <section class="relative w-full bg-obsidian-deep text-alabaster-cream pt-16 pb-20 overflow-hidden">
    <div class="absolute -top-32 -left-32 w-96 h-96 rounded-full bg-champagne-gold/10 blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 -right-48 w-[500px] h-[500px] rounded-full bg-warm-bronze/10 blur-3xl pointer-events-none"></div>

    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Badge Row -->
      <div class="flex flex-wrap items-center gap-2 mb-6">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-champagne-gold text-obsidian-deep rounded-full text-[11px] font-bold tracking-widest uppercase">
          <span class="material-symbols-outlined text-[14px]">verified</span>
          Affiliated with B&WSSC • Skill India
        </span>
        <span class="hidden sm:inline text-muted-slate">•</span>
        <span class="text-metallic-gold-light text-xs tracking-wider">Govt. Recognized Beautician & Cosmetology Diplomas in Kakkanad, Kochi</span>
      </div>

      <!-- Hero Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 flex flex-col items-start">
          <p class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase mb-2 font-semibold">
            Official Academy Portal: <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="underline hover:text-white">livart.co.in ↗</a>
          </p>
          <h1 class="font-serif-luxury text-4xl sm:text-5xl lg:text-6xl text-alabaster-cream leading-[1.15] mb-6 font-normal">
            LivArt Beauty Academy <br />
            <span class="italic text-gold-gradient">Where Passion Becomes Mastery.</span>
          </h1>
          <p class="text-base sm:text-lg text-gray-300 max-w-xl mb-6 leading-relaxed">
            Train under Master Stylist & Celebrity Artist <strong>Stephy Sebastian</strong> (former National Educator for L'Oréal Professionnel & Wella). Experience 100% live salon floor apprenticeship, master international chemical formulations, and earn Government-approved certifications valid across India and the Gulf.
          </p>

          <div class="bg-obsidian-surface/90 border-l-2 border-champagne-gold p-4 sm:p-5 rounded-r-xl mb-8 max-w-xl shadow-lg">
            <p class="font-serif-luxury text-base sm:text-lg text-alabaster-cream italic">
              “If your mind can think it, you can achieve it. If I can, you can too.”
            </p>
            <span class="block mt-2 font-label-caps text-[11px] text-champagne-gold tracking-widest uppercase">
              — Stephy Sebastian, Founder & Creative Director
            </span>
          </div>

          <div class="flex flex-wrap items-center gap-4 w-full sm:w-auto">
            <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-6 py-3.5 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase shadow-xl transition-all">
              <span>Visit livart.co.in</span>
              <span class="material-symbols-outlined text-[16px]">open_in_new</span>
            </a>
            <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20would%20like%20to%20inquire%20about%20your%20beautician%20courses" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-3.5 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase transition-all shadow-lg">
              <span class="material-symbols-outlined text-[16px]">chat</span>
              <span>WhatsApp Admissions</span>
            </a>
            <a href="tel:{ACADEMY_PHONE_TEL}" class="inline-flex items-center justify-center gap-2 border border-champagne-gold/40 hover:bg-champagne-gold hover:text-obsidian-deep text-champagne-gold px-6 py-3.5 rounded-lg font-label-caps text-xs font-bold tracking-widest uppercase transition-all shadow-lg">
              <span class="material-symbols-outlined text-[16px]">call</span>
              <span>Call 096332 11151</span>
            </a>
          </div>

          <!-- Trust Badges -->
          <div class="grid grid-cols-3 gap-6 pt-10 mt-6 border-t border-white/10 w-full max-w-xl">
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">100%</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Live Model Practical</span>
            </div>
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">B&WSSC</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Govt. Affiliation</span>
            </div>
            <div>
              <span class="font-serif-luxury text-2xl sm:text-3xl font-bold text-champagne-gold block">Gulf & UK</span>
              <span class="text-xs text-muted-slate uppercase tracking-wider">Valid Certification</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5 relative">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-white/10 bg-obsidian-surface">
            <img src="../assets/images/brand/stephy-sebastian.webp" alt="Stephy Sebastian - Founder of LivArt Salon and LivArt Beauty Academy Kakkanad" class="w-full h-full object-cover" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep via-transparent to-transparent"></div>
            <div class="absolute bottom-6 left-6 right-6">
              <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block mb-1">Master Cosmetology Educator</span>
              <h3 class="font-serif-luxury text-2xl font-bold text-white mb-2">Stephy Sebastian</h3>
              <p class="text-xs text-gray-300 leading-relaxed mb-3">
                Former National Trainer for L'Oréal Professionnel & Wella. 5 years of healthcare nursing background shaping clinical hygiene excellence.
              </p>
              <div class="flex items-center gap-3">
                <a href="{ACADEMY_FOUNDER_URL}" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-champagne-gold hover:underline flex items-center gap-1">
                  <span>Read Full Bio on livart.co.in</span>
                  <span class="material-symbols-outlined text-[13px]">open_in_new</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- B&WSSC Government Credential Section -->
  <section class="py-16 bg-surface-bright border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-4 bg-obsidian-deep text-alabaster-cream p-8 rounded-3xl shadow-xl border border-champagne-gold/20">
          <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block mb-2">National Skill Qualification</span>
          <h3 class="font-serif-luxury text-2xl font-bold text-white mb-4">Why B&WSSC Affiliation Matters</h3>
          <p class="text-xs text-gray-300 leading-relaxed mb-4">
            LivArt Beauty Academy is proud to offer government-approved beautician and cosmetology courses affiliated with the <strong>Beauty and Wellness Sector Skill Council (B&WSSC)</strong> under the Ministry of Skill Development and Entrepreneurship (MSDE), Government of India.
          </p>
          <div class="space-y-2 text-xs text-metallic-gold-light border-t border-white/10 pt-4">
            <p class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span> Legally licensed salon entrepreneurship in India</p>
            <p class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span> Recognized for Gulf employment visas (UAE, Qatar, Saudi)</p>
            <p class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-champagne-gold">check_circle</span> Credit transfer eligibility for UK, Canada & Europe</p>
          </div>
        </div>

        <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-warm-bronze flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-[24px]">school</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Govt. Recognized Certification</h4>
              <p class="text-xs text-gray-600 leading-relaxed">
                Diplomas and certificates issued carry Government of India seals, giving your resume instant credibility across domestic and global recruiters.
              </p>
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-warm-bronze pt-4 block">• Certified Credibility</span>
          </div>

          <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-warm-bronze flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-[24px]">flight_takeoff</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Gulf & Global Placement</h4>
              <p class="text-xs text-gray-600 leading-relaxed">
                High demand in top salons across Dubai, Abu Dhabi, Doha, and Muscat. We assist in preparing portfolio decks and international interview prep.
              </p>
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-warm-bronze pt-4 block">• Global Mobility</span>
          </div>

          <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-champagne-gold/15 text-warm-bronze flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-[24px]">storefront</span>
              </div>
              <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Salon Entrepreneurship</h4>
              <p class="text-xs text-gray-600 leading-relaxed">
                Learn how to launch your own beauty salon, navigate business registration, vendor sourcing, staff management, and client retention strategies.
              </p>
            </div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-warm-bronze pt-4 block">• Business Mastery</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Comprehensive Courses Catalog -->
  <section class="py-20 bg-ivory-surface" id="courses">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-bold block mb-2">
          Professional Course Catalog
        </span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl lg:text-5xl text-obsidian-deep font-bold mb-4">
          Government Affiliated Diplomas & Masterclasses
        </h2>
        <p class="text-sm sm:text-base text-gray-600 leading-relaxed">
          From full 6-month Cosmetology Diplomas to specialized Bridal Makeup and Hair Texturing certifications. Full curriculum details available at <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="text-warm-bronze font-bold hover:underline">livart.co.in</a>.
        </p>
      </div>

      <!-- Course Cards -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Course 1: Cosmetology -->
        <div class="bg-surface-bright rounded-3xl p-8 border border-black/5 shadow-md flex flex-col justify-between hover:shadow-xl transition-all">
          <div>
            <div class="flex items-center justify-between mb-4 pb-4 border-b border-black/5">
              <span class="text-[11px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-3 py-1 rounded-full">Flagship Program</span>
              <span class="text-xs font-mono text-gray-500 font-semibold">6 Months • Full Diploma</span>
            </div>
            <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-obsidian-deep mb-3">
              Diploma in Cosmetology
            </h3>
            <p class="text-sm text-gray-600 leading-relaxed mb-6">
              Our all-inclusive master diploma designed for candidates who aspire to become complete salon professionals or salon owners. Covers the entire spectrum of hair cutting, hair coloring, clinical skin aesthetics, HD bridal makeup, and business administration.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-gray-700 mb-6 bg-surface-container-low p-4 rounded-xl">
              <div>
                <strong class="text-obsidian-deep block mb-1">Hair Modules:</strong>
                <p>Precision Haircuts, Balayage, Keratin, Hair Botox, Scalp SPA</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-1">Skin & Makeup:</strong>
                <p>Hydra Facial, Chemical Peels, Bridal HD Makeup, Saree Draping</p>
              </div>
            </div>

            <ul class="text-xs text-gray-600 space-y-2 mb-6">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Govt. B&WSSC Affiliated Certification</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> 100% Practical Training on LivArt Salon Floor</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Complete Professional Tool Kit & Product Kit Included</li>
            </ul>
          </div>

          <div class="flex flex-wrap items-center gap-3 pt-4 border-t border-black/5">
            <a href="{ACADEMY_URL}/certification-course-in-cosmetology/" target="_blank" rel="noopener noreferrer" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
              <span>View Full Syllabus on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
            <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20am%20interested%20in%20the%20Diploma%20in%20Cosmetology" target="_blank" rel="noopener noreferrer" class="text-emerald-700 bg-emerald-50 hover:bg-emerald-100 px-4 py-2.5 rounded-lg text-xs font-semibold transition-colors flex items-center gap-1">
              <span class="material-symbols-outlined text-[15px]">chat</span> WhatsApp Inquiries
            </a>
          </div>
        </div>

        <!-- Course 2: Bridal Makeup -->
        <div class="bg-surface-bright rounded-3xl p-8 border border-black/5 shadow-md flex flex-col justify-between hover:shadow-xl transition-all">
          <div>
            <div class="flex items-center justify-between mb-4 pb-4 border-b border-black/5">
              <span class="text-[11px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-3 py-1 rounded-full">Artistry Masterclass</span>
              <span class="text-xs font-mono text-gray-500 font-semibold">2 Months • Intensive</span>
            </div>
            <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-obsidian-deep mb-3">
              Professional Bridal Makeup Course
            </h3>
            <p class="text-sm text-gray-600 leading-relaxed mb-6">
              Mentored directly by Stephy Sebastian. Master 4K Ultra HD cameras and lighting aesthetics, high-definition airbrush foundation application, traditional Kerala Nair, Syrian Christian, and Muslim bridal looks, and modern couture fusion styling.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-gray-700 mb-6 bg-surface-container-low p-4 rounded-xl">
              <div>
                <strong class="text-obsidian-deep block mb-1">Techniques:</strong>
                <p>Airbrush, Cut-Crease Eye Art, Contour & Strobing, Lash Applications</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-1">Bridal Protocols:</strong>
                <p>Traditional & Modern Saree Draping, Veil Fixing, Big-Day Vanity</p>
              </div>
            </div>

            <ul class="text-xs text-gray-600 space-y-2 mb-6">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Stephy Sebastian Personal Feedback & Mentorship</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Professional Model Photoshoot for Your Social Portfolio</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Bridal Client Communication & Pricing Strategy</li>
            </ul>
          </div>

          <div class="flex flex-wrap items-center gap-3 pt-4 border-t border-black/5">
            <a href="{ACADEMY_URL}/bridal-makeup-course/" target="_blank" rel="noopener noreferrer" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
              <span>View Full Syllabus on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
            <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20am%20interested%20in%20the%20Bridal%20Makeup%20Course" target="_blank" rel="noopener noreferrer" class="text-emerald-700 bg-emerald-50 hover:bg-emerald-100 px-4 py-2.5 rounded-lg text-xs font-semibold transition-colors flex items-center gap-1">
              <span class="material-symbols-outlined text-[15px]">chat</span> WhatsApp Inquiries
            </a>
          </div>
        </div>

        <!-- Course 3: Hair Styling & Cuts -->
        <div class="bg-surface-bright rounded-3xl p-8 border border-black/5 shadow-md flex flex-col justify-between hover:shadow-xl transition-all">
          <div>
            <div class="flex items-center justify-between mb-4 pb-4 border-b border-black/5">
              <span class="text-[11px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-3 py-1 rounded-full">Hair Science</span>
              <span class="text-xs font-mono text-gray-500 font-semibold">4 Months • Certified</span>
            </div>
            <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-obsidian-deep mb-3">
              Professional Hair Styling & Haircuts
            </h3>
            <p class="text-sm text-gray-600 leading-relaxed mb-6">
              Learn advanced hair cutting techniques and color formulations benchmarked to international L'Oréal Professionnel and Wella protocols. Covers precision shears handling, sectioning geometry, creative balayage, hair botox, and straightening treatments.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-gray-700 mb-6 bg-surface-container-low p-4 rounded-xl">
              <div>
                <strong class="text-obsidian-deep block mb-1">Haircuts & Texturing:</strong>
                <p>Bobs, Pixie, Graduated Layers, Texturizing Shears, Fade Art</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-1">Color & Chemistry:</strong>
                <p>Global Colour, Foilyage, Root Smudge, Neutralizing Undertones</p>
              </div>
            </div>

            <ul class="text-xs text-gray-600 space-y-2 mb-6">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> International Brand Standard Protocols (L'Oréal & Wella)</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Hands-on Chemical Texturing (Keratin, Botox, Straightening)</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> High-Demand Skill for Salons across India & Gulf</li>
            </ul>
          </div>

          <div class="flex flex-wrap items-center gap-3 pt-4 border-t border-black/5">
            <a href="{ACADEMY_URL}/hair-styling-course/" target="_blank" rel="noopener noreferrer" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
              <span>View Full Syllabus on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
            <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20am%20interested%20in%20the%20Hair%20Styling%20Course" target="_blank" rel="noopener noreferrer" class="text-emerald-700 bg-emerald-50 hover:bg-emerald-100 px-4 py-2.5 rounded-lg text-xs font-semibold transition-colors flex items-center gap-1">
              <span class="material-symbols-outlined text-[15px]">chat</span> WhatsApp Inquiries
            </a>
          </div>
        </div>

        <!-- Course 4: Skin Care & Aesthetics -->
        <div class="bg-surface-bright rounded-3xl p-8 border border-black/5 shadow-md flex flex-col justify-between hover:shadow-xl transition-all">
          <div>
            <div class="flex items-center justify-between mb-4 pb-4 border-b border-black/5">
              <span class="text-[11px] font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-3 py-1 rounded-full">Dermal Aesthetics</span>
              <span class="text-xs font-mono text-gray-500 font-semibold">4 Months • Certified</span>
            </div>
            <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-obsidian-deep mb-3">
              Skin Care & Advanced Aesthetics
            </h3>
            <p class="text-sm text-gray-600 leading-relaxed mb-6">
              A comprehensive clinical aesthetic curriculum rooted in Stephy Sebastian's medical nursing principles. Train on advanced aesthetic machines, Hydra facials, ultrasonic extractions, enzyme peeling, and derma care for hyperpigmentation and acne.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-gray-700 mb-6 bg-surface-container-low p-4 rounded-xl">
              <div>
                <strong class="text-obsidian-deep block mb-1">Clinical Skin Science:</strong>
                <p>Fitzpatrick Skin Types, Dermal Layers, Acne Pathologies, De-Tan</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-1">Machine Handling:</strong>
                <p>Hydra Vacuum Systems, High Frequency, Galvanic, Ultrasonic Scrubber</p>
              </div>
            </div>

            <ul class="text-xs text-gray-600 space-y-2 mb-6">
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Hospital-Grade Clinical Sanitization & Safety Ethics</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Training with Cheryl's Cosmeceuticals & Dermalogica</li>
              <li class="flex items-center gap-2"><span class="material-symbols-outlined text-[15px] text-emerald-600">verified</span> Practical Diagnosis on Live Clients at Kakkanad</li>
            </ul>
          </div>

          <div class="flex flex-wrap items-center gap-3 pt-4 border-t border-black/5">
            <a href="{ACADEMY_URL}/skin-care-course/" target="_blank" rel="noopener noreferrer" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5">
              <span>View Full Syllabus on livart.co.in</span>
              <span class="material-symbols-outlined text-[14px]">open_in_new</span>
            </a>
            <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20am%20interested%20in%20the%20Skin%20Care%20Course" target="_blank" rel="noopener noreferrer" class="text-emerald-700 bg-emerald-50 hover:bg-emerald-100 px-4 py-2.5 rounded-lg text-xs font-semibold transition-colors flex items-center gap-1">
              <span class="material-symbols-outlined text-[15px]">chat</span> WhatsApp Inquiries
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- The LivArt Advantage -->
  <section class="py-20 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-16">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.25em] uppercase font-bold block mb-2">The Finishing Edge</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl font-bold text-obsidian-deep">Why Study at LivArt Beauty Academy?</h2>
        <p class="text-xs text-muted-slate mt-2">Discover how our active salon floor pedagogy accelerates your career beyond theory.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5">
          <div class="w-12 h-12 rounded-xl bg-champagne-gold/20 text-warm-bronze flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[24px]">group_work</span>
          </div>
          <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Active Salon Floor</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Students do not just practice on dummy heads. You assist senior stylists on genuine salon clients inside LivArt Kakkanad, learning real client pressure, handling, and bedside manner.
          </p>
        </div>

        <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5">
          <div class="w-12 h-12 rounded-xl bg-champagne-gold/20 text-warm-bronze flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[24px]">verified_user</span>
          </div>
          <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Clinical Discipline</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Founded by a former healthcare nurse, LivArt trains you in clinical-grade disinfection, scalp pathology identification, and safe chemical texturing practices.
          </p>
        </div>

        <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5">
          <div class="w-12 h-12 rounded-xl bg-champagne-gold/20 text-warm-bronze flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[24px]">photo_camera</span>
          </div>
          <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">Portfolio Building</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Graduates leave with an enviable Instagram-ready digital portfolio of professional photoshoots showcasing their hair transformations and bridal looks.
          </p>
        </div>

        <div class="bg-surface-container-low p-6 rounded-2xl border border-black/5">
          <div class="w-12 h-12 rounded-xl bg-champagne-gold/20 text-warm-bronze flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[24px]">work</span>
          </div>
          <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-2">100% Placement Support</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Strong alumni network across premium salons in Kochi, Bangalore, Chennai, and Gulf countries. Many graduates also open thriving boutique salons.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Admission & Contact CTA -->
  <section class="py-20 bg-obsidian-deep text-alabaster-cream relative overflow-hidden">
    <div class="max-w-[1100px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="bg-obsidian-surface border border-champagne-gold/30 rounded-3xl p-8 sm:p-12 text-center">
        <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
          New Batch Admissions Open
        </span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl font-bold text-white mb-4">
          Begin Your Cosmetology Career Today
        </h2>
        <p class="text-sm text-gray-300 max-w-2xl mx-auto leading-relaxed mb-8">
          Limited seats per batch to guarantee personal mentorship by Stephy Sebastian and senior educators. Visit our campus at Anchorage Business Center, Kakkanad or reach out directly.
        </p>

        <div class="flex flex-wrap items-center justify-center gap-4">
          <a href="{ACADEMY_URL}" target="_blank" rel="noopener noreferrer" class="bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep px-8 py-3.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-xl flex items-center gap-2">
            <span>Visit Academy Portal (livart.co.in)</span>
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
          </a>
          <a href="https://wa.me/919633211151?text=Hi%20LivArt%20Academy,%20I%20would%20like%20to%20apply%20for%20the%20upcoming%20batch" target="_blank" rel="noopener noreferrer" class="bg-emerald-600 hover:bg-emerald-500 text-white px-7 py-3.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-xl flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px]">chat</span>
            <span>WhatsApp Admissions ({ACADEMY_PHONE})</span>
          </a>
          <a href="tel:{ACADEMY_PHONE_TEL}" class="border border-white/20 hover:border-champagne-gold text-white hover:text-champagne-gold px-6 py-3.5 rounded-lg text-xs font-bold tracking-widest uppercase transition-all flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px] text-champagne-gold">call</span>
            <span>Call 096332 11151</span>
          </a>
        </div>

        <div class="mt-8 pt-8 border-t border-white/10 text-xs text-gray-400">
          <p><strong>Campus Address:</strong> 2nd Floor, Anchorage Business Center, Seaport-Airport Road, Kakkanad, Kochi, Kerala 682030</p>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "academy", "index.html"), "w") as f:
        f.write(html)
    print("✓ academy/index.html built")

if __name__ == "__main__":
    build_about_page()
    build_teams_page()
    build_hair_page()
    build_makeup_page()
    build_skincare_page()
    build_packages_page()
    build_gallery_page()
    build_contact_page()
    build_academy_page()

