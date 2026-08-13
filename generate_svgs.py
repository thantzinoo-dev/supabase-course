import os

os.makedirs("images", exist_ok=True)

# Common styling definitions
SVG_HEADER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#0b0f19; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; border-radius:12px; overflow:hidden;">
  <defs>
    <linearGradient id="bg-card" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="grad-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="grad-green" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="grad-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
    <linearGradient id="grad-amber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="grad-rose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
    <linearGradient id="grad-blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#38bdf8" flood-opacity="0.3"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
    <marker id="arrow-cyan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fb7185"/>
    </marker>
  </defs>
  <!-- Background Pattern Grid -->
  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1e293b" stroke-width="0.5" stroke-opacity="0.5"/>
  </pattern>
  <rect width="100%" height="100%" fill="url(#grid)"/>
'''

def save_svg(filename, content):
    with open(os.path.join("images", filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated images/{filename}")

# 1. 01-diy-flow.svg
svg_01_diy = SVG_HEADER.format(width=900, height=180) + '''
  <text x="30" y="38" fill="#94a3b8" font-size="13" font-weight="600" letter-spacing="1">TRADITIONAL DIY ARCHITECTURE</text>
  
  <!-- Flow nodes -->
  <!-- User -->
  <g transform="translate(30, 60)" filter="url(#shadow)">
    <rect width="110" height="70" rx="10" fill="url(#bg-card)" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="55" y="32" fill="#60a5fa" font-size="18" text-anchor="middle">👤</text>
    <text x="55" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">User / Client</text>
  </g>
  <line x1="140" y1="95" x2="168" y2="95" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Express API -->
  <g transform="translate(170, 60)" filter="url(#shadow)">
    <rect width="120" height="70" rx="10" fill="url(#bg-card)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="60" y="32" fill="#fbbf24" font-size="18" text-anchor="middle">🚀</text>
    <text x="60" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">Express API</text>
  </g>
  <line x1="290" y1="95" x2="318" y2="95" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Controller -->
  <g transform="translate(320, 60)" filter="url(#shadow)">
    <rect width="110" height="70" rx="10" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <text x="55" y="32" fill="#94a3b8" font-size="18" text-anchor="middle">⚙️</text>
    <text x="55" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">Controller</text>
  </g>
  <line x1="430" y1="95" x2="458" y2="95" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Service -->
  <g transform="translate(460, 60)" filter="url(#shadow)">
    <rect width="110" height="70" rx="10" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <text x="55" y="32" fill="#94a3b8" font-size="18" text-anchor="middle">💼</text>
    <text x="55" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">Service Layer</text>
  </g>
  <line x1="570" y1="95" x2="598" y2="95" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- ORM -->
  <g transform="translate(600, 60)" filter="url(#shadow)">
    <rect width="120" height="70" rx="10" fill="url(#bg-card)" stroke="#a855f7" stroke-width="1.5"/>
    <text x="60" y="32" fill="#c084fc" font-size="18" text-anchor="middle">🗄️</text>
    <text x="60" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">ORM / Query</text>
  </g>
  <line x1="720" y1="95" x2="748" y2="95" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Postgres -->
  <g transform="translate(750, 60)" filter="url(#shadow)">
    <rect width="120" height="70" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="32" fill="#38bdf8" font-size="18" text-anchor="middle">🐘</text>
    <text x="60" y="52" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Postgres DB</text>
  </g>
</svg>'''
save_svg("01-diy-flow.svg", svg_01_diy)

# 2. 01-supabase-flow.svg
svg_01_supa = SVG_HEADER.format(width=900, height=180) + '''
  <text x="30" y="38" fill="#34d399" font-size="13" font-weight="600" letter-spacing="1">SUPABASE MANAGED ARCHITECTURE</text>
  
  <!-- User -->
  <g transform="translate(30, 60)" filter="url(#shadow)">
    <rect width="120" height="70" rx="10" fill="url(#bg-card)" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="60" y="32" font-size="18" text-anchor="middle">👤</text>
    <text x="60" y="52" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">User / Client</text>
  </g>
  <line x1="150" y1="95" x2="188" y2="95" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- SDK -->
  <g transform="translate(190, 60)" filter="url(#shadow)">
    <rect width="150" height="70" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="75" y="32" font-size="18" text-anchor="middle">📦</text>
    <text x="75" y="52" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">Supabase SDK</text>
  </g>
  <line x1="340" y1="95" x2="378" y2="95" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- Kong API Gateway -->
  <g transform="translate(380, 60)" filter="url(#shadow)">
    <rect width="150" height="70" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="75" y="32" font-size="18" text-anchor="middle">🌐</text>
    <text x="75" y="52" fill="#38bdf8" font-size="13" font-weight="600" text-anchor="middle">Kong Gateway</text>
  </g>
  <line x1="530" y1="95" x2="568" y2="95" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- Services -->
  <g transform="translate(570, 60)" filter="url(#shadow)">
    <rect width="150" height="70" rx="10" fill="url(#bg-card)" stroke="#c084fc" stroke-width="1.5"/>
    <text x="75" y="30" font-size="16" text-anchor="middle">⚡ 🔐 📦 📡</text>
    <text x="75" y="52" fill="#c084fc" font-size="12" font-weight="600" text-anchor="middle">Managed Services</text>
  </g>
  <line x1="720" y1="95" x2="748" y2="95" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- Postgres -->
  <g transform="translate(750, 60)" filter="url(#shadow)">
    <rect width="120" height="70" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <text x="60" y="32" font-size="18" text-anchor="middle">🐘</text>
    <text x="60" y="52" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Postgres DB</text>
  </g>
