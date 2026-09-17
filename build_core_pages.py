import os
import json
from generator import (
    BASE_DIR, SITE_NAME, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    INSTAGRAM_HANDLE, INSTAGRAM_URL, FACEBOOK_URL, LOGO_URL,
    render_head, render_header, render_footer
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# -------------------------------------------------------------
# 1. ABOUT US PAGE (/about-us/)
# -------------------------------------------------------------
def build_about_page():
    ensure_dir(os.path.join(BASE_DIR, "about-us"))
    
    html = render_head(
        title="About Us | LivArt Salon & Make-Up Studio Kakkanad Kochi",
        description="Learn about LivArt Salon founded by Stephy Sebastian and Nipun Conso. World-class hair stylists, bridal makeup artists, and clinical skincare in Kakkanad, Kochi.",
        canonical_path="/about-us/",
        root_prefix="../"
    )
    html += render_header(active_slug="about-us", root_prefix="../")
    
    stylists = [
        {"name": "Stephy Sebastian", "role": "Founder & Creative Director", "exp": "10+ Years", "spec": "Bridal Artistry & Hair Transformations", "img": "https://livartsalon.com/wp-content/uploads/2024/02/Stephy-Sebastian.webp"},
        {"name": "Arul Britto", "role": "Senior Hair Stylist & Educator", "exp": "8+ Years", "spec": "Precision Haircuts & Balayage", "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner14.jpg"},
        {"name": "Roopa", "role": "Master Makeup Artist", "exp": "7+ Years", "spec": "HD Bridal Makeup & Saree Draping", "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner24.jpg"},
        {"name": "Vipitha", "role": "Senior Skincare Aesthetician", "exp": "6+ Years", "spec": "Hydra Facials & Derma Therapies", "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner21.jpg"},
        {"name": "Abhishek", "role": "Creative Color Specialist", "exp": "5+ Years", "spec": "Ombre, Highlights & Keratin", "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner19.jpg"},
        {"name": "Om Prakash", "role": "Senior Stylist & Grooming Expert", "exp": "6+ Years", "spec": "Groom Styling & Hair Texture", "img": "https://livartsalon.com/wp-content/uploads/2023/05/poster1.jpg"},
        {"name": "Abhin", "role": "Hair Spa & Scalp Therapist", "exp": "5+ Years", "spec": "Deep Conditioning & Head Massages", "img": "https://livartsalon.com/wp-content/uploads/2023/05/livee11.jpg"}
    ]

    team_html = ""
    for s in stylists:
        team_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-lg transition-all flex flex-col justify-between">
          <div class="h-64 overflow-hidden bg-obsidian-deep">
            <img src="{s['img']}" alt="{s['name']} - {s['role']} at LivArt Salon Kakkanad" class="w-full h-full object-cover object-top hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-6 flex flex-col justify-between flex-grow">
            <div>
              <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">{s['exp']} Mastery</span>
              <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-1">{s['name']}</h3>
              <p class="text-xs text-gray-500 font-medium mb-3">{s['role']}</p>
              <p class="text-xs text-gray-700 leading-relaxed"><strong class="text-obsidian-deep">Specialty:</strong> {s['spec']}</p>
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
        Where passion meets mastery. Founded by Stephy Sebastian and Nipun Conso to establish Cochin's premier haute couture beauty studio.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-20">
        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden shadow-2xl bg-obsidian-deep border border-black/10">
            <img src="https://livartsalon.com/wp-content/uploads/2024/02/Stephy-Sebastian.webp" alt="Stephy Sebastian LivArt Founder" class="w-full h-full object-cover" />
          </div>
        </div>
        <div class="lg:col-span-6">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-2">Our Genesis</span>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl font-bold text-obsidian-deep mb-6">Built on Artistry, Humanity & World-Class Standards</h2>
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            LivArt Hair and Makeup Studio was established by <strong>Stephy Sebastian</strong> and <strong>Nipun Conso</strong> as a destination salon in Kakkanad that offers top-of-the-line hair, makeup & skin services, with a resolute focus on cutting-edge international techniques and unmatched customer hospitality.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Having gained invaluable experience working with industry leaders for over a decade, our founder Stephy Sebastian specializes in looks that make you feel truly on top of the world. In 2021, she expanded her vision by launching the <strong>LivArt Academy</strong>, mentoring the next generation of hair and makeup professionals.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-6">
            We provide customized beauty services tailored to all skin tones and hair textures, ensuring that every transformation is authentic to your personal essence.
          </p>
          <button data-open-booking class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold tracking-widest uppercase transition-all shadow-md">
            Consult Our Team
          </button>
        </div>
      </div>

      <!-- Team Grid -->
      <div class="border-t border-black/5 pt-16">
        <div class="text-center max-w-xl mx-auto mb-12">
          <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">Passionate Professionals</span>
          <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">Meet Our Master Stylists & Artists</h2>
          <p class="text-xs text-muted-slate mt-2">Certified experts dedicated to perfecting your hair, skin, and bridal aesthetics.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {team_html}
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
    html = render_head(
        title="Meet Our Founder & Stylists | LivArt Salon Kakkanad",
        description="Get to know Stephy Sebastian, founder of LivArt Hair & Makeup Studio and LivArt Academy. Former nurse turned master stylist curating luxury beauty in Kochi.",
        canonical_path="/teams/",
        root_prefix="../"
    )
    html += render_header(active_slug="about-us", root_prefix="../")

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
    <div class="max-w-[1100px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-surface-container-low rounded-3xl p-8 sm:p-12 border border-black/5 shadow-md grid grid-cols-1 md:grid-cols-12 gap-10 items-center mb-16">
        <div class="md:col-span-5">
          <div class="rounded-2xl overflow-hidden shadow-xl bg-obsidian-deep">
            <img src="https://livartsalon.com/wp-content/uploads/2024/02/Stephy-Sebastian.webp" alt="Stephy Sebastian Livart Founder" class="w-full h-full object-cover" />
          </div>
        </div>
        <div class="md:col-span-7">
          <span class="text-xs font-bold uppercase tracking-widest text-warm-bronze block mb-1">Founder & Creative Director</span>
          <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-4">Stephy Sebastian</h2>
          <div class="prose text-sm text-gray-700 space-y-3 leading-relaxed">
            <p>
              Stephy serves as the visionary pillar of LivArt Hair and Makeup Studio, portraying the qualities of a true stylist curated from genuine passion and love for the artistry. As a former nurse, Stephy served in demanding medical conditions that forged her unmatched resilience and compassion—traits that make her an inspiration to all who meet her.
            </p>
            <p>
              Her transition from nursing to hair and makeup artistry was fueled by a lifelong commitment to pursuing what she loves most. Stephy completed her master education under the industry's finest mentors and has spent over a decade honing her craft.
            </p>
            <p>
              In 2021, she established the <strong>LivArt Academy</strong>, where she has successfully trained hundreds of emerging beauty professionals. Stephy's mother taught her to give back to the younger generation, and that spirit continues to guide LivArt's mentorship ethos today.
            </p>
            <p class="italic text-obsidian-deep font-serif-luxury text-base pt-2">
              “In other words, Stephy is a character who gets things done, fulfills her dreams, and LIVes the ART.”
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-black/5 flex gap-4">
            <button data-open-booking data-service="Personal Consultation with Founder Stephy Sebastian" class="bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
              Book with Stephy
            </button>
            <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" class="border border-black/10 hover:bg-black/5 px-5 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-obsidian-deep transition-all flex items-center gap-1.5">
              <span>View On Instagram</span>
              <span class="material-symbols-outlined text-[15px]">open_in_new</span>
            </a>
          </div>
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
        title="Hair Styling, Balayage, Cuts & Hair Spa | LivArt Salon Kakkanad",
        description="Expert haircuts, L'Oreal hair spa, creative balayage, hot oil massage, and keratin treatments at LivArt Salon Kakkanad. Handcrafted by master stylists in Kochi.",
        canonical_path="/hair-styling/",
        root_prefix="../"
    )
    html += render_header(active_slug="hair-styling", root_prefix="../")

    hair_services = [
        ("Relaxo Hot Oil Head Massage", "Let our expert staff soothe your senses with a hot oil head massage. Formulated to stimulate scalp micro-circulation, nourish deep hair follicles, and relieve cranial tension.", "From Rs. 850", "https://livartsalon.com/wp-content/uploads/2022/10/banner18.jpg"),
        ("L’Oreal Professional Hair Spa", "Deep steam infusion and therapeutic acupressure massage that repairs cuticle breakdown, cures dryness, and restores lustrous mirror-like gloss.", "Rs. 1,200 (Reg. 1800)", "https://livartsalon.com/wp-content/uploads/2023/05/livee11.jpg"),
        ("Balayage & Dimensional Colouring", "Hand-painted dimensional hues tailored to your undertone. Seamless transitions, soft root melting, and zero ammonia damage.", "From Rs. 5,999", "https://livartsalon.com/wp-content/uploads/2022/10/banner19.jpg"),
        ("Precision Haircuts & Blowouts", "Structural haircutting customized to your bone structure and hair density, finished with our iconic runway bouncy blowout.", "From Rs. 850", "https://livartsalon.com/wp-content/uploads/2022/10/banner14.jpg"),
        ("Hair Botox Anti-Aging Treatment", "Fills structural keratin gaps in hair strands, eliminates 95% of frizz, and revitalizes damaged ends without harsh chemicals.", "Rs. 5,999", "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_-offer-poster2_11-7-2023-1.jpg"),
        ("Permanent Hair Straightening", "Thermal rebonding and permanent straightening for mirror-like silky pin-straight hair that endures through any humidity.", "From Rs. 4,000", "https://livartsalon.com/wp-content/uploads/2023/05/poster1.jpg")
    ]

    services_html = ""
    for title, desc, price, img in hair_services:
        services_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div class="h-48 overflow-hidden bg-obsidian-deep">
            <img src="{img}" alt="{title} at LivArt Salon Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" />
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
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Hair Styling & Treatments in Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        LivArt Salon specializes in hair artistry and is committed to creating art with your hair. State-of-the-art facilities and world-class stylists tailored to your unique hair type.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {services_html}
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
        title="Bridal Makeup & Groom Packages in Kochi | LivArt Salon Kakkanad",
        description="Best bridal makeup in Kochi curated by Stephy Sebastian. Silver, Gold & Diamond Bridal Packages, and Groom Black Diamond packages at LivArt Salon Kakkanad.",
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
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Bridal & Groom Makeup Packages in Kochi</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Curated by Stephy Sebastian. Flawless HD and airbrush makeup designed to withstand long ceremonial hours and look breathtaking in high-resolution photography.
      </p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {pkgs_html}
      </div>

      <div class="mt-16 p-8 bg-ivory-surface rounded-3xl border border-black/5 text-center max-w-3xl mx-auto">
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-2">Planning a Destination Wedding in Kerala?</h3>
        <p class="text-xs text-gray-600 leading-relaxed mb-6">
          Stephy Sebastian and her senior bridal team travel for destination weddings across Kochi, Kumarakom, Munnar, and Kovalam. We customize group styling for bridesmaids and family members.
        </p>
        <button data-open-booking data-service="Destination Bridal Consultation" class="bg-champagne-gold text-obsidian-deep px-6 py-3 rounded-lg text-xs font-bold uppercase tracking-widest hover:bg-metallic-gold-light transition-all shadow-md">
          Request Destination Bridal Quote
        </button>
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
        title="Skincare, Facials, Cheryl's & Pedicure | LivArt Salon Kakkanad",
        description="Indulge in premium skincare at LivArt Salon Kakkanad. De-tan treatments, Hydra Facials, Cheryl's Pro Facials, deluxe pedicure/manicure, and our 1-Year 20% loyalty program.",
        canonical_path="/skin-care/",
        root_prefix="../"
    )
    html += render_header(active_slug="skin-care", root_prefix="../")

    skin_services = [
        ("Skin Miracle Hydra Facial", "Our advanced vortex extraction and hyaluronic infusion facial that clears congestion and restores dewy glass-skin luminosity.", "Rs. 4,000", "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_offer-poster1_11-7-2023-1.jpg"),
        ("De-Tan + Skin Miracle Combo", "Signature dual ritual that erases sun tanning, lightens pigment spots, and floods the dermis in brightening vitamins.", "From Rs. 2,499", "https://livartsalon.com/wp-content/uploads/2022/10/banner21.jpg"),
        ("Pro Facial by Cheryl’s Cosmeceuticals", "Clinically formulated protocols by Cheryl's designed specifically for Indian skin to treat active acne, uneven tone, and dullness.", "From Rs. 2,200", "https://livartsalon.com/wp-content/uploads/2022/10/banner22.jpg"),
        ("Deluxe Manicure & Pedicure Spa", "Deep dead-skin exfoliation, cuticle conditioning, relaxing foot reflexology massage, and precision nail shaping.", "From Rs. 1,400", "https://livartsalon.com/wp-content/uploads/2022/10/banner23.jpg"),
        ("Herbal Waxing & Threading", "Painless threading for brows and facial contours, alongside gentle honey and chocolate wax formulations that prevent irritation.", "From Rs. 100", "https://livartsalon.com/wp-content/uploads/2022/10/banner25.jpg"),
        ("Skin Bleaching & Derma Glow", "Safe, ammonia-free dermatological bleaching rituals that illuminate the complexion for festive and wedding readiness.", "From Rs. 1,200", "https://livartsalon.com/wp-content/uploads/2022/10/banner26.jpg")
    ]

    services_html = ""
    for title, desc, price, img in skin_services:
        services_html += f"""
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
          <div class="h-48 overflow-hidden bg-obsidian-deep">
            <img src="{img}" alt="{title} at LivArt Salon Kakkanad" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" />
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
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Skincare & Facial Therapies in Kakkanad</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Discover exceptional skincare services designed to enhance the cellular health and radiance of your complexion. Safe, clinically tested formulations tailored to Kerala's climate.
      </p>
    </div>
  </section>

  <!-- Loyalty Program Callout Banner (Clean & Genuine) -->
  <section class="w-full bg-gold-gradient py-6">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-obsidian-deep text-champagne-gold flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-[24px]">verified</span>
        </div>
        <div>
          <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep">LivArt Salon Loyalty Privilege Program</h3>
          <p class="text-xs text-black/80 font-medium">
            Spend <strong>Rs. 1,000</strong> on any skincare or salon service and receive an exclusive <strong>1-Year Privilege Membership Card</strong> offering <strong>20% discount</strong> on all future visits.
          </p>
        </div>
      </div>
      <button data-open-booking data-service="1-Year 20% Membership Offer" class="shrink-0 bg-obsidian-deep text-white hover:bg-obsidian-surface px-6 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
        Claim 20% Membership
      </button>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {services_html}
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
        title="Salon Packages & Pricing | LivArt Salon Kakkanad Kochi",
        description="Transparent pricing on Bridal, Groom, Hair Care, and Skincare combo packages at LivArt Salon Kakkanad. Luxury services starting from Rs. 2,499.",
        canonical_path="/packages/",
        root_prefix="../"
    )
    html += render_header(active_slug="packages", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Curated Value Rituals</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Exclusive LivArt Salon Packages</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Transparent, all-inclusive luxury salon packages combining our highest-rated hair therapies, bridal glamour, and restorative facials.
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

  <!-- Interactive Feed Section -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10 text-center">
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep mb-2">Featured Instagram Reels & Client Transformations</h2>
        <p class="text-xs text-muted-slate">Click any reel to watch, read styling details, and instantly book that exact look with our stylists.</p>
      </div>

      <div id="instagram-feed-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
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
        title="Contact Us & Book Appointment | LivArt Salon Kakkanad Kochi",
        description="Book your hair, makeup, or skincare appointment at LivArt Salon Kakkanad. Call +91 70120 59591 or visit Anchorage Business Center, Seaport-Airport Road.",
        canonical_path="/contact-us/",
        root_prefix="../"
    )
    html += render_header(active_slug="contact-us", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Concierge & Studio</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">Connect With LivArt Salon</h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Come to us & get sharp. We are located in the heart of Kakkanad on Seaport-Airport Road.
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
                <option value="De-Tan + Skin Miracle Whitening Combo (Rs. 2499)">De-Tan + Skin Miracle Whitening Combo (Rs. 2499)</option>
                <option value="Hair Colouring & Balayage">Hair Colouring & Balayage</option>
                <option value="Hair Botox Treatment">Hair Botox Treatment</option>
                <option value="Permanent Blow Dry">Permanent Blow Dry</option>
                <option value="L'Oreal Hair Spa">L'Oreal Hair Spa</option>
                <option value="Bridal Makeup Consultation">Bridal Makeup Consultation</option>
                <option value="Groom Package">Groom Package</option>
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
            <span class="text-xs font-bold uppercase tracking-widest text-champagne-gold block mb-2">Our Locations</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-white mb-4">LivArt Kakkanad Studio</h3>
            <div class="space-y-4 text-xs text-gray-300">
              <p><strong class="text-white">Address:</strong><br />{ADDRESS}</p>
              <p><strong class="text-white">Direct Phone:</strong><br /><a href="tel:{PHONE_TEL}" class="text-champagne-gold text-sm font-bold">{PHONE}</a></p>
              <p><strong class="text-white">Email:</strong><br /><a href="mailto:{EMAIL}" class="hover:underline">{EMAIL}</a></p>
              <p><strong class="text-white">Opening Hours:</strong><br />{HOURS}</p>
            </div>

            <div class="mt-6 pt-6 border-t border-white/10 flex gap-3">
              <a href="https://wa.me/917012059591" target="_blank" rel="noopener noreferrer" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[16px]">chat</span> WhatsApp
              </a>
              <a href="tel:{PHONE_TEL}" class="flex-1 bg-champagne-gold hover:bg-metallic-gold-light text-obsidian-deep py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5">
                <span class="material-symbols-outlined text-[16px]">call</span> Call Desk
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

if __name__ == "__main__":
    build_about_page()
    build_teams_page()
    build_hair_page()
    build_makeup_page()
    build_skincare_page()
    build_packages_page()
    build_gallery_page()
    build_contact_page()
