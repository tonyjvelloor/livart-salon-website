/**
 * LivArt Salon & Make-Up Studio — Core Client Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initBookingModal();
  initServiceFilter();
  initStickyHeader();
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

      // Build WhatsApp message
      const msg = [
        "Hello LivArt Salon & Makeup Studio Kakkanad!",
        "",
        "I would like to reserve an appointment:",
        `• Name: ${name}`,
        `• Phone: ${phone}`,
        `• Service / Package: ${service}`,
        `• Preferred Date: ${date}`,
        `• Preferred Time: ${time}`,
        notes ? `• Special Notes: ${notes}` : "",
        "",
        "Please confirm my appointment slot. Thank you!"
      ].filter(line => line !== null).join("\n");

      const waUrl = `https://wa.me/917012059591?text=${encodeURIComponent(msg)}`;

      setTimeout(() => {
        window.open(waUrl, '_blank');
      }, 600);
    });
  }
}
