import os
import json
from generator import (
    BASE_DIR, SITE_NAME, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    render_head, render_header, render_footer
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

LOCATIONS_DATA = [
    {
        "slug": "infopark-kochi",
        "name": "Infopark Kochi (Phase 1 & Phase 2)",
        "short_name": "Infopark",
        "distance": "1.8 km • 4–6 mins drive",
        "landmarks": "Carnival Infopark, Lulu Cyber Tower 1 & 2, World Trade Center Kochi, Athulya & Thapasya",
        "commute_directions": "Take the Infopark Expressway toward Seaport-Airport Road. Turn right at the NGO Quarters junction; Anchorage Business Centre is on your left on the 2nd Floor, with dedicated reserved client parking.",
        "badge": "Tech Park Sanctuary",
        "title": "Best Beauty Parlour & Hair Salon near Infopark Kochi | LivArt",
        "desc": "Top salon & beauty parlour near Infopark Kochi. 5 mins from Lulu Cyber Tower. L'Oreal hair spa, hair botox, nail art, hydra facials & bridal makeup at LivArt.",
        "headline": "Premier Beauty Parlour, Hair Salon & Spa Near Infopark Kochi",
        "subheading": "Recharge 5 minutes from your workstation. Express lunchtime scalp therapies, post-shift unwinding, and master styling curated for Kochi's tech community.",
        "img": "../assets/images/instagram/CpsA0o_OSo5.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          For software engineers, product leaders, and corporate teams across <strong>Infopark Phase 1 & Phase 2</strong>, long screen hours, air-conditioned dry office air, and high Kerala humidity can take a serious toll on scalp vitality and skin health.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Situated just <strong>1.8 km from Infopark Main Gate</strong> at Anchorage Business Centre on Seaport-Airport Road, <strong>LivArt Salon & Make-Up Studio</strong> is the preferred luxury grooming sanctuary for IT professionals. Whether you need a quick 45-minute express <em>L'Oréal Hair Spa</em> during your lunch break, an executive beard trim before an international client presentation, or a weekend <em>Hair Botox rejuvenation</em>, our master team accommodates your dynamic schedule.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Tailored for Infopark Professionals</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Late Evening Working Hours:</strong> Open Monday to Saturday until 8:30 PM, letting you decompress after your sprint or shift.</li>
          <li><strong>Stress-Relief Scalp Acupressure:</strong> Hot oil head massages and steam therapies specifically targeting neck, shoulder, and cranial strain caused by desk posture.</li>
          <li><strong>High-Speed Reserved Parking:</strong> Ample client parking so you never waste precious break time searching for a spot.</li>
          <li><strong>Club LivArt Corporate Privilege:</strong> Flat 25% savings across all 234 salon treatments with our Grand Member Card.</li>
        </ul>
        """,
        "featured_services": [
            ("L'Oreal Professional Hair Spa", "Express scalp rejuvenation and acupressure massage.", "₹800", "45 mins"),
            ("Capillary Hair Botox", "Humidity-proof anti-frizz formula lasting up to 5 months.", "₹5,999", "2.5 hrs"),
            ("Executive Haircut & Beard Architecture", "Bone-structure tailored cut with precision razor lines.", "₹600", "40 mins"),
            ("Skin Miracle Hydra Facial", "Painless vortex pore extraction & hyaluronic infusion.", "₹4,000", "60 mins")
        ],
        "faqs": [
            {
                "q": "How far is LivArt Salon from Infopark Kochi?",
                "a": "LivArt Salon is located just 1.8 km from Infopark Phase 1 Main Gate (approximately 4 to 6 minutes drive via the Infopark Expressway onto Seaport-Airport Road)."
            },
            {
                "q": "Can I get an express service during my lunch break?",
                "a": "Yes! We offer 30-to-45 minute express services including L'Oreal Hair Spa, Beard Architecture, Instant D-Tan Cleanses, and Precision Haircuts. WhatsApp us in advance to reserve your exact time slot."
            },
            {
                "q": "Are evening appointments available after office hours?",
                "a": "Absolutely. LivArt Kakkanad operates Monday through Saturday until 8:30 PM and Sundays until 7:30 PM to accommodate corporate and shift workers."
            }
        ]
    },
    {
        "slug": "smartcity-kochi",
        "name": "SmartCity Kochi",
        "short_name": "SmartCity",
        "distance": "2.4 km • 6–8 mins drive",
        "landmarks": "SmartCity Pavilion, Sands InfinIT, Interlink Global, Edachira Junction",
        "commute_directions": "Head west from SmartCity toward Edachira Junction, proceed along the Seaport-Airport Road toward NGO Quarters. LivArt is situated on the 2nd Floor of Anchorage Business Centre.",
        "badge": "Corporate Tech Hub",
        "title": "Best Unisex Salon near SmartCity Kochi | Luxury Grooming | LivArt",
        "desc": "Luxury salon near SmartCity Kochi. 7 mins away at Anchorage Business Centre. L'Oreal hair colour, keratin smoothing, Hydra facials, and bridal styling by Stephy Sebastian.",
        "headline": "Executive Grooming & Dermal Aesthetics Near SmartCity Kochi",
        "subheading": "Premium styling, anti-frizz hair therapies, and revitalizing facials engineered for SmartCity Kochi executives and professionals.",
        "img": "../assets/images/instagram/DbLJRauyFro.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          As <strong>SmartCity Kochi</strong> expands into a world-class IT and technology hub, business leaders, entrepreneurs, and global consultants require grooming and aesthetic care that reflects their executive caliber.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Located an easy 7-minute drive away on Seaport-Airport Road, <strong>LivArt Salon & Make-Up Studio</strong> offers a tranquil private environment away from corporate hustle. Directed by celebrity artist and master educator <strong>Stephy Sebastian</strong>, LivArt delivers bespoke hair architecture, clinical dermal therapies, and red-carpet wedding packages.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Why SmartCity Clients Prefer LivArt</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Direct Master Consultations:</strong> Stylists analyze your face structure, hair porosity, and daily routine before scissors touch your hair.</li>
          <li><strong>Clinical Hygiene Standards:</strong> Autoclave-sanitized stainless instruments and single-use hygiene kits for absolute peace of mind.</li>
          <li><strong>Seamless WhatsApp Concierge:</strong> Instant booking and digital confirmations via +91 70120 59591.</li>
        </ul>
        """,
        "featured_services": [
            ("Director's Haircut with Stephy Sebastian", "Bespoke structural cut tailored to your facial architecture.", "₹1,500", "45 mins"),
            ("LivArt Majestic Keratin Smoothing", "Thermal protein seal delivering silky, manageable locks.", "From ₹5,000", "3 hrs"),
            ("Casmara Spanish Luxury Facial", "Cooling marine alginate peel-off mask that tones & depuffs.", "From ₹5,000", "90 mins"),
            ("Black Diamond Groom Package", "Complete camera-ready matte makeover for wedding events.", "₹7,500", "2 hrs")
        ],
        "faqs": [
            {
                "q": "What is the fastest route from SmartCity Kochi to LivArt Salon?",
                "a": "Drive via Edachira to Seaport-Airport Road. Anchorage Business Centre is on the 2nd Floor, right next to the NGO Quarters and Mavelipuram junction."
            },
            {
                "q": "Does LivArt offer weekend bridal trials for SmartCity residents?",
                "a": "Yes! Stephy Sebastian hosts dedicated pre-wedding bridal trials on Saturdays and Sundays. Advance booking is recommended."
            }
        ]
    },
    {
        "slug": "kakkanad",
        "name": "Kakkanad Central (Seaport-Airport Road)",
        "short_name": "Kakkanad",
        "distance": "0 km • Flagship Atelier Location",
        "landmarks": "Civil Station Kakkanad, NGO Quarters, Mavelipuram Road, Collectorate Junction",
        "commute_directions": "Located directly on Seaport-Airport Road on the 2nd Floor of Anchorage Business Centre, directly opposite NGO Quarters and Mavelipuram junction.",
        "badge": "Flagship Headquarters",
        "title": "Best Salon & Beauty Parlour in Kakkanad, Kochi | Hair & Bridal | LivArt",
        "desc": "Rated #1 salon in Kakkanad Kochi on Seaport-Airport Rd. Hair botox, keratin, hydra facials, nail art & bridal makeup by celebrity artist Stephy Sebastian. 4.9★.",
        "headline": "Kakkanad's Premier Haute Couture Salon & Make-Up Studio",
        "subheading": "Welcome to our flagship atelier. 234 certified beauty treatments, L'Oréal and Casmara certified master technicians, and Cochin's top bridal artist.",
        "img": "../assets/images/instagram/DW1NAndDGuP.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Established in the heart of Kakkanad on Seaport-Airport Road, <strong>LivArt Salon & Make-Up Studio</strong> represents the pinnacle of contemporary cosmetology in Ernakulam district.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Featuring separate luxury styling zones for men and women, private bridal dressing suites, and a specialized scalp therapy lounge, LivArt caters to discerning residents across Kakkanad, NGO Quarters, and Mavelipuram. With over <strong>480+ five-star verified Google reviews</strong>, LivArt has redefined beauty standards across Kochi.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">The LivArt Kakkanad Distinction</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>234 Transparently Priced Services:</strong> Full menu transparency with zero surprise add-ons.</li>
          <li><strong>Club LivArt Membership:</strong> Save up to 25% flat on all treatments year-round.</li>
          <li><strong>Celebrity Artistry:</strong> Founder Stephy Sebastian brings national educator credentials from L'Oréal and Wella.</li>
        </ul>
        """,
        "featured_services": [
            ("Capillary Hair Botox", "100% Formaldehyde-free frizz elimination.", "₹5,999", "3 hrs"),
            ("4K Ultra-HD Bridal Makeup", "Flawless camera-ready bridal base with saree draping.", "₹25,000", "3.5 hrs"),
            ("Skin Miracle Hydra Facial", "Painless vortex suction and deep peptide infusion.", "₹4,000", "75 mins"),
            ("Deluxe Spa Pedicure & Reflexology", "Dead-skin callus therapy and acupressure massage.", "₹1,200", "60 mins")
        ],
        "faqs": [
            {
                "q": "Where exactly is LivArt Salon located in Kakkanad?",
                "a": "LivArt is on the 2nd Floor of Anchorage Business Centre, Seaport-Airport Road, near NGO Quarters and Mavelipuram Road, Kakkanad, Kochi 682030."
            },
            {
                "q": "Is parking available at the Kakkanad salon?",
                "a": "Yes, Anchorage Business Centre features dedicated ground-level reserved parking for LivArt salon patrons."
            }
        ]
    },
    {
        "slug": "thrikkakara",
        "name": "Thrikkakara",
        "short_name": "Thrikkakara",
        "distance": "2.2 km • 5–7 mins drive",
        "landmarks": "Thrikkakara Vamana Moorthy Temple, Model Engineering College, Thrikkakara Municipality",
        "commute_directions": "Drive east along Pipeline Road or Civil Station Road toward Seaport-Airport Road. Turn onto Seaport-Airport Road heading toward NGO Quarters; Anchorage Business Centre is on your left.",
        "badge": "Heritage & Family Hub",
        "title": "Best Salon near Thrikkakara, Kochi | Bridal & Hair Care | LivArt",
        "desc": "Leading family salon near Thrikkakara. 5 mins from Thrikkakara Temple. Traditional Hindu Muhurtham makeup, saree pleating, kids haircuts, and hair botox at LivArt.",
        "headline": "Exquisite Bridal Makeovers & Family Hair Care Near Thrikkakara",
        "subheading": "Authentic Kerala Hindu Muhurtham bridal styling, precision saree draping, and luxurious restorative hair care for Thrikkakara families.",
        "img": "../assets/images/instagram/DULWym5CHa0.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          For families and brides living around the historic <strong>Thrikkakara Temple</strong> and Model Engineering College campus, finding a beauty parlour that balances traditional Kerala wedding aesthetics with modern dermatological science is vital.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          <strong>LivArt Salon</strong> is just 5 minutes away on Seaport-Airport Road. Our bridal studio specializes in timeless <em>Hindu Muhurtham bridal styling</em>: glowing temple gold makeup, smudge-proof kohl, authentic fresh jasmine floral styling, and precision Kanchipuram silk saree draping with box pleating that stays immaculate throughout sacred rituals.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Family & Bridal Specialties</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Muhurtham Bridal Artistry:</strong> Sweat-proof and tear-proof HD makeup tailored for traditional Kerala wedding lighting.</li>
          <li><strong>Pre-Pleated Saree Draping:</strong> Ironed box folding and on-client saree pinning from ₹1,000.</li>
          <li><strong>Complete Family Packages:</strong> Haircuts, organic threading, herbal waxing, and gentle styling for children and seniors.</li>
        </ul>
        """,
        "featured_services": [
            ("Hindu Muhurtham Bridal Package", "Traditional radiance, jasmine setting, and silk saree draping.", "From ₹18,000", "3.5 hrs"),
            ("Pre-Pleated Saree Draping", "Ironed box folding and precision waist-cinching.", "₹1,000", "30 mins"),
            ("O3+ Bridal Brightening Facial", "Pigmentation correction and luminous bridal radiance.", "₹3,000", "75 mins"),
            ("Women's Precision Haircut & Blowout", "Layer, feather, or bob cuts finished with runway bounce.", "₹800", "45 mins")
        ],
        "faqs": [
            {
                "q": "How long does it take to reach LivArt Salon from Thrikkakara?",
                "a": "LivArt is approximately 2.2 km away, taking around 5 to 7 minutes via Civil Station Road to Seaport-Airport Road."
            },
            {
                "q": "Do you offer saree draping services for wedding guests from Thrikkakara?",
                "a": "Yes! We offer on-client saree draping (₹1,500), pre-pleated box folding (₹1,000), and rapid saree styling for wedding guests and bridesmaids."
            }
        ]
    },
    {
        "slug": "palarivattom",
        "name": "Palarivattom",
        "short_name": "Palarivattom",
        "distance": "4.5 km • 10–12 mins drive",
        "landmarks": "Palarivattom Junction, Pipeline Road, Padivattom, Jawaharlal Nehru Stadium Corridor",
        "commute_directions": "Head east along Civil Station Road straight toward Kakkanad. Merge onto Seaport-Airport Road at the Collectorate Junction; LivArt is 500 meters ahead on the 2nd Floor of Anchorage Business Centre.",
        "badge": "Urban Metro Corridor",
        "title": "Top Luxury Salon near Palarivattom, Kochi | Hair & Bridal | LivArt",
        "desc": "Skip city traffic! Top luxury salon 10 mins from Palarivattom on Seaport-Airport Rd Kakkanad. Ample parking, celebrity bridal artist Stephy Sebastian, Hair Botox.",
        "headline": "Couture Artistry & Hair Care Just 10 Minutes from Palarivattom",
        "subheading": "Avoid city parking hassles and experience spacious luxury salon facilities, celebrity bridal consultations, and advanced humidity-proof hair smoothing.",
        "img": "../assets/images/instagram/DYuASLuK_le.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Residents of <strong>Palarivattom and Padivattom</strong> frequently face severe traffic congestion and near-impossible parking at commercial salons along the Palarivattom–Bypass stretch.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          A pleasant 10-minute drive down Civil Station Road brings you to <strong>LivArt Salon Kakkanad</strong>, where dedicated reserved parking, tranquil high-ceiling interiors, and personal attention from celebrity stylist <strong>Stephy Sebastian</strong> await. Discerning brides and style connoisseurs choose LivArt as their serene alternative to crowded central city parlours.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Signature Experiences</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Hassle-Free Private Suites:</strong> Enjoy dedicated, unhurried bridal trials and scalp spas in serene luxury.</li>
          <li><strong>Ammonia-Free Balayage:</strong> Custom French freehand painting using premium L'Oréal Inoa palettes.</li>
          <li><strong>Zero Wait Time:</strong> Pre-scheduled appointments guarantee your chair and master stylist the moment you arrive.</li>
        </ul>
        """,
        "featured_services": [
            ("Dimensional Balayage & Toning", "Hand-painted caramel babylights with zero ammonia damage.", "From ₹2,500", "2.5 hrs"),
            ("Capillary Hair Botox", "Deep keratin void filling eliminating 95% of frizz.", "₹5,999", "3 hrs"),
            ("Airbrush Bridal Makeup", "16-hour waterproof micro-mist silicone bridal base.", "₹50,000", "3 hrs"),
            ("Deluxe Manicure & Pedicure Spa", "Full callus filing, sugar scrub, and reflexology massage.", "₹1,900", "90 mins")
        ],
        "faqs": [
            {
                "q": "Why travel from Palarivattom to LivArt Salon in Kakkanad?",
                "a": "LivArt offers dedicated stress-free parking, larger private styling suites, and direct service from former L'Oreal national educator Stephy Sebastian, just 10 minutes down Civil Station Road."
            },
            {
                "q": "Can I book a bridal trial if I live in Palarivattom?",
                "a": "Yes! We welcome brides from Palarivattom for personalized consultations and makeup trials. WhatsApp +91 70120 59591 to coordinate with Stephy Sebastian."
            }
        ]
    },
    {
        "slug": "kalamassery",
        "name": "Kalamassery",
        "short_name": "Kalamassery",
        "distance": "5.2 km • 10–12 mins drive",
        "landmarks": "CUSAT Campus, Premier Junction, Kalamassery Metro, Kerala Startup Mission",
        "commute_directions": "Drive south directly down Seaport-Airport Road toward Kakkanad. Anchorage Business Centre is on your right near the NGO Quarters junction, featuring dedicated client parking.",
        "badge": "Academic & Tech Corridor",
        "title": "Best Salon near Kalamassery, Kochi | Hair Botox & Balayage | LivArt",
        "desc": "Top hair salon near Kalamassery & CUSAT. Direct 10-min drive down Seaport-Airport Rd. Trend haircuts, balayage, keratin smoothing, and bridal styling at LivArt.",
        "headline": "Trendsetting Hair Styling & Aesthetics Direct from Kalamassery",
        "subheading": "Direct expressway access down Seaport-Airport Road. Trendy hair colours, texture transformations, and clinical skincare for students, faculty, and professionals.",
        "img": "../assets/images/instagram/C5pwjmOidQU.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Connected seamlessly via the <strong>Seaport-Airport Road expressway</strong>, Kalamassery residents, university scholars at CUSAT, and researchers at the Startup Village have direct, traffic-free access to <strong>LivArt Salon Kakkanad</strong> in under 12 minutes.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Whether you want a modern textured wolf cut, vibrant balayage colour melt, or permanent humidity smoothing through our signature <em>Capillary Hair Botox</em>, our salon is the top choice for trend-conscious individuals along the northern corridor.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Popular Northern Corridor Services</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Direct Seaport-Airport Connectivity:</strong> Straight drive with zero city bottlenecks.</li>
          <li><strong>Student & Club Privileges:</strong> Special annual membership savings offering up to 25% off all haircuts and hair colouring.</li>
          <li><strong>Advanced Texture Treatments:</strong> Keratin smoothing and thermal rebonding that withstand heavy monsoons.</li>
        </ul>
        """,
        "featured_services": [
            ("Creative Balayage Hair Colouring", "Multi-dimensional caramel, copper, and ash tones.", "From ₹2,500", "2.5 hrs"),
            ("Capillary Hair Botox Rejuvenation", "Flat rate anti-aging hair repair complex.", "₹5,999", "3 hrs"),
            ("LivArt Permanent Hair Rebonding", "Pin-straight silky glass hair enduring through monsoon.", "From ₹5,000", "3.5 hrs"),
            ("Precision Haircut & Styling", "Custom face-framing layers or modern fade cuts.", "From ₹400", "40 mins")
        ],
        "faqs": [
            {
                "q": "How do I get to LivArt Salon from Kalamassery?",
                "a": "Simply drive straight south down Seaport-Airport Road for approximately 5 km. LivArt is on the 2nd Floor of Anchorage Business Centre, right at the NGO Quarters intersection."
            },
            {
                "q": "Are there membership discounts for frequent hair coloring and cuts?",
                "a": "Yes! Our Club LivArt Privilege Cards (Classic 10%, Premium 15%, Grand 25%) provide instant flat discounts on all hair, skin, and grooming treatments for an entire year."
            }
        ]
    },
    {
        "slug": "edachira",
        "name": "Edachira Junction",
        "short_name": "Edachira",
        "distance": "1.2 km • 3 mins drive",
        "landmarks": "Infopark North Gate, DLF Riverside, Trinity World, Edachira Bus Stop",
        "commute_directions": "Drive south along Seaport-Airport Road toward Kakkanad. Anchorage Business Centre is on your right in under 3 minutes.",
        "badge": "Neighborhood Proximity",
        "title": "Best Salon in Edachira, Kakkanad | Hair, Waxing & Skin Care | LivArt",
        "desc": "Closest luxury salon to Edachira Kakkanad. 3 mins from DLF & Infopark North Gate. Painless Rica waxing, Hydra Facials, hair spa, haircuts & bridal services.",
        "headline": "Your Neighborhood Luxury Salon 3 Minutes from Edachira",
        "subheading": "Walking and quick driving distance for Edachira and DLF apartment communities. Precision hair styling, pain-free waxing, and relaxing scalp spas.",
        "img": "../assets/images/instagram/DRXFRQCEgpm.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          For residents of <strong>Edachira, DLF Riverside, Trinity World</strong>, and neighboring high-rise communities, having a certified, hygienic luxury salon just 3 minutes away is the ultimate lifestyle convenience.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          At <strong>LivArt Salon</strong>, you never have to settle for basic neighbourhood parlour standards. Experience international Rica waxing, organic eyebrow threading, medical-grade <em>Skin Miracle Hydra Facials</em>, and nourishing hair spas in a serene, temperature-controlled environment.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Walk-In & Rapid Care Services</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Pain-Free Rica Waxing:</strong> Italian liposoluble wax that protects sensitive tropical skin.</li>
          <li><strong>Organic Threading:</strong> Precision brow shaping and facial hair removal without skin pinching.</li>
          <li><strong>Instant De-Tan Therapy:</strong> Sara herbal milk protein treatments removing weekend sun tan in 30 minutes.</li>
        </ul>
        """,
        "featured_services": [
            ("Rica Liposoluble Full Waxing", "Gentle, redness-free Italian wax for arms and legs.", "₹1,800", "45 mins"),
            ("Sara Herbal D-Tan Whitening", "Quick facial sun tan removal with instant radiance.", "₹800", "30 mins"),
            ("L'Oreal Professional Hair Spa", "Deep steam treatment for dry, frizzy city hair.", "From ₹800", "60 mins"),
            ("Designer Haircut & Runway Blow Dry", "Personalized layers and bouncy salon blowout.", "₹800", "45 mins")
        ],
        "faqs": [
            {
                "q": "How close is LivArt Salon to Edachira Junction?",
                "a": "LivArt is only 1.2 km from Edachira Junction, taking less than 3 minutes by car or auto down Seaport-Airport Road."
            },
            {
                "q": "Can I walk in without an appointment from Edachira?",
                "a": "Walk-ins are welcomed 7 days a week! For weekends or specialized treatments like Hair Botox and Hydra Facials, a quick WhatsApp reservation ensures zero wait."
            }
        ]
    },
    {
        "slug": "vazhakkala",
        "name": "Vazhakkala & Padamughal",
        "short_name": "Vazhakkala",
        "distance": "3.1 km • 7–9 mins drive",
        "landmarks": "Padamughal Junction, Vazhakkala Church, Palachuvadu, Chembumukku",
        "commute_directions": "Drive east along Padamughal–Kakkanad Road onto Seaport-Airport Road. Turn toward NGO Quarters; Anchorage Business Centre is on your left on the 2nd Floor.",
        "badge": "Residential Beauty Hub",
        "title": "Best Salon near Vazhakkala & Padamughal, Kochi | LivArt",
        "desc": "Top-rated beauty parlour & hair salon near Vazhakkala and Padamughal. 7 mins away in Kakkanad. Pre-bridal skincare, hair spa, haircuts, and bridal makeup.",
        "headline": "Elevated Bridal Artistry & Hair Care Near Vazhakkala",
        "subheading": "A quick 7-minute drive for Vazhakkala and Padamughal residents seeking high-definition bridal artistry, pre-wedding skin prep, and luxury hair rejuvenation.",
        "img": "../assets/images/instagram/DTc2O2fCFZI.jpg",
        "story": """
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Residents across <strong>Vazhakkala, Padamughal, and Palachuvadu</strong> looking for modern aesthetic treatments and master bridal artistry find their ideal salon home at <strong>LivArt Salon Kakkanad</strong>.
        </p>
        <p class="text-base text-gray-700 leading-relaxed mb-4">
          Co-founded by celebrity artist <strong>Stephy Sebastian</strong>, LivArt is renowned for creating custom Christian bridal gown looks with cathedral veil pinning, Muslim Nikah glam with dramatic winged eyeliner, and pre-bridal skin brightening regimens that prepare brides for their wedding week.
        </p>
        <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mt-8 mb-3">Pre-Bridal & Beauty Favorites</h3>
        <ul class="list-disc pl-5 space-y-2.5 text-sm text-gray-700 mb-6">
          <li><strong>Pre-Wedding Dermal Regimens:</strong> 3-stage Hydra Facial, lactic brightening peel, and deep body polishing.</li>
          <li><strong>Christian & Nikah Bridal Couture:</strong> Bespoke veil and dupatta setting designed to look breathtaking on camera.</li>
          <li><strong>Full Family Grooming:</strong> Executive men's styling, children's cuts, and luxury pedicures under one roof.</li>
        </ul>
        """,
        "featured_services": [
            ("Signature Bridal Couture Package", "Direct artistry by Stephy Sebastian with pre-bridal prep.", "₹25,000", "Full Day"),
            ("Skin Miracle Hydra Facial", "Vortex vacuum pore cleanse and deep hyaluronic glow.", "₹4,000", "75 mins"),
            ("Capillary Hair Botox", "Eliminates frizz and repairs broken hair bonds.", "₹5,999", "3 hrs"),
            ("Deluxe Spa Pedicure", "Herbal foot soak, callus filing, and acupressure massage.", "₹1,200", "60 mins")
        ],
        "faqs": [
            {
                "q": "How far is LivArt Salon from Vazhakkala?",
                "a": "LivArt is approximately 3.1 km from Vazhakkala (7 to 9 minutes drive via Padamughal Road onto Seaport-Airport Road)."
            },
            {
                "q": "Does LivArt offer custom pre-bridal packages for Vazhakkala brides?",
                "a": "Yes! Our Silver, Gold, and Diamond Couture bridal packages include pre-wedding skincare, hair spa rituals, nail gel art, and trial sessions customized to your wedding timeline."
            }
        ]
    }
]

# -------------------------------------------------------------
# 1. BUILD /locations/ DIRECTORY INDEX (HUB PAGE)
# -------------------------------------------------------------
def build_locations_hub():
    ensure_dir(os.path.join(BASE_DIR, "locations"))

    hub_breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": "Locations", "item": BASE_URL + "/locations/"}
        ]
    }

    cards_html = ""
    for loc in LOCATIONS_DATA:
        services_pills = "".join([f'<span class="inline-block bg-black/5 text-gray-700 px-2 py-0.5 rounded text-[10px] font-semibold">{s[0]}</span>' for s in loc["featured_services"][:3]])
        
        cards_html += f"""
        <div class="bg-surface-container-low rounded-3xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between group">
          <div class="h-48 overflow-hidden bg-obsidian-deep relative">
            <img src="{loc['img']}" alt="LivArt Salon serving {loc['name']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-deep/80 via-transparent to-transparent"></div>
            <div class="absolute top-3 left-3 bg-champagne-gold text-obsidian-deep px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest">
              {loc['badge']}
            </div>
            <div class="absolute bottom-3 left-4 right-4 text-white">
              <span class="text-[10px] font-bold text-champagne-gold uppercase tracking-wider block">{loc['distance']}</span>
              <h3 class="font-serif-luxury text-xl font-bold">{loc['name']}</h3>
            </div>
          </div>

          <div class="p-6 flex flex-col justify-between flex-grow">
            <div>
              <p class="text-xs text-muted-slate mb-4 leading-relaxed">
                {loc['desc']}
              </p>
              <div class="mb-4">
                <span class="text-[10px] font-bold uppercase tracking-wider text-warm-bronze block mb-1.5">Key Landmarks:</span>
                <p class="text-xs text-gray-600 line-clamp-2">{loc['landmarks']}</p>
              </div>
              <div class="flex flex-wrap gap-1.5 mb-6">
                {services_pills}
              </div>
            </div>

            <div class="pt-4 border-t border-black/5 flex items-center justify-between">
              <a href="./{loc['slug']}/index.html" class="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-obsidian-deep hover:text-champagne-gold transition-colors">
                <span>Explore Neighborhood Hub</span>
                <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
              </a>
              <a href="https://wa.me/917012059591?text=Hi%20LivArt%20Salon,%20I%20am%20inquiring%20from%20{loc['short_name']}" target="_blank" rel="noopener noreferrer" class="p-2 rounded-lg bg-emerald-50 text-emerald-700 hover:bg-emerald-600 hover:text-white transition-colors" title="WhatsApp Booking from {loc['short_name']}">
                <span class="material-symbols-outlined text-[18px]">chat</span>
              </a>
            </div>
          </div>
        </div>
        """

    html = render_head(
        title="Salon Locations & Neighborhood Directory in Kochi | LivArt Kakkanad",
        description="Find LivArt Salon near you across Kochi: Infopark, SmartCity, Kakkanad, Thrikkakara, Palarivattom, Kalamassery, Edachira, and Vazhakkala. Reserved parking & master stylists.",
        canonical_path="/locations/",
        extra_schema=hub_breadcrumb_schema,
        root_prefix="../"
    )
    html += render_header(active_slug="locations", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <!-- Hero Section -->
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
        Kochi Regional Presence & Commute Directory
      </span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">
        LivArt Salon Neighborhood Locations in Kochi
      </h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Centrally anchored on Seaport-Airport Road in Kakkanad, LivArt provides world-class hair styling, clinical skincare, and celebrity bridal artistry to residents and professionals across Greater Kochi.
      </p>
    </div>
  </section>

  <!-- Neighborhood Directory Grid -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-xl mx-auto mb-12">
        <span class="font-label-caps text-xs text-warm-bronze tracking-[0.2em] uppercase font-semibold block mb-1">
          Select Your Area
        </span>
        <h2 class="font-serif-luxury text-3xl font-bold text-obsidian-deep">
          Find Your Nearest LivArt Service Route
        </h2>
        <p class="text-xs text-muted-slate mt-2">
          Discover personalized transit directions, express office packages, and neighborhood-specific salon perks.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        {cards_html}
      </div>

      <!-- Studio Location Banner -->
      <div class="mt-16 p-8 sm:p-12 bg-obsidian-deep text-alabaster-cream rounded-3xl border border-champagne-gold/30 shadow-2xl flex flex-col lg:flex-row items-center justify-between gap-8">
        <div class="max-w-2xl">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-champagne-gold/10 border border-champagne-gold/30 text-champagne-gold text-[10px] font-bold uppercase tracking-widest mb-3">
            <span class="material-symbols-outlined text-[14px]">location_on</span>
            <span>Flagship Atelier & Academy</span>
          </div>
          <h3 class="font-serif-luxury text-2xl sm:text-3xl font-bold text-white mb-2">
            Anchorage Business Centre, Seaport-Airport Road
          </h3>
          <p class="text-xs sm:text-sm text-gray-300 leading-relaxed mb-4">
            2nd Floor, NGO Quarters – Mavelipuram Road Junction, Kakkanad, Kochi, Kerala 682030.<br />
            Featuring reserved client parking, elevator access, separate gent/ladies zones, and private bridal dressing suites.
          </p>
          <div class="flex flex-wrap items-center gap-4 text-xs text-champagne-gold font-bold">
            <span>GPS: 10.021406° N, 76.342732° E</span>
            <span>•</span>
            <span>Mon–Sat: 9:30 AM – 8:30 PM</span>
            <span>•</span>
            <span>Sunday: 10:00 AM – 7:30 PM</span>
          </div>
        </div>
        <div class="flex flex-col sm:flex-row items-center gap-4 shrink-0 w-full lg:w-auto">
          <a href="https://maps.google.com/?q=LivArt+Salon+Kakkanad" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto bg-champagne-gold hover:bg-white text-obsidian-deep px-6 py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all shadow-md flex items-center justify-center gap-2">
            <span>Open in Google Maps</span>
            <span class="material-symbols-outlined text-[16px]">directions</span>
          </a>
          <a href="tel:{PHONE_TEL}" class="w-full sm:w-auto border border-white/20 hover:bg-white/10 text-white px-6 py-3.5 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center justify-center gap-2">
            <span class="material-symbols-outlined text-[16px]">call</span>
            <span>Call Desk {PHONE}</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")

    with open(os.path.join(BASE_DIR, "locations", "index.html"), "w") as f:
        f.write(html)
    print("✓ locations/index.html hub built")

# -------------------------------------------------------------
# 2. BUILD INDIVIDUAL /locations/[slug]/ SPOKE PAGES
# -------------------------------------------------------------
def build_location_spokes():
    for loc in LOCATIONS_DATA:
        dir_path = os.path.join(BASE_DIR, "locations", loc["slug"])
        ensure_dir(dir_path)

        # Build Rich Schema (LocalBusiness + FAQPage + BreadcrumbList)
        faq_entities = [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            } for item in loc["faqs"]
        ]

        extra_schemas = [
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Locations", "item": BASE_URL + "/locations/"},
                    {"@type": "ListItem", "position": 3, "name": loc["name"], "item": f"{BASE_URL}/locations/{loc['slug']}/"}
                ]
            },
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]

        faq_items_html = ""
        for idx, faq in enumerate(loc["faqs"]):
            faq_items_html += f"""
            <details class="faq-item group bg-surface-container-low rounded-xl p-5 border border-black/5 transition-all">
              <summary class="flex items-center justify-between cursor-pointer font-serif-luxury text-base sm:text-lg font-bold text-obsidian-deep list-none select-none">
                <span>{idx + 1}. {faq['q']}</span>
                <span class="faq-icon material-symbols-outlined text-warm-bronze transition-transform duration-300">expand_more</span>
              </summary>
              <div class="mt-4 pt-4 border-t border-black/5 text-xs sm:text-sm text-gray-700 leading-relaxed">
                {faq['a']}
              </div>
            </details>
            """

        services_html = ""
        for s_title, s_desc, s_price, s_dur in loc["featured_services"]:
            services_html += f"""
            <div class="bg-surface-container-low p-5 rounded-2xl border border-black/5 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-2">
                  <span class="text-[10px] font-bold uppercase tracking-wider text-warm-bronze">{s_dur}</span>
                  <span class="font-serif-luxury text-base font-bold text-obsidian-deep">{s_price}</span>
                </div>
                <h4 class="font-serif-luxury text-lg font-bold text-obsidian-deep mb-1">{s_title}</h4>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">{s_desc}</p>
              </div>
              <button data-open-booking data-service="{s_title}" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-2 rounded-lg text-xs font-bold uppercase tracking-wider transition-all">
                Book This Service
              </button>
            </div>
            """

        other_locations_html = ""
        for other in LOCATIONS_DATA:
            if other["slug"] != loc["slug"]:
                other_locations_html += f"""
                <a href="../{other['slug']}/index.html" class="p-3 bg-surface-container-low hover:bg-champagne-gold/10 rounded-xl border border-black/5 text-xs font-semibold text-obsidian-deep flex items-center justify-between transition-colors">
                  <span>{other['short_name']}</span>
                  <span class="text-[10px] text-muted-slate font-normal">{other['distance'].split('•')[0].strip()}</span>
                </a>
                """

        og_img = loc["img"].replace("../", f"{BASE_URL}/")
        html = render_head(
            title=loc["title"],
            description=loc["desc"],
            canonical_path=f"/locations/{loc['slug']}/",
            extra_schema=extra_schemas,
            root_prefix="../../",
            og_image=og_img
        )
        html += render_header(active_slug="locations", root_prefix="../../")

        whatsapp_prefill = f"Hi%20LivArt%20Salon,%20I%20am%20contacting%20you%20from%20{loc['short_name']}%20to%20book%20an%20appointment"

        html += f"""
<main class="flex-grow">
  <!-- Breadcrumb Bar -->
  <div class="bg-surface-container py-3 border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-xs text-muted-slate flex items-center gap-2">
      <a href="../../index.html" class="hover:text-obsidian-deep">Home</a>
      <span>/</span>
      <a href="../index.html" class="hover:text-obsidian-deep">Locations</a>
      <span>/</span>
      <span class="text-obsidian-deep font-semibold">{loc['name']}</span>
    </div>
  </div>

  <!-- Hero Header -->
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center gap-2 mb-3">
        <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold px-2.5 py-0.5 rounded-full bg-champagne-gold/10 border border-champagne-gold/30">
          {loc['badge']}
        </span>
        <span class="text-xs text-gray-400">•</span>
        <span class="text-xs text-gray-300 font-medium">{loc['distance']} to LivArt Kakkanad</span>
      </div>
      <h1 class="font-serif-luxury text-3xl sm:text-5xl font-bold text-alabaster-cream mb-4">
        {loc['headline']}
      </h1>
      <p class="text-base text-gray-300 max-w-3xl leading-relaxed mb-6">
        {loc['subheading']}
      </p>
      <div class="flex flex-wrap gap-4">
        <a href="https://wa.me/917012059591?text={whatsapp_prefill}" target="_blank" rel="noopener noreferrer" class="bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all shadow-md flex items-center gap-2">
          <span class="material-symbols-outlined text-[16px]">chat</span>
          <span>Book via WhatsApp ({loc['short_name']})</span>
        </a>
        <a href="https://maps.google.com/?q=LivArt+Salon+Kakkanad" target="_blank" rel="noopener noreferrer" class="border border-white/20 hover:bg-white/10 text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px]">directions</span>
          <span>Get Driving Directions</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Main Content & Neighborhood Insights -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <!-- Left 8 Columns: Narrative & Services -->
        <div class="lg:col-span-8">
          <div class="rounded-3xl overflow-hidden shadow-lg mb-8 max-h-[400px] bg-obsidian-deep relative">
            <img src="{loc['img']}" alt="LivArt Salon serving clients from {loc['name']}" class="w-full h-full object-cover" loading="lazy" />
            <div class="absolute bottom-4 left-4 right-4 bg-obsidian-deep/85 backdrop-blur-md p-4 rounded-2xl border border-white/10 text-white text-xs">
              <strong class="text-champagne-gold">Commute Route from {loc['short_name']}:</strong> {loc['commute_directions']}
            </div>
          </div>

          <div class="prose max-w-none text-gray-800">
            {loc['story']}
          </div>

          <!-- Featured Local Services Grid -->
          <div class="mt-12">
            <div class="flex items-center justify-between mb-6">
              <div>
                <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block">Client Favorites</span>
                <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep">Popular Treatments for {loc['short_name']} Patrons</h3>
              </div>
              <a href="../../services/index.html#catalog" class="text-xs font-bold text-champagne-gold hover:underline flex items-center gap-1">
                <span>All 234 Services</span>
                <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
              </a>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
              {services_html}
            </div>
          </div>

          <!-- Neighborhood FAQ Section -->
          <div class="mt-16">
            <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">Local Knowledge Base</span>
            <h3 class="font-serif-luxury text-2xl font-bold text-obsidian-deep mb-6">Frequently Asked Questions: {loc['short_name']} to LivArt</h3>
            <div class="space-y-4">
              {faq_items_html}
            </div>
          </div>
        </div>

        <!-- Right 4 Columns: Commute Card & Quick Booking Sidebar -->
        <div class="lg:col-span-4 flex flex-col gap-6">
          <!-- Commute & Location Info Box -->
          <div class="bg-surface-container-low p-6 rounded-3xl border border-black/5 shadow-sm">
            <div class="flex items-center gap-3 pb-4 border-b border-black/5 mb-4">
              <div class="w-10 h-10 rounded-xl bg-champagne-gold/20 text-champagne-gold flex items-center justify-center shrink-0">
                <span class="material-symbols-outlined text-[20px]">near_me</span>
              </div>
              <div>
                <h4 class="font-serif-luxury text-base font-bold text-obsidian-deep">{loc['short_name']} Commute Stats</h4>
                <p class="text-[11px] text-muted-slate">{loc['distance']}</p>
              </div>
            </div>

            <div class="space-y-3 text-xs text-gray-700 mb-6">
              <div>
                <strong class="text-obsidian-deep block mb-0.5">Nearby Landmarks:</strong>
                <p class="text-gray-600">{loc['landmarks']}</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-0.5">Studio Address:</strong>
                <p class="text-gray-600">2nd Floor, Anchorage Business Centre, Seaport-Airport Rd, Kakkanad</p>
              </div>
              <div>
                <strong class="text-obsidian-deep block mb-0.5">Parking:</strong>
                <p class="text-emerald-700 font-medium">✓ Reserved Client Ground Parking</p>
              </div>
            </div>

            <a href="https://maps.google.com/?q=LivArt+Salon+Kakkanad" target="_blank" rel="noopener noreferrer" class="w-full bg-obsidian-deep hover:bg-champagne-gold text-white hover:text-obsidian-deep py-3 rounded-xl text-xs font-bold uppercase tracking-widest transition-all flex items-center justify-center gap-2 mb-3">
              <span class="material-symbols-outlined text-[16px]">navigation</span>
              <span>Start Navigation</span>
            </a>

            <a href="https://wa.me/917012059591?text={whatsapp_prefill}" target="_blank" rel="noopener noreferrer" class="w-full border border-emerald-600/30 text-emerald-700 hover:bg-emerald-50 py-2.5 rounded-xl text-xs font-bold uppercase tracking-wider transition-all flex items-center justify-center gap-1.5">
              <span class="material-symbols-outlined text-[16px]">chat</span>
              <span>Reserve via WhatsApp</span>
            </a>
          </div>

          <!-- Club LivArt Privilege Callout -->
          <div class="bg-gradient-to-br from-obsidian-deep to-obsidian-surface text-alabaster-cream p-6 rounded-3xl border border-champagne-gold/30 shadow-xl">
            <span class="text-[10px] font-bold uppercase tracking-widest text-champagne-gold block mb-2">Club LivArt Privilege</span>
            <h4 class="font-serif-luxury text-lg font-bold text-white mb-2">Save 25% on Every Visit</h4>
            <p class="text-xs text-gray-300 leading-relaxed mb-4">
              Living or working in {loc['short_name']}? Unlock flat 25% savings across all 234 treatments for 1 full year with our Grand Membership Card.
            </p>
            <a href="../../packages/index.html#memberships" class="inline-flex items-center gap-1 text-xs font-bold text-champagne-gold hover:underline">
              <span>View Membership Tiers</span>
              <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
            </a>
          </div>

          <!-- Other Kochi Neighborhoods -->
          <div class="bg-surface-container-low p-6 rounded-3xl border border-black/5">
            <h4 class="font-serif-luxury text-base font-bold text-obsidian-deep mb-3">Other Kochi Neighborhoods</h4>
            <div class="flex flex-col gap-2">
              {other_locations_html}
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
        print(f"✓ locations/{loc['slug']}/index.html built")

if __name__ == "__main__":
    build_locations_hub()
    build_location_spokes()
