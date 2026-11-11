window.HELP_IMPROVE_VIDEOJS = false;

// Copy BibTeX to clipboard
function copyBibTeX() {
    const bibtexElement = document.getElementById('bibtex-code');
    const button = document.querySelector('.copy-bibtex-btn');
    const copyText = button.querySelector('.copy-text');
    
    if (bibtexElement) {
        navigator.clipboard.writeText(bibtexElement.textContent).then(function() {
            // Success feedback
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        }).catch(function(err) {
            console.error('Failed to copy: ', err);
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = bibtexElement.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        });
    }
}

// Scroll to top functionality
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Show/hide scroll to top button
window.addEventListener('scroll', function() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
});

// Video carousel autoplay when in view
function setupVideoCarouselAutoplay() {
    const carouselVideos = document.querySelectorAll('.results-carousel video');
    
    if (carouselVideos.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            if (entry.isIntersecting) {
                // Video is in view, play it
                video.play().catch(e => {
                    // Autoplay failed, probably due to browser policy
                    console.log('Autoplay prevented:', e);
                });
            } else {
                // Video is out of view, pause it
                video.pause();
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the video is visible
    });
    
    carouselVideos.forEach(video => {
        observer.observe(video);
    });
}

if (window.jQuery) $(document).ready(function() {
    // Check for click events on the navbar burger icon

    var options = {
		slidesToScroll: 1,
		slidesToShow: 1,
		loop: true,
		infinite: true,
		autoplay: true,
		autoplaySpeed: 5000,
    }

	// Initialize all div with carousel class
    if (window.bulmaCarousel) bulmaCarousel.attach('.carousel', options);

    if (window.bulmaSlider) bulmaSlider.attach();
    
    // Setup video autoplay for carousel
    setupVideoCarouselAutoplay();

})


/* ==========================================================================
   Visual refresh: hero film background, navigation, film lightbox, reveal
   ========================================================================== */
;(function () {
    'use strict';

    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---- Hero background video ---- */
    var heroVideo = document.querySelector('[data-hero-video]');
    var heroToggle = document.querySelector('[data-hero-video-toggle]');
    var hero = heroVideo ? heroVideo.closest('.cad-rsi-hero') : null;
    var userPaused = false;
    var heroInView = true;

    function playHero() {
        if (!heroVideo) return;
        var p = heroVideo.play();
        if (p && typeof p.catch === 'function') p.catch(function () {});
    }

    function syncToggle() {
        if (!heroToggle || !heroVideo) return;
        var paused = heroVideo.paused;
        heroToggle.classList.toggle('is-paused', paused);
        heroToggle.setAttribute('aria-pressed', paused ? 'true' : 'false');
        heroToggle.setAttribute('aria-label', paused ? 'Play background video' : 'Pause background video');
    }

    if (heroVideo) {
        var markPlaying = function () {
            heroVideo.classList.add('is-playing');
            heroVideo.playbackRate = 0.85;
        };
        heroVideo.addEventListener('playing', markPlaying);
        heroVideo.addEventListener('timeupdate', function onFirstFrame() {
            if (heroVideo.currentTime > 0) {
                markPlaying();
                heroVideo.removeEventListener('timeupdate', onFirstFrame);
            }
        });
        heroVideo.addEventListener('play', syncToggle);
        heroVideo.addEventListener('pause', syncToggle);
        // Autoplay may already be running before this deferred script executes.
        if (!heroVideo.paused || heroVideo.currentTime > 0) markPlaying();

        if (reduceMotion) {
            userPaused = true;
            heroVideo.removeAttribute('autoplay');
            heroVideo.pause();
        }

        if (heroToggle) {
            heroToggle.addEventListener('click', function () {
                if (heroVideo.paused) {
                    userPaused = false;
                    heroVideo.classList.add('is-playing');
                    playHero();
                } else {
                    userPaused = true;
                    heroVideo.pause();
                }
                syncToggle();
            });
        }

        if ('IntersectionObserver' in window && hero) {
            new IntersectionObserver(function (entries) {
                heroInView = entries[0].isIntersecting;
                if (heroInView && !userPaused && !document.documentElement.classList.contains('film-open')) playHero();
                else if (!heroInView) heroVideo.pause();
            }, { threshold: 0.02 }).observe(hero);
        }
        syncToggle();
    }

    /* ---- Navigation: solid on scroll, active section ---- */
    var nav = document.querySelector('[data-site-nav]');
    if (nav) {
        var links;
        var onScroll = function () {
            nav.classList.toggle('is-solid', window.scrollY > 24);
            // Over the title hero no section link is "current".
            if (links && hero && window.scrollY < hero.offsetHeight * 0.5) {
                links.forEach(function (a) { a.classList.remove('is-active'); });
            }
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        links = Array.prototype.slice.call(nav.querySelectorAll('.site-nav-links a'));
        var targets = links.map(function (a) {
            return document.querySelector(a.getAttribute('href'));
        });
        if ('IntersectionObserver' in window) {
            var spy = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) return;
                    var i = targets.indexOf(entry.target);
                    links.forEach(function (a, j) { a.classList.toggle('is-active', j === i); });
                });
            }, { rootMargin: '-45% 0px -50% 0px' });
            targets.forEach(function (t) { if (t) spy.observe(t); });
        }
    }

    /* ---- Film lightbox ---- */
    var modal = document.getElementById('film-modal');
    var openers = document.querySelectorAll('[data-film-open]');
    if (modal && typeof modal.showModal === 'function') {
        var filmVideo = modal.querySelector('video');
        var closeFilm = function () {
            if (modal.open) modal.close();
        };
        Array.prototype.forEach.call(openers, function (opener) {
            opener.addEventListener('click', function (event) {
                event.preventDefault();
                document.documentElement.classList.add('film-open');
                if (heroVideo) heroVideo.pause();
                modal.showModal();
                if (filmVideo) {
                    try { filmVideo.currentTime = 0; } catch (e) {}
                    var p = filmVideo.play();
                    if (p && typeof p.catch === 'function') p.catch(function () {});
                }
            });
        });
        modal.addEventListener('click', function (event) {
            if (event.target === modal) closeFilm();
        });
        var closeBtn = modal.querySelector('[data-film-close]');
        if (closeBtn) closeBtn.addEventListener('click', closeFilm);
        modal.addEventListener('close', function () {
            document.documentElement.classList.remove('film-open');
            if (filmVideo) filmVideo.pause();
            if (heroVideo && heroInView && !userPaused) playHero();
        });
    }

    /* ---- Scroll reveal ---- */
    if (!reduceMotion && 'IntersectionObserver' in window) {
        var revealTargets = document.querySelectorAll(
            '.section-eyebrow, main .title.is-3, .abstract-section .content, .mechatlas-atlas, ' +
            'main figure, .comparison-table-shell, .cad-replay-stage, .bibtex-section pre'
        );
        var revealer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-in');
                    revealer.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
        Array.prototype.forEach.call(revealTargets, function (el) {
            if (el.closest('.cad-rsi-hero')) return;
            el.classList.add('reveal');
            revealer.observe(el);
        });
        // Never leave content hidden in print.
        window.addEventListener('beforeprint', function () {
            Array.prototype.forEach.call(document.querySelectorAll('.reveal'), function (el) {
                el.classList.add('is-in');
            });
        });
    }
})();
