import React, {useMemo, useState} from 'react';
import styles from './Flashcards.module.css';

/**
 * Interactive flashcard deck. cards: [{q, a}]
 *
 * - click the card to flip it
 * - "again" re-queues the card at the end of the session
 * - "got it" marks it done for this session
 * - "list" tab shows every card expanded for reference
 */
export default function Flashcards({title, cards}) {
  const [order, setOrder] = useState(() => cards.map((_, i) => i));
  const [flipped, setFlipped] = useState(false);
  const [got, setGot] = useState(() => new Set());
  const [againCount, setAgainCount] = useState(0);
  const [view, setView] = useState('cards');

  const currentIdx = order[0];
  const finished = order.length === 0;
  const done = got.size;
  const total = cards.length;

  function rate(understood) {
    setFlipped(false);
    setOrder((prev) => {
      const [head, ...rest] = prev;
      if (understood) {
        setGot((g) => new Set(g).add(head));
        return rest;
      }
      setAgainCount((n) => n + 1);
      return [...rest, head]; // re-queue at the end
    });
  }

  function restart() {
    setOrder(cards.map((_, i) => i));
    setGot(new Set());
    setAgainCount(0);
    setFlipped(false);
  }

  const pct = total ? Math.round((done / total) * 100) : 0;
  const current = useMemo(
    () => (currentIdx === undefined ? null : cards[currentIdx]),
    [currentIdx, cards],
  );

  return (
    <div className={styles.wrap}>
      <div className={styles.header}>
        <span className={styles.title}>{title}</span>
        <div className={styles.tabs} role="tablist">
          <button
            type="button"
            role="tab"
            aria-selected={view === 'cards'}
            className={view === 'cards' ? styles.tabActive : styles.tab}
            onClick={() => setView('cards')}
          >
            cards
          </button>
          <button
            type="button"
            role="tab"
            aria-selected={view === 'list'}
            className={view === 'list' ? styles.tabActive : styles.tab}
            onClick={() => setView('list')}
          >
            list
          </button>
        </div>
      </div>

      <div className={styles.progressRow}>
        <div className={styles.bar}>
          <div className={styles.fill} style={{width: `${pct}%`}} />
        </div>
        <span className={styles.count}>
          {done}/{total} got it{againCount ? ` · ${againCount} again` : ''}
        </span>
      </div>

      {view === 'list' ? (
        <dl className={styles.list}>
          {cards.map((c, i) => (
            <div key={i} className={styles.listItem}>
              <dt>{c.q}</dt>
              <dd>{c.a}</dd>
            </div>
          ))}
        </dl>
      ) : finished ? (
        <div className={styles.done}>
          <p className={styles.doneEmoji}>🎉</p>
          <p className={styles.doneText}>
            Session complete — <strong>{done}/{total}</strong> on the first pass
            {againCount ? `, ${againCount} re-queued` : ''}.
          </p>
          <button type="button" className="button button--primary button--sm" onClick={restart}>
            ↺ go again
          </button>
        </div>
      ) : (
        <>
          <div
            className={flipped ? `${styles.card} ${styles.cardFlipped}` : styles.card}
            onClick={() => setFlipped((f) => !f)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                setFlipped((f) => !f);
              }
            }}
            role="button"
            tabIndex={0}
            aria-label="Flip card"
          >
            <div className={styles.cardInner}>
              <div className={styles.face}>
                <span className={styles.faceLabel}>question</span>
                <p className={styles.qText}>{current.q}</p>
                <span className={styles.flipHint}>click to reveal ↻</span>
              </div>
              <div className={styles.faceBack}>
                <span className={styles.faceLabel}>answer</span>
                <p className={styles.aText}>{current.a}</p>
                <span className={styles.flipHint}>click to flip back ↻</span>
              </div>
            </div>
          </div>
          <div className={styles.rateRow}>
            <button
              type="button"
              className={`button button--secondary button--sm ${styles.againBtn}`}
              disabled={!flipped}
              onClick={() => rate(false)}
            >
              ↺ again
            </button>
            <button
              type="button"
              className="button button--primary button--sm"
              disabled={!flipped}
              onClick={() => rate(true)}
            >
              ✓ got it
            </button>
          </div>
        </>
      )}
    </div>
  );
}
