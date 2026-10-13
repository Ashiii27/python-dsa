import React, {useEffect} from 'react';
import {useLocation} from '@docusaurus/router';

/**
 * Site-wide micro-interaction layer:
 *  - reveal-on-scroll for [data-reveal] elements (with stagger via --reveal-delay)
 *  - navbar scroll state (blur + border once the page moves)
 * Re-runs on every route change so new pages animate in too.
 */
export default function Root({children}) {
  const location = useLocation();

  useEffect(() => {
    const doc = document.documentElement;
    doc.classList.add('js-reveal');

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ---- reveal on scroll ----
    let observer;
    const scan = () => {
      const nodes = document.querySelectorAll('[data-reveal]:not(.is-visible)');
      if (reduce) {
        nodes.forEach((el) => el.classList.add('is-visible'));
        return;
      }
      if (!observer) {
        observer = new IntersectionObserver(
          (entries) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
              }
            });
          },
          {threshold: 0.12, rootMargin: '0px 0px -6% 0px'},
        );
      }
      nodes.forEach((el) => observer.observe(el));
    };
    scan();

    // ---- navbar scrolled state ----
    const navbar = document.querySelector('.navbar');
    const onScroll = () => {
      if (!navbar) return;
      navbar.classList.toggle('navbar--scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, {passive: true});

    return () => {
      observer?.disconnect();
      window.removeEventListener('scroll', onScroll);
    };
  }, [location.pathname]);

  return <>{children}</>;
}