</svg>'''
save_svg("01-supabase-flow.svg", svg_01_supa)

# 3. 01-supabase-architecture.svg
svg_01_arch = SVG_HEADER.format(width=900, height=480) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">SUPABASE ARCHITECTURE &amp; SERVICES</text>
  
  <!-- Kong Gateway (Top) -->
  <g transform="translate(250, 55)" filter="url(#shadow)">
    <rect width="400" height="60" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="28" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">🌐 Kong API Gateway</text>
    <text x="200" y="47" fill="#94a3b8" font-size="11" text-anchor="middle">API Routing • Rate Limiting • Auth Header Verification</text>
  </g>

  <!-- Distribution Lines from Kong -->
  <path d="M 450 115 L 450 150 M 90 150 L 810 150 
           M 90 150 L 90 180 M 235 150 L 235 180 M 380 150 L 380 180 
           M 525 150 L 525 180 M 670 150 L 670 180 M 810 150 L 810 180" 
        fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Service 1: GoTrue -->
  <g transform="translate(25, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#fb7185" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">🔐</text>
    <text x="65" y="55" fill="#fb7185" font-size="13" font-weight="700" text-anchor="middle">GoTrue</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">Auth &amp; JWT</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">OAuth / Password</text>
  </g>

  <!-- Service 2: PostgREST -->
  <g transform="translate(170, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">⚡</text>
    <text x="65" y="55" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">PostgREST</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">Auto REST API</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">Table to CRUD</text>
  </g>

  <!-- Service 3: Realtime -->
  <g transform="translate(315, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">📡</text>
    <text x="65" y="55" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Realtime</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">WebSockets</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">Elixir Server</text>
  </g>

  <!-- Service 4: Storage -->
  <g transform="translate(460, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">📦</text>
    <text x="65" y="55" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Storage</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">S3-Compatible</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">Images / Files</text>
  </g>

  <!-- Service 5: Functions -->
  <g transform="translate(605, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#c084fc" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">🚀</text>
    <text x="65" y="55" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">Edge Functions</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">Deno Serverless</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">TypeScript/JS</text>
  </g>

  <!-- Service 6: postgres_meta -->
  <g transform="translate(750, 180)" filter="url(#shadow)">
    <rect width="130" height="110" rx="10" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <text x="65" y="32" font-size="20" text-anchor="middle">⚙️</text>
    <text x="65" y="55" fill="#94a3b8" font-size="13" font-weight="700" text-anchor="middle">postgres_meta</text>
    <text x="65" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">Schema API</text>
    <text x="65" y="93" fill="#64748b" font-size="10" text-anchor="middle">Dashboard Tool</text>
  </g>

  <!-- Convergence to Postgres -->
  <path d="M 90 290 L 90 320 M 235 290 L 235 320 M 380 290 L 380 320 
           M 525 290 L 525 320 M 670 290 L 670 320 M 810 290 L 810 320
           M 90 320 L 810 320 M 450 320 L 450 350" 
        fill="none" stroke="#34d399" stroke-width="1.5"/>

  <!-- Postgres Database (Bottom) -->
  <g transform="translate(250, 350)" filter="url(#shadow)">
    <rect width="400" height="85" rx="12" fill="url(#bg-card)" stroke="#34d399" stroke-width="2.5"/>
    <text x="200" y="34" fill="#34d399" font-size="18" font-weight="700" text-anchor="middle">🐘 PostgreSQL Database Engine</text>
    <text x="200" y="58" fill="#f8fafc" font-size="12" text-anchor="middle">Core Relational Database • Row Level Security (RLS) • WAL Stream</text>
    <text x="200" y="74" fill="#94a3b8" font-size="11" text-anchor="middle">SQL Queries • Triggers • Extensions (pgvector, uuid-ossp)</text>
  </g>
</svg>'''
save_svg("01-supabase-architecture.svg", svg_01_arch)

# 4. 01-flutter-architecture.svg
svg_01_flutter = SVG_HEADER.format(width=900, height=280) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">CLIENT INTEGRATION &amp; ROUTING</text>
  
  <!-- Flutter App -->
  <g transform="translate(40, 70)" filter="url(#shadow)">
    <rect width="180" height="150" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="45" font-size="28" text-anchor="middle">📱</text>
    <text x="90" y="75" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Flutter App</text>
    <text x="90" y="100" fill="#94a3b8" font-size="11" text-anchor="middle">supabase_flutter SDK</text>
    <rect x="25" y="115" width="130" height="22" rx="6" fill="#1e293b"/>
    <text x="90" y="130" fill="#34d399" font-size="10" font-family="monospace" text-anchor="middle">Supabase.initialize()</text>
  </g>

  <!-- Arrow -->
  <path d="M 220 145 L 300 145" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <text x="260" y="135" fill="#94a3b8" font-size="10" text-anchor="middle">HTTP / WS</text>

  <!-- Kong Gateway -->
  <g transform="translate(310, 70)" filter="url(#shadow)">
    <rect width="200" height="150" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="45" font-size="28" text-anchor="middle">☁️</text>
    <text x="100" y="75" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Supabase Cloud</text>
    <text x="100" y="98" fill="#f8fafc" font-size="12" text-anchor="middle">Kong API Gateway</text>
    <text x="100" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">Route by path prefix</text>
    <text x="100" y="142" fill="#64748b" font-size="10" font-family="monospace" text-anchor="middle">/auth, /rest, /realtime</text>
  </g>

  <!-- Branching Arrows -->
  <path d="M 510 100 L 590 85" stroke="#fb7185" stroke-width="1.5" marker-end="url(#arrow-rose)"/>
  <path d="M 510 130 L 590 120" stroke="#34d399" stroke-width="1.5" marker-end="url(#arrow-green)"/>
  <path d="M 510 160 L 590 155" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrow-cyan)"/>
  <path d="M 510 190 L 590 190" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Target Services -->
  <g transform="translate(600, 60)" filter="url(#shadow)">
    <rect width="260" height="36" rx="8" fill="url(#bg-card)" stroke="#fb7185" stroke-width="1"/>
    <text x="130" y="23" fill="#fb7185" font-size="12" font-weight="600" text-anchor="middle">🔐 GoTrue (Auth &amp; Session)</text>
  </g>
  <g transform="translate(600, 102)" filter="url(#shadow)">
    <rect width="260" height="36" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="1"/>
    <text x="130" y="23" fill="#34d399" font-size="12" font-weight="600" text-anchor="middle">⚡ PostgREST (Auto CRUD Queries)</text>
  </g>
  <g transform="translate(600, 144)" filter="url(#shadow)">
    <rect width="260" height="36" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1"/>
    <text x="130" y="23" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">📡 Realtime (Live Subscriptions)</text>
  </g>
  <g transform="translate(600, 186)" filter="url(#shadow)">
    <rect width="260" height="36" rx="8" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1"/>
    <text x="130" y="23" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">📦 Storage (File &amp; Image Uploads)</text>
  </g>
