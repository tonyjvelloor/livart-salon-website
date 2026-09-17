/**
 * LivArt Salon & Make-Up Studio — Categorized Instagram Reels Database & Player
 * 48 Curated Reels: 21 Celebrity Visits + 27 Bridal Works
 * Direct links to https://www.instagram.com/livart_salon/
 */

const CELEBRITY_REELS = [
  {
    title: "Amala Shaji Blow Dry Transformation",
    handle: "@amalashaji",
    url: "https://www.instagram.com/livart_salon/reel/Db7rJBtuj4B/",
    code: "Db7rJBtuj4B",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "Influencer Spotlight",
    service: "Permanent Blow Dry & Styling",
    poster: "/assets/images/instagram/Db7rJBtuj4B.jpg"
  },
  {
    title: "Azmin Yasar Styled at Salon",
    handle: "@azmin_yasar",
    url: "https://www.instagram.com/livart_salon/reel/DbLJRauyFro/",
    code: "DbLJRauyFro",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "Hair Styling",
    service: "Hair Styling & Texture",
    poster: "/assets/images/instagram/DbLJRauyFro.jpg"
  },
  {
    title: "Rithu Manthra Styled at Salon",
    handle: "@rithumanthra_",
    url: "https://www.instagram.com/livart_salon/reel/DZkDGP8N7ei/",
    code: "DZkDGP8N7ei",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Model & Actress",
    service: "Haute Couture Hair & Makeup",
    poster: "/assets/images/instagram/DZkDGP8N7ei.jpg"
  },
  {
    title: "Madona Tixeira - IPL Anchor Hairstyle",
    handle: "@madonnatixy",
    url: "https://www.instagram.com/livart_salon/reel/DYv8wyxMjAl/",
    code: "DYv8wyxMjAl",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "IPL Anchor",
    service: "Runway Blow Dry & Styling",
    poster: "/assets/images/instagram/DYv8wyxMjAl.jpg"
  },
  {
    title: "Actress Amala Rose Kurian Review - Hair Botox",
    handle: "@amala_rose_kurian",
    url: "https://www.instagram.com/livart_salon/reel/DW1NAndDGuP/",
    code: "DW1NAndDGuP",
    category: "celebrity",
    tag: "Celebrity Review",
    badge: "Hair Botox",
    service: "Hair Botox Treatment (Rs. 5999)",
    poster: "/assets/images/instagram/DW1NAndDGuP.jpg"
  },
  {
    title: "Client Madona Tixeira Thank-You",
    handle: "@madonnatixy",
    url: "https://www.instagram.com/livart_salon/reel/DOajrjXkqH_/",
    code: "DOajrjXkqH_",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Client Love",
    service: "Salon Styling Experience",
    poster: "/assets/images/instagram/DOajrjXkqH_.jpg"
  },
  {
    title: "Poomaram Actress Sangeetha at Salon",
    handle: "Actress Sangeetha",
    url: "https://www.instagram.com/livart_salon/reel/DIYwMqNSFPo/",
    code: "DIYwMqNSFPo",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Film Star",
    service: "Personalized Beauty Ritual",
    poster: "/assets/images/instagram/DIYwMqNSFPo.jpg"
  },
  {
    title: "Actress Amala Rose Kurian Salon Session",
    handle: "@amala_rose_kurian",
    url: "https://www.instagram.com/livart_salon/reel/DEXOFvGTyDZ/",
    code: "DEXOFvGTyDZ",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Couture Styling",
    service: "Hair Styling & Hair Spa",
    poster: "/assets/images/instagram/DEXOFvGTyDZ.jpg"
  },
  {
    title: "Anchor Meenakshi Sudheer Makeover",
    handle: "Meenakshi Sudheer",
    url: "https://www.instagram.com/livart_salon/reel/DD09-1GTd2F/",
    code: "DD09-1GTd2F",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "TV Anchor",
    service: "Camera-Ready Glamour Makeover",
    poster: "/assets/images/instagram/DD09-1GTd2F.jpg"
  },
  {
    title: "Makeover for Madona Tixeira",
    handle: "@madonnatixy",
    url: "https://www.instagram.com/livart_salon/reel/DDYbKpnTbKk/",
    code: "DDYbKpnTbKk",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "Anchor Makeover",
    service: "Hair Styling & Makeup",
    poster: "/assets/images/instagram/DDYbKpnTbKk.jpg"
  },
  {
    title: "RJ Soorya Hair Colouring Artistry",
    handle: "RJ Soorya",
    url: "https://www.instagram.com/livart_salon/reel/DABMk4mtv8b/",
    code: "DABMk4mtv8b",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "RJ Glam",
    service: "L'Oreal Glossy Hair Colouring",
    poster: "/assets/images/instagram/DABMk4mtv8b.jpg"
  },
  {
    title: "RJ Surya Festive Onam Look",
    handle: "RJ Surya",
    url: "https://www.instagram.com/livart_salon/reel/C_hxrh3y5NY/",
    code: "C_hxrh3y5NY",
    category: "celebrity",
    tag: "Celebrity Festive",
    badge: "Onam Glam",
    service: "Festive Saree Draping & Makeup",
    poster: "/assets/images/instagram/C_hxrh3y5NY.jpg"
  },
  {
    title: "Anchor Meenakshi Sudheer Detox Pedicure",
    handle: "Meenakshi Sudheer",
    url: "https://www.instagram.com/livart_salon/reel/C88tG9iSEKp/",
    code: "C88tG9iSEKp",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Foot Spa",
    service: "Deluxe Pedicure Spa",
    poster: "/assets/images/instagram/C88tG9iSEKp.jpg"
  },
  {
    title: "News Anchor Shiju Abdul Rasheed Haircut",
    handle: "Shiju Abdul Rasheed",
    url: "https://www.instagram.com/livart_salon/reel/C7l9fP5P3u9/",
    code: "C7l9fP5P3u9",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "News Anchor",
    service: "Precision Haircut & Grooming",
    poster: "/assets/images/instagram/C7l9fP5P3u9.jpg"
  },
  {
    title: "Client RJ Bincy Compliment & Review",
    handle: "RJ Bincy",
    url: "https://www.instagram.com/livart_salon/reel/C6F_GKgtlHk/",
    code: "C6F_GKgtlHk",
    category: "celebrity",
    tag: "Celebrity Review",
    badge: "Verified Patrons",
    service: "Signature Salon Ritual",
    poster: "/assets/images/instagram/C6F_GKgtlHk.jpg"
  },
  {
    title: "RJ Bincy Hair Makeover",
    handle: "RJ Bincy",
    url: "https://www.instagram.com/livart_salon/reel/C5pwjmOidQU/",
    code: "C5pwjmOidQU",
    category: "celebrity",
    tag: "Celebrity Makeover",
    badge: "Hair Rebirth",
    service: "Hair Styling & Keratin Treatment",
    poster: "/assets/images/instagram/C5pwjmOidQU.jpg"
  },
  {
    title: "Ms. Ajmi - Icon of the Year Awardee",
    handle: "Ms. Ajmi",
    url: "https://www.instagram.com/livart_salon/reel/C4VCBeStpUM/",
    code: "C4VCBeStpUM",
    category: "celebrity",
    tag: "Celebrity Visit",
    badge: "Award Recipient",
    service: "Red Carpet Makeup & Styling",
    poster: "/assets/images/instagram/C4VCBeStpUM.jpg"
  },
  {
    title: "Actress Suvarna Menon Hair Botox Review",
    handle: "@iamsuvarnamenon",
    url: "https://www.instagram.com/livart_salon/reel/Cujo9fqpEsB/",
    code: "Cujo9fqpEsB",
    category: "celebrity",
    tag: "Celebrity Review",
    badge: "Actress Favorite",
    service: "Hair Botox Treatment (Rs. 5999)",
    poster: "/assets/images/instagram/Cujo9fqpEsB.jpg"
  },
  {
    title: "Actress Shivani Menon Viral New Look",
    handle: "Actress Shivani Menon",
    url: "https://www.instagram.com/livart_salon/reel/CsQ-ptyuuv-/",
    code: "CsQ-ptyuuv-",
    category: "celebrity",
    tag: "Viral Sensation",
    badge: "🔥 99K Likes Viral",
    service: "Signature Haircut & Balayage",
    poster: "/assets/images/instagram/CsQ-ptyuuv-.jpg"
  },
  {
    title: "RJ Soorya Festive Vishu Look",
    handle: "RJ Soorya",
    url: "https://www.instagram.com/livart_salon/reel/CrAzwEnJ8FV/",
    code: "CrAzwEnJ8FV",
    category: "celebrity",
    tag: "Celebrity Festive",
    badge: "Vishu Radiance",
    service: "Traditional Kerala Kasavu Styling",
    poster: "/assets/images/instagram/CrAzwEnJ8FV.jpg"
  },
  {
    title: "Model Shaluz Boon Viral Hair Styling",
    handle: "@shaluz_boon",
    url: "https://www.instagram.com/livart_salon/reel/CpsA0o_OSo5/",
    code: "CpsA0o_OSo5",
    category: "celebrity",
    tag: "Viral Sensation",
    badge: "🔥 13K Likes Viral",
    service: "Model Haircut & Runway Finish",
    poster: "/assets/images/instagram/CpsA0o_OSo5.jpg"
  }
];

