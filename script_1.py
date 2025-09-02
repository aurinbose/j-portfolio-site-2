# Create the complete CSS file content
css_content = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    font-size: 16px;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #0a0a0a;
    color: #ffffff;
    line-height: 1.6;
    overflow-x: hidden;
}

/* CSS Variables */
:root {
    --primary-color: #00d4ff;
    --secondary-color: #0088cc;
    --accent-color: #ff6b35;
    --background-dark: #0a0a0a;
    --background-section: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
    --text-muted: #808080;
    --border-color: #333333;
    --card-background: #2a2a2a;
    --gradient-primary: linear-gradient(135deg, #00d4ff, #0088cc);
    --gradient-secondary: linear-gradient(135deg, #ff6b35, #ff8c42);
    --shadow-light: 0 4px 20px rgba(0, 212, 255, 0.1);
    --shadow-medium: 0 8px 30px rgba(0, 212, 255, 0.2);
    --shadow-heavy: 0 20px 60px rgba(0, 212, 255, 0.3);
    --border-radius: 12px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.section {
    padding: 80px 0;
}

.section__title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 3rem;
    background: var(--gradient-primary);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Header */
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(10, 10, 10, 0.9);
    backdrop-filter: blur(10px);
    z-index: 1000;
    transition: var(--transition);
}

.header.scroll-header {
    background: rgba(10, 10, 10, 0.95);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

.nav__logo span {
    font-size: 1.5rem;
    font-weight: 700;
    background: var(--gradient-primary);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav__list {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav__link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: var(--transition);
    position: relative;
}

.nav__link:hover,
.nav__link.active-link {
    color: var(--primary-color);
}

.nav__link::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gradient-primary);
    transition: var(--transition);
}

.nav__link:hover::after,
.nav__link.active-link::after {
    width: 100%;
}

.nav__toggle,
.nav__close {
    display: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--text-primary);
}

/* Hero Section */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    position: relative;
    background: var(--background-dark);
    overflow: hidden;
}

.hero__container {
    position: relative;
    z-index: 2;
}

.hero__content {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.hero__image {
    width: 150px;
    height: 150px;
    margin: 0 auto 2rem;
    border-radius: 50%;
    background: var(--gradient-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-heavy);
    animation: float 3s ease-in-out infinite;
}

.hero__image-placeholder {
    font-size: 3rem;
    font-weight: 700;
    color: white;
}

.hero__name {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    background: var(--gradient-primary);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero__title {
    font-size: 1.5rem;
    font-weight: 500;
    color: var(--text-secondary);
    margin-bottom: 1rem;
}

.hero__tagline {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2.5rem;
    line-height: 1.7;
}

.hero__buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

/* Buttons */
.button {
    display: inline-flex;
    align-items: center;
    padding: 12px 24px;
    border-radius: var(--border-radius);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95rem;
    transition: var(--transition);
    cursor: pointer;
    border: 2px solid transparent;
}

.button--primary {
    background: var(--gradient-primary);
    color: white;
    box-shadow: var(--shadow-light);
}

.button--primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

.button--outline {
    background: transparent;
    color: var(--primary-color);
    border-color: var(--primary-color);
}

.button--outline:hover {
    background: var(--primary-color);
    color: white;
    transform: translateY(-2px);
}

/* Hero Background Animation */
.hero__background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 1;
}

.hero__particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: var(--primary-color);
    border-radius: 50%;
    animation: particle 20s linear infinite;
}

.hero__particle:nth-child(1) {
    top: 20%;
    left: 20%;
    animation-delay: 0s;
}

.hero__particle:nth-child(2) {
    top: 60%;
    right: 20%;
    animation-delay: 5s;
}

.hero__particle:nth-child(3) {
    bottom: 20%;
    left: 60%;
    animation-delay: 10s;
}

/* About Section */
.about {
    background: var(--background-section);
}

.about__container {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 4rem;
    align-items: center;
}

.about__image {
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: var(--gradient-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-heavy);
    margin: 0 auto;
}

.about__image-placeholder {
    font-size: 5rem;
    font-weight: 700;
    color: white;
}

.about__description {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.8;
}

.about__stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.about__stat {
    text-align: center;
    padding: 1rem;
    background: var(--card-background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
}

.about__stat-number {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
}

.about__stat-label {
    font-size: 0.9rem;
    color: var(--text-muted);
}

.about__info {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.about__info-item {
    color: var(--text-secondary);
}

.about__info-item a {
    color: var(--primary-color);
    text-decoration: none;
}

/* Services Section */
.services__container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.service__card {
    padding: 2rem;
    background: var(--card-background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    text-align: center;
    transition: var(--transition);
}

.service__card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-medium);
    border-color: var(--primary-color);
}

.service__icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.service__title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.service__description {
    color: var(--text-secondary);
    line-height: 1.6;
}

/* Skills Section */
.skills {
    background: var(--background-section);
}

.skills__container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 3rem;
}

.skills__category-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 2rem;
    color: var(--primary-color);
}

.skill__item {
    margin-bottom: 1.5rem;
}

.skill__header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
}

.skill__name {
    font-weight: 500;
    color: var(--text-primary);
}

.skill__percentage {
    color: var(--primary-color);
    font-weight: 600;
}

.skill__bar {
    height: 8px;
    background: var(--border-color);
    border-radius: 4px;
    overflow: hidden;
}

.skill__progress {
    height: 100%;
    background: var(--gradient-primary);
    border-radius: 4px;
    transition: width 2s ease-in-out;
}

/* Experience Section */
.experience__container {
    max-width: 800px;
    margin: 0 auto;
}