</svg>'''
save_svg("01-flutter-architecture.svg", svg_01_flutter)

# 5. 01-request-sequence.svg
svg_01_seq = SVG_HEADER.format(width=900, height=360) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">REQUEST LIFECYCLE: supabase.from('recipes').select()</text>
  
  <!-- Lifelines -->
  <g transform="translate(100, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="70" y="25" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">📱 Flutter App</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(340, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="70" y="25" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">🌐 Kong Gateway</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(560, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="70" y="25" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">⚡ PostgREST</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(760, 60)">
    <rect width="120" height="40" rx="8" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="60" y="25" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">🐘 Postgres DB</text>
    <line x1="60" y1="40" x2="60" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <!-- Step 1 -->
  <line x1="170" y1="130" x2="400" y2="130" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <rect x="180" y="112" width="210" height="20" rx="4" fill="#0f172a"/>
  <text x="285" y="126" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">1. GET /rest/v1/recipes</text>

  <!-- Step 2 -->
  <line x1="410" y1="165" x2="620" y2="165" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="430" y="147" width="170" height="20" rx="4" fill="#0f172a"/>
  <text x="515" y="161" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">2. Route to PostgREST</text>

  <!-- Step 3 -->
  <line x1="630" y1="200" x2="810" y2="200" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
  <rect x="640" y="182" width="160" height="20" rx="4" fill="#0f172a"/>
  <text x="720" y="196" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">3. SELECT * FROM recipes</text>

  <!-- Step 4 -->
  <line x1="820" y1="235" x2="640" y2="235" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
  <text x="730" y="228" fill="#fbbf24" font-size="10" text-anchor="middle">4. Table Rows</text>

  <!-- Step 5 -->
  <line x1="630" y1="260" x2="420" y2="260" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
  <text x="525" y="253" fill="#34d399" font-size="10" text-anchor="middle">5. JSON Array</text>

  <!-- Step 6 -->
  <line x1="410" y1="285" x2="180" y2="285" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <rect x="200" y="270" width="190" height="20" rx="4" fill="#0f172a"/>
  <text x="295" y="284" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">6. 200 OK (Recipes JSON)</text>
</svg>'''
save_svg("01-request-sequence.svg", svg_01_seq)

# 6. 02-api-keys-security.svg
svg_02_keys = SVG_HEADER.format(width=900, height=380) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">SUPABASE API KEYS &amp; SECURITY BOUNDARIES</text>
  
  <!-- Left Side: Public Zone -->
  <g transform="translate(40, 65)" filter="url(#shadow)">
    <rect width="380" height="230" rx="14" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="20" y="20" width="340" height="35" rx="8" fill="#0369a1" fill-opacity="0.3"/>
    <text x="190" y="42" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">📱 PUBLIC FRONTEND CLIENT</text>
    
    <text x="30" y="85" fill="#f8fafc" font-size="14" font-weight="600">Key: sb_publishable_... (or anon)</text>
    <text x="30" y="110" fill="#94a3b8" font-size="12">• Used in Flutter app, Next.js browser bundle</text>
    <text x="30" y="130" fill="#94a3b8" font-size="12">• Client extracts can NEVER be prevented</text>
    
    <!-- Security Box -->
    <rect x="25" y="150" width="330" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="40" y="173" fill="#34d399" font-size="13" font-weight="700">🛡️ Row Level Security (RLS) Enforced</text>
    <text x="40" y="193" fill="#94a3b8" font-size="11">Only permitted rows are returned to the user</text>
  </g>

  <!-- Right Side: Server Zone -->
  <g transform="translate(480, 65)" filter="url(#shadow)">
    <rect width="380" height="230" rx="14" fill="url(#bg-card)" stroke="#fb7185" stroke-width="1.5"/>
    <rect x="20" y="20" width="340" height="35" rx="8" fill="#be123c" fill-opacity="0.3"/>
    <text x="190" y="42" fill="#fb7185" font-size="13" font-weight="700" text-anchor="middle">🔒 TRUSTED BACKEND SERVER</text>
    
    <text x="30" y="85" fill="#f8fafc" font-size="14" font-weight="600">Key: sb_secret_... (or service_role)</text>
    <text x="30" y="110" fill="#94a3b8" font-size="12">• Used ONLY in secure server environments</text>
    <text x="30" y="130" fill="#94a3b8" font-size="12">• Edge Functions, secure Node.js scripts</text>
    
    <!-- Warning Box -->
    <rect x="25" y="150" width="330" height="55" rx="8" fill="#1e293b" stroke="#fb7185" stroke-width="1.5"/>
    <text x="40" y="173" fill="#fb7185" font-size="13" font-weight="700">⚠️ Bypasses RLS Completely (Full Admin)</text>
    <text x="40" y="193" fill="#fb7185" font-size="11">NEVER put this in Flutter / Client code or GitHub!</text>
  </g>

  <!-- Bottom Callout -->
  <g transform="translate(40, 315)">
    <rect width="820" height="40" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="410" y="25" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">💡 Golden Rule: Client-side secret key leak = Total Database Compromise. Always rely on RLS with Publishable Key.</text>
  </g>
