import re

with open('css/style.css', 'r') as f:
    css = f.read()

# 1. Colors to Dark Theme
css = css.replace('--primary-color: #0A2540;', '--primary-color: #050a15;')
css = css.replace('--primary-light: #1A3E6D;', '--primary-light: #0a1122;')
css = css.replace('--text-main: #333333;', '--text-main: #ffffff;')
css = css.replace('--text-dark: #1A1A1A;', '--text-dark: #f0f0f0;')
css = css.replace('--bg-main: #FFFFFF;', '--bg-main: #02050a;')
css = css.replace('--bg-light: #F8FAFC;', '--bg-light: #050a15;')
css = css.replace('--border-color: #E2E8F0;', '--border-color: rgba(255, 255, 255, 0.1);')

# 2. Add --text-muted
css = css.replace('--text-dark: #f0f0f0;\n', '--text-dark: #f0f0f0;\n    --text-muted: rgba(255, 255, 255, 0.6);\n')

# 3. Headings letter spacing
css = css.replace('letter-spacing: 0.05em;', 'letter-spacing: 0.1em;')

# 4. English Subtitle class
en_subtitle = """
.en-subtitle {
    font-family: var(--font-heading);
    font-size: 0.9rem;
    color: var(--secondary-color);
    letter-spacing: 0.2em;
    display: block;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    font-weight: 600;
}
"""
css = css.replace('/* =========================================\n   ボタン\n   ========================================= */', en_subtitle + '/* =========================================\n   ボタン\n   ========================================= */')

# 5. Button Primary colors
css = css.replace('.btn-primary {\n    background-color: var(--primary-color);\n    color: #fff;', '.btn-primary {\n    background-color: var(--text-main);\n    color: #000;')

# 6. Button Hover
css = css.replace('background-color: var(--primary-light);', 'background-color: var(--secondary-color);\n    color: #fff;')

# 7. Replace Header
header_css = """
/* =========================================
   ヘッダー
   ========================================= */
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    background-color: transparent;
    transition: var(--transition-base);
    padding: 20px 0;
}

.header.scrolled {
    background-color: rgba(5, 10, 21, 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: var(--shadow-sm);
    padding: 12px 0;
}

.header-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo a {
    font-family: var(--font-heading);
    font-size: 1.6rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: 0.1em;
}

.header.scrolled .logo a {
    color: var(--text-main);
}

.nav-menu ul {
    display: flex;
    gap: 30px;
}

.nav-menu a {
    color: rgba(255, 255, 255, 0.9);
    font-weight: 500;
    position: relative;
}

.header.scrolled .nav-menu a {
    color: var(--text-main);
}

.nav-menu a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background-color: var(--secondary-color);
    transition: var(--transition-base);
}

.nav-menu a:hover::after {
    width: 100%;
}

.menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    width: 30px;
    height: 20px;
    position: relative;
    z-index: 1001;
}

.menu-toggle span {
    display: block;
    width: 100%;
    height: 2px;
    background-color: #fff;
    position: absolute;
    transition: var(--transition-base);
}

.header.scrolled .menu-toggle span {
    background-color: var(--text-main);
}

.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 9px; }
.menu-toggle span:nth-child(3) { top: 18px; }

.menu-toggle.active span:nth-child(1) {
    top: 9px;
    transform: rotate(45deg);
    background-color: #fff;
}

.menu-toggle.active span:nth-child(2) { opacity: 0; }

.menu-toggle.active span:nth-child(3) {
    top: 9px;
    transform: rotate(-45deg);
    background-color: #fff;
}
"""
css = re.sub(r'/\* =========================================\n   ヘッダー\n   ========================================= \*/.*?/\* =========================================\n   1\. Heroセクション\n   ========================================= \*/', header_css + '\n/* =========================================\n   1. Heroセクション\n   ========================================= */', css, flags=re.DOTALL)

