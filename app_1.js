// Portfolio Website JavaScript

// DOM Elements
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');
const navLinks = document.querySelectorAll('.nav__link');
const header = document.getElementById('header');
const sections = document.querySelectorAll('section[id]');
const contactForm = document.getElementById('contact-form');

// Mobile Navigation Functions
function showMenu() {
    if (navMenu) {
        navMenu.classList.add('show-menu');
        document.body.style.overflow = 'hidden';
    }
}

function hideMenu() {
    if (navMenu) {
        navMenu.classList.remove('show-menu');
        document.body.style.overflow = 'auto';
    }
}

// Initialize mobile navigation after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation event listeners
    const toggle = document.getElementById('nav-toggle');
    const close = document.getElementById('nav-close');
    const menu = document.getElementById('nav-menu');
    
    if (toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            showMenu();
        });
    }
    
    if (close) {
        close.addEventListener('click', function(e) {
            e.preventDefault();
            hideMenu();
        });
    }
    
    // Close menu when clicking on nav links
    const allNavLinks = document.querySelectorAll('.nav__link');
    allNavLinks.forEach(link => {
        link.addEventListener('click', function() {
            hideMenu();
        });
    });
    
    // Close menu when clicking outside
    if (menu) {
        menu.addEventListener('click', function(e) {
            if (e.target === menu) {
                hideMenu();
            }
        });
    }
});

// Header scroll effect
function scrollHeader() {
    if (header) {
        if (window.scrollY >= 50) {
            header.classList.add('scroll-header');
        } else {
            header.classList.remove('scroll-header');
        }
    }
}

window.addEventListener('scroll', scrollHeader);

// Active section highlighting
function scrollActive() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 200;
        const sectionId = current.getAttribute('id');
        const sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']');

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            if (sectionsClass) {
                sectionsClass.classList.add('active-link');
            }
        } else {
            if (sectionsClass) {
                sectionsClass.classList.remove('active-link');
            }
        }
    });
}

window.addEventListener('scroll', scrollActive);

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                const headerHeight = header ? header.offsetHeight : 70;
                const targetPosition = target.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            
            // Animate skill bars when skills section is visible
            if (entry.target.classList.contains('skills')) {
                animateSkillBars();
            }
            
            // Animate stats when about section is visible
            if (entry.target.classList.contains('about')) {
                animateStats();
            }
        }
    });
}, observerOptions);

// Skill bar animation
function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skill__progress');
    
    skillBars.forEach(bar => {
        const skillLevel = bar.getAttribute('data-skill');
        setTimeout(() => {
            bar.style.width = skillLevel + '%';
        }, 200);
    });
}

// Stats counter animation
function animateStats() {
    const stats = document.querySelectorAll('.stat__number');
    
    stats.forEach(stat => {
        const target = stat.textContent;
        const isPercentage = target.includes('%');
        const isPlus = target.includes('+');
        let numericTarget = parseInt(target.replace(/[^\d]/g, ''));
        
        if (isNaN(numericTarget)) return;
        
        let current = 0;
        const increment = numericTarget / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= numericTarget) {
                current = numericTarget;
                clearInterval(timer);
            }
            
            let displayValue = Math.floor(current);
            if (isPlus) displayValue += '+';
            if (isPercentage) displayValue += '%';
            
            stat.textContent = displayValue;
        }, 30);
    });
}

// Typing animation for hero text
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing animation when page loads
window.addEventListener('load', () => {
    const heroTitle = document.querySelector('.hero__title');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        typeWriter(heroTitle, originalText, 80);
    }
});