const BRIDAL_REELS = [
  {
    title: "Bridal Transformation & Special Offers",
    desc: "Complete bridal makeover package with glowing skin preparation and veil placement.",
    url: "https://www.instagram.com/livart_salon/reel/DdOmdkItPmF/",
    code: "DdOmdkItPmF",
    category: "bridal",
    badge: "Special Bridal Offer",
    service: "Gold Bridal Package",
    poster: "/assets/images/instagram/DdOmdkItPmF.jpg"
  },
  {
    title: "LivArt Academy Student Bride",
    desc: "Trained under Stephy Sebastian at LivArt Academy, styling a breathtaking wedding look.",
    url: "https://www.instagram.com/livart_salon/reel/Da8Hb68SA5B/",
    code: "Da8Hb68SA5B",
    category: "bridal",
    badge: "Academy Bride",
    service: "Bridal Makeup & Hair",
    poster: "/assets/images/instagram/Da8Hb68SA5B.jpg"
  },
  {
    title: "Hindu Bride Soft Glow Look",
    desc: "Dewy coral tones, temple jewelry coordination, and immaculate kasavu saree pleating.",
    url: "https://www.instagram.com/livart_salon/reel/DZSWz8wyz5i/",
    code: "DZSWz8wyz5i",
    category: "bridal",
    badge: "Hindu Bridal",
    service: "Diamond Bridal Package",
    poster: "/assets/images/instagram/DZSWz8wyz5i.jpg"
  },
  {
    title: "Christian Bridal Look by Stephy Sebastian",
    desc: "Elegant white gown styling, porcelain veil anchoring, and soft smoky eye glam.",
    url: "https://www.instagram.com/livart_salon/reel/DYuASLuK_le/",
    code: "DYuASLuK_le",
    category: "bridal",
    badge: "Christian Bridal",
    service: "Christian Bridal Couture",
    poster: "/assets/images/instagram/DYuASLuK_le.jpg"
  },
  {
    title: "Wedding Reception Glam (Deepika)",
    desc: "Glamorous cocktail evening makeover with high-shine lip lacquer and tousled waves.",
    url: "https://www.instagram.com/livart_salon/reel/DYFFX0RKhnx/",
    code: "DYFFX0RKhnx",
    category: "bridal",
    badge: "Reception Glam",
    service: "Reception Glam Package",
    poster: "/assets/images/instagram/DYFFX0RKhnx.jpg"
  },
  {
    title: "Reception Look Red Carpet Glam",
    desc: "Sculpted cheekbones, radiant contour, and dramatic evening shimmer eyes.",
    url: "https://www.instagram.com/livart_salon/reel/DX6qGl_SKf1/",
    code: "DX6qGl_SKf1",
    category: "bridal",
    badge: "Evening Glam",
    service: "Evening Bridal Reception",
    poster: "/assets/images/instagram/DX6qGl_SKf1.jpg"
  },
  {
    title: "Distinguished Groom Makeup & Styling",
    desc: "Camera-ready natural matte complexion, beard shaping, and hair design for the groom.",
    url: "https://www.instagram.com/livart_salon/reel/DXb3cLlEsmy/",
    code: "DXb3cLlEsmy",
    category: "bridal",
    badge: "Groom Sanctuary",
    service: "Black Diamond Groom Package",
    poster: "/assets/images/instagram/DXb3cLlEsmy.jpg"
  },
  {
    title: "Reception Glam Transformation",
    desc: "Effortless party glamour designed to transition seamlessly from photography to dance.",
    url: "https://www.instagram.com/livart_salon/reel/DWtk05cjLnI/",
    code: "DWtk05cjLnI",
    category: "bridal",
    badge: "Reception Glam",
    service: "Reception Makeup Package",
    poster: "/assets/images/instagram/DWtk05cjLnI.jpg"
  },
  {
    title: "Bridal Look Recreation (Part 1 Story)",
    desc: "Behind-the-scenes story recreating a timeless vintage bridal look for modern ceremonies.",
    url: "https://www.instagram.com/livart_salon/reel/DVyTy0qDJEN/",
    code: "DVyTy0qDJEN",
    category: "bridal",
    badge: "Bridal Story",
    service: "Custom Bridal Consultation",
    poster: "/assets/images/instagram/DVyTy0qDJEN.jpg"
  },
  {
    title: "Pre-Wedding High Definition (HD) Makeup",
    desc: "Ultra-fine HD pigments formulated for close-up video shoots and pre-wedding films.",
    url: "https://www.instagram.com/livart_salon/reel/DUap-mOkvuu/",
    code: "DUap-mOkvuu",
    category: "bridal",
    badge: "HD Pre-Wedding",
    service: "Pre-Wedding HD Makeup",
    poster: "/assets/images/instagram/DUap-mOkvuu.jpg"
  },
  {
    title: "Hindu Bridal Complete Makeover",
    desc: "Traditional jasmine hair braiding, gold eye shimmer, and waterproof setting.",
    url: "https://www.instagram.com/livart_salon/reel/DULWym5CHa0/",
    code: "DULWym5CHa0",
    category: "bridal",
    badge: "Hindu Bride",
    service: "Diamond Bridal Package",
    poster: "/assets/images/instagram/DULWym5CHa0.jpg"
  },
  {
    title: "Bridal Look with Designer Lehenga",
    desc: "Intricate dupatta setting, jewelry balancing, and regal bridal radiance.",
    url: "https://www.instagram.com/livart_salon/reel/DT7y-uAkh47/",
    code: "DT7y-uAkh47",
    category: "bridal",
    badge: "Lehenga Bride",
    service: "Gold Bridal Package",
    poster: "/assets/images/instagram/DT7y-uAkh47.jpg"
  },
  {
    title: "Christian Bridal Makeover (2 Looks)",
    desc: "Church ceremony soft modesty transitioned into an evening reception glam transformation.",
    url: "https://www.instagram.com/livart_salon/reel/DTu8FlyknZz/",
    code: "DTu8FlyknZz",
    category: "bridal",
    badge: "2-Look Bride",
    service: "Diamond Bridal Package",
    poster: "/assets/images/instagram/DTu8FlyknZz.jpg"
  },
  {
    title: "Muslim Bride Bespoke Makeup",
    desc: "Airbrush complexion, dramatic winged liner, and meticulous hijab & jewelry styling.",
    url: "https://www.instagram.com/livart_salon/reel/DTc2O2fCFZI/",
    code: "DTc2O2fCFZI",
    category: "bridal",
    badge: "Muslim Bride",
    service: "Gold Bridal Package",
    poster: "/assets/images/instagram/DTc2O2fCFZI.jpg"
  },
  {
    title: "Christian Bridal Transformation",
    desc: "Luminous porcelain skin, romantic half-up half-down curls, and flawless white veil drape.",
    url: "https://www.instagram.com/livart_salon/reel/DSpYR2dCJ5-/",
    code: "DSpYR2dCJ5-",
    category: "bridal",
    badge: "Christian Bride",
    service: "Christian Bridal Couture",
    poster: "/assets/images/instagram/DSpYR2dCJ5-.jpg"
  },
  {
    title: "Bride Natural Skin & Simple Aesthetic",
    desc: "Soft minimalism accentuating natural freckles and bone structure with subtle glow.",
    url: "https://www.instagram.com/livart_salon/reel/DSNGmIaEp4d/",
    code: "DSNGmIaEp4d",
    category: "bridal",
    badge: "Natural Minimalist",
    service: "Silver Bridal Package",
    poster: "/assets/images/instagram/DSNGmIaEp4d.jpg"
  },
  {
    title: "Glass Skin Bridal Makeup Kerala",
    desc: "Hydrating skincare prep followed by sheer micro-pigments for a reflective glass skin finish.",
    url: "https://www.instagram.com/livart_salon/reel/DRXFRQCEgpm/",
    code: "DRXFRQCEgpm",
    category: "bridal",
    badge: "Glass Skin",
    service: "Skin Miracle Hydra Glow Bridal",
    poster: "/assets/images/instagram/DRXFRQCEgpm.jpg"
  },
  {
    title: "Engagement Makeover (Personal Story)",
    desc: "Custom look tailored for an emotional family milestone, highlighting personal elegance.",
    url: "https://www.instagram.com/livart_salon/reel/DQ1XHMIjLJ8/",
    code: "DQ1XHMIjLJ8",
    category: "bridal",
    badge: "Engagement",
    service: "Engagement Glam Package",
    poster: "/assets/images/instagram/DQ1XHMIjLJ8.jpg"
  },
  {
    title: "Bride Alka Engagement Look",
    desc: "Radiant blush tones and polished Hollywood waves for bride Alka's special celebration.",
    url: "https://www.instagram.com/livart_salon/reel/DQMWOO5jNhc/",
    code: "DQMWOO5jNhc",
    category: "bridal",
    badge: "Real Bride Alka",
    service: "Engagement Makeup",
    poster: "/assets/images/instagram/DQMWOO5jNhc.jpg"
  },
  {
    title: "Bridal Makeup Glow",
    desc: "Warm bronze highlights and peach flush designed to look luminous under warm studio lamps.",
    url: "https://www.instagram.com/livart_salon/reel/DMDB3b4Nm0p/",
    code: "DMDB3b4Nm0p",
    category: "bridal",
    badge: "Warm Glow",
    service: "Gold Bridal Package",
    poster: "/assets/images/instagram/DMDB3b4Nm0p.jpg"
  },
  {
    title: "Signature Bridal Transformation",
    desc: "Step-by-step master application from skin priming to final setting spray by Stephy.",
    url: "https://www.instagram.com/livart_salon/reel/DK13xiot6zA/",
    code: "DK13xiot6zA",
    category: "bridal",
    badge: "Master Transformation",
    service: "Diamond Bridal Package",
    poster: "/assets/images/instagram/DK13xiot6zA.jpg"
  },
  {
    title: "Bridal & Party Hairstyle Volume Trick",
    desc: "Insider backstage technique for achieving sky-high volume without heavy hairspray crunch.",
    url: "https://www.instagram.com/livart_salon/reel/DJrQLH3Tk0n/",
    code: "DJrQLH3Tk0n",
    category: "bridal",
    badge: "Stylist Secret",
    service: "Bridal Hair Styling",
    poster: "/assets/images/instagram/DJrQLH3Tk0n.jpg"
  },
  {
    title: "Bride Trial Makeup Session",
    desc: "Behind the scenes of our relaxed pre-wedding trial session aligning with the bride's jewelry.",
    url: "https://www.instagram.com/livart_salon/reel/DIoW2P5TF7G/",
    code: "DIoW2P5TF7G",
    category: "bridal",
    badge: "Trial Session",
    service: "Bridal Trial Consultation",
    poster: "/assets/images/instagram/DIoW2P5TF7G.jpg"
  },
  {
    title: "Bridal Beauty at its Finest",
    desc: "Timeless traditional South Indian bridal majesty crafted at LivArt Kakkanad studio.",
    url: "https://www.instagram.com/livart_salon/reel/DIED9XjSKku/",
    code: "DIED9XjSKku",
    category: "bridal",
    badge: "Haute Couture",
    service: "Diamond Bridal Package",
    poster: "/assets/images/instagram/DIED9XjSKku.jpg"
  },
  {
    title: "Signature Bridal Makeup Artistry",
    desc: "Soft contouring and long-wear pigments ensuring zero oxidation throughout the ceremony.",
    url: "https://www.instagram.com/livart_salon/reel/DGVbSkPSXIi/",
    code: "DGVbSkPSXIi",
    category: "bridal",
    badge: "Bridal Art",
    service: "Gold Bridal Package",
    poster: "/assets/images/instagram/DGVbSkPSXIi.jpg"
  },
  {
    title: "Essential Bridal Hair Tip for To-Be Brides",
    desc: "Why regular hair spa therapy 4 weeks before the wedding makes bridal hair styling effortless.",
    url: "https://www.instagram.com/livart_salon/reel/DC9Ou8ETksn/",
    code: "DC9Ou8ETksn",
    category: "bridal",
    badge: "Hair Secret",
    service: "L'Oreal Hair Spa & Prep",
    poster: "/assets/images/instagram/DC9Ou8ETksn.jpg"
  },
  {
    title: "Christian Bride Niby Katherine",
    desc: "Spotlight on real bride Niby Katherine's bespoke bridal styling and veil draping.",
    url: "https://www.instagram.com/livart_salon/reel/C7CYp17t9yd/",
    code: "C7CYp17t9yd",
    category: "bridal",
    badge: "Real Bride Niby",
    service: "Christian Bridal Couture",
    poster: "/assets/images/instagram/C7CYp17t9yd.jpg"
  }
];

