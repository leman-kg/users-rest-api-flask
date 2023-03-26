import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import Link from 'next/link'

export default function App({ Component, pageProps }: AppProps) {
  <nav className="header-nav">
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/users/add">New User</Link>
      </li>
    </ul>
  </nav>
  return <Component {...pageProps} />
}
