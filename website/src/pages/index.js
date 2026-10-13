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
      <div className="container">
        <h1 className={styles.heroTitle}>
          Python <span className={styles.grad}>DSA Masterclass</span>
        </h1>
        <p className={styles.heroSub}>
          A complete, hands-on course — from your first Python program to
          top-tier interview readiness. Two tracks, interactive exercises, and a
          curriculum built on patterns and proofs.
        </p>
        <div className={styles.ctaRow}>
          <Link className="button button--primary button--lg" to="/python">
            Start with Python →
          </Link>
          <Link className="button button--outline button--lg" to="/dsa">
            Jump to DSA Track
          </Link>
        </div>
        <div className={styles.stats}>
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

function TrackCards() {
  return (
    <section className={styles.section}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Choose your track</h2>
        <div className={styles.trackGrid}>
          <div className={styles.trackCard}>
            <div className={styles.trackTag}>Track 1</div>
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
              Begin Track 1
            </Link>
          </div>
          <div className={styles.trackCard}>
            <div className={styles.trackTag}>Track 2</div>
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
              Begin Track 2
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

function HowItWorks() {
  return (
    <section className={clsx(styles.section, styles.sectionAlt)}>
      <div className="container">
        <h2 className={styles.sectionTitle}>How every topic works</h2>
        <div className={styles.steps}>
          <div className={styles.step}>
            <div className={styles.stepNum}>1</div>
            <h3>Understand</h3>
            <p>Read the notes and study guide. Trace the worked example by hand until the invariant clicks.</p>
          </div>
          <div className={styles.step}>
            <div className={styles.stepNum}>2</div>
            <h3>Implement</h3>
            <p>Code the core templates without looking. Run the tests in your browser until they go green.</p>
          </div>
          <div className={styles.step}>
            <div className={styles.stepNum}>3</div>
            <h3>Drill</h3>
            <p>Solve the problem ladder: brute force → optimized → complexity → edge cases, every time.</p>
          </div>
          <div className={styles.step}>
            <div className={styles.stepNum}>4</div>
            <h3>Review</h3>
            <p>Spaced flashcards and revision checklists convert knowledge into interview-day recall.</p>
          </div>
        </div>
      </div>
    </section>
  );
}

function FeatureGrid() {
  return (
    <section className={styles.section}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Built like a course, not a dump of notes</h2>
        <div className={styles.featureGrid}>
          {FEATURES.map((f) => (
            <div key={f.title} className={styles.feature}>
              <h3>{f.title}</h3>
              <p>{f.body}</p>
            </div>
          ))}
        </div>
        <div className={styles.startBox}>
          <h3>Ready?</h3>
          <p>
            New to programming? Start Track 1. Already comfortable in Python?{' '}
            <Link to="/guides/learning-path">Open the learning path</Link> and
            go straight to the DSA curriculum.
          </p>
          <div className={styles.ctaRow}>
            <Link className="button button--primary button--lg" to="/python">
              Start learning
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
        <TrackCards />
        <HowItWorks />
        <FeatureGrid />
      </main>
    </Layout>
  );
}