const ALL_REELS = [...CELEBRITY_REELS, ...BRIDAL_REELS];

const CONTAINER_CONFIGS = {
  'instagram-feed-grid': { category: 'all', limit: 6, initialLimit: 6, step: 6 },
  'celebrity-reels-grid': { category: 'celebrity', limit: 6, initialLimit: 6, step: 6 },
  'bridal-reels-grid': { category: 'bridal', limit: 6, initialLimit: 6, step: 6 }
};

function generateDirectEmbedCard(reel) {
  const isCeleb = reel.category === "celebrity";
  const badgeColor = isCeleb ? "text-amber-300 border-amber-400/40 bg-amber-950/40" : "text-rose-300 border-rose-400/40 bg-rose-950/40";
  const isSubpage = (window.location.pathname.includes('/gallery') || window.location.pathname.includes('/services') || window.location.pathname.includes('/about-us') || window.location.pathname.includes('/teams') || window.location.pathname.includes('/blog') || window.location.pathname.includes('/packages') || window.location.pathname.includes('/make-up') || window.location.pathname.includes('/hair-styling') || window.location.pathname.includes('/skin-care') || window.location.pathname.includes('/academy') || window.location.pathname.includes('/contact-us'));
  const rootPrefix = isSubpage ? '../' : '';
  const posterSrc = rootPrefix + 'assets/images/instagram/' + reel.code + '.jpg';

  return `
  <div class="direct-embed-card bg-obsidian-surface rounded-2xl border border-white/10 shadow-2xl p-3 sm:p-4 flex flex-col justify-between hover:border-champagne-gold/50 transition-all duration-300">
    <!-- Top Meta Info -->
    <div class="flex items-center justify-between gap-2 pb-2.5 mb-2 border-b border-white/10">
      <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider border ${badgeColor}">
        ${reel.badge}
      </span>
      <div class="flex items-center gap-1 text-[11px] text-metallic-gold-light truncate">
        <span class="font-bold truncate">${subLabel}</span>
        <span class="material-symbols-outlined text-[13px] text-sky-400" style="font-variation-settings: 'FILL' 1;">verified</span>
      </div>
    </div>

    <!-- Direct Official Instagram Player: Renders Authentic Instagram Reel Thumbnail & Player (0ms delay, no raw text) -->
    <div class="instagram-embed-box relative w-full h-[460px] sm:h-[520px] bg-black rounded-xl overflow-hidden my-2 shadow-inner">
      <!-- Authentic Instagram Cover Image Background while iframe loads -->
      <img src="${posterSrc}" alt="${reel.title}" class="absolute inset-0 w-full h-full object-cover opacity-70 pointer-events-none transition-opacity duration-500" loading="lazy" />
      <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-black/40 pointer-events-none flex flex-col items-center justify-center gap-2">
        <div class="w-10 h-10 rounded-full border-2 border-champagne-gold/40 border-t-champagne-gold animate-spin"></div>
        <span class="text-[10px] text-champagne-gold font-bold uppercase tracking-wider bg-black/60 px-2.5 py-0.5 rounded-full backdrop-blur-sm">Instagram Direct Player</span>
      </div>

      <!-- Direct Official Embed Iframe (Meta Instagram) -->
      <iframe 
        src="https://www.instagram.com/reel/${reel.code}/embed/" 
        class="relative z-10 w-full h-full border-0 rounded-xl bg-transparent" 
        frameborder="0" 
        scrolling="no" 
        allowtransparency="true" 
        allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
        loading="lazy"
        title="${reel.title}">
      </iframe>
    </div>

    <!-- Bottom Actions & Booking -->
    <div class="pt-3 mt-1 border-t border-white/10 flex items-center justify-between gap-2">
      <div class="text-left flex-1 min-w-0">
        <h5 class="font-serif-luxury text-xs text-white font-bold truncate mb-0.5" title="${reel.title}">
          ${reel.title}
        </h5>
        <span class="text-[10px] text-gray-400 truncate block">${reel.service}</span>
      </div>
      <div class="flex items-center gap-1.5 shrink-0">
        <a href="${reel.url}" target="_blank" rel="noopener noreferrer" class="bg-white/15 hover:bg-white/25 text-white p-2 sm:p-1.5 rounded-lg transition-all flex items-center justify-center min-w-[36px] min-h-[36px]" title="Watch on Instagram App / Web" aria-label="Watch on Instagram">
          <span class="material-symbols-outlined text-[16px] sm:text-[14px]">open_in_new</span>
        </a>
        <button onclick="openBookingModal('${reel.service}')" class="bg-champagne-gold hover:bg-white active:scale-95 text-obsidian-deep py-2 px-3.5 sm:py-1.5 sm:px-3 rounded-lg text-[11px] sm:text-[10px] font-bold uppercase tracking-wider transition-all shadow-md min-h-[36px]">
          Book Look
        </button>
      </div>
    </div>
  </div>
  `;
}