</svg>'''
save_svg("02-api-keys-security.svg", svg_02_keys)

# 7. 03-relationship-map.svg
svg_03_er = SVG_HEADER.format(width=900, height=440) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">MONT-SHA DATABASE SCHEMA &amp; RELATIONSHIPS</text>
  
  <!-- auth.users -->
  <g transform="translate(40, 65)" filter="url(#shadow)">
    <rect width="240" height="120" rx="10" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <rect x="0" y="0" width="240" height="32" rx="10" fill="#334155" fill-opacity="0.5"/>
    <text x="15" y="21" fill="#94a3b8" font-size="13" font-weight="700">🔐 auth.users (Supabase Auth)</text>
    <text x="15" y="55" fill="#38bdf8" font-size="12" font-family="monospace">PK  id (uuid)</text>
    <text x="15" y="75" fill="#cbd5e1" font-size="12" font-family="monospace">    email (text)</text>
    <text x="15" y="95" fill="#64748b" font-size="11">Managed by GoTrue</text>
  </g>

  <!-- 1:1 connector -->
  <path d="M 280 120 L 340 120" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <text x="310" y="112" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">1 : 1</text>

  <!-- public.profiles -->
  <g transform="translate(340, 65)" filter="url(#shadow)">
    <rect width="250" height="150" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="32" rx="10" fill="#0369a1" fill-opacity="0.3"/>
    <text x="15" y="21" fill="#38bdf8" font-size="13" font-weight="700">📋 public.profiles</text>
    <text x="15" y="55" fill="#38bdf8" font-size="12" font-family="monospace">PK,FK id (uuid)</text>
    <text x="15" y="75" fill="#cbd5e1" font-size="12" font-family="monospace">      display_name (text)</text>
    <text x="15" y="95" fill="#cbd5e1" font-size="12" font-family="monospace">      avatar_path (text)</text>
    <text x="15" y="115" fill="#cbd5e1" font-size="12" font-family="monospace">      created_at (timestamptz)</text>
  </g>

  <!-- 1:N connector (Profiles to Recipes) -->
  <path d="M 465 215 L 465 270" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
  <text x="480" y="245" fill="#34d399" font-size="11" font-weight="700">1 : N</text>

  <!-- public.recipes -->
  <g transform="translate(340, 270)" filter="url(#shadow)">
    <rect width="250" height="150" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="32" rx="10" fill="#065f46" fill-opacity="0.4"/>
    <text x="15" y="21" fill="#34d399" font-size="13" font-weight="700">🍲 public.recipes</text>
    <text x="15" y="52" fill="#34d399" font-size="11" font-family="monospace">PK  id (uuid)</text>
    <text x="15" y="70" fill="#38bdf8" font-size="11" font-family="monospace">FK  author_id (uuid)</text>
    <text x="15" y="88" fill="#cbd5e1" font-size="11" font-family="monospace">    title (text), desc (text)</text>
    <text x="15" y="106" fill="#cbd5e1" font-size="11" font-family="monospace">    ingredients, steps (jsonb)</text>
    <text x="15" y="124" fill="#cbd5e1" font-size="11" font-family="monospace">    is_published (bool)</text>
  </g>

  <!-- 1:N connector (Recipes to Comments) -->
  <path d="M 590 345 L 650 345" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="620" y="335" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">1 : N</text>

  <!-- 1:N connector (Profiles to Comments) -->
  <path d="M 590 140 L 760 140 L 760 270" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
  <text x="680" y="130" fill="#fbbf24" font-size="11">author_id (1 : N)</text>

  <!-- public.comments -->
  <g transform="translate(650, 270)" filter="url(#shadow)">
    <rect width="220" height="150" rx="10" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#78350f" fill-opacity="0.4"/>
    <text x="15" y="21" fill="#fbbf24" font-size="13" font-weight="700">💬 public.comments</text>
    <text x="15" y="52" fill="#fbbf24" font-size="11" font-family="monospace">PK  id (uuid)</text>
    <text x="15" y="70" fill="#34d399" font-size="11" font-family="monospace">FK  recipe_id (uuid)</text>
    <text x="15" y="88" fill="#38bdf8" font-size="11" font-family="monospace">FK  author_id (uuid)</text>
    <text x="15" y="106" fill="#cbd5e1" font-size="11" font-family="monospace">    body (text)</text>
    <text x="15" y="124" fill="#cbd5e1" font-size="11" font-family="monospace">    created_at (timestamptz)</text>
  </g>
</svg>'''
save_svg("03-relationship-map.svg", svg_03_er)

