import React, {useEffect, useState} from 'react';
import styles from './SelfCheck.module.css';

function key(id) {
  return `pds-selfcheck-${id}`;
}

/**
 * Active-recall checkpoint list. items: [{q, hint?}]
 * Ticks persist in localStorage per lesson.
 */
export default function SelfCheck({id, items}) {
  const [done, setDone] = useState(null);
  const [hints, setHints] = useState(() => new Set());

  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(key(id));
      setDone(raw ? new Set(JSON.parse(raw)) : new Set());
    } catch {
      setDone(new Set());
    }
  }, [id]);

  function toggle(i) {
    setDone((prev) => {
      const next = new Set(prev || []);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      try {
        window.localStorage.setItem(key(id), JSON.stringify([...next]));
      } catch {
        /* ignore */
      }
      return next;
    });
  }

  function toggleHint(i) {
    setHints((prev) => {
      const next = new Set(prev);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      return next;
    });
  }

  function reset() {
    setDone(new Set());
    try {
      window.localStorage.removeItem(key(id));
    } catch {
      /* ignore */
    }
  }

  const confident = done ? items.filter((_, i) => done.has(i)).length : 0;
  const all = done && confident === items.length;

  return (
    <div className={styles.wrap}>
      <ul className={styles.list}>
        {items.map((item, i) => {
          const checked = !!(done && done.has(i));
          return (
            <li key={i} className={styles.item}>
              <div className={styles.row}>
                <span className={styles.num}>{i + 1}</span>
                <p className={checked ? styles.qDone : styles.q}>{item.q}</p>
                <div className={styles.actions}>
                  {item.hint ? (
                    <button
                      type="button"
                      className={styles.hintBtn}
                      onClick={() => toggleHint(i)}
                      aria-expanded={hints.has(i)}
                    >
                      {hints.has(i) ? 'hide hint' : 'hint'}
                    </button>
                  ) : null}
                  <label className={styles.checkLabel}>
                    <input
                      type="checkbox"
                      checked={checked}
                      onChange={() => toggle(i)}
                    />
                    can answer
                  </label>
                </div>
              </div>
              {item.hint && hints.has(i) ? (
                <p className={styles.hint}>{item.hint}</p>
              ) : null}
            </li>
          );
        })}
      </ul>
      <div className={styles.footer}>
        <span className={all ? styles.countAll : styles.count}>
          {all ? '✓ all checkpoints clear — ' : ''}
          {confident}/{items.length} confident
        </span>
        <button type="button" className={styles.reset} onClick={reset}>
          reset
        </button>
      </div>
    </div>
  );
}
