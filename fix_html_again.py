import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Header update
header_new = """
    <!-- header -->
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
"""
text = re.sub(r'<!-- header -->.*?</header>', header_new.strip(), text, flags=re.DOTALL)

# Hero update
hero_new = """
    <!-- Hero Section -->
    <section class="hero dark-hero">
        <div class="hero-bg"></div>
        <div class="hero-overlay"></div>
        <div class="container hero-content">
            <div class="hero-text fade-up">
                <p class="en-subtitle" style="color:#fff; opacity:0.8; font-size: 1rem; margin-bottom: 2rem;">. <br>DELIVER<br>BEYOND</p>
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
"""
text = re.sub(r'<!-- Hero Section -->.*?(?=<!-- About Us Section -->)', hero_new.strip() + '\n\n    ', text, flags=re.DOTALL)


# Update About Us
about_new = """
    <!-- About Us Section -->
    <section id="about" class="section dark-section">
        <div class="container">
            <div class="section-title text-center fade-up">
                <span class="en-subtitle">ABOUT US</span>
                <h2>工藤企画が選ばれる3つの理由</h2>
            </div>
            <div class="features-wrapper mt-xl">
                <!-- Reason 1 -->
                <div class="dark-card fade-up">
                    <div class="feature-header">
                        <span class="feature-number">01</span>
                    </div>
                    <div class="feature-content">
                        <h3>ミスのない緻密な検品体制</h3>
                        <p>長年培ってきた独自のチェックフローを導入。二重トリプルチェックを徹底し、納品先にご迷惑をかけない高品質な仕上がりをお約束します。</p>
                    </div>
                </div>
                <!-- Reason 2 -->
                <div class="dark-card fade-up" style="transition-delay: 0.1s;">
                    <div class="feature-header">
                        <span class="feature-number">02</span>
                    </div>
                    <div class="feature-content">
                        <h3>小ロットからの柔軟な対応力</h3>
                        <p>「この細かい作業だけお願いしたい」「急遽今週中に梱包が必要になった」といったイレギュラーなご要望にも、柔軟・迅速に対応可能です。</p>
                    </div>
                </div>
                <!-- Reason 3 -->
                <div class="dark-card fade-up" style="transition-delay: 0.2s;">
                    <div class="feature-header">
                        <span class="feature-number">03</span>
                    </div>
                    <div class="feature-content">
                        <h3>任せて安心のセキュリティ</h3>
                        <p>お預かりした大切な商材や販促物、個人情報などは社内で厳重に管理。作業エリアへの入退室管理なども徹底しています。</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
text = re.sub(r'<!-- About Us Section -->.*?<!-- Services Section -->', about_new.strip() + '\n\n    <!-- Services Section -->', text, flags=re.DOTALL)


# Update Services
services_new = """
    <!-- Services Section -->
    <section id="business" class="section dark-section border-top-line">
        <div class="container">
            <div class="section-title text-center fade-up">
                <span class="en-subtitle">BUSINESS FIELD</span>
                <h2>主な業務内容</h2>
            </div>
            <div class="service-grid mt-xl">
                <div class="dark-service-card fade-up">
                    <div class="service-img-wrapper">
                        <div class="service-img img-packing"></div>
                        <div class="img-overlay"></div>
                    </div>
                    <div class="service-info">
                        <h3>梱包・封入・発送代行</h3>
                        <p>DMの封入、カタログ発送、ノベルティの袋詰めなど、あらゆる梱包作業を代行。指定倉庫や各店舗への一括・個別配送手配までワンストップで承ります。</p>
                    </div>
                </div>
                
                <div class="dark-service-card fade-up" style="transition-delay: 0.1s;">
                    <div class="service-img-wrapper">
                        <div class="service-img img-inspection"></div>
                        <div class="img-overlay"></div>
                    </div>
                    <div class="service-info">
                        <h3>検品・シール貼り</h3>
                        <p>商品の全数検品、アパレル商品のタグ付け・値札付け、成分表示シールや訂正シールの正確な貼付など、細かな注意が必要な作業も安心してお任せください。</p>
                    </div>
                </div>
                
                <div class="dark-service-card fade-up" style="transition-delay: 0.2s;">
                    <div class="service-img-wrapper">
                        <div class="service-img img-assembly"></div>
                        <div class="img-overlay"></div>
                    </div>
                    <div class="service-info">
                        <h3>組み立て・セット加工</h3>
                        <p>販促用POPの組み立て、複数商品のギフトセット化（アソート）、箱折りなど、機械では対応できない複雑な手作業も熟練スタッフが丁寧・迅速に仕上げます。</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
text = re.sub(r'<!-- Services Section -->.*?<!-- Recruit Section -->', services_new.strip() + '\n\n    <!-- Recruit Section -->', text, flags=re.DOTALL)


# Recruit
recruit_new = """
    <!-- Recruit Section -->
    <section id="recruit" class="section dark-section border-top-line" style="background-color: var(--primary-light);">
        <div class="container">
            <div class="recruit-wrapper">
                <div class="recruit-content fade-up">
                    <div class="section-title">
                        <span class="en-subtitle">RECRUIT INFO</span>
                        <h2>採用情報（パート・内職）</h2>
                    </div>
                    <h3 class="recruit-catch">私たちと一緒に働きませんか？</h3>
                    <p class="recruit-lead">
                        「空いた時間を有効活用したい」<br>
                        「モクモクと作業するのが好き」<br>
                        そんなあなたにピッタリな職場です。
                    </p>
                    <p class="text-muted" style="margin-bottom: 30px;">
                        工藤企画では、横浜市港北区高田西周辺で勤務可能なパートスタッフ、およびご自宅で作業可能な内職スタッフを募集しています。未経験の方でも、先輩スタッフが丁寧にイチから教えるので安心です。
                    </p>
                    <a href="#contact" class="btn btn-secondary">エントリーする</a>
                </div>
                
                <div class="recruit-details-card fade-up">
                    <h3 style="color:#fff;">募集要項</h3>
                    <dl class="recruit-list">
                        <dt>募集職種</dt>
                        <dd>場内軽作業スタッフ（パートタイム）、内職スタッフ</dd>
                        
                        <dt>仕事内容</dt>
                        <dd>シール貼り、簡単な組み立て、封入、検品などの手作業全般</dd>
                        
                        <dt>勤務地</dt>
                        <dd>神奈川県横浜市港北区高田西<br>（グリーンライン高田駅 徒歩〇分）</dd>
                        
                        <dt>勤務時間</dt>
                        <dd>9:00〜17:00 の間で応相談<br>★週2日〜、1日3時間〜OK！扶養内勤務歓迎</dd>
                        
                        <dt>休日・休暇</dt>
                        <dd>土・日・祝休み、GW、夏季、年末年始</dd>
                    </dl>
                </div>
            </div>
        </div>
    </section>
"""
text = re.sub(r'<!-- Recruit Section -->.*?<!-- Company Section -->', recruit_new.strip() + '\n\n    <!-- Company Section -->', text, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