# 8. 04-rls-flow.svg
svg_04_rls = SVG_HEADER.format(width=900, height=320) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">ROW LEVEL SECURITY (RLS) EVALUATION ENGINE</text>
  
  <!-- Client -->
  <g transform="translate(40, 100)" filter="url(#shadow)">
    <rect width="180" height="110" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="40" font-size="24" text-anchor="middle">📱</text>
    <text x="90" y="65" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Client Query</text>
    <text x="90" y="85" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">JWT Header Attached</text>
  </g>

  <!-- Arrow -->
  <path d="M 220 155 L 290 155" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

  <!-- Gateway / RLS Core -->
  <g transform="translate(290, 75)" filter="url(#shadow)">
    <rect width="260" height="160" rx="14" fill="url(#bg-card)" stroke="#a855f7" stroke-width="2"/>
    <text x="130" y="35" font-size="24" text-anchor="middle">🔒</text>
    <text x="130" y="62" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">PostgreSQL RLS Engine</text>
    <rect x="20" y="80" width="220" height="60" rx="8" fill="#1e293b"/>
    <text x="130" y="102" fill="#94a3b8" font-size="11" text-anchor="middle">Evaluates SQL Policy Rule:</text>
    <text x="130" y="122" fill="#38bdf8" font-size="11" font-family="monospace" text-anchor="middle">(select auth.uid()) = author_id</text>
  </g>

  <!-- Branch Pass -->
  <path d="M 550 125 L 630 100" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
  <text x="590" y="105" fill="#34d399" font-size="11" font-weight="700">PASS</text>

  <!-- Result Pass -->
  <g transform="translate(640, 65)" filter="url(#shadow)">
    <rect width="220" height="80" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <text x="25" y="32" font-size="18">✅</text>
    <text x="55" y="32" fill="#34d399" font-size="13" font-weight="700">Query Allowed</text>
    <text x="25" y="55" fill="#cbd5e1" font-size="11">Returns requested rows or</text>
    <text x="25" y="70" fill="#cbd5e1" font-size="11">executes mutation (insert/update)</text>
  </g>

  <!-- Branch Fail -->
  <path d="M 550 185 L 630 210" stroke="#fb7185" stroke-width="2" marker-end="url(#arrow-rose)"/>
  <text x="590" y="210" fill="#fb7185" font-size="11" font-weight="700">FAIL</text>

  <!-- Result Fail -->
  <g transform="translate(640, 165)" filter="url(#shadow)">
    <rect width="220" height="80" rx="10" fill="url(#bg-card)" stroke="#fb7185" stroke-width="2"/>
    <text x="25" y="32" font-size="18">❌</text>
    <text x="55" y="32" fill="#fb7185" font-size="13" font-weight="700">Access Denied</text>
    <text x="25" y="55" fill="#cbd5e1" font-size="11">Returns empty rows (0 results)</text>
    <text x="25" y="70" fill="#cbd5e1" font-size="11">or throws 403 Forbidden</text>
  </g>
</svg>'''
save_svg("04-rls-flow.svg", svg_04_rls)

# 9. 06-auth-trigger-flow.svg
svg_06_auth = SVG_HEADER.format(width=900, height=360) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">USER SIGNUP &amp; PROFILE AUTO-CREATION TRIGGER</text>
  
  <!-- Lifelines -->
  <g transform="translate(60, 60)">
    <rect width="130" height="40" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="65" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">📱 Flutter / Web</text>
    <line x1="65" y1="40" x2="65" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(260, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#fb7185" stroke-width="1.5"/>
    <text x="70" y="25" fill="#fb7185" font-size="12" font-weight="700" text-anchor="middle">🔐 GoTrue Auth</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(470, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <text x="70" y="25" fill="#94a3b8" font-size="12" font-weight="700" text-anchor="middle">🗄️ auth.users</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(680, 60)">
    <rect width="160" height="40" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="80" y="25" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">📋 public.profiles</text>
    <line x1="80" y1="40" x2="80" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <!-- Step 1 -->
  <line x1="125" y1="125" x2="320" y2="125" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <rect x="135" y="108" width="180" height="20" rx="4" fill="#0f172a"/>
  <text x="225" y="122" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">1. supabase.auth.signUp()</text>

  <!-- Step 2 -->
  <line x1="330" y1="160" x2="530" y2="160" stroke="#fb7185" stroke-width="2" marker-end="url(#arrow-rose)"/>
  <rect x="350" y="143" width="160" height="20" rx="4" fill="#0f172a"/>
  <text x="430" y="157" fill="#fb7185" font-size="11" font-weight="600" text-anchor="middle">2. INSERT new user row</text>

  <!-- Step 3: Trigger -->
  <line x1="540" y1="200" x2="750" y2="200" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
  <rect x="550" y="180" width="190" height="24" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
  <text x="645" y="196" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">⚡ Trigger: handle_new_user()</text>

  <!-- Step 4 -->
  <line x1="760" y1="235" x2="540" y2="235" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
  <text x="650" y="228" fill="#cbd5e1" font-size="10" text-anchor="middle">Profile row created</text>

  <!-- Step 5 -->
  <line x1="330" y1="270" x2="135" y2="270" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <rect x="145" y="253" width="170" height="20" rx="4" fill="#0f172a"/>
  <text x="230" y="267" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">5. Return User + JWT Session</text>
</svg>'''
save_svg("06-auth-trigger-flow.svg", svg_06_auth)

