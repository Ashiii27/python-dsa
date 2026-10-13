import React, {useEffect, useState} from 'react';
import styles from './TrackProgress.module.css';

function storageKey(track) {
  return `pds-progress-${track}`;
}

/**
 * Persistent checklist of track items (localStorage).
 * items: [{id, title, href}]
 */
export default function TrackProgress({track, items}) {
  const [done, setDone] = useState(null); // null until hydrated

  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(storageKey(track));
      setDone(raw ? new Set(JSON.parse(raw)) : new Set());
    } catch {
      setDone(new Set());
    }
  }, [track]);

  function toggle(id) {
    setDone((prev) => {
      const next = new Set(prev || []);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        window.localStorage.setItem(storageKey(track), JSON.stringify([...next]));
      } catch {
        /* private mode etc. */
      }
      return next;
    });
  }

  function reset() {
    setDone(new Set());
    try {
      window.localStorage.removeItem(storageKey(track));
    } catch {
      /* ignore */
    }
  }

  const finished = done ? items.filter((i) => done.has(i.id)).length : 0;
  const pct = items.length ? Math.round((finished / items.length) * 100) : 0;

  return (
    <div className={styles.wrap}>
      <div className={styles.top}>
        <div className={styles.barWrap}>
          <div className={styles.bar}>
            <div className={styles.fill} style={{width: `${pct}%`}} />
          </div>
          <span className={styles.count}>
            {finished}/{items.length} complete ({pct}%)
          </span>
        </div>
        <button className="button button--secondary button--sm" onClick={reset}>
          Reset
        </button>
      </div>
      <ul className={styles.list}>
        {items.map((item) => {
          const checked = !!(done && done.has(item.id));
          return (
            <li key={item.id} className={styles.item}>
              <label className={styles.label}>
                <input
                  type="checkbox"
                  checked={checked}
                  onChange={() => toggle(item.id)}
                />
                <a
                  href={item.href}
                  className={checked ? styles.doneLink : styles.link}
                >
                  {item.title}
                </a>
              </label>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
