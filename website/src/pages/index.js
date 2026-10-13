import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const STATS = [
  {num: '12', label: 'hands-on Python modules'},
  {num: '24', label: 'DSA topics, basics → advanced'},
  {num: '35', label: 'problem write-ups with proofs & tests'},
  {num: '280+', label: 'curated practice problems'},
];

const TICKER = [
  'two pointers', 'sliding window', 'prefix sums', 'monotonic stack',
  'fast & slow pointers', 'binary search on answer', 'Kadane', 'topological sort',
  'Dijkstra', 'union find', 'backtracking', 'DP states', 'trie traversal',
  'segment tree', 'rolling hash', 'greedy exchange', 'heap / top-k', 'bitmask DP',
];

const FEATURES = [
  {
    title: 'Learn by running code',
    body: 'Every lesson and worked problem ships with an in-browser Python runner. Edit the stubs, run the real unit tests, and see results instantly — no install.',
  },
  {
    title: 'Two tracks, one path',
    body: 'Start with the Python Track (syntax → OOP → testing → packaging), then the DSA Track (complexity → arrays → graphs → DP → advanced structures). Each hands you to the next.',
  },
  {
    title: 'Patterns, not memorization',
    body: 'Study guides teach the mental model, the invariant, and the proof. Pattern-signal tables tell you which tool to reach for — then you derive the solution yourself.',
  },
  {
    title: 'Progress that persists',
    body: 'Check off lessons and topics as you go. Your progress is saved in the browser so the site works like a real course dashboard.',
  },
  {
    title: 'Interview-grade depth',
    body: 'Brute force → optimized → invariant → complexity → edge cases. The write-up structure mirrors how strong candidates talk through problems.',
  },
  {
    title: 'Revise actively',
    body: 'Flashcards, revision checklists, a visual pattern guide, and a problem-solving framework turn knowledge into recall under pressure.',
  },
];

