import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './NotFound.module.css';

export default function NotFound() {
  return (
    <Layout title="Page not found" description="This page wandered off the path.">
      <div className={styles.wrap}>
        <p className={styles.code}>404</p>
        <h1 className={styles.title}>This page wandered off the path.</h1>
        <p className={styles.sub}>
          Even the best-planned traversal hits a dead end sometimes. Try one of
          these instead:
        </p>
        <div className={styles.links}>
          <Link className="button button--primary" to="/python">
            Python Track
          </Link>
          <Link className="button button--secondary" to="/dsa">
            DSA Track
          </Link>
          <Link className="button button--outline" to="/">
            Home
          </Link>
        </div>
      </div>
    </Layout>
  );
}