function renderDirectEmbedReels(containerId = "instagram-feed-grid") {
  const container = document.getElementById(containerId);
  if (!container) return;

  const config = CONTAINER_CONFIGS[containerId] || { category: 'all', limit: 6, initialLimit: 6, step: 6 };

  let allItems = ALL_REELS;
  if (config.category === "celebrity") {
    allItems = CELEBRITY_REELS;
  } else if (config.category === "bridal") {
    allItems = BRIDAL_REELS;
  }

  const totalCount = allItems.length;
  const currentLimit = config.limit;
  const visibleItems = allItems.slice(0, currentLimit);
  const shownCount = visibleItems.length;
  const hasMore = shownCount < totalCount;
  const isExpanded = currentLimit > config.initialLimit;

  // Render direct embed cards instantly (0ms delay)
  container.innerHTML = visibleItems.map(generateDirectEmbedCard).join('');

  // Render / Update Expand Controls Bar
  let expandBar = document.getElementById(containerId + '-expand-bar');
  if (!expandBar) {
    expandBar = document.createElement('div');
    expandBar.id = containerId + '-expand-bar';
    expandBar.className = 'mt-10 text-center w-full flex justify-center px-4 sm:px-0';
    container.parentNode.insertBefore(expandBar, container.nextSibling);
  }

  const stepCount = Math.min(config.step, totalCount - shownCount);

  expandBar.innerHTML = `
    <div class="flex flex-col sm:flex-row flex-wrap items-center justify-center gap-3 p-3 bg-obsidian-surface border border-champagne-gold/30 rounded-2xl shadow-2xl w-full sm:w-auto">
      <div class="flex items-center gap-2 px-3 py-1 text-center justify-center">
        <span class="w-2 h-2 rounded-full bg-champagne-gold animate-pulse"></span>
        <span class="text-xs text-gray-200 font-medium">
          Showing <strong class="text-champagne-gold">${shownCount}</strong> of <strong class="text-white">${totalCount}</strong> Video Reels
        </span>
      </div>

      ${hasMore ? `
      <button onclick="window.expandReels('${containerId}', ${config.step})" class="w-full sm:w-auto justify-center bg-champagne-gold hover:bg-white active:scale-95 text-obsidian-deep px-5 py-3 sm:py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-md flex items-center gap-1.5 min-h-[44px] sm:min-h-[auto]">
        <span class="material-symbols-outlined text-[18px] sm:text-[16px]">expand_more</span>
        <span>Expand (+${stepCount} More Videos)</span>
      </button>

      <button onclick="window.expandAllReels('${containerId}')" class="w-full sm:w-auto justify-center bg-white/10 hover:bg-white/20 active:scale-95 text-white border border-white/20 px-4 py-3 sm:py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1.5 min-h-[44px] sm:min-h-[auto]">
        <span class="material-symbols-outlined text-[18px] sm:text-[16px]">fullscreen</span>
        <span>Expand All (${totalCount})</span>
      </button>
      ` : `
      <span class="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs font-bold">
        <span class="material-symbols-outlined text-[16px]">check_circle</span>
        <span>All ${totalCount} Video Reels Loaded</span>
      </span>
      `}

      ${isExpanded ? `
      <button onclick="window.collapseReels('${containerId}')" class="w-full sm:w-auto justify-center bg-white/5 hover:bg-white/15 active:scale-95 text-gray-300 hover:text-white px-4 py-3 sm:py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-1 border border-white/10 min-h-[44px] sm:min-h-[auto]">
        <span class="material-symbols-outlined text-[18px] sm:text-[16px]">expand_less</span>
        <span>Collapse to Limited View (6)</span>
      </button>
      ` : ''}
    </div>
  `;
}