# 8. Replace Hero
hero_css = """
.dark-hero {
    position: relative;
    height: 100vh;
    min-height: 700px;
    display: flex;
    align-items: center;
    padding-top: 80px;
    overflow: hidden;
}

.hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url('../images/hero-bg.png') center/cover no-repeat;
    z-index: -2;
    transform: scale(1.05);
    animation: zoomOut 20s ease infinite alternate;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgba(5, 10, 21, 0.95) 0%, rgba(5, 10, 21, 0.6) 50%, rgba(5, 10, 21, 0.4) 100%);
    z-index: -1;
}

@keyframes zoomOut {
    0% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.hero-content {
    position: relative;
    z-index: 1;
}

.hero-text {
    max-width: 800px;
    color: #fff;
    padding-left: 5%;
}

.hero-en-title {
    font-family: var(--font-heading);
    font-size: clamp(4rem, 8vw, 7rem);
    font-weight: 800;
    line-height: 1;
    margin-bottom: 0;
    letter-spacing: -0.02em;
    color: #fff;
    text-transform: uppercase;
}

.hero-divider {
    width: 60px;
    height: 4px;
    background-color: var(--secondary-color);
    margin: 2rem 0;
}

.hero-text h1 {
    color: #fff;
    font-size: 1.8rem;
    line-height: 1.4;
    font-weight: 500;
    margin-bottom: 1.5rem;
    letter-spacing: 0.1em;
}

.hero-text p {
    font-size: 1.05rem;
    opacity: 0.8;
    margin-bottom: 2.5rem;
    line-height: 2;
    max-width: 600px;
}

.scroll-indicator {
    position: absolute;
    bottom: 40px;
    left: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    z-index: 10;
}

.scroll-indicator span {
    font-family: var(--font-heading);
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    writing-mode: vertical-rl;
    transform: rotate(180deg);
}

.scroll-indicator .line {
    width: 1px;
    height: 60px;
    background-color: rgba(255, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
}

.scroll-indicator .line::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 50%;
    background-color: var(--secondary-color);
    animation: scrollDown 2s ease-in-out infinite;
}

@keyframes scrollDown {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(200%); }
}

/* =========================================
   2. Dual Track (For BUSINESS / For RECRUIT)
   ========================================= */
.dual-track {
    width: 100%;
    background-color: var(--bg-main);
}

.track-container {
    display: grid;
    grid-template-columns: 1fr;
    min-height: auto;
}

@media screen and (min-width: 993px) {
    .track-container {
        grid-template-columns: 1fr 1fr !important;
        min-height: 600px;
    }
}

.track-card {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 60px 50px;
    overflow: hidden;
    color: #fff;
    text-decoration: none;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.track-card:last-child {
    border-right: none;
}

.track-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    z-index: 1;
    transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.img-business { background-image: url('../images/service-packing.png'); }
.img-recruit { background-image: url('../images/hero-bg.png'); }

.track-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to top, rgba(5, 10, 21, 0.95) 0%, rgba(5, 10, 21, 0.4) 100%);
    z-index: 2;
    transition: background 0.4s ease;
}

.track-content {
    position: relative;
    z-index: 3;
    transition: transform 0.4s ease;
}

.track-subtitle {
    font-family: var(--font-body);
    font-size: 0.9rem;
    color: var(--secondary-color);
    font-weight: 600;
    letter-spacing: 0.1em;
    display: block;
    margin-bottom: 0.5rem;
}

.track-title {
    font-family: var(--font-heading);
    font-size: 3rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 1rem;
    line-height: 1.1;
    letter-spacing: 0.05em;
}

.track-card p {
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 2rem;
    line-height: 1.8;
    max-width: 90%;
}

.track-arrow {
    width: 50px;
    height: 50px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s ease;
}

.track-arrow::after {
    content: '→';
    color: #fff;
    font-size: 1.2rem;
}

.track-card:hover .track-bg {
    transform: scale(1.05);
}

.track-card:hover::before {
    background: linear-gradient(to top, rgba(5, 10, 21, 0.95) 0%, rgba(5, 10, 21, 0.2) 100%);
}

.track-card:hover .track-content {
    transform: translateY(-10px);
}

.track-card:hover .track-arrow {
    background-color: var(--secondary-color);
    border-color: var(--secondary-color);
}
"""
css = re.sub(r'\.hero \{.*?/\* =========================================\n   2\. About Usセクション\n   ========================================= \*/', hero_css + '\n/* =========================================\n   3. About Usセクション (Dark)\n   ========================================= */', css, flags=re.DOTALL)

