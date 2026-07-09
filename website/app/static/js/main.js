/**
 * SnackPie Website - Main JavaScript
 * Shared utilities and navigation functions
 */

// Mobile menu toggle
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  const backdrop = document.getElementById('mobileMenuBackdrop');
  const btn = document.getElementById('navMenuBtn');
  const isOpen = menu.classList.contains('open');
  
  menu.classList.toggle('open');
  if (backdrop) backdrop.classList.toggle('open');
  if (btn) btn.setAttribute('aria-expanded', String(!isOpen));
  
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

// Nav reacts to scroll position and visible page section
const nav = document.querySelector('.nav');
const navLinks = Array.from(document.querySelectorAll('.nav-link'));
const sections = Array.from(document.querySelectorAll('main section[id], main article[id]'));

function updateNavOnScroll() {
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 12);
}

updateNavOnScroll();
window.addEventListener('scroll', updateNavOnScroll, { passive: true });

if (sections.length > 0) {
  const sectionObserver = new IntersectionObserver((entries) => {
    const visible = entries
      .filter(entry => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) return;
    const id = visible.target.id;
    document.querySelectorAll('.docs-toc-link').forEach(link => {
      link.classList.toggle('section-active', link.getAttribute('href') === `#${id}`);
    });
  }, { rootMargin: '-25% 0px -55% 0px', threshold: [0.1, 0.4, 0.7] });

  sections.forEach(section => sectionObserver.observe(section));
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

// Theme toggle (light/dark), persisted to localStorage
function getStoredTheme() {
  try { return localStorage.getItem('snackpie-theme'); } catch { return null; }
}

function applyTheme(theme) {
  if (theme === 'dark' || theme === 'light') {
    document.documentElement.setAttribute('data-theme', theme);
  }

  const activeTheme = theme === 'dark' ? 'dark' : 'light';
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.setAttribute('aria-pressed', activeTheme === 'dark' ? 'true' : 'false');
    btn.setAttribute('aria-label', activeTheme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
  }

  const metaTheme = document.querySelector('meta[name="theme-color"]');
  if (metaTheme) metaTheme.setAttribute('content', activeTheme === 'dark' ? '#293681' : '#D0E7E6');
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  const next = current === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try { localStorage.setItem('snackpie-theme', next); } catch {}
}

// Sync toggle state on load
document.addEventListener('DOMContentLoaded', () => {
  const stored = getStoredTheme();
  const theme = stored || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyTheme(theme);
});

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
  if (!getStoredTheme()) applyTheme(event.matches ? 'dark' : 'light');
});

window.addEventListener('load', () => {
  const loadingScreen = document.getElementById('loadingScreen');
  if (!loadingScreen) return;
  setTimeout(() => loadingScreen.classList.add('hidden'), 450);
  setTimeout(() => loadingScreen.remove(), 900);
});

// Export for use in other scripts
window.SnackPie = {
  toggleMobileMenu,
  copyToClipboard,
  Storage,
  debounce,
  toggleTheme,
  applyTheme
};