.experience__item {
    display: flex;
    gap: 2rem;
    margin-bottom: 3rem;
}

.experience__timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.experience__dot {
    width: 16px;
    height: 16px;
    background: var(--primary-color);
    border-radius: 50%;
    box-shadow: 0 0 0 4px rgba(0, 212, 255, 0.2);
}

.experience__line {
    width: 2px;
    height: 100px;
    background: var(--border-color);
    margin-top: 1rem;
}

.experience__item:last-child .experience__line {
    display: none;
}

.experience__content {
    flex: 1;
    padding: 1rem 0;
}

.experience__header {
    margin-bottom: 1rem;
}

.experience__title {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.experience__company {
    display: block;
    font-weight: 600;
    color: var(--primary-color);
    margin-bottom: 0.25rem;
}

.experience__period,
.experience__location {
    display: block;
    font-size: 0.9rem;
    color: var(--text-muted);
}

.experience__description {
    color: var(--text-secondary);
    margin-bottom: 1rem;
    font-style: italic;
}

.experience__achievements {
    list-style: none;
    padding: 0;
}

.experience__achievements li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.5rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

.experience__achievements li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--primary-color);
    font-weight: bold;
}

/* Projects Section */
.projects {
    background: var(--background-section);
}

.projects__container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.project__card {
    background: var(--card-background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    overflow: hidden;
    transition: var(--transition);
}

.project__card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-medium);
    border-color: var(--primary-color);
}

.project__image {
    height: 200px;
    background: var(--gradient-primary);
    display: flex;
    align-items: center;
    justify-content: center;
}

.project__placeholder {
    font-size: 4rem;
}

.project__content {
    padding: 1.5rem;
}

.project__title {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.project__description {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 1rem;
}

.project__technologies {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.project__tech {
    padding: 0.25rem 0.75rem;
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid var(--primary-color);
    border-radius: 20px;
    font-size: 0.8rem;
    color: var(--primary-color);
}

.project__year {
    font-weight: 600;
    color: var(--primary-color);
}

/* Certifications Section */
.certifications__container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.certification__card {
    padding: 2rem;
    background: var(--card-background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    text-align: center;
    transition: var(--transition);
}

.certification__card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-light);
    border-color: var(--primary-color);
}

.certification__badge {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.certification__name {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.certification__issuer {
    color: var(--text-secondary);
    margin-bottom: 1rem;
}

.certification__date {
    color: var(--primary-color);
    font-weight: 600;
}

/* Contact Section */
.contact {
    background: var(--background-section);
}

.contact__container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
}

.contact__info {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.contact__item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.5rem;
    background: var(--card-background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border-color);
    transition: var(--transition);
}

.contact__item:hover {
    border-color: var(--primary-color);
}

.contact__icon {
    font-size: 2rem;
    color: var(--primary-color);
}

.contact__details h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.contact__details a {
    color: var(--primary-color);
    text-decoration: none;
}

.contact__details span {
    color: var(--text-secondary);
}

.contact__form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact__input-group {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.contact__input {
    padding: 1rem;
    background: var(--card-background);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    color: var(--text-primary);
    font-size: 0.95rem;
    transition: var(--transition);
}

.contact__input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.1);
}

.contact__textarea {
    resize: vertical;
    min-height: 120px;
}

.contact__button {
    justify-self: flex-start;
}

/* Footer */
.footer {
    padding: 2rem 0;
    background: var(--background-dark);
    border-top: 1px solid var(--border-color);
}

.footer__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer__social {
    display: flex;
    gap: 1rem;
}

.footer__social-link {
    color: var(--text-secondary);
    text-decoration: none;
    transition: var(--transition);
}

.footer__social-link:hover {
    color: var(--primary-color);
}

/* Animations */
@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-20px);
    }
}

@keyframes particle {
    0% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    90% {
        opacity: 1;
    }
    100% {
        transform: translateY(-100vh) rotate(360deg);
        opacity: 0;
    }
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .nav__menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        height: 100vh;
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(10px);
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: var(--transition);
    }

    .nav__menu.show-menu {
        right: 0;
    }

    .nav__list {
        flex-direction: column;
        gap: 3rem;
    }

    .nav__toggle,
    .nav__close {
        display: block;
    }

    .nav__close {
        position: absolute;
        top: 2rem;
        right: 2rem;
    }

    .hero__name {
        font-size: 2.5rem;
    }

    .hero__title {
        font-size: 1.2rem;
    }

    .hero__buttons {
        flex-direction: column;
        align-items: center;
    }

    .about__container {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .about__stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .skills__container {
        grid-template-columns: 1fr;
    }

    .experience__item {
        gap: 1rem;
    }

    .contact__container {
        grid-template-columns: 1fr;
    }

    .contact__input-group {
        grid-template-columns: 1fr;
    }

    .footer__content {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }

    .section {
        padding: 60px 0;
    }

    .section__title {
        font-size: 2rem;
    }

    .hero__image {
        width: 120px;
        height: 120px;
    }

    .about__image {
        width: 250px;
        height: 250px;
    }

    .about__stats {
        grid-template-columns: 1fr;
    }
}

/* Scroll animations */
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease-out;
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Print styles */
@media print {
    .header,
    .hero__background,
    .nav__toggle,
    .nav__close {
        display: none !important;
    }
    
    body {
        background: white !important;
        color: black !important;
    }
}'''

print("Created complete CSS file with:")
print("- Modern dark theme design")
print("- Responsive layout for all screen sizes") 
print("- Smooth animations and transitions")
print("- Professional styling for all sections")
print("- Mobile-first responsive design")
print("- Accessibility considerations")