# 9. Replace About Us
about_css = """
.features-wrapper {
    display: grid;
    gap: 30px;
}

@media screen and (min-width: 993px) {
    .features-wrapper {
        grid-template-columns: repeat(3, 1fr) !important;
    }
    .dark-card {
        flex-direction: column !important;
        text-align: center;
        align-items: center;
    }
}

.dark-card {
    background: var(--primary-light);
    border-radius: 4px;
    padding: 50px 40px;
    display: flex;
    gap: 20px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition-base);
    border: 1px solid var(--border-color);
}

.dark-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-md);
    border-color: var(--secondary-color);
}

.feature-header {
    margin-bottom: 20px;
}

.feature-number {
    font-family: var(--font-heading);
    font-size: 3.5rem;
    font-weight: 800;
    color: var(--secondary-color);
    line-height: 1;
    opacity: 0.8;
}

.feature-content h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: var(--text-main);
    letter-spacing: 0.05em;
}

.feature-content p {
    font-size: 0.95rem;
    color: var(--text-muted);
    line-height: 1.8;
}

/* =========================================
   4. Servicesセクション (Dark Cards)
   ========================================= */
.service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 40px;
}

.dark-service-card {
    background-color: var(--primary-light);
    border-radius: 4px;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: var(--transition-base);
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color);
}

.dark-service-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-md);
    border-color: var(--secondary-color);
}

.service-img-wrapper {
    position: relative;
    height: 240px;
    overflow: hidden;
}

.service-img {
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: transform var(--transition-slow);
}

.img-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, transparent 0%, rgba(5, 10, 21, 0.8) 100%);
    z-index: 1;
    transition: opacity 0.4s ease;
}

.dark-service-card:hover .service-img {
    transform: scale(1.05);
}

.dark-service-card:hover .img-overlay {
    opacity: 0.5;
}

.img-packing { background-image: url('../images/service-packing.png'); }
.img-inspection { background-image: url('../images/service-inspection.png'); }
.img-assembly { background-image: url('../images/service-assembly.png'); }

.service-info {
    padding: 40px 30px;
    flex-grow: 1;
    position: relative;
    z-index: 2;
}

.service-info h3 {
    font-size: 1.4rem;
    margin-bottom: 1rem;
    color: var(--text-main);
}

.service-info p {
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.8;
}
"""
css = re.sub(r'\.features-wrapper \{.*?/\* =========================================\n   4\. Recruitセクション\n   ========================================= \*/', about_css + '\n/* =========================================\n   5. Recruitセクション\n   ========================================= */', css, flags=re.DOTALL)

# 10. Replace Recruit
recruit_css = """
.recruit-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.recruit-content h3 {
    font-size: 1.8rem;
    margin-bottom: 20px;
}

.recruit-catch {
    color: var(--secondary-color);
    font-size: 1.5rem;
    line-height: 1.5;
    margin-bottom: 30px;
    font-weight: 500;
}

.recruit-lead {
    font-size: 1rem;
    line-height: 1.8;
}

.recruit-details-card {
    background: var(--primary-light);
    padding: 50px;
    border-radius: 4px;
    box-shadow: var(--shadow-sm);
    border-top: 4px solid var(--secondary-color);
}

.recruit-details-card h3 {
    font-size: 1.6rem;
    margin-bottom: 25px;
    text-align: center;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 15px;
    color: var(--text-main);
}

.recruit-list dt {
    font-weight: 700;
    color: var(--secondary-color);
    margin-top: 20px;
    display: flex;
    align-items: center;
}

.recruit-list dt::before {
    content: '';
    display: inline-block;
    width: 6px;
    height: 6px;
    background-color: var(--secondary-color);
    margin-right: 10px;
}

.recruit-list dd {
    margin-left: 0;
    margin-bottom: 5px;
    padding-left: 16px;
    border-bottom: 1px dashed var(--border-color);
    padding-bottom: 10px;
    color: var(--text-main);
}

.recruit-list dd:last-child {
    border-bottom: none;
}
"""
css = re.sub(r'\.recruit-wrapper \{.*?/\* =========================================\n   5\. Company & Accessセクション\n   ========================================= \*/', recruit_css + '\n/* =========================================\n   6. Company & Accessセクション\n   ========================================= */', css, flags=re.DOTALL)

# 11. Replace Company
company_css = """
.company-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
}

.company-table {
    width: 100%;
}

.company-table dt {
    font-weight: 600;
    padding: 20px 0;
    border-bottom: 1px solid var(--border-color);
    width: 25%;
    float: left;
    clear: both;
    color: var(--text-muted);
}

.company-table dd {
    padding: 20px 0;
    border-bottom: 1px solid var(--border-color);
    width: 75%;
    float: left;
    color: var(--text-main);
}

.company-table::after {
    content: "";
    display: table;
    clear: both;
}

.company-map iframe {
    filter: invert(90%) hue-rotate(180deg) contrast(100%);
}
"""
css = re.sub(r'\.company-wrapper \{.*?/\* =========================================\n   6\. Contactセクション\n   ========================================= \*/', company_css + '\n/* =========================================\n   7. Contactセクション\n   ========================================= */', css, flags=re.DOTALL)