function processInstagramEmbeds() {
  if (window.instgrm && window.instgrm.Embeds) {
    window.instgrm.Embeds.process();
  } else if (!document.querySelector('script[src*="instagram.com/embed.js"]')) {
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.instagram.com/embed.js';
    document.body.appendChild(script);
  }
}

// Global Controls
window.expandReels = function(containerId, step = 6) {
  if (!CONTAINER_CONFIGS[containerId]) {
    CONTAINER_CONFIGS[containerId] = { category: 'all', limit: 6, initialLimit: 6, step: 6 };
  }
  CONTAINER_CONFIGS[containerId].limit += step;
  renderDirectEmbedReels(containerId);
};

window.expandAllReels = function(containerId) {
  if (!CONTAINER_CONFIGS[containerId]) {
    CONTAINER_CONFIGS[containerId] = { category: 'all', limit: 6, initialLimit: 6, step: 6 };
  }
  CONTAINER_CONFIGS[containerId].limit = 999;
  renderDirectEmbedReels(containerId);
};

window.collapseReels = function(containerId) {
  if (CONTAINER_CONFIGS[containerId]) {
    CONTAINER_CONFIGS[containerId].limit = CONTAINER_CONFIGS[containerId].initialLimit;
    renderDirectEmbedReels(containerId);
    const container = document.getElementById(containerId);
    if (container) {
      container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
};

window.filterReelsCategory = function(cat, containerId = "instagram-feed-grid") {
  const buttons = document.querySelectorAll('.reel-filter-btn');
  buttons.forEach(btn => {
    if (btn.getAttribute('data-category') === cat) {
      btn.classList.add('bg-champagne-gold', 'text-obsidian-deep');
      btn.classList.remove('bg-obsidian-surface', 'text-gray-300');
    } else {
      btn.classList.remove('bg-champagne-gold', 'text-obsidian-deep');
      btn.classList.add('bg-obsidian-surface', 'text-gray-300');
    }
  });

  if (!CONTAINER_CONFIGS[containerId]) {
    CONTAINER_CONFIGS[containerId] = { category: 'all', limit: 6, initialLimit: 6, step: 6 };
  }
  CONTAINER_CONFIGS[containerId].category = cat;
  CONTAINER_CONFIGS[containerId].limit = CONTAINER_CONFIGS[containerId].initialLimit;
  renderDirectEmbedReels(containerId);
};

window.renderDirectEmbedReels = renderDirectEmbedReels;
window.renderCategorizedReels = renderDirectEmbedReels;

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('instagram-feed-grid')) {
    renderDirectEmbedReels('instagram-feed-grid');
  }
  if (document.getElementById('celebrity-reels-grid')) {
    renderDirectEmbedReels('celebrity-reels-grid');
  }
  if (document.getElementById('bridal-reels-grid')) {
    renderDirectEmbedReels('bridal-reels-grid');
  }
});