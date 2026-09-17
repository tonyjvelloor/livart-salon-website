import subprocess
import re
import os
import time
import json

REELS_DATA = [
    # Celebrity Visits (21)
    {"code": "Db7rJBtuj4B", "title": "Amala Shaji Blow Dry Transformation", "category": "celebrity", "handle": "@amalashaji", "badge": "Influencer Spotlight", "service": "Permanent Blow Dry & Styling"},
    {"code": "DbLJRauyFro", "title": "Azmin Yasar Styled at Salon", "category": "celebrity", "handle": "@azmin_yasar", "badge": "Hair Styling", "service": "Hair Styling & Texture"},
    {"code": "DZkDGP8N7ei", "title": "Rithu Manthra Styled at Salon", "category": "celebrity", "handle": "@rithumanthra_", "badge": "Model & Actress", "service": "Haute Couture Hair & Makeup"},
    {"code": "DYv8wyxMjAl", "title": "Madona Tixeira - IPL Anchor Hairstyle", "category": "celebrity", "handle": "@madonnatixy", "badge": "IPL Anchor", "service": "Runway Blow Dry & Styling"},
    {"code": "DW1NAndDGuP", "title": "Actress Amala Rose Kurian Review - Hair Botox", "category": "celebrity", "handle": "@amala_rose_kurian", "badge": "Hair Botox", "service": "Hair Botox Treatment (Rs. 5999)"},
    {"code": "DOajrjXkqH_", "title": "Client Madona Tixeira Thank-You", "category": "celebrity", "handle": "@madonnatixy", "badge": "Client Love", "service": "Salon Styling Experience"},
    {"code": "DIYwMqNSFPo", "title": "Poomaram Actress Sangeetha at Salon", "category": "celebrity", "handle": "Actress Sangeetha", "badge": "Film Star", "service": "Personalized Beauty Ritual"},
    {"code": "DEXOFvGTyDZ", "title": "Actress Amala Rose Kurian Salon Session", "category": "celebrity", "handle": "@amala_rose_kurian", "badge": "Couture Styling", "service": "Hair Styling & Hair Spa"},
    {"code": "DD09-1GTd2F", "title": "Anchor Meenakshi Sudheer Makeover", "category": "celebrity", "handle": "Meenakshi Sudheer", "badge": "TV Anchor", "service": "Camera-Ready Glamour Makeover"},
    {"code": "DDYbKpnTbKk", "title": "Makeover for Madona Tixeira", "category": "celebrity", "handle": "@madonnatixy", "badge": "Anchor Makeover", "service": "Hair Styling & Makeup"},
    {"code": "DABMk4mtv8b", "title": "RJ Soorya Hair Colouring Artistry", "category": "celebrity", "handle": "RJ Soorya", "badge": "RJ Glam", "service": "L'Oreal Glossy Hair Colouring"},
    {"code": "C_hxrh3y5NY", "title": "RJ Surya Festive Onam Look", "category": "celebrity", "handle": "RJ Surya", "badge": "Onam Glam", "service": "Festive Saree Draping & Makeup"},
    {"code": "C88tG9iSEKp", "title": "Anchor Meenakshi Sudheer Detox Pedicure", "category": "celebrity", "handle": "Meenakshi Sudheer", "badge": "Foot Spa", "service": "Deluxe Pedicure Spa"},
    {"code": "C7l9fP5P3u9", "title": "News Anchor Shiju Abdul Rasheed Haircut", "category": "celebrity", "handle": "Shiju Abdul Rasheed", "badge": "News Anchor", "service": "Precision Haircut & Grooming"},
    {"code": "C6F_GKgtlHk", "title": "Client RJ Bincy Compliment & Styling", "category": "celebrity", "handle": "RJ Bincy", "badge": "Radio Host", "service": "Signature Blowout & Finish"},
    {"code": "C5pwjmOidQU", "title": "RJ Bincy Hair Transformation Makeover", "category": "celebrity", "handle": "RJ Bincy", "badge": "Hair Makeover", "service": "Keratin Infusion Therapy"},
    {"code": "C4VCBeStpUM", "title": "Ms. Ajmi 'Icon of the Year' Styling", "category": "celebrity", "handle": "Ms. Ajmi", "badge": "Award Winner", "service": "Red Carpet Hair & Glow"},
    {"code": "Cujo9fqpEsB", "title": "Actress Suvarna Menon Hair Botox Review", "category": "celebrity", "handle": "@iamsuvarnamenon", "badge": "Actress Review", "service": "Hair Botox Nourishment"},
    {"code": "CsQ-ptyuuv-", "title": "Actress Shivani Menon Makeover (99K Viral)", "category": "celebrity", "handle": "@shivanimenon", "badge": "99K Viral Hit", "service": "Celebrity Hair Transformation"},
    {"code": "CrAzwEnJ8FV", "title": "RJ Soorya Traditional Vishu Makeover", "category": "celebrity", "handle": "RJ Soorya", "badge": "Vishu Festive", "service": "Traditional Kerala Aesthetics"},
    {"code": "CpsA0o_OSo5", "title": "Model Shaluz Boon Hair Styling (13K Viral)", "category": "celebrity", "handle": "@shaluz_boon", "badge": "13K Viral Hit", "service": "Glamour Styling & Waves"},

    # Bridal Works (27)
    {"code": "DdOmdkItPmF", "title": "Bridal Transformation & Special Offer Showcase", "category": "bridal", "badge": "Bridal Offer", "service": "Bridal Couture Package"},
    {"code": "Da8Hb68SA5B", "title": "LivArt Academy Student Bride Makeover", "category": "bridal", "badge": "Academy Bride", "service": "Professional Bridal Artistry"},
    {"code": "DZSWz8wyz5i", "title": "Hindu Bride Soft Radiant Glamour", "category": "bridal", "badge": "Hindu Bride", "service": "Traditional Muhurtham Makeup"},
    {"code": "DYuASLuK_le", "title": "Christian Bridal Grace & Veil Setting", "category": "bridal", "badge": "Christian Bride", "service": "Christian Bridal Couture"},
    {"code": "DYFFX0RKhnx", "title": "Wedding Reception Glamour for Deepika", "category": "bridal", "badge": "Reception Glam", "service": "High-Definition Bridal Glow"},
    {"code": "DX6qGl_SKf1", "title": "Evening Reception Couture Glam", "category": "bridal", "badge": "Reception Look", "service": "Evening Reception Makeup"},
    {"code": "DXb3cLlEsmy", "title": "Groom Contemporary Styling & Makeup", "category": "bridal", "badge": "Groom Glamour", "service": "Groom Black Diamond Package"},
    {"code": "DWtk05cjLnI", "title": "Modern Bridal Reception Glam", "category": "bridal", "badge": "Reception Chic", "service": "Airbrush Bridal Finish"},
    {"code": "DVyTy0qDJEN", "title": "Bridal Look Recreation Journey", "category": "bridal", "badge": "Bridal Story", "service": "Custom Bridal Styling"},
    {"code": "DUap-mOkvuu", "title": "Pre-Wedding HD Bridal Makeover", "category": "bridal", "badge": "Pre-Wedding", "service": "HD Pre-Wedding Glamour"},
    {"code": "DULWym5CHa0", "title": "Traditional Hindu Bridal Makeover Complete", "category": "bridal", "badge": "Complete Bridal", "service": "Muhurtham Saree & Temple Makeup"},
    {"code": "DT7y-uAkh47", "title": "Regal Bridal Look with Designer Lehenga", "category": "bridal", "badge": "Lehenga Bride", "service": "Royal Lehenga Bridal Makeover"},
    {"code": "DTu8FlyknZz", "title": "Christian Bridal Makeover - Two Signature Looks", "category": "bridal", "badge": "Dual Bridal Look", "service": "Bridal Church & Reception Styling"},
    {"code": "DTc2O2fCFZI", "title": "Muslim Bride Nikah & Manavatti Elegance", "category": "bridal", "badge": "Muslim Bride", "service": "Nikah Glamour & Hijab Styling"},
    {"code": "DSpYR2dCJ5-", "title": "Christian Bridal Transformation & Hair Veil", "category": "bridal", "badge": "Christian Bride", "service": "Bespoke Bridal Package"},
    {"code": "DSNGmIaEp4d", "title": "Bride Natural Glowing Skin Minimal Look", "category": "bridal", "badge": "Minimalist Bride", "service": "Natural Dewy Bridal Finish"},
    {"code": "DRXFRQCEgpm", "title": "Glass Skin Bridal Makeup Artistry", "category": "bridal", "badge": "Glass Skin Bride", "service": "Ultra-Hydrating Bridal Makeup"},
    {"code": "DQ1XHMIjLJ8", "title": "Engagement Makeover & Personal Story", "category": "bridal", "badge": "Engagement", "service": "Engagement Diamond Glow"},
    {"code": "DQMWOO5jNhc", "title": "Bride Alka Engagement Radiance", "category": "bridal", "badge": "Bride Alka", "service": "Signature Engagement Makeover"},
    {"code": "DMDB3b4Nm0p", "title": "Radiant Bridal Makeup Glow & Florals", "category": "bridal", "badge": "Radiant Glow", "service": "Floral Bridal Hair & Makeup"},
    {"code": "DK13xiot6zA", "title": "Full Bridal Transformation at LivArt Studio", "category": "bridal", "badge": "Transformation", "service": "Bridal Gold Package"},
    {"code": "DJrQLH3Tk0n", "title": "Bridal & Party Hairstyle Volume Artistry", "category": "bridal", "badge": "Hairstyle Volume", "service": "Haute Couture Hair Sculpting"},
    {"code": "DIoW2P5TF7G", "title": "Bespoke Bride Trial Makeup Session", "category": "bridal", "badge": "Trial Session", "service": "Pre-Bridal Consultation & Trial"},
    {"code": "DIED9XjSKku", "title": "Bridal Beauty at its Finest - Kakkanad", "category": "bridal", "badge": "Finest Bridal", "service": "Bridal Silver/Gold Package"},
    {"code": "DGVbSkPSXIi", "title": "Exquisite Bridal Makeup & Jewelry Setting", "category": "bridal", "badge": "Jewelry Setting", "service": "Traditional South Indian Bridal"},
    {"code": "DC9Ou8ETksn", "title": "Essential Bridal Hair Tip for To-Be Brides", "category": "bridal", "badge": "Stylist Tips", "service": "Bridal Hair Health Therapy"},
    {"code": "C7CYp17t9yd", "title": "Christian Bride Niby Katherine Spotlight", "category": "bridal", "badge": "Real Bride Niby", "service": "Christian Bridal Couture"}
]

