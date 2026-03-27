const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

export default function HomePage() {
  return (
    <main className="container">
      <h1>RMOS</h1>
      <p>Next.js frontend is running.</p>
      <p>
        API base URL: <code>{apiBase}</code>
      </p>
      <a href={`${apiBase}/docs`} target="_blank" rel="noreferrer">
        Open API Docs
      </a>
    </main>
  );
}
