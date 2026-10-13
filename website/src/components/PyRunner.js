import React, {useRef, useState} from 'react';
import styles from './PyRunner.module.css';

const PYODIDE_VERSION = '0.26.4';
const PYODIDE_BASE = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

let pyodidePromise = null;
function loadPyodideOnce() {
  if (pyodidePromise) return pyodidePromise;
  pyodidePromise = (async () => {
    if (typeof window === 'undefined') throw new Error('browser only');
    if (!window.loadPyodide) {
      await new Promise((resolve, reject) => {
        const s = document.createElement('script');
        s.src = `${PYODIDE_BASE}pyodide.js`;
        s.onload = resolve;
        s.onerror = () => reject(new Error('Could not load Pyodide from CDN.'));
        document.head.appendChild(s);
      });
    }
    return window.loadPyodide({indexURL: PYODIDE_BASE});
  })();
  return pyodidePromise;
}

const RUN_TESTS_PY = `
import io, os, sys, unittest

sys.path.insert(0, os.getcwd())
loader = unittest.TestLoader()
suite = loader.discover(os.getcwd(), pattern='test_*.py')
buf = io.StringIO()
result = unittest.TextTestRunner(stream=buf, verbosity=2).run(suite)
out = buf.getvalue()
print(out)
print(f"=== {result.testsRun} tests run: {len(result.failures)} failed, {len(result.errors)} errors ===")
if result.wasSuccessful():
    print("ALL TESTS PASSED")
`;

/**
 * In-browser Python playground powered by Pyodide.
 *
 * props:
 *  - code: initial user code (editable)
 *  - tests: optional unittest file, run against `module`.py
 *  - module: name of the module the tests import (e.g. "solution", "exercises")
 *  - extraFiles: optional {filename: content} map written alongside
 *  - title: card title
 */
export default function PyRunner({code = '', tests = '', module = 'main', extraFiles = {}, title = 'Python playground'}) {
  const [editor, setEditor] = useState(code);
  const [output, setOutput] = useState('');
  const [status, setStatus] = useState('idle'); // idle | loading | running | ok | fail
  const initialCode = useRef(code);

  async function run(withTests) {
    setStatus('loading');
    setOutput('Loading the Python runtime (first run downloads ~10 MB)…\n');
    try {
      const py = await loadPyodideOnce();
      setStatus('running');
      const chunks = [];
      py.setStdout({batched: (s) => chunks.push(s + '\n')});
      py.setStderr({batched: (s) => chunks.push(s + '\n')});

      const work = '/work';
      py.runPython(`
import shutil, os
shutil.rmtree('${work}', ignore_errors=True)
os.makedirs('${work}', exist_ok=True)
os.chdir('${work}')
`);
      const FS = py.FS;
      FS.writeFile(`${work}/${module}.py`, editor);
      for (const [name, content] of Object.entries(extraFiles)) {
        FS.writeFile(`${work}/${name}`, content);
      }
      if (withTests && tests) {
        // test files are named test_*.py so discovery finds them
        const testName = 'test_suite.py';
        FS.writeFile(`${work}/${testName}`, tests);
      }
      setOutput('Running…\n');
      chunks.length = 0;
      if (withTests) {
        await py.runPythonAsync(RUN_TESTS_PY);
      } else {
        await py.runPythonAsync(editor);
      }
      const text = chunks.join('');
      setOutput(text || '(no output)');
      if (withTests) {
        setStatus(text.includes('ALL TESTS PASSED') ? 'ok' : 'fail');
      } else {
        setStatus('ok');
      }
    } catch (err) {
      setStatus('fail');
      setOutput(String(err && err.message ? err.message : err));
    }
  }

  function reset() {
    setEditor(initialCode.current);
    setOutput('');
    setStatus('idle');
  }

  const statusLabel = {
    idle: 'Ready',
    loading: 'Loading runtime…',
    running: 'Running…',
    ok: tests ? 'Tests passed' : 'Finished',
    fail: tests ? 'Tests failed' : 'Error',
  }[status];

  return (
    <div className={styles.card}>
      <div className={styles.header}>
        <span className={styles.title}>{title}</span>
        <span className={`${styles.status} ${styles['status-' + status]}`}>{statusLabel}</span>
      </div>
      <textarea
        className={styles.editor}
        value={editor}
        spellCheck={false}
        onChange={(e) => setEditor(e.target.value)}
        aria-label="Python code editor"
      />
      <div className={styles.actions}>
        <button className="button button--primary button--sm" onClick={() => run(false)}>
          ▶ Run code
        </button>
        {tests ? (
          <button className="button button--success button--sm" onClick={() => run(true)}>
            ✓ Run tests
          </button>
        ) : null}
        <button className="button button--secondary button--sm" onClick={reset}>
          ↺ Reset
        </button>
        <span className={styles.hint}>Runs in your browser with Pyodide — nothing to install</span>
      </div>
      {output ? (
        <pre className={styles.output}>
          <code>{output}</code>
        </pre>
      ) : null}
    </div>
  );
}
