/**
 * カスタムスクリプト (main.js)
 * 工藤企画ウェブサイトのインタラクション制御
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // 1. フッター年号の自動更新
    const yearElem = document.getElementById('year');
    if (yearElem) {
        yearElem.textContent = new Date().getFullYear();
    }

    // 2. ヘッダーのスクロール時のスタイル変更
    const header = document.getElementById('header');
    
    function checkScroll() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
    
    // 初期チェックとスクロールイベント
    checkScroll();
    window.addEventListener('scroll', checkScroll);

    // 3. モバイル用ハンバーガーメニュートグル
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-menu a');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // アクセシビリティ対応
            const expanded = this.getAttribute('aria-expanded') === 'true' || false;
            this.setAttribute('aria-expanded', !expanded);
        });

        // メニュー内リンククリック時にメニューを閉じる
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // 4. スムーススクロール実装 (アンカーリンク)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                e.preventDefault();
                
                // ヘッダーの高さを考慮してスクロール
                const headerHeight = header ? header.offsetHeight : 0;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 5. スクロール時のフェードアップアニメーション
    const fadeElements = document.querySelectorAll('.fade-up');
    
    const fadeObserverOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // 少し画面内に入ってから発火
        threshold: 0.1
    };
    
    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            // 要素が画面内に入った場合
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // 一度表示したら監視を解除 (再度スクロールして消したくない場合)
                observer.unobserve(entry.target);
            }
        });
    }, fadeObserverOptions);
    
    // 監視要素をセット
    fadeElements.forEach(elem => {
        fadeObserver.observe(elem);
    });

    // 6. フォームのダミー送信アクション (ボタンのみのデモ用)
    const formButtons = document.querySelectorAll('.contact-buttons .btn');
    formButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            // 本番環境では実際のリンクをセットするかフォーム送信処理を行う
            alert('現在デモ環境です。実際のフォーム画面へ遷移します。');
        });
    });

});
