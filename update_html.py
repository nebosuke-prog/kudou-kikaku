with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Update Head section for CSS versioning
text = re.sub(r'<link rel="stylesheet" href="css/style\.css\?[^"]*">', '<link rel="stylesheet" href="css/style.css?v=11">', text)

# 2. Replace Header, Hero, Dual Track
new_top = """<!-- header -->
    <header class="header">
        <div class="header-inner container">
            <div class="logo">
                <a href="/">KUDOU KIKAKU</a>
            </div>
            <nav class="nav-menu">
                <ul>
                    <li><a href="#about">ABOUT US</a></li>
                    <li><a href="#business">BUSINESS</a></li>
                    <li><a href="#recruit">RECRUIT</a></li>
                    <li><a href="#company">COMPANY</a></li>
                </ul>
            </nav>
            <div class="header-action">
                <a href="#contact" class="btn btn-primary btn-sm btn-shadow">ENTRY & CONTACT</a>
            </div>
            <!-- SP Menu Button -->
            <button class="menu-toggle" aria-label="メニューを開く">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero dark-hero">
            <div class="hero-bg"></div>
            <div class="hero-overlay"></div>
            <div class="container hero-content">
                <div class="hero-text fade-up">
                    <p class="en-subtitle" style="color:#fff; opacity:0.8;">. <br>DELIVER<br>BEYOND</p>
                    <h1 class="hero-en-title">品質と正確性の、その先へ。</h1>
                    <p>
                        横浜市港北区の「工藤企画」は、正確・丁寧な梱包・発送代行や検品などの軽作業を通じ、<br>
                        企業様のビジネスを強力にスケールさせるアウトソーシング・パートナーです。<br>
                        <br>
                        企業の皆様には確かな安心を、地域の皆様には心地よい働きがいを。<br>
                        手作業の力で双方の未来をクリエイトします。
                    </p>
                </div>
            </div>
            <div class="scroll-indicator">
                <span>SCROLL</span>
                <div class="line"></div>
            </div>
        </section>

        <!-- Dual Track Navigation -->
        <section class="dual-track">
            <div class="track-container">
                <a href="#business" class="track-card">
                    <div class="track-bg img-business"></div>
                    <div class="track-content">
                        <span class="track-subtitle">法人のお客様へ</span>
                        <h2 class="track-title">For BUSINESS</h2>
                        <p>梱包・発送代行、検品・軽作業のアウトソーシング。<br>貴社のコアビジネスへの集中を加速させます。</p>
                        <div class="track-arrow"></div>
                    </div>
                </a>
                <a href="#recruit" class="track-card">
                    <div class="track-bg img-recruit"></div>
                    <div class="track-content">
                        <span class="track-subtitle">求職者の方へ</span>
                        <h2 class="track-title">For RECRUIT</h2>
                        <p>高田西周辺でのパート・内職スタッフ募集。<br>未経験から始められる、地域密着の温かい職場です。</p>
                        <div class="track-arrow"></div>
                    </div>
                </a>
            </div>
        </section>

        <!-- About Us Section -->"""

text = re.sub(r'<!-- header -->.*?<!-- About Us Section -->', new_top, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html to include Dual Track.")
