/**
 * SnackPie Website - Main JavaScript
 * Shared utilities and navigation functions
 */

// Mobile menu toggle
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  const btn = document.querySelector('.nav-menu-btn');
  const isOpen = menu.classList.contains('open');
  
  menu.classList.toggle('open');
  btn.setAttribute('aria-expanded', !isOpen);
  
  // Prevent body scroll when menu is open
  document.body.style.overflow = isOpen ? '' : 'hidden';
}

// Close mobile menu on link click
document.querySelectorAll('.nav-mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    toggleMobileMenu();
  });
});

// Close mobile menu on escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const menu = document.getElementById('mobileMenu');
    if (menu && menu.classList.contains('open')) {
      toggleMobileMenu();
    }
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#') {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
});

// Intersection Observer for scroll animations
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  
  document.querySelectorAll('.card, .feature-card').forEach(el => {
    observer.observe(el);
  });
}

// Copy to clipboard utility
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    // Fallback for older browsers
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand('copy');
      return true;
    } catch {
      return false;
    } finally {
      document.body.removeChild(textarea);
    }
  }
}

// LocalStorage helpers
const Storage = {
  get(key) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : null;
    } catch {
      return null;
    }
  },
  
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Storage full or unavailable
    }
  },
  
  remove(key) {
    try {
      localStorage.removeItem(key);
    } catch {
      // Ignore
    }
  }
};

// Debounce utility
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Export for use in other scripts
window.SnackPie = {
  toggleMobileMenu,
  copyToClipboard,
  Storage,
  debounce
};