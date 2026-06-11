#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sunday Suite — bilingual static-site generator.
EN -> site root (primary).  NO -> /no/.  Shared assets in /assets/.
Run:  python3 build.py
"""
import os
ROOTDIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------- icons
IC = {
 "rec":'<circle cx="12" cy="12" r="4" fill="currentColor" stroke="none"/><path d="M12 2a10 10 0 0 1 0 20"/><path d="M2 12a10 10 0 0 0 6 9.3"/>',
 "mic":'<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v4M8 22h8"/>',
 "screen":'<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M10 9l4 2.5-4 2.5z" fill="currentColor" stroke="none"/><path d="M8 21h8M12 17v4"/>',
 "calendar":'<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/><path d="M8 14l2.5 2.5L16 12"/>',
 "note":'<path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3" fill="currentColor" stroke="none"/><circle cx="17" cy="16" r="3" fill="currentColor" stroke="none"/>',
 "caption":'<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M6 10h5M6 14h8" stroke-width="2.4"/>',
 "doc":'<path d="M6 2h8l4 4v16H6z"/><path d="M14 2v4h4M9 13h6M9 17h6M9 9h2"/>',
 "check":'<path d="M20 6L9 17l-5-5"/>',
 "bolt":'<path d="M13 2L3 14h7l-1 8 10-12h-7z"/>',
 "wave":'<path d="M2 12h3l2-7 4 16 3-11 2 5h6"/>',
 "layers":'<path d="M12 2l9 5-9 5-9-5z"/><path d="M3 12l9 5 9-5"/>',
 "search":'<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',
 "sliders":'<path d="M4 7h16M4 17h16"/><circle cx="9" cy="7" r="2.4" fill="currentColor" stroke="none"/><circle cx="15" cy="17" r="2.4" fill="currentColor" stroke="none"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/>',
 "shield":'<path d="M12 2l8 3v6c0 5-3.5 8-8 11-4.5-3-8-6-8-11V5z"/>',
 "bell":'<path d="M6 9a6 6 0 0 1 12 0c0 7 3 7 3 9H3c0-2 3-2 3-9z"/><path d="M10.5 21a2.4 2.4 0 0 0 3 0"/>',
 "sparkle":'<path d="M12 3l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>',
 "text":'<path d="M4 6h16M4 12h10M4 18h7"/>',
 "star":'<path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/>',
 "code":'<path d="M8 9l-4 3 4 3M16 9l4 3-4 3M13 5l-2 14"/>',
 "focus":'<circle cx="12" cy="12" r="3"/><path d="M3 7V4h3M21 7V4h-3M3 17v3h3M21 17v3h-3"/>',
 "stack":'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "people":'<circle cx="9" cy="8" r="3.5"/><path d="M3 21c0-3.3 2.7-5 6-5s6 1.7 6 5"/><path d="M16 6a3 3 0 0 1 0 6M22 21c0-2.5-1.4-4-4-4.5"/>',
 "split":'<path d="M6 3v6a3 3 0 0 0 3 3h6a3 3 0 0 1 3 3v6"/><path d="M3 6h6M15 18h6"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "arrowne":'<path d="M7 17L17 7M9 7h8v8"/>',
}
def sv(k, sw="2"):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg>'
CROSS = '<svg class="mark cross" viewBox="0 0 20 26"><path d="M8 0h4v8h8v4h-8v14H8V12H0V8h8z"/></svg>'
DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
 '<linearGradient id="goldgrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2D58A"/><stop offset="1" stop-color="#EBB84B"/></linearGradient>'
 '<linearGradient id="threadgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EBB84B" stop-opacity="0"/><stop offset=".35" stop-color="#EBB84B" stop-opacity=".9"/><stop offset="1" stop-color="#D4A23A" stop-opacity=".25"/></linearGradient>'
 '</defs></svg>')

# --------------------------------------------------------------------- chrome
CH = {
 "en":{"lang":"en","other":"NO","nav_products":"Products","nav_phil":"Philosophy","nav_together":"Together",
   "nav_cta":"Get in touch","all_products":"All products","keep_posted":"Keep me posted",
   "status_build":"In development","status_beta":"Beta · free","family_kicker":"Part of the family",
   "family_title":"Plays well with the rest of Sunday Suite","standalone_title":"Standalone — but part of the family",
   "standalone_lead":"The tool stands entirely on its own, but shares the account, design language and golden thread with the rest of Sunday Suite.",
   "status_head":"Status: in development","what_kicker":"What it does",
   "foot_tag":"A family of Norwegian-built tools for the modern church. Seven apps, one golden thread.",
   "foot_products":"Products","foot_suite":"The suite","foot_legal":"Legal","foot_terms":"Terms of Use","foot_privacy":"Privacy",
   "foot_phil":"Philosophy","foot_together":"Better together","foot_toolbox":"Community tools","foot_contact":"Contact",
   "foot_bottom":"&copy; 2026 Sunday Suite &middot; Richard Fossland. Built in Norway.",
   "back_home":"&larr; Back to home","cta_back":"Back to the products"},
 "no":{"lang":"no","other":"EN","nav_products":"Produkter","nav_phil":"Filosofi","nav_together":"Sammen",
   "nav_cta":"Ta kontakt","all_products":"Alle produkter","keep_posted":"Hold meg oppdatert",
   "status_build":"Under utvikling","status_beta":"Beta · gratis","family_kicker":"Del av familien",
   "family_title":"Spiller sammen med resten av Sunday Suite","standalone_title":"Frittstående — men en del av familien",
   "standalone_lead":"Verktøyet står helt på egne bein, men deler konto, designspråk og den gylne tråden med resten av Sunday Suite.",
   "status_head":"Status: under utvikling","what_kicker":"Hva det gjør",
   "foot_tag":"En familie av norskbygde verktøy for den moderne menigheten. Sju apper, én gylden tråd.",
   "foot_products":"Produkter","foot_suite":"Suiten","foot_legal":"Juridisk","foot_terms":"Vilkår for bruk","foot_privacy":"Personvern",
   "foot_phil":"Filosofi","foot_together":"Bedre sammen","foot_toolbox":"Fellesskapsverktøy","foot_contact":"Kontakt",
   "foot_bottom":"&copy; 2026 Sunday Suite &middot; Richard Fossland. Bygd i Norge.",
   "back_home":"&larr; Tilbake til forsiden","cta_back":"Tilbake til produktene"},
}
SLUGS = ["sundayrec","sundaystudio","sundaystage","sundayplan","sundaysong","sundayedit","sundaypaper"]
PNAME = {"sundayrec":"SundayRec","sundaystudio":"SundayStudio","sundaystage":"SundayStage",
         "sundayplan":"SundayPlan","sundaysong":"SundaySong","sundayedit":"SundayEdit","sundaypaper":"SundayPaper"}

def links(lang, root):
    base = "" if lang=="en" else "no/"
    return {
      "assets": root+"assets/",
      "home":   root+base+"index.html",
      "app":    lambda s: root+base+"apps/"+s+".html",
      "legal":  lambda n: root+base+"legal/"+n+".html",
    }

def nav(c, L, other_href):
    return (f'<header class="nav" id="nav"><div class="wrap nav-inner">'
      f'<a href="{L["home"]}" class="brand">{CROSS}<span><b>Sunday</b> Suite</span></a>'
      f'<nav class="links">'
      f'<a href="{L["home"]}#products" class="linkitem">{c["nav_products"]}</a>'
      f'<a href="{L["home"]}#philosophy" class="linkitem">{c["nav_phil"]}</a>'
      f'<a href="{other_href}" class="lang-switch">{c["other"]}</a>'
      f'<a href="mailto:dev@sundaysuite.app" class="nav-cta">{c["nav_cta"]}</a>'
      f'</nav></div></header>')

def footer(c, L):
    prod = "".join(f'<a href="{L["app"](s)}">{PNAME[s]}</a>' for s in SLUGS)
    return (f'<footer><div class="wrap"><div class="foot-top">'
      f'<div class="foot-brand"><div class="brand">{CROSS}<span><b>Sunday</b> Suite</span></div><p>{c["foot_tag"]}</p></div>'
      f'<div class="foot-cols">'
      f'<div class="foot-col"><h5>{c["foot_products"]}</h5>{prod}</div>'
      f'<div class="foot-col"><h5>{c["foot_suite"]}</h5><a href="{L["home"]}#philosophy">{c["foot_phil"]}</a><a href="{L["home"]}#together">{c["foot_together"]}</a><a href="{L["home"]}#toolbox">{c["foot_toolbox"]}</a><a href="mailto:dev@sundaysuite.app">{c["foot_contact"]}</a></div>'
      f'<div class="foot-col"><h5>{c["foot_legal"]}</h5><a href="{L["legal"]("terms")}">{c["foot_terms"]}</a><a href="{L["legal"]("privacy")}">{c["foot_privacy"]}</a></div>'
      f'</div></div>'
      f'<div class="foot-bottom"><div>{c["foot_bottom"]}</div><div><a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> &middot; sundaysuite.app</div></div>'
      f'</div></footer>')

def shell(c, L, other_href, title, desc, body_open, content, navscrolled=False):
    nv = nav(c, L, other_href)
    if navscrolled: nv = nv.replace('class="nav"','class="nav scrolled"')
    return (f'<!DOCTYPE html>\n<html lang="{c["lang"]}">\n<head>\n<meta charset="UTF-8" />\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
      f'<title>{title}</title>\n<meta name="description" content="{desc}" />\n'
      f'<link rel="icon" href="{L["assets"]}favicon.svg" type="image/svg+xml" />\n'
      f'<meta property="og:title" content="{title}" />\n<meta property="og:description" content="{desc}" />\n'
      f'<meta property="og:type" content="website" />\n<meta property="og:site_name" content="Sunday Suite" />\n<meta name="twitter:card" content="summary" />\n'
      f'<link rel="preconnect" href="https://fonts.googleapis.com" />\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
      f'<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,900;1,500&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />\n'
      f'<link rel="stylesheet" href="{L["assets"]}site.css" />\n</head>\n<body{body_open}>\n\n{DEFS}\n\n{nv}\n\n{content}\n\n{footer(c,L)}\n\n'
      f'<script src="{L["assets"]}site.js"></script>\n</body>\n</html>\n')

# ===================================================================== HOME
HOME = {
 "en":{"title":"Sunday Suite — Tools for the modern church",
   "desc":"Sunday Suite is a family of Norwegian-built tools for the church: recording, presentation, planning, song, podcasting, captioning and print — bound together by one golden thread.",
   "eyebrow":"Norwegian-built church technology · in development",
   "h1":'Seven tools.<br><em>One golden thread.</em>',
   "sub":"Sunday Suite is a family of programs for the modern church — from recording and streaming to presentation, planning, song, podcasting, captioning and print. Each tool stands on its own, but they share one account, one design language, and one thread of gold.",
   "b1":"See the products","b2":"Why Sunday?",
   "m1":"<b>7</b> products, one ecosystem","m2":"<b>TONO &amp; CCLI</b> built in from day one","m3":"<b>Local-first</b> — your data stays with you",
   "g_kicker":"The products","g_title":"The family of Sunday apps",
   "g_lead":"Seven tools in active development. Each product owns its own deep jewel tone, and the golden cross binds them together. Click through to read more about each one.",
   "one_h":"One Sunday account","one_tag":"Sign in once",
   "one_p":"The goal: one account signs you into every tool, and what you do in one program shows up where it's needed in the others — no double work.",
   "one_f":["Single sign-on","Shared design language","Secure key handling"],
   "p_kicker":"The philosophy","p_h2":'The first church-technology ecosystem built for <em>Nordic reality</em>.',
   "p_lead":"The world's best church tools are built for American churches. Sunday Suite starts with the Norwegian and Nordic reality — TONO, Bokmål and Nynorsk, privacy and local control — and has global ambitions from there.",
   "moat":[("star","TONO as a first-class citizen","Every work has a TONO ID from day one, and every use knows whether it was streamed — a separate royalty pool. No US competitor does this."),
           ("shield","Local and private first","Recording, video and transcription run on your own machine. Your data stays with you unless you choose to share it."),
           ("people","One account, all Sunday","The goal is one sign-in across Rec, Stage, Plan and Song, with keys kept safely in the keychain.")],
   "mg_kicker":"Better together","mg_title":"When the tools talk to each other",
   "mg_lead":"The real magic happens at the seams. This is how the Sunday apps are designed to play together as they're finished.",
   "chips":[("Stage","Rec","cue becomes a chapter marker"),("Stage","Rec","lyrics become SRT captions"),
            ("Plan","Stage","setlist becomes a published service"),("Rec","Plan","transcript returns as metadata"),
            ("Stage","Song","every shown song is logged for TONO/CCLI"),("Plan","Paper","setlist becomes a printed program in one click"),
            ("Paper","Song","a scanned songbook becomes catalog entries"),("Rec","Paper","the sermon becomes a parish-magazine draft"),
            ("Rec","Edit","sermon + transcript ready for captioning")],
   "tb_kicker":"Beyond the suite","tb_title":"A little toolbox for building community",
   "tb_lead":"Alongside the seven core products, Sunday Suite tinkers with small, playful tools for church and classroom — games and group activities that help people meet, mix and connect. They run straight in the browser, nothing to install. A corner of the workshop that will keep growing.",
   "tb_note":"More fellowship tools are on the workbench. Have an idea for one?",
   "tb_open":"Open","tb_soon":"Coming soon",
   "cta_h":"Let's build a better Sunday together.",
   "cta_p":"Want to try the SundayRec beta, collaborate, or just hear where Sunday Suite is headed? We'd love to hear from you.",
   "cta_back":"Back to the products"},
 "no":{"title":"Sunday Suite — Verktøyene for den moderne menigheten",
   "desc":"Sunday Suite er en familie av norskbygde verktøy for menigheten: opptak, presentasjon, planlegging, sang, podkast, teksting og dokumenter — bundet sammen av én gylden tråd.",
   "eyebrow":"Norskbygd kirketeknologi · under utvikling",
   "h1":'Sju verktøy.<br><em>Én gylden tråd.</em>',
   "sub":"Sunday Suite er en familie av programmer for den moderne menigheten — fra opptak og strømming til presentasjon, planlegging, sang, podkast, teksting og trykksaker. Hvert verktøy står på egne bein, men deler én konto, ett designspråk og én tråd av gull.",
   "b1":"Se programmene","b2":"Hvorfor Sunday?",
   "m1":"<b>7</b> produkter, ett økosystem","m2":"<b>TONO &amp; CCLI</b> innebygd fra dag én","m3":"<b>Lokalt først</b> — dine data blir hos deg",
   "g_kicker":"Produktene","g_title":"Familien av Sunday-apper",
   "g_lead":"Sju verktøy under utvikling. Hvert produkt eier sin egen dype juveltone, og det gylne korset binder dem sammen. Klikk deg inn for å lese mer om hvert program.",
   "one_h":"Én Sunday-konto","one_tag":"Logg inn én gang",
   "one_p":"Målet: én konto signerer deg inn på alle verktøyene, og det du gjør i ett program dukker opp der det trengs i de andre — uten dobbeltarbeid.",
   "one_f":["Felles innlogging","Delt designspråk","Sikker nøkkelhåndtering"],
   "p_kicker":"Filosofien","p_h2":'Det første kirketeknologi&shy;økosystemet bygd for <em>nordisk virkelighet</em>.',
   "p_lead":"Verdens beste menighetsverktøy er bygd for amerikanske kirker. Sunday Suite starter med den norske og nordiske hverdagen — TONO, bokmål og nynorsk, personvern og lokal kontroll — og har globale ambisjoner derfra.",
   "moat":[("star","TONO i førsteklasse","Hvert verk har TONO-ID fra dag én, og hver bruk vet om den ble strømmet — egen royalty-pott. Ingen amerikansk konkurrent gjør dette."),
           ("shield","Lokalt og privat først","Opptak, video og transkripsjon kjøres på din egen maskin. Dataene blir hos deg med mindre du selv velger å dele."),
           ("people","Én konto, hele søndagen","Målet er at én innlogging signerer deg inn på Rec, Stage, Plan og Song, med nøkler trygt i nøkkelringen.")],
   "mg_kicker":"Bedre sammen","mg_title":"Når verktøyene snakker sammen",
   "mg_lead":"Den virkelige magien skjer i skjøtene. Slik er Sunday-appene designet for å spille sammen etter hvert som de blir ferdige.",
   "chips":[("Stage","Rec","cue blir kapittelmerke i opptaket"),("Stage","Rec","sangtekst blir SRT-teksting"),
            ("Plan","Stage","setliste blir publisert gudstjeneste"),("Rec","Plan","transkripsjon tilbake som metadata"),
            ("Stage","Song","hver vist sang loggføres for TONO/CCLI"),("Plan","Paper","setliste blir trykt program med ett klikk"),
            ("Paper","Song","skannet sangbok blir katalogoppføringer"),("Rec","Paper","preken blir menighetsblad-utkast"),
            ("Rec","Edit","preken + transkripsjon klar for teksting")],
   "tb_kicker":"Utenfor suiten","tb_title":"En liten verktøykasse for å bygge fellesskap",
   "tb_lead":"Ved siden av de sju kjerneproduktene snekrer Sunday Suite på små, lekne verktøy for menighet og klasserom — spill og gruppeaktiviteter som hjelper folk å møtes, bli kjent og knytte bånd. De kjører rett i nettleseren, uten installasjon. En krok av verkstedet som bare kommer til å vokse.",
   "tb_note":"Flere fellesskapsverktøy ligger på arbeidsbenken. Har du en idé til ett?",
   "tb_open":"Åpne","tb_soon":"Kommer snart",
   "cta_h":"La oss bygge en bedre søndag sammen.",
   "cta_p":"Vil du teste SundayRec-betaen, samarbeide eller bare høre mer om hvor Sunday Suite er på vei? Vi vil gjerne høre fra deg.",
   "cta_back":"Tilbake til produktene"},
}

# per-card teaser content (tag / desc / feats), keyed by slug then lang
CARD = {
 "sundayrec":{"accent":"rec","icon":"rec","status":"beta",
   "en":("Record · stream · publish","Records the service, transcribes the sermon, streams live and publishes the podcast — by itself. The mature core of the suite, out in beta.",["Audio &amp; video","Live stream","AI transcription","Podcast"]),
   "no":("Opptak · strømming · podkast","Tar opp gudstjenesten, transkriberer talen, strømmer live og publiserer podkasten — av seg selv. Den modne kjernen i suiten, ute i beta.",["Lyd &amp; video","Live-strøm","AI-transkripsjon","Podkast"])},
 "sundaystudio":{"accent":"studio","icon":"mic","status":"build",
   "en":("Podcast &amp; jingle production","The simplest professional podcast producer: many mics at once, AI cleanup, a jingle in under a minute, and a finished, normalized MP3.",["Multi-mic","AI mastering","Jingle","Export"]),
   "no":("Podkast- &amp; jingleproduksjon","Den enkleste proffe podkastprodusenten: mange mikrofoner samtidig, AI-opprydding, en jingle på under ett minutt og en ferdig, normalisert MP3.",["Fleirmikrofon","AI-mastering","Jingle","Eksport"])},
 "sundaystage":{"accent":"stage","icon":"screen","status":"build",
   "en":("On-screen presentation","Lyrics, Bible verses and media on the screen behind the altar — a Nordic alternative to ProPresenter, with cue control and safe, isolated output.",["Lyrics","Cues","Media","⌘K palette"]),
   "no":("Presentasjon på storskjerm","Sangtekster, bibelvers og media på skjermen bak alteret — et nordisk alternativ til ProPresenter, med køstyring og trygg, isolert visning.",["Sangtekster","Køer","Media","⌘K-palett"])},
 "sundayplan":{"accent":"plan","icon":"calendar","status":"build",
   "en":("Planning &amp; volunteer rota","Plan the service and schedule volunteers in minutes. A fair auto-fill engine balances skill, rotation and burnout.",["Service plan","Auto-rota","SMS","TONO status"]),
   "no":("Planlegging &amp; frivillig-turnus","Planlegg gudstjenesten og sett opp de frivillige på minutter. En rettferdig auto-fyll-motor balanserer kompetanse, rotasjon og utbrenthet.",["Tjenesteplan","Auto-turnus","SMS","TONO-status"])},
 "sundaysong":{"accent":"song","icon":"note","status":"build",
   "en":("Song database with AI &amp; TONO","Find the right song with semantic search and AI across languages — and get TONO and CCLI reporting for free. No US competitor does this.",["Semantic search","AI picks","TONO + CCLI","Multilingual"]),
   "no":("Sangdatabase med AI &amp; TONO","Finn riktig sang med semantisk søk og AI på tvers av språk — og få TONO- og CCLI-rapporteringen gratis på kjøpet. Ingen amerikansk konkurrent gjør dette.",["Semantisk søk","AI-forslag","TONO + CCLI","Fleirspråk"])},
 "sundayedit":{"accent":"edit","icon":"caption","status":"build",
   "en":("AI video captioning","Caption video ten times faster. Every word gets a confidence score and is colour-coded — you fix only the amber. Local and private: the video is never uploaded.",["Confidence","Context priming","Local Whisper","SRT/VTT"]),
   "no":("AI-teksting av video","Tekst video ti ganger raskere. Hvert ord får en konfidens-score og fargemarkeres — du retter bare det gule. Lokal og privat: videoen lastes aldri opp.",["Konfidens","Kontekst-priming","Lokal Whisper","SRT/VTT"])},
 "sundaypaper":{"accent":"paper-c","icon":"doc","status":"build",
   "en":("AI document &amp; PDF tool","Split songbooks, lay out service programs, parish magazines, large-print editions and forms — with professional Typst layout and OCR under the hood.",["Songbook split","Programs","Parish mag","Large print"]),
   "no":("AI-dokument &amp; PDF-verktøy","Splitt sangbøker, sett opp gudstjenesteprogrammer, lag menighetsblad, storskrift-utgaver og skjemaer — med profesjonell Typst-layout og OCR under panseret.",["Sangbok-splitt","Programmer","Menighetsblad","Storskrift"])},
}

# community-toolbox tools (live web apps on *.sundaysuite.app); soon=not yet deployed
TOOLS = [
 {"name":"SundayQuiz","accent":"quiz","url":"https://quiz.sundaysuite.app","live":True,
  "en":("Icebreaker","Get-to-know-you bingo for a first gathering — everyone hunts for people who match the squares, and the room warms up fast."),
  "no":("Bli kjent","Bli-kjent-bingo for første samling — alle jakter på folk som passer rutene, og rommet tiner opp på et blunk.")},
 {"name":"SundayChess","accent":"chess","url":"https://chess.sundaysuite.app","live":True,
  "en":("Classroom","A Kahoot-style chess tournament for the classroom — Swiss rounds and a knockout, run from one screen with a solo bot to practice against."),
  "no":("Klasserom","Sjakkturnering i Kahoot-stil for klasserommet — sveitsiske runder og sluttspill, styrt fra én skjerm, med solo-bot å øve mot.")},
 {"name":"SundayTurnering","accent":"turnering","url":"https://turnering.sundaysuite.app","live":True,
  "en":("Sport &amp; play","A live tournament board for any sport or game — leagues, cups and playoffs, with a big-screen view and a phone in every hand."),
  "no":("Idrett &amp; lek","Live turneringstavle for hvilken som helst idrett eller lek — serie, cup og sluttspill, med storskjerm-visning og en telefon i hver hånd.")},
 {"name":"SundayMarket","accent":"market","url":"https://marked.sundaysuite.app","live":True,
  "en":("Group game","A fast, friendly trading game for a group — buy low, sell high, dodge the famine and out-trade the table before the bell."),
  "no":("Gruppespill","Et kjapt og vennlig handelsspill for en gruppe — kjøp billig, selg dyrt, unngå hungersnøden og slå bordet før det ringer ut.")},
 {"name":"SundayHarvest","accent":"harvest","url":"https://harvest.sundaysuite.app","live":True,
  "en":("Party game","Biblical social deduction — wheat among the tares (Matthew 13). No one gets eliminated; everyone plays to the final reveal."),
  "no":("Selskapsspill","Bibelsk social deduction — hvete blant ugresset (Matteus 13). Ingen elimineres; alle er med helt til den store avsløringen.")},
]

def render_toolbox(lang, h, c, L):
    arrow = sv("arrowne","2.5")
    cards=""
    for i,t in enumerate(TOOLS):
        tag,desc=t[lang]; live=t["live"]; d=f' data-d="{(i%3)+1}"' if i%3 else ""
        suffix=t["name"][6:]
        inner=(f'<div class="tb-top"><span class="tb-dot"></span><span class="tb-tag">{tag}</span></div>'
          f'<h4><span class="sunday">Sunday</span>{suffix}</h4><p>{desc}</p>')
        if live:
            cards+=(f'      <a class="tb-card reveal"{d} style="--c:var(--{t["accent"]})" href="{t["url"]}" '
              f'target="_blank" rel="noopener">{inner}'
              f'<span class="tb-go">{h["tb_open"]}{arrow}</span></a>\n')
        else:
            cards+=(f'      <div class="tb-card soon reveal"{d} style="--c:var(--{t["accent"]})">{inner}'
              f'<span class="tb-go">{h["tb_soon"]}</span></div>\n')
    return (f'''<section class="toolbox" id="toolbox"><div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{h["tb_kicker"]}</div><h2 class="section-title">{h["tb_title"]}</h2><p class="section-lead">{h["tb_lead"]}</p></div>
  <div class="tb-grid">
{cards}  </div>
  <p class="tb-note reveal">{h["tb_note"]} <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a></p>
</div></section>''')

def status_badge(st, c):
    if st=="beta": return f'<span class="status beta">{c["status_beta"].split(" ·")[0] if False else ("Beta" if c["lang"]=="en" else "Beta")}</span>'
    return f'<span class="status build">{c["status_build"]}</span>'

def render_home(lang):
    c=CH[lang]; h=HOME[lang]; root="" if lang=="en" else "../"; L=links(lang,root)
    other = "no/index.html" if lang=="en" else "../index.html"
    arrow = sv("arrow","2.5")
    readmore = "Read more" if lang=="en" else "Les mer"
    cards=""
    for i,s in enumerate(SLUGS):
        cd=CARD[s]; tag,desc,feats=cd[lang]; d=f' data-d="{(i%3)+1}"' if i%3 else f' data-d="1"'
        feats_html="".join(f"<li>{x}</li>" for x in feats)
        cards+=(f'      <a class="card link reveal"{d} style="--c:var(--{cd["accent"]})" href="{L["app"](s)}">'
          f'<span class="glowdot"></span><div class="card-top"><img class="logo-tile" src="{L["assets"]}logos/{s}.svg" alt="{PNAME[s]} logo" width="52" height="52" loading="lazy" />'
          f'{status_badge(cd["status"],c)}</div>'
          f'<h3><span class="sunday">Sunday</span>{PNAME[s][6:]}</h3><div class="tag">{tag}</div>'
          f'<p>{desc}</p><ul class="feats">{feats_html}</ul>'
          f'<span class="more">{readmore}{arrow}</span></a>\n')
    one_f="".join(f"<li>{x}</li>" for x in h["one_f"])
    cards+=(f'      <div class="card reveal" data-d="5" style="--c:var(--gold-deep); background:linear-gradient(160deg,#fff,#FBF3DF)">'
      f'<div class="card-top"><div class="icon-tile" style="background:var(--gold-grad); color:#14171E; box-shadow:none">'
      f'<svg class="cross" viewBox="0 0 20 26" style="width:18px;height:24px"><path d="M8 0h4v8h8v4h-8v14H8V12H0V8h8z"/></svg></div></div>'
      f'<h3 style="color:var(--gold-deep)">{h["one_h"]}</h3><div class="tag" style="color:var(--gold-deep)">{h["one_tag"]}</div>'
      f'<p style="color:var(--txt-on-paper-dim)">{h["one_p"]}</p><ul class="feats">{one_f}</ul></div>\n')
    moat="".join(f'<div class="row"><div class="ico">{sv(ic)}</div><div><h4>{t}</h4><p>{d}</p></div></div>' for ic,t,d in h["moat"])
    chips="".join(f'<div class="chip"><span class="from">{a}</span><span class="arrow">&rarr;</span><span class="to">{b}</span>&nbsp;{t}</div>' for a,b,t in h["chips"])
    content=(f'''<main id="top">
<section class="hero"><div class="hero-bg"><div class="glow"></div><div class="grain"></div></div>
  <div class="wrap hero-inner">
    <span class="eyebrow reveal in"><span class="dot"></span>{h["eyebrow"]}</span>
    <h1 class="hero-title reveal in" data-d="1">{h["h1"]}</h1>
    <p class="hero-sub reveal in" data-d="2">{h["sub"]}</p>
    <div class="hero-actions reveal in" data-d="3"><a href="#products" class="btn btn-primary">{h["b1"]}</a><a href="#philosophy" class="btn btn-ghost">{h["b2"]}</a></div>
    <div class="hero-meta reveal in" data-d="4"><div>{h["m1"]}</div><div>{h["m2"]}</div><div>{h["m3"]}</div></div>
  </div>
  <div class="thread" aria-hidden="true"><svg viewBox="0 0 40 130" preserveAspectRatio="none"><path class="line" d="M20 0 C20 50 8 60 20 90 C30 115 20 120 20 130"/></svg></div>
</section>

<section class="gallery" id="products"><div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{h["g_kicker"]}</div><h2 class="section-title">{h["g_title"]}</h2><p class="section-lead">{h["g_lead"]}</p></div>
  <div class="grid">
{cards}  </div>
</div></section>

<section class="philo" id="philosophy"><div class="glow"></div><div class="wrap philo-grid">
  <div class="reveal"><div class="section-kicker" style="color:var(--gold)">{h["p_kicker"]}</div><h2>{h["p_h2"]}</h2><p class="lead">{h["p_lead"]}</p></div>
  <div class="moat reveal" data-d="1">{moat}</div>
</div></section>

<section class="magic" id="together"><div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{h["mg_kicker"]}</div><h2 class="section-title">{h["mg_title"]}</h2><p class="section-lead">{h["mg_lead"]}</p></div>
  <div class="chips reveal" data-d="1">{chips}</div>
</div></section>

{render_toolbox(lang, h, c, L)}

<section class="cta"><div class="glow"></div><div class="wrap cta-inner reveal">
  <svg class="bigcross cross" viewBox="0 0 20 26"><path d="M8 0h4v8h8v4h-8v14H8V12H0V8h8z"/></svg>
  <h2>{h["cta_h"]}</h2><p>{h["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="mailto:dev@sundaysuite.app" class="btn btn-primary">dev@sundaysuite.app</a><a href="#products" class="btn btn-ghost">{h["cta_back"]}</a></div>
</div></section>
</main>''')
    return shell(c,L,other,h["title"],h["desc"]," id=\"top\"".replace(' id="top"',''),content)

# ===================================================================== APPS
APP = {
 "sundayrec":{"accent":"rec","icon":"rec",
  "en":{"tagline":"Your sermon, ready to share.",
    "meta":"SundayRec records the service, transcribes the sermon, streams live and publishes the podcast — by itself. Free beta for Mac and Windows. Your files stay yours.",
    "lead":"Set the schedule once. Every Sunday, SundayRec records the service, transcribes the sermon, streams it live, and publishes to your podcast — all by itself. Free desktop app for Mac and Windows. No subscription, no cloud relay. Your files stay yours.",
    "what":"The whole Sunday, from record to published","whatlead":"One app for a chain many churches solve today with five separate tools.",
    "features":[("rec","Scheduled recording","Enter the service times and recording starts and stops automatically — even if the machine is asleep."),
      ("bolt","Live streaming","Stream to YouTube, Facebook and more at once over RTMP — with overlays and lower-thirds."),
      ("text","AI transcription","Local speech-to-text transcribes the sermon on your own machine — nothing is uploaded."),
      ("wave","Built-in editor","Cut, adjust and master the audio with professional loudness normalization before publishing."),
      ("screen","NDI receiver","Record straight from ProPresenter, OBS or Keynote over the network — no extra capture card."),
      ("globe","Podcast publishing","Upload to YouTube and publish to a podcast RSS with review-before-publish, in one flow.")],
    "hl_kicker":"Built for trust","hl_title":"Local first. Your files never leave the machine — unless you ask.",
    "hl_p":"SundayRec is a desktop app, not a cloud service. Recording, editing and transcription happen on your own machine. If you enable cloud backup to Google Drive or publishing to a podcast host, the app uploads on your behalf — the relationship with that service is yours.",
    "checks":["No analytics, no telemetry","Backed by over 1000 automated tests","Seven languages, including Norwegian Bokmål and Nynorsk"],
    "status_head":"Status: beta",
    "status":"SundayRec is the mature core of the suite and can be downloaded and used for free today, but it's still in beta. Test your first recordings before relying on it for a critical service. This page on sundaysuite.app is SundayRec's home — there's no separate site to visit; downloads come straight from GitHub.",
    "cta_h":"Ready to record next Sunday?","cta_p":"Download SundayRec free for Mac and Windows — no account needed — or get in touch to follow development."},
  "no":{"tagline":"Prekenen din, klar til å deles.",
    "meta":"SundayRec tar opp gudstjenesten, transkriberer talen, strømmer live og publiserer podkasten — av seg selv. Gratis beta for Mac og Windows. Dine filer blir hos deg.",
    "lead":"Sett tidsplanen én gang. Hver søndag tar SundayRec opp gudstjenesten, transkriberer talen, strømmer den live og publiserer den til podkasten — helt av seg selv. Gratis skrivebordsapp for Mac og Windows. Ingen abonnement, ingen sky-relé. Filene dine blir dine.",
    "what":"Hele søndagen, fra opptak til publisert","whatlead":"Én app som dekker kjeden mange menigheter i dag løser med fem ulike verktøy.",
    "features":[("rec","Planlagt opptak","Legg inn gudstjenestetidene, så starter og stopper opptaket automatisk — selv om maskinen sover."),
      ("bolt","Live-strømming","Send direkte til YouTube, Facebook og flere samtidig over RTMP — med overlays og lower-thirds."),
      ("text","AI-transkripsjon","Lokal tale-til-tekst transkriberer prekenen på din egen maskin — ingenting lastes opp."),
      ("wave","Innebygd editor","Klipp, juster og masterer lyden med profesjonell loudness-normalisering før publisering."),
      ("screen","NDI-mottaker","Ta opp rett fra ProPresenter, OBS eller Keynote over nettverket — uten ekstra capture-kort."),
      ("globe","Podkast-publisering","Last opp til YouTube og publiser til podkast-RSS med review-før-publisering, i én flyt.")],
    "hl_kicker":"Bygd for tillit","hl_title":"Lokalt først. Filene dine forlater aldri maskinen — med mindre du ber om det.",
    "hl_p":"SundayRec er en skrivebordsapp, ikke en skytjeneste. Opptak, redigering og transkripsjon skjer på din egen maskin. Velger du sky-backup til Google Drive eller publisering til en podkast-host, er det appen som laster opp på dine vegne — forholdet til tjenesten er ditt.",
    "checks":["Ingen analyse, ingen telemetri","Over 1000 automatiske tester i ryggen","Sju språk, inkludert bokmål og nynorsk"],
    "status_head":"Status: beta",
    "status":"SundayRec er den modne kjernen i suiten og kan lastes ned og brukes gratis i dag, men er fortsatt i beta. Test gjerne de første opptakene før du stoler på den til en kritisk gudstjeneste. Denne siden på sundaysuite.app er hjemmebasen til SundayRec — det finnes ingen egen nettside å besøke; nedlasting kommer rett fra GitHub.",
    "cta_h":"Klar til å ta opp neste søndag?","cta_p":"Last ned SundayRec gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil følge utviklingen."},
  "chips":[("Stage","Rec","cue→chapter / cue blir kapittelmerke"),("Stage","Rec","lyrics→SRT / sangtekst blir SRT"),("Rec","Plan","transcript / transkripsjon"),("Rec","Edit","sermon ready / preken klar"),("Rec","Paper","sermon→magazine / preken→blad")],
 },
}

# Generic builder for the six in-development apps; rec is rendered specially.
APPDATA = {
 "sundaystudio":{"accent":"studio","icon":"mic","short":"Studio",
  "en":{"tagline":"The simplest professional podcast producer.",
    "meta":"SundayStudio is podcast and jingle production for churches: many mics at once, AI cleanup, a jingle in under a minute and a finished, LUFS-normalized MP3.",
    "lead":"Many microphones at once, AI-driven cleanup and leveling, a generated jingle in under a minute, and a finished LUFS-normalized MP3 ready for Spotify and Apple Podcasts. Simpler than GarageBand, friendlier than Audacity, far cheaper than the pro tools.",
    "what":"From raw take to finished episode","whatlead":"Everything you need for a professional church podcast, in one app.",
    "features":[("mic","Multi-track recording","Record 5–8 mics at once, each on its own track, with low-latency monitoring and solo/mute."),
      ("sparkle","AI cleanup","Automatic leveling and consistent sound across voices — no sound engineer required."),
      ("bolt","A jingle in a minute","Generate a finished theme tune for the podcast in under a minute."),
      ("wave","Waveform editor","Cut, crossfade, remove silence and bounce the timeline — not just whole takes."),
      ("sliders","Mastering &amp; loudness","Built-in DSP chain and LUFS normalization, ready for the streaming services."),
      ("layers","Finished export","Bounce to a mastered WAV and encode to MP3 in one click, ready to upload.")],
    "hl_kicker":"For the church","hl_title":"Professional podcasts without a sound engineer.",
    "hl_p":"SundayStudio takes the hard parts of audio production — levels, loudness, noise — and makes them automatic, so you can focus on the content.",
    "checks":["Quick-start templates for different recording formats","A project format that keeps all your raw material","Cheaper and simpler than the pro tools"],
    "status":"SundayStudio is well under way: the foundation, the multi-track recorder, the waveform editor, the DSP and mastering chain, the AI leveling and the export pipeline are in place. What remains needs real hardware, ffmpeg and live API keys. Not available for download yet.",
    "cta_h":"Want to hear when Studio is ready?","cta_p":"SundayStudio is in development. Get in touch to test early or follow the road to launch."},
  "no":{"tagline":"Den enkleste proffe podkastprodusenten.",
    "meta":"SundayStudio er podkast- og jingleproduksjon for menigheter: mange mikrofoner samtidig, AI-opprydding, jingle på minuttet og en ferdig, LUFS-normalisert MP3.",
    "lead":"Mange mikrofoner samtidig, AI-drevet opprydding og nivåjustering, en generert jingle på under ett minutt, og en ferdig LUFS-normalisert MP3 klar for Spotify og Apple Podcasts. Enklere enn GarageBand, vennligere enn Audacity, langt billigere enn proff-verktøyene.",
    "what":"Fra råopptak til ferdig episode","whatlead":"Alt du trenger for en proff menighetspodkast, samlet i én app.",
    "features":[("mic","Fleirspors-opptak","Ta opp 5–8 mikrofoner samtidig, hvert spor for seg, med lav-latens monitor og solo/mute."),
      ("sparkle","AI-opprydding","Automatisk nivåjustering og jevn lyd på tvers av stemmer — uten lydteknikar."),
      ("bolt","Jingle på minuttet","Generer en ferdig kjenningsmelodi til podkasten på under ett minutt."),
      ("wave","Bølgeform-editor","Klipp, krysston, fjern stillhet og bounce tidslinjen — ikke bare hele opptak."),
      ("sliders","Mastering &amp; loudness","Innebygd DSP-kjede og LUFS-normalisering klar for strømmetjenestene."),
      ("layers","Ferdig eksport","Bounce til mastret WAV og encode til MP3 med ett klikk, klar for opplasting.")],
    "hl_kicker":"For menigheten","hl_title":"Proff podkast uten lydteknikar.",
    "hl_p":"SundayStudio tar de vanskelige delene av lydproduksjon — nivåer, loudness, støy — og gjør dem automatiske, slik at du kan konsentrere deg om innholdet.",
    "checks":["Forhåndslagde maler for ulike opptaksformat","Prosjektformat som tar vare på alt råmateriale","Billigere og enklere enn proff-verktøyene"],
    "status":"SundayStudio er langt på vei: fundamentet, fleirspors-opptakeren, bølgeform-editoren, DSP- og mastering-kjeden, AI-nivåjusteringen og eksport-løypa er på plass. Det som gjenstår krever ekte maskinvare, ffmpeg og live API-nøkler. Ikke ute for nedlasting ennå.",
    "cta_h":"Vil du høre når Studio er klar?","cta_p":"SundayStudio er under utvikling. Ta kontakt om du vil teste tidlig eller følge med på veien mot lansering."},
  "chips":None},
 "sundaystage":{"accent":"stage","icon":"screen","short":"Stage",
  "en":{"tagline":"Lyrics and media on the big screen.",
    "meta":"SundayStage shows lyrics, Bible verses and media on the big screen behind the altar — a Nordic alternative to ProPresenter, with cue control and safe, isolated output.",
    "lead":"Show lyrics, Bible verses, announcements and media on the screen behind the altar. A modern presentation tool in the ProPresenter class, built for Nordic churches, with cue control, seamless transitions and a live engine with an isolated output process for safe display.",
    "what":"Everything on screen, safely controlled","whatlead":"Made to hold up when it matters — in the middle of the service.",
    "features":[("text","Lyrics &amp; verses","Show text line by line with fast transitions and clean typography on the big screen."),
      ("layers","Cues and order","Build the order for the whole service in advance and run it with a single keypress."),
      ("screen","Media &amp; backgrounds","Images, video and backgrounds with soft transitions between elements."),
      ("shield","Isolated output","The live engine runs in its own output process, so a glitch in the app won't black out the screen."),
      ("bolt","⌘K command palette","Find and show anything in seconds — a dark interface made for the stage."),
      ("search","Full-text search","Search the whole song base with FTS5 and bring up the right song instantly.")],
    "hl_kicker":"Built for live","hl_title":"Confident on the big screen when it counts.",
    "hl_p":"Nothing is worse than a black screen in the middle of worship. SundayStage isolates the display in its own process, so the app can fail without the congregation noticing.",
    "checks":["Isolated output process protects the display","A dark interface made for the stage","TONO ID on songs from day one"],
    "status":"SundayStage is in early development. The data model, the app shell with a ⌘K palette and full-text search are in place; the slide editor and live engine are in progress. Not available for download yet.",
    "cta_h":"Want to follow Stage to launch?","cta_p":"SundayStage is in development. Get in touch if your church wants to be early when the presentation tool is ready."},
  "no":{"tagline":"Sangtekster og media på storskjerm.",
    "meta":"SundayStage viser sangtekster, bibelvers og media på storskjerm bak alteret — et nordisk alternativ til ProPresenter, med køstyring og trygg, isolert visning.",
    "lead":"Vis sangtekster, bibelvers, kunngjøringer og media på skjermen bak alteret. Et moderne presentasjonsverktøy i ProPresenter-klassen, bygd for nordiske menigheter, med køstyring, sømløse overganger og en live-motor med isolert utgangsprosess for trygg visning.",
    "what":"Alt på skjermen, trygt styrt","whatlead":"Laget for å stå imot når det gjelder — midt i gudstjenesten.",
    "features":[("text","Sangtekster &amp; vers","Vis tekst vers for vers med raske overganger og ren typografi på storskjerm."),
      ("layers","Køer og rekkefølge","Bygg rekkefølgen for hele gudstjenesten på forhånd og styr den med ett tastetrykk."),
      ("screen","Media &amp; bakgrunner","Bilder, video og bakgrunner med myke overganger mellom elementene."),
      ("shield","Isolert visning","Live-motoren kjører i en egen utgangsprosess, så en feil i appen ikke svartlegger skjermen."),
      ("bolt","⌘K-kommandopalett","Finn og vis hva som helst på sekunder — et mørkt grensesnitt laget for scenen."),
      ("search","Fulltekstsøk","Søk i hele sangbasen med FTS5 og hent fram riktig sang umiddelbart.")],
    "hl_kicker":"Bygd for live","hl_title":"Trygg på storskjerm når det gjelder.",
    "hl_p":"Ingenting er verre enn en svart skjerm midt i lovsangen. SundayStage isolerer visningen i en egen prosess, slik at appen kan feile uten at menigheten merker det.",
    "checks":["Isolert utgangsprosess beskytter visningen","Mørkt grensesnitt laget for scenen","TONO-ID på sang fra dag én"],
    "status":"SundayStage er i tidlig utvikling. Datamodellen, app-skallet med ⌘K-palett og fulltekstsøk er på plass; slide-editoren og live-motoren er under arbeid. Ikke ute for nedlasting ennå.",
    "cta_h":"Vil du følge Stage mot lansering?","cta_p":"SundayStage er under utvikling. Ta kontakt om menigheten din vil være tidlig ute når presentasjonsverktøyet er klart."},
  "chips":[("Stage","Rec","cue→chapter / cue blir kapittelmerke"),("Stage","Rec","lyrics→SRT / sangtekst blir SRT"),("Plan","Stage","setlist / setliste"),("Stage","Song","logged / loggføres")]},
 "sundayplan":{"accent":"plan","icon":"calendar","short":"Plan",
  "en":{"tagline":"Planning and volunteer rota, done in minutes.",
    "meta":"SundayPlan plans the service and schedules volunteers with a fair auto-fill engine — and keeps track of TONO licence status.",
    "lead":"Plan the service and schedule volunteers without spreadsheets. A deterministic auto-fill engine balances skill, fair rotation, frequency, burnout and fixed pairs — and keeps track of the church's TONO licence status along the way.",
    "what":"No more spreadsheets and phone rounds","whatlead":"From an empty plan to a fully staffed service, fairly distributed.",
    "features":[("calendar","Service plan","Build the service plan with roles, tasks and responsibilities in one place."),
      ("sparkle","Fair auto-rota","A seven-component scoring engine suggests who fits — fairly distributed over time."),
      ("people","People and teams","Keep track of volunteers, skills and who belongs to which team."),
      ("bell","Notifications","Send requests and reminders by SMS and email once the plan is ready."),
      ("star","TONO licence status","Licence status, customer ID and denomination are first-class fields from the start."),
      ("shield","Access control","Row-level security on every table — each church sees only its own data.")],
    "hl_kicker":"End of the puzzle","hl_title":"Fair rotas without playing solitaire.",
    "hl_p":"The auto-fill engine weighs skill, rotation, how often people serve, burnout risk, who works well together and variety — and suggests a plan you can adjust.",
    "checks":["Seven-component scoring: skill, rotation, burnout and more","Norway first: TONO status and denomination built in","Row-level security on all data"],
    "status":"SundayPlan is in early development. The data model with the fair auto-fill engine and row-level security is in place; the admin interface and notifications are in progress. Not available for use yet.",
    "cta_h":"Want to test Plan early?","cta_p":"SundayPlan is in development. Get in touch if your church wants to help shape the planning tool."},
  "no":{"tagline":"Planlegging og frivillig-turnus, ferdig på minutter.",
    "meta":"SundayPlan planlegger gudstjenesten og setter opp de frivillige med en rettferdig auto-fyll-motor — og holder styr på TONO-lisensstatus.",
    "lead":"Planlegg gudstjenesten og sett opp de frivillige uten regneark. En deterministisk auto-fyll-motor balanserer kompetanse, rettferdig rotasjon, frekvens, utbrenthet og faste par — og holder samtidig styr på TONO-lisensstatus for menigheten.",
    "what":"Slutt på regneark og telefonrunder","whatlead":"Fra tom plan til ferdig satt opp gudstjeneste, rettferdig fordelt.",
    "features":[("calendar","Tjenesteplan","Bygg gudstjenesteplanen med roller, oppgaver og ansvar samlet ett sted."),
      ("sparkle","Rettferdig auto-turnus","En scoring-motor med sju komponenter foreslår hvem som passer — rettferdig over tid."),
      ("people","Folk og lag","Hold oversikt over frivillige, kompetanse og hvem som hører til hvilket lag."),
      ("bell","Varsling","Send forespørsler og påminnelser på SMS og e-post når planen er klar."),
      ("star","TONO-lisensstatus","Lisensstatus, kunde-ID og kirkesamfunn er førsteklasses felt fra start."),
      ("shield","Tilgangsstyring","Rad-nivå sikkerhet på hver tabell — hver menighet ser bare sine egne data.")],
    "hl_kicker":"Slutt på kabalen","hl_title":"Rettferdig turnus uten å legge kabal.",
    "hl_p":"Auto-fyll-motoren veier kompetanse, rotasjon, hvor ofte folk tjener, fare for utbrenthet, hvem som jobber godt sammen og variasjon — og foreslår en plan du kan justere.",
    "checks":["Sju-komponents scoring: kompetanse, rotasjon, utbrenthet og mer","Norge først: TONO-status og kirkesamfunn innebygd","Rad-nivå sikkerhet på all data"],
    "status":"SundayPlan er i tidlig utvikling. Datamodellen med den rettferdige auto-fyll-motoren og rad-nivå sikkerhet er på plass; admin-grensesnittet og varsling er under arbeid. Ikke ute for bruk ennå.",
    "cta_h":"Vil du teste Plan tidlig?","cta_p":"SundayPlan er under utvikling. Ta kontakt om menigheten din vil være med å forme planleggingsverktøyet."},
  "chips":[("Plan","Stage","setlist / setliste"),("Rec","Plan","transcript / transkripsjon"),("Plan","Song","licensing / lisens"),("Plan","Paper","program / program")]},
 "sundaysong":{"accent":"song","icon":"note","short":"Song",
  "en":{"tagline":"The song database that reports for you.",
    "meta":"SundaySong is a song database with semantic search, AI recommendations and automatic TONO and CCLI reporting — built for Nordic reality.",
    "lead":"Find the right song with semantic search and AI recommendations across languages — and get the reporting for free. Every use is logged for both CCLI and TONO, with a separate field for whether the song was streamed. No US competitor builds for TONO like this.",
    "what":"Search, suggest, and report automatically","whatlead":"The song catalog and the rights reporting in one and the same service.",
    "features":[("search","Semantic search","Search by feeling and theme, not just title — powered by vector search with pgvector."),
      ("sparkle","AI recommendations","Get suggestions for songs that fit the text, theme and tone of the service."),
      ("star","TONO + CCLI","Every performance becomes a reportable usage log for both rights organizations."),
      ("bolt","Streaming flag","<code>was_streamed</code> separates in-room use from streamed use — a separate royalty pool."),
      ("globe","Multilingual","Canonical songs with variants and translations linked across languages."),
      ("code","Open API","A public SDK lets the other Sunday apps look up and log songs.")],
    "hl_kicker":"The moat","hl_title":"Built for TONO from the first row in the database.",
    "hl_p":"Most song tools are built around American CCLI. SundaySong has <code>tono_work_id</code> on every song and a streaming flag on every use from day one — that's the Nordic moat.",
    "checks":["tono_work_id on every song from day one","was_streamed flag on every use","Norwegian-labelled TONO reports alongside CCLI"],
    "status":"SundaySong is in early development. The data model and API contract with the TONO fields are in place, and the public SDK compiles against the contract; song import, search and AI are in progress. Not available for use yet.",
    "cta_h":"Want in on the TONO moat?","cta_p":"SundaySong is in development. Get in touch if your church or organization wants to follow the song database."},
  "no":{"tagline":"Sangdatabasen som rapporterer for deg.",
    "meta":"SundaySong er en sangdatabase med semantisk søk, AI-anbefalinger og automatisk TONO- og CCLI-rapportering — bygd for norsk virkelighet.",
    "lead":"Finn riktig sang med semantisk søk og AI-anbefalinger på tvers av språk — og få rapporteringen gratis. Hver bruk loggføres for både CCLI og TONO, med eget felt for om sangen ble strømmet. Ingen amerikansk konkurrent bygger for TONO slik.",
    "what":"Søk, foreslå, og rapporter automatisk","whatlead":"Sangkatalogen og rettighetsrapporteringen i én og samme tjeneste.",
    "features":[("search","Semantisk søk","Søk på følelse og tema, ikke bare tittel — drevet av vektorsøk med pgvector."),
      ("sparkle","AI-anbefalinger","Få forslag til sanger som passer tekst, tema og tone i gudstjenesten."),
      ("star","TONO + CCLI","Hver fremføring blir en rapporterbar bruks-logg for begge rettighetsorganisasjonene."),
      ("bolt","Strømme-flagg","<code>was_streamed</code> skiller bruk i rommet fra strømmet bruk — egen royalty-pott."),
      ("globe","Fleirspråk","Kanoniske sanger med varianter og oversettelser koblet på tvers av språk."),
      ("code","Åpent API","Et offentlig SDK lar de andre Sunday-appene slå opp og loggføre sanger.")],
    "hl_kicker":"Moaten","hl_title":"Bygd for TONO fra første rad i databasen.",
    "hl_p":"De fleste sangverktøy er bygd rundt amerikansk CCLI. SundaySong har <code>tono_work_id</code> på hver sang og et strømme-flagg på hver bruk fra dag én — det er den nordiske moaten.",
    "checks":["tono_work_id på hver sang fra dag én","was_streamed-flagg på hver bruk","Norsk-merkede TONO-rapporter ved siden av CCLI"],
    "status":"SundaySong er i tidlig utvikling. Datamodellen og API-kontrakten med TONO-feltene er på plass, og det offentlige SDK-et kompilerer mot kontrakten; sangimport, søk og AI er under arbeid. Ikke ute for bruk ennå.",
    "cta_h":"Vil du være med på TONO-moaten?","cta_p":"SundaySong er under utvikling. Ta kontakt om menigheten eller organisasjonen din vil følge sangdatabasen."},
  "chips":[("Stage","Song","logged / loggføres"),("Plan","Song","licensing / lisens"),("Paper","Song","catalog / katalog"),("Rec","Song","streaming flag / strømme-flagg")]},
 "sundayedit":{"accent":"edit","icon":"caption","short":"Edit",
  "en":{"tagline":"Caption video ten times faster.",
    "meta":"SundayEdit is AI video captioning with confidence highlighting and context priming. Local Whisper — the video is never uploaded. A standalone product.",
    "lead":"Every word gets a confidence score from the recognition model and is colour-coded. The ones the model is sure about you don't touch — you fix only the few per cent that light up amber. Tell the app what the video is about, and Whisper biases toward your names and jargon. Local and private: the video is never uploaded.",
    "what":"Two genuine innovations in captioning","whatlead":"Confidence highlighting and context priming — no one else has both.",
    "features":[("focus","Confidence highlighting","Colour-codes every word by certainty, so you fix only what's actually uncertain."),
      ("sparkle","Context priming","Tell it what the video is about, and the model recognizes names, jargon and foreign words correctly."),
      ("shield","Local Whisper","Speech-to-text runs on your own machine — works offline, nothing is uploaded."),
      ("text","Glossary","A dedicated word list for the church's names and terms, across projects."),
      ("layers","Export to everything","Write SRT, VTT, ASS and TXT — ready for YouTube, Premiere or whatever you use."),
      ("search","Focus mode","Jump straight to the words below the threshold and watch your progress as you fix.")],
    "hl_kicker":"Two genuine innovations","hl_title":"Human review at ten times the speed.",
    "hl_p":"The 92% the model is sure about, you don't touch. You fix only the 8% that light up amber. That turns captioning into something you can actually finish before next Sunday.",
    "checks":["No competitor has confidence highlighting + context priming","Local Whisper — the video never leaves the machine","A standalone product, with an optional link to SundayRec"],
    "status":"SundayEdit is in early development. The confidence editor and the export (SRT/VTT/ASS/TXT) work against sample data; video import, the Whisper engine and burn-in are in progress. A standalone product with its own brand. Not available for use yet.",
    "cta_h":"Want to caption faster?","cta_p":"SundayEdit is in development and will be a standalone product. Get in touch to test the confidence captioning early."},
  "no":{"tagline":"Tekst video ti ganger raskere.",
    "meta":"SundayEdit er AI-teksting av video med konfidens-fremheving og kontekst-priming. Lokal Whisper — videoen lastes aldri opp. Frittstående produkt.",
    "lead":"Hvert ord får en konfidens-score fra gjenkjenningsmodellen og fargemarkeres. Det modellen er sikker på rører du ikke — du retter bare de få prosentene som lyser gult. Fortell appen hva videoen handler om, så biaser Whisper mot dine navn og fagord. Lokalt og privat: videoen lastes aldri opp.",
    "what":"To ekte nyvinninger i teksting","whatlead":"Konfidens-fremheving og kontekst-priming — ingen andre har begge.",
    "features":[("focus","Konfidens-fremheving","Fargekoder hvert ord etter sikkerhet, så du retter bare det som faktisk er usikkert."),
      ("sparkle","Kontekst-priming","Fortell hva videoen handler om, så gjenkjenner modellen navn, fagord og fremmedord riktig."),
      ("shield","Lokal Whisper","Tale-til-tekst kjører på din egen maskin — fungerer offline, ingenting lastes opp."),
      ("text","Glossar","Egen ordliste for menighetens navn og uttrykk, på tvers av prosjekter."),
      ("layers","Eksport til alt","Skriv ut SRT, VTT, ASS og TXT — klar for YouTube, Premiere eller hva du bruker."),
      ("search","Fokusmodus","Hopp rett til ordene under terskelen og se fremgangen din mens du retter.")],
    "hl_kicker":"To ekte nyvinninger","hl_title":"Menneskelig gjennomgang i ti ganger farten.",
    "hl_p":"De 92 prosentene modellen er sikker på rører du ikke. Du retter bare de 8 som lyser gult. Det gjør teksting til noe du faktisk rekker før neste søndag.",
    "checks":["Ingen konkurrent har konfidens-fremheving + kontekst-priming","Lokal Whisper — videoen forlater aldri maskinen","Frittstående produkt, valgfri kobling til SundayRec"],
    "status":"SundayEdit er i tidlig utvikling. Konfidens-editoren og eksporten (SRT/VTT/ASS/TXT) virker mot testdata; video-import, Whisper-motoren og innbrenning er under arbeid. Et frittstående produkt med egen merkevare. Ikke ute for bruk ennå.",
    "cta_h":"Vil du tekste raskere?","cta_p":"SundayEdit er under utvikling og blir et frittstående produkt. Ta kontakt om du vil teste konfidens-tekstingen tidlig."},
  "chips":[("Rec","Edit","sermon + transcript / preken + transkripsjon")]},
 "sundaypaper":{"accent":"paper-c","icon":"doc","short":"Paper",
  "en":{"tagline":"The AI document tool for the church.",
    "meta":"SundayPaper splits songbooks, lays out service programs, parish magazines, large-print editions and forms with professional Typst layout and OCR.",
    "lead":"Split scanned songbooks into single songs, lay out service programs, make parish magazines, large-print editions and forms — all with professional Typst layout, a PDF engine and OCR under the hood. The print the church makes every week, without fighting Word.",
    "what":"Print without typesetting expertise","whatlead":"From a scanned songbook to a finished program — with book quality, automatically.",
    "features":[("split","Songbook split","Split a scanned songbook into single songs with OCR — ready for the catalog in SundaySong."),
      ("doc","Service programs","Make beautiful programs with professional Typst typography, not clumsy Word templates."),
      ("layers","Parish magazine","Lay out the magazine with columns, images and clean layout — ready for print or PDF."),
      ("text","Large print","Generate large-print editions automatically for those who need bigger text."),
      ("stack","Forms","Make sign-up and collection forms that look like the church, not a spreadsheet."),
      ("search","OCR &amp; PDF","pdfium, lopdf and Tesseract turn PDFs into editable, searchable content.")],
    "hl_kicker":"Print, made simple","hl_title":"Professional layout without being a typesetter.",
    "hl_p":"SundayPaper uses Typst — the same class as professional book production — but hides the complexity behind ready-made templates, so a volunteer can make print that looks professional.",
    "checks":["The Typst engine gives book quality automatically","OCR turns scanned pages into editable text","From setlist to finished program in one click"],
    "status":"SundayPaper is at the planning stage. The build plan is written and the architecture chosen (Typst, pdfium, Tesseract OCR), but the app itself hasn't been started yet.",
    "cta_h":"Want to shape Paper?","cta_p":"SundayPaper is at the planning stage. Get in touch if your church has print needs we should know about."},
  "no":{"tagline":"AI-dokumentverktøyet for menigheten.",
    "meta":"SundayPaper splitter sangbøker, lager gudstjenesteprogrammer, menighetsblad, storskrift og skjemaer med profesjonell Typst-layout og OCR.",
    "lead":"Splitt skannede sangbøker til enkeltsanger, sett opp gudstjenesteprogrammer, lag menighetsblad, storskrift-utgaver og skjemaer — alt med profesjonell Typst-layout, PDF-motor og OCR under panseret. Trykksakene menigheten lager hver uke, uten å kjempe med Word.",
    "what":"Trykksaker uten typograf-kunnskap","whatlead":"Fra skannet sangbok til ferdig program — med bok-kvalitet automatisk.",
    "features":[("split","Sangbok-splitt","Del en skannet sangbok i enkeltsanger med OCR — klar for katalogen i SundaySong."),
      ("doc","Gudstjenesteprogram","Lag pene programmer med profesjonell Typst-typografi, ikke klønete Word-maler."),
      ("layers","Menighetsblad","Sett opp bladet med spalter, bilder og ren layout — klart for trykk eller PDF."),
      ("text","Storskrift","Generer storskrift-utgaver automatisk for dem som trenger større tekst."),
      ("stack","Skjemaer","Lag påmeldings- og innsamlingsskjemaer som ser ut som menigheten, ikke et regneark."),
      ("search","OCR &amp; PDF","pdfium, lopdf og Tesseract gjør PDF-er om til redigerbart, søkbart innhold.")],
    "hl_kicker":"Trykksaker, gjort enkelt","hl_title":"Profesjonell layout uten å være typograf.",
    "hl_p":"SundayPaper bruker Typst — samme klasse som proff bokproduksjon — men gjemmer kompleksiteten bak ferdige maler, slik at en frivillig kan lage trykksaker som ser profesjonelle ut.",
    "checks":["Typst-motor gir bok-kvalitet automatisk","OCR gjør skannede sider om til redigerbar tekst","Fra setliste til ferdig program med ett klikk"],
    "status":"SundayPaper er på planleggingsstadiet. Byggeplanen er skrevet og arkitekturen valgt (Typst, pdfium, Tesseract OCR), men selve appen er ikke startet ennå.",
    "cta_h":"Vil du forme Paper?","cta_p":"SundayPaper er på planleggingsstadiet. Ta kontakt om menigheten din har trykksak-behov vi bør kjenne til."},
  "chips":[("Plan","Paper","program / program"),("Paper","Song","catalog / katalog"),("Rec","Paper","magazine / blad")]},
}

CHECKSVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>'

def chip_html(a,b,t): return f'<div class="chip"><span class="from">{a}</span><span class="arrow">&rarr;</span><span class="to">{b}</span>&nbsp;{t}</div>'

def app_body(c, L, slug, accent, icon, short, d, chips, status_head=None, hero_actions=None):
    feats=""
    for i,(ik,t,desc) in enumerate(d["features"]):
        dd=f' data-d="{i%3}"' if i%3 else ""
        feats+=f'        <div class="feat reveal"{dd}><div class="fi">{sv(ik)}</div><h3>{t}</h3><p>{desc}</p></div>\n'
    checks="".join(f'          <li>{CHECKSVG}{x}</li>\n' for x in d["checks"])
    if chips:
        ch="".join("        "+chip_html(*x)+"\n" for x in chips)
        intgr=(f'      <div class="section-head"><div class="section-kicker kicker-c">{c["family_kicker"]}</div><h2 class="section-title">{c["family_title"]}</h2></div>\n'
               f'      <div class="intgr" style="justify-content:center; max-width:920px; margin:0 auto">\n{ch}      </div>')
    else:
        intgr=(f'      <div class="section-head"><div class="section-kicker kicker-c">{c["family_kicker"]}</div><h2 class="section-title">{c["standalone_title"]}</h2>'
               f'<p class="section-lead">{c["standalone_lead"]}</p></div>')
    sh = status_head or c["status_head"]
    if hero_actions is None:
        hero_actions=f'<a href="mailto:dev@sundaysuite.app" class="btn btn-accent">{c["keep_posted"]}</a><a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a>'
        badge=f'<span class="status on-ink build">{c["status_build"]}</span>'
    else:
        badge=f'<span class="status on-ink beta">{("Beta · free" if c["lang"]=="en" else "Beta · gratis")}</span>'
    return (f'''<main>
<section class="app-hero"><div class="grain"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><span>{PNAME[slug]}</span></div>
  <div class="app-hero-inner">
    <div class="app-badges"><img class="logo-hero" src="{L["assets"]}logos/{slug}.svg" alt="{PNAME[slug]} logo" width="64" height="64" />{badge}</div>
    <h1 class="app-title"><span class="sunday">Sunday</span>{short}</h1>
    <div class="app-tagline">{d["tagline"]}</div>
    <p class="app-lead">{d["lead"]}</p>
    <div class="app-hero-actions">{hero_actions}</div>
  </div>
</div></section>

<div class="app-body">
  <section class="app-section"><div class="wrap">
    <div class="section-head"><div class="section-kicker kicker-c">{c["what_kicker"]}</div><h2 class="section-title">{d["what"]}</h2><p class="section-lead">{d["whatlead"]}</p></div>
    <div class="feat-grid">
{feats}    </div>
  </div></section>

  <section class="app-section alt"><div class="wrap split">
    <div class="reveal"><div class="section-kicker kicker-c">{d["hl_kicker"]}</div><h2>{d["hl_title"]}</h2><p>{d["hl_p"]}</p>
      <ul class="checks">
{checks}      </ul>
    </div>
    <div class="visual reveal" data-d="1"><img class="logo-big" src="{L["assets"]}logos/{slug}.svg" alt="{PNAME[slug]} logo" width="150" height="150" /><div class="ph">{short}</div></div>
  </div></section>

  <section class="app-section"><div class="wrap">
{intgr}
    <div class="callout reveal" style="margin:48px auto 0">
      <h4><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--c)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v5M12 16h.01"/></svg>{sh}</h4>
      <p>{d["status"]}</p>
    </div>
  </div></section>
</div>

<section class="app-cta"><div class="wrap">
  <h2>{d["cta_h"]}</h2><p>{d["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="mailto:dev@sundaysuite.app" class="btn btn-primary">dev@sundaysuite.app</a><a href="{L["home"]}#products" class="btn btn-ghost">{c["cta_back"] if "cta_back" in c else c["all_products"]}</a></div>
</div></section>
</main>''')

def render_app(lang, slug):
    c=CH[lang]; root="../" if lang=="en" else "../../"; L=links(lang,root)
    other = (f'../no/apps/{slug}.html' if lang=="en" else f'../../apps/{slug}.html')
    if slug=="sundayrec":
        a=APP["sundayrec"]; d=a[lang]
        ha=(f'<a href="https://github.com/richardfossland/sundayrec/releases" target="_blank" rel="noopener" class="btn btn-accent">'
            f'{"Download the beta (Mac &amp; Windows)" if lang=="en" else "Last ned betaen (Mac &amp; Windows)"}</a>'
            f'<a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a>')
        chips=[(x[0],x[1], x[2].split(" / ")[0] if lang=="en" else x[2].split(" / ")[1]) for x in a["chips"]]
        body=app_body(c,L,slug,a["accent"],a["icon"],"Rec",d,chips,status_head=d["status_head"],hero_actions=ha)
        # rec CTA: clean full-block replace (download primary + email + all products)
        dl = "Download the beta" if lang=="en" else "Last ned betaen"
        old_cta=(f'<div class="hero-actions" style="justify-content:center"><a href="mailto:dev@sundaysuite.app" class="btn btn-primary">dev@sundaysuite.app</a>'
                 f'<a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a></div>')
        new_cta=(f'<div class="hero-actions" style="justify-content:center">'
                 f'<a href="https://github.com/richardfossland/sundayrec/releases" target="_blank" rel="noopener" class="btn btn-primary">{dl}</a>'
                 f'<a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">dev@sundaysuite.app</a></div>')
        body=body.replace(old_cta,new_cta,1)
        title=f'{PNAME[slug]} — {d["tagline"]} | Sunday Suite'
    else:
        ad=APPDATA[slug]; d=ad[lang]
        chips=None
        if ad["chips"]:
            chips=[(x[0],x[1], x[2].split(" / ")[0] if lang=="en" else x[2].split(" / ")[1]) for x in ad["chips"]]
        body=app_body(c,L,slug,ad["accent"],ad["icon"],ad["short"],d,chips)
        title=f'{PNAME[slug]} — {d["tagline"]} | Sunday Suite'
    return shell(c,L,other,title,d["meta"],f' style="--c:var(--{(APP["sundayrec"]["accent"] if slug=="sundayrec" else APPDATA[slug]["accent"])})"',body)

# ===================================================================== LEGAL
def legal_shell(lang, name, h1, updated, note, toc, prose):
    c=CH[lang]; root="../" if lang=="en" else "../../"; L=links(lang,root)
    other=(f'../no/legal/{name}.html' if lang=="en" else f'../../legal/{name}.html')
    crumb_label = h1
    content=(f'''<main>
<section class="legal-hero"><div class="glow"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><span>{crumb_label}</span></div>
  <h1>{h1}</h1><div class="updated">{updated}</div>
</div></section>
<section class="legal-body"><div class="wrap">
  <div class="note"><p>{note}</p></div>
  <div class="toc"><h4>{"Contents" if lang=="en" else "Innhold"}</h4><ol>{toc}</ol></div>
  <div class="prose">
{prose}
    <p style="margin-top:40px"><a href="{L["home"]}">{c["back_home"]}</a> &middot; <a href="{L["legal"]("privacy" if name=="terms" else "terms")}">{c["foot_privacy"] if name=="terms" else c["foot_terms"]}</a></p>
  </div>
</div></section>
</main>''')
    title=("Terms of Use" if name=="terms" else "Privacy Policy") if lang=="en" else ("Vilkår for bruk" if name=="terms" else "Personvernerklæring")
    if name=="terms":
        desc=("Terms of Use for Sunday Suite and sundaysuite.app." if lang=="en" else "Vilkår for bruk av Sunday Suite og sundaysuite.app.")
    else:
        desc=("Privacy Policy for Sunday Suite — local-first, your content stays with you." if lang=="en" else "Personvernerklæring for Sunday Suite — lokalt først, innholdet ditt blir hos deg.")
    return shell(c,L,other,f'{title} — Sunday Suite',desc,'',content,navscrolled=True)

def toc(items): return "".join(f'<li><a href="#{i}">{t}</a></li>' for i,t in items)
def h2(n,i,t): return f'<h2 id="{i}"><span class="num">{n}.</span>{t}</h2>'

# ---- Terms EN
def terms_en():
    note='<strong>Note:</strong> This document is a good-faith template and is not legal advice. Have it reviewed by a lawyer before relying on it commercially — especially the sections on intellectual property, liability and consumer protection.'
    items=[("s1","About these Terms"),("s2","The Service"),("s3","Price, beta and availability"),("s4","Licence"),("s5","Intellectual property and trademarks"),("s6","Your content"),("s7","Third-party services"),("s8","Acceptable use"),("s9","Disclaimer of warranties"),("s10","Limitation of liability"),("s11","Changes to these Terms"),("s12","Governing law and venue"),("s13","Contact")]
    rows="".join(f"<tr><td>{p}</td><td>{w}</td><td>{s}</td></tr>" for p,w,s in [
      ("SundayRec","Recording, streaming, transcription and podcast publishing for the church service","Beta"),
      ("SundayStudio","Podcast and jingle production for churches","In development"),
      ("SundayStage","Presentation of lyrics and media on the big screen","In development"),
      ("SundayPlan","Service planning and volunteer rota","In development"),
      ("SundaySong","Song database with AI and TONO/CCLI reporting","In development"),
      ("SundayEdit","AI video captioning (standalone product)","In development"),
      ("SundayPaper","AI document and PDF tool for print","Planning")])
    prose=f'''    <p class="lead">Please read these Terms of Use ("Terms") before using the software in Sunday Suite or the website sundaysuite.app (together the "Service"), operated by Richard Fossland ("we", "us" or "our"). By downloading, installing or using a Sunday program you agree to be bound by these Terms. If you do not agree, do not use the Service.</p>
    {h2(1,"s1","About these Terms")}
    <p>Sunday Suite is a family of standalone programs for churches and organizations. These Terms apply to all programs in the suite, both those out in beta and those still in development, and to the website. Individual programs may have their own supplementary terms; in case of conflict, the supplementary terms for the program in question prevail over these general Terms.</p>
    {h2(2,"s2","The Service")}
    <p>Sunday Suite currently consists of the following programs. The status indicates maturity and may change without notice:</p>
    <table class="app-legal-table"><thead><tr><th>Program</th><th>What it is</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
    <p>The programs are delivered mainly as desktop applications for macOS and Windows and/or as web-based services. Not all programs are available for download yet.</p>
    {h2(3,"s3","Price, beta and availability")}
    <p>The programs available today are provided free of charge. There is no purchase, subscription or licence fee. We reserve the right to introduce paid features or plans in the future, but any change will be communicated clearly.</p>
    <p>Software marked "beta" or "in development" is offered at an early stage. It may contain bugs, change materially or be withdrawn without notice, and you should verify the first results before using it for anything critical. We give no guarantee that the Service will be available, uninterrupted or preserved over time.</p>
    {h2(4,"s4","Licence")}
    <p>Subject to your compliance with these Terms, we grant you a non-exclusive, non-transferable and revocable licence to download and use the Sunday programs for your organization's own purposes.</p>
    <p>You may not:</p>
    <ul><li>redistribute, sell, rent or sublicense the software;</li><li>decompile, reverse-engineer or attempt to derive the source code, except to the extent mandatory law permits;</li><li>remove or alter any copyright notices, trademarks or other proprietary markings;</li><li>use the software, name or design to create, market or operate a competing or confusingly similar product; or</li><li>use the Service for any unlawful purpose.</li></ul>
    {h2(5,"s5","Intellectual property and trademarks")}
    <p>Sunday Suite and all programs in the suite — <strong>SundayRec, SundayStudio, SundayStage, SundayPlan, SundaySong, SundayEdit and SundayPaper</strong> — together with source code, design, graphics, the golden cross, logos, names, text and all other content, are owned by Richard Fossland and protected by applicable law on copyright, trademarks and other intellectual property rights.</p>
    <h3>Trademarks</h3>
    <p>The names "Sunday Suite", the "Sunday" family of product names listed above, and the associated cross and gold symbol, are our trademarks (registered or being established). You are granted no right to use these trademarks, and you must not use them — or names, logos or designs likely to be confused with them — without prior written consent. This also applies to product, domain, app-store and company names.</p>
    <h3>No transfer of rights</h3>
    <p>Nothing in these Terms transfers any intellectual property rights to you. All use not expressly permitted is reserved to the rights holder. We reserve all rights not expressly granted here.</p>
    {h2(6,"s6","Your content")}
    <p>You retain full ownership of all content you create with the Sunday programs — recordings, video, text, transcripts, plans, songs and documents. We do not access, store or process your content on our servers. The programs run locally on your machine unless otherwise expressly stated. See the <a href="privacy.html">Privacy Policy</a> for how data is handled.</p>
    {h2(7,"s7","Third-party services")}
    <p>If you enable cloud backup (for example Google Drive), publishing (for example YouTube or a podcast host), speech-to-text models, email alerts or other integrations, your use is governed by the respective third parties' own terms. The Sunday program is the tool that acts on your behalf; the relationship with the third party is yours.</p>
    {h2(8,"s8","Acceptable use")}
    <p>You are responsible for ensuring your use of the Service is lawful — including that you have the necessary rights and consents to record, stream, display and publish content, and that you comply with applicable rules on copyright, privacy and rights reporting (for example TONO and CCLI). Tools in the suite that help with such reporting do not relieve you of responsibility for the reporting being correct.</p>
    {h2(9,"s9","Disclaimer of warranties")}
    <p>The Service is provided "as is" and "as available", without warranties of any kind, whether express or implied, including warranties of merchantability, fitness for a particular purpose or non-infringement. We do not warrant that the Service will be uninterrupted, error-free or free of viruses. While we test extensively, software is software — verify the first results before basing an important service on the Service.</p>
    {h2(10,"s10","Limitation of liability")}
    <p>To the maximum extent permitted by applicable law, we are not liable for indirect, incidental or consequential damages, or special or punitive damages, including loss of data or recordings, arising from your use of or inability to use the Service. Nothing in these Terms limits liability that cannot be excluded under mandatory law, including towards consumers.</p>
    {h2(11,"s11","Changes to these Terms")}
    <p>We may update these Terms at any time. Material changes are notified by updating the date at the top of this page. Continued use of the Service after a change means you accept the new Terms.</p>
    {h2(12,"s12","Governing law and venue")}
    <p>These Terms are governed by Norwegian law. Any disputes shall be subject to the exclusive jurisdiction of the Norwegian courts, unless mandatory consumer-protection rules provide otherwise.</p>
    {h2(13,"s13","Contact")}
    <p>Questions about these Terms? Contact us at <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("en","terms","Terms of Use","Last updated: 8 June 2026",note,toc(items),prose)

# ---- Privacy EN
def privacy_en():
    note='<strong>Note:</strong> This document is a good-faith template and is not legal advice. Have it reviewed by a privacy professional before relying on it — especially regarding GDPR and the processing of personal data in recordings.'
    items=[("p1","In short"),("p2","Data on your machine"),("p3","OAuth tokens"),("p4","Cloud uploads"),("p5","Publishing"),("p6","Email alerts"),("p7","No analytics or telemetry"),("p8","Content stays on the machine"),("p9","The website sundaysuite.app"),("p10","Third-party services"),("p11","Your rights"),("p12","Changes"),("p13","Contact")]
    prose=f'''    <p class="lead">Sunday Suite is built "local-first". The programs run on your own machine, and your content stays with you unless you choose to upload or publish it. This policy explains what is processed, where, and by whom.</p>
    {h2(1,"p1","In short")}
    <ul><li>The programs are desktop apps that store data locally on your machine.</li><li>We run no central server that receives your recordings, videos or documents.</li><li>Data leaves the machine only when you actively enable a cloud, publishing or alert feature.</li><li>We collect no analytics or telemetry from the programs.</li></ul>
    {h2(2,"p2","Data on your machine")}
    <p>Settings, projects, recordings, video, transcripts, plans, songs and documents are stored locally in the program's data folder on your machine. You control these files and can delete them at any time.</p>
    {h2(3,"p3","OAuth tokens")}
    <p>If you connect a third-party account (for example Google), the access and refresh tokens are stored securely in your operating system's keychain on your machine — not with us. You can disconnect at any time, which removes the stored tokens.</p>
    {h2(4,"p4","Cloud uploads")}
    <p>If you enable cloud backup, the selected files are uploaded directly from your machine to your own cloud account (for example Google Drive). The files do not pass through us. Storage is governed by your agreement with the cloud provider.</p>
    {h2(5,"p5","Publishing")}
    <p>If you choose to publish — for example upload to YouTube or send to a podcast host via RSS — the content and necessary metadata are sent directly from your machine to the service you have chosen, on your behalf.</p>
    {h2(6,"p6","Email alerts")}
    <p>If a program can send you alerts (for example via your own SMTP server or a notification service), they are sent with the configuration you provide. We do not receive a copy of these alerts.</p>
    {h2(7,"p7","No analytics or telemetry")}
    <p>The programs contain no analytics, tracking or telemetry. We do not know what you record, show, plan or publish. The programs may contact an update service to check whether a newer version exists; such a request does not contain your content.</p>
    {h2(8,"p8","Content stays on the machine")}
    <p>Recording, video and transcription are processed locally. Speech-to-text (Whisper) runs on your own machine. Your content leaves the machine only when you enable a cloud, publishing or sharing feature, as described above.</p>
    {h2(9,"p9","The website sundaysuite.app")}
    <p>The website is an information site. If you get in touch via the email links, we process your email address and the content of your message to reply to you. If the website later offers forms or a newsletter, their use will be described here, and you will be able to unsubscribe at any time.</p>
    {h2(10,"p10","Third-party services")}
    <p>When you enable an integration, the relevant third party's privacy rules apply to that part of the processing. Examples may be Google (Drive/YouTube), a podcast host or an email provider. You choose whether and when these are used.</p>
    {h2(11,"p11","Your rights")}
    <p>Since most data lives locally on your machine, you have direct control and can view, change, export and delete it yourself. For personal data we may process (for example an email enquiry), you have the right under the privacy regulation (GDPR) to access, rectification, erasure and restriction. Contact us to exercise these rights.</p>
    {h2(12,"p12","Changes")}
    <p>We may update this policy. Material changes are notified by updating the date at the top of the page.</p>
    {h2(13,"p13","Contact")}
    <p>Questions about privacy? Contact the data controller Richard Fossland at <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("en","privacy","Privacy Policy","Last updated: 8 June 2026",note,toc(items),prose)

# ---- Terms NO
def terms_no():
    note='<strong>Merk:</strong> Dette dokumentet er en mal levert i god tro og er ikke juridisk rådgivning. Få det gjennomgått av en advokat før du stoler på det kommersielt — særlig avsnittene om immaterielle rettigheter, ansvar og forbrukervern.'
    items=[("s1","Om vilkårene"),("s2","Tjenesten"),("s3","Pris, beta og tilgjengelighet"),("s4","Lisens"),("s5","Immaterielle rettigheter og varemerker"),("s6","Ditt innhold"),("s7","Tredjepartstjenester"),("s8","Akseptabel bruk"),("s9","Fraskrivelse av garantier"),("s10","Ansvarsbegrensning"),("s11","Endringer i vilkårene"),("s12","Lovvalg og verneting"),("s13","Kontakt")]
    rows="".join(f"<tr><td>{p}</td><td>{w}</td><td>{s}</td></tr>" for p,w,s in [
      ("SundayRec","Opptak, strømming, transkripsjon og podkast-publisering for gudstjenesten","Beta"),
      ("SundayStudio","Podkast- og jingleproduksjon for menigheter","Under utvikling"),
      ("SundayStage","Presentasjon av sangtekster og media på storskjerm","Under utvikling"),
      ("SundayPlan","Gudstjenesteplanlegging og frivillig-turnus","Under utvikling"),
      ("SundaySong","Sangdatabase med AI og TONO/CCLI-rapportering","Under utvikling"),
      ("SundayEdit","AI-teksting av video (frittstående produkt)","Under utvikling"),
      ("SundayPaper","AI-dokument- og PDF-verktøy for trykksaker","Planlegging")])
    prose=f'''    <p class="lead">Les disse vilkårene for bruk («Vilkårene») før du bruker programvaren i Sunday Suite eller nettstedet sundaysuite.app (samlet «Tjenesten»), drevet av Richard Fossland («vi», «oss» eller «vår»). Ved å laste ned, installere eller bruke et Sunday-program godtar du å være bundet av disse Vilkårene. Godtar du dem ikke, skal du ikke bruke Tjenesten.</p>
    {h2(1,"s1","Om vilkårene")}
    <p>Sunday Suite er en familie av selvstendige programmer for menigheter og organisasjoner. Vilkårene gjelder for alle programmene i suiten, både de som er ute i beta og de som fortsatt er under utvikling, samt for nettstedet. Enkelte programmer kan ha egne tilleggsvilkår; ved motstrid gjelder tilleggsvilkårene for det aktuelle programmet foran disse generelle Vilkårene.</p>
    {h2(2,"s2","Tjenesten")}
    <p>Sunday Suite består i dag av følgende programmer. Statusen angir modenhet og kan endres uten varsel:</p>
    <table class="app-legal-table"><thead><tr><th>Program</th><th>Hva det er</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
    <p>Programmene leveres i hovedsak som skrivebordsapplikasjoner for macOS og Windows og/eller som nettbaserte tjenester. Ikke alle programmer er tilgjengelige for nedlasting ennå.</p>
    {h2(3,"s3","Pris, beta og tilgjengelighet")}
    <p>Programmene som er tilgjengelige i dag, leveres uten kostnad. Det er ingen kjøps-, abonnements- eller lisensavgift. Vi forbeholder oss retten til å innføre betalte funksjoner eller planer i fremtiden, men eventuelle endringer vil bli kommunisert tydelig.</p>
    <p>Programvare merket «beta» eller «under utvikling» tilbys i en tidlig fase. Den kan inneholde feil, endres vesentlig eller bli trukket tilbake uten varsel, og du bør verifisere de første resultatene før du bruker den til noe kritisk. Vi gir ingen garanti for at Tjenesten vil være tilgjengelig, uavbrutt eller bevart over tid.</p>
    {h2(4,"s4","Lisens")}
    <p>Under forutsetning av at du følger disse Vilkårene, gir vi deg en ikke-eksklusiv, ikke-overførbar og gjenkallelig lisens til å laste ned og bruke Sunday-programmene for din organisasjons egne formål.</p>
    <p>Du har ikke lov til å:</p>
    <ul><li>videredistribuere, selge, leie ut eller viderelisensiere programvaren;</li><li>dekompilere, reversutvikle eller forsøke å utlede kildekoden, unntatt i den grad ufravikelig lov tillater det;</li><li>fjerne eller endre opphavsrettsmerker, varemerker eller andre rettighetsmerker;</li><li>bruke programvaren, navnet eller utformingen til å lage, markedsføre eller drive et konkurrerende eller forvekselbart produkt; eller</li><li>bruke Tjenesten til ulovlige formål.</li></ul>
    {h2(5,"s5","Immaterielle rettigheter og varemerker")}
    <p>Sunday Suite og alle programmene i suiten — <strong>SundayRec, SundayStudio, SundayStage, SundayPlan, SundaySong, SundayEdit og SundayPaper</strong> — sammen med kildekode, design, grafikk, det gylne korset, logoer, navn, tekst og alt øvrig innhold, eies av Richard Fossland og er beskyttet av gjeldende lovgivning om opphavsrett, varemerker og andre immaterielle rettigheter.</p>
    <h3>Varemerker</h3>
    <p>Navnene «Sunday Suite», «Sunday»-familien av produktnavn nevnt over, samt det tilhørende kors- og gull-symbolet, er våre varemerker (registrerte eller under etablering). Du får ingen rett til å bruke disse varemerkene, og du må ikke bruke dem — eller navn, logoer eller utforming som er egnet til å forveksles med dem — uten skriftlig forhåndssamtykke. Dette gjelder også produkt-, domene-, app-butikk- og selskapsnavn.</p>
    <h3>Ingen rettighetsoverføring</h3>
    <p>Ingenting i disse Vilkårene overfører immaterielle rettigheter til deg. All bruk som ikke uttrykkelig er tillatt, er forbeholdt rettighetshaver. Vi forbeholder oss alle rettigheter som ikke uttrykkelig er gitt her.</p>
    {h2(6,"s6","Ditt innhold")}
    <p>Du beholder full eiendomsrett til alt innhold du lager med Sunday-programmene — opptak, video, tekst, transkripsjoner, planer, sanger og dokumenter. Vi får ikke tilgang til, lagrer ikke og behandler ikke innholdet ditt på våre servere. Programmene kjører lokalt på din maskin med mindre annet er uttrykkelig angitt. Se <a href="privacy.html">Personvernerklæringen</a> for hvordan data håndteres.</p>
    {h2(7,"s7","Tredjepartstjenester")}
    <p>Hvis du aktiverer sky-backup (for eksempel Google Drive), publisering (for eksempel YouTube eller en podkast-host), tale-til-tekst-modeller, e-postvarsler eller andre integrasjoner, reguleres din bruk av de respektive tredjepartenes egne vilkår. Sunday-programmet er verktøyet som handler på dine vegne; forholdet til tredjeparten er ditt.</p>
    {h2(8,"s8","Akseptabel bruk")}
    <p>Du er ansvarlig for at din bruk av Tjenesten er lovlig — herunder at du har nødvendige rettigheter og samtykker til å ta opp, strømme, vise og publisere innhold, og at du følger gjeldende regler om opphavsrett, personvern og rettighetsrapportering (for eksempel TONO og CCLI). Verktøy i suiten som hjelper med slik rapportering, fritar deg ikke fra ansvaret for at rapporteringen er riktig.</p>
    {h2(9,"s9","Fraskrivelse av garantier")}
    <p>Tjenesten leveres «som den er» og «som tilgjengelig», uten garantier av noe slag, verken uttrykkelige eller underforståtte, herunder garantier om salgbarhet, egnethet for et bestemt formål eller at den ikke krenker tredjeparts rettigheter. Vi garanterer ikke at Tjenesten er uavbrutt, feilfri eller fri for virus. Selv om vi tester grundig, er programvare programvare — verifiser de første resultatene før du baserer en viktig gudstjeneste på Tjenesten.</p>
    {h2(10,"s10","Ansvarsbegrensning")}
    <p>I den grad gjeldende lov tillater det, er vi ikke ansvarlige for indirekte tap, tilfeldige eller følgeskader, eller spesielle skader eller straffeerstatning, herunder tap av data eller opptak, som følge av din bruk av eller manglende evne til å bruke Tjenesten. Ingenting i disse Vilkårene begrenser ansvar som ikke kan fraskrives etter ufravikelig lov, herunder overfor forbrukere.</p>
    {h2(11,"s11","Endringer i vilkårene")}
    <p>Vi kan oppdatere disse Vilkårene når som helst. Vesentlige endringer varsles ved å oppdatere datoen øverst på denne siden. Fortsatt bruk av Tjenesten etter en endring innebærer at du godtar de nye Vilkårene.</p>
    {h2(12,"s12","Lovvalg og verneting")}
    <p>Disse Vilkårene reguleres av norsk rett. Eventuelle tvister skal være underlagt de norske domstolenes eksklusive jurisdiksjon, med mindre ufravikelige forbrukervernregler bestemmer noe annet.</p>
    {h2(13,"s13","Kontakt")}
    <p>Spørsmål om disse Vilkårene? Kontakt oss på <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("no","terms","Vilkår for bruk","Sist oppdatert: 8. juni 2026",note,toc(items),prose)

# ---- Privacy NO
def privacy_no():
    note='<strong>Merk:</strong> Dette dokumentet er en mal levert i god tro og er ikke juridisk rådgivning. Få det gjennomgått av en personvernkyndig før du baserer deg på det — særlig med tanke på GDPR og behandling av personopplysninger i opptak.'
    items=[("p1","Kort fortalt"),("p2","Data på din maskin"),("p3","OAuth-tokens"),("p4","Sky-opplastinger"),("p5","Publisering"),("p6","E-postvarsler"),("p7","Ingen analyse eller telemetri"),("p8","Innhold forlater ikke maskinen"),("p9","Nettstedet sundaysuite.app"),("p10","Tredjepartstjenester"),("p11","Dine rettigheter"),("p12","Endringer"),("p13","Kontakt")]
    prose=f'''    <p class="lead">Sunday Suite er bygd «lokalt først». Programmene kjører på din egen maskin, og innholdet ditt blir hos deg med mindre du selv velger å laste det opp eller publisere det. Denne erklæringen forklarer hva som behandles, hvor, og av hvem.</p>
    {h2(1,"p1","Kort fortalt")}
    <ul><li>Programmene er skrivebordsapper som lagrer data lokalt på din maskin.</li><li>Vi driver ingen sentral server som mottar opptakene, videoene eller dokumentene dine.</li><li>Data forlater maskinen bare når du aktivt aktiverer en sky-, publiserings- eller varselfunksjon.</li><li>Vi samler ikke inn analyse eller telemetri fra programmene.</li></ul>
    {h2(2,"p2","Data på din maskin")}
    <p>Innstillinger, prosjekter, opptak, video, transkripsjoner, planer, sanger og dokumenter lagres lokalt i programmets datamappe på din maskin. Du kontrollerer disse filene og kan slette dem når som helst.</p>
    {h2(3,"p3","OAuth-tokens")}
    <p>Hvis du kobler til en tredjepartskonto (for eksempel Google), lagres tilgangs- og oppdateringstokenene trygt i operativsystemets nøkkelring/keychain på din maskin — ikke hos oss. Du kan koble fra når som helst, noe som fjerner de lagrede tokenene.</p>
    {h2(4,"p4","Sky-opplastinger")}
    <p>Aktiverer du sky-backup, lastes de valgte filene opp direkte fra din maskin til din egen skykonto (for eksempel Google Drive). Filene går ikke via oss. Lagringen styres av din avtale med skyleverandøren.</p>
    {h2(5,"p5","Publisering")}
    <p>Velger du å publisere — for eksempel laste opp til YouTube eller sende til en podkast-host via RSS — sendes innholdet og nødvendige metadata direkte fra din maskin til den tjenesten du har valgt, på dine vegne.</p>
    {h2(6,"p6","E-postvarsler")}
    <p>Hvis et program kan sende deg varsler (for eksempel via din egen SMTP-server eller en varslingstjeneste), sendes de med den konfigurasjonen du selv oppgir. Vi mottar ikke kopi av disse varslene.</p>
    {h2(7,"p7","Ingen analyse eller telemetri")}
    <p>Programmene inneholder ingen analyseverktøy, sporing eller telemetri. Vi vet ikke hva du tar opp, viser, planlegger eller publiserer. Programmene kan kontakte en oppdateringstjeneste for å sjekke om en nyere versjon finnes; en slik forespørsel inneholder ikke ditt innhold.</p>
    {h2(8,"p8","Innhold forlater ikke maskinen")}
    <p>Opptak, video og transkripsjon behandles lokalt. Tale-til-tekst (Whisper) kjører på din egen maskin. Ditt innhold forlater maskinen bare når du selv aktiverer en sky-, publiserings- eller delefunksjon, slik beskrevet over.</p>
    {h2(9,"p9","Nettstedet sundaysuite.app")}
    <p>Nettstedet er en informasjonsside. Tar du kontakt via e-postlenkene, behandler vi e-postadressen din og innholdet i henvendelsen for å svare deg. Hvis nettstedet senere tilbyr skjemaer eller nyhetsbrev, vil bruken av disse beskrives her, og du vil kunne melde deg av når som helst.</p>
    {h2(10,"p10","Tredjepartstjenester")}
    <p>Når du aktiverer en integrasjon, gjelder den aktuelle tredjepartens personvernregler for den delen av behandlingen. Eksempler kan være Google (Drive/YouTube), en podkast-host eller en e-postleverandør. Du velger selv om og når disse tas i bruk.</p>
    {h2(11,"p11","Dine rettigheter")}
    <p>Siden de fleste dataene ligger lokalt på din maskin, har du direkte kontroll og kan se, endre, eksportere og slette dem selv. For personopplysninger vi måtte behandle (for eksempel en e-posthenvendelse), har du etter personvernregelverket (GDPR) rett til innsyn, retting, sletting og begrensning. Kontakt oss for å utøve disse rettighetene.</p>
    {h2(12,"p12","Endringer")}
    <p>Vi kan oppdatere denne erklæringen. Vesentlige endringer varsles ved å oppdatere datoen øverst på siden.</p>
    {h2(13,"p13","Kontakt")}
    <p>Spørsmål om personvern? Kontakt behandlingsansvarlig Richard Fossland på <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("no","privacy","Personvernerklæring","Sist oppdatert: 8. juni 2026",note,toc(items),prose)

# ===================================================================== WRITE
def W(path, html):
    full=os.path.join(ROOTDIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(html)
    print("wrote", path)

for lang in ("en","no"):
    pre = "" if lang=="en" else "no/"
    W(pre+"index.html", render_home(lang))
    for s in SLUGS:
        W(pre+f"apps/{s}.html", render_app(lang,s))
    W(pre+"legal/terms.html",   terms_en()   if lang=="en" else terms_no())
    W(pre+"legal/privacy.html", privacy_en() if lang=="en" else privacy_no())
print("done")
