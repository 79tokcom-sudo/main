<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>ATELIER — NOTE</title>
  <link rel="icon" href="assets/mark.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+KR:wght@300;400;500;600&family=Noto+Serif+KR:wght@400;500;600&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>
    :root {
      --canvas: #09090B;
      --surface: #121214;
      --hairline: rgba(245, 240, 232, 0.12);
      --ivory: #F4F0E6;
      --muted: #8A8478;
      --ember: #FF4D1C;
      --ember-dim: #C43A12;
      --live: #7CFFB2;
      --display: "Fraunces", "Noto Serif KR", serif;
      --sans: "Outfit", "Noto Sans KR", sans-serif;
      --mono: "IBM Plex Mono", "Noto Sans KR", ui-monospace, monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    html, body { background: var(--canvas); color: var(--ivory); }
    body {
      font-family: var(--sans);
      font-weight: 400;
      min-height: 100vh;
      overflow-x: hidden;
    }
    img { max-width: 100%; display: block; }
    button, input, textarea { font: inherit; color: inherit; }
    button { cursor: pointer; }
    a { color: inherit; }

    .skip {
      position: absolute;
      left: 12px;
      top: -40px;
      z-index: 80;
      background: var(--ember);
      color: #1a0905;
      padding: 8px 12px;
      font-size: 13px;
    }
    .skip:focus { top: 12px; }

    .spot {
      position: fixed;
      width: 72vmax;
      height: 72vmax;
      left: 0;
      top: 0;
      border-radius: 50%;
      pointer-events: none;
      z-index: 0;
      background: radial-gradient(circle, rgba(255, 186, 132, 0.07) 0%, rgba(255, 77, 28, 0.03) 32%, transparent 64%);
      transform: translate3d(-50%, -50%, 0);
      transition: transform 0.7s cubic-bezier(0.22, 1, 0.36, 1);
      will-change: transform;
    }
    .grain {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 60;
      opacity: 0.045;
      background: url("assets/grain.png") repeat;
      background-size: 220px;
      mix-blend-mode: overlay;
    }

    .wrap {
      width: min(1440px, calc(100% - 48px));
      margin-inline: auto;
    }

    /* Top bar */
    .topbar {
      position: relative;
      z-index: 2;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      padding: 22px 0 20px;
      border-bottom: 1px solid var(--hairline);
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }
    .brand img {
      width: 28px;
      height: 28px;
      object-fit: cover;
    }
    .wordmark {
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.28em;
      font-weight: 500;
    }
    .wordmark small {
      display: block;
      margin-top: 3px;
      font-size: 10px;
      letter-spacing: 0.18em;
      color: var(--muted);
      font-weight: 400;
    }
    .nav {
      display: flex;
      gap: 28px;
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.14em;
    }
    .nav a {
      text-decoration: none;
      color: var(--muted);
      transition: color 0.2s;
    }
    .nav a:hover, .nav a:focus-visible { color: var(--ivory); }
    .top-actions {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .live {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--hairline);
      padding: 6px 10px 6px 8px;
      border-radius: 999px;
    }
    .live i {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--live);
      box-shadow: 0 0 8px var(--live);
      animation: pulse 2.4s ease-in-out infinite;
      font-style: normal;
    }
    .btn-ember {
      background: transparent;
      border: 1px solid var(--ember);
      color: var(--ivory);
      padding: 9px 14px;
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      transition: background 0.2s, color 0.2s, box-shadow 0.2s;
    }
    .btn-ember:hover, .btn-ember:focus-visible {
      background: var(--ember);
      color: #1a0905;
      box-shadow: 0 0 0 1px var(--ember);
      outline: none;
    }
    .btn-ghost {
      background: transparent;
      border: 1px solid var(--hairline);
      color: var(--ivory);
      padding: 9px 14px;
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.12em;
    }
    .btn-ghost:hover, .btn-ghost:focus-visible {
      border-color: var(--ivory);
      outline: none;
    }
    .btn-ghost:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    /* Hero */
    .hero {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 40px;
      align-items: end;
      padding: 72px 0 56px;
    }
    .hero h1 {
      font-family: var(--display);
      font-optical-sizing: auto;
      font-weight: 500;
      font-size: clamp(2.4rem, 6.4vw, 6.4rem);
      letter-spacing: -0.035em;
      line-height: 0.98;
      max-width: 14ch;
      animation: rise 0.9s ease both;
    }
    .hero h1 em {
      font-style: italic;
      font-weight: 400;
      display: block;
    }
    .lede {
      margin-top: 22px;
      max-width: 42ch;
      color: var(--muted);
      font-size: 16px;
      font-weight: 300;
      line-height: 1.65;
      animation: rise 0.9s ease 0.1s both;
    }
    .meta {
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding-bottom: 8px;
      animation: rise 0.9s ease 0.18s both;
    }
    .meta span {
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
      border-bottom: 1px solid var(--hairline);
      padding-bottom: 10px;
      white-space: nowrap;
    }
    .meta span:last-child { border-bottom: 0; padding-bottom: 0; }

    /* Gallery */
    .gallery-head {
      position: relative;
      z-index: 1;
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 18px;
    }
    .gallery-head h2,
    .kicker {
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-weight: 500;
    }
    .gallery-head p { color: var(--muted); font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; }

    .gallery {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: 1.2fr 0.9fr 0.9fr;
      gap: 14px 16px;
      align-items: stretch;
    }
    .still {
      display: flex;
      flex-direction: column;
      gap: 12px;
      text-align: left;
      background: none;
      border: 0;
      color: inherit;
      min-width: 0;
    }
    .still:focus-visible .frame {
      outline: 2px solid var(--ember);
      outline-offset: 3px;
    }
    .still.featured {
      grid-column: 1 / 3;
      grid-row: 1 / 3;
      height: 100%;
    }
    .frame {
      position: relative;
      aspect-ratio: 16 / 9;
      overflow: hidden;
      border: 1px solid var(--hairline);
      background: var(--surface);
      box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.45);
      transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .still.featured .frame {
      flex: 1 1 auto;
      aspect-ratio: auto;
      height: auto;
      min-height: 280px;
    }
    .frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scale(1);
      transition: transform 8s ease-out, filter 0.4s;
    }
    .shade {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(9, 9, 11, 0.55) 100%);
      opacity: 0.55;
      transition: opacity 0.35s, background 0.35s;
      pointer-events: none;
    }
    .play {
      position: absolute;
      right: 16px;
      bottom: 16px;
      width: 36px;
      height: 36px;
      border: 1px solid rgba(245, 240, 232, 0.35);
      display: grid;
      place-items: center;
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 0.3s, transform 0.3s;
      pointer-events: none;
    }
    .play svg { display: block; }
    .run-cue {
      position: absolute;
      left: 16px;
      bottom: 16px;
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--ivory);
      opacity: 0;
      transform: translateX(-14px);
      transition: opacity 0.4s, transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
      pointer-events: none;
    }
    .ember-bar {
      position: absolute;
      left: 0;
      bottom: 0;
      height: 2px;
      width: 100%;
      background: var(--ember);
      transform: scaleX(0);
      transform-origin: left center;
      transition: transform 0.85s cubic-bezier(0.22, 1, 0.36, 1);
      pointer-events: none;
    }
    .still:hover .frame,
    .still:focus-visible .frame { transform: scale(1.02); }
    .still:hover img,
    .still:focus-visible img { transform: scale(1.08); filter: brightness(0.72); }
    .still:hover .shade,
    .still:focus-visible .shade {
      opacity: 1;
      background: rgba(9, 9, 11, 0.45);
    }
    .still:hover .play,
    .still:focus-visible .play { opacity: 1; transform: none; }
    .still:hover .run-cue,
    .still:focus-visible .run-cue { opacity: 1; transform: none; }
    .still.featured:hover .ember-bar,
    .still.featured:focus-visible .ember-bar { transform: scaleX(1); }

    .still-meta h3 {
      font-family: var(--display);
      font-weight: 500;
      font-size: 1.35rem;
      letter-spacing: -0.02em;
    }
    .labels {
      display: flex;
      flex-wrap: wrap;
      gap: 8px 12px;
      margin-top: 6px;
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .add-tile .frame {
      display: grid;
      place-items: center;
      border-style: dashed;
      background: transparent;
      box-shadow: none;
    }
    .add-inner {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      padding: 20px;
      text-align: center;
    }
    .add-inner .plus {
      width: 36px;
      height: 36px;
      border: 1px solid var(--hairline);
      display: grid;
      place-items: center;
    }
    .add-inner p {
      font-size: 14px;
      color: var(--muted);
      max-width: 18ch;
      line-height: 1.5;
    }
    .add-tile:hover .frame,
    .add-tile:focus-visible .frame {
      border-color: var(--ember);
      transform: none;
    }
    .add-tile:hover img { transform: none; filter: none; }

    /* About */
    .about {
      position: relative;
      z-index: 1;
      margin-top: 88px;
      padding: 28px 0 48px;
      border-top: 1px solid var(--hairline);
      display: grid;
      grid-template-columns: 1.4fr 1fr auto;
      gap: 32px;
      align-items: start;
    }
    .about h2 {
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }
    .about p {
      color: var(--muted);
      line-height: 1.7;
      max-width: 52ch;
      font-weight: 300;
    }
    .about a {
      color: var(--ivory);
      text-decoration: none;
      border-bottom: 1px solid var(--ember);
    }
    .about a:hover, .about a:focus-visible { color: var(--ember); }
    .about .copy-label {
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }

    /* Run stage */
    #view-run {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 20;
      background: var(--canvas);
      grid-template-columns: 1fr 300px;
      grid-template-rows: auto 1fr;
    }
    body.is-running { overflow: hidden; }
    body.is-running #view-index { visibility: hidden; pointer-events: none; }
    body.is-running #view-run { display: grid; }

    .rail {
      grid-column: 1 / -1;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 14px 20px;
      border-bottom: 1px solid var(--hairline);
    }
    .rail-left, .rail-right { display: flex; align-items: center; gap: 14px; min-width: 0; }
    .back {
      background: none;
      border: 0;
      color: var(--ivory);
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.1em;
      padding: 6px 0;
    }
    .back:hover, .back:focus-visible { color: var(--ember); outline: none; }
    .rail h2 {
      font-family: var(--display);
      font-weight: 500;
      font-size: 1.25rem;
      letter-spacing: -0.02em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .theater {
      position: relative;
      margin: 16px 0 16px 16px;
      border: 1px solid var(--hairline);
      background: #000;
      min-height: 0;
      overflow: hidden;
      box-shadow: inset 0 0 80px rgba(0, 0, 0, 0.5);
    }
    .theater iframe {
      width: 100%;
      height: 100%;
      border: 0;
      background: #000;
    }
    .poster {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: opacity 0.5s;
    }
    .poster.is-gone { opacity: 0; pointer-events: none; }
    .empty-stage {
      position: absolute;
      inset: 0;
      display: none;
      place-items: end start;
      padding: 36px;
      background:
        linear-gradient(180deg, rgba(9,9,11,0.2), rgba(9,9,11,0.78)),
        var(--thumb, #121214) center/cover;
    }
    .empty-stage.is-on { display: grid; }
    .empty-stage h3 {
      font-family: var(--display);
      font-size: clamp(1.6rem, 3vw, 2.4rem);
      font-weight: 400;
      max-width: 16ch;
    }
    .empty-stage p { margin-top: 10px; color: #cfc6b6; font-size: 15px; }
    .strip {
      border-left: 1px solid var(--hairline);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      min-height: 0;
      overflow: auto;
    }
    .strip img {
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      border: 1px solid var(--hairline);
    }
    .strip p { color: var(--muted); font-size: 14px; line-height: 1.65; font-weight: 300; }

    /* Modal */
    .studio {
      width: min(440px, 100vw);
      height: 100vh;
      max-height: 100vh;
      margin: 0 0 0 auto;
      background: var(--surface);
      color: var(--ivory);
      border: 0;
      border-left: 1px solid var(--hairline);
      padding: 0;
    }
    .studio::backdrop { background: rgba(5, 5, 6, 0.62); }
    .studio-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 22px;
      border-bottom: 1px solid var(--hairline);
    }
    .studio-head h2 {
      font-family: var(--display);
      font-size: 1.5rem;
      font-weight: 500;
    }
    .icon-btn {
      width: 36px;
      height: 36px;
      background: none;
      border: 1px solid var(--hairline);
      color: var(--ivory);
      display: grid;
      place-items: center;
    }
    .icon-btn:hover, .icon-btn:focus-visible { border-color: var(--ivory); outline: none; }
    form.studio-form {
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      overflow: auto;
      height: calc(100vh - 73px);
    }
    .drop {
      position: relative;
      border: 1px dashed var(--hairline);
      min-height: 180px;
      display: grid;
      place-items: center;
      cursor: pointer;
      overflow: hidden;
      background: var(--canvas);
    }
    .drop.is-hot { border-color: var(--ember); box-shadow: inset 0 0 0 1px var(--ember); }
    .drop input {
      position: absolute;
      inset: 0;
      opacity: 0;
      cursor: pointer;
    }
    .drop-hint {
      text-align: center;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.5;
      padding: 16px;
      pointer-events: none;
    }
    .drop-hint strong { display: block; color: var(--ivory); font-weight: 500; margin-bottom: 4px; }
    .drop img.preview {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      pointer-events: none;
    }
    .drop.has-preview .drop-hint { display: none; }
    label.field { display: flex; flex-direction: column; gap: 8px; }
    label.field span {
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }
    input[type="text"], input[type="url"], input[type="number"], textarea {
      background: var(--canvas);
      border: 1px solid var(--hairline);
      padding: 11px 12px;
      color: var(--ivory);
      border-radius: 0;
      outline: none;
    }
    input:focus, textarea:focus { border-color: rgba(255, 77, 28, 0.7); }
    textarea { min-height: 88px; resize: vertical; }
    .form-actions {
      display: flex;
      gap: 10px;
      margin-top: auto;
      padding-top: 8px;
    }
    .form-error {
      color: var(--ember);
      font-size: 13px;
      min-height: 1.2em;
    }

    .morph-clone {
      position: fixed;
      z-index: 34;
      object-fit: cover;
      border: 1px solid var(--hairline);
      pointer-events: none;
      box-shadow: inset 0 0 60px rgba(0,0,0,0.4);
    }

    @keyframes rise {
      from { opacity: 0; transform: translateY(18px); }
      to { opacity: 1; transform: none; }
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.35; }
    }

    @media (max-width: 1024px) {
      .gallery { grid-template-columns: 1.15fr 1fr; }
      .still.featured { grid-column: 1; grid-row: 1 / 3; }
      #view-run { grid-template-columns: 1fr; grid-template-rows: auto 1fr auto; }
      .theater { margin: 12px 12px 0; min-height: 48vh; }
      .strip {
        border-left: 0;
        border-top: 1px solid var(--hairline);
        flex-direction: row;
        align-items: center;
      }
      .strip img { width: 160px; flex: 0 0 160px; }
    }
    @media (max-width: 760px) {
      .wrap { width: calc(100% - 28px); }
      .topbar {
        display: grid;
        grid-template-columns: 1fr auto;
        align-items: center;
        gap: 12px 10px;
      }
      .nav { width: auto; grid-column: 1 / -1; }
      .top-actions { flex-wrap: wrap; justify-content: flex-end; gap: 8px; }
      .btn-ember { padding: 8px 10px; letter-spacing: 0.06em; white-space: nowrap; }
      .hero { grid-template-columns: 1fr; gap: 24px; padding: 48px 0 36px; }
      .meta { flex-direction: row; flex-wrap: wrap; gap: 8px 18px; }
      .meta span { border-bottom: 0; padding-bottom: 0; }
      .gallery { grid-template-columns: 1fr; }
      .still.featured { grid-column: auto; grid-row: auto; }
      .still.featured .frame { min-height: 0; aspect-ratio: 16 / 9; }
      .about { grid-template-columns: 1fr; gap: 20px; margin-top: 56px; }
      .strip { flex-direction: column; align-items: stretch; }
      .strip img { width: 100%; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      .spot, .frame, .frame img, .run-cue, .play, .ember-bar, .shade, .poster, .still {
        transition: none !important;
        animation: none !important;
      }
      .live i { animation: none; }
    }
  </style>
</head>
<body>
  <a class="skip" href="#works">작품으로 건너뛰기</a>
  <div class="spot" id="spot" aria-hidden="true"></div>
  <div class="grain" aria-hidden="true"></div>

  <div id="view-index">
    <header class="topbar wrap">
      <a class="brand" href="#/" data-home>
        <img src="assets/mark.png" alt="" width="28" height="28" />
        <span class="wordmark">ATELIER<small>NOTE</small></span>
      </a>
      <nav class="nav" aria-label="주요">
        <a href="#works">작품</a>
        <a href="#about">소개</a>
        <a href="#contact">연락</a>
      </nav>
      <div class="top-actions">
        <span class="live" aria-label="라이브 상태"><i></i> Live</span>
        <button type="button" class="btn-ember" id="open-studio">작품 추가</button>
      </div>
    </header>

    <main>
      <section class="hero wrap" aria-labelledby="hero-title">
        <div>
          <h1 id="hero-title">선택과 실행이 <em>한 화면에서.</em></h1>
          <p class="lede">캘린더, 스튜디오, 론칭까지 — 제품 표면을 설계하고 바로 무대에 올립니다. 스틸을 고르면 실행이 시작됩니다.</p>
        </div>
        <div class="meta">
          <span>Based in Seoul</span>
          <span>Available Q4</span>
          <span id="work-count">선정 작품 3</span>
        </div>
      </section>

      <section id="works" class="wrap" aria-labelledby="works-title">
        <div class="gallery-head">
          <h2 id="works-title">작품</h2>
          <p>Selected stills</p>
        </div>
        <div class="gallery" id="gallery"></div>
      </section>

      <section id="about" class="about wrap" aria-labelledby="about-title">
        <div>
          <h2 id="about-title">소개</h2>
          <p>NOTE는 서울에서 제품 표면을 만듭니다. 계획의 리듬, 작업실의 밤, 론칭의 한 컷 — 선택과 실행 사이의 거리를 지우는 일을 합니다.</p>
        </div>
        <div id="contact">
          <h2>연락</h2>
          <p><a href="mailto:hello@atelier.note">hello@atelier.note</a></p>
        </div>
        <p class="copy-label">© 2026 Atelier / Note</p>
      </section>
    </main>
  </div>

  <section id="view-run" aria-label="실행 무대">
    <div class="rail">
      <div class="rail-left">
        <button type="button" class="back" id="back-index">← 작품 목록</button>
        <h2 id="run-title">작품</h2>
      </div>
      <div class="rail-right">
        <div class="labels" id="run-tags"></div>
        <span class="live"><i></i> Live</span>
      </div>
    </div>
    <div class="theater" id="theater">
      <img class="poster" id="run-poster" alt="" />
      <iframe id="run-frame" title="작품 실행 화면" hidden></iframe>
      <div class="empty-stage" id="empty-stage">
        <div>
          <h3>실행 URL이 아직 없습니다</h3>
          <p>이 스틸은 무대의 포스터로만 남아 있습니다.</p>
        </div>
      </div>
    </div>
    <aside class="strip">
      <img id="strip-thumb" alt="" />
      <div>
        <p id="strip-desc"></p>
        <p class="labels" id="strip-year"></p>
      </div>
      <a class="btn-ghost" id="open-tab" href="#" target="_blank" rel="noopener noreferrer">새 탭에서 열기</a>
    </aside>
  </section>

  <dialog class="studio" id="studio" aria-labelledby="studio-title">
    <div class="studio-head">
      <h2 id="studio-title">작품 등록</h2>
      <button type="button" class="icon-btn" id="close-studio" aria-label="닫기">
        <svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 2l10 10M12 2L2 12" stroke="currentColor" stroke-width="1.4"/></svg>
      </button>
    </div>
    <form class="studio-form" id="studio-form">
      <label class="drop" id="drop">
        <input type="file" id="thumb-input" accept="image/jpeg,image/png,image/webp" aria-label="썸네일 이미지 선택" />
        <div class="drop-hint">
          <strong>썸네일을 놓거나 클릭해서 선택</strong>
          JPG, PNG, WEBP · 16:9 권장
        </div>
        <img class="preview" id="thumb-preview" alt="선택한 썸네일 미리보기" hidden />
      </label>
      <label class="field">
        <span>제목</span>
        <input type="text" id="field-title" name="title" required placeholder="Planner Hub" autocomplete="off" />
      </label>
      <label class="field">
        <span>짧은 소개</span>
        <textarea id="field-desc" name="description" placeholder="한 화면에서 무엇을 실행하나요?"></textarea>
      </label>
      <label class="field">
        <span>태그 · 쉼표로 구분</span>
        <input type="text" id="field-tags" name="tags" placeholder="제품, 캘린더" />
      </label>
      <label class="field">
        <span>연도</span>
        <input type="number" id="field-year" name="year" min="2000" max="2100" value="2026" />
      </label>
      <label class="field">
        <span>실행 URL</span>
        <input type="text" id="field-url" name="url" inputmode="url" placeholder="https:// 또는 상대 경로" />
      </label>
      <p class="form-error" id="form-error" role="alert"></p>
      <div class="form-actions">
        <button type="submit" class="btn-ember">저장</button>
        <button type="button" class="btn-ghost" id="cancel-studio">취소</button>
      </div>
    </form>
  </dialog>

  <script>
    (function () {
      const STORAGE_KEY = "atelier.works.v1";
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      const SEEDS = [
        {
          id: "planner",
          title: "Planner Hub",
          year: "2026",
          tags: ["제품", "캘린더"],
          description: "일정과 의도를 한 운영체제로 묶는 플래닝 OS. 주간 리듬과 실행 큐를 하나의 표면에서 다룹니다.",
          thumbnail: "assets/thumb-planner.jpg",
          url: "assets/works/planner.html"
        },
        {
          id: "studio",
          title: "스튜디오 리뉴얼",
          year: "2026",
          tags: ["브랜딩", "UI"],
          description: "작업실의 밤을 기준으로 재구성한 브랜드 시스템. 모니터 빛과 지문의 온도를 그대로 옮겼습니다.",
          thumbnail: "assets/thumb-studio.jpg",
          url: "assets/works/studio.html"
        },
        {
          id: "launch",
          title: "제품 론칭",
          year: "2025",
          tags: ["모션", "캠페인"],
          description: "금속 캡슐이 어둠에서 떠오르는 드롭 키비주얼. 림라이트 한 줄로 제품의 무게를 설명합니다.",
          thumbnail: "assets/thumb-launch.jpg",
          url: "assets/works/launch.html"
        }
      ];

      const gallery = document.getElementById("gallery");
      const studio = document.getElementById("studio");
      const form = document.getElementById("studio-form");
      const drop = document.getElementById("drop");
      const thumbInput = document.getElementById("thumb-input");
      const thumbPreview = document.getElementById("thumb-preview");
      const formError = document.getElementById("form-error");
      const spot = document.getElementById("spot");
      const workCount = document.getElementById("work-count");

      let works = loadWorks();
      let pendingThumb = "";

      function loadWorks() {
        try {
          const raw = localStorage.getItem(STORAGE_KEY);
          if (!raw) return SEEDS.map(function (w) { return Object.assign({}, w); });
          const parsed = JSON.parse(raw);
          if (!Array.isArray(parsed) || !parsed.length) {
            return SEEDS.map(function (w) { return Object.assign({}, w); });
          }
          return parsed;
        } catch (e) {
          return SEEDS.map(function (w) { return Object.assign({}, w); });
        }
      }

      function saveWorks() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(works));
      }

      function playIcon() {
        return '<svg width="10" height="12" viewBox="0 0 10 12" aria-hidden="true"><path d="M2 1.5v9l7-4.5-7-4.5z" fill="currentColor"/></svg>';
      }

      function plusIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M7 2v10M2 7h10" stroke="currentColor" stroke-width="1.3"/></svg>';
      }

      function escapeHtml(str) {
        return String(str)
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;");
      }

      function renderGallery() {
        const cards = works.map(function (work, i) {
          const featured = i === 0 ? " featured" : "";
          const tags = (work.tags || []).map(function (t) {
            return "<span>" + escapeHtml(t) + "</span>";
          }).join("");
          return (
            '<article class="still' + featured + '" data-id="' + escapeHtml(work.id) + '" tabindex="0" role="link" aria-label="' + escapeHtml(work.title) + ' 실행">' +
              '<div class="frame">' +
                '<img src="' + escapeHtml(work.thumbnail) + '" alt="' + escapeHtml(work.title) + ' 썸네일" />' +
                '<div class="shade"></div>' +
                '<span class="play">' + playIcon() + '</span>' +
                '<span class="run-cue">실행 →</span>' +
                (i === 0 ? '<span class="ember-bar" aria-hidden="true"></span>' : '') +
              '</div>' +
              '<div class="still-meta">' +
                '<h3>' + escapeHtml(work.title) + '</h3>' +
                '<div class="labels"><span>' + escapeHtml(work.year) + '</span>' + tags + '</div>' +
              '</div>' +
            '</article>'
          );
        }).join("");

        const addTile =
          '<button type="button" class="still add-tile" data-add>' +
            '<div class="frame">' +
              '<div class="add-inner">' +
                '<span class="plus">' + plusIcon() + '</span>' +
                '<p>썸네일을 넣고 작품을 등록</p>' +
              '</div>' +
            '</div>' +
          '</button>';

        gallery.innerHTML = cards + addTile;
        workCount.textContent = "선정 작품 " + works.length;
      }

      function findWork(id) {
        return works.find(function (w) { return w.id === id; });
      }

      function runnableUrl(url) {
        if (!url) return "";
        var trimmed = String(url).trim();
        if (!trimmed || trimmed === "#" || trimmed === "about:blank") return "";
        return trimmed;
      }

      function morphThenGo(card, id) {
        if (reduceMotion) {
          location.hash = "#/run/" + encodeURIComponent(id);
          return;
        }
        var img = card.querySelector("img");
        if (!img) {
          location.hash = "#/run/" + encodeURIComponent(id);
          return;
        }
        var r = img.getBoundingClientRect();
        var clone = img.cloneNode(true);
        clone.className = "morph-clone";
        clone.style.top = r.top + "px";
        clone.style.left = r.left + "px";
        clone.style.width = r.width + "px";
        clone.style.height = r.height + "px";
        clone.style.transition = "top 0.72s cubic-bezier(0.22, 1, 0.36, 1), left 0.72s cubic-bezier(0.22, 1, 0.36, 1), width 0.72s cubic-bezier(0.22, 1, 0.36, 1), height 0.72s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.35s ease";
        document.body.appendChild(clone);
        requestAnimationFrame(function () {
          var wide = window.innerWidth > 1024;
          clone.style.top = "61px";
          clone.style.left = "16px";
          clone.style.width = wide ? "calc(100% - 332px)" : "calc(100% - 32px)";
          clone.style.height = wide ? "calc(100% - 77px)" : "48vh";
        });
        window.setTimeout(function () {
          location.hash = "#/run/" + encodeURIComponent(id);
          clone.style.opacity = "0";
          window.setTimeout(function () { clone.remove(); }, 380);
        }, 720);
      }

      function showIndex() {
        document.body.classList.remove("is-running");
        var frame = document.getElementById("run-frame");
        frame.hidden = true;
        frame.removeAttribute("src");
      }

      function showRun(id) {
        var work = findWork(id);
        if (!work) {
          location.hash = "#/";
          return;
        }
        document.body.classList.add("is-running");
        document.getElementById("run-title").textContent = work.title;
        document.getElementById("run-tags").innerHTML = (work.tags || []).map(function (t) {
          return "<span>" + escapeHtml(t) + "</span>";
        }).join("");
        document.getElementById("run-poster").src = work.thumbnail;
        document.getElementById("run-poster").alt = work.title + " 포스터";
        document.getElementById("run-poster").classList.remove("is-gone");
        document.getElementById("strip-thumb").src = work.thumbnail;
        document.getElementById("strip-thumb").alt = work.title + " 스틸";
        document.getElementById("strip-desc").textContent = work.description || "";
        document.getElementById("strip-year").textContent = work.year;

        var url = runnableUrl(work.url);
        var frame = document.getElementById("run-frame");
        var empty = document.getElementById("empty-stage");
        var openTab = document.getElementById("open-tab");
        empty.style.setProperty("--thumb", "url('" + work.thumbnail.replace(/'/g, "%27") + "')");

        if (!url) {
          frame.hidden = true;
          frame.removeAttribute("src");
          empty.classList.add("is-on");
          openTab.setAttribute("aria-disabled", "true");
          openTab.href = "#";
          openTab.classList.add("is-off");
          openTab.style.opacity = "0.4";
          openTab.style.pointerEvents = "none";
          document.getElementById("run-poster").classList.add("is-gone");
          return;
        }

        empty.classList.remove("is-on");
        openTab.removeAttribute("aria-disabled");
        openTab.style.opacity = "";
        openTab.style.pointerEvents = "";
        openTab.href = url;
        frame.hidden = false;
        frame.title = work.title + " 실행 화면";
        frame.onload = function () {
          document.getElementById("run-poster").classList.add("is-gone");
        };
        frame.src = url;
      }

      function route() {
        var hash = (location.hash || "#/").replace(/^#/, "") || "/";
        var run = hash.match(/^\/run\/(.+)$/);
        if (run) showRun(decodeURIComponent(run[1]));
        else showIndex();
      }

      gallery.addEventListener("click", function (e) {
        if (e.target.closest("[data-add]")) {
          openStudio();
          return;
        }
        var card = e.target.closest("[data-id]");
        if (card) morphThenGo(card, card.getAttribute("data-id"));
      });

      gallery.addEventListener("keydown", function (e) {
        var card = e.target.closest("[data-id]");
        if (!card) return;
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          morphThenGo(card, card.getAttribute("data-id"));
        }
      });

      document.getElementById("back-index").addEventListener("click", function () {
        location.hash = "#/";
      });
      document.querySelector("[data-home]").addEventListener("click", function (e) {
        e.preventDefault();
        location.hash = "#/";
      });

      function openStudio() {
        formError.textContent = "";
        studio.showModal();
        document.getElementById("field-title").focus();
      }
      function closeStudio() {
        studio.close();
      }

      document.getElementById("open-studio").addEventListener("click", openStudio);
      document.getElementById("close-studio").addEventListener("click", closeStudio);
      document.getElementById("cancel-studio").addEventListener("click", closeStudio);

      studio.addEventListener("click", function (e) {
        var rect = studio.getBoundingClientRect();
        if (e.target === studio && (e.clientX < rect.left)) closeStudio();
      });

      function acceptFile(file) {
        if (!file) return;
        if (!/^image\/(jpeg|png|webp)$/i.test(file.type)) {
          formError.textContent = "JPG, PNG, WEBP만 사용할 수 있습니다.";
          return;
        }
        var reader = new FileReader();
        reader.onload = function () {
          pendingThumb = String(reader.result || "");
          thumbPreview.src = pendingThumb;
          thumbPreview.hidden = false;
          drop.classList.add("has-preview");
          formError.textContent = "";
        };
        reader.readAsDataURL(file);
      }

      thumbInput.addEventListener("change", function () {
        acceptFile(thumbInput.files && thumbInput.files[0]);
      });
      ["dragenter", "dragover"].forEach(function (ev) {
        drop.addEventListener(ev, function (e) {
          e.preventDefault();
          drop.classList.add("is-hot");
        });
      });
      ["dragleave", "drop"].forEach(function (ev) {
        drop.addEventListener(ev, function (e) {
          e.preventDefault();
          drop.classList.remove("is-hot");
        });
      });
      drop.addEventListener("drop", function (e) {
        var file = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
        acceptFile(file);
      });

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!pendingThumb) {
          formError.textContent = "썸네일 이미지를 넣어 주세요.";
          return;
        }
        var title = document.getElementById("field-title").value.trim();
        if (!title) {
          formError.textContent = "제목을 입력해 주세요.";
          return;
        }
        var tags = document.getElementById("field-tags").value
          .split(/[,，]/)
          .map(function (t) { return t.trim(); })
          .filter(Boolean)
          .slice(0, 3);
        works.push({
          id: "work-" + Date.now(),
          title: title,
          year: String(document.getElementById("field-year").value || "2026"),
          tags: tags,
          description: document.getElementById("field-desc").value.trim(),
          thumbnail: pendingThumb,
          url: document.getElementById("field-url").value.trim()
        });
        saveWorks();
        renderGallery();
        form.reset();
        pendingThumb = "";
        thumbPreview.hidden = true;
        thumbPreview.removeAttribute("src");
        drop.classList.remove("has-preview");
        document.getElementById("field-year").value = "2026";
        closeStudio();
      });

      if (!reduceMotion) {
        window.addEventListener("pointermove", function (e) {
          spot.style.transform = "translate3d(" + (e.clientX - spot.offsetWidth / 2) + "px," + (e.clientY - spot.offsetHeight / 2) + "px,0)";
        }, { passive: true });
      }

      window.addEventListener("hashchange", route);
      renderGallery();
      route();
    })();
  </script>
</body>
</html>
