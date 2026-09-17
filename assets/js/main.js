/**
 * LivArt Salon & Make-Up Studio — Core Client Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initBookingModal();
  initServiceFilter();
  initStickyHeader();
  initHeroSlideshow();
});

// Mobile Navigation Toggle
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-btn');
  const closeBtn = document.getElementById('mobile-menu-close');
  const drawer = document.getElementById('mobile-drawer');
  const backdrop = document.getElementById('mobile-backdrop');

  if (!toggleBtn || !drawer) return;

  function openMenu() {
    drawer.classList.remove('translate-x-full');
    backdrop.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    drawer.classList.add('translate-x-full');
    backdrop.classList.add('hidden');
    document.body.style.overflow = '';
  }

  toggleBtn.addEventListener('click', openMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  if (backdrop) backdrop.addEventListener('click', closeMenu);

  // Close when clicking any nav link in drawer
  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}

// Sticky Header Blur Enhancement
function initStickyHeader() {
  const header = document.querySelector('header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('shadow-lg', 'bg-surface/95');
    } else {
      header.classList.remove('shadow-lg');
    }
  });
}

// Service Filter Tabs (Interactive)
function initServiceFilter() {
  const tabs = document.querySelectorAll('.service-tab-btn');
  const items = document.querySelectorAll('.service-item');

  if (!tabs.length || !items.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const category = tab.getAttribute('data-category');

      // Update active button state
      tabs.forEach(t => {
        t.classList.remove('bg-obsidian-deep', 'text-alabaster-cream');
        t.classList.add('bg-surface-container', 'text-on-surface');
      });
      tab.classList.add('bg-obsidian-deep', 'text-alabaster-cream');
      tab.classList.remove('bg-surface-container', 'text-on-surface');

      // Filter service cards
      items.forEach(item => {
        const itemCat = item.getAttribute('data-cat');
        if (category === 'all' || itemCat === category) {
          item.classList.remove('hidden');
          item.classList.add('flex');
        } else {
          item.classList.remove('flex');
          item.classList.add('hidden');
        }
      });
    });
  });
}

// Booking Modal & WhatsApp Concierge
function initBookingModal() {
  const modal = document.getElementById('booking-modal');
  const modalTriggers = document.querySelectorAll('[data-open-booking]');
  const modalClose = document.getElementById('booking-modal-close');
  const form = document.getElementById('reservation-form');
  const dateInput = document.getElementById('book-date');

  // Set minimum date to today
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
    dateInput.value = today;
  }

  window.openBookingModal = function(servicePreselect = '') {
    if (!modal) return;
    if (servicePreselect) {
      const select = document.getElementById('book-service');
      if (select) {
        for (let opt of select.options) {
          if (opt.value === servicePreselect || opt.text.toLowerCase().includes(servicePreselect.toLowerCase())) {
            opt.selected = true;
            break;
          }
        }
      }
    }
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  };

  window.closeBookingModal = function() {
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  };

  modalTriggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const service = btn.getAttribute('data-service') || '';
      window.openBookingModal(service);
    });
  });

  if (modalClose) modalClose.addEventListener('click', window.closeBookingModal);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) window.closeBookingModal();
    });
  }

  // Handle Form Submission (WhatsApp Integration)
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('book-name')?.value || '';
      const phone = document.getElementById('book-phone')?.value || '';
      const service = document.getElementById('book-service')?.value || '';
      const date = document.getElementById('book-date')?.value || '';
      const time = document.getElementById('book-time')?.value || '';
      const notes = document.getElementById('book-notes')?.value || '';

      const confirmation = document.getElementById('booking-confirmation-msg');
      if (confirmation) {
        confirmation.classList.remove('hidden');
      }

      // Differentiate Salon Services vs Academy Courses
      const isAcademy = service.toLowerCase().includes('academy') || service.toLowerCase().includes('course');
      const targetPhone = isAcademy ? '919633211151' : '917012059591';
      const greeting = isAcademy ? 'Hello LivArt Beauty Academy Kakkanad!' : 'Hello LivArt Salon & Makeup Studio Kakkanad!';

      // Build WhatsApp message
      const msg = [
        greeting,
        "",
        isAcademy ? "I would like to inquire about course admissions:" : "I would like to reserve an appointment:",
        `• Name: ${name}`,
        `• Phone: ${phone}`,
        `• Inquiring For: ${service}`,
        `• Preferred Date: ${date}`,
        `• Preferred Time: ${time}`,
        notes ? `• Special Notes: ${notes}` : "",
        "",
        isAcademy ? "Please share course fees, syllabus, and upcoming batch details. Thank you!" : "Please confirm my appointment slot. Thank you!"
      ].filter(line => line !== null).join("\n");

      const waUrl = `https://wa.me/${targetPhone}?text=${encodeURIComponent(msg)}`;

      setTimeout(() => {
        window.open(waUrl, '_blank');
      }, 600);
    });
  }
}

// Hero Visual Showcase Slideshow
function initHeroSlideshow() {
  const container = document.getElementById('hero-showcase-container');
  if (!container) return;

  const slides = container.querySelectorAll('.hero-slide');
  const dots = container.querySelectorAll('.hero-dot');
  const prevBtn = document.getElementById('hero-slide-prev');
  const nextBtn = document.getElementById('hero-slide-next');
  const tagEl = document.getElementById('hero-slider-tag');
  const titleEl = document.getElementById('hero-slider-title');
  const counterEl = document.getElementById('hero-slider-counter');

  if (!slides.length) return;

  let currentIndex = 0;
  let timer = null;
  const slideCount = slides.length;
  const intervalTime = 3800;

  function showSlide(index) {
    if (index < 0) index = slideCount - 1;
    if (index >= slideCount) index = 0;
    currentIndex = index;

    slides.forEach((s, idx) => {
      if (idx === currentIndex) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    dots.forEach((d, idx) => {
      if (idx === currentIndex) {
        d.classList.add('bg-champagne-gold', 'w-4');
        d.classList.remove('bg-white/40', 'w-2');
      } else {
        d.classList.remove('bg-champagne-gold', 'w-4');
        d.classList.add('bg-white/40', 'w-2');
      }
    });

    const activeSlide = slides[currentIndex];
    if (activeSlide) {
      const tag = activeSlide.getAttribute('data-tag') || 'Kakkanad Sanctuary';
      const title = activeSlide.getAttribute('data-title') || 'Seaport-Airport Atelier';

      if (tagEl) {
        tagEl.style.opacity = '0';
        setTimeout(() => {
          tagEl.textContent = tag;
          tagEl.style.opacity = '1';
        }, 150);
      }
      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(() => {
          titleEl.textContent = title;
          titleEl.style.opacity = '1';
        }, 150);
      }
      if (counterEl) {
        counterEl.textContent = `${currentIndex + 1}/${slideCount}`;
      }
    }
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  function prevSlide() {
    showSlide(currentIndex - 1);
  }

  function startAutoPlay() {
    stopAutoPlay();
    timer = setInterval(nextSlide, intervalTime);
  }

  function stopAutoPlay() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  // Navigation Event Listeners
  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      nextSlide();
      startAutoPlay();
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      prevSlide();
      startAutoPlay();
    });
  }

  dots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      e.stopPropagation();
      const idx = parseInt(dot.getAttribute('data-index'), 10);
      if (!isNaN(idx)) {
        showSlide(idx);
        startAutoPlay();
      }
    });
  });

  // Pause on hover
  container.addEventListener('mouseenter', stopAutoPlay);
  container.addEventListener('mouseleave', startAutoPlay);

  // Touch Swipe Support for Mobile
  let touchStartX = 0;
  let touchEndX = 0;

  container.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    stopAutoPlay();
  }, { passive: true });

  container.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
    startAutoPlay();
  }, { passive: true });

  // Initial Autoplay start
  startAutoPlay();
}
