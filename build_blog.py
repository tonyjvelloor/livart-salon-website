import os
import json
from generator import (
    LOGO_URL,
    BASE_DIR, SITE_NAME, BASE_URL, PHONE, PHONE_TEL, EMAIL, ADDRESS, HOURS,
    render_head, render_header, render_footer
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

BLOG_POSTS = [
    {
        "slug": "how-to-choose-the-right-salon-for-your-needs",
        "title": "How to Choose the Right Salon for Your Needs",
        "category": "Salon Guide",
        "cat_slug": "hair",
        "date": "September 12, 2024",
        "read_time": "5 min read",
        "desc": "Key factors to evaluate when choosing a salon in Kochi: stylist certification, hygiene standards, product authenticity, and customer consultations.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner14.jpg",
        "content": """
        <p>Finding the right salon is about discovering a trusted team that understands your individual hair texture, skin sensitivity, and aesthetic ambitions. Here is what discerning clients look for:</p>
        <h3>1. In-Depth Stylist Consultation</h3>
        <p>A premier salon never rushes into a cut or color. Masters take time to analyze your face shape, daily routine, hair porosity, and previous chemical history before recommending styles.</p>
        <h3>2. Authenticity of Formulations</h3>
        <p>Ensure your salon utilizes sealed, certified international products (such as L'Oreal Professionnel and Cheryl's Cosmeceuticals). Counterfeit or cheap products cause irreversible cuticle breakdown.</p>
        <h3>3. Hospital-Grade Hygiene Protocols</h3>
        <p>At LivArt Salon Kakkanad, instruments undergo clinical sanitization between every single client appointment, ensuring serene peace of mind.</p>
        """
    },
    {
        "slug": "what-is-in-your-make-up-bag",
        "title": "What is in your make-up bag?",
        "category": "Makeup",
        "cat_slug": "makeup",
        "date": "August 28, 2024",
        "read_time": "4 min read",
        "desc": "Master artist Stephy Sebastian shares essential everyday makeup bag items for Indian humidity and tropical skin tones.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner26.jpg",
        "content": """
        <p>Curating the ideal daily beauty kit doesn't require dozens of products—it requires formulas tailored to Indian skin undertones and humid weather:</p>
        <h3>1. Lightweight Matte Primer & Tint</h3>
        <p>Silicone or water-gel primers prevent foundation from separating in Kerala heat. Pair with a breathable skin tint.</p>
        <h3>2. Cream-to-Powder Blush</h3>
        <p>Warm terracotta and peach tones bring natural radiance to olive and dusky complexions without sliding off.</p>
        <h3>3. Waterproof Kohl & Mascara</h3>
        <p>Smudge-proof eye makeup is essential. Look for ophthalmologist-tested formulas that resist monsoon humidity.</p>
        """
    },
    {
        "slug": "what-is-balayage-hair-colouring",
        "title": "What is Balayage Hair colouring?",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "August 15, 2024",
        "read_time": "6 min read",
        "desc": "Understand balayage hair color technique, difference from highlights, maintenance tips, and top shades for Indian hair at LivArt Kakkanad.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner19.jpg",
        "content": """
        <p>Originating from the French word meaning 'to sweep', Balayage is a freehand hair coloring technique where master colorists hand-paint highlights onto sections of hair, creating a sun-kissed, graduated gradient.</p>
        <h3>Balayage vs. Traditional Foil Highlights</h3>
        <p>Unlike traditional highlights that leave stark demarcation lines at the root, Balayage blends seamlessly into your natural base tone, allowing hair to grow out naturally with zero awkward re-growth lines.</p>
        <h3>Top Balayage Tones for Indian Hair</h3>
        <ul>
          <li><strong>Honey Caramel:</strong> Adds warmth and dimension to dark brown and black hair.</li>
          <li><strong>Melted Chocolate & Mocha:</strong> Subtle, sophisticated corporate-friendly gradient.</li>
          <li><strong>Chestnut Auburn:</strong> Ideal for warm undertones looking for radiant depth.</li>
        </ul>
        """
    },
    {
        "slug": "indian-summer-care-everything-you-need-to-know",
        "title": "Indian Summer Care: Everything You Need To Know",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "July 30, 2024",
        "read_time": "5 min read",
        "desc": "Complete summer skin and hair care guide for Indian tropical weather: sun protection, deep hydration, and anti-pigmentation rituals.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner21.jpg",
        "content": """
        <p>High temperatures combined with intense coastal humidity present a double challenge: dehydration and excess sebum. Here is how to shield your skin and hair:</p>
        <h3>Barrier Repair & Broad Spectrum Defense</h3>
        <p>Apply broad-spectrum PA++++ sunscreen with SPF 50 every 3 hours. Seek out non-comedogenic gel formulations.</p>
        <h3>De-Tan Scalp & Skin Facials</h3>
        <p>Monthly salon de-tan rituals break down melanin buildup from ultraviolet exposure, keeping skin luminous and unclogged.</p>
        """
    },
    {
        "slug": "embrace-the-summer-glow-essential-skin-care-tips",
        "title": "Embrace the Summer Glow: Essential Skin Care Tips",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "July 18, 2024",
        "read_time": "4 min read",
        "desc": "How to achieve luminous, glass skin during summer months without oiliness or breakouts.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner22.jpg",
        "content": """
        <p>Summer glow should come from deep cellular hydration, not grease. Incorporate hyaluronic serums and antioxidant Vitamin C topicals to protect skin collagen from sun stress.</p>
        """
    },
    {
        "slug": "rain-proof-your-hair-essential-tips-for-monsoon-hair-care",
        "title": "Rain-Proof Your Hair: Essential Tips for Monsoon Hair Care",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "June 25, 2024",
        "read_time": "5 min read",
        "desc": "Monsoon hair survival guide: combating humidity frizz, scalp fungal buildup, and breakage with LivArt Salon treatments.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_-offer-poster2_11-7-2023-1.jpg",
        "content": """
        <p>Monsoons in Kerala bring 90%+ ambient humidity. Rainwater is acidic and collects atmospheric pollutants, weakening keratin bonds. A Keratin smoothing or Hair Botox treatment provides an impermeable hydrophobic shield that repels moisture.</p>
        """
    },
    {
        "slug": "5-most-stylish-and-practical-hairstyles-for-this-monsoon",
        "title": "5 Most Stylish and Practical Hairstyles for this Monsoon!",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "June 10, 2024",
        "read_time": "4 min read",
        "desc": "Chic, easy-to-manage haircuts and updos that look polished and stay frizz-free throughout rainy days.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/05/poster1.jpg",
        "content": """
        <p>Keep your tresses chic and tangle-free with textured lob cuts, high braided ponytails, messy French twists, and permanent blowouts that hold structure naturally.</p>
        """
    },
    {
        "slug": "anything-and-everything-about-hair-botox-treatment",
        "title": "Anything and Everything about Hair Botox Treatment",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "May 22, 2024",
        "read_time": "6 min read",
        "desc": "Comprehensive guide to Hair Botox: how it works, active ingredients, differences from Keratin, and why it's Kochi's top anti-frizz treatment.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_-offer-poster2_11-7-2023-1.jpg",
        "content": """
        <p>Despite its name, Hair Botox contains zero botulinum toxin. It is a deep-conditioning, anti-aging capillary treatment designed to 'fill in' cracks in hair fibers like cosmetic botox fills skin wrinkles.</p>
        <h3>Active Nourishing Agents</h3>
        <p>Formulated with caviar oil, collagen, amino acids, and vitamin E, Hair Botox restores structural elasticity to dry, heat-damaged, or over-processed hair.</p>
        """
    },
    {
        "slug": "hair-colouring-guidelines-dos-and-donts-for-a-stunning-transformation",
        "title": "Hair Colouring Guidelines: Dos and Don'ts for a Stunning Transformation",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "May 05, 2024",
        "read_time": "5 min read",
        "desc": "Stylist advice on preparing your hair for color, maintaining vibrancy, and avoiding tone fade.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_offer-poster3_11-7-2023-1.jpg",
        "content": """
        <p>Do opt for ammonia-free L'Oreal formulations. Don't wash hair with piping hot water. Do use color-protecting sulfate-free shampoo to seal the outer cuticle.</p>
        """
    },
    {
        "slug": "revealing-the-real-glow-all-you-need-to-know-about-hydra-facial",
        "title": "Revealing the Real Glow: All you need to know about Hydra Facial!",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "April 20, 2024",
        "read_time": "6 min read",
        "desc": "How Hydra Facial combines vortex extraction, lactic exfoliation, and hyaluronic infusion for poreless, red-carpet radiance.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_offer-poster1_11-7-2023-1.jpg",
        "content": """
        <p>Discover why the Skin Miracle Hydra Facial is Kakkanad's most booked pre-event aesthetic ritual. With zero downtime, pores are painlessly vacuumed clean while antioxidants infuse into fresh dermal layers.</p>
        """
    },
    {
        "slug": "picture-perfect-wedding-beauty-care-tips-for-brides-to-be",
        "title": "Picture-Perfect Wedding: Beauty Care Tips for Brides-to-Be",
        "category": "Bridal",
        "cat_slug": "makeup",
        "date": "April 02, 2024",
        "read_time": "7 min read",
        "desc": "Stephy Sebastian's 6-month bridal beauty timeline: pre-bridal facials, hair spa schedules, makeup trials, and big-day preparations.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner24.jpg",
        "content": """
        <p>A flawless wedding day glow begins months before walking down the aisle. Follow Stephy Sebastian's proven milestone calendar to ensure your skin and hair look breathtaking in 4K photography.</p>
        """
    },
    {
        "slug": "what-haircuts-are-best-for-your-face-shape",
        "title": "Which Haircuts Are Best For Your Face Shape?",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "March 18, 2024",
        "read_time": "5 min read",
        "desc": "Expert face shape analysis: round, oval, square, and heart face haircut recommendations by LivArt senior stylists.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner14.jpg",
        "content": """
        <p>Discover how layering, face-framing curtain bangs, and blunt lob cuts balance facial proportions and highlight cheekbones and jawlines.</p>
        """
    },
    {
        "slug": "daily-hair-care-routine-for-indian-hair",
        "title": "Daily Hair Care Routine for Indian Hair",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "March 01, 2024",
        "read_time": "5 min read",
        "desc": "Scientifically backed daily and weekly hair care rituals designed specifically for Indian hair density, oil production, and hard water conditions.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/05/livee11.jpg",
        "content": """
        <p>Indian hair tends to be coarse and prone to humidity frizz. Balancing traditional scalp oil massage with modern sulfate-free clarifying washes keeps follicles robust and shiny.</p>
        """
    },
    {
        "slug": "exploring-ombre-hair-color-a-stylish-gradient-for-your-tresses",
        "title": "Exploring Ombre Hair Color: A Stylish Gradient for Your Tresses",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "February 15, 2024",
        "read_time": "4 min read",
        "desc": "The difference between Ombre and Balayage, color pairing ideas, and aftercare for radiant dark-to-light hair gradients.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner19.jpg",
        "content": """
        <p>Ombre creates a dramatic two-tone transition from deep roots into striking lighter ends. Learn how LivArt colorists blend seamless gradients that preserve hair strength.</p>
        """
    },
    {
        "slug": "glow-and-shield-easy-sunscreen-hacks-for-your-skins-radiance",
        "title": "Glow and Shield: Easy Sunscreen Hacks for Your Skin's Radiance!",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "February 01, 2024",
        "read_time": "4 min read",
        "desc": "How to avoid white cast, reapply over makeup, and choose broad-spectrum sunscreens for Indian skin.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner21.jpg",
        "content": """
        <p>Sun protection is the number one anti-aging secret. Explore sunscreen sticks, setting mists, and lightweight gel formulations that protect without greasy residue.</p>
        """
    },
    {
        "slug": "hair-myths-debunked",
        "title": "Hair Myths Debunked",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "January 20, 2024",
        "read_time": "5 min read",
        "desc": "Salon experts bust common hair myths: trimming frequency, split ends repair, gray hair plucking, and daily shampooing truths.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner18.jpg",
        "content": """
        <p>Separating hair science from folklore. Learn the truth about frequent haircuts, heat protectants, and why professional salon treatments make all the difference.</p>
        """
    },
    {
        "slug": "why-pedicure-is-important-in-beauty-care-relaxing-health-and-aesthetic-benefits",
        "title": "Why Pedicure is Important in Beauty Care: Relaxing Health and Aesthetic Benefits",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "January 05, 2024",
        "read_time": "5 min read",
        "desc": "Beyond pretty nails: the medical and relaxation benefits of regular professional pedicures for blood circulation and foot health.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner23.jpg",
        "content": """
        <p>Your feet bear the weight of your entire day. Professional pedicures eliminate cracked heels, prevent fungal infections, and stimulate acupressure zones.</p>
        """
    },
    {
        "slug": "7-tips-for-maintaining-your-salon-styled-hair-between-visits",
        "title": "7 Tips for Maintaining Your Salon-Styled Hair Between Visits",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "December 18, 2023",
        "read_time": "4 min read",
        "desc": "How to extend your salon blowout, keep balayage bright, and retain moisture between salon visits.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/05/poster1.jpg",
        "content": """
        <p>Silk pillowcases, leave-in serums, cool water rinses, and gentle micro-fiber drying extend that fresh-out-of-the-salon glow for weeks.</p>
        """
    },
    {
        "slug": "top-10-advantages-of-hair-spa-in-salon",
        "title": "Top 10 Advantages Of Hair Spa in Salon",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "December 02, 2023",
        "read_time": "6 min read",
        "desc": "10 proven benefits of professional salon hair spa therapies: scalp detox, follicle stimulation, dandruff control, and deep mental stress reduction.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/05/livee11.jpg",
        "content": """
        <p>A professional hair spa goes far beyond home conditioning. High-temperature steam opens the hair cuticle, driving active nutrients into the cortex while acupressure relieves cranial tension.</p>
        """
    },
    {
        "slug": "treat-your-feet-experience-luxury-with-our-deluxe-pedicure-services",
        "title": "Treat Your Feet: Experience Luxury with Our Deluxe Pedicure Services",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "November 19, 2023",
        "read_time": "4 min read",
        "desc": "Indulge in LivArt's deluxe foot spa ritual featuring herbal soaks, sea salt exfoliation, and relaxing reflexology massage.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner23.jpg",
        "content": """
        <p>Experience the ultimate foot pampering session at LivArt Salon Kakkanad. Our deluxe pedicure leaves your feet baby-soft and completely rejuvenated.</p>
        """
    },
    {
        "slug": "perfect-bridal-makeup-artist-a-guide-to-finding-your-ideal-look-for-the-big-day",
        "title": "Perfect Bridal Makeup Artist: A Guide to Finding Your Ideal Look for the Big Day",
        "category": "Bridal",
        "cat_slug": "makeup",
        "date": "November 05, 2023",
        "read_time": "6 min read",
        "desc": "How to choose your bridal makeup artist in Kochi, ask the right trial questions, and articulate your vision for a timeless wedding look.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner24.jpg",
        "content": """
        <p>Choosing your bridal artist is one of the most critical decisions of your wedding. Learn what portfolio cues to look for and how Stephy Sebastian personalizes bridal aesthetics.</p>
        """
    },
    {
        "slug": "classic-and-modern-wedding-hairstyles-for-bride",
        "title": "Exploring Classic and Modern Wedding Hairstyles for Bride",
        "category": "Bridal",
        "cat_slug": "hair",
        "date": "October 22, 2023",
        "read_time": "5 min read",
        "desc": "Inspirational wedding hairstyles: traditional South Indian jasmine braids, romantic textured low buns, and glamorous Hollywood waves.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner25.jpg",
        "content": """
        <p>From traditional Kerala kasavu saree braids adorned with fresh temple flowers to contemporary Christian bridal veils with soft tousled waves, explore top bridal hair trends.</p>
        """
    },
    {
        "slug": "tips-and-tricks-at-womens-beauty-parlour",
        "title": "Expert Makeup Tips and Tricks at a Women's Beauty Parlour",
        "category": "Makeup",
        "cat_slug": "makeup",
        "date": "October 08, 2023",
        "read_time": "5 min read",
        "desc": "Insider beauty parlour tips from LivArt stylists: color correcting dark circles, setting powder secrets, and natural eyebrow feathering.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner26.jpg",
        "content": """
        <p>Learn the professional hacks used by senior makeup artists to achieve seamless blending, crease-free concealer, and lipstick that lasts all day.</p>
        """
    },
    {
        "slug": "perfect-head-massage-experience",
        "title": "Stress Reliever: Salon Secrets – Insider Advice for the Perfect Head Massage Experience",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "September 24, 2023",
        "read_time": "4 min read",
        "desc": "The therapeutic science of warm oil Indian head massages: pressure points, stress relief, and root nourishment.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner18.jpg",
        "content": """
        <p>A traditional head massage activates marma pressure points, draining lymphatic congestion, lowering cortisol, and encouraging robust follicular health.</p>
        """
    },
    {
        "slug": "haircuts-and-techniques-by-leading-stylists",
        "title": "Your Gateway to Trendsetting Haircuts and Techniques by Leading Stylists",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "September 10, 2023",
        "read_time": "5 min read",
        "desc": "Discover modern dry cutting, point cutting, and texturizing techniques practiced by LivArt Salon stylists in Kakkanad.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner14.jpg",
        "content": """
        <p>A great haircut is engineered to fall into place with minimal effort at home. Learn how precision texturizing removes bulk while maintaining bouncy movement.</p>
        """
    },
    {
        "slug": "the-best-facial-treatments-at-your-salon",
        "title": "The Skincare Sanctum: The Best Facials & Treatments at your Salon",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "August 25, 2023",
        "read_time": "5 min read",
        "desc": "Guide to choosing between Hydra Facials, De-Tan Whitening, Gold Glow, and Cheryl's Pro Facials for your specific skin concerns.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner21.jpg",
        "content": """
        <p>Not all facials are created equal. Understand the clinical difference between clarifying extraction facials, hydrating treatments, and anti-pigmentation rituals.</p>
        """
    },
    {
        "slug": "makeup-tips-to-match-with-your-new-hairstyle",
        "title": "Refresh Your Look: 9 Makeup Tips to Match with your New Hairstyle",
        "category": "Makeup",
        "cat_slug": "makeup",
        "date": "August 12, 2023",
        "read_time": "4 min read",
        "desc": "How to harmonize your makeup with a new pixie cut, bob, long layers, or vibrant balayage color transformation.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner25.jpg",
        "content": """
        <p>A drastic haircut alters your facial focal points. Discover how adjusting your brow structure, eye contouring, and lip tones complements your new hairstyle.</p>
        """
    },
    {
        "slug": "best-hair-straightening-types-to-try",
        "title": "6 Best Hair Straightening Types To Try in 2024, Which is Best For You?",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "July 28, 2023",
        "read_time": "6 min read",
        "desc": "Rebonding vs Keratin vs Nanoplastia vs Botox: A stylist comparison of popular hair straightening and smoothing treatments in Kochi.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/05/poster1.jpg",
        "content": """
        <p>Permanent straightening rebonds sulfur links for pin-straight locks, while Keratin and Hair Botox smooth frizz without altering your natural curl structure permanently.</p>
        """
    },
    {
        "slug": "skin-care-tips-for-summer-in-india",
        "title": "7 Skin Care Tips for Summer in India",
        "category": "Skin Care",
        "cat_slug": "skin-care",
        "date": "July 14, 2023",
        "read_time": "5 min read",
        "desc": "Combat sweat, acne breakouts, and tanning with these 7 practical summer skincare guidelines from LivArt aestheticians.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner22.jpg",
        "content": """
        <p>Double-cleansing, cooling aloe gels, chemical exfoliation with salicylic acid, and avoiding heavy mineral oils keep skin pristine in intense Indian summers.</p>
        """
    },
    {
        "slug": "hair-colouring-tips-at-home",
        "title": "14 Tips To Take Care Of Your Colored Hair At Home",
        "category": "Hair",
        "cat_slug": "hair",
        "date": "June 29, 2023",
        "read_time": "6 min read",
        "desc": "14 expert stylist rules to protect hair color vibrancy, prevent brassiness, and retain moisture long after your salon appointment.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_offer-poster3_11-7-2023-1.jpg",
        "content": """
        <p>Maintain that rich salon color with purple toning shampoos, weekly deep conditioning masks, heat protection sprays, and UV filtering leave-in treatments.</p>
        """
    },
    {
        "slug": "professional-salon-makeup-vs-diy-bridal-makeup",
        "title": "Professional Salon Makeup vs DIY Bridal Makeup: Pros and Cons",
        "category": "Bridal",
        "cat_slug": "makeup",
        "date": "June 15, 2023",
        "read_time": "5 min read",
        "desc": "Why hiring a professional bridal artist guarantees stress-free wedding radiance, camera-proof longevity, and superior lighting response.",
        "img": "https://livartsalon.com/wp-content/uploads/2022/10/banner24.jpg",
        "content": """
        <p>Wedding day lighting, HD camera flash, and tear-filled moments demand professional waterproof formulations, precision color matching, and structural setting powders.</p>
        """
    },
    {
        "slug": "pre-wedding-skincare-tips-salon-treatments-for-a-bridal-glow-youll-love",
        "title": "Pre-Wedding Skincare Tips & Salon Treatments for a Bridal Glow You'll Love",
        "category": "Bridal",
        "cat_slug": "skin-care",
        "date": "May 30, 2023",
        "read_time": "6 min read",
        "desc": "Step-by-step bridal skincare plan: exfoliation, hydration, de-tan therapies, and why you should avoid new chemical peels right before the wedding.",
        "img": "https://livartsalon.com/wp-content/uploads/2023/07/livart-salon_offer-poster1_11-7-2023-1.jpg",
        "content": """
        <p>Achieving radiant bridal skin requires strategic timing. Discover which facials to book 4 weeks out and which gentle hydrating treatments to reserve for the wedding week.</p>
        """
    }
]

def build_blog_system():
    # 1. Main Blog Directory (/blog/)
    ensure_dir(os.path.join(BASE_DIR, "blog"))
    
    blog_cards_html = ""
    for post in BLOG_POSTS:
        blog_cards_html += f"""
        <article class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between" data-category="{post['cat_slug']}">
          <div class="h-48 overflow-hidden bg-obsidian-deep">
            <img src="{post['img']}" alt="{post['title']}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy" />
          </div>
          <div class="p-6 flex flex-col justify-between flex-grow">
            <div>
              <div class="flex items-center justify-between text-xs text-muted-slate mb-2">
                <span class="font-bold text-warm-bronze uppercase tracking-wider">{post['category']}</span>
                <span>{post['read_time']}</span>
              </div>
              <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2 hover:text-warm-bronze transition-colors">
                <a href="../{post['slug']}/index.html">{post['title']}</a>
              </h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-4">{post['desc']}</p>
            </div>
            <div class="pt-4 border-t border-black/5 flex items-center justify-between">
              <span class="text-[11px] text-muted-slate">{post['date']}</span>
              <a href="../{post['slug']}/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze flex items-center gap-1 uppercase tracking-wider">
                <span>Read</span> <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
              </a>
            </div>
          </div>
        </article>
        """

    html = render_head(
        title="LivArt Beauty Journal | Hair, Makeup & Skincare Insights Kochi",
        description="Read 32 comprehensive beauty, hair care, bridal makeup, and skincare guides curated by Stephy Sebastian and master stylists at LivArt Salon Kakkanad.",
        canonical_path="/blog/",
        root_prefix="../"
    )
    html += render_header(active_slug="blog", root_prefix="../")

    html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">
        The Atelier Journal • Kakkanad, Kochi
      </span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">
        LivArt Hair, Makeup & Skincare Journal
      </h1>
      <p class="text-base text-gray-300 max-w-2xl mx-auto leading-relaxed">
        Expert styling advice, product science, monsoon hair tips, and bridal beauty secrets curated by Stephy Sebastian and our master artists.
      </p>
    </div>
  </section>

  <!-- Filterable Category Links -->
  <section class="py-6 bg-surface-container border-b border-black/5">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap items-center justify-center gap-4 text-xs font-bold uppercase tracking-wider">
      <a href="index.html" class="px-4 py-2 rounded-full bg-obsidian-deep text-white">All Articles (32)</a>
      <a href="../category/hair/index.html" class="px-4 py-2 rounded-full bg-white text-obsidian-deep hover:bg-champagne-gold hover:text-white transition-all shadow-sm">Hair Styling & Care</a>
      <a href="../category/makeup/index.html" class="px-4 py-2 rounded-full bg-white text-obsidian-deep hover:bg-champagne-gold hover:text-white transition-all shadow-sm">Makeup & Bridal</a>
      <a href="../category/skin-care/index.html" class="px-4 py-2 rounded-full bg-white text-obsidian-deep hover:bg-champagne-gold hover:text-white transition-all shadow-sm">Skincare & Facials</a>
    </div>
  </section>

  <!-- Blog Articles Grid -->
  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {blog_cards_html}
      </div>
    </div>
  </section>
</main>
"""
    html += render_footer(root_prefix="../")
    with open(os.path.join(BASE_DIR, "blog", "index.html"), "w") as f:
        f.write(html)
    print("✓ blog/index.html built with all 32 articles")

    # 2. Individual 32 Blog Post Pages
    for post in BLOG_POSTS:
        post_dir = os.path.join(BASE_DIR, post["slug"])
        ensure_dir(post_dir)

        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": post["title"],
            "image": post["img"],
            "datePublished": "2024-05-01",
            "dateModified": "2026-09-17",
            "author": {
                "@type": "Person",
                "name": "Stephy Sebastian"
            },
            "publisher": {
                "@type": "Organization",
                "name": SITE_NAME,
                "logo": {
                    "@type": "ImageObject",
                    "url": LOGO_URL
                }
            },
            "description": post["desc"]
        }

        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE_URL + "/blog/"},
                {"@type": "ListItem", "position": 3, "name": post["title"], "item": f"{BASE_URL}/{post['slug']}/"}
            ]
        }

        post_html = render_head(
            title=f"{post['title']} | LivArt Salon Kakkanad",
            description=post["desc"],
            canonical_path=f"/{post['slug']}/",
            extra_schema=article_schema,
            root_prefix="../"
        )
        post_html += render_header(active_slug="blog", root_prefix="../")

        post_html += f"""
<main class="flex-grow">
  <!-- Breadcrumb -->
  <div class="bg-surface-container py-3 border-b border-black/5">
    <div class="max-w-[960px] mx-auto px-4 sm:px-6 lg:px-8 text-xs text-muted-slate flex items-center gap-2">
      <a href="../index.html" class="hover:text-obsidian-deep">Home</a>
      <span>/</span>
      <a href="../blog/index.html" class="hover:text-obsidian-deep">Blog</a>
      <span>/</span>
      <span class="text-obsidian-deep font-semibold truncate">{post['title']}</span>
    </div>
  </div>

  <!-- Article Header -->
  <article class="py-16 bg-surface-bright">
    <div class="max-w-[860px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-6">
        <span class="text-xs font-bold uppercase tracking-widest text-warm-bronze bg-champagne-gold/15 px-3 py-1 rounded-full">
          {post['category']}
        </span>
      </div>
      <h1 class="font-serif-luxury text-3xl sm:text-4xl lg:text-5xl font-bold text-obsidian-deep mb-4 leading-tight">
        {post['title']}
      </h1>
      
      <div class="flex items-center gap-4 text-xs text-muted-slate pb-6 mb-8 border-b border-black/10">
        <span>By <strong>Stephy Sebastian</strong></span>
        <span>•</span>
        <span>{post['date']}</span>
        <span>•</span>
        <span>{post['read_time']}</span>
      </div>

      <!-- Featured Image -->
      <div class="rounded-3xl overflow-hidden shadow-xl mb-10 max-h-[460px] bg-obsidian-deep">
        <img src="{post['img']}" alt="{post['title']}" class="w-full h-full object-cover" />
      </div>

      <!-- Content Body -->
      <div class="prose prose-lg max-w-none text-gray-800 leading-relaxed space-y-6">
        {post['content']}
        
        <p>
          Whether you are looking to revitalize tired hair, explore radiant bridal makeup, or pamper your skin with a clinical facial, the experienced stylists at <strong>LivArt Salon Kakkanad</strong> are here to assist. 
        </p>
      </div>

      <!-- Author Card & Booking CTA Box -->
      <div class="mt-12 p-8 bg-surface-container-low rounded-3xl border border-black/5 flex flex-col sm:flex-row items-center gap-6">
        <img src="https://livartsalon.com/wp-content/uploads/2024/02/Stephy-Sebastian.webp" alt="Stephy Sebastian" class="w-20 h-20 rounded-full object-cover shadow-md shrink-0" />
        <div class="text-center sm:text-left">
          <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze">Written by LivArt Founder</span>
          <h4 class="font-serif-luxury text-xl font-bold text-obsidian-deep">Stephy Sebastian</h4>
          <p class="text-xs text-gray-600 mt-1 leading-relaxed">
            Founder & Master Artist at LivArt Salon & Makeup Studio Kakkanad, and mentor at LivArt Academy.
          </p>
        </div>
      </div>

      <div class="mt-8 p-8 bg-gold-gradient rounded-3xl text-obsidian-deep flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl">
        <div>
          <h3 class="font-serif-luxury text-2xl font-bold mb-1">Experience the LivArt Difference</h3>
          <p class="text-xs text-black/80 font-medium">Book a personalized styling or facial session at our Kakkanad studio.</p>
        </div>
        <button data-open-booking class="bg-obsidian-deep hover:bg-obsidian-surface text-alabaster-cream px-6 py-3 rounded-lg text-xs font-bold uppercase tracking-widest transition-all shrink-0">
          Book Appointment
        </button>
      </div>
    </div>
  </article>
</main>
"""
        post_html += render_footer(root_prefix="../")

        with open(os.path.join(post_dir, "index.html"), "w") as f:
            f.write(post_html)

    print("✓ All 32 blog post pages generated")

# -------------------------------------------------------------
# 3. CATEGORY ARCHIVE PAGES
# -------------------------------------------------------------
def build_category_pages():
    categories = [
        {"slug": "hair", "name": "Hair Styling & Treatments", "desc": "Articles on haircuts, balayage, hair botox, keratin smoothing, and hair spa therapies."},
        {"slug": "makeup", "name": "Makeup & Bridal Artistry", "desc": "Bridal packages, HD airbrush techniques, and daily beauty essentials."},
        {"slug": "skin-care", "name": "Skincare & Facials", "desc": "Hydra facials, de-tan therapies, Cheryl's pro facials, and tropical summer skin tips."}
    ]

    for cat in categories:
        cat_dir = os.path.join(BASE_DIR, "category", cat["slug"])
        ensure_dir(cat_dir)

        matching_posts = [p for p in BLOG_POSTS if p["cat_slug"] == cat["slug"]]

        cards_html = ""
        for post in matching_posts:
            cards_html += f"""
            <article class="bg-surface-container-low rounded-2xl overflow-hidden border border-black/5 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
              <div class="h-48 overflow-hidden bg-obsidian-deep">
                <img src="{post['img']}" alt="{post['title']}" class="w-full h-full object-cover" loading="lazy" />
              </div>
              <div class="p-6 flex flex-col justify-between flex-grow">
                <div>
                  <span class="text-[10px] font-bold uppercase tracking-widest text-warm-bronze block mb-1">{post['category']}</span>
                  <h3 class="font-serif-luxury text-xl font-bold text-obsidian-deep mb-2">
                    <a href="../../{post['slug']}/index.html" class="hover:text-warm-bronze">{post['title']}</a>
                  </h3>
                  <p class="text-xs text-gray-600 mb-4">{post['desc']}</p>
                </div>
                <div class="pt-4 border-t border-black/5 flex items-center justify-between">
                  <span class="text-[11px] text-muted-slate">{post['date']}</span>
                  <a href="../../{post['slug']}/index.html" class="text-xs font-bold text-obsidian-deep hover:text-warm-bronze flex items-center gap-1 uppercase tracking-wider">
                    Read <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                  </a>
                </div>
              </div>
            </article>
            """

        html = render_head(
            title=f"{cat['name']} Archive | LivArt Salon Kakkanad",
            description=cat["desc"],
            canonical_path=f"/category/{cat['slug']}/",
            root_prefix="../../"
        )
        html += render_header(active_slug="blog", root_prefix="../../")

        html += f"""
<main class="flex-grow">
  <section class="bg-obsidian-deep text-alabaster-cream py-16">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="font-label-caps text-xs text-champagne-gold tracking-[0.25em] uppercase font-bold block mb-2">Category Archive</span>
      <h1 class="font-serif-luxury text-4xl sm:text-5xl font-bold text-alabaster-cream mb-4">{cat['name']}</h1>
      <p class="text-base text-gray-300 max-w-xl mx-auto leading-relaxed">{cat['desc']}</p>
    </div>
  </section>

  <section class="py-16 bg-surface-bright">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {cards_html}
      </div>
    </div>
  </section>
</main>
"""
        html += render_footer(root_prefix="../../")

        with open(os.path.join(cat_dir, "index.html"), "w") as f:
            f.write(html)

    print("✓ category/ archives built (hair, makeup, skin-care)")

# -------------------------------------------------------------
# 4. REDIRECTS, ROBOTS.TXT, AND SITEMAP.XML
# -------------------------------------------------------------
def build_seo_server_files():
    # 1. robots.txt
    robots_content = f"""User-agent: *
Allow: /
Disallow: /wp-admin/
Disallow: /wp-login.php
Disallow: /wp-includes/
Disallow: /aapaa/
Disallow: /lp_business_gift

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(BASE_DIR, "robots.txt"), "w") as f:
        f.write(robots_content)

    # 2. _redirects (Cloudflare Pages / Netlify format)
    redirects_content = """# 301 Permanent Redirects for Broken/Moved Links
/hair-works/* /hair-styling/ 301
/hair-works /hair-styling/ 301
/services/livart-hair-straightening /services/livart-hair-straightening/ 301
/services/loreal-glossy-hair-colouring /services/loreal-glossy-hair-colouring/ 301
/services/loreal-lustrous-hair-spa /services/loreal-lustrous-hair-spa/ 301
/services/livart-majestic-keratin-treatment /services/livart-majestic-keratin-treatment/ 301
/services/skin-miracle-hydra-facial /services/skin-miracle-hydra-facial/ 301

# 410 Gone for Russian/Ukrainian Gambling Spam & Injected Backdoors
/kto-vladelec-kosmolot-obzor-sobstvennikov-kompanii/* / 410
/kosmolot-kto-hozjain-informacija-o-sobstvennikah/* / 410
/kosmolot-licenzija-jak-kompanija-stala-pershim/* / 410
/kosmolot-ukraina-nadijnij-partner-derzhavi-v/* / 410
/kosmolot-v-ukraine-lider-igornoj-industrii/* / 410
/kosmolot-ua-pershij-licenzovanij-onlajn-operator/* / 410
/oprovergaem-mify-pochemu-kosmolot-razvod/* / 410
/kosmolot-ne-vyvodit-dengi-razveivaem-mif-o/* / 410
/kosmolot-reklama-unikalnij-pidhid-do-medijnih/* / 410
/chto-osobennogo-v-reklame-cosmolot-socialnaja/* / 410
/kosmolot-otzyvy-sotrudnikov-razvitie-it-sektora-i/* / 410
/aapaa/* / 410
/lp_business_gift* / 410
"""
    with open(os.path.join(BASE_DIR, "_redirects"), "w") as f:
        f.write(redirects_content)

    # 3. .htaccess (Apache format)
    htaccess_content = """# LivArt Salon — Clean Redirection & Security Rules
RewriteEngine On

# Redirect /hair-works/ to /hair-styling/
RewriteRule ^hair-works/?$ /hair-styling/ [R=301,L]

# Return 410 Gone for known malicious spam URLs
RewriteRule ^kto-vladelec-kosmolot.*$ - [G,L]
RewriteRule ^kosmolot.*$ - [G,L]
RewriteRule ^oprovergaem-mify.*$ - [G,L]
RewriteRule ^chto-osobennogo.*$ - [G,L]
RewriteRule ^aapaa.*$ - [G,L]
RewriteRule ^lp_business_gift.*$ - [G,L]

# Security Headers
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set X-XSS-Protection "1; mode=block"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""
    with open(os.path.join(BASE_DIR, ".htaccess"), "w") as f:
        f.write(htaccess_content)

    # 4. sitemap.xml
    all_urls = [
        ("/", "1.0"),
        ("/services/", "0.9"),
        ("/services/loreal-lustrous-hair-spa/", "0.9"),
        ("/services/livart-majestic-keratin-treatment/", "0.8"),
        ("/services/livart-hair-straightening/", "0.8"),
        ("/services/loreal-glossy-hair-colouring/", "0.8"),
        ("/services/skin-miracle-hydra-facial/", "0.8"),
        ("/hair-styling/", "0.8"),
        ("/make-up/", "0.8"),
        ("/skin-care/", "0.8"),
        ("/packages/", "0.8"),
        ("/gallery/", "0.8"),
        ("/about-us/", "0.8"),
        ("/teams/", "0.7"),
        ("/contact-us/", "0.8"),
        ("/blog/", "0.8"),
        ("/category/hair/", "0.7"),
        ("/category/makeup/", "0.7"),
        ("/category/skin-care/", "0.7")
    ]

    for p in BLOG_POSTS:
        all_urls.append((f"/{p['slug']}/", "0.7"))

    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for path, prio in all_urls:
        sitemap_xml += f"""  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>2026-09-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{prio}</priority>
  </url>
"""
    sitemap_xml += "</urlset>\n"

    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w") as f:
        f.write(sitemap_xml)

    print("✓ robots.txt, _redirects, .htaccess, and sitemap.xml built")

if __name__ == "__main__":
    build_blog_system()
    build_category_pages()
    build_seo_server_files()