# 10. 07-storage-structure.svg
svg_07_store = SVG_HEADER.format(width=900, height=320) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">STORAGE BUCKET HIERARCHY &amp; UPLOAD PIPELINE</text>
  
  <!-- Left Side: Folder Hierarchy -->
  <g transform="translate(40, 65)" filter="url(#shadow)">
    <rect width="380" height="225" rx="12" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="0" y="0" width="380" height="35" rx="12" fill="#78350f" fill-opacity="0.3"/>
    <text x="20" y="23" fill="#fbbf24" font-size="13" font-weight="700">🪣 Bucket: recipe-images (Public)</text>
    
    <!-- Tree View -->
    <g transform="translate(30, 55)">
      <text x="0" y="20" fill="#38bdf8" font-size="14" font-family="monospace">📁 &lt;user_id&gt;/</text>
      <text x="140" y="20" fill="#64748b" font-size="11">(User UUID - matches auth.uid)</text>
      
      <text x="30" y="55" fill="#38bdf8" font-size="14" font-family="monospace">└── 📁 &lt;recipe_id&gt;/</text>
      <text x="200" y="55" fill="#64748b" font-size="11">(Recipe UUID)</text>
      
      <text x="60" y="90" fill="#34d399" font-size="14" font-family="monospace">└── 🖼️ cover.jpg</text>
      <text x="210" y="90" fill="#34d399" font-size="11">(Max 5 MB)</text>
    </g>

    <rect x="20" y="170" width="340" height="35" rx="6" fill="#1e293b"/>
    <text x="35" y="192" fill="#94a3b8" font-size="11">Protected by Storage RLS: foldername[1] = auth.uid()</text>
  </g>

  <!-- Right Side: 3-step Pipeline -->
  <g transform="translate(460, 65)" filter="url(#shadow)">
    <rect width="400" height="225" rx="12" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="400" height="35" rx="12" fill="#065f46" fill-opacity="0.3"/>
    <text x="20" y="23" fill="#34d399" font-size="13" font-weight="700">🚀 3-Step Recipe &amp; Image Creation</text>
    
    <!-- Steps -->
    <g transform="translate(20, 50)">
      <rect width="360" height="40" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="25" fill="#38bdf8" font-size="12" font-weight="700">1️⃣ INSERT Recipe Draft</text>
      <text x="180" y="25" fill="#94a3b8" font-size="11">→ Retrieve new recipe_id</text>
    </g>

    <g transform="translate(20, 100)">
      <rect width="360" height="40" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="25" fill="#fbbf24" font-size="12" font-weight="700">2️⃣ Upload to Storage</text>
      <text x="165" y="25" fill="#94a3b8" font-size="11">→ &lt;user_id&gt;/&lt;recipe_id&gt;/cover.jpg</text>
    </g>

    <g transform="translate(20, 150)">
      <rect width="360" height="40" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="25" fill="#34d399" font-size="12" font-weight="700">3️⃣ UPDATE recipes row</text>
      <text x="185" y="25" fill="#34d399" font-size="11">→ SET cover_image_path = path</text>
    </g>
  </g>
</svg>'''
save_svg("07-storage-structure.svg", svg_07_store)

# 11. 08-realtime-flow.svg
svg_08_realtime = SVG_HEADER.format(width=900, height=360) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">REALTIME WEBSOCKET STREAM &amp; POSTGRES WAL EVENT</text>
  
  <!-- Lifelines -->
  <g transform="translate(60, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="70" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">👩 Alice (Client A)</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(300, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="70" y="25" fill="#cbd5e1" font-size="12" font-weight="700" text-anchor="middle">🌐 Supabase API</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(500, 60)">
    <rect width="150" height="40" rx="8" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="75" y="25" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">🐘 Postgres (WAL)</text>
    <line x1="75" y1="40" x2="75" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <g transform="translate(710, 60)">
    <rect width="140" height="40" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="70" y="25" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">👨 Bob (Client B)</text>
    <line x1="70" y1="40" x2="70" y2="280" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <!-- Step 0: Bob Subscribes -->
  <line x1="780" y1="120" x2="380" y2="120" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow-green)"/>
  <rect x="420" y="103" width="310" height="20" rx="4" fill="#0f172a"/>
  <text x="575" y="117" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">1. Bob subscribes: channel('recipe-123')</text>

  <!-- Step 1: Alice Posts -->
  <line x1="130" y1="160" x2="360" y2="160" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <rect x="145" y="143" width="200" height="20" rx="4" fill="#0f172a"/>
  <text x="245" y="157" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">2. Alice POST /rest/v1/comments</text>

  <!-- Step 2: DB Insert -->
  <line x1="380" y1="195" x2="560" y2="195" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="395" y="178" width="150" height="20" rx="4" fill="#0f172a"/>
  <text x="470" y="192" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">3. INSERT into comments</text>

  <!-- Step 3: WAL Broadcast -->
  <line x1="580" y1="230" x2="770" y2="230" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
  <rect x="590" y="213" width="170" height="20" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
  <text x="675" y="227" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">4. Push WebSocket Event</text>

  <!-- Step 4: Bob UI Updates -->
  <rect x="700" y="255" width="160" height="30" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1"/>
  <text x="780" y="275" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">🎉 Bob's UI Updates Live!</text>
</svg>'''
save_svg("08-realtime-flow.svg", svg_08_realtime)

# 12. 09-edge-functions-flow.svg
svg_09_func = SVG_HEADER.format(width=900, height=240) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">EDGE FUNCTION INVOCATION PIPELINE</text>
  
  <!-- Client -->
  <g transform="translate(40, 70)" filter="url(#shadow)">
    <rect width="200" height="120" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="45" font-size="24" text-anchor="middle">📱 💻</text>
    <text x="100" y="72" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Flutter / Next.js</text>
    <text x="100" y="95" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">functions.invoke('view-count')</text>
  </g>

  <!-- Step 1 Arrow -->
  <path d="M 240 130 L 330 130" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <text x="285" y="120" fill="#38bdf8" font-size="10" text-anchor="middle">1. JWT + Body</text>

  <!-- Edge Function -->
  <g transform="translate(340, 70)" filter="url(#shadow)">
    <rect width="240" height="120" rx="12" fill="url(#bg-card)" stroke="#c084fc" stroke-width="2"/>
    <text x="120" y="45" font-size="24" text-anchor="middle">🚀</text>
    <text x="120" y="72" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">Edge Function (Deno)</text>
    <text x="120" y="95" fill="#cbd5e1" font-size="11" text-anchor="middle">Verifies JWT • Custom Logic</text>
  </g>

  <!-- Step 2 Arrow -->
  <path d="M 580 130 L 660 130" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
  <text x="620" y="120" fill="#34d399" font-size="10" text-anchor="middle">2. rpc() call</text>

  <!-- Postgres -->
  <g transform="translate(670, 70)" filter="url(#shadow)">
    <rect width="190" height="120" rx="12" fill="url(#bg-card)" stroke="#34d399" stroke-width="1.5"/>
    <text x="95" y="45" font-size="24" text-anchor="middle">🐘</text>
    <text x="95" y="72" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Postgres Database</text>
    <text x="95" y="95" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">increment_recipe_views()</text>
  </g>