OUT_DIR = "assets/images/instagram"
os.makedirs(OUT_DIR, exist_ok=True)

success_count = 0
failed = []

for idx, item in enumerate(REELS_DATA, 1):
    code = item["code"]
    target_path = os.path.join(OUT_DIR, f"{code}.jpg")
    item["url"] = f"https://www.instagram.com/livart_salon/reel/{code}/"
    item["local_img"] = target_path
    
    if os.path.exists(target_path) and os.path.getsize(target_path) > 10000:
        print(f"[{idx}/{len(REELS_DATA)}] Already downloaded: {code} ({os.path.getsize(target_path)} bytes)")
        success_count += 1
        continue

    print(f"[{idx}/{len(REELS_DATA)}] Fetching embed for {code}...")
    embed_url = f"https://www.instagram.com/reel/{code}/embed/"
    res = subprocess.run(["curl", "-sL", embed_url], capture_output=True, text=True)
    html = res.stdout
    
    img_url = None
    m_srcset = re.search(r"srcset=\"([^\"]+)\"", html)
    if m_srcset:
        candidates = []
        for part in m_srcset.group(1).split(","):
            part = part.strip()
            if not part: continue
            tokens = part.split(" ")
            u = tokens[0].replace("&amp;", "&")
            w = int(tokens[1].replace("w", "")) if len(tokens) > 1 and tokens[1].endswith("w") and tokens[1][:-1].isdigit() else 0
            candidates.append((w, u))
        if candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            img_url = candidates[0][1]

    if not img_url:
        m_img = re.search(r"class=\"EmbeddedMediaImage\"[^>]*src=\"([^\"]+)\"", html)
        if not m_img:
            m_img = re.search(r"src=\"([^\"]+)\"[^>]*class=\"EmbeddedMediaImage\"", html)
        if m_img:
            img_url = m_img.group(1).replace("&amp;", "&")

    if not img_url:
        all_fb = re.findall(r"https://[^\" \t\n\r<>]*(?:cdninstagram|fbcdn)[^\" \t\n\r<>]*", html)
        if all_fb:
            img_url = all_fb[0].replace("&amp;", "&")

    if img_url:
        dl = subprocess.run(["curl", "-sL", img_url, "-o", target_path])
        if os.path.exists(target_path) and os.path.getsize(target_path) > 10000:
            print(f"  ✓ Successfully downloaded {code}.jpg ({os.path.getsize(target_path)} bytes)")
            success_count += 1
        else:
            print(f"  ✗ Failed downloading image for {code}")
            failed.append(code)
    else:
        print(f"  ✗ No image URL found in embed HTML for {code}")
        failed.append(code)

    time.sleep(0.3)

with open(os.path.join(OUT_DIR, "reels_metadata.json"), "w") as f:
    json.dump(REELS_DATA, f, indent=2)

print("="*50)
print(f"DOWNLOAD COMPLETE: {success_count}/{len(REELS_DATA)} images successfully downloaded.")
if failed:
    print(f"Failed codes ({len(failed)}):", failed)
else:
    print("ALL 48 ORIGINAL INSTAGRAM IMAGES SAVED LOCALLY!")