# 12. Replace Footer
footer_css = """
/* =========================================
   8. Footer
   ========================================= */
.footer {
    background-color: var(--primary-color);
    color: var(--text-muted);
    padding: 80px 0 40px;
    border-top: 1px solid var(--border-color);
}

.footer-logo {
    font-family: var(--font-heading);
    font-size: 2.2rem;
    font-weight: 800;
    color: #fff;
    margin-bottom: 20px;
    letter-spacing: 0.05em;
}

.footer-address {
    margin-bottom: 40px;
    font-size: 0.95rem;
    line-height: 1.8;
}

.footer-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 30px;
    margin-bottom: 50px;
}

.footer-links a {
    color: var(--text-main);
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.footer-links a:hover {
    color: var(--secondary-color);
}

.copyright {
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 30px;
    text-align: center;
}
"""
css = re.sub(r'/\* =========================================\n   フッター\n   ========================================= \*/.*?/\* =========================================\n   レスポンシブデザイン \(Media Queries\)\n   ========================================= \*/', footer_css + '\n/* =========================================\n   レスポンシブデザイン (Media Queries)\n   ========================================= */', css, flags=re.DOTALL)


# 13. Mobile Overrides
mobile_css = """
    /* ヘッダー SP対応 */
    .header { padding: 15px 0; }
    .logo a { font-size: 1.4rem; }

    /* フルスクリーン・ハンバーガーメニューのリッチ化 */
    .nav-menu {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background-color: rgba(5, 10, 21, 0.98);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.4s ease, visibility 0.4s ease;
        z-index: 1000;
    }

    .nav-menu.active { opacity: 1; visibility: visible; }
    .nav-menu ul { flex-direction: column; gap: 30px; text-align: center; }
    
    .nav-menu a {
        color: #fff;
        font-size: 1.6rem;
        font-family: var(--font-heading);
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        display: block;
        transform: translateY(20px);
        opacity: 0;
        transition: transform 0.4s ease, opacity 0.4s ease, color 0.2s ease;
    }

    .nav-menu.active a { transform: translateY(0); opacity: 1; }
    .nav-menu.active li:nth-child(1) a { transition-delay: 0.1s; }
    .nav-menu.active li:nth-child(2) a { transition-delay: 0.2s; }
    .nav-menu.active li:nth-child(3) a { transition-delay: 0.3s; }
    .nav-menu.active li:nth-child(4) a { transition-delay: 0.4s; }

    .nav-menu a:hover { color: var(--secondary-color); }
    .header-action { display: none; }
    
    .menu-toggle { display: block; z-index: 1001; }
    .header.scrolled .menu-toggle span { background-color: var(--text-main); }
    .menu-toggle.active span { background-color: #fff !important; }

    /* セクション調整 */
    .section-title h2 { font-size: 1.8rem; }
    
    .hero-en-title { font-size: clamp(3rem, 10vw, 4.5rem); }
    .hero-text h1 { font-size: 1.5rem; margin-bottom: 1rem; }
    .hero-text p { font-size: 1rem; line-height: 1.8; }
    .hero-buttons { flex-direction: column; gap: 15px; }

    .track-container { grid-template-columns: 1fr !important; min-height: auto; }
    .track-card { padding: 50px 30px; min-height: 400px; border-right: none; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
    .track-title { font-size: 2.2rem; }

    .btn { width: 100%; padding: 16px 20px; font-size: 1rem; }
    
    .dark-card { flex-direction: column; gap: 15px; padding: 25px; text-align: center; }
    .feature-icon { font-size: 2.5rem; margin-bottom: -10px; }
    
    .service-grid { grid-template-columns: 1fr; gap: 20px; }
    .service-img-wrapper { height: 180px; }
    
    .recruit-wrapper, .company-wrapper { gap: 40px; }
    .recruit-content h3 { font-size: 1.5rem; }
    .recruit-details-card { padding: 25px; border-radius: 12px; }
    .recruit-details-card h3 { font-size: 1.3rem; }
    
    .contact-methods { padding: 20px 15px; gap: 20px; }
    .contact-phone, .contact-web { padding: 25px 20px; }
    .phone-number { font-size: 2rem; }
    
    .footer { padding: 40px 0 20px; }
    .footer-links { flex-direction: column; gap: 15px; }
"""
css = re.sub(r'    /\* ヘッダー SP対応 \*/.*?\}', mobile_css + '\n}', css, flags=re.DOTALL)

with open('css/style.css', 'w') as f:
    f.write(css)