</svg>'''
save_svg("09-edge-functions-flow.svg", svg_09_func)

# 13. 10-migration-lifecycle.svg
svg_10_mig = SVG_HEADER.format(width=900, height=220) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">SUPABASE CLI DATABASE MIGRATION WORKFLOW</text>
  
  <!-- Steps 1 to 5 -->
  <g transform="translate(30, 70)" filter="url(#shadow)">
    <rect width="140" height="90" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="70" y="35" font-size="18" text-anchor="middle">1️⃣</text>
    <text x="70" y="60" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">migration new</text>
    <text x="70" y="78" fill="#94a3b8" font-size="10" text-anchor="middle">Create SQL file</text>
  </g>
  <line x1="170" y1="115" x2="200" y2="115" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <g transform="translate(205, 70)" filter="url(#shadow)">
    <rect width="140" height="90" rx="10" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="70" y="35" font-size="18" text-anchor="middle">2️⃣</text>
    <text x="70" y="60" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Write Schema</text>
    <text x="70" y="78" fill="#94a3b8" font-size="10" text-anchor="middle">DDL / Tables / RLS</text>
  </g>
  <line x1="345" y1="115" x2="375" y2="115" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <g transform="translate(380, 70)" filter="url(#shadow)">
    <rect width="140" height="90" rx="10" fill="url(#bg-card)" stroke="#c084fc" stroke-width="1.5"/>
    <text x="70" y="35" font-size="18" text-anchor="middle">3️⃣</text>
    <text x="70" y="60" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">db reset</text>
    <text x="70" y="78" fill="#94a3b8" font-size="10" text-anchor="middle">Test in local Docker</text>
  </g>
  <line x1="520" y1="115" x2="550" y2="115" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

  <g transform="translate(555, 70)" filter="url(#shadow)">
    <rect width="140" height="90" rx="10" fill="url(#bg-card)" stroke="#64748b" stroke-width="1.5"/>
    <text x="70" y="35" font-size="18" text-anchor="middle">4️⃣</text>
    <text x="70" y="60" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">Git Commit</text>
    <text x="70" y="78" fill="#94a3b8" font-size="10" text-anchor="middle">Version control</text>
  </g>
  <line x1="695" y1="115" x2="725" y2="115" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <g transform="translate(730, 70)" filter="url(#shadow)">
    <rect width="140" height="90" rx="10" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <text x="70" y="35" font-size="18" text-anchor="middle">5️⃣</text>
    <text x="70" y="60" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">db push</text>
    <text x="70" y="78" fill="#34d399" font-size="10" text-anchor="middle">Deploy to Cloud</text>
  </g>
</svg>'''
save_svg("10-migration-lifecycle.svg", svg_10_mig)

# 14. 11-environments.svg
svg_11_env = SVG_HEADER.format(width=900, height=280) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">MULTI-ENVIRONMENT ISOLATION STRATEGY</text>
  
  <!-- Environment 1: Dev -->
  <g transform="translate(40, 70)" filter="url(#shadow)">
    <rect width="250" height="160" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="125" y="35" font-size="20" text-anchor="middle">💻 📱</text>
    <text x="125" y="60" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Local Development</text>
    <text x="125" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">Flutter (.env) • Next.js (.env.local)</text>
    <line x1="30" y1="95" x2="220" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="125" y="120" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">🛠️ Dev Supabase Project</text>
    <text x="125" y="140" fill="#64748b" font-size="10" text-anchor="middle">Local Docker or Dev Cloud</text>
  </g>

  <!-- Environment 2: Staging -->
  <g transform="translate(325, 70)" filter="url(#shadow)">
    <rect width="250" height="160" rx="12" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="125" y="35" font-size="20" text-anchor="middle">🧪 🚀</text>
    <text x="125" y="60" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">CI / Staging (QA)</text>
    <text x="125" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">Automated Tests • QA Testers</text>
    <line x1="30" y1="95" x2="220" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="125" y="120" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">🧪 Staging Supabase Project</text>
    <text x="125" y="140" fill="#64748b" font-size="10" text-anchor="middle">Preview Branch / Test DB</text>
  </g>

  <!-- Environment 3: Prod -->
  <g transform="translate(610, 70)" filter="url(#shadow)">
    <rect width="250" height="160" rx="12" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <text x="125" y="35" font-size="20" text-anchor="middle">🔒 🌐</text>
    <text x="125" y="60" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Production Store</text>
    <text x="125" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">App Store / Play Store / Web</text>
    <line x1="30" y1="95" x2="220" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="125" y="120" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">🔒 Production Supabase Project</text>
    <text x="125" y="140" fill="#34d399" font-size="10" text-anchor="middle">Strict RLS • Daily Backups</text>
  </g>
