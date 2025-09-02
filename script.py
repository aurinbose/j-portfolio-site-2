import zipfile
import os
from io import StringIO

# Create the complete HTML file content
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aurin Bose - Data Analyst | BI & ESG Reporting</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Header Navigation -->
    <header class="header" id="header">
        <nav class="nav container">
            <div class="nav__logo">
                <span>Aurin Bose</span>
            </div>
            <div class="nav__menu" id="nav-menu">
                <ul class="nav__list">
                    <li class="nav__item"><a href="#home" class="nav__link active-link">Home</a></li>
                    <li class="nav__item"><a href="#about" class="nav__link">About</a></li>
                    <li class="nav__item"><a href="#services" class="nav__link">Services</a></li>
                    <li class="nav__item"><a href="#skills" class="nav__link">Skills</a></li>
                    <li class="nav__item"><a href="#experience" class="nav__link">Experience</a></li>
                    <li class="nav__item"><a href="#projects" class="nav__link">Projects</a></li>
                    <li class="nav__item"><a href="#certifications" class="nav__link">Certifications</a></li>
                    <li class="nav__item"><a href="#contact" class="nav__link">Contact</a></li>
                </ul>
                <div class="nav__close" id="nav-close">✕</div>
            </div>
            <div class="nav__toggle" id="nav-toggle">☰</div>
        </nav>
    </header>

    <main class="main">
        <!-- Hero Section -->
        <section class="hero section" id="home">
            <div class="hero__container container">
                <div class="hero__content">
                    <div class="hero__image">
                        <div class="hero__image-placeholder">AB</div>
                    </div>
                    <h1 class="hero__name">Aurin Bose</h1>
                    <h2 class="hero__title">Data Analyst | BI & ESG Reporting</h2>
                    <p class="hero__tagline">Transforming data into actionable insights with 3+ years of experience in business intelligence, data governance, and ESG reporting</p>
                    <div class="hero__buttons">
                        <a href="#contact" class="button button--primary">Contact Me</a>
                        <a href="Aurin-Bose-Resume-ATS.pdf" class="button button--outline" target="_blank">View Resume</a>
                    </div>
                </div>
                <div class="hero__background">
                    <div class="hero__particle"></div>
                    <div class="hero__particle"></div>
                    <div class="hero__particle"></div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section class="about section" id="about">
            <div class="container">
                <h2 class="section__title">About Me</h2>
                <div class="about__container">
                    <div class="about__image">
                        <div class="about__image-placeholder">AB</div>
                    </div>
                    <div class="about__content">
                        <p class="about__description">
                            Data Analyst with 3+ years of experience in business intelligence, data governance, and ESG reporting. 
                            Skilled in SQL, Python, Power BI, and Tableau, with a strong focus on transforming data into actionable 
                            insights. Certified in Google Analytics, Power BI, and Databricks, and currently driving data-driven 
                            solutions as an Associate Consultant at Ernst & Young.
                        </p>
                        <div class="about__stats">
                            <div class="about__stat">
                                <span class="about__stat-number">3+</span>
                                <span class="about__stat-label">Years Experience</span>
                            </div>
                            <div class="about__stat">
                                <span class="about__stat-number">50+</span>
                                <span class="about__stat-label">Projects Completed</span>
                            </div>
                            <div class="about__stat">
                                <span class="about__stat-number">5</span>
                                <span class="about__stat-label">Certifications</span>
                            </div>
                            <div class="about__stat">
                                <span class="about__stat-number">100%</span>
                                <span class="about__stat-label">Client Satisfaction</span>
                            </div>
                        </div>
                        <div class="about__info">
                            <div class="about__info-item">
                                <strong>Location:</strong> Gurgaon, HR
                            </div>
                            <div class="about__info-item">
                                <strong>Email:</strong> <a href="mailto:aurinbose@gmail.com">aurinbose@gmail.com</a>
                            </div>
                            <div class="about__info-item">
                                <strong>Phone:</strong> (+91) 7605018291
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services Section -->
        <section class="services section" id="services">
            <div class="container">
                <h2 class="section__title">Services & Expertise</h2>
                <div class="services__container">
                    <div class="service__card">
                        <div class="service__icon">📊</div>
                        <h3 class="service__title">Data Analysis</h3>
                        <p class="service__description">Advanced statistical analysis and data modeling to uncover insights and drive business decisions</p>
                    </div>
                    <div class="service__card">
                        <div class="service__icon">📈</div>
                        <h3 class="service__title">Business Intelligence</h3>
                        <p class="service__description">Creating comprehensive BI solutions and dashboards for data-driven decision making</p>
                    </div>
                    <div class="service__card">
                        <div class="service__icon">🌍</div>
                        <h3 class="service__title">ESG Reporting</h3>
                        <p class="service__description">Environmental, Social, and Governance reporting and compliance solutions</p>
                    </div>
                    <div class="service__card">
                        <div class="service__icon">📋</div>
                        <h3 class="service__title">Data Visualization</h3>
                        <p class="service__description">Interactive dashboards and visualizations using Tableau, Power BI, and modern tools</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Skills Section -->
        <section class="skills section" id="skills">
            <div class="container">
                <h2 class="section__title">Technical Skills</h2>
                <div class="skills__container">
                    <div class="skills__category">
                        <h3 class="skills__category-title">Programming</h3>
                        <div class="skills__items">
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">SQL</span>
                                    <span class="skill__percentage">95%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 95%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Python</span>
                                    <span class="skill__percentage">88%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 88%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">R</span>
                                    <span class="skill__percentage">75%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 75%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Java</span>
                                    <span class="skill__percentage">70%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 70%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="skills__category">
                        <h3 class="skills__category-title">Visualization</h3>
                        <div class="skills__items">
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Tableau</span>
                                    <span class="skill__percentage">92%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 92%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Power BI</span>
                                    <span class="skill__percentage">90%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 90%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Excel</span>
                                    <span class="skill__percentage">95%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 95%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">D3.js</span>
                                    <span class="skill__percentage">65%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 65%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="skills__category">
                        <h3 class="skills__category-title">Cloud & Tools</h3>
                        <div class="skills__items">
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Azure</span>
                                    <span class="skill__percentage">85%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 85%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">AWS</span>
                                    <span class="skill__percentage">80%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 80%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Git</span>
                                    <span class="skill__percentage">88%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 88%"></div>
                                </div>
                            </div>
                            <div class="skill__item">
                                <div class="skill__header">
                                    <span class="skill__name">Databricks</span>
                                    <span class="skill__percentage">82%</span>
                                </div>
                                <div class="skill__bar">
                                    <div class="skill__progress" style="width: 82%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Experience Section -->
        <section class="experience section" id="experience">
            <div class="container">
                <h2 class="section__title">Professional Experience</h2>
                <div class="experience__container">
                    <div class="experience__item">
                        <div class="experience__timeline">
                            <div class="experience__dot"></div>
                            <div class="experience__line"></div>
                        </div>
                        <div class="experience__content">
                            <div class="experience__header">
                                <h3 class="experience__title">Associate Consultant</h3>
                                <span class="experience__company">Ernst & Young</span>
                                <span class="experience__period">June 2023 – Present</span>
                                <span class="experience__location">Gurgaon, India</span>
                            </div>
                            <p class="experience__description">Tech Consulting, Data & Analytics & ESG</p>
                            <ul class="experience__achievements">
                                <li>Contributed to large-scale data pipeline migration project for international investment firm</li>
                                <li>Conducted comprehensive data criticality assessment for major South African bank</li>
                                <li>Played pivotal role in enterprise-wide data governance efforts</li>
                                <li>Anchored end-to-end implementation of Enablon for global ESG reporting</li>
                                <li>Delivered data discovery and quality assurance using Microsoft Purview</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="experience__item">
                        <div class="experience__timeline">
                            <div class="experience__dot"></div>
                        </div>
                        <div class="experience__content">
                            <div class="experience__header">
                                <h3 class="experience__title">Production Support Specialist</h3>
                                <span class="experience__company">Tata Consulting Services</span>
                                <span class="experience__period">Sept 2020 – March 2022</span>
                                <span class="experience__location">Warsaw, Poland</span>
                            </div>
                            <p class="experience__description">Application support and release management</p>
                            <ul class="experience__achievements">
                                <li>Resolved urgent incident tickets via ServiceNow with minimal disruption</li>
                                <li>Led weekly release management meetings for APAC region</li>
                                <li>Developed weekly and monthly impact reports for stakeholder decision-making</li>
                                <li>Conducted application testing using PL/SQL and Excel</li>
                                <li>Trained new hires on internal processes and tools</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section class="projects section" id="projects">
            <div class="container">
                <h2 class="section__title">Featured Projects</h2>
                <div class="projects__container">
                    <div class="project__card">
                        <div class="project__image">
                            <div class="project__placeholder">📊</div>
                        </div>
                        <div class="project__content">
                            <h3 class="project__title">ESG Reporting Dashboard</h3>
                            <p class="project__description">Comprehensive ESG metrics dashboard for sustainability reporting using Tableau and advanced data integration techniques</p>
                            <div class="project__technologies">
                                <span class="project__tech">Tableau</span>
                                <span class="project__tech">Python</span>
                                <span class="project__tech">SQL</span>
                                <span class="project__tech">Enablon</span>
                            </div>
                            <span class="project__year">2024</span>
                        </div>
                    </div>
                    
                    <div class="project__card">
                        <div class="project__image">
                            <div class="project__placeholder">📈</div>
                        </div>
                        <div class="project__content">
                            <h3 class="project__title">Financial Risk Analytics</h3>
                            <p class="project__description">Advanced risk modeling and analytics platform for investment decision-making with real-time data processing</p>
                            <div class="project__technologies">
                                <span class="project__tech">Python</span>
                                <span class="project__tech">R</span>
                                <span class="project__tech">Azure</span>
                                <span class="project__tech">Power BI</span>
                            </div>
                            <span class="project__year">2023</span>
                        </div>
                    </div>
                    
                    <div class="project__card">
                        <div class="project__image">
                            <div class="project__placeholder">🔗</div>
                        </div>
                        <div class="project__content">
                            <h3 class="project__title">Supply Chain Optimization</h3>
                            <p class="project__description">Data-driven supply chain analysis and optimization tool reducing costs by 15% through predictive modeling</p>
                            <div class="project__technologies">
                                <span class="project__tech">SQL</span>
                                <span class="project__tech">Tableau</span>
                                <span class="project__tech">Python</span>
                                <span class="project__tech">AWS</span>
                            </div>
                            <span class="project__year">2023</span>
                        </div>
                    </div>
                    
                    <div class="project__card">
                        <div class="project__image">
                            <div class="project__placeholder">👥</div>
                        </div>
                        <div class="project__content">
                            <h3 class="project__title">Customer Analytics Platform</h3>
                            <p class="project__description">Comprehensive customer behavior analysis and segmentation platform with machine learning insights</p>
                            <div class="project__technologies">
                                <span class="project__tech">Python</span>
                                <span class="project__tech">Databricks</span>
                                <span class="project__tech">Power BI</span>
                                <span class="project__tech">Azure</span>
                            </div>
                            <span class="project__year">2022</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Certifications Section -->
        <section class="certifications section" id="certifications">
            <div class="container">
                <h2 class="section__title">Certifications</h2>
                <div class="certifications__container">
                    <div class="certification__card">
                        <div class="certification__badge">🏆</div>
                        <h3 class="certification__name">Databricks Certified Data Analyst Associate</h3>
                        <p class="certification__issuer">Databricks</p>
                        <span class="certification__date">Nov 2024</span>
                    </div>
                    
                    <div class="certification__card">
                        <div class="certification__badge">📊</div>
                        <h3 class="certification__name">Google Business Intelligence Professional Certificate</h3>
                        <p class="certification__issuer">Coursera</p>
                        <span class="certification__date">May 2023</span>
                    </div>
                    
                    <div class="certification__card">
                        <div class="certification__badge">🎯</div>
                        <h3 class="certification__name">Google Data Analytics Professional Certificate</h3>
                        <p class="certification__issuer">Coursera</p>
                        <span class="certification__date">Jan 2023</span>
                    </div>
                    
                    <div class="certification__card">
                        <div class="certification__badge">📈</div>
                        <h3 class="certification__name">Microsoft Power BI Data Analyst</h3>
                        <p class="certification__issuer">Microsoft</p>
                        <span class="certification__date">Mar 2023</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="contact section" id="contact">
            <div class="container">
                <h2 class="section__title">Get In Touch</h2>
                <div class="contact__container">
                    <div class="contact__info">
                        <div class="contact__item">
                            <div class="contact__icon">📧</div>
                            <div class="contact__details">
                                <h3>Email</h3>
                                <a href="mailto:aurinbose@gmail.com">aurinbose@gmail.com</a>
                            </div>
                        </div>
                        
                        <div class="contact__item">
                            <div class="contact__icon">📱</div>
                            <div class="contact__details">
                                <h3>Phone</h3>
                                <span>(+91) 7605018291</span>
                            </div>
                        </div>
                        
                        <div class="contact__item">
                            <div class="contact__icon">📍</div>
                            <div class="contact__details">
                                <h3>Location</h3>
                                <span>Gurgaon, HR</span>
                            </div>
                        </div>
                        
                        <div class="contact__item">
                            <div class="contact__icon">💼</div>
                            <div class="contact__details">
                                <h3>LinkedIn</h3>
                                <a href="https://linkedin.com/in/aurin-bose" target="_blank">linkedin.com/in/aurin-bose</a>
                            </div>
                        </div>
                    </div>
                    
                    <div class="contact__form-container">
                        <form class="contact__form" id="contact-form">
                            <div class="contact__input-group">
                                <input type="text" class="contact__input" placeholder="Name" name="name" required>
                                <input type="email" class="contact__input" placeholder="Email" name="email" required>
                            </div>
                            <input type="text" class="contact__input" placeholder="Subject" name="subject" required>
                            <textarea class="contact__input contact__textarea" placeholder="Message" name="message" rows="5" required></textarea>
                            <button type="submit" class="button button--primary contact__button">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer__content">
                <p>&copy; 2025 Aurin Bose. All rights reserved.</p>
                <div class="footer__social">
                    <a href="https://linkedin.com/in/aurin-bose" class="footer__social-link" target="_blank">LinkedIn</a>
                    <a href="mailto:aurinbose@gmail.com" class="footer__social-link">Email</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>'''

print("Created complete HTML file structure")
print("File contains all sections: Hero, About, Services, Skills, Experience, Projects, Certifications, Contact")