function Hero() {
  return (
    <header className={styles.hero}>
      <div className={styles.heroGrain} aria-hidden="true" />
      <div className={clsx('container', styles.heroInner)}>
        <p className={styles.eyebrow} style={{animationDelay: '0.05s'}}>
          <span className={styles.eyebrowDot} />
          open source · one repo · learn by running code
        </p>
        <h1 className={styles.heroTitle}>
          <span style={{animationDelay: '0.15s'}}>Master Python.</span>{' '}
          <span style={{animationDelay: '0.3s'}}>Then master</span>{' '}
          <span className={styles.heroAccent} style={{animationDelay: '0.45s'}}>
            the algorithms
            <svg className={styles.squiggle} viewBox="0 0 280 16" fill="none" aria-hidden="true">
              <path
                d="M3 11.5c22-6 44-7 66-4 24 3.4 46 5.6 70 3 22-2.4 44-7.4 66-6.2 22 1.2 44 6.8 66 7.8"
                stroke="currentColor"
                strokeWidth="5"
                strokeLinecap="round"
              />
            </svg>
          </span>
          <br />
          <span className={styles.heroItal} style={{animationDelay: '0.6s'}}>
            that run the industry.
          </span>
        </h1>
        <p className={styles.heroSub} style={{animationDelay: '0.75s'}}>
          A complete, hands-on course — from your first Python program to
          top-tier interview readiness. Two tracks, interactive exercises, and a
          curriculum built on patterns and proofs, not memorization.
        </p>
        <div className={styles.ctaRow} style={{animationDelay: '0.9s'}}>
          <Link className="button button--primary button--lg" to="/python">
            Start with Python&nbsp;→
          </Link>
          <Link className="button button--outline button--lg" to="/dsa">
            Jump to the DSA Track
          </Link>
        </div>
        <div className={styles.stats} style={{animationDelay: '1.05s'}}>
          {STATS.map((s) => (
            <div key={s.label} className={styles.stat}>
              <div className={styles.statNum}>{s.num}</div>
              <div className={styles.statLabel}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>
    </header>
  );
}

function Ticker() {
  const row = [...TICKER, ...TICKER];
  return (
    <div className={styles.ticker} aria-hidden="true">
      <div className={styles.tickerTrack}>
        {row.map((word, i) => (
          <span key={i} className={styles.tickerItem}>
            {word}
            <span className={styles.tickerSep}>✳</span>
          </span>
        ))}
      </div>
    </div>
  );
}

function TrackCards() {
  return (
    <section className={styles.section}>
      <div className="container">
        <p className={styles.kicker} data-reveal>choose your track</p>
        <h2 className={styles.sectionTitle} data-reveal>
          Two tracks. One <em className={styles.em}>unbroken</em> path.
        </h2>
        <div className={styles.trackGrid}>
          <article className={styles.trackCard} data-reveal style={{'--reveal-delay': '0.1s'}}>
            <div className={styles.trackNum}>01</div>
            <h3>Basics → Advanced Programming with Python</h3>
            <p>
              12 hands-on modules with notes, stub exercises, reference
              solutions, and auto-graded tests — plus capstone projects. Takes
              you from installation to shipping a tested Python project.
            </p>
            <ul className={styles.trackList}>
              <li>Syntax, types, collections, control flow</li>
              <li>Functions, iterators, generators, OOP</li>
              <li>Errors, testing, files, the standard library</li>
              <li>Typing, packaging, and DSA-ready Python idioms</li>
            </ul>
            <Link className="button button--primary" to="/python">
              Begin Track 01&nbsp;→
            </Link>
          </article>
          <article className={styles.trackCard} data-reveal style={{'--reveal-delay': '0.22s'}}>
            <div className={styles.trackNum}>02</div>
            <h3>Data Structures &amp; Algorithms with Python</h3>
            <p>
              24 topics from complexity analysis to segment trees and design
              problems. Every topic has a study guide, a pattern table, and a
              problem ladder with fully worked write-ups.
            </p>
            <ul className={styles.trackList}>
              <li>Arrays, linked lists, stacks, hashing, recursion</li>
              <li>Binary search, trees, heaps, graphs, DP, greedy</li>
              <li>Tries, union-find, Fenwick trees, bit tricks</li>
              <li>Advanced strings, graphs, and data-structure design</li>
            </ul>
            <Link className="button button--primary" to="/dsa">
              Begin Track 02&nbsp;→
            </Link>
          </article>
        </div>
      </div>
    </section>
  );
}

function HowItWorks() {
  return (
    <section className={clsx(styles.section, styles.sectionAlt)}>
      <div className="container">
        <p className={styles.kicker} data-reveal>the loop</p>
        <h2 className={styles.sectionTitle} data-reveal>
          How every topic <em className={styles.em}>actually</em> sticks
        </h2>
        <div className={styles.steps}>
          {[
            {n: '1', t: 'Understand', d: 'Read the notes and study guide. Trace the worked example by hand until the invariant clicks.'},
            {n: '2', t: 'Implement', d: 'Code the core templates without looking. Run the tests in your browser until they go green.'},
            {n: '3', t: 'Drill', d: 'Solve the problem ladder: brute force → optimized → complexity → edge cases, every time.'},
            {n: '4', t: 'Review', d: 'Spaced flashcards and revision checklists convert knowledge into interview-day recall.'},
          ].map((s, i) => (
            <div key={s.n} className={styles.step} data-reveal style={{'--reveal-delay': `${i * 0.12}s`}}>
              <div className={styles.stepNum}>{s.n}</div>
              <h3>{s.t}</h3>
              <p>{s.d}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function FeatureGrid() {
  return (
    <section className={styles.section}>
      <div className="container">
        <p className={styles.kicker} data-reveal>why it works</p>
        <h2 className={styles.sectionTitle} data-reveal>
          Built like a course, not a <em className={styles.em}>dump of notes</em>
        </h2>
        <div className={styles.featureGrid}>
          {FEATURES.map((f, i) => (
            <div key={f.title} className={styles.feature} data-reveal style={{'--reveal-delay': `${(i % 3) * 0.1}s`}}>
              <h3>{f.title}</h3>
              <p>{f.body}</p>
            </div>
          ))}
        </div>
        <div className={styles.startBox} data-reveal>
          <h3>Ready when you are.</h3>
          <p>
            New to programming? Start Track 01. Already comfortable in Python?{' '}
            <Link to="/guides/learning-path">Open the learning path</Link> and
            go straight to the DSA curriculum.
          </p>
          <div className={styles.ctaRow}>
            <Link className="button button--primary button--lg" to="/python">
              Start learning&nbsp;→
            </Link>
            <Link className="button button--secondary button--lg" to="/practice/top-interview-questions">
              Browse practice problems
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <Hero />
      <main>
        <Ticker />
        <TrackCards />
        <HowItWorks />
        <FeatureGrid />
      </main>
    </Layout>
  );
}