</svg>'''
save_svg("11-environments.svg", svg_11_env)

# 15. 11-release-flow.svg
svg_11_rel = SVG_HEADER.format(width=900, height=180) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="15" font-weight="700" text-anchor="middle">PRODUCTION RELEASE CHECKLIST FLOW</text>
  
  <g transform="translate(25, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">1️⃣</text>
    <text x="62" y="52" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Migration Test</text>
    <text x="62" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">Local/Staging</text>
  </g>
  <line x1="150" y1="102" x2="168" y2="102" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>

  <g transform="translate(170, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#c084fc" stroke-width="1"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">2️⃣</text>
    <text x="62" y="52" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">RLS Scenarios</text>
    <text x="62" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">User A vs User B</text>
  </g>
  <line x1="295" y1="102" x2="313" y2="102" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>

  <g transform="translate(315, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#fbbf24" stroke-width="1"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">3️⃣</text>
    <text x="62" y="52" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Client Builds</text>
    <text x="62" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">Flutter + Next.js</text>
  </g>
  <line x1="440" y1="102" x2="458" y2="102" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>

  <g transform="translate(460, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">4️⃣</text>
    <text x="62" y="52" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Prod Migrate</text>
    <text x="62" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">Apply SQL</text>
  </g>
  <line x1="585" y1="102" x2="603" y2="102" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>

  <g transform="translate(605, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="1"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">5️⃣</text>
    <text x="62" y="52" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Smoke Test</text>
    <text x="62" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">Auth, CRUD, Media</text>
  </g>
  <line x1="730" y1="102" x2="748" y2="102" stroke="#34d399" stroke-width="1.5" marker-end="url(#arrow-green)"/>

  <g transform="translate(750, 60)" filter="url(#shadow)">
    <rect width="125" height="85" rx="8" fill="url(#bg-card)" stroke="#34d399" stroke-width="2"/>
    <text x="62" y="30" font-size="16" text-anchor="middle">6️⃣</text>
    <text x="62" y="52" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Monitor Logs</text>
    <text x="62" y="70" fill="#34d399" font-size="9" text-anchor="middle">Sentry / Supabase</text>
  </g>
</svg>'''
save_svg("11-release-flow.svg", svg_11_rel)

# 16. readme-architecture.svg
svg_readme = SVG_HEADER.format(width=900, height=360) + '''
  <text x="450" y="35" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">MONT-SHA SYSTEM ARCHITECTURE (MULTI-CLIENT)</text>
  
  <!-- Clients -->
  <g transform="translate(40, 75)" filter="url(#shadow)">
    <rect width="180" height="95" rx="10" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="38" font-size="22" text-anchor="middle">📱</text>
    <text x="90" y="65" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Flutter Mobile App</text>
    <text x="90" y="82" fill="#94a3b8" font-size="10" text-anchor="middle">Android &amp; iOS Client</text>
  </g>

  <g transform="translate(40, 195)" filter="url(#shadow)">
    <rect width="180" height="95" rx="10" fill="url(#bg-card)" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="90" y="38" font-size="22" text-anchor="middle">💻</text>
    <text x="90" y="65" fill="#60a5fa" font-size="13" font-weight="700" text-anchor="middle">Next.js Web App</text>
    <text x="90" y="82" fill="#94a3b8" font-size="10" text-anchor="middle">SSR &amp; App Router</text>
  </g>

  <!-- Connectors to Kong -->
  <path d="M 220 122 L 290 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
  <path d="M 220 242 L 290 195" stroke="#60a5fa" stroke-width="2" marker-end="url(#arrow-cyan)"/>

  <!-- Kong Gateway -->
  <g transform="translate(300, 100)" filter="url(#shadow)">
    <rect width="150" height="165" rx="12" fill="url(#bg-card)" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="45" font-size="26" text-anchor="middle">🌐</text>
    <text x="75" y="75" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Kong Gateway</text>
    <text x="75" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">API Routing</text>
    <text x="75" y="125" fill="#94a3b8" font-size="10" text-anchor="middle">Auth Verification</text>
    <text x="75" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">Rate Limiting</text>
  </g>

  <!-- Services Box -->
  <g transform="translate(490, 65)" filter="url(#shadow)">
    <rect width="180" height="235" rx="12" fill="url(#bg-card)" stroke="#c084fc" stroke-width="1.5"/>
    <text x="90" y="28" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">⚡ SUPABASE SERVICES</text>
    
    <text x="20" y="65" fill="#fb7185" font-size="12" font-weight="600">🔐 GoTrue Auth</text>
    <text x="20" y="105" fill="#34d399" font-size="12" font-weight="600">⚡ PostgREST (CRUD)</text>
    <text x="20" y="145" fill="#38bdf8" font-size="12" font-weight="600">📡 Realtime (WS)</text>
    <text x="20" y="185" fill="#fbbf24" font-size="12" font-weight="600">📦 Storage (S3)</text>
    <text x="20" y="225" fill="#c084fc" font-size="12" font-weight="600">🚀 Edge Functions</text>
  </g>

  <!-- Connector Kong to Services -->
  <path d="M 450 182 L 480 182" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

  <!-- Connector Services to Postgres -->
  <path d="M 670 182 L 710 182" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- Postgres Engine -->
  <g transform="translate(720, 90)" filter="url(#shadow)">
    <rect width="150" height="185" rx="12" fill="url(#bg-card)" stroke="#34d399" stroke-width="2.5"/>
    <text x="75" y="45" font-size="28" text-anchor="middle">🐘</text>
    <text x="75" y="75" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">PostgreSQL</text>
    <text x="75" y="100" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Database Core</text>
    <text x="75" y="125" fill="#34d399" font-size="10" text-anchor="middle">Row Level Security</text>
    <text x="75" y="145" fill="#94a3b8" font-size="10" text-anchor="middle">WAL Replication</text>
    <text x="75" y="165" fill="#94a3b8" font-size="10" text-anchor="middle">JSONB &amp; Triggers</text>
  </g>
</svg>'''
save_svg("readme-architecture.svg", svg_readme)

print("All SVGs successfully created!")