// Parallax effect for hero particles
function parallaxEffect() {
    const scrolled = window.pageYOffset;
    const particles = document.querySelector('.hero__particles');
    
    if (particles) {
        particles.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
}

window.addEventListener('scroll', parallaxEffect);

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button class="notification__close">&times;</button>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        padding: 16px 24px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 10000;
        transform: translateX(400px);
        transition: transform 0.3s ease;
        max-width: 400px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        font-family: var(--font-family-base, sans-serif);
    `;
    
    // Set background color based on type
    switch(type) {
        case 'success':
            notification.style.backgroundColor = '#10B981';
            break;
        case 'error':
            notification.style.backgroundColor = '#EF4444';
            break;
        case 'warning':
            notification.style.backgroundColor = '#F59E0B';
            break;
        default:
            notification.style.backgroundColor = '#3B82F6';
    }
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button functionality
    const closeButton = notification.querySelector('.notification__close');
    closeButton.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 0;
        margin: 0;
        line-height: 1;
    `;
    
    closeButton.addEventListener('click', () => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => notification.remove(), 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.style.transform = 'translateX(400px)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Contact form handling - Initialize after DOM loads
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(form);
            const name = formData.get('name');
            const email = formData.get('email');
            const message = formData.get('message');
            
            // Basic validation
            if (!name || !email || !message) {
                showNotification('Please fill in all fields.', 'error');
                return;
            }
            
            if (!isValidEmail(email)) {
                showNotification('Please enter a valid email address.', 'error');
                return;
            }
            
            // Simulate form submission
            const submitButton = form.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;
            
            setTimeout(() => {
                showNotification('Thank you for your message! I\'ll get back to you soon.', 'success');
                form.reset();
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }, 2000);
        });
    }
});

// Timeline animation on scroll
function animateTimeline() {
    const timelineItems = document.querySelectorAll('.timeline__item');
    
    timelineItems.forEach((item, index) => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 200);
                }
            });
        }, { threshold: 0.5 });
        
        // Initial state
        item.style.opacity = '0';
        item.style.transform = 'translateY(30px)';
        item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        observer.observe(item);
    });
}

// Card hover effects
function initCardEffects() {
    const cards = document.querySelectorAll('.service__card, .project__card, .certification__card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Initialize all animations and effects
document.addEventListener('DOMContentLoaded', function() {
    // Add loading class to body initially
    document.body.classList.add('loading');
    
    // Observe all sections and cards for animations
    document.querySelectorAll('section, .service__card, .project__card, .certification__card, .timeline__item').forEach(el => {
        el.classList.add('animate-in');
        observer.observe(el);
    });
    
    // Remove loading class after page load
    window.addEventListener('load', () => {
        document.body.classList.remove('loading');
        animateTimeline();
        initCardEffects();
    });
    
    // Add smooth transitions to all elements
    const style = document.createElement('style');
    style.textContent = `
        .loading * {
            transition: none !important;
        }
        
        .notification {
            font-family: var(--font-family-base);
        }
        
        @media (max-width: 768px) {
            .notification {
                right: 10px;
                left: 10px;
                max-width: none;
                transform: translateX(0) translateY(-100px);
            }
            
            .notification.show {
                transform: translateX(0) translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
});

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    // Close mobile menu with Escape key
    if (e.key === 'Escape' && navMenu && navMenu.classList.contains('show-menu')) {
        hideMenu();
    }
    
    // Navigate sections with arrow keys (when not in form)
    if (!e.target.matches('input, textarea, select')) {
        const currentSection = getCurrentSection();
        const sectionIds = ['home', 'about', 'services', 'skills', 'experience', 'projects', 'certifications', 'contact'];
        const currentIndex = sectionIds.indexOf(currentSection);
        
        if (e.key === 'ArrowDown' && currentIndex < sectionIds.length - 1) {
            e.preventDefault();
            scrollToSection(sectionIds[currentIndex + 1]);
        } else if (e.key === 'ArrowUp' && currentIndex > 0) {
            e.preventDefault();
            scrollToSection(sectionIds[currentIndex - 1]);
        }
    }
});

// Get current section based on scroll position
function getCurrentSection() {
    const scrollY = window.pageYOffset;
    let current = 'home';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 200;
        const sectionHeight = section.offsetHeight;
        
        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });
    
    return current;
}

// Scroll to section
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section && header) {
        const headerHeight = header.offsetHeight;
        const targetPosition = section.offsetTop - headerHeight;
        
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
}

// Performance optimization: throttle scroll events
function throttle(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply throttling to scroll events
const throttledScrollHeader = throttle(scrollHeader, 10);
const throttledScrollActive = throttle(scrollActive, 10);
const throttledParallax = throttle(parallaxEffect, 10);

window.addEventListener('scroll', throttledScrollHeader);
window.addEventListener('scroll', throttledScrollActive);
window.addEventListener('scroll', throttledParallax);

// Debug mode (remove in production)
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.log('Portfolio website loaded successfully!');
    console.log('Available sections:', Array.from(sections).map(s => s.id));
}