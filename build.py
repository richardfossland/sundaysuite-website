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
 # community-toolbox tool marks
 "quiz":'<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9h18M9 3v18"/><path d="M12.5 13.5l1.5 1.5 3-3.5"/>',
 "chess":'<circle cx="12" cy="5.5" r="2.5"/><path d="M9.5 8.5h5l-1 5h-3z"/><path d="M7 21h10l-1.5-4.5h-7z"/>',
 "trophy":'<path d="M7 4h10v4.5a5 5 0 0 1-10 0z"/><path d="M7 6.5H4.5v1a3 3 0 0 0 3 3M17 6.5h2.5v1a3 3 0 0 1-3 3"/><path d="M12 13.5V17M9 21h6M10.5 17h3"/>',
 "trade":'<path d="M3.5 8.5h13l-3.2-3.2M20.5 15.5h-13l3.2 3.2"/>',
 "wheat":'<path d="M12 21.5V8.5"/><path d="M12 8.5c2.1 0 3.6-1.6 3.6-3.6C13.5 4.9 12 6.5 12 8.5zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 4.9 12 6.5 12 8.5z"/><path d="M12 13c2.1 0 3.6-1.6 3.6-3.6C13.5 9.4 12 11 12 13zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 9.4 12 11 12 13z"/><path d="M12 17.5c2.1 0 3.6-1.6 3.6-3.6C13.5 13.9 12 15.5 12 17.5zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 13.9 12 15.5 12 17.5z"/>',
 "tictactoe":'<path d="M9 3v18M15 3v18M3 9h18M3 15h18"/><path d="M4.7 4.7l2.6 2.6M7.3 4.7L4.7 7.3"/><circle cx="18" cy="18" r="1.9"/>',
 "basar":'<circle cx="12" cy="13" r="8.2"/><path d="M12 4.8v16.4M3.8 13h16.4M6.2 7.2l11.6 11.6M17.8 7.2L6.2 18.8"/><circle cx="12" cy="13" r="1.3" fill="currentColor" stroke="none"/><path d="M12 1.6l2.3 3.2h-4.6z" fill="currentColor" stroke="none"/>',
 "panel":'<path d="M21 4H3a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h4v4l5-4h9a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1z"/><path d="M9.6 9.2a2.4 2.4 0 1 1 3.1 2.5c-.8.3-1.2.8-1.2 1.5v.3"/><path d="M11.5 15.4v.3"/>',
 "licks":'<rect x="3" y="5.5" width="18" height="13" rx="1.6"/><path d="M8 5.5v13M12.5 5.5v13M17 5.5v13"/><rect x="6.8" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/><rect x="11.3" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/><rect x="15.8" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/>',
 "welcome":'<path d="M13.5 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h7.5"/><path d="M13.5 21l5.5-1.8V4.8L13.5 3z"/><circle cx="15.6" cy="12" r="0.9" fill="currentColor" stroke="none"/><path d="M8 12h3M9.7 10.3L8 12l1.7 1.7"/>',
 "school":'<path d="M12 3.5 2.5 8 12 12.5 21.5 8 12 3.5z"/><path d="M6 10.4V15c0 1.6 2.7 3 6 3s6-1.4 6-3v-4.6"/><path d="M21.5 8v5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
 "sync":'<path d="M3 8h13M12.5 4.5L16 8l-3.5 3.5"/><path d="M21 16H8M11.5 12.5L8 16l3.5 3.5"/>',
 "dice":'<rect x="3" y="3" width="18" height="18" rx="3.5"/><circle cx="8.2" cy="8.2" r="1.5" fill="currentColor" stroke="none"/><circle cx="15.8" cy="8.2" r="1.5" fill="currentColor" stroke="none"/><circle cx="8.2" cy="15.8" r="1.5" fill="currentColor" stroke="none"/><circle cx="15.8" cy="15.8" r="1.5" fill="currentColor" stroke="none"/>',
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
 "en":{"lang":"en","other":"NO","nav_products":"Products","nav_phil":"Philosophy","nav_together":"Together","nav_toolbox":"Toolbox",
   "nav_cta":"Get in touch","all_products":"All products","keep_posted":"Keep me posted",
   "nav_build":"Build with us","foot_build":"Build with us",
   "status_labels":{"beta":"Beta","build":"In development","early":"Early days"},
   "status_heads":{"beta":"Status: beta","build":"Status: in development","early":"Status: early days"},
   "family_kicker":"Part of the family",
   "family_title":"Plays well with the rest of Sunday Suite","standalone_title":"Standalone — but part of the family",
   "standalone_lead":"The tool stands entirely on its own, but shares the account, design language and golden thread with the rest of Sunday Suite.",
   "what_kicker":"What it does",
   "foot_tag":"A family of Norwegian-built tools for church and classroom. Twelve apps, one golden thread — open source on GitHub.",
   "foot_products":"Products","foot_suite":"The suite","foot_legal":"Legal","foot_terms":"Terms of Use","foot_privacy":"Privacy",
   "foot_phil":"Philosophy","foot_together":"Better together","foot_toolbox":"Community tools","foot_contact":"Contact",
   "foot_bottom":"&copy; 2026 Sunday Suite &middot; Richard Fossland. Built in Norway.",
   "back_home":"&larr; Back to home","cta_back":"Back to the products",
   "nav_help":"Help","foot_help":"Help &amp; guides","back_help":"&larr; Back to Help"},
 "no":{"lang":"no","other":"EN","nav_products":"Produkter","nav_phil":"Filosofi","nav_together":"Sammen","nav_toolbox":"Verktøykassa",
   "nav_cta":"Ta kontakt","all_products":"Alle produkter","keep_posted":"Hold meg oppdatert",
   "nav_build":"Bygg med oss","foot_build":"Bygg med oss",
   "status_labels":{"beta":"Beta","build":"Under utvikling","early":"Påbegynt"},
   "status_heads":{"beta":"Status: beta","build":"Status: under utvikling","early":"Status: påbegynt"},
   "family_kicker":"Del av familien",
   "family_title":"Spiller sammen med resten av Sunday Suite","standalone_title":"Frittstående — men en del av familien",
   "standalone_lead":"Verktøyet står helt på egne bein, men deler konto, designspråk og den gylne tråden med resten av Sunday Suite.",
   "what_kicker":"Hva det gjør",
   "foot_tag":"En familie av norskbygde verktøy for menighet og klasserom. Tolv apper, én gylden tråd — åpen kildekode på GitHub.",
   "foot_products":"Produkter","foot_suite":"Suiten","foot_legal":"Juridisk","foot_terms":"Vilkår for bruk","foot_privacy":"Personvern",
   "foot_phil":"Filosofi","foot_together":"Bedre sammen","foot_toolbox":"Fellesskapsverktøy","foot_contact":"Kontakt",
   "foot_bottom":"&copy; 2026 Sunday Suite &middot; Richard Fossland. Bygd i Norge.",
   "back_home":"&larr; Tilbake til forsiden","cta_back":"Tilbake til produktene",
   "nav_help":"Hjelp","foot_help":"Hjelp &amp; veiledninger","back_help":"&larr; Tilbake til hjelpen"},
}
SLUGS = ["sundayrec","sundayscreen","sundaystudio","sundaystage","sundayplan","sundaysong","sundayedit","sundaysync","sundaypaper","sundaytranslate","sundayinfo","sundaybooking"]
PNAME = {"sundayrec":"SundayRec","sundayscreen":"SundayScreen","sundaystudio":"SundayStudio","sundaystage":"SundayStage",
         "sundayplan":"SundayPlan","sundaysong":"SundaySong","sundayedit":"SundayEdit","sundaysync":"SundaySync","sundaypaper":"SundayPaper",
         "sundaytranslate":"SundayTranslate","sundayinfo":"SundayInfo","sundaybooking":"SundayBooking"}
# Single source of truth for product maturity: beta / build / early.
# Everything usable is honestly "beta" — the whole suite is open source and unfinished.
# Drives home-card badges, product-page heroes + CTAs and the legal status table.
STATUS = {"sundayrec":"beta","sundayscreen":"beta","sundaystage":"beta",
          "sundayedit":"beta","sundaysync":"beta","sundayinfo":"beta","sundaybooking":"beta",
          "sundaystudio":"build","sundaytranslate":"build",
          "sundayplan":"early","sundaysong":"early","sundaypaper":"early"}

GITHUB_ORG = "https://github.com/SundaySuite-app"

SITE = "https://sundaysuite.app"
def clean_url(path):
    """Repo html path -> canonical live URL (Pages serves clean, extensionless URLs)."""
    if path.endswith("index.html"): path = path[:-len("index.html")]
    elif path.endswith(".html"):    path = path[:-len(".html")]
    return SITE + "/" + path

def links(lang, root):
    base = "" if lang=="en" else "no/"
    helpdir = "help/" if lang=="en" else "no/hjelp/"
    return {
      "assets": root+"assets/",
      "home":   root+base+"index.html",
      "app":    lambda s: root+base+"apps/"+s+".html",
      "legal":  lambda n: root+base+"legal/"+n+".html",
      "help":   lambda n="index": root+helpdir+n+".html",
      "toolbox": root+base+("toolbox.html" if lang=="en" else "verktoykasse.html"),
      "build":  root+base+("build.html" if lang=="en" else "bygg.html"),
    }

def nav(c, L, other_href):
    return (f'<header class="nav" id="nav"><div class="wrap nav-inner">'
      f'<a href="{L["home"]}" class="brand">{CROSS}<span><b>Sunday</b> Suite</span></a>'
      f'<button class="nav-burger" id="navBurger" type="button" aria-label="{"Menu" if c["lang"]=="en" else "Meny"}" aria-controls="navLinks" aria-expanded="false"><span></span><span></span><span></span></button>'
      f'<nav class="links" id="navLinks">'
      f'<a href="{L["home"]}#products" class="linkitem">{c["nav_products"]}</a>'
      f'<a href="{L["home"]}#philosophy" class="linkitem">{c["nav_phil"]}</a>'
      f'<a href="{L["toolbox"]}" class="linkitem">{c["nav_toolbox"]}</a>'
      f'<a href="{L["build"]}" class="linkitem">{c["nav_build"]}</a>'
      f'<a href="{L["help"]("index")}" class="linkitem">{c["nav_help"]}</a>'
      f'<a href="{other_href}" class="lang-switch">{c["other"]}</a>'
      f'<a href="mailto:dev@sundaysuite.app" class="nav-cta">{c["nav_cta"]}</a>'
      f'</nav></div></header>')

def footer(c, L):
    prod = "".join(f'<a href="{L["app"](s)}">{PNAME[s]}</a>' for s in SLUGS)
    return (f'<footer><div class="wrap"><div class="foot-top">'
      f'<div class="foot-brand"><div class="brand">{CROSS}<span><b>Sunday</b> Suite</span></div><p>{c["foot_tag"]}</p></div>'
      f'<div class="foot-cols">'
      f'<div class="foot-col"><h5>{c["foot_products"]}</h5>{prod}</div>'
      f'<div class="foot-col"><h5>{c["foot_suite"]}</h5><a href="{L["home"]}#philosophy">{c["foot_phil"]}</a><a href="{L["home"]}#together">{c["foot_together"]}</a><a href="{L["toolbox"]}">{c["foot_toolbox"]}</a><a href="{L["build"]}">{c["foot_build"]}</a><a href="{L["help"]("index")}">{c["foot_help"]}</a><a href="{GITHUB_ORG}" target="_blank" rel="noopener">GitHub</a><a href="mailto:dev@sundaysuite.app">{c["foot_contact"]}</a></div>'
      f'<div class="foot-col"><h5>{c["foot_legal"]}</h5><a href="{L["legal"]("terms")}">{c["foot_terms"]}</a><a href="{L["legal"]("privacy")}">{c["foot_privacy"]}</a></div>'
      f'</div></div>'
      f'<div class="foot-bottom"><div>{c["foot_bottom"]}</div><div><a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> &middot; sundaysuite.app</div></div>'
      f'</div></footer>')

def shell(c, L, other_href, title, desc, body_open, content, navscrolled=False, pair=None):
    nv = nav(c, L, other_href)
    if navscrolled: nv = nv.replace('class="nav"','class="nav scrolled"')
    seo = ""
    if pair:
        en_url, no_url = clean_url(pair[0]), clean_url(pair[1])
        own = en_url if c["lang"]=="en" else no_url
        seo = (f'<link rel="canonical" href="{own}" />\n'
               f'<link rel="alternate" hreflang="en" href="{en_url}" />\n'
               f'<link rel="alternate" hreflang="no" href="{no_url}" />\n'
               f'<link rel="alternate" hreflang="x-default" href="{en_url}" />\n'
               f'<meta property="og:url" content="{own}" />\n')
    return (f'<!DOCTYPE html>\n<html lang="{c["lang"]}">\n<head>\n<meta charset="UTF-8" />\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
      f'<title>{title}</title>\n<meta name="description" content="{desc}" />\n'
      f'<link rel="icon" href="{L["assets"]}favicon.svg" type="image/svg+xml" />\n'
      f'{seo}'
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
   "eyebrow":"Norwegian-built church technology · open source · in beta",
   "h1":'Twelve tools.<br><em>One golden thread.</em>',
   "sub":"Sunday Suite is a family of open-source programs for the modern church — from recording, multicam sync and streaming to presentation, planning, song, podcasting, captioning and print. Each tool stands on its own, but they share one account, one design language, and one thread of gold.",
   "b1":"See the products","b2":"Why Sunday?",
   "m1":"<b>12</b> products, one ecosystem","m2":"<b>Open source</b> — built in the open on GitHub","m3":"<b>Local-first</b> — your data stays with you",
   "g_kicker":"The products","g_title":"The family of Sunday apps",
   "g_lead":"Twelve tools — seven in beta you can try today, the rest on the workbench. Each product owns its own deep jewel tone, and the golden cross binds them together. Click through to read more about each one.",
   "grp_now":"Try today","grp_dev":"In development","grp_early":"On the drawing board",
   "one_h":"One Sunday account","one_tag":"Sign in once",
   "one_p":"The goal: one account signs you into every tool, and what you do in one program shows up where it's needed in the others — no double work.",
   "one_f":["Single sign-on","Shared design language","Secure key handling"],
   "p_kicker":"The philosophy","p_h2":'The first church-technology ecosystem built for <em>Nordic reality</em>.',
   "p_lead":"The world's best church tools are built for American churches. Sunday Suite starts with the Norwegian and Nordic reality — TONO, Bokmål and Nynorsk, privacy and local control — and has global ambitions from there.",
   "moat":[("star","TONO as a first-class citizen","TONO is part of the data model from the first row: every work can carry a TONO ID, and every use can note whether it was streamed (a separate royalty pool). It has started shipping, too — the SundayStage beta already exports a TONO and CCLI usage log of what actually reached the screen."),
           ("shield","Local and private first","Recording, video and transcription run on your own machine. Your data stays with you unless you choose to share it."),
           ("people","One account, all Sunday","The goal is one sign-in across Rec, Stage, Plan and Song, with keys kept safely in the keychain.")],
   "mg_kicker":"Better together","mg_title":"When the tools talk to each other",
   "mg_lead":"The real magic happens at the seams. This is how the Sunday apps are designed to play together as they're finished.",
   "chips":[("Stage","Rec","cue becomes a chapter marker"),("Stage","Rec","lyrics become SRT captions"),
            ("Plan","Stage","setlist becomes a published service"),("Rec","Plan","transcript returns as metadata"),
            ("Stage","Song","every shown song can be logged for TONO/CCLI"),("Plan","Paper","setlist becomes a printed program in one click"),
            ("Paper","Song","a scanned songbook becomes catalog entries"),("Rec","Paper","the sermon becomes a parish-magazine draft"),
            ("Rec","Sync","recordings become a multicam timeline"),
            ("Rec","Edit","sermon + transcript ready for captioning")],
   "os_kicker":"Built in the open","os_h":"Open source. Honestly unfinished.",
   "os_p":"All of Sunday Suite is built in the open — the code lives on GitHub, the betas are free, and the roadmap is shaped by the churches that use it. If you can test, translate, design or code, there's a place for you at the workbench.",
   "os_btn":"Build with us","os_gh":"See the code on GitHub",
   "tb_kicker":"Beyond the suite","tb_title":"A little toolbox for building community",
   "tb_lead":"Alongside the twelve core products, Sunday Suite tinkers with small, playful tools for church and classroom — games and group activities that help people meet, mix and connect. They run straight in the browser, nothing to install. A corner of the workshop that will keep growing.",
   "tb_note":"More fellowship tools are on the workbench. Have an idea for one?",
   "tb_open":"Open","tb_soon":"Coming soon","tb_more":"Explore the whole toolbox",
   "cta_h":"Let's build a better Sunday together.",
   "cta_p":"Try a beta, help build the suite, or just tell us what your church needs. We'd love to hear from you.",
   "cta_back":"Back to the products"},
 "no":{"title":"Sunday Suite — Verktøyene for den moderne menigheten",
   "desc":"Sunday Suite er en familie av norskbygde verktøy for menigheten: opptak, presentasjon, planlegging, sang, podkast, teksting og dokumenter — bundet sammen av én gylden tråd.",
   "eyebrow":"Norskbygd kirketeknologi · åpen kildekode · i beta",
   "h1":'Tolv verktøy.<br><em>Én gylden tråd.</em>',
   "sub":"Sunday Suite er en familie av åpen kildekode-programmer for den moderne menigheten — fra opptak, multikam-synk og strømming til presentasjon, planlegging, sang, podkast, teksting og trykksaker. Hvert verktøy står på egne bein, men deler én konto, ett designspråk og én tråd av gull.",
   "b1":"Se programmene","b2":"Hvorfor Sunday?",
   "m1":"<b>12</b> produkter, ett økosystem","m2":"<b>Åpen kildekode</b> — bygges i det åpne på GitHub","m3":"<b>Lokalt først</b> — dine data blir hos deg",
   "g_kicker":"Produktene","g_title":"Familien av Sunday-apper",
   "g_lead":"Tolv verktøy — sju i beta som du kan prøve i dag, resten på arbeidsbenken. Hvert produkt eier sin egen dype juveltone, og det gylne korset binder dem sammen. Klikk deg inn for å lese mer om hvert program.",
   "grp_now":"Prøv i dag","grp_dev":"Under utvikling","grp_early":"På tegnebrettet",
   "one_h":"Én Sunday-konto","one_tag":"Logg inn én gang",
   "one_p":"Målet: én konto signerer deg inn på alle verktøyene, og det du gjør i ett program dukker opp der det trengs i de andre — uten dobbeltarbeid.",
   "one_f":["Felles innlogging","Delt designspråk","Sikker nøkkelhåndtering"],
   "p_kicker":"Filosofien","p_h2":'Det første kirketeknologi&shy;økosystemet bygd for <em>nordisk virkelighet</em>.',
   "p_lead":"Verdens beste menighetsverktøy er bygd for amerikanske kirker. Sunday Suite starter med den norske og nordiske hverdagen — TONO, bokmål og nynorsk, personvern og lokal kontroll — og har globale ambisjoner derfra.",
   "moat":[("star","TONO i førsteklasse","TONO er en del av datamodellen fra første rad: hvert verk kan bære en TONO-ID, og hver bruk kan merke om den ble strømmet (egen royalty-pott). Og det har begynt å rekke ut — SundayStage-betaen eksporterer allerede en TONO- og CCLI-logg over det som faktisk nådde skjermen."),
           ("shield","Lokalt og privat først","Opptak, video og transkripsjon kjøres på din egen maskin. Dataene blir hos deg med mindre du selv velger å dele."),
           ("people","Én konto, hele søndagen","Målet er at én innlogging signerer deg inn på Rec, Stage, Plan og Song, med nøkler trygt i nøkkelringen.")],
   "mg_kicker":"Bedre sammen","mg_title":"Når verktøyene snakker sammen",
   "mg_lead":"Den virkelige magien skjer i skjøtene. Slik er Sunday-appene designet for å spille sammen etter hvert som de blir ferdige.",
   "chips":[("Stage","Rec","cue blir kapittelmerke i opptaket"),("Stage","Rec","sangtekst blir SRT-teksting"),
            ("Plan","Stage","setliste blir publisert gudstjeneste"),("Rec","Plan","transkripsjon tilbake som metadata"),
            ("Stage","Song","hver vist sang kan loggføres for TONO/CCLI"),("Plan","Paper","setliste blir trykt program med ett klikk"),
            ("Paper","Song","skannet sangbok blir katalogoppføringer"),("Rec","Paper","preken blir menighetsblad-utkast"),
            ("Rec","Sync","opptak blir multikam-tidslinje"),
            ("Rec","Edit","preken + transkripsjon klar for teksting")],
   "os_kicker":"Bygges i det åpne","os_h":"Åpen kildekode. Ærlig uferdig.",
   "os_p":"Hele Sunday Suite bygges i det åpne — koden bor på GitHub, betaene er gratis, og veikartet formes av menighetene som bruker verktøyene. Kan du teste, oversette, designe eller kode, er det plass til deg ved arbeidsbenken.",
   "os_btn":"Bygg med oss","os_gh":"Se koden på GitHub",
   "tb_kicker":"Utenfor suiten","tb_title":"En liten verktøykasse for å bygge fellesskap",
   "tb_lead":"Ved siden av de tolv kjerneproduktene snekrer Sunday Suite på små, lekne verktøy for menighet og klasserom — spill og gruppeaktiviteter som hjelper folk å møtes, bli kjent og knytte bånd. De kjører rett i nettleseren, uten installasjon. En krok av verkstedet som bare kommer til å vokse.",
   "tb_note":"Flere fellesskapsverktøy ligger på arbeidsbenken. Har du en idé til ett?",
   "tb_open":"Åpne","tb_soon":"Kommer snart","tb_more":"Utforsk hele verktøykassa",
   "cta_h":"La oss bygge en bedre søndag sammen.",
   "cta_p":"Prøv en beta, bli med og bygg suiten, eller bare fortell oss hva menigheten din trenger. Vi vil gjerne høre fra deg.",
   "cta_back":"Tilbake til produktene"},
}

# per-card teaser content (tag / desc / feats), keyed by slug then lang
CARD = {
 "sundayrec":{"accent":"rec","icon":"rec",
   "en":("Record · stream · publish","Records the service, transcribes the sermon, streams live and publishes the podcast — by itself. The mature core of the suite, out in beta.",["Audio &amp; video","Live stream","AI transcription","Podcast"]),
   "no":("Opptak · strømming · podkast","Tar opp gudstjenesten, transkriberer talen, strømmer live og publiserer podkasten — av seg selv. Den modne kjernen i suiten, ute i beta.",["Lyd &amp; video","Live-strøm","AI-transkripsjon","Podkast"])},
 "sundayscreen":{"accent":"screen","icon":"clock",
   "en":("Offline classroom screen","Plan the lesson by designing the screen it will show — clock, timer, name picker, groups, traffic light, a link with a QR code and images. Calm, fullscreen, and needs no internet at all.",["Lesson planner","Link &amp; QR","Class profiles","Fully offline"]),
   "no":("Offline klasseromsskjerm","Planlegg timen ved å designe skjermen den skal vise — klokke, timer, navnetrekker, grupper, trafikklys, lenke med QR-kode og bilder. Rolig, i fullskjerm, og helt uten behov for nett.",["Timeplanlegger","Lenke &amp; QR","Klasseprofiler","Helt offline"])},
 "sundaystudio":{"accent":"studio","icon":"mic",
   "en":("Podcast &amp; jingle production","The simplest professional podcast producer: many mics at once, AI cleanup, a jingle in under a minute, and a finished, normalized MP3.",["Multi-mic","AI mastering","Jingle","Export"]),
   "no":("Podkast- &amp; jingleproduksjon","Den enkleste proffe podkastprodusenten: mange mikrofoner samtidig, AI-opprydding, en jingle på under ett minutt og en ferdig, normalisert MP3.",["Fleirmikrofon","AI-mastering","Jingle","Eksport"])},
 "sundaystage":{"accent":"stage","icon":"screen",
   "en":("On-screen presentation","Lyrics, Bible verses and media on the screen behind the altar — a Nordic alternative to ProPresenter, with cue control and safe, isolated output.",["Lyrics","Cues","Output lock","TONO log"]),
   "no":("Presentasjon på storskjerm","Sangtekster, bibelvers og media på skjermen bak alteret — et nordisk alternativ til ProPresenter, med køstyring og trygg, isolert visning.",["Sangtekster","Køer","Output-lås","TONO-logg"])},
 "sundayplan":{"accent":"plan","icon":"calendar",
   "en":("Planning &amp; volunteer rota","Plan the service and schedule volunteers in minutes. A fair auto-fill engine balances skill, rotation and burnout.",["Service plan","Auto-rota","SMS","TONO status"]),
   "no":("Planlegging &amp; frivillig-turnus","Planlegg gudstjenesten og sett opp de frivillige på minutter. En rettferdig auto-fyll-motor balanserer kompetanse, rotasjon og utbrenthet.",["Tjenesteplan","Auto-turnus","SMS","TONO-status"])},
 "sundaysong":{"accent":"song","icon":"note",
   "en":("Song database with AI &amp; TONO","Find the right song with semantic search and AI across languages — with TONO and CCLI as first-class fields in the data model from the start.",["Semantic search","AI picks","TONO + CCLI","Multilingual"]),
   "no":("Sangdatabase med AI &amp; TONO","Finn riktig sang med semantisk søk og AI på tvers av språk — med TONO og CCLI som førsteklasses felt i datamodellen fra start.",["Semantisk søk","AI-forslag","TONO + CCLI","Fleirspråk"])},
 "sundayedit":{"accent":"edit","icon":"caption",
   "en":("AI video captioning","Caption video ten times faster. Every word gets a confidence score and is colour-coded — you fix only the amber. Local and private: the video is never uploaded.",["Confidence","Context priming","Local Whisper","SRT/VTT"]),
   "no":("AI-teksting av video","Tekst video ti ganger raskere. Hvert ord får en konfidens-score og fargemarkeres — du retter bare det gule. Lokal og privat: videoen lastes aldri opp.",["Konfidens","Kontekst-priming","Lokal Whisper","SRT/VTT"])},
 "sundaysync":{"accent":"sync","icon":"sync",
   "en":("Multicam audio sync","Drop in every camera and recorder from the service; get back one synchronized timeline as FCPXML for DaVinci Resolve. No timecode needed — the audio itself is the clock.",["Any cameras","FCPXML out","No timecode","Fully local"]),
   "no":("Multikam lydsynk","Slipp inn alle kameraer og opptakere fra gudstjenesten; få tilbake én synkronisert tidslinje som FCPXML for DaVinci Resolve. Ingen timekode — lyden selv er klokka.",["Alle kameraer","FCPXML ut","Ingen timekode","Helt lokalt"])},
 "sundaypaper":{"accent":"paper-c","icon":"doc",
   "en":("AI document &amp; PDF tool","Split songbooks, lay out service programs, parish magazines, large-print editions and forms — with professional Typst layout and OCR under the hood.",["Songbook split","Programs","Parish mag","Large print"]),
   "no":("AI-dokument &amp; PDF-verktøy","Splitt sangbøker, sett opp gudstjenesteprogrammer, lag menighetsblad, storskrift-utgaver og skjemaer — med profesjonell Typst-layout og OCR under panseret.",["Sangbok-splitt","Programmer","Menighetsblad","Storskrift"])},
 "sundaytranslate":{"accent":"translate","icon":"globe",
   "en":("Live translation &amp; hearing help","Anyone in the pew hears the service in their own language — or louder and clearer — straight in their earbuds. An interpreter speaks; phones listen. Nothing to install.",["Live interpreting","Assistive listening","AI captions","Any phone"]),
   "no":("Live tolking &amp; lyttehjelp","Hvem som helst i benken hører gudstjenesten på sitt eget språk — eller klarere og høyere — rett i øreproppene. En tolk snakker; mobilene lytter. Ingenting å installere.",["Live tolking","Lytteanlegg","AI-undertekster","Hvilken som helst mobil"])},
 "sundayinfo":{"accent":"info","icon":"screen",
   "en":("Digital signage for the church","Turn any TV into the church noticeboard — service times, today's plan, weather and a Bible verse. Pair a screen in seconds; it keeps running even if the network drops.",["Any screen","Multi-editor","Church year","Works offline"]),
   "no":("Digital infoskjerm for menigheten","Gjør en hvilken som helst TV til menighetens infotavle — gudstjenestetider, dagens plan, vær og bibelvers. Par en skjerm på sekunder; den går videre selv om nettet faller.",["Enhver skjerm","Flere redaktører","Kirkeår","Virker offline"])},
 "sundaybooking":{"accent":"booking","icon":"calendar",
   "en":("Rooms, rentals &amp; appointments","Book rooms, rentals and appointments without double-bookings — the calendar makes overlaps structurally impossible. Signs in with your Sunday account.",["No double-booking","Rooms &amp; rentals","Approval queue","Shared account"]),
   "no":("Rom, utleie &amp; avtaler","Book rom, utleie og avtaler uten dobbeltbooking — kalenderen gjør overlapp strukturelt umulig. Logger inn med Sunday-kontoen din.",["Ingen dobbeltbooking","Rom &amp; utleie","Godkjenningskø","Delt konto"])},
}

# community-toolbox tools (live web apps on *.sundaysuite.app); soon=not yet deployed
TOOLS = [
 {"name":"SundayQuiz","accent":"quiz","icon":"quiz","url":"https://quiz.sundaysuite.app","live":True,
  "en":("Icebreaker","Get-to-know-you bingo for a first gathering — everyone hunts for people who match the squares, and the room warms up fast.","Any group · 5 min"),
  "no":("Bli kjent","Bli-kjent-bingo for første samling — alle jakter på folk som passer rutene, og rommet tiner opp på et blunk.","Enhver gruppe · 5 min")},
 {"name":"SundayChess","accent":"chess","icon":"chess","url":"https://chess.sundaysuite.app","live":True,
  "en":("Classroom","A big-screen chess tournament for the classroom — Swiss rounds and a knockout, run from one screen with a solo bot to practice against.","Classroom · solo or teams"),
  "no":("Klasserom","Sjakkturnering på storskjerm for klasserommet — sveitsiske runder og sluttspill, styrt fra én skjerm, med solo-bot å øve mot.","Klasserom · solo eller lag")},
 {"name":"SundayTurnering","accent":"turnering","icon":"trophy","url":"https://turnering.sundaysuite.app","live":True,
  "en":("Sport &amp; play","A live tournament board for any sport or game — leagues, cups and playoffs, with a big-screen view and a phone in every hand.","Any sport · league or cup"),
  "no":("Idrett &amp; lek","Live turneringstavle for hvilken som helst idrett eller lek — serie, cup og sluttspill, med storskjerm-visning og en telefon i hver hånd.","Enhver idrett · serie eller cup")},
 {"name":"SundayMarket","accent":"market","icon":"trade","url":"https://marked.sundaysuite.app","live":True,
  "en":("Group game","A fast, friendly trading game for a group — buy low, sell high, dodge the famine and out-trade the table before the bell.","Group · fast rounds"),
  "no":("Gruppespill","Et kjapt og vennlig handelsspill for en gruppe — kjøp billig, selg dyrt, unngå hungersnøden og slå bordet før det ringer ut.","Gruppe · raske runder")},
 {"name":"SundayHarvest","accent":"harvest","icon":"wheat","url":"https://harvest.sundaysuite.app","live":True,
  "en":("Party game","Biblical social deduction — wheat among the tares (Matthew 13). No one gets eliminated; everyone plays to the final reveal.","Party · no elimination"),
  "no":("Selskapsspill","Bibelsk social deduction — hvete blant ugresset (Matteus 13). Ingen elimineres; alle er med helt til den store avsløringen.","Selskap · ingen utslag")},
 {"name":"SundayTicTacToe","accent":"tictactoe","icon":"tictactoe","url":"https://tictactoe.sundaysuite.app","live":True,
  "en":("Classroom","Tic-tac-toe as a tournament — three board sizes, Swiss rounds and a knockout, run from one screen with a bot to practise against.","Classroom · 3×3 to 5×5"),
  "no":("Klasserom","Bondesjakk som turnering — tre brettstørrelser, sveitsiske runder og sluttspill, styrt fra én skjerm, med en bot å øve mot.","Klasserom · 3×3 til 5×5")},
 {"name":"SundayBasar","accent":"basar","icon":"basar","url":"https://basar.sundaysuite.app","live":True,
  "en":("Fundraiser","A digital church bazaar — sell raffle tickets and draw the prizes live on the big screen. The app never touches money; you confirm each Vipps payment yourself.","Any event · live draw"),
  "no":("Basar","En digital bedehus-basar — selg årer og trekk premiene live på storskjerm. Appen rører aldri penger; du bekrefter hver Vipps-betaling selv.","Arrangement · live trekning")},
 {"name":"SundayPanel","accent":"panel","icon":"panel","url":"https://panel.sundaysuite.app","live":True,
  "en":("Youth","Anonymous questions from the floor to a panel on the big screen — no app, no login. Everyone asks with a word-code or QR; you curate what goes up.","Youth · word-code or QR"),
  "no":("Ungdom","Anonyme spørsmål fra salen til et panel på storskjerm — ingen app, ingen innlogging. Alle spør med ordkode eller QR; du velger hva som vises.","Ungdom · ordkode eller QR")},
 {"name":"SundayLicks","accent":"licks","icon":"licks","url":"https://licks.sundaysuite.app","live":True,
  "en":("Band practice","A practice library of gospel and worship licks for piano, guitar and bass — live tempo and transpose to any key. Everything plays from notes, never audio, so it never stutters.","Piano · guitar · bass"),
  "no":("Bandøving","Et øvingsbibliotek av gospel- og lovsang-licks for piano, gitar og bass — live tempo og transponering til alle tonearter. Alt spilles fra noter, aldri lyd, så det aldri hakker.","Piano · gitar · bass")},
 {"name":"SundayWelcome","accent":"welcome","icon":"welcome","url":"https://welcome.sundaysuite.app","live":True,
  "en":("Welcome newcomers","A digital welcome note for first-time visitors — they scan a QR, leave their details, and the team follows up. No one falls through the cracks.","Newcomer follow-up"),
  "no":("Ta imot nykommere","En digital velkomstlapp for førstegangsbesøkende — de skanner en QR, legger igjen kontaktinfo, og teamet følger opp. Ingen faller mellom to stoler.","Nykommer-oppfølging")},
 {"name":"SundaySchool","accent":"school","icon":"school","url":"https://school.sundaysuite.app","live":True,
  "en":("Music & theology school","The church's own school — eleven subjects, from piano, guitar, bass and drums to worship planning, sight-reading, rhythm and sound tech, plus theology. A rights-cleared library of 51 hymns in 104 playable arrangements.","11 subjects · 51 hymns · 104 arrangements"),
  "no":("Musikk- og teologiskole","Menighetens egen skole — elleve fag, fra piano, gitar, bass og trommer til lovsangsledelse, bladspill, rytme og lydteknikk, pluss teologi. Et rettighetsklarert bibliotek med 51 salmer i 104 spillbare arrangementer.","11 fag · 51 verk · 104 arrangementer")},
]

# copy for the dedicated toolbox landing page (/toolbox.html + /no/verktoykasse.html)
TBPAGE = {
 "en":{"title":"The Sunday toolbox — free community games for church &amp; classroom | Sunday Suite",
   "desc":"A little toolbox of free, browser-based games and group activities from Sunday Suite — icebreakers, classroom chess, tournaments and more. Nothing to install.",
   "crumb":"Toolbox","kicker":"Beyond the suite","h1":"The Sunday toolbox",
   "tagline":"Small, playful tools for church and classroom.",
   "lead":"Free, browser-based games and group activities that help people meet, mix and connect — alongside the twelve core Sunday Suite products. Nothing to install: open one on the big screen, everyone joins on their phones.",
   "meta":["<b>Free</b> — no account needed","<b>Nothing to install</b> — runs in the browser","<b>Phones</b> + a big screen"],
   "act_browse":"Browse the tools","act_back":"Back to the suite",
   "g_kicker":"The tools","g_title":"Gather a room in one click",
   "g_lead":"Each one runs live in the browser — open it on a shared screen and everyone joins from a phone. Click a card to start.",
   "cta_h":"Part of one golden thread.","cta_p":"These little tools share the design language — and the heart — of the twelve core Sunday Suite apps. Have an idea for the next one? We'd love to hear it.",
   "cta_suite":"See the products","cta_mail":"dev@sundaysuite.app"},
 "no":{"title":"Verktøykassa — gratis fellesskapsspill for menighet og klasserom | Sunday Suite",
   "desc":"En liten verktøykasse med gratis, nettleserbaserte spill og gruppeaktiviteter fra Sunday Suite — bli-kjent-leker, klasseromssjakk, turneringer og mer. Ingenting å installere.",
   "crumb":"Verktøykassa","kicker":"Utenfor suiten","h1":"Verktøykassa",
   "tagline":"Små, lekne verktøy for menighet og klasserom.",
   "lead":"Gratis, nettleserbaserte spill og gruppeaktiviteter som hjelper folk å møtes, bli kjent og knytte bånd — ved siden av de tolv kjerneproduktene i Sunday Suite. Ingenting å installere: åpne ett på storskjermen, og alle blir med fra sine egne telefoner.",
   "meta":["<b>Gratis</b> — ingen konto","<b>Ingen installasjon</b> — kjører i nettleseren","<b>Telefoner</b> + storskjerm"],
   "act_browse":"Se verktøyene","act_back":"Tilbake til suiten",
   "g_kicker":"Verktøyene","g_title":"Samle rommet med ett klikk",
   "g_lead":"Hvert verktøy kjører live i nettleseren — åpne det på en storskjerm, så blir alle med fra telefonen. Klikk på et kort for å starte.",
   "cta_h":"En del av den samme gylne tråden.","cta_p":"Disse små verktøyene deler designspråket — og hjertet — med de tolv kjerneproduktene i Sunday Suite. Har du en idé til det neste? Vi vil gjerne høre den.",
   "cta_suite":"Se produktene","cta_mail":"dev@sundaysuite.app"},
}

def toolbox_cards(lang, h):
    """The shared workbench card grid — used by the home teaser and the dedicated page."""
    arrow = sv("arrowne","2.5")
    cards=""
    for i,t in enumerate(TOOLS):
        tag,desc,setting = t[lang]; live=t["live"]; d=f' data-d="{(i%3)+1}"' if i%3 else ""
        suffix=t["name"][6:]
        ico=sv(t.get("icon","sparkle"),"1.9")
        inner=(f'<span class="tb-glow" aria-hidden="true"></span>'
          f'<div class="tb-head"><span class="tb-ico">{ico}</span><span class="tb-tag">{tag}</span></div>'
          f'<h4><span class="sunday">Sunday</span>{suffix}</h4><p>{desc}</p>')
        go=(f'<span class="tb-go">{h["tb_open"]}{arrow}</span>' if live else f'<span class="tb-go">{h["tb_soon"]}</span>')
        foot=f'<div class="tb-foot"><span class="tb-set">{setting}</span>{go}</div>'
        if live:
            cards+=(f'      <a class="tb-card reveal"{d} style="--c:var(--{t["accent"]})" href="{t["url"]}" '
              f'target="_blank" rel="noopener">{inner}{foot}</a>\n')
        else:
            cards+=(f'      <div class="tb-card soon reveal"{d} style="--c:var(--{t["accent"]})">{inner}{foot}</div>\n')
    return cards

def render_toolbox(lang, h, c, L):
    rarrow = sv("arrow","2.5")
    cards = toolbox_cards(lang, h)
    return (f'''<section class="toolbox" id="toolbox">
  <span class="tb-aura" aria-hidden="true"></span>
  <div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{h["tb_kicker"]}</div><h2 class="section-title">{h["tb_title"]}</h2><p class="section-lead">{h["tb_lead"]}</p></div>
  <div class="tb-grid">
{cards}  </div>
  <div class="tb-cta reveal"><a class="btn btn-ghost" href="{L["toolbox"]}">{h["tb_more"]}{rarrow}</a></div>
  <p class="tb-note reveal">{h["tb_note"]} <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a></p>
</div></section>''')

def render_toolbox_page(lang):
    c=CH[lang]; h=HOME[lang]; p=TBPAGE[lang]
    root="" if lang=="en" else "../"; L=links(lang,root)
    other = "no/verktoykasse.html" if lang=="en" else "../toolbox.html"
    cards = toolbox_cards(lang, h)
    meta = "".join(f"<div>{m}</div>" for m in p["meta"])
    content=(f'''<main>
<section class="app-hero"><div class="grain"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><span>{p["crumb"]}</span></div>
  <div class="app-hero-inner">
    <div class="section-kicker" style="color:var(--gold)">{p["kicker"]}</div>
    <h1 class="app-title" style="margin-top:14px">{p["h1"]}</h1>
    <div class="app-tagline">{p["tagline"]}</div>
    <p class="app-lead">{p["lead"]}</p>
    <div class="hero-meta" style="margin-top:34px; justify-content:flex-start">{meta}</div>
    <div class="app-hero-actions"><a href="#tools" class="btn btn-primary">{p["act_browse"]}</a><a href="{L["home"]}#products" class="btn btn-ghost">{p["act_back"]}</a></div>
  </div>
</div></section>

<section class="toolbox" id="tools">
  <span class="tb-aura" aria-hidden="true"></span>
  <div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{p["g_kicker"]}</div><h2 class="section-title">{p["g_title"]}</h2><p class="section-lead">{p["g_lead"]}</p></div>
  <div class="tb-grid">
{cards}  </div>
  <p class="tb-note reveal">{h["tb_note"]} <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a></p>
</div></section>

<section class="app-cta"><div class="wrap">
  <h2>{p["cta_h"]}</h2><p>{p["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="{L["home"]}#products" class="btn btn-primary">{p["cta_suite"]}</a><a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">{p["cta_mail"]}</a></div>
</div></section>
</main>''')
    return shell(c,L,other,p["title"],p["desc"],' style="--c:var(--gold)"',content,pair=("toolbox.html","no/verktoykasse.html"))

def status_badge(st, c, on_ink=False):
    return f'<span class="status{" on-ink" if on_ink else ""} {st}">{c["status_labels"][st]}</span>'

# ============================================================== BUILD WITH US
# Apps served by the suite's update rings (stable/beta) — gets "beta ring" links.
RING_APPS = {"sundayrec","sundayscreen","sundaystage","sundaysync"}

# Public repositories, shown on the build page. lic None = licence file on its way.
REPOS = [
 {"name":"sundayrec","repo":"SundaySuite-app/sundayrec","lic":"MIT","en":"Automatic church service recorder","no":"Automatisk gudstjenesteopptaker"},
 {"name":"sundayscreen","repo":"SundaySuite-app/sundayscreen","lic":"MIT","en":"Offline classroom screen","no":"Offline klasseromsskjerm"},
 {"name":"sundaystage","repo":"SundaySuite-app/sundaystage","lic":"MIT","en":"Live presentation for churches","no":"Live presentasjon for menigheter"},
 {"name":"sundaystage-web","repo":"SundaySuite-app/sundaystage-web","lic":"MIT","en":"Web companion for SundayStage","no":"Web-følgesvenn for SundayStage"},
 {"name":"sundaysync","repo":"SundaySuite-app/sundaysync","lic":"MIT","en":"Multicam audio sync &rarr; FCPXML","no":"Multikam lydsynk &rarr; FCPXML"},
 {"name":"sundaytranslate","repo":"SundaySuite-app/sundaytranslate","lic":"MIT","en":"Live interpretation &amp; captions","no":"Live tolking &amp; undertekster"},
 {"name":"sundaytranslate-relay","repo":"SundaySuite-app/sundaytranslate-relay","lic":"MIT","en":"Local audio relay for SundayTranslate","no":"Lokal lydrelé for SundayTranslate"},
 {"name":"sundayedit","repo":"SundaySuite-app/sundayedit","lic":"MIT","en":"AI video captioning","no":"AI-teksting av video"},
 {"name":"sundaystudio","repo":"SundaySuite-app/sundaystudio","lic":"MIT","en":"Podcast &amp; jingle production","no":"Podkast- &amp; jingleproduksjon"},
 {"name":"sundayschool","repo":"richardfossland/sundayschool","lic":"MIT","en":"Music &amp; theology school (toolbox)","no":"Musikk- og teologiskole (verktøykassa)"},
 {"name":"sundaychess","repo":"richardfossland/sundaychess","lic":"MIT","en":"Classroom chess tournaments (toolbox)","no":"Klasseromssjakk-turneringer (verktøykassa)"},
]

BUILDPAGE = {
 "en":{"title":"Build with us — open-source church tools | Sunday Suite",
   "desc":"Sunday Suite is an open-source, honestly unfinished family of church tools. Try the betas, read the code on GitHub, and help build twelve tools for the churches of the Nordics — and beyond.",
   "crumb":"Build with us","kicker":"Open source","h1":"Build a better Sunday with us.",
   "tagline":"Open-source church tools — free, unfinished, and honest about both.",
   "lead":"Sunday Suite is one developer in Norway building twelve tools in the open, with the doors unlocked and the lights on. The code lives on GitHub, the betas are free, and the roadmap is shaped by the churches that use them. This page is the workbench — pull up a chair.",
   "m_beta":"apps in beta today","m_code":"<b>The code</b> — public on GitHub","m_lic":"<b>MIT</b> — every repository",
   "act_gh":"Sunday Suite on GitHub","act_mail":"dev@sundaysuite.app",
   "hn_kicker":"Read this first","hn_title":"What “unfinished” honestly means",
   "hn_lead":"We would rather under-promise on a website than let you down on a Sunday. Here is exactly how far each tier has come:",
   "hn_feats":[("check","Beta","It works, and we use it ourselves — but keep a fallback the first Sundays, and expect rough edges. Your bug report is worth gold."),
     ("sliders","In development","Real code, real progress, not ready for your service yet. Follow along, or help it get there faster."),
     ("doc","On the drawing board","A vision and an architecture, honestly still on paper. The best time to tell us what your church needs.")],
   "hn_note":"The apps send nothing home unless you opt in to anonymous telemetry — so when something breaks, we usually don't know. A two-line email about what went wrong is a genuine contribution.",
   "bt_kicker":"Try the betas","bt_title":"Seven betas, ready for a test drive",
   "bt_lead":"Five desktop apps for Mac and Windows, two web apps in the browser — all free, no account needed for the downloads. The buttons always fetch the newest release.",
   "bt_ring":"Fresh from the beta ring:","bt_more":"Read more",
   "code_kicker":"The code","code_title":"Every repository, open on GitHub",
   "code_lead":"All of it is MIT-licensed: read it, learn from it, run it, fork it. Each repository carries a CONTRIBUTING guide to get you started. The only thing the licence doesn't hand over is the brand — fork the code freely, but give your fork its own name.",
   "lic_pending":"licence on its way",
   "ways_kicker":"Ways to help","ways_title":"Six ways to build with us",
   "ways_lead":"You don't need to be a developer — the most valuable contributions often come from the people running the projector on Sunday.",
   "ways":[("check","Test &amp; report","Use a beta for something real and tell us what broke — in a GitHub issue or a plain email. This is the contribution we need most."),
     ("code","Write code","Rust, TypeScript, Svelte, Preact — pick a repo, open an issue to say hello, and send a pull request."),
     ("globe","Translate","Norwegian Bokmål and Nynorsk are first-class here, and more languages are welcome — translation files are friendly territory for a first contribution."),
     ("sparkle","Design","Icons, layouts, the feel of a screen in a dark church — if you have the eye, the suite has the canvas."),
     ("text","Improve the guides","The help section is written for volunteers, not developers. If a guide confused you, that's a bug — tell us or rewrite it."),
     ("star","Tell us what you need","The roadmap is shaped by real churches. Two sentences about your Sunday morning can change what gets built next.")],
   "how_head":"How we work",
   "how_p":"Bugs and ideas go in a GitHub issue on the repo in question, or to <a href=\"mailto:dev@sundaysuite.app\">dev@sundaysuite.app</a> if GitHub isn't your thing. Every repository carries a CONTRIBUTING guide with the specifics. There is no ticket robot and no call centre — every message lands with the person who wrote the code, and every one gets an answer.",
   "cta_h":"One golden thread. Many hands.","cta_p":"Whether you test one beta on one Sunday or send a hundred pull requests — you're helping build free tools for churches everywhere. Welcome to the workbench."},
 "no":{"title":"Bygg med oss — åpen kildekode-verktøy for kirka | Sunday Suite",
   "desc":"Sunday Suite er en åpen kildekode-familie av kirkeverktøy — ærlig uferdig. Prøv betaene, les koden på GitHub, og bli med og bygg tolv verktøy for menighetene i Norden — og videre.",
   "crumb":"Bygg med oss","kicker":"Åpen kildekode","h1":"Bygg en bedre søndag med oss.",
   "tagline":"Åpen kildekode-verktøy for kirka — gratis, uferdige, og ærlige på begge deler.",
   "lead":"Sunday Suite er én utvikler i Norge som bygger tolv verktøy i det åpne, med dørene ulåst og lyset på. Koden bor på GitHub, betaene er gratis, og veikartet formes av menighetene som bruker dem. Denne siden er arbeidsbenken — trekk fram en stol.",
   "m_beta":"apper i beta i dag","m_code":"<b>Koden</b> — offentlig på GitHub","m_lic":"<b>MIT</b> — hvert repositorium",
   "act_gh":"Sunday Suite på GitHub","act_mail":"dev@sundaysuite.app",
   "hn_kicker":"Les dette først","hn_title":"Hva «uferdig» ærlig betyr",
   "hn_lead":"Vi vil heller love for lite på en nettside enn å skuffe deg på en søndag. Her er nøyaktig hvor langt hvert nivå har kommet:",
   "hn_feats":[("check","Beta","Det virker, og vi bruker det selv — men ha en reserveløsning de første søndagene, og regn med skarpe kanter. Feilrapporten din er gull verdt."),
     ("sliders","Under utvikling","Ekte kode, ekte framdrift, ikke klart for gudstjenesten din ennå. Følg med, eller hjelp det fram raskere."),
     ("doc","På tegnebrettet","En visjon og en arkitektur, ærlig talt fortsatt på papir. Beste tidspunkt å fortelle oss hva menigheten din trenger.")],
   "hn_note":"Appene sender ingenting hjem med mindre du takker ja til anonym telemetri — så når noe ryker, vet vi det som regel ikke. En e-post på to linjer om hva som gikk galt, er et ekte bidrag.",
   "bt_kicker":"Prøv betaene","bt_title":"Sju betaer, klare for prøvetur",
   "bt_lead":"Fem skrivebordsapper for Mac og Windows, to web-apper i nettleseren — alt gratis, ingen konto for nedlastingene. Knappene henter alltid nyeste utgivelse.",
   "bt_ring":"Ferskt fra beta-ringen:","bt_more":"Les mer",
   "code_kicker":"Koden","code_title":"Hvert repositorium, åpent på GitHub",
   "code_lead":"Alt sammen er MIT-lisensiert: les den, lær av den, kjør den, fork den. Hvert repositorium har en CONTRIBUTING-guide som får deg i gang. Det eneste lisensen ikke gir fra seg, er merkevaren — fork gjerne koden, men gi forken ditt eget navn.",
   "lic_pending":"lisens på vei",
   "ways_kicker":"Måter å hjelpe på","ways_title":"Seks måter å bygge med oss",
   "ways_lead":"Du trenger ikke være utvikler — de mest verdifulle bidragene kommer ofte fra dem som styrer projektoren på søndag.",
   "ways":[("check","Test &amp; rapporter","Bruk en beta til noe ekte og fortell oss hva som røyk — i en GitHub-issue eller en helt vanlig e-post. Dette er bidraget vi trenger mest."),
     ("code","Skriv kode","Rust, TypeScript, Svelte, Preact — velg et repo, åpne en issue for å si hei, og send en pull request."),
     ("globe","Oversett","Bokmål og nynorsk er førsteklasses her, og flere språk er velkomne — oversettelsesfiler er vennlig terreng for et første bidrag."),
     ("sparkle","Design","Ikoner, layouter, følelsen av en skjerm i en mørk kirke — har du øyet, har suiten lerretet."),
     ("text","Forbedre guidene","Hjelpeseksjonen er skrevet for frivillige, ikke utviklere. Forvirret en guide deg, er det en feil — si fra eller skriv den om."),
     ("star","Fortell oss hva du trenger","Veikartet formes av ekte menigheter. To setninger om søndagsmorgenen din kan endre hva som bygges videre.")],
   "how_head":"Slik jobber vi",
   "how_p":"Feil og idéer går i en GitHub-issue på det aktuelle repoet, eller til <a href=\"mailto:dev@sundaysuite.app\">dev@sundaysuite.app</a> om GitHub ikke er din greie. Hvert repositorium har en CONTRIBUTING-guide med detaljene. Det finnes ingen billettrobot og ikke noe kundesenter — hver melding lander hos den som skrev koden, og alle får svar.",
   "cta_h":"Én gylden tråd. Mange hender.","cta_p":"Enten du tester én beta én søndag eller sender hundre pull requests — du er med og bygger gratis verktøy for menigheter overalt. Velkommen til arbeidsbenken."},
}

def render_build_page(lang):
    c=CH[lang]; p=BUILDPAGE[lang]
    root="" if lang=="en" else "../"; L=links(lang,root)
    other = "no/bygg.html" if lang=="en" else "../build.html"
    nbeta = sum(1 for s in SLUGS if STATUS[s]=="beta")
    meta = f'<div><b>{nbeta}</b> {p["m_beta"]}</div><div>{p["m_code"]}</div><div>{p["m_lic"]}</div>'
    # beta cards — generated from STATUS/APP/APPDATA so the list can never go stale
    cards=""
    for i,s in enumerate([x for x in SLUGS if STATUS[x]=="beta"]):
        cd=CARD[s]; tag=cd[lang][0]
        a=APP.get(s) or APPDATA[s]
        if a.get("repo"):
            act=(f'<a href="/download/{s}/mac">Mac</a> · <a href="/download/{s}/windows">Windows</a> · '
                 f'<a href="https://github.com/{a["repo"]}" target="_blank" rel="noopener">GitHub</a>')
            if s in RING_APPS:
                act+=(f'<br><span class="dl-ring">{p["bt_ring"]} '
                      f'<a href="/download/{s}/mac?channel=beta">Mac</a> · '
                      f'<a href="/download/{s}/windows?channel=beta">Windows</a></span>')
        else:
            sub=a["url"].replace("https://","")
            act=f'<a href="{a["url"]}" target="_blank" rel="noopener">{("Open " if lang=="en" else "Åpne ")}{sub}</a>'
        cards+=(f'      <div class="card reveal" data-d="{(i%3)+1}" style="--c:var(--{cd["accent"]})">'
          f'<div class="card-top"><img class="logo-tile" src="{L["assets"]}logos/{s}.svg" alt="{PNAME[s]} logo" width="52" height="52" loading="lazy" />{status_badge("beta",c)}</div>'
          f'<h3><span class="sunday">Sunday</span>{PNAME[s][6:]}</h3><div class="tag">{tag}</div>'
          f'<p class="dl-links">{act}</p>'
          f'<a class="more" href="{L["app"](s)}">{p["bt_more"]}{sv("arrow","2.5")}</a></div>\n')
    repos="".join(
        f'      <a class="repo-row reveal" href="https://github.com/{r["repo"]}" target="_blank" rel="noopener">'
        f'<span class="repo-name">{r["name"]}</span><span class="repo-desc">{r[lang]}</span>'
        f'<span class="repo-lic{"" if r["lic"] else " pending"}">{r["lic"] or p["lic_pending"]}</span></a>\n'
        for r in REPOS)
    hn="".join(f'        <div class="feat reveal"><div class="fi">{sv(ik)}</div><h3>{t}</h3><p>{d}</p></div>\n' for ik,t,d in p["hn_feats"])
    ways="".join(f'        <div class="feat reveal"{" data-d=%d"%(i%3) if i%3 else ""}><div class="fi">{sv(ik)}</div><h3>{t}</h3><p>{d}</p></div>\n' for i,(ik,t,d) in enumerate(p["ways"]))
    content=(f'''<main>
<section class="app-hero"><div class="grain"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><span>{p["crumb"]}</span></div>
  <div class="app-hero-inner">
    <div class="section-kicker" style="color:var(--gold)">{p["kicker"]}</div>
    <h1 class="app-title" style="margin-top:14px">{p["h1"]}</h1>
    <div class="app-tagline">{p["tagline"]}</div>
    <p class="app-lead">{p["lead"]}</p>
    <div class="hero-meta" style="margin-top:34px; justify-content:flex-start">{meta}</div>
    <div class="app-hero-actions"><a href="{GITHUB_ORG}" target="_blank" rel="noopener" class="btn btn-primary">{p["act_gh"]}</a><a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">{p["act_mail"]}</a></div>
  </div>
</div></section>

<div class="app-body">
  <section class="app-section"><div class="wrap">
    <div class="section-head"><div class="section-kicker kicker-c">{p["hn_kicker"]}</div><h2 class="section-title">{p["hn_title"]}</h2><p class="section-lead">{p["hn_lead"]}</p></div>
    <div class="feat-grid">
{hn}    </div>
    <div class="callout reveal" style="margin:40px auto 0"><p>{p["hn_note"]}</p></div>
  </div></section>

  <section class="app-section alt" id="betas"><div class="wrap">
    <div class="section-head"><div class="section-kicker kicker-c">{p["bt_kicker"]}</div><h2 class="section-title">{p["bt_title"]}</h2><p class="section-lead">{p["bt_lead"]}</p></div>
    <div class="grid">
{cards}    </div>
  </div></section>

  <section class="app-section" id="code"><div class="wrap">
    <div class="section-head"><div class="section-kicker kicker-c">{p["code_kicker"]}</div><h2 class="section-title">{p["code_title"]}</h2><p class="section-lead">{p["code_lead"]}</p></div>
    <div class="repo-list reveal">
{repos}    </div>
  </div></section>

  <section class="app-section alt" id="ways"><div class="wrap">
    <div class="section-head"><div class="section-kicker kicker-c">{p["ways_kicker"]}</div><h2 class="section-title">{p["ways_title"]}</h2><p class="section-lead">{p["ways_lead"]}</p></div>
    <div class="feat-grid">
{ways}    </div>
    <div class="callout reveal" style="margin:40px auto 0"><h4>{p["how_head"]}</h4><p>{p["how_p"]}</p></div>
  </div></section>
</div>

<section class="app-cta"><div class="wrap">
  <h2>{p["cta_h"]}</h2><p>{p["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="{GITHUB_ORG}" target="_blank" rel="noopener" class="btn btn-primary">{p["act_gh"]}</a><a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">{p["act_mail"]}</a></div>
</div></section>
</main>''')
    return shell(c,L,other,p["title"],p["desc"],' style="--c:var(--gold-deep)"',content,pair=("build.html","no/bygg.html"))

def render_home(lang):
    c=CH[lang]; h=HOME[lang]; root="" if lang=="en" else "../"; L=links(lang,root)
    other = "no/index.html" if lang=="en" else "../index.html"
    arrow = sv("arrow","2.5")
    readmore = "Read more" if lang=="en" else "Les mer"
    def product_card(s, i):
        cd=CARD[s]; tag,desc,feats=cd[lang]; d=f' data-d="{(i%3)+1}"' if i%3 else f' data-d="1"'
        feats_html="".join(f"<li>{x}</li>" for x in feats)
        dev=" dev" if STATUS[s] in ("build","early") else ""
        return (f'      <a class="card link reveal{dev}"{d} style="--c:var(--{cd["accent"]})" href="{L["app"](s)}">'
          f'<span class="glowdot"></span><div class="card-top"><img class="logo-tile" src="{L["assets"]}logos/{s}.svg" alt="{PNAME[s]} logo" width="52" height="52" loading="lazy" />'
          f'{status_badge(STATUS[s],c)}</div>'
          f'<h3><span class="sunday">Sunday</span>{PNAME[s][6:]}</h3><div class="tag">{tag}</div>'
          f'<p>{desc}</p><ul class="feats">{feats_html}</ul>'
          f'<span class="more">{readmore}{arrow}</span></a>\n')
    def mini_card(s, i):
        cd=CARD[s]; tag,desc,feats=cd[lang]; d=f' data-d="{(i%3)+1}"' if i%3 else f' data-d="1"'
        return (f'      <a class="card mini link reveal dev"{d} style="--c:var(--{cd["accent"]})" href="{L["app"](s)}">'
          f'<img class="logo-tile" src="{L["assets"]}logos/{s}.svg" alt="{PNAME[s]} logo" width="40" height="40" loading="lazy" />'
          f'<span class="mini-body"><h3><span class="sunday">Sunday</span>{PNAME[s][6:]}</h3><span class="tag">{tag}</span></span>'
          f'{status_badge(STATUS[s],c)}</a>\n')
    def grid_label(txt):
        return f'<div class="grid-label reveal"><span class="line"></span><h3>{txt}</h3><span class="line"></span></div>'
    avail=[s for s in SLUGS if STATUS[s]=="beta"]
    indev=[s for s in SLUGS if STATUS[s]=="build"]
    early=[s for s in SLUGS if STATUS[s]=="early"]
    cards_avail="".join(product_card(s,i) for i,s in enumerate(avail))
    cards_early="".join(mini_card(s,i) for i,s in enumerate(early))
    cards="".join(product_card(s,i) for i,s in enumerate(indev))
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
  {grid_label(h["grp_now"])}
  <div class="grid">
{cards_avail}  </div>
  {grid_label(h["grp_dev"])}
  <div class="grid">
{cards}  </div>
  {grid_label(h["grp_early"])}
  <div class="grid">
{cards_early}  </div>
</div></section>

<section class="philo" id="philosophy"><div class="glow"></div><div class="wrap philo-grid">
  <div class="reveal"><div class="section-kicker" style="color:var(--gold)">{h["p_kicker"]}</div><h2>{h["p_h2"]}</h2><p class="lead">{h["p_lead"]}</p></div>
  <div class="moat reveal" data-d="1">{moat}</div>
</div></section>

<section class="magic" id="together"><div class="wrap">
  <div class="section-head reveal"><div class="section-kicker">{h["mg_kicker"]}</div><h2 class="section-title">{h["mg_title"]}</h2><p class="section-lead">{h["mg_lead"]}</p></div>
  <div class="chips reveal" data-d="1">{chips}</div>
</div></section>

<section class="cta" id="opensource"><div class="glow"></div><div class="wrap cta-inner reveal">
  <div class="section-kicker" style="color:var(--gold)">{h["os_kicker"]}</div>
  <h2>{h["os_h"]}</h2><p>{h["os_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="{L["build"]}" class="btn btn-primary">{h["os_btn"]}</a><a href="{GITHUB_ORG}" target="_blank" rel="noopener" class="btn btn-ghost">{h["os_gh"]}</a></div>
</div></section>

{render_toolbox(lang, h, c, L)}

<section class="cta"><div class="glow"></div><div class="wrap cta-inner reveal">
  <svg class="bigcross cross" viewBox="0 0 20 26"><path d="M8 0h4v8h8v4h-8v14H8V12H0V8h8z"/></svg>
  <h2>{h["cta_h"]}</h2><p>{h["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center"><a href="mailto:dev@sundaysuite.app" class="btn btn-primary">dev@sundaysuite.app</a><a href="#products" class="btn btn-ghost">{h["cta_back"]}</a></div>
</div></section>
</main>''')
    return shell(c,L,other,h["title"],h["desc"]," id=\"top\"".replace(' id="top"',''),content,pair=("index.html","no/index.html"))

# ===================================================================== APPS
APP = {
 "sundayrec":{"accent":"rec","icon":"rec","short":"Rec","repo":"SundaySuite-app/sundayrec",
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
    "checks":["No ads, no tracking — optional anonymous quality telemetry, off by default","Backed by over 1000 automated tests","Seven languages, including Norwegian Bokmål and Nynorsk"],
    "status":"SundayRec is the mature core of the suite and can be downloaded and used for free today, but it's still in beta. Test your first recordings before relying on it for a critical service. This page on sundaysuite.app is SundayRec's home — there's no separate site to visit, and the download buttons here always fetch the latest release.",
    "install_head":"Download &amp; install notes",
    "install_mac":"<strong>Mac:</strong> Apple Silicon (M1 or newer) only for now — there is no Intel build; get in touch if you need one. The app is signed but not yet notarized, so the very first launch is <em>right-click the app → Open</em>.",
    "install_win":"<strong>Windows:</strong> the installer can trigger a SmartScreen notice the first time — choose <em>More info → Run anyway</em>.",
    "install_all":"All versions &amp; release notes on GitHub",
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
    "checks":["Ingen reklame, ingen sporing — valgfri anonym kvalitetstelemetri, av som standard","Over 1000 automatiske tester i ryggen","Sju språk, inkludert bokmål og nynorsk"],
    "status":"SundayRec er den modne kjernen i suiten og kan lastes ned og brukes gratis i dag, men er fortsatt i beta. Test gjerne de første opptakene før du stoler på den til en kritisk gudstjeneste. Denne siden på sundaysuite.app er hjemmebasen til SundayRec — det finnes ingen egen nettside å besøke, og nedlastingsknappene her henter alltid nyeste utgivelse.",
    "install_head":"Nedlasting &amp; installasjon",
    "install_mac":"<strong>Mac:</strong> foreløpig kun Apple Silicon (M1 eller nyere) — det finnes ingen Intel-build; ta kontakt om du trenger en. Appen er signert, men ennå ikke notarisert, så aller første start er <em>høyreklikk på appen → Åpne</em>.",
    "install_win":"<strong>Windows:</strong> installasjonen kan utløse et SmartScreen-varsel første gang — velg <em>Mer info → Kjør likevel</em>.",
    "install_all":"Alle versjoner &amp; utgivelsesnotater på GitHub",
    "cta_h":"Klar til å ta opp neste søndag?","cta_p":"Last ned SundayRec gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil følge utviklingen."},
  "chips":[("Stage","Rec","cue→chapter / cue blir kapittelmerke"),("Stage","Rec","lyrics→SRT / sangtekst blir SRT"),("Rec","Plan","transcript / transkripsjon"),("Rec","Edit","sermon ready / preken klar"),("Rec","Paper","sermon→magazine / preken→blad")],
 },
 "sundayscreen":{"accent":"screen","icon":"clock","short":"Screen","repo":"SundaySuite-app/sundayscreen",
  "en":{"tagline":"The classroom screen that never needs the internet.",
    "meta":"SundayScreen puts clock, timer, name picker, group maker, dice and traffic light on the projector — fully offline. Free desktop beta for Mac and Windows.",
    "lead":"Plan the lesson by designing the screen it will show. Pick a period in the planner, press <em>Design the screen</em>, and build exactly what the class will see — a clock, a big countdown, today's message, a traffic light, a name picker, groups, dice, a link with a QR code and images — while the board on the wall carries on untouched. Everything runs on your own machine: no account, no cloud, and no internet needed. Free desktop app for Mac and Windows.",
    "what":"The planner where the screen is the plan","whatlead":"Design each lesson in a miniature of the real editor, then drag, resize and arrange the tools right on the display surface.",
    "features":[("calendar","Lesson planner","Pick a period and design its screen in a miniature of the real editor, while the board on the wall carries on untouched. Merge two periods into a double lesson when you need one — the timer's “rest of the lesson” then carries through the break."),
      ("clock","Clock &amp; timer","A digital or analog clock, a countdown with huge digits and a gentle chime, and a stopwatch. The timer keeps perfect time even if the machine sleeps."),
      ("people","Name picker &amp; groups","Draw a random pupil — with no repeats until everyone has had a turn — and split the class into fair groups in one click."),
      ("focus","Traffic light, symbols &amp; dice","Show how to work right now: silence, whisper, collaborate or hands up — plus one to three animated dice and big messages in beautiful type."),
      ("globe","Link, QR &amp; images","Put a link on the screen with a QR code the class can scan from their desks, and show the class photo or a map. Images travel with the layout when you move it to another machine."),
      ("stack","Class profiles","Every class keeps its own name list, its own lessons and its own screen layout — and each screen can have its own background colour. Switch class in two clicks.")],
    "hl_kicker":"Built for the classroom","hl_title":"Local first. Pupil names never leave the machine.",
    "hl_p":"SundayScreen is a desktop app, not a web service. There is nothing to sign into and nothing is uploaded — the school network can be down all day and the screen won't care. If the machine restarts mid-lesson, the app brings back exactly the screen you had: the drawn name, the light colour, the dice.",
    "checks":["No account, no telemetry — pupil data stays on the machine","A restart mid-lesson restores the screen exactly","Free and open source (MIT)"],
    "status":"SundayScreen is out in beta and free to download and use today. The newest build turns it into a planner: design each lesson's screen ahead of time, merge two periods into a double lesson, and put a link with a QR code or an image on the wall. It grew out of a teacher's own classroom, as part of the Sunday Suite family — this page is its home, and the download buttons always fetch the latest release.",
    "install_head":"Download &amp; install notes",
    "install_mac":"<strong>Mac:</strong> Apple Silicon (M1 or newer) only for now. The beta is not yet signed with an Apple developer certificate, so the very first launch is <em>right-click the app &rarr; Open</em>.",
    "install_win":"<strong>Windows:</strong> the installer can trigger a SmartScreen notice the first time — choose <em>More info &rarr; Run anyway</em>.",
    "install_all":"All versions &amp; release notes on GitHub",
    "cta_h":"Ready for Monday morning?","cta_p":"Download SundayScreen free for Mac and Windows — no account needed — or get in touch to follow development."},
  "no":{"tagline":"Klasseromsskjermen som aldri trenger nett.",
    "meta":"SundayScreen legger klokke, timer, navnetrekker, gruppegenerator, terning og trafikklys på projektoren — helt offline. Gratis skrivebords-beta for Mac og Windows.",
    "lead":"Planlegg timen ved å designe skjermen den skal vise. Velg en time i planleggeren, trykk <em>Design skjermen</em>, og bygg nøyaktig det klassen skal se — klokke, stor nedtelling, dagens beskjed, trafikklys, navnetrekker, grupper, terning, lenke med QR-kode og bilder — mens tavla på veggen står urørt. Alt kjører på din egen maskin: ingen konto, ingen sky, og ikke noe behov for nett. Gratis skrivebordsapp for Mac og Windows.",
    "what":"Planleggeren der skjermen er planen","whatlead":"Design hver time i en miniatyr av den ekte editoren, og dra, skaler og ordne verktøyene rett på visningsflaten.",
    "features":[("calendar","Timeplanlegger","Velg en time og design skjermen dens i en miniatyr av den ekte editoren, mens tavla på veggen står urørt. Slå sammen to timer til en dobbelttime når du trenger det — tidtakerens «resten av timen» holder da gjennom friminuttet."),
      ("clock","Klokke &amp; timer","Digital eller analog klokke, nedtelling med digre sifre og et mildt lydvarsel, og stoppeklokke. Timeren holder perfekt tid selv om maskinen sover."),
      ("people","Navnetrekker &amp; grupper","Trekk en tilfeldig elev — uten gjentak før alle har hatt sin tur — og del klassen i rettferdige grupper med ett klikk."),
      ("focus","Trafikklys, symboler &amp; terning","Vis hvordan det jobbes akkurat nå: stille, hviske, samarbeide eller rekk opp hånda — pluss én til tre animerte terninger og store beskjeder i vakker typografi."),
      ("globe","Lenke, QR &amp; bilder","Legg en lenke på skjermen med QR-kode klassen kan skanne fra pultene, og vis klassebildet eller et kart. Bildene blir med når du flytter oppsettet til en annen maskin."),
      ("stack","Klasseprofiler","Hver klasse har sin egen navneliste, sine egne timer og sitt eget skjermoppsett — og hver skjerm kan få sin egen bakgrunnsfarge. Bytt klasse med to klikk.")],
    "hl_kicker":"Bygd for klasserommet","hl_title":"Lokalt først. Elevnavn forlater aldri maskinen.",
    "hl_p":"SundayScreen er en skrivebordsapp, ikke en nettjeneste. Det finnes ingenting å logge inn på, og ingenting lastes opp — skolenettet kan ligge nede hele dagen uten at skjermen bryr seg. Starter maskinen på nytt midt i timen, henter appen tilbake nøyaktig skjermen du hadde: det trukne navnet, lysfargen, terningkastet.",
    "checks":["Ingen konto, ingen telemetri — elevdata blir på maskinen","Restart midt i timen gjenoppretter skjermen eksakt","Gratis og åpen kildekode (MIT)"],
    "status":"SundayScreen er ute i beta og kan lastes ned og brukes gratis i dag. Nyeste utgave gjør den til en planlegger: design skjermen for hver time på forhånd, slå sammen to timer til en dobbelttime, og legg en lenke med QR-kode eller et bilde på veggen. Appen har vokst ut av en lærers eget klasserom, som en del av Sunday Suite-familien — denne siden er hjemmebasen, og nedlastingsknappene henter alltid nyeste utgivelse.",
    "install_head":"Nedlasting &amp; installasjon",
    "install_mac":"<strong>Mac:</strong> foreløpig kun Apple Silicon (M1 eller nyere). Betaen er ennå ikke signert med Apple-utviklersertifikat, så aller første start er <em>høyreklikk på appen &rarr; Åpne</em>.",
    "install_win":"<strong>Windows:</strong> installasjonen kan utløse et SmartScreen-varsel første gang — velg <em>Mer info &rarr; Kjør likevel</em>.",
    "install_all":"Alle versjoner &amp; utgivelsesnotater på GitHub",
    "cta_h":"Klar til mandag morgen?","cta_p":"Last ned SundayScreen gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil følge utviklingen."},
  "chips":None,
 },
 "sundaysync":{"accent":"sync","icon":"sync","short":"Sync","repo":"SundaySuite-app/sundaysync",
  "en":{"tagline":"Every camera, one timeline.",
    "meta":"SundaySync aligns every camera and recorder from the service by their audio and exports one synchronized FCPXML timeline for DaVinci Resolve. Free beta for Mac and Windows.",
    "lead":"Drop in every file from the service — phones, handycams, the audio recorder on the pulpit — and SundaySync lines them all up by listening to the audio itself. No timecode, no clapperboard. Out comes one synchronized multicam timeline as FCPXML, ready to open in DaVinci Resolve. Free desktop app for Mac and Windows, fully local.",
    "what":"From memory cards to a cut-ready timeline","whatlead":"Drop everything in, press sync, open Resolve.",
    "features":[("wave","Audio waveform sync","Every clip is aligned by cross-correlating its audio — sample-accurate, with no clapperboard or timecode needed."),
      ("layers","Every source, one timeline","Cameras, phones and audio recorders all land in one synchronized multicam timeline."),
      ("code","FCPXML for Resolve","Export an FCPXML and open it straight in DaVinci Resolve — angles named, clips placed."),
      ("bolt","ffmpeg built in","The media engine ships inside the app — nothing else to install, and a first-launch self-test proves it works."),
      ("search","Listen before you export","Play the synchronized sources together in the app and hear that everything lines up."),
      ("shield","Fully local","Your footage never leaves the machine. No account, no cloud, no upload.")],
    "hl_kicker":"Built for church shoots","hl_title":"No timecode? No problem. The audio is the clock.",
    "hl_p":"A multicam rig in a church is rarely broadcast gear — it's phones, handycams and a recorder on the pulpit, and nothing shares timecode. SundaySync listens to what every device heard and aligns them to within a few samples, the way a patient editor would by hand — in seconds.",
    "checks":["Sample-accurate alignment, verified against DaVinci Resolve","Bundled ffmpeg — works on a clean machine","Free and fully local — nothing is uploaded"],
    "status":"SundaySync is out in beta on the suite's beta ring and free to download today. Sync your first service before relying on it for a deadline — and tell us how it went.",
    "install_head":"Download &amp; install notes",
    "install_mac":"<strong>Mac:</strong> Apple Silicon (M1 or newer) only for now — there is no Intel build; get in touch if you need one. The app is signed but not yet notarized, so the very first launch is <em>right-click the app &rarr; Open</em>.",
    "install_win":"<strong>Windows:</strong> the installer can trigger a SmartScreen notice the first time — choose <em>More info &rarr; Run anyway</em>.",
    "install_all":"All versions &amp; release notes on GitHub",
    "cta_h":"Ready to cut this week's service?","cta_p":"Download SundaySync free for Mac and Windows — no account needed — or get in touch to follow development."},
  "no":{"tagline":"Hvert kamera, én tidslinje.",
    "meta":"SundaySync justerer alle kameraer og opptakere fra gudstjenesten etter lyden og eksporterer én synkronisert FCPXML-tidslinje for DaVinci Resolve. Gratis beta for Mac og Windows.",
    "lead":"Slipp inn alle filene fra gudstjenesten — mobiler, handycam-er, lydopptakeren på talerstolen — og SundaySync legger dem kant i kant ved å lytte til selve lyden. Ingen timekode, ingen klapper. Ut kommer én synkronisert multikam-tidslinje som FCPXML, klar til å åpnes i DaVinci Resolve. Gratis skrivebordsapp for Mac og Windows, helt lokal.",
    "what":"Fra minnekort til klippeklar tidslinje","whatlead":"Slipp alt inn, trykk synk, åpne Resolve.",
    "features":[("wave","Lydbølge-synk","Hvert klipp justeres ved å krysskorrelere lyden — sample-nøyaktig, uten klapper eller timekode."),
      ("layers","Alle kilder, én tidslinje","Kameraer, mobiler og lydopptakere lander i én synkronisert multikam-tidslinje."),
      ("code","FCPXML for Resolve","Eksporter en FCPXML og åpne den rett i DaVinci Resolve — vinkler navngitt, klipp plassert."),
      ("bolt","ffmpeg innebygd","Mediemotoren følger med inne i appen — ingenting annet å installere, og en selvtest ved første start beviser at den virker."),
      ("search","Lytt før du eksporterer","Spill de synkroniserte kildene sammen i appen og hør at alt ligger kant i kant."),
      ("shield","Helt lokalt","Opptakene dine forlater aldri maskinen. Ingen konto, ingen sky, ingen opplasting.")],
    "hl_kicker":"Bygd for kirkeopptak","hl_title":"Ingen timekode? Ikke noe problem. Lyden er klokka.",
    "hl_p":"En multikam-rigg i en kirke er sjelden kringkastingsutstyr — det er mobiler, handycam-er og en opptaker på talerstolen, og ingenting deler timekode. SundaySync lytter til hva hver enhet hørte og justerer dem til innenfor noen få samples, slik en tålmodig klipper ville gjort for hånd — på sekunder.",
    "checks":["Sample-nøyaktig justering, verifisert mot DaVinci Resolve","Bundlet ffmpeg — virker på en ren maskin","Gratis og helt lokal — ingenting lastes opp"],
    "status":"SundaySync er ute i beta på suitens beta-ring og gratis å laste ned i dag. Synk din første gudstjeneste før du stoler på den mot en deadline — og fortell oss hvordan det gikk.",
    "install_head":"Nedlasting &amp; installasjon",
    "install_mac":"<strong>Mac:</strong> foreløpig kun Apple Silicon (M1 eller nyere) — det finnes ingen Intel-build; ta kontakt om du trenger en. Appen er signert, men ennå ikke notarisert, så aller første start er <em>høyreklikk på appen &rarr; Åpne</em>.",
    "install_win":"<strong>Windows:</strong> installasjonen kan utløse et SmartScreen-varsel første gang — velg <em>Mer info &rarr; Kjør likevel</em>.",
    "install_all":"Alle versjoner &amp; utgivelsesnotater på GitHub",
    "cta_h":"Klar til å klippe ukas gudstjeneste?","cta_p":"Last ned SundaySync gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil følge utviklingen."},
  "chips":[("Rec","Sync","recordings become a timeline / opptak blir tidslinje"),("Sync","Edit","synced sermon ready for captions / synket preken klar for teksting")],
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
 "sundaystage":{"accent":"stage","icon":"screen","short":"Stage","repo":"SundaySuite-app/sundaystage",
  "en":{"tagline":"Lyrics and media on the big screen.",
    "meta":"SundayStage shows lyrics, Bible verses and media on the big screen behind the altar — a Nordic alternative to ProPresenter, with cue control and safe, isolated output.",
    "lead":"Show lyrics, Bible verses, announcements and media on the screen behind the altar. A modern presentation tool in the ProPresenter class, built for Nordic churches, with cue control, seamless transitions and a live engine with an isolated output process for safe display.",
    "what":"Everything on screen, safely controlled","whatlead":"Made to hold up when it matters — in the middle of the service.",
    "features":[("text","Lyrics &amp; verses","Show text line by line with fast transitions and clean typography on the big screen."),
      ("layers","Cues and order","Build the order for the whole service in advance and run it with a single keypress."),
      ("screen","Media &amp; backgrounds","Images, video and backgrounds with soft transitions between elements."),
      ("shield","Output lock &amp; blackout","Freeze what the congregation sees with ⌘L — clicks, jumps, messages and the network remote are all refused until you unlock. Blackout is ⇧B, and it always gets through: an emergency stop outranks a lock."),
      ("bolt","⌘K palette &amp; section jump","Find and show anything in seconds, or type <code>R</code> when the band takes the chorus again. The letters come from the song itself, in your language — and full-text search brings up the right song instantly."),
      ("star","Song usage log","Every song that actually reached the congregation screen is logged by itself, with CCLI number, TONO id, copyright and author copied into the row. Export a CSV for the period you need to report.")],
    "hl_kicker":"Built for live","hl_title":"Confident on the big screen when it counts.",
    "hl_p":"Nothing is worse than a black screen in the middle of worship. SundayStage isolates the display in its own process, so the app can fail without the congregation noticing.",
    "checks":["Isolated output process protects the display","An emergency stop always outranks the output lock","The song log records what actually reached the screen — not what was planned"],
    "status":"SundayStage is out in beta and free to download today. The buttons above give you the stable build; the newest work — the output lock, blackout moving from Escape to ⇧B, section jump and the TONO/CCLI song usage log — is fresh on the beta ring, which you can pick up from the <a href=\"/build#betas\">Build with us</a> page. The slide editor is still growing. Try it on a rehearsal night before you trust it with a service — and tell us what breaks.",
    "install_head":"Download &amp; install notes",
    "install_mac":"<strong>Mac:</strong> Apple Silicon (M1 or newer) only for now — there is no Intel build; get in touch if you need one. The app is signed but not yet notarized, so the very first launch is <em>right-click the app &rarr; Open</em>.",
    "install_win":"<strong>Windows:</strong> the installer can trigger a SmartScreen notice the first time — choose <em>More info &rarr; Run anyway</em>.",
    "install_all":"All versions &amp; release notes on GitHub",
    "cta_h":"Ready to try Stage on the big screen?","cta_p":"Download SundayStage free for Mac and Windows — no account needed — or get in touch to help shape the presentation tool."},
  "no":{"tagline":"Sangtekster og media på storskjerm.",
    "meta":"SundayStage viser sangtekster, bibelvers og media på storskjerm bak alteret — et nordisk alternativ til ProPresenter, med køstyring og trygg, isolert visning.",
    "lead":"Vis sangtekster, bibelvers, kunngjøringer og media på skjermen bak alteret. Et moderne presentasjonsverktøy i ProPresenter-klassen, bygd for nordiske menigheter, med køstyring, sømløse overganger og en live-motor med isolert utgangsprosess for trygg visning.",
    "what":"Alt på skjermen, trygt styrt","whatlead":"Laget for å stå imot når det gjelder — midt i gudstjenesten.",
    "features":[("text","Sangtekster &amp; vers","Vis tekst vers for vers med raske overganger og ren typografi på storskjerm."),
      ("layers","Køer og rekkefølge","Bygg rekkefølgen for hele gudstjenesten på forhånd og styr den med ett tastetrykk."),
      ("screen","Media &amp; bakgrunner","Bilder, video og bakgrunner med myke overganger mellom elementene."),
      ("shield","Output-lås &amp; blackout","Frys det menigheten ser med ⌘L — klikk, hopp, meldinger og nettverksfjernkontrollen blir alle avvist til du låser opp. Blackout er ⇧B, og den slipper alltid gjennom: en nødstopp rangerer over en lås."),
      ("bolt","⌘K-palett &amp; seksjonshopp","Finn og vis hva som helst på sekunder, eller skriv <code>R</code> når bandet tar refrenget igjen. Bokstavene kommer fra sangen selv, på ditt språk — og fulltekstsøket henter fram riktig sang umiddelbart."),
      ("star","Sangbrukslogg","Hver sang som faktisk nådde menighetsskjermen loggføres av seg selv, med CCLI-nummer, TONO-ID, copyright og opphavsperson kopiert inn i raden. Eksporter en CSV for perioden du skal rapportere.")],
    "hl_kicker":"Bygd for live","hl_title":"Trygg på storskjerm når det gjelder.",
    "hl_p":"Ingenting er verre enn en svart skjerm midt i lovsangen. SundayStage isolerer visningen i en egen prosess, slik at appen kan feile uten at menigheten merker det.",
    "checks":["Isolert utgangsprosess beskytter visningen","En nødstopp rangerer alltid over output-låsen","Loggen fører det som faktisk nådde skjermen — ikke det som lå i planen"],
    "status":"SundayStage er ute i beta og gratis å laste ned i dag. Knappene over gir deg stable-utgaven; det nyeste — output-låsen, blackout flyttet fra Escape til ⇧B, seksjonshopp og sangbruksloggen for TONO og CCLI — er ferskt på beta-ringen, som du finner på <a href=\"/no/bygg#betas\">Bygg med oss</a>-siden. Slide-editoren vokser fortsatt. Prøv den på en øvingskveld før du stoler på den i en gudstjeneste — og fortell oss hva som ryker.",
    "install_head":"Nedlasting &amp; installasjon",
    "install_mac":"<strong>Mac:</strong> foreløpig kun Apple Silicon (M1 eller nyere) — det finnes ingen Intel-build; ta kontakt om du trenger en. Appen er signert, men ennå ikke notarisert, så aller første start er <em>høyreklikk på appen &rarr; Åpne</em>.",
    "install_win":"<strong>Windows:</strong> installasjonen kan utløse et SmartScreen-varsel første gang — velg <em>Mer info &rarr; Kjør likevel</em>.",
    "install_all":"Alle versjoner &amp; utgivelsesnotater på GitHub",
    "cta_h":"Klar til å prøve Stage på storskjermen?","cta_p":"Last ned SundayStage gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil forme presentasjonsverktøyet."},
  "chips":[("Stage","Rec","cue→chapter / cue blir kapittelmerke"),("Stage","Rec","lyrics→SRT / sangtekst blir SRT"),("Plan","Stage","setlist / setliste"),("Stage","Song","can log / kan loggføres")]},
 "sundayplan":{"accent":"plan","icon":"calendar","short":"Plan",
  "en":{"tagline":"Planning and volunteer rota, done in minutes.",
    "meta":"SundayPlan plans the service and schedules volunteers with a fair auto-fill engine — with TONO licence status as a first-class field.",
    "lead":"Plan the service and schedule volunteers without spreadsheets. A deterministic auto-fill engine balances skill, fair rotation, frequency, burnout and fixed pairs — with the church's TONO licence status as a first-class field from the start.",
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
    "meta":"SundayPlan planlegger gudstjenesten og setter opp de frivillige med en rettferdig auto-fyll-motor — med TONO-lisensstatus som førsteklasses felt.",
    "lead":"Planlegg gudstjenesten og sett opp de frivillige uten regneark. En deterministisk auto-fyll-motor balanserer kompetanse, rettferdig rotasjon, frekvens, utbrenthet og faste par — med menighetens TONO-lisensstatus som førsteklasses felt fra start.",
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
  "en":{"tagline":"A song database built for Nordic rights reality.",
    "meta":"SundaySong is a song database with semantic search, AI recommendations and TONO/CCLI as first-class fields in the data model — built for Nordic reality.",
    "lead":"Find the right song with semantic search and AI recommendations across languages — with TONO and CCLI built into the data model from the first row. Every song can carry a TONO id, and every use can record whether it was streamed (a separate royalty pool).",
    "what":"Search, suggest — with rights in the data model","whatlead":"The song catalog with rights identifiers as first-class data.",
    "features":[("search","Semantic search","Search by feeling and theme, not just title — powered by vector search with pgvector."),
      ("sparkle","AI recommendations","Get suggestions for songs that fit the text, theme and tone of the service."),
      ("star","TONO + CCLI","TONO and CCLI ids are first-class fields, so songs and uses carry the data a report would need."),
      ("bolt","Streaming flag","<code>was_streamed</code> separates in-room use from streamed use — a separate royalty pool."),
      ("globe","Multilingual","Canonical songs with variants and translations linked across languages."),
      ("code","Open API","A public SDK lets the other Sunday apps look up and log songs.")],
    "hl_kicker":"The moat","hl_title":"Built for TONO from the first row in the database.",
    "hl_p":"Most song tools are built around American CCLI. SundaySong has <code>tono_work_id</code> on every song and a streaming flag on every use from day one — that's the Nordic moat.",
    "checks":["tono_work_id on every song from day one","was_streamed flag on every use","Designed for Norwegian-labelled TONO reports alongside CCLI"],
    "status":"SundaySong is in early development. The data model and API contract with the TONO fields are in place, and the public SDK compiles against the contract; song import, search and AI are in progress. Not available for use yet.",
    "cta_h":"Want in on the TONO moat?","cta_p":"SundaySong is in development. Get in touch if your church or organization wants to follow the song database."},
  "no":{"tagline":"En sangdatabase bygd for nordisk rettighets-virkelighet.",
    "meta":"SundaySong er en sangdatabase med semantisk søk, AI-anbefalinger og TONO/CCLI som førsteklasses felt i datamodellen — bygd for norsk virkelighet.",
    "lead":"Finn riktig sang med semantisk søk og AI-anbefalinger på tvers av språk — med TONO og CCLI bygd inn i datamodellen fra første rad. Hver sang kan bære en TONO-ID, og hver bruk kan registrere om den ble strømmet (egen royalty-pott).",
    "what":"Søk, foreslå — med rettigheter i datamodellen","whatlead":"Sangkatalogen med rettighets-ID-er som førsteklasses data.",
    "features":[("search","Semantisk søk","Søk på følelse og tema, ikke bare tittel — drevet av vektorsøk med pgvector."),
      ("sparkle","AI-anbefalinger","Få forslag til sanger som passer tekst, tema og tone i gudstjenesten."),
      ("star","TONO + CCLI","TONO- og CCLI-ID-er er førsteklasses felt, så sanger og bruk bærer dataene en rapport vil trenge."),
      ("bolt","Strømme-flagg","<code>was_streamed</code> skiller bruk i rommet fra strømmet bruk — egen royalty-pott."),
      ("globe","Fleirspråk","Kanoniske sanger med varianter og oversettelser koblet på tvers av språk."),
      ("code","Åpent API","Et offentlig SDK lar de andre Sunday-appene slå opp og loggføre sanger.")],
    "hl_kicker":"Moaten","hl_title":"Bygd for TONO fra første rad i databasen.",
    "hl_p":"De fleste sangverktøy er bygd rundt amerikansk CCLI. SundaySong har <code>tono_work_id</code> på hver sang og et strømme-flagg på hver bruk fra dag én — det er den nordiske moaten.",
    "checks":["tono_work_id på hver sang fra dag én","was_streamed-flagg på hver bruk","Designet for norsk-merkede TONO-rapporter ved siden av CCLI"],
    "status":"SundaySong er i tidlig utvikling. Datamodellen og API-kontrakten med TONO-feltene er på plass, og det offentlige SDK-et kompilerer mot kontrakten; sangimport, søk og AI er under arbeid. Ikke ute for bruk ennå.",
    "cta_h":"Vil du være med på TONO-moaten?","cta_p":"SundaySong er under utvikling. Ta kontakt om menigheten eller organisasjonen din vil følge sangdatabasen."},
  "chips":[("Stage","Song","logged / loggføres"),("Plan","Song","licensing / lisens"),("Paper","Song","catalog / katalog"),("Rec","Song","streaming flag / strømme-flagg")]},
 "sundayedit":{"accent":"edit","icon":"caption","short":"Edit","repo":"SundaySuite-app/sundayedit",
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
    "status":"SundayEdit is out in beta and free to download today — the confidence editor, local Whisper transcription and export to SRT, VTT, ASS and TXT all work. A standalone product with its own brand, maturing in the open. Caption a real video and tell us where it stumbles.",
    "install_head":"Download &amp; install notes",
    "install_mac":"<strong>Mac:</strong> a universal build — works on both Apple Silicon and Intel Macs. The app is signed but not yet notarized, so the very first launch is <em>right-click the app &rarr; Open</em>.",
    "install_win":"<strong>Windows:</strong> the installer can trigger a SmartScreen notice the first time — choose <em>More info &rarr; Run anyway</em>.",
    "install_all":"All versions &amp; release notes on GitHub",
    "cta_h":"Want to caption faster?","cta_p":"Download SundayEdit free for Mac and Windows — no account needed — or get in touch to follow development."},
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
    "status":"SundayEdit er ute i beta og gratis å laste ned i dag — konfidens-editoren, lokal Whisper-transkripsjon og eksport til SRT, VTT, ASS og TXT virker. Et frittstående produkt med egen merkevare, som modnes i det åpne. Tekst en ekte video og fortell oss hvor den snubler.",
    "install_head":"Nedlasting &amp; installasjon",
    "install_mac":"<strong>Mac:</strong> universal-build — virker på både Apple Silicon og Intel. Appen er signert, men ennå ikke notarisert, så aller første start er <em>høyreklikk på appen &rarr; Åpne</em>.",
    "install_win":"<strong>Windows:</strong> installasjonen kan utløse et SmartScreen-varsel første gang — velg <em>Mer info &rarr; Kjør likevel</em>.",
    "install_all":"Alle versjoner &amp; utgivelsesnotater på GitHub",
    "cta_h":"Vil du tekste raskere?","cta_p":"Last ned SundayEdit gratis for Mac og Windows — ingen konto nødvendig — eller ta kontakt om du vil følge utviklingen."},
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
 "sundaytranslate":{"accent":"translate","icon":"globe","short":"Translate",
  "en":{"tagline":"The service, in every language — and every ear.",
    "meta":"SundayTranslate streams live interpretation and assistive listening to any phone in the pew — your own language, or louder and clearer, with no app to install.",
    "lead":"Walk into a service in a language you don't speak and hear it interpreted live in your earbuds, on your own phone. The same channel carries clean room audio for the hard of hearing — a hearing loop without the hardware. Fully web-based, anonymous, nothing to install.",
    "what":"One link, every listener","whatlead":"From the interpreter in the back room to the phone in the pew, in about a second.",
    "features":[("people","Live interpreter","An interpreter speaks into their phone; everyone who chose that language hears them, about a second behind."),
      ("wave","Assistive listening","The original room audio becomes an earbud channel for the hard of hearing — a hearing loop with no hardware in the floor."),
      ("caption","AI captions","Optional live subtitles in any language to read along on the phone — Whisper transcription and Claude translation."),
      ("globe","Any phone, any language","Listeners join with a six-digit code or a QR. No app, no account, anonymous — it just plays."),
      ("mic","AI voice","Where no human interpreter is on hand, the phone can even speak the translation itself (experimental)."),
      ("shield","Private by design","No audio is recorded and sessions expire after the service. The write secret never reaches a listener's phone.")],
    "hl_kicker":"Built for the pew","hl_title":"Everyone hears, in the language they think in.",
    "hl_p":"Newcomers, guests and the hard of hearing follow the whole service — without a translator at their side or a hearing loop in the floor. They just open a link.",
    "checks":["No install, no account — anonymous for listeners","Runs on the church's own Cloudflare and Supabase","No audio recorded; sessions self-expire"],
    "status":"SundayTranslate is code-complete across all three phases — live interpretation, assistive listening and AI captions — and will launch as a web app once the final on-device testing is done. Not available for use yet.",
    "cta_h":"Want SundayTranslate for your church?","cta_p":"SundayTranslate is in development. Get in touch if your congregation wants to be early with live translation and hearing help."},
  "no":{"tagline":"Gudstjenesten — på alle språk, og i hvert øre.",
    "meta":"SundayTranslate strømmer live tolking og lytteanlegg til hvilken som helst mobil i benken — på ditt eget språk, eller klarere og høyere, uten app å installere.",
    "lead":"Kom inn til en gudstjeneste på et språk du ikke forstår, og hør den tolket live i øreproppene, på din egen mobil. Den samme kanalen bærer ren romlyd for hørselshemmede — en teleslynge uten maskinvaren. Helt nettbasert, anonymt, ingenting å installere.",
    "what":"Én lenke, alle lyttere","whatlead":"Fra tolken i bakrommet til mobilen i benken på omtrent ett sekund.",
    "features":[("people","Live tolk","En tolk snakker inn i sin egen mobil; alle som valgte det språket hører hen, omtrent ett sekund bak."),
      ("wave","Lytteanlegg","Den originale romlyden blir en øreproppkanal for hørselshemmede — en teleslynge uten maskinvare i gulvet."),
      ("caption","AI-undertekster","Valgfrie live-undertekster på hvilket som helst språk å lese på mobilen — Whisper-transkripsjon og Claude-oversettelse."),
      ("globe","Hvilken som helst mobil og språk","Lyttere blir med via en sekssifret kode eller en QR. Ingen app, ingen konto, anonymt — det bare spiller."),
      ("mic","AI-stemme","Der ingen menneskelig tolk er for hånden, kan mobilen til og med lese oversettelsen selv (eksperimentelt)."),
      ("shield","Privat i sin natur","Ingen lyd tas opp, og økter utløper etter gudstjenesten. Skrive-hemmeligheten når aldri en lytters mobil.")],
    "hl_kicker":"Bygd for benken","hl_title":"Alle hører, på språket de tenker på.",
    "hl_p":"Nykommere, gjester og hørselshemmede følger hele gudstjenesten — uten en tolk ved siden av seg eller en teleslynge i gulvet. De bare åpner en lenke.",
    "checks":["Ingen installasjon, ingen konto — anonymt for lyttere","Kjører på menighetens egen Cloudflare og Supabase","Ingen lyd tas opp; økter utløper av seg selv"],
    "status":"SundayTranslate er kode-komplett gjennom alle tre faser — live tolking, lytteanlegg og AI-undertekster — og vil lanseres som en web-app når siste testing på enhet er ferdig. Ikke ute for bruk ennå.",
    "cta_h":"Vil du ha SundayTranslate i menigheten din?","cta_p":"SundayTranslate er under utvikling. Ta kontakt om menigheten din vil være tidlig ute med live tolking og lyttehjelp."},
  "chips":[]},
 "sundayinfo":{"accent":"info","icon":"screen","short":"Info","url":"https://info.sundaysuite.app",
  "en":{"tagline":"Your church, on every screen.",
    "meta":"SundayInfo is digital signage for churches — service times, plans, weather and the church year on any TV, paired from your phone and running even when the network drops.",
    "lead":"Turn any screen in the building into the church's noticeboard. Service times, today's plan, announcements, weather and a verse for the season — composed from your phone or laptop and shown on a TV, a Chromecast, a PC or a Raspberry Pi. Multi-tenant and multi-editor, with a local cache so it keeps running when the network doesn't.",
    "what":"One screen, always current","whatlead":"Everything a visitor needs to see in the foyer, kept up to date by itself.",
    "features":[("screen","Any screen","TV browser, Chromecast, a PC or a Raspberry Pi — if it shows a web page, it shows SundayInfo."),
      ("people","Many editors, many churches","Multi-tenant from the start, with roles so several people can keep the boards up to date."),
      ("calendar","Knows the church year","Advent, Lent, Easter and ordinary time — the look and the verse follow the season automatically."),
      ("shield","Pairs in seconds","A code on the TV, a tap from your phone — the screen is claimed once and never asks again."),
      ("bolt","Survives a network drop","A local snapshot keeps the last content on screen through an outage, then catches up on its own."),
      ("globe","Vipps QR &amp; live data","Show a Vipps giving QR, the weather and live data alongside the plan, refreshed on the screen's own clock.")],
    "hl_kicker":"Built for the foyer","hl_title":"Always on, always current — even when the network isn't.",
    "hl_p":"A 30-second heartbeat is the source of truth, realtime is just a hint, and a local snapshot survives a dropped connection. The screen runs on its own clock, so the church year and the day's mode are always right.",
    "checks":["Multi-tenant with roles from day one","Pairs once; only a hashed token is stored","Keeps showing content through a network outage"],
    "status":"SundayInfo is up and running in beta at info.sundaysuite.app. Pair a screen, invite editors and publish — sign in with your Sunday account. Testing on real TVs is exactly what the beta is for, so tell us how your screen behaves.",
    "cta_h":"Want SundayInfo on your foyer screen?","cta_p":"It's in beta at info.sundaysuite.app. Get in touch if your church wants help getting the first screen on the wall."},
  "no":{"tagline":"Menigheten din, på hver skjerm.",
    "meta":"SundayInfo er digital infoskjerm for menigheter — gudstjenestetider, planer, vær og kirkeår på en hvilken som helst TV, paret fra mobilen og i drift selv om nettet faller.",
    "lead":"Gjør en hvilken som helst skjerm i bygget til menighetens infotavle. Gudstjenestetider, dagens plan, kunngjøringer, vær og et vers for sesongen — satt sammen fra mobil eller PC og vist på en TV, en Chromecast, en PC eller en Raspberry Pi. Multi-tenant og fler-redaktør, med lokal cache så den går videre når nettet ikke gjør det.",
    "what":"Én skjerm, alltid oppdatert","whatlead":"Alt en besøkende trenger å se i foajeen, holdt oppdatert av seg selv.",
    "features":[("screen","Enhver skjerm","TV-nettleser, Chromecast, en PC eller en Raspberry Pi — viser den en nettside, viser den SundayInfo."),
      ("people","Mange redaktører, mange menigheter","Multi-tenant fra start, med roller så flere kan holde tavlene oppdatert."),
      ("calendar","Kan kirkeåret","Advent, faste, påske og det alminnelige kirkeår — uttrykket og verset følger sesongen automatisk."),
      ("shield","Pares på sekunder","En kode på TV-en, ett trykk fra mobilen — skjermen claimes én gang og spør aldri igjen."),
      ("bolt","Tåler nettbrudd","Et lokalt øyeblikksbilde holder siste innhold på skjermen gjennom et brudd, og tar igjen av seg selv."),
      ("globe","Vipps-QR &amp; sanntidsdata","Vis en Vipps-QR for gaver, været og sanntidsdata ved siden av planen, oppdatert på skjermens egen klokke.")],
    "hl_kicker":"Bygd for foajeen","hl_title":"Alltid på, alltid oppdatert — selv når nettet ikke er det.",
    "hl_p":"Et 30-sekunders hjerteslag er sannheten, realtime er bare et hint, og et lokalt øyeblikksbilde overlever et brudd. Skjermen går på sin egen klokke, så kirkeåret og dagens modus er alltid riktig.",
    "checks":["Multi-tenant med roller fra dag én","Pares én gang; kun en hashet token lagres","Viser innhold videre gjennom nettbrudd"],
    "status":"SundayInfo er oppe og går i beta på info.sundaysuite.app. Par en skjerm, inviter redaktører og publiser — logg inn med Sunday-kontoen din. Testing på ekte TV-er er akkurat det betaen er til, så fortell oss hvordan skjermen din oppfører seg.",
    "cta_h":"Vil du ha SundayInfo på foajé-skjermen?","cta_p":"Den er i beta på info.sundaysuite.app. Ta kontakt om menigheten din vil ha hjelp til å få den første skjermen opp på veggen."},
  "chips":[("Plan","Info","today's service / dagens gudstjeneste"),("Booking","Info","rooms in use / lokaler i bruk")]},
 "sundaybooking":{"accent":"booking","icon":"calendar","short":"Booking","url":"https://booking.sundaysuite.app",
  "en":{"tagline":"Book the church — without double-bookings.",
    "meta":"SundayBooking handles room bookings, external rentals and appointments for the church, with double-bookings made structurally impossible. Signs in with your Sunday account.",
    "lead":"Manage internal rooms, external rentals and appointment bookings in one calendar where overlaps are structurally impossible — set-up and clean-up time included. Staff approve requests; members and renters ask through a link, no account needed for the public flow. Signs in with your shared Sunday account.",
    "what":"Every space, one honest calendar","whatlead":"From a wedding to a choir rehearsal — requested, checked and approved without a clash.",
    "features":[("calendar","Conflict-proof calendar","An exclusion constraint in the database makes a double-booking impossible — including rig and clean-up buffers."),
      ("check","Approval queue","Requests land in a queue staff approve or decline, with suggested alternatives when a slot is taken."),
      ("people","Internal &amp; external","Rooms for staff and volunteers, plus public rentals via a link and a magic-link status page — no account needed."),
      ("stack","Resources &amp; bundles","Define rooms, equipment and event types once; bundle them so booking the hall books the chairs too."),
      ("bell","Live presence","See “someone is asking for this time right now” as it happens, so two planners don't grab the same slot."),
      ("globe","ICS feed &amp; utilisation","Subscribe to a room's calendar as an ICS feed and watch a utilisation dashboard fill in.")],
    "hl_kicker":"Correct by construction","hl_title":"A double-booking isn't caught — it's impossible.",
    "hl_p":"Booking goes through an atomic database function that locks the resources and rejects any overlap on the effective time range, set-up and clean-up included. The wedding and the choir rehearsal can never land on the same room.",
    "checks":["Overlaps blocked by the database, not by a check after the fact","Public rentals without an account, via magic link","One shared Sunday account across the suite"],
    "status":"SundayBooking is up and running in beta at booking.sundaysuite.app. Sign in with your Sunday account to manage resources and approvals; testing across devices is exactly what the beta is for.",
    "cta_h":"Want bookings without the clashes?","cta_p":"It's in beta at booking.sundaysuite.app. Get in touch if your church wants help setting up rooms and rentals."},
  "no":{"tagline":"Book menigheten — uten dobbeltbooking.",
    "meta":"SundayBooking håndterer rombooking, ekstern utleie og avtaler for menigheten, med dobbeltbooking gjort strukturelt umulig. Logger inn med Sunday-kontoen din.",
    "lead":"Styr interne rom, ekstern utleie og avtalebooking i én kalender der overlapp er strukturelt umulig — rigge- og ryddetid inkludert. Staben godkjenner forespørsler; medlemmer og leietakere spør via en lenke, uten konto for den offentlige flyten. Logger inn med den delte Sunday-kontoen din.",
    "what":"Hvert lokale, én ærlig kalender","whatlead":"Fra bryllup til korøvelse — forespurt, sjekket og godkjent uten kollisjon.",
    "features":[("calendar","Kollisjonssikker kalender","En exclusion-constraint i databasen gjør dobbeltbooking umulig — inkludert rigge- og ryddebuffere."),
      ("check","Godkjenningskø","Forespørsler havner i en kø staben godkjenner eller avslår, med forslag til alternativer når en tid er opptatt."),
      ("people","Internt &amp; eksternt","Rom for stab og frivillige, pluss offentlig utleie via lenke og en magic-link-statusside — uten konto."),
      ("stack","Ressurser &amp; pakker","Definer rom, utstyr og arrangementstyper én gang; pakk dem så booking av salen også booker stolene."),
      ("bell","Live tilstedeværelse","Se «noen ber om denne tiden nå» idet det skjer, så to planleggere ikke tar samme tid."),
      ("globe","ICS-feed &amp; utnyttelse","Abonner på et roms kalender som ICS-feed og følg et utnyttelses-dashboard fylles inn.")],
    "hl_kicker":"Riktig ved konstruksjon","hl_title":"En dobbeltbooking fanges ikke — den er umulig.",
    "hl_p":"Booking går gjennom en atomisk databasefunksjon som låser ressursene og avviser ethvert overlapp på det effektive tidsrommet, rigge- og ryddetid inkludert. Bryllupet og korøvelsen kan aldri havne på samme rom.",
    "checks":["Overlapp blokkeres av databasen, ikke av en sjekk i etterkant","Offentlig utleie uten konto, via magic link","Én delt Sunday-konto på tvers av suiten"],
    "status":"SundayBooking er oppe og går i beta på booking.sundaysuite.app. Logg inn med Sunday-kontoen din for å styre ressurser og godkjenninger; testing på tvers av enheter er akkurat det betaen er til.",
    "cta_h":"Vil du ha booking uten kollisjoner?","cta_p":"Den er i beta på booking.sundaysuite.app. Ta kontakt om menigheten din vil ha hjelp til å sette opp rom og utleie."},
  "chips":[("Plan","Booking","shared church / delt menighet"),("Booking","Info","rooms in use / lokaler i bruk")]},
}

CHECKSVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>'

def chip_html(a,b,t): return f'<div class="chip"><span class="from">{a}</span><span class="arrow">&rarr;</span><span class="to">{b}</span>&nbsp;{t}</div>'

def app_body(c, L, slug, short, d, chips, st, hero_actions=None, cta_actions=None, extra=""):
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
    sh = c["status_heads"][st]
    badge = status_badge(st, c, on_ink=True)
    if hero_actions is None:
        hero_actions=f'<a href="mailto:dev@sundaysuite.app" class="btn btn-accent">{c["keep_posted"]}</a><a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a>'
    if cta_actions is None:
        cta_actions=f'<a href="mailto:dev@sundaysuite.app" class="btn btn-primary">dev@sundaysuite.app</a><a href="{L["home"]}#products" class="btn btn-ghost">{c["cta_back"]}</a>'
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
    </div>{extra}
  </div></section>
</div>

<section class="app-cta"><div class="wrap">
  <h2>{d["cta_h"]}</h2><p>{d["cta_p"]}</p>
  <div class="hero-actions" style="justify-content:center">{cta_actions}</div>
</div></section>
</main>''')

def render_app(lang, slug):
    c=CH[lang]; root="../" if lang=="en" else "../../"; L=links(lang,root)
    other = (f'../no/apps/{slug}.html' if lang=="en" else f'../../apps/{slug}.html')
    st=STATUS[slug]
    a=APP.get(slug) or APPDATA[slug]; d=a[lang]
    chips=None
    if a["chips"]:
        chips=[(x[0],x[1], x[2].split(" / ")[0] if lang=="en" else x[2].split(" / ")[1]) for x in a["chips"]]
    if a.get("repo"):
        universal = "niversal" in d["install_mac"]
        dl_mac = (("Download for Mac" if universal else "Download for Mac (Apple&nbsp;Silicon)") if lang=="en"
                  else ("Last ned for Mac" if universal else "Last ned for Mac (Apple&nbsp;Silicon)"))
        dl_win = "Download for Windows" if lang=="en" else "Last ned for Windows"
        ha=(f'<a href="/download/{slug}/mac" class="btn btn-accent">{dl_mac}</a>'
            f'<a href="/download/{slug}/windows" class="btn btn-accent">{dl_win}</a>'
            f'<a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a>')
        ca=(f'<a href="/download/{slug}/mac" class="btn btn-primary">{dl_mac}</a>'
            f'<a href="/download/{slug}/windows" class="btn btn-primary">{dl_win}</a>'
            f'<a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">dev@sundaysuite.app</a>')
        extra=(f'\n    <div class="callout reveal" style="margin:18px auto 0">\n'
               f'      <h4><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--c)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 21h16"/></svg>{d["install_head"]}</h4>\n'
               f'      <p>{d["install_mac"]}</p>\n'
               f'      <p>{d["install_win"]}</p>\n'
               f'      <p><span data-app-version="{slug}" hidden></span><a href="https://github.com/{a["repo"]}/releases" target="_blank" rel="noopener">{d["install_all"]}</a></p>\n'
               f'    </div>')
        body=app_body(c,L,slug,a["short"],d,chips,st,hero_actions=ha,cta_actions=ca,extra=extra)
    elif a.get("url"):
        sub=a["url"].replace("https://","")
        visit=(f'Open {sub}' if lang=="en" else f'Åpne {sub}')
        ha=(f'<a href="{a["url"]}" target="_blank" rel="noopener" class="btn btn-accent">{visit}</a>'
            f'<a href="{L["home"]}#products" class="btn btn-ghost">{c["all_products"]}</a>')
        ca=(f'<a href="{a["url"]}" target="_blank" rel="noopener" class="btn btn-primary">{visit}</a>'
            f'<a href="mailto:dev@sundaysuite.app" class="btn btn-ghost">dev@sundaysuite.app</a>')
        body=app_body(c,L,slug,a["short"],d,chips,st,hero_actions=ha,cta_actions=ca)
    else:
        body=app_body(c,L,slug,a["short"],d,chips,st)
    title=f'{PNAME[slug]} — {d["tagline"]} | Sunday Suite'
    return shell(c,L,other,title,d["meta"],f' style="--c:var(--{a["accent"]})"',body,pair=(f"apps/{slug}.html",f"no/apps/{slug}.html"))

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
    return shell(c,L,other,f'{title} — Sunday Suite',desc,'',content,navscrolled=True,pair=(f"legal/{name}.html",f"no/legal/{name}.html"))

def toc(items): return "".join(f'<li><a href="#{i}">{t}</a></li>' for i,t in items)
def h2(n,i,t): return f'<h2 id="{i}"><span class="num">{n}.</span>{t}</h2>'

# ---- Terms EN
def terms_en():
    note='<strong>Note:</strong> This document is a good-faith template and is not legal advice. Have it reviewed by a lawyer before relying on it commercially — especially the sections on intellectual property, liability and consumer protection.'
    items=[("s1","About these Terms"),("s2","The Service"),("s3","Price, beta and availability"),("s4","Licence"),("s5","Intellectual property and trademarks"),("s6","Your content"),("s7","Third-party services"),("s8","Acceptable use"),("s9","Disclaimer of warranties"),("s10","Limitation of liability"),("s11","Changes to these Terms"),("s12","Governing law and venue"),("s13","Contact")]
    lbl=CH["en"]["status_labels"]
    descs={"sundayrec":"Recording, streaming, transcription and podcast publishing for the church service",
      "sundayscreen":"Offline classroom screen with clock, timer, name picker and group maker (desktop app)",
      "sundaystudio":"Podcast and jingle production for churches",
      "sundaystage":"Presentation of lyrics and media on the big screen",
      "sundayplan":"Service planning and volunteer rota",
      "sundaysong":"Song database with AI and TONO/CCLI reporting",
      "sundayedit":"AI video captioning (standalone product)",
      "sundaysync":"Multicamera audio sync for church and event shoots (desktop app)",
      "sundaypaper":"AI document and PDF tool for print",
      "sundaytranslate":"Live translation and assistive listening for the service (web app)",
      "sundayinfo":"Digital signage for the church (web app)",
      "sundaybooking":"Room, rental and appointment booking (web app)"}
    rows="".join(f"<tr><td>{PNAME[s]}</td><td>{descs[s]}</td><td>{lbl[STATUS[s]]}</td></tr>" for s in SLUGS)
    toolnames=", ".join(t["name"] for t in TOOLS)
    prose=f'''    <p class="lead">Please read these Terms of Use ("Terms") before using the software in Sunday Suite or the website sundaysuite.app (together the "Service"), operated by Richard Fossland ("we", "us" or "our"). By downloading, installing or using a Sunday program you agree to be bound by these Terms. If you do not agree, do not use the Service.</p>
    {h2(1,"s1","About these Terms")}
    <p>Sunday Suite is a family of standalone programs for churches and organizations. These Terms apply to all programs in the suite, both those out in beta and those still in development, and to the website. Individual programs may have their own supplementary terms; in case of conflict, the supplementary terms for the program in question prevail over these general Terms.</p>
    {h2(2,"s2","The Service")}
    <p>Sunday Suite currently consists of the following programs. The status indicates maturity and may change without notice:</p>
    <table class="app-legal-table"><thead><tr><th>Program</th><th>What it is</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
    <p>The programs are delivered mainly as desktop applications for macOS and Windows and/or as web-based services. Not all programs are available for download yet.</p>
    <p>Alongside the core products, Sunday Suite also offers a set of free community web tools — <strong>{toolnames}</strong> — running in the browser on subdomains of sundaysuite.app. These Terms apply to the community tools in the same way as to the programs above.</p>
    {h2(3,"s3","Price, beta and availability")}
    <p>The programs available today are provided free of charge. There is no purchase, subscription or licence fee. We reserve the right to introduce paid features or plans in the future, but any change will be communicated clearly.</p>
    <p>Software marked "beta" or "in development" is offered at an early stage. It may contain bugs, change materially or be withdrawn without notice, and you should verify the first results before using it for anything critical. We give no guarantee that the Service will be available, uninterrupted or preserved over time.</p>
    {h2(4,"s4","Licence")}
    <p>Subject to your compliance with these Terms, we grant you a non-exclusive, non-transferable and revocable licence to download and use the Sunday programs, as distributed via sundaysuite.app, for your organization's own purposes.</p>
    <h3>Open source</h3>
    <p>Sunday Suite is built in the open: much of the suite's source code is published in public repositories on <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a> under open-source licences — MIT where a licence file is present. For that code, the repository's own licence governs your rights, and nothing in these Terms limits what that licence grants you, including the rights to use, study, modify and redistribute the code.</p>
    <p>Except to the extent an applicable open-source licence expressly permits it, you may not:</p>
    <ul><li>redistribute, sell, rent or sublicense the software;</li><li>decompile, reverse-engineer or attempt to derive the source code, except to the extent mandatory law permits;</li><li>remove or alter any copyright notices, trademarks or other proprietary markings;</li><li>use the "Sunday" names, logos or trade dress in a way likely to cause confusion about origin or endorsement; or</li><li>use the Service for any unlawful purpose.</li></ul>
    {h2(5,"s5","Intellectual property and trademarks")}
    <p>The website, design, graphics, the golden cross, logos, names and text are owned by Richard Fossland and protected by applicable law on copyright, trademarks and other intellectual property rights. The source code of the Sunday programs — <strong>SundayRec, SundayScreen, SundayStudio, SundayStage, SundayPlan, SundaySong, SundayEdit, SundaySync, SundayPaper, SundayTranslate, SundayInfo and SundayBooking</strong>, together with the community tools listed in section 2 — is &copy; Richard Fossland and contributors. Every public Sunday repository is currently published under the <strong>MIT Licence</strong>, and that licence governs your rights to the code it contains. Should a repository ever be published without a licence file, it is published for reading only, and no licence to that code is granted until one is added.</p>
    <h3>Trademarks</h3>
    <p>The names "Sunday Suite", the "Sunday" family of product names listed above (including the community tools listed in section 2), and the associated cross and gold symbol, are our trademarks (registered or being established). You are granted no right to use these trademarks, and you must not use them — or names, logos or designs likely to be confused with them — without prior written consent. This also applies to product, domain, app-store and company names. The open-source licences cover the code — they grant no rights to the "Sunday" names, the cross-and-gold mark or the logos.</p>
    <h3>No transfer of rights</h3>
    <p>Except as granted by an applicable open-source licence, nothing in these Terms transfers any intellectual property rights to you. All use not expressly permitted is reserved to the rights holder. We reserve all rights not expressly granted here.</p>
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
    return legal_shell("en","terms","Terms of Use","Last updated: 29 August 2026",note,toc(items),prose)

# ---- Privacy EN
def privacy_en():
    note='<strong>Note:</strong> This document is a good-faith template and is not legal advice. Have it reviewed by a privacy professional before relying on it — especially regarding GDPR and the processing of personal data in recordings.'
    items=[("p1","In short"),("p2","Data on your machine"),("p3","OAuth tokens"),("p4","Cloud uploads"),("p5","Publishing"),("p6","Email alerts"),("p7","No analytics or telemetry"),("p8","Content stays on the machine"),("p9","The website sundaysuite.app"),("p10","Community web tools"),("p11","Third-party services"),("p12","Your rights"),("p13","Changes"),("p14","Contact")]
    prose=f'''    <p class="lead">Sunday Suite is built "local-first". The programs run on your own machine, and your content stays with you unless you choose to upload or publish it. This policy explains what is processed, where, and by whom.</p>
    {h2(1,"p1","In short")}
    <ul><li>The programs are desktop apps that store data locally on your machine.</li><li>We run no central server that receives your recordings, videos or documents.</li><li>Data leaves the machine only when you actively enable a cloud, publishing or alert feature.</li><li>We collect nothing from the programs unless you opt in to anonymous quality telemetry.</li></ul>
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
    <p>The programs contain no advertising and no tracking. We do not know what you record, show, plan or publish. Some apps offer an optional, anonymous quality telemetry — a setting that is <strong>off until you switch it on</strong>, and that never contains your content, recordings or names. The programs may also contact the suite's update service to check whether a newer version exists; such a request does not contain your content.</p>
    {h2(8,"p8","Content stays on the machine")}
    <p>Recording, video and transcription are processed locally. Speech-to-text (Whisper) runs on your own machine. Your content leaves the machine only when you enable a cloud, publishing or sharing feature, as described above.</p>
    {h2(9,"p9","The website sundaysuite.app")}
    <p>The website is an information site. If you get in touch via the email links, we process your email address and the content of your message to reply to you. The download buttons for the desktop apps look up the newest version via the suite's own update service and then redirect to the release on GitHub, served under GitHub's own privacy terms; neither request carries any personal data. If the website later offers forms or a newsletter, their use will be described here, and you will be able to unsubscribe at any time.</p>
    {h2(10,"p10","Community web tools")}
    <p>The free community tools in the toolbox (games and group activities on subdomains of sundaysuite.app) are designed to store as little as possible: sessions are anonymous for participants and expire after use. Two exceptions are worth knowing. <strong>SundayWelcome</strong> stores the contact details a newcomer chooses to submit so the church team can follow up; that data belongs to the church in question, and deletion can be requested at any time from the church or via <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. <strong>SundayBasar</strong> never touches money — payments happen directly in Vipps between you and the organiser, and the app only records what the organiser confirms manually.</p>
    {h2(11,"p11","Third-party services")}
    <p>When you enable an integration, the relevant third party's privacy rules apply to that part of the processing. Examples may be Google (Drive/YouTube), a podcast host or an email provider. You choose whether and when these are used.</p>
    {h2(12,"p12","Your rights")}
    <p>Since most data lives locally on your machine, you have direct control and can view, change, export and delete it yourself. For personal data we may process (for example an email enquiry), you have the right under the privacy regulation (GDPR) to access, rectification, erasure and restriction. Contact us to exercise these rights.</p>
    {h2(13,"p13","Changes")}
    <p>We may update this policy. Material changes are notified by updating the date at the top of the page.</p>
    {h2(14,"p14","Contact")}
    <p>Questions about privacy? Contact the data controller Richard Fossland at <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("en","privacy","Privacy Policy","Last updated: 29 August 2026",note,toc(items),prose)

# ---- Terms NO
def terms_no():
    note='<strong>Merk:</strong> Dette dokumentet er en mal levert i god tro og er ikke juridisk rådgivning. Få det gjennomgått av en advokat før du stoler på det kommersielt — særlig avsnittene om immaterielle rettigheter, ansvar og forbrukervern.'
    items=[("s1","Om vilkårene"),("s2","Tjenesten"),("s3","Pris, beta og tilgjengelighet"),("s4","Lisens"),("s5","Immaterielle rettigheter og varemerker"),("s6","Ditt innhold"),("s7","Tredjepartstjenester"),("s8","Akseptabel bruk"),("s9","Fraskrivelse av garantier"),("s10","Ansvarsbegrensning"),("s11","Endringer i vilkårene"),("s12","Lovvalg og verneting"),("s13","Kontakt")]
    lbl=CH["no"]["status_labels"]
    descs={"sundayrec":"Opptak, strømming, transkripsjon og podkast-publisering for gudstjenesten",
      "sundayscreen":"Offline klasseromsskjerm med klokke, timer, navnetrekker og gruppegenerator (skrivebordsapp)",
      "sundaystudio":"Podkast- og jingleproduksjon for menigheter",
      "sundaystage":"Presentasjon av sangtekster og media på storskjerm",
      "sundayplan":"Gudstjenesteplanlegging og frivillig-turnus",
      "sundaysong":"Sangdatabase med AI og TONO/CCLI-rapportering",
      "sundayedit":"AI-teksting av video (frittstående produkt)",
      "sundaysync":"Multikamera lydsynkronisering for gudstjeneste- og arrangementopptak (skrivebordsapp)",
      "sundaypaper":"AI-dokument- og PDF-verktøy for trykksaker",
      "sundaytranslate":"Live tolking og lytteanlegg for gudstjenesten (web-app)",
      "sundayinfo":"Digital infoskjerm for menigheten (web-app)",
      "sundaybooking":"Rom-, utleie- og avtalebooking (web-app)"}
    rows="".join(f"<tr><td>{PNAME[s]}</td><td>{descs[s]}</td><td>{lbl[STATUS[s]]}</td></tr>" for s in SLUGS)
    toolnames=", ".join(t["name"] for t in TOOLS)
    prose=f'''    <p class="lead">Les disse vilkårene for bruk («Vilkårene») før du bruker programvaren i Sunday Suite eller nettstedet sundaysuite.app (samlet «Tjenesten»), drevet av Richard Fossland («vi», «oss» eller «vår»). Ved å laste ned, installere eller bruke et Sunday-program godtar du å være bundet av disse Vilkårene. Godtar du dem ikke, skal du ikke bruke Tjenesten.</p>
    {h2(1,"s1","Om vilkårene")}
    <p>Sunday Suite er en familie av selvstendige programmer for menigheter og organisasjoner. Vilkårene gjelder for alle programmene i suiten, både de som er ute i beta og de som fortsatt er under utvikling, samt for nettstedet. Enkelte programmer kan ha egne tilleggsvilkår; ved motstrid gjelder tilleggsvilkårene for det aktuelle programmet foran disse generelle Vilkårene.</p>
    {h2(2,"s2","Tjenesten")}
    <p>Sunday Suite består i dag av følgende programmer. Statusen angir modenhet og kan endres uten varsel:</p>
    <table class="app-legal-table"><thead><tr><th>Program</th><th>Hva det er</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
    <p>Programmene leveres i hovedsak som skrivebordsapplikasjoner for macOS og Windows og/eller som nettbaserte tjenester. Ikke alle programmer er tilgjengelige for nedlasting ennå.</p>
    <p>Ved siden av kjerneproduktene tilbyr Sunday Suite også en samling gratis fellesskapsverktøy på nett — <strong>{toolnames}</strong> — som kjører i nettleseren på underdomener av sundaysuite.app. Disse Vilkårene gjelder for fellesskapsverktøyene på samme måte som for programmene over.</p>
    {h2(3,"s3","Pris, beta og tilgjengelighet")}
    <p>Programmene som er tilgjengelige i dag, leveres uten kostnad. Det er ingen kjøps-, abonnements- eller lisensavgift. Vi forbeholder oss retten til å innføre betalte funksjoner eller planer i fremtiden, men eventuelle endringer vil bli kommunisert tydelig.</p>
    <p>Programvare merket «beta» eller «under utvikling» tilbys i en tidlig fase. Den kan inneholde feil, endres vesentlig eller bli trukket tilbake uten varsel, og du bør verifisere de første resultatene før du bruker den til noe kritisk. Vi gir ingen garanti for at Tjenesten vil være tilgjengelig, uavbrutt eller bevart over tid.</p>
    {h2(4,"s4","Lisens")}
    <p>Under forutsetning av at du følger disse Vilkårene, gir vi deg en ikke-eksklusiv, ikke-overførbar og gjenkallelig lisens til å laste ned og bruke Sunday-programmene, slik de distribueres via sundaysuite.app, for din organisasjons egne formål.</p>
    <h3>Åpen kildekode</h3>
    <p>Sunday Suite bygges i det åpne: mye av suitens kildekode er publisert i offentlige repositorier på <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a> under åpen kildekode-lisenser — MIT der lisensfil foreligger. For den koden er det repositoriets egen lisens som styrer rettighetene dine, og ingenting i disse Vilkårene innskrenker det lisensen gir deg, herunder retten til å bruke, studere, endre og videredistribuere koden.</p>
    <p>Med mindre en gjeldende åpen kildekode-lisens uttrykkelig tillater det, har du ikke lov til å:</p>
    <ul><li>videredistribuere, selge, leie ut eller viderelisensiere programvaren;</li><li>dekompilere, reversutvikle eller forsøke å utlede kildekoden, unntatt i den grad ufravikelig lov tillater det;</li><li>fjerne eller endre opphavsrettsmerker, varemerker eller andre rettighetsmerker;</li><li>bruke «Sunday»-navnene, logoene eller utformingen på en måte som er egnet til å skape forveksling om opphav eller tilknytning; eller</li><li>bruke Tjenesten til ulovlige formål.</li></ul>
    {h2(5,"s5","Immaterielle rettigheter og varemerker")}
    <p>Nettstedet, designet, grafikken, det gylne korset, logoene, navnene og teksten eies av Richard Fossland og er beskyttet av gjeldende lovgivning om opphavsrett, varemerker og andre immaterielle rettigheter. Kildekoden til Sunday-programmene — <strong>SundayRec, SundayScreen, SundayStudio, SundayStage, SundayPlan, SundaySong, SundayEdit, SundaySync, SundayPaper, SundayTranslate, SundayInfo og SundayBooking</strong>, sammen med fellesskapsverktøyene nevnt i punkt 2 — er &copy; Richard Fossland og bidragsytere. Hvert offentlige Sunday-repositorium er i dag publisert under <strong>MIT-lisensen</strong>, og den lisensen styrer rettighetene dine til koden det inneholder. Skulle et repositorium noen gang bli publisert uten lisensfil, er det publisert kun for lesing, og ingen lisens til den koden gis før en legges til.</p>
    <h3>Varemerker</h3>
    <p>Navnene «Sunday Suite», «Sunday»-familien av produktnavn nevnt over (inkludert fellesskapsverktøyene i punkt 2), samt det tilhørende kors- og gull-symbolet, er våre varemerker (registrerte eller under etablering). Du får ingen rett til å bruke disse varemerkene, og du må ikke bruke dem — eller navn, logoer eller utforming som er egnet til å forveksles med dem — uten skriftlig forhåndssamtykke. Dette gjelder også produkt-, domene-, app-butikk- og selskapsnavn. Åpen kildekode-lisensene dekker koden — de gir ingen rett til «Sunday»-navnene, kors-og-gull-merket eller logoene.</p>
    <h3>Ingen rettighetsoverføring</h3>
    <p>Ut over det en gjeldende åpen kildekode-lisens gir, overfører ingenting i disse Vilkårene immaterielle rettigheter til deg. All bruk som ikke uttrykkelig er tillatt, er forbeholdt rettighetshaver. Vi forbeholder oss alle rettigheter som ikke uttrykkelig er gitt her.</p>
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
    return legal_shell("no","terms","Vilkår for bruk","Sist oppdatert: 29. august 2026",note,toc(items),prose)

# ---- Privacy NO
def privacy_no():
    note='<strong>Merk:</strong> Dette dokumentet er en mal levert i god tro og er ikke juridisk rådgivning. Få det gjennomgått av en personvernkyndig før du baserer deg på det — særlig med tanke på GDPR og behandling av personopplysninger i opptak.'
    items=[("p1","Kort fortalt"),("p2","Data på din maskin"),("p3","OAuth-tokens"),("p4","Sky-opplastinger"),("p5","Publisering"),("p6","E-postvarsler"),("p7","Ingen analyse eller telemetri"),("p8","Innhold forlater ikke maskinen"),("p9","Nettstedet sundaysuite.app"),("p10","Fellesskapsverktøy på nett"),("p11","Tredjepartstjenester"),("p12","Dine rettigheter"),("p13","Endringer"),("p14","Kontakt")]
    prose=f'''    <p class="lead">Sunday Suite er bygd «lokalt først». Programmene kjører på din egen maskin, og innholdet ditt blir hos deg med mindre du selv velger å laste det opp eller publisere det. Denne erklæringen forklarer hva som behandles, hvor, og av hvem.</p>
    {h2(1,"p1","Kort fortalt")}
    <ul><li>Programmene er skrivebordsapper som lagrer data lokalt på din maskin.</li><li>Vi driver ingen sentral server som mottar opptakene, videoene eller dokumentene dine.</li><li>Data forlater maskinen bare når du aktivt aktiverer en sky-, publiserings- eller varselfunksjon.</li><li>Vi samler ikke inn noe fra programmene med mindre du takker ja til anonym kvalitetstelemetri.</li></ul>
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
    <p>Programmene inneholder ingen reklame og ingen sporing. Vi vet ikke hva du tar opp, viser, planlegger eller publiserer. Noen apper tilbyr en valgfri, anonym kvalitetstelemetri — en innstilling som er <strong>av til du skrur den på</strong>, og som aldri inneholder innholdet, opptakene eller navnene dine. Programmene kan også kontakte suitens oppdateringstjeneste for å sjekke om en nyere versjon finnes; en slik forespørsel inneholder ikke ditt innhold.</p>
    {h2(8,"p8","Innhold forlater ikke maskinen")}
    <p>Opptak, video og transkripsjon behandles lokalt. Tale-til-tekst (Whisper) kjører på din egen maskin. Ditt innhold forlater maskinen bare når du selv aktiverer en sky-, publiserings- eller delefunksjon, slik beskrevet over.</p>
    {h2(9,"p9","Nettstedet sundaysuite.app")}
    <p>Nettstedet er en informasjonsside. Tar du kontakt via e-postlenkene, behandler vi e-postadressen din og innholdet i henvendelsen for å svare deg. Nedlastingsknappene for skrivebordsappene slår opp nyeste versjon via suitens egen oppdateringstjeneste og videresender så til utgivelsen på GitHub, betjent under GitHubs egne personvernvilkår; ingen av forespørslene bærer persondata. Hvis nettstedet senere tilbyr skjemaer eller nyhetsbrev, vil bruken av disse beskrives her, og du vil kunne melde deg av når som helst.</p>
    {h2(10,"p10","Fellesskapsverktøy på nett")}
    <p>De gratis fellesskapsverktøyene i verktøykassa (spill og gruppeaktiviteter på underdomener av sundaysuite.app) er designet for å lagre minst mulig: økter er anonyme for deltakerne og utløper etter bruk. To unntak er verdt å kjenne til. <strong>SundayWelcome</strong> lagrer kontaktinformasjonen en nykommer selv velger å legge igjen, slik at menighetens team kan følge opp; disse dataene tilhører den aktuelle menigheten, og sletting kan når som helst kreves hos menigheten eller via <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. <strong>SundayBasar</strong> rører aldri penger — betalinger skjer direkte i Vipps mellom deg og arrangøren, og appen registrerer bare det arrangøren selv bekrefter manuelt.</p>
    {h2(11,"p11","Tredjepartstjenester")}
    <p>Når du aktiverer en integrasjon, gjelder den aktuelle tredjepartens personvernregler for den delen av behandlingen. Eksempler kan være Google (Drive/YouTube), en podkast-host eller en e-postleverandør. Du velger selv om og når disse tas i bruk.</p>
    {h2(12,"p12","Dine rettigheter")}
    <p>Siden de fleste dataene ligger lokalt på din maskin, har du direkte kontroll og kan se, endre, eksportere og slette dem selv. For personopplysninger vi måtte behandle (for eksempel en e-posthenvendelse), har du etter personvernregelverket (GDPR) rett til innsyn, retting, sletting og begrensning. Kontakt oss for å utøve disse rettighetene.</p>
    {h2(13,"p13","Endringer")}
    <p>Vi kan oppdatere denne erklæringen. Vesentlige endringer varsles ved å oppdatere datoen øverst på siden.</p>
    {h2(14,"p14","Kontakt")}
    <p>Spørsmål om personvern? Kontakt behandlingsansvarlig Richard Fossland på <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return legal_shell("no","privacy","Personvernerklæring","Sist oppdatert: 29. august 2026",note,toc(items),prose)

# ===================================================================== HELP
# Task-based help articles for non-technical volunteers and planners.
# EN lives at /help/, NO at /no/hjelp/ — same English file slugs in both
# languages so the language switch is a simple directory swap.
HELP_ORDER = ["recording-with-sundayrec","signage-with-sundayinfo","booking-with-sundaybooking",
              "licensing-ccli-tono","your-data-and-privacy","community-toolbox","faq"]
# Help guides removed 2026-08-29 (SundayPlan demoted to the drawing board); build.py
# generates 301 redirects for them via _redirects so old links keep working.
REMOVED_HELP = ["getting-started","volunteers-and-teams","plan-a-service","messages-and-magic-links"]

HELP_INDEX = {
 "en":{"title":"Help & guides — Sunday Suite",
   "meta":"Plain-language guides for Sunday Suite: record with SundayRec, put SundayInfo on a screen, book rooms with SundayBooking, run the community toolbox — plus licensing, privacy and FAQ.",
   "crumb":"Help","h1":"Help &amp; guides",
   "lead":"Plain-language guides for church volunteers and planners — no technical background needed. Start at the top if you're new, or jump straight to the question you have.",
   "read":"Read the guide",
   "contact":"Can't find what you're looking for? We answer every email:"},
 "no":{"title":"Hjelp & veiledninger — Sunday Suite",
   "meta":"Lettleste veiledninger for Sunday Suite: ta opp med SundayRec, få SundayInfo på skjermen, book rom med SundayBooking, kjør verktøykassa — pluss lisens, personvern og FAQ.",
   "crumb":"Hjelp","h1":"Hjelp &amp; veiledninger",
   "lead":"Lettleste veiledninger for frivillige og planleggere i menigheten — ingen teknisk bakgrunn nødvendig. Start øverst om du er ny, eller hopp rett til spørsmålet du har.",
   "read":"Les veiledningen",
   "contact":"Finner du ikke det du leter etter? Vi svarer på hver e-post:"},
}

HELPDOC = {
 # ------------------------------------------------------------ 5 recording with sundayrec
 "recording-with-sundayrec":{"accent":"rec",
  "en":{"tag":"SundayRec","card":"Recording with SundayRec",
    "desc":"Download the free beta for Mac or Windows, make your first recording and find the file afterwards — in five minutes.",
    "h1":"Recording with SundayRec","sub":"Download the beta, record your first service and find the file afterwards.",
    "note":"<strong>Beta:</strong> SundayRec is free and works today, but it is still in beta. Do a test recording before you rely on it for a service that matters — press record, talk for a minute, stop, and check the file.",
    "body":'''    <p class="lead">SundayRec is the desktop app that records the service — audio and video — on your own machine. No subscription, no account, and your files never leave the computer unless you choose to upload them. Here is the five-minute version.</p>
    <h2>1. Download and install</h2>
    <p>Download SundayRec straight from the <a href="@@RECAPP@@">SundayRec product page</a> on this site — one button for Mac (Apple Silicon) and one for Windows, always pointing at the latest release. Install it like any other program; on Mac the very first launch is <em>right-click → Open</em> (the app is signed but not yet notarized), and Windows may show a SmartScreen notice — choose <em>More info → Run anyway</em>. All versions and release notes live on <a href="https://github.com/SundaySuite-app/sundayrec/releases" target="_blank" rel="noopener">GitHub</a>.</p>
    <h2>2. Make your first recording</h2>
    <p>Open SundayRec and check that the right microphone (and camera, if you record video) is selected in the settings. Then press <strong>record</strong>. When the service is over, press <strong>stop</strong>. That's genuinely it — scheduling, transcription, streaming and podcast publishing exist too, but plain record→stop is the place to start.</p>
    <h2>3. Find your file</h2>
    <p>Finished recordings appear in the app's history list, and from there you can jump straight to the file on disk. The recordings are ordinary audio and video files — you can play them, copy them to a USB stick, or hand them to whoever edits, like any other file.</p>
    <h2>Good habits</h2>
    <ul>
      <li><strong>Test first.</strong> A one-minute test recording before the real thing catches a wrong microphone while it's still fixable.</li>
      <li><strong>Check disk space.</strong> Video takes room; SundayRec shows you how much space is free.</li>
      <li><strong>Let it warm up.</strong> Start the machine a little before the service rather than thirty seconds before.</li>
    </ul>
    <h2>Going further</h2>
    <p>When record→stop feels comfortable, SundayRec can do much more: scheduled recordings that start by themselves, local AI transcription of the sermon, live streaming and podcast publishing. Read more on the <a href="@@RECAPP@@">SundayRec product page</a>, or just explore the settings — and email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> if you get stuck.</p>'''},
  "no":{"tag":"SundayRec","card":"Ta opp med SundayRec",
    "desc":"Last ned gratis-betaen for Mac eller Windows, gjør ditt første opptak og finn fila etterpå — på fem minutter.",
    "h1":"Ta opp med SundayRec","sub":"Last ned betaen, ta opp din første gudstjeneste og finn fila etterpå.",
    "note":"<strong>Beta:</strong> SundayRec er gratis og fungerer i dag, men er fortsatt i beta. Gjør et testopptak før du stoler på den til en gudstjeneste som betyr noe — trykk opptak, snakk i ett minutt, stopp, og sjekk fila.",
    "body":'''    <p class="lead">SundayRec er skrivebordsappen som tar opp gudstjenesten — lyd og video — på din egen maskin. Ingen abonnement, ingen konto, og filene dine forlater aldri datamaskinen med mindre du selv velger å laste dem opp. Her er fem-minutters-versjonen.</p>
    <h2>1. Last ned og installer</h2>
    <p>Last ned SundayRec rett fra <a href="@@RECAPP@@">produktsiden for SundayRec</a> her på nettstedet — én knapp for Mac (Apple Silicon) og én for Windows, som alltid peker på nyeste utgivelse. Installer som et hvilket som helst annet program; på Mac er aller første start <em>høyreklikk → Åpne</em> (appen er signert, men ennå ikke notarisert), og Windows kan vise et SmartScreen-varsel — velg <em>Mer info → Kjør likevel</em>. Alle versjoner og utgivelsesnotater ligger på <a href="https://github.com/SundaySuite-app/sundayrec/releases" target="_blank" rel="noopener">GitHub</a>.</p>
    <h2>2. Gjør ditt første opptak</h2>
    <p>Åpne SundayRec og sjekk at riktig mikrofon (og kamera, hvis du tar opp video) er valgt i innstillingene. Trykk så <strong>opptak</strong>. Når gudstjenesten er over, trykker du <strong>stopp</strong>. Det er faktisk alt — tidsplan, transkripsjon, strømming og podkast-publisering finnes også, men rent opptak→stopp er stedet å begynne.</p>
    <h2>3. Finn fila di</h2>
    <p>Ferdige opptak dukker opp i appens historikkliste, og derfra kan du hoppe rett til fila på disken. Opptakene er helt vanlige lyd- og videofiler — du kan spille dem av, kopiere dem til en minnepinne eller gi dem til den som redigerer, som en hvilken som helst annen fil.</p>
    <h2>Gode vaner</h2>
    <ul>
      <li><strong>Test først.</strong> Et ettminutts testopptak før alvoret avslører feil mikrofon mens det fortsatt kan fikses.</li>
      <li><strong>Sjekk diskplass.</strong> Video tar plass; SundayRec viser deg hvor mye som er ledig.</li>
      <li><strong>La den varme opp.</strong> Start maskinen litt før gudstjenesten i stedet for tretti sekunder før.</li>
    </ul>
    <h2>Veien videre</h2>
    <p>Når opptak→stopp kjennes trygt, kan SundayRec mye mer: planlagte opptak som starter av seg selv, lokal AI-transkripsjon av talen, live-strømming og podkast-publisering. Les mer på <a href="@@RECAPP@@">produktsiden for SundayRec</a>, eller bare utforsk innstillingene — og send en e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> om du står fast.</p>'''}},
 # ------------------------------------------------------------ signage with sundayinfo
 "signage-with-sundayinfo":{"accent":"info",
  "en":{"tag":"SundayInfo","card":"Signage with SundayInfo",
    "desc":"Turn any TV into the church noticeboard — pair a screen with a code, invite editors, and keep it running even when the network drops.",
    "h1":"Signage with SundayInfo","sub":"From a blank TV to a living noticeboard in the foyer.",
    "note":"<strong>In beta:</strong> SundayInfo is up and running at <a href=\"https://info.sundaysuite.app\" target=\"_blank\" rel=\"noopener\">info.sundaysuite.app</a> and free to use — sign in with your Sunday account. We're still testing on a variety of real TVs, so if your screen does something odd, tell us: <a href=\"mailto:dev@sundaysuite.app\">dev@sundaysuite.app</a>.",
    "body":'''    <p class="lead">SundayInfo turns any screen in the building into the church's noticeboard: service times, today's plan, announcements, the weather and a verse for the season. If a device can show a web page — a TV browser, a Chromecast, a PC or a Raspberry Pi — it can show SundayInfo. Here is how to get the first screen on the wall.</p>
    <h2>1. Sign in and create your church</h2>
    <p>Open <a href="https://info.sundaysuite.app" target="_blank" rel="noopener">info.sundaysuite.app</a> and sign in with your Sunday account. The first time, you create your church — and you can invite more editors later, so keeping the boards fresh never depends on one person.</p>
    <h2>2. Pair the screen</h2>
    <p>On the TV (or whatever drives it), open the screen link — a short pairing code appears on the display. From your phone or laptop, enter the code, and the screen is claimed for your church. It pairs once and never asks again; only a hashed token is stored on the device.</p>
    <h2>3. Compose the board</h2>
    <p>Choose what the screen shows: service times, today's plan, announcements, the weather, a Vipps giving QR, and a verse that follows the church year — Advent, Lent, Easter and ordinary time change the look and the verse automatically. You compose from your phone or laptop; the screen updates on its own clock.</p>
    <h2>Several editors, several screens</h2>
    <p>SundayInfo is built for teams: invite the people who should keep the boards up to date, and give each screen its own content if you like — one board in the foyer, another outside the kids' rooms. Every editor sees only your church's screens.</p>
    <h2>When the network drops</h2>
    <p>Screens keep going through an outage: a local snapshot holds the last published content on the display, and when the connection returns the screen catches up by itself. A dropped wifi should never mean a black wall on Sunday morning.</p>
    <h2>Good habits</h2>
    <ul>
      <li><strong>Put the screen where guests actually look</strong> — the foyer beats the office corridor.</li>
      <li><strong>Keep announcements short.</strong> A noticeboard is read in passing, not studied.</li>
      <li><strong>Check it on a Sunday.</strong> Walk past your own screen now and then — the board is for the people walking by.</li>
    </ul>
    <p>Read more on the <a href="@@INFOAPP@@">SundayInfo product page</a>, or email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> if you'd like help getting the first screen up.</p>'''},
  "no":{"tag":"SundayInfo","card":"Infoskjermer med SundayInfo",
    "desc":"Gjør en hvilken som helst TV til menighetens infotavle — par en skjerm med en kode, inviter redaktører, og la den gå videre selv om nettet faller.",
    "h1":"Infoskjermer med SundayInfo","sub":"Fra svart TV til en levende infotavle i foajeen.",
    "note":"<strong>I beta:</strong> SundayInfo er oppe og går på <a href=\"https://info.sundaysuite.app\" target=\"_blank\" rel=\"noopener\">info.sundaysuite.app</a> og gratis å bruke — logg inn med Sunday-kontoen din. Vi tester fortsatt på ulike ekte TV-er, så gjør skjermen din noe rart, si fra: <a href=\"mailto:dev@sundaysuite.app\">dev@sundaysuite.app</a>.",
    "body":'''    <p class="lead">SundayInfo gjør en hvilken som helst skjerm i bygget til menighetens infotavle: gudstjenestetider, dagens plan, kunngjøringer, været og et vers for sesongen. Kan en enhet vise en nettside — en TV-nettleser, en Chromecast, en PC eller en Raspberry Pi — kan den vise SundayInfo. Slik får du den første skjermen opp på veggen.</p>
    <h2>1. Logg inn og opprett menigheten</h2>
    <p>Åpne <a href="https://info.sundaysuite.app" target="_blank" rel="noopener">info.sundaysuite.app</a> og logg inn med Sunday-kontoen din. Første gang oppretter du menigheten — og du kan invitere flere redaktører senere, så tavlene aldri avhenger av én person.</p>
    <h2>2. Par skjermen</h2>
    <p>På TV-en (eller det som driver den) åpner du skjermlenken — en kort paringskode vises på displayet. Fra mobilen eller PC-en skriver du inn koden, og skjermen claimes for menigheten din. Den pares én gang og spør aldri igjen; kun en hashet token lagres på enheten.</p>
    <h2>3. Sett sammen tavla</h2>
    <p>Velg hva skjermen skal vise: gudstjenestetider, dagens plan, kunngjøringer, været, en Vipps-QR for gaver, og et vers som følger kirkeåret — advent, faste, påske og det alminnelige kirkeår endrer uttrykk og vers automatisk. Du komponerer fra mobil eller PC; skjermen oppdaterer seg på sin egen klokke.</p>
    <h2>Flere redaktører, flere skjermer</h2>
    <p>SundayInfo er bygd for team: inviter de som skal holde tavlene oppdatert, og gi gjerne hver skjerm sitt eget innhold — én tavle i foajeen, en annen utenfor barnerommene. Hver redaktør ser bare din menighets skjermer.</p>
    <h2>Når nettet faller</h2>
    <p>Skjermene går videre gjennom et brudd: et lokalt øyeblikksbilde holder det sist publiserte innholdet på displayet, og når forbindelsen er tilbake, tar skjermen igjen av seg selv. Et wifi-brudd skal aldri bety en svart vegg søndag morgen.</p>
    <h2>Gode vaner</h2>
    <ul>
      <li><strong>Sett skjermen der gjestene faktisk ser</strong> — foajeen slår kontorgangen.</li>
      <li><strong>Hold kunngjøringene korte.</strong> En infotavle leses i forbifarten, ikke studeres.</li>
      <li><strong>Sjekk den en søndag.</strong> Gå forbi din egen skjerm av og til — tavla er til for dem som går forbi.</li>
    </ul>
    <p>Les mer på <a href="@@INFOAPP@@">produktsiden for SundayInfo</a>, eller send en e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> om du vil ha hjelp til å få opp den første skjermen.</p>'''}},
 # ------------------------------------------------------------ booking with sundaybooking
 "booking-with-sundaybooking":{"accent":"booking",
  "en":{"tag":"SundayBooking","card":"Rooms &amp; rentals with SundayBooking",
    "desc":"One honest calendar for rooms, rentals and appointments — where a double-booking isn't caught afterwards, it's impossible.",
    "h1":"Rooms &amp; rentals with SundayBooking","sub":"From request to approved booking — without a single clash.",
    "note":"<strong>In beta:</strong> SundayBooking is up and running at <a href=\"https://booking.sundaysuite.app\" target=\"_blank\" rel=\"noopener\">booking.sundaysuite.app</a> and free to use — sign in with your Sunday account.",
    "body":'''    <p class="lead">SundayBooking manages internal rooms, external rentals and appointment bookings in one calendar where overlaps are structurally impossible — set-up and clean-up time included. Staff approve requests; members and renters ask through a link, with no account needed. Here is how to set it up.</p>
    <h2>1. Sign in</h2>
    <p>Open <a href="https://booking.sundaysuite.app" target="_blank" rel="noopener">booking.sundaysuite.app</a> and sign in with your Sunday account — the same account that will carry you across the whole suite.</p>
    <h2>2. Define rooms and resources</h2>
    <p>Set up the spaces and things people book: the main hall, the kitchen, meeting rooms, the projector, the minibus. Define event types with their own rules, and bundle resources so booking the hall can book the chairs and the kitchen along with it — once, not as three separate requests.</p>
    <h2>3. How requests come in</h2>
    <p>Staff and trusted volunteers book directly in the calendar. Everyone else — members and external renters — asks through a link: they pick a time, describe what they need, and get a personal magic-link status page to follow their request. No account, no password, no phone tag.</p>
    <h2>4. The approval queue</h2>
    <p>Requests land in a queue where staff approve or decline. If a slot is taken, SundayBooking suggests alternatives instead of just saying no. You can also see "someone is asking about this time right now" as it happens, so two planners don't chase the same evening.</p>
    <h2>Why a double-booking can't happen</h2>
    <p>This is the part spreadsheets can't promise: every booking goes through an atomic database check that locks the resources and rejects any overlap on the effective time range — rig time and clean-up buffers included. The wedding and the choir rehearsal can never land on the same room. It isn't caught by someone paying attention; it's rejected by construction.</p>
    <h2>Calendars out, insight in</h2>
    <p>Subscribe to any room's calendar as an ICS feed in the calendar app you already use, and watch the utilisation dashboard fill in — which spaces earn their keep, and which evenings stand empty.</p>
    <p>Read more on the <a href="@@BOOKINGAPP@@">SundayBooking product page</a>, or email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> if you'd like help setting up rooms and rentals.</p>'''},
  "no":{"tag":"SundayBooking","card":"Rom &amp; utleie med SundayBooking",
    "desc":"Én ærlig kalender for rom, utleie og avtaler — der en dobbeltbooking ikke fanges i etterkant, men er umulig.",
    "h1":"Rom &amp; utleie med SundayBooking","sub":"Fra forespørsel til godkjent booking — uten en eneste kollisjon.",
    "note":"<strong>I beta:</strong> SundayBooking er oppe og går på <a href=\"https://booking.sundaysuite.app\" target=\"_blank\" rel=\"noopener\">booking.sundaysuite.app</a> og gratis å bruke — logg inn med Sunday-kontoen din.",
    "body":'''    <p class="lead">SundayBooking styrer interne rom, ekstern utleie og avtalebooking i én kalender der overlapp er strukturelt umulig — rigge- og ryddetid inkludert. Staben godkjenner forespørsler; medlemmer og leietakere spør via en lenke, uten konto. Slik setter du det opp.</p>
    <h2>1. Logg inn</h2>
    <p>Åpne <a href="https://booking.sundaysuite.app" target="_blank" rel="noopener">booking.sundaysuite.app</a> og logg inn med Sunday-kontoen din — den samme kontoen som skal bære deg gjennom hele suiten.</p>
    <h2>2. Definer rom og ressurser</h2>
    <p>Sett opp lokalene og tingene folk booker: storsalen, kjøkkenet, møterom, prosjektoren, minibussen. Definer arrangementstyper med egne regler, og pakk ressurser sammen slik at booking av salen også kan booke stolene og kjøkkenet — én gang, ikke som tre separate forespørsler.</p>
    <h2>3. Slik kommer forespørslene inn</h2>
    <p>Stab og betrodde frivillige booker rett i kalenderen. Alle andre — medlemmer og eksterne leietakere — spør via en lenke: de velger en tid, beskriver behovet, og får en personlig magic-link-statusside der de følger forespørselen sin. Ingen konto, ikke noe passord, ingen telefonrunder.</p>
    <h2>4. Godkjenningskøen</h2>
    <p>Forespørsler havner i en kø der staben godkjenner eller avslår. Er en tid opptatt, foreslår SundayBooking alternativer i stedet for bare å si nei. Du kan også se «noen spør om denne tiden nå» idet det skjer, så to planleggere ikke jakter på samme kveld.</p>
    <h2>Hvorfor en dobbeltbooking ikke kan skje</h2>
    <p>Dette er delen regneark ikke kan love: hver booking går gjennom en atomisk databasesjekk som låser ressursene og avviser ethvert overlapp på det effektive tidsrommet — rigge- og ryddebuffere inkludert. Bryllupet og korøvelsen kan aldri havne på samme rom. Det fanges ikke av at noen følger med; det avvises ved konstruksjon.</p>
    <h2>Kalendere ut, innsikt inn</h2>
    <p>Abonner på et hvilket som helst roms kalender som ICS-feed i kalenderappen du allerede bruker, og følg utnyttelses-dashbordet fylles inn — hvilke lokaler som gjør nytte for seg, og hvilke kvelder som står tomme.</p>
    <p>Les mer på <a href="@@BOOKINGAPP@@">produktsiden for SundayBooking</a>, eller send en e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> om du vil ha hjelp til å sette opp rom og utleie.</p>'''}},
 # ------------------------------------------------------------ 6 licensing
 "licensing-ccli-tono":{"accent":"song",
  "en":{"tag":"Licensing","card":"Licensing: CCLI &amp; TONO",
    "desc":"What Sunday Suite is designed to track for your music licences, where the numbers will live — and why TONO support matters for Nordic churches.",
    "h1":"Licensing: CCLI &amp; TONO","sub":"What the suite is designed to track, where your licence numbers will live — and why TONO matters.",
    "note":"<strong>One honest line:</strong> Sunday Suite helps you keep licence information in order, but the responsibility for correct reporting to TONO and CCLI always stays with the church. The tools make it easier — they don't take over the obligation.",
    "body":'''    <p class="lead">Most churches sing and stream songs that are protected by copyright, and cover this through licences — internationally often <strong>CCLI</strong>, and in Norway and the Nordics through <strong>TONO</strong>. Sunday Suite is built with both in mind from day one, with TONO as a first-class citizen rather than an afterthought.</p>
    <h2>What Sunday Suite is designed to keep track of</h2>
    <p>Across the suite's data models, your church's licence information is designed in as proper, first-class fields: TONO customer ID and licence status, your denomination, and your CCLI licence number. The goal is that the suite always knows whether your licences are in order — instead of the numbers living in someone's old email.</p>
    <h2>Where the numbers will live</h2>
    <p>The licence fields have their home in SundayPlan, the suite's planning tool — which is still on the drawing board. Until it opens, keep your TONO customer ID and CCLI licence number somewhere safe (they're on your agreements or invoices), and know that a first-class home for them is part of the plan.</p>
    <h2>Why TONO matters — and why we emphasise it</h2>
    <p>The big international church tools are built around American CCLI, and TONO — which is what actually applies for Norwegian rights holders — is usually missing entirely. Sunday Suite is designed the other way around: TONO fields from the first row of the database, including the distinction between songs used <em>in the room</em> and songs that were <em>streamed</em>, which TONO treats as a separate royalty pool.</p>
    <h2>What works today, and what is coming</h2>
    <p><strong>The first piece has shipped.</strong> The SundayStage beta keeps a song usage log, and it writes itself: every song that actually reached the congregation screen is recorded — a song that was only previewed, or that sat in the plan without being shown, does not count, and neither does a quick flick past. The rehearsal and the service on the same day share one row; next Sunday gets its own.</p>
    <p>Each row is a snapshot: title, CCLI number, TONO id, copyright and author are copied in, so a January report can still be sent in April even if the song was deleted in February. A separate <em>Missing</em> column names what the row does not know, so you can see what needs filling in before you submit. Export it as CSV for the period you need, under Settings &rarr; Advanced. The log is local, you can delete it yourself, and it clears automatically after two years.</p>
    <p>Still ahead: the same automatic logging across the rest of the suite, and the licence numbers themselves living in <a href="@@SONGAPP@@">SundaySong</a> and SundayPlan. If licensing is what your church needs most, say so: <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''},
  "no":{"tag":"Lisens","card":"Lisens: CCLI &amp; TONO",
    "desc":"Hva Sunday Suite er designet for å holde styr på for musikklisensene dine, hvor numrene skal bo — og hvorfor TONO-støtte betyr noe for nordiske menigheter.",
    "h1":"Lisens: CCLI &amp; TONO","sub":"Hva suiten er designet for å holde styr på, hvor lisensnumrene dine skal bo — og hvorfor TONO betyr noe.",
    "note":"<strong>Én ærlig linje:</strong> Sunday Suite hjelper deg å holde lisensinformasjonen i orden, men ansvaret for riktig rapportering til TONO og CCLI ligger alltid hos menigheten. Verktøyene gjør det enklere — de overtar ikke forpliktelsen.",
    "body":'''    <p class="lead">De fleste menigheter synger og strømmer sanger som er beskyttet av opphavsrett, og dekker dette gjennom lisenser — internasjonalt ofte <strong>CCLI</strong>, og i Norge og Norden gjennom <strong>TONO</strong>. Sunday Suite er bygd med begge i tankene fra dag én, med TONO i førsteklasse i stedet for som en ettertanke.</p>
    <h2>Hva Sunday Suite er designet for å holde styr på</h2>
    <p>På tvers av suitens datamodeller er menighetens lisensinformasjon designet inn som ordentlige, førsteklasses felt: TONO-kunde-ID og lisensstatus, kirkesamfunn, og CCLI-lisensnummeret deres. Målet er at suiten alltid vet om lisensene er i orden — i stedet for at numrene bor i en gammel e-post hos noen.</p>
    <h2>Hvor numrene skal bo</h2>
    <p>Lisensfeltene hører hjemme i SundayPlan, suitens planleggingsverktøy — som fortsatt er på tegnebrettet. Til det åpner: ta vare på TONO-kunde-ID-en og CCLI-lisensnummeret et trygt sted (de står på avtalene eller fakturaene deres), og vit at et førsteklasses hjem for dem er en del av planen.</p>
    <h2>Hvorfor TONO betyr noe — og hvorfor vi legger vekt på det</h2>
    <p>De store internasjonale menighetsverktøyene er bygd rundt amerikansk CCLI, og TONO — som er det som faktisk gjelder for norske rettighetshavere — mangler som regel helt. Sunday Suite er designet motsatt vei: TONO-felt fra første rad i databasen, inkludert skillet mellom sanger brukt <em>i rommet</em> og sanger som ble <em>strømmet</em>, som TONO behandler som en egen royalty-pott.</p>
    <h2>Hva som virker i dag, og hva som kommer</h2>
    <p><strong>Den første brikken har rukket ut.</strong> SundayStage-betaen fører en sangbrukslogg, og den skriver seg selv: hver sang som faktisk nådde menighetsskjermen blir registrert — en sang som bare ble forhåndsvist, eller som lå i planen uten å bli sendt, teller ikke, og det gjør heller ikke en rask gjennombla. Generalprøven og gudstjenesten samme dag deler én rad; neste søndag får sin egen.</p>
    <p>Hver rad er et øyeblikksbilde: tittel, CCLI-nummer, TONO-ID, copyright og opphavsperson kopieres inn, så januarrapporten kan sendes i april selv om sangen ble slettet i februar. En egen <em>Mangler</em>-kolonne navngir det raden ikke vet, så du ser hva som må fylles ut før innsending. Eksporter den som CSV for perioden du skal rapportere, under Innstillinger &rarr; Avansert. Loggen er lokal, du kan slette den selv, og den ryddes automatisk etter to år.</p>
    <p>Det som gjenstår: den samme automatiske loggingen i resten av suiten, og at selve lisensnumrene bor i <a href="@@SONGAPP@@">SundaySong</a> og SundayPlan. Er lisens det menigheten din trenger mest, si fra: <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''}},
 # ------------------------------------------------------------ 7 data & privacy
 "your-data-and-privacy":{"accent":"gold-deep",
  "en":{"tag":"Privacy","card":"Your data &amp; privacy",
    "desc":"Local-first by principle: what the desktop apps keep on your machine, what the web apps store, and how to get your data out — or gone.",
    "h1":"Your data &amp; privacy","sub":"What lives where, how to export it, and how to erase it.",
    "note":None,
    "body":'''    <p class="lead">Sunday Suite is built "local-first": your content belongs to you, stays with you, and leaves your control only when you actively choose it. Here is what that means in everyday terms — and which buttons to press.</p>
    <h2>Local-first by design</h2>
    <p>The desktop apps — like SundayRec, SundayScreen and SundaySync — do their work on your own machine. Recordings, pupil names, video and transcription are processed locally; nothing is uploaded unless you switch on a cloud or publishing feature yourself. There is no advertising and no tracking in the apps; where an app offers quality telemetry it is anonymous, optional and off until you say yes.</p>
    <h2>What the web apps store</h2>
    <p>The web apps — SundayInfo and SundayBooking — store what they must to do their job: your church's screens and boards, rooms and bookings. It is your church's data alone: row-level security in the database means each church can only ever see its own rows. Nothing is sold, shared or used for advertising.</p>
    <h2>Getting your data out — and gone</h2>
    <p>Your data is never locked in. Email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> to get a copy of your church's data from the web apps, or to have your Sunday account and everything stored for your church removed entirely. As the planning tools mature, self-service export and erasure are part of the design — store only what you need remains the house rule.</p>
    <h2>Cloud AI is off until you turn it on</h2>
    <p>Some features can use cloud-based AI. These are governed by a consent toggle that is <strong>off by default</strong> — nothing is sent to any AI service unless your church actively switches it on. Local AI, like the speech-to-text in SundayRec, runs entirely on your own machine either way.</p>
    <h2>Read the full policy</h2>
    <p>The complete picture — OAuth tokens, cloud uploads, your GDPR rights — is in the <a href="@@PRIVACY@@">Privacy Policy</a>. Questions about your data? Email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''},
  "no":{"tag":"Personvern","card":"Dine data &amp; personvern",
    "desc":"Lokalt først av prinsipp: hva skrivebordsappene beholder på maskinen din, hva web-appene lagrer, og hvordan du får dataene ut — eller bort.",
    "h1":"Dine data &amp; personvern","sub":"Hva som bor hvor, hvordan du eksporterer det, og hvordan du sletter det.",
    "note":None,
    "body":'''    <p class="lead">Sunday Suite er bygd «lokalt først»: innholdet ditt tilhører deg, blir hos deg, og forlater din kontroll bare når du aktivt velger det. Her er hva det betyr i praksis — og hvilke knapper du trykker på.</p>
    <h2>Lokalt først, etter design</h2>
    <p>Skrivebordsappene — som SundayRec, SundayScreen og SundaySync — gjør jobben sin på din egen maskin. Opptak, elevnavn, video og transkripsjon behandles lokalt; ingenting lastes opp med mindre du selv skrur på en sky- eller publiseringsfunksjon. Det er ingen reklame og ingen sporing i appene; der en app tilbyr kvalitetstelemetri, er den anonym, valgfri og av til du sier ja.</p>
    <h2>Hva web-appene lagrer</h2>
    <p>Web-appene — SundayInfo og SundayBooking — lagrer det de må for å gjøre jobben sin: menighetens skjermer og tavler, rom og bookinger. Det er menighetens data alene: rad-nivå sikkerhet i databasen gjør at hver menighet bare kan se sine egne rader. Ingenting selges, deles eller brukes til reklame.</p>
    <h2>Få dataene dine ut — og bort</h2>
    <p>Dataene dine er aldri innelåst. Send en e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> for å få en kopi av menighetens data fra web-appene, eller for å få Sunday-kontoen din og alt som er lagret for menigheten fjernet helt. Etter hvert som planleggingsverktøyene modnes, er selvbetjent eksport og sletting en del av designet — «lagre bare det du trenger» er fortsatt husregelen.</p>
    <h2>Sky-AI er av til du skrur den på</h2>
    <p>Noen funksjoner kan bruke skybasert AI. Disse styres av en samtykke-bryter som er <strong>av som standard</strong> — ingenting sendes til noen AI-tjeneste med mindre menigheten aktivt skrur det på. Lokal AI, som tale-til-tekst i SundayRec, kjører uansett helt på din egen maskin.</p>
    <h2>Les hele erklæringen</h2>
    <p>Hele bildet — OAuth-tokens, sky-opplastinger, GDPR-rettighetene dine — finner du i <a href="@@PRIVACY@@">Personvernerklæringen</a>. Spørsmål om dataene dine? Send e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''}},
 # ------------------------------------------------------------ community toolbox
 "community-toolbox":{"accent":"gold-deep",
  "en":{"tag":"Toolbox","card":"Using the community toolbox",
    "desc":"Eleven free browser tools for church and classroom — how to run one on the big screen, with everyone joining from their phones.",
    "h1":"Using the community toolbox","sub":"Free games and group tools — nothing to install, no accounts.",
    "note":"<strong>All free:</strong> every tool runs straight in the browser on <em>*.sundaysuite.app</em> — no installation, no account, no cost. The full list lives on the <a href=\"@@TOOLBOX@@\">toolbox page</a>.",
    "body":'''    <p class="lead">Alongside the core products, Sunday Suite keeps a toolbox of small, playful web tools for church and classroom — icebreakers, tournaments, a digital bazaar, anonymous Q&amp;A and more. They all follow the same recipe: open one on the big screen, and everyone joins from their own phone. Here is how to run one well.</p>
    <h2>How every tool works</h2>
    <p>Open the tool on a shared screen — a projector, a TV, a classroom smartboard. The screen shows a QR code or a short code; everyone joins by scanning or typing it on their phone. Nobody creates an account, nobody installs anything, and participants stay anonymous. When the session is over, it expires by itself.</p>
    <h2>Pick the right tool for the room</h2>
    <ul>
      <li><strong>A first gathering:</strong> <a href="https://quiz.sundaysuite.app" target="_blank" rel="noopener">SundayQuiz</a> — get-to-know-you bingo that warms a room up fast.</li>
      <li><strong>The classroom:</strong> <a href="https://chess.sundaysuite.app" target="_blank" rel="noopener">SundayChess</a> and <a href="https://tictactoe.sundaysuite.app" target="_blank" rel="noopener">SundayTicTacToe</a> — big-screen tournaments with Swiss rounds and a knockout.</li>
      <li><strong>Sports day or games night:</strong> <a href="https://turnering.sundaysuite.app" target="_blank" rel="noopener">SundayTurnering</a> — a live tournament board for any sport or game.</li>
      <li><strong>A group evening:</strong> <a href="https://marked.sundaysuite.app" target="_blank" rel="noopener">SundayMarket</a> (fast, friendly trading game) and <a href="https://harvest.sundaysuite.app" target="_blank" rel="noopener">SundayHarvest</a> (biblical social deduction — no one gets eliminated).</li>
      <li><strong>The fundraiser:</strong> <a href="https://basar.sundaysuite.app" target="_blank" rel="noopener">SundayBasar</a> — sell raffle tickets and draw prizes live on the big screen. The app never touches money; you confirm each Vipps payment yourself.</li>
      <li><strong>Youth night:</strong> <a href="https://panel.sundaysuite.app" target="_blank" rel="noopener">SundayPanel</a> — anonymous questions from the floor to a panel, with you curating what goes up.</li>
      <li><strong>Musicians:</strong> <a href="https://licks.sundaysuite.app" target="_blank" rel="noopener">SundayLicks</a> — a practice library of gospel and worship licks for piano, guitar and bass.</li>
      <li><strong>Newcomers:</strong> <a href="https://welcome.sundaysuite.app" target="_blank" rel="noopener">SundayWelcome</a> — a digital welcome note, so no first-time visitor falls through the cracks.</li>
      <li><strong>Learning:</strong> <a href="https://school.sundaysuite.app" target="_blank" rel="noopener">SundaySchool</a> — the church's own music and theology school, eleven subjects deep.</li>
    </ul>
    <h2>Tips for a smooth session</h2>
    <ul>
      <li><strong>Test five minutes before.</strong> Open the tool on the big screen and join from your own phone once, before the room fills up.</li>
      <li><strong>Check the wifi.</strong> Every phone in the room will be online at once — the venue's guest network should be up to it.</li>
      <li><strong>Read the code aloud.</strong> A QR on screen plus the short code spoken once gets even the least technical participant in.</li>
    </ul>
    <h2>What about privacy?</h2>
    <p>The tools are built to store as little as possible: participants are anonymous and sessions expire after use. The deliberate exception is SundayWelcome, which stores the contact details a newcomer chooses to leave so the church can follow up — see the <a href="@@PRIVACY@@">Privacy Policy</a> for the details.</p>
    <h2>The toolbox keeps growing</h2>
    <p>More fellowship tools are on the workbench. Have an idea for the next one — something your church or classroom actually needs? Tell us: <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''},
  "no":{"tag":"Verktøykassa","card":"Slik bruker du verktøykassa",
    "desc":"Elleve gratis nettleserverktøy for menighet og klasserom — slik kjører du ett på storskjermen, mens alle blir med fra mobilen.",
    "h1":"Slik bruker du verktøykassa","sub":"Gratis spill og gruppeverktøy — ingenting å installere, ingen kontoer.",
    "note":"<strong>Alt er gratis:</strong> hvert verktøy kjører rett i nettleseren på <em>*.sundaysuite.app</em> — ingen installasjon, ingen konto, ingen kostnad. Hele lista bor på <a href=\"@@TOOLBOX@@\">verktøykasse-siden</a>.",
    "body":'''    <p class="lead">Ved siden av kjerneproduktene holder Sunday Suite en verktøykasse med små, lekne nettverktøy for menighet og klasserom — bli-kjent-leker, turneringer, digital basar, anonyme spørsmål og mer. Alle følger samme oppskrift: åpne ett på storskjermen, så blir alle med fra sin egen mobil. Slik kjører du det godt.</p>
    <h2>Slik virker hvert verktøy</h2>
    <p>Åpne verktøyet på en delt skjerm — prosjektor, TV eller smartboard. Skjermen viser en QR-kode eller en kort kode; alle blir med ved å skanne eller taste den på mobilen. Ingen oppretter konto, ingen installerer noe, og deltakerne er anonyme. Når økta er over, utløper den av seg selv.</p>
    <h2>Velg riktig verktøy for rommet</h2>
    <ul>
      <li><strong>Første samling:</strong> <a href="https://quiz.sundaysuite.app" target="_blank" rel="noopener">SundayQuiz</a> — bli-kjent-bingo som tiner opp et rom på et blunk.</li>
      <li><strong>Klasserommet:</strong> <a href="https://chess.sundaysuite.app" target="_blank" rel="noopener">SundayChess</a> og <a href="https://tictactoe.sundaysuite.app" target="_blank" rel="noopener">SundayTicTacToe</a> — storskjermturneringer med sveitsiske runder og sluttspill.</li>
      <li><strong>Idrettsdag eller spillkveld:</strong> <a href="https://turnering.sundaysuite.app" target="_blank" rel="noopener">SundayTurnering</a> — live turneringstavle for hvilken som helst idrett eller lek.</li>
      <li><strong>Gruppekveld:</strong> <a href="https://marked.sundaysuite.app" target="_blank" rel="noopener">SundayMarket</a> (kjapt og vennlig handelsspill) og <a href="https://harvest.sundaysuite.app" target="_blank" rel="noopener">SundayHarvest</a> (bibelsk social deduction — ingen elimineres).</li>
      <li><strong>Basaren:</strong> <a href="https://basar.sundaysuite.app" target="_blank" rel="noopener">SundayBasar</a> — selg årer og trekk premiene live på storskjerm. Appen rører aldri penger; du bekrefter hver Vipps-betaling selv.</li>
      <li><strong>Ungdomskvelden:</strong> <a href="https://panel.sundaysuite.app" target="_blank" rel="noopener">SundayPanel</a> — anonyme spørsmål fra salen til et panel, der du velger hva som vises.</li>
      <li><strong>Musikerne:</strong> <a href="https://licks.sundaysuite.app" target="_blank" rel="noopener">SundayLicks</a> — øvingsbibliotek med gospel- og lovsang-licks for piano, gitar og bass.</li>
      <li><strong>Nykommere:</strong> <a href="https://welcome.sundaysuite.app" target="_blank" rel="noopener">SundayWelcome</a> — en digital velkomstlapp, så ingen førstegangsbesøkende faller mellom to stoler.</li>
      <li><strong>Læring:</strong> <a href="https://school.sundaysuite.app" target="_blank" rel="noopener">SundaySchool</a> — menighetens egen musikk- og teologiskole, elleve fag dyp.</li>
    </ul>
    <h2>Tips for en smidig økt</h2>
    <ul>
      <li><strong>Test fem minutter før.</strong> Åpne verktøyet på storskjermen og bli med fra din egen mobil én gang, før rommet fylles.</li>
      <li><strong>Sjekk wifien.</strong> Hver mobil i rommet skal på nett samtidig — gjestenettet bør tåle det.</li>
      <li><strong>Les koden høyt.</strong> QR på skjermen pluss kortkoden lest høyt én gang får med selv den minst tekniske deltakeren.</li>
    </ul>
    <h2>Hva med personvern?</h2>
    <p>Verktøyene er bygd for å lagre minst mulig: deltakerne er anonyme, og økter utløper etter bruk. Det bevisste unntaket er SundayWelcome, som lagrer kontaktinfoen en nykommer selv velger å legge igjen, slik at menigheten kan følge opp — se <a href="@@PRIVACY@@">Personvernerklæringen</a> for detaljene.</p>
    <h2>Verktøykassa vokser videre</h2>
    <p>Flere fellesskapsverktøy ligger på arbeidsbenken. Har du en idé til det neste — noe menigheten eller klasserommet ditt faktisk trenger? Si fra: <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''}},
 # ------------------------------------------------------------ 8 faq
 "faq":{"accent":"gold-deep",
  "en":{"tag":"FAQ","card":"Frequently asked questions",
    "desc":"Price, languages, browsers, offline use, who sees your data, how to delete everything — the short answers in one place.",
    "h1":"Frequently asked questions","sub":"The short answers, in one place.",
    "note":None,
    "body":'''    <p class="lead">The questions we get most often, answered briefly. If yours isn't here, email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> — a real person reads it.</p>
    <h2>What does it cost?</h2>
    <p>Nothing, for now. Everything that is available today — the web apps, the desktop betas and all the community tools — is free. Paid plans may come later, but any change will be communicated clearly and well in advance.</p>
    <h2>Which apps can I actually use today?</h2>
    <p>Seven products are in beta today. Five desktop apps download free for Mac and Windows — <strong>SundayRec</strong> (record the service), <strong>SundayScreen</strong> (classroom screen), <strong>SundayStage</strong> (presentation), <strong>SundaySync</strong> (multicam sync) and <strong>SundayEdit</strong> (captioning) — and two web apps run in the browser: <strong>SundayInfo</strong> (<a href="https://info.sundaysuite.app" target="_blank" rel="noopener">info.sundaysuite.app</a>) and <strong>SundayBooking</strong> (<a href="https://booking.sundaysuite.app" target="_blank" rel="noopener">booking.sundaysuite.app</a>). All the betas are gathered on the <a href="@@BUILD@@">Build with us</a> page. SundayStudio and SundayTranslate are in development; SundayPlan, SundaySong and SundayPaper are on the drawing board. Beyond the suite, eleven free community tools are live in the <a href="@@TOOLBOX@@">toolbox</a> — icebreakers, classroom chess, tournaments, a digital bazaar and more.</p>
    <h2>Is Sunday Suite really open source?</h2>
    <p>Yes — every public Sunday repository is MIT-licensed. The code lives on <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a>, free to read, run, learn from and fork. The Sunday names and the cross-and-gold mark are trademarks, so a fork needs its own name, but the code itself is yours to use. Want to join in? Start at <a href="@@BUILD@@">Build with us</a>.</p>
    <h2>Which languages are supported?</h2>
    <p>SundayRec ships in seven languages, including Norwegian Bokmål and Nynorsk. The rest of the suite speaks English and Norwegian first, with more languages as the tools mature. This website is in English and Norwegian.</p>
    <h2>Which browsers work with the web apps?</h2>
    <p>Any modern, up-to-date browser: Chrome, Edge, Firefox or Safari, on computer, tablet or phone. If your browser updates itself (most do), you're fine.</p>
    <h2>Who can see my church's data?</h2>
    <p>Only your church. In the web apps (SundayInfo, SundayBooking), row-level security in the database keeps every church's data separate. Content you create in the desktop apps stays on your own machine. We sell nothing and run no ads. More in <a href="your-data-and-privacy.html">Your data &amp; privacy</a>.</p>
    <h2>Does it work offline?</h2>
    <p>The desktop apps, yes: SundayRec records, edits and transcribes entirely on your machine, and SundayScreen is built to run with no internet at all. The web apps need a connection.</p>
    <h2>Is AI used on my data?</h2>
    <p>Local AI — like the sermon transcription in SundayRec — runs on your own machine and uploads nothing. Features that would use cloud AI sit behind a consent toggle that is off by default.</p>
    <h2>Can I delete everything?</h2>
    <p>Yes. Email us to have your Sunday account and your church's data in the web apps removed entirely. Files from the desktop apps live on your own disk — deleting them is up to you, as it should be.</p>
    <h2>How do I get help?</h2>
    <p>Email <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. There is no call centre and no ticket robot — your message lands with the people building the suite, and we answer every email.</p>'''},
  "no":{"tag":"FAQ","card":"Ofte stilte spørsmål",
    "desc":"Pris, språk, nettlesere, frakoblet bruk, hvem som ser dataene dine, hvordan du sletter alt — de korte svarene samlet.",
    "h1":"Ofte stilte spørsmål","sub":"De korte svarene, samlet på ett sted.",
    "note":None,
    "body":'''    <p class="lead">Spørsmålene vi får oftest, besvart kort. Står ikke ditt her, send en e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a> — et ekte menneske leser den.</p>
    <h2>Hva koster det?</h2>
    <p>Ingenting, foreløpig. Alt som er tilgjengelig i dag — web-appene, skrivebords-betaene og alle fellesskapsverktøyene — er gratis. Betalte planer kan komme senere, men eventuelle endringer kommuniseres tydelig og i god tid.</p>
    <h2>Hvilke apper kan jeg faktisk bruke i dag?</h2>
    <p>Sju produkter er i beta i dag. Fem skrivebordsapper kan lastes ned gratis for Mac og Windows — <strong>SundayRec</strong> (ta opp gudstjenesten), <strong>SundayScreen</strong> (klasseromsskjerm), <strong>SundayStage</strong> (presentasjon), <strong>SundaySync</strong> (multikam-synk) og <strong>SundayEdit</strong> (teksting) — og to web-apper kjører i nettleseren: <strong>SundayInfo</strong> (<a href="https://info.sundaysuite.app" target="_blank" rel="noopener">info.sundaysuite.app</a>) og <strong>SundayBooking</strong> (<a href="https://booking.sundaysuite.app" target="_blank" rel="noopener">booking.sundaysuite.app</a>). Alle betaene er samlet på <a href="@@BUILD@@">Bygg med oss</a>-siden. SundayStudio og SundayTranslate er under utvikling; SundayPlan, SundaySong og SundayPaper er på tegnebrettet. Utenfor suiten er elleve gratis fellesskapsverktøy live i <a href="@@TOOLBOX@@">verktøykassa</a> — bli-kjent-leker, klasseromssjakk, turneringer, digital basar og mer.</p>
    <h2>Er Sunday Suite virkelig åpen kildekode?</h2>
    <p>Ja — hvert offentlige Sunday-repositorium er MIT-lisensiert. Koden bor på <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a>, fri til å leses, kjøres, læres av og forkes. Sunday-navnene og kors-og-gull-merket er varemerker, så en fork trenger sitt eget navn, men selve koden er din å bruke. Vil du være med? Start på <a href="@@BUILD@@">Bygg med oss</a>.</p>
    <h2>Hvilke språk støttes?</h2>
    <p>SundayRec leveres på sju språk, inkludert bokmål og nynorsk. Resten av suiten snakker engelsk og norsk først, med flere språk etter hvert som verktøyene modnes. Dette nettstedet finnes på engelsk og norsk.</p>
    <h2>Hvilke nettlesere fungerer med web-appene?</h2>
    <p>Alle moderne, oppdaterte nettlesere: Chrome, Edge, Firefox eller Safari, på PC, nettbrett eller mobil. Oppdaterer nettleseren din seg selv (det gjør de fleste), er du i mål.</p>
    <h2>Hvem kan se menighetens data?</h2>
    <p>Bare din menighet. I web-appene (SundayInfo, SundayBooking) holder rad-nivå sikkerhet i databasen hver menighets data adskilt. Innhold du lager i skrivebordsappene blir på din egen maskin. Vi selger ingenting og kjører ingen reklame. Mer i <a href="your-data-and-privacy.html">Dine data &amp; personvern</a>.</p>
    <h2>Fungerer det uten internett?</h2>
    <p>Skrivebordsappene, ja: SundayRec tar opp, redigerer og transkriberer helt på din maskin, og SundayScreen er bygd for å kjøre helt uten nett. Web-appene trenger internettforbindelse.</p>
    <h2>Brukes AI på dataene mine?</h2>
    <p>Lokal AI — som preken-transkripsjonen i SundayRec — kjører på din egen maskin og laster ikke opp noe. Funksjoner som ville brukt sky-AI, ligger bak en samtykke-bryter som er av som standard.</p>
    <h2>Kan jeg slette alt?</h2>
    <p>Ja. Send oss en e-post for å få Sunday-kontoen din og menighetens data i web-appene fjernet helt. Filer fra skrivebordsappene ligger på din egen disk — å slette dem er opp til deg, slik det skal være.</p>
    <h2>Hvordan får jeg hjelp?</h2>
    <p>Send e-post til <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. Det finnes ikke noe kundesenter og ingen billettrobot — meldingen din lander hos dem som bygger suiten, og vi svarer på hver e-post.</p>'''}},
}

def help_fill(s, L):
    return (s.replace("@@PRIVACY@@", L["legal"]("privacy"))
             .replace("@@RECAPP@@",  L["app"]("sundayrec"))
             .replace("@@SCREENAPP@@", L["app"]("sundayscreen"))
             .replace("@@SONGAPP@@", L["app"]("sundaysong"))
             .replace("@@INFOAPP@@", L["app"]("sundayinfo"))
             .replace("@@BOOKINGAPP@@", L["app"]("sundaybooking"))
             .replace("@@TOOLBOX@@", L["toolbox"])
             .replace("@@BUILD@@", L["build"]))

def render_help_index(lang):
    c=CH[lang]; root="../" if lang=="en" else "../../"; L=links(lang,root)
    other = "../no/hjelp/index.html" if lang=="en" else "../../help/index.html"
    hi=HELP_INDEX[lang]; arrow=sv("arrow","2.5")
    cards=""
    for slug in HELP_ORDER:
        doc=HELPDOC[slug]; d=doc[lang]
        cards+=(f'    <a class="card link" style="--c:var(--{doc["accent"]})" href="{slug}.html">'
          f'<h3 style="font-size:22px">{d["card"]}</h3><div class="tag">{d["tag"]}</div>'
          f'<p>{d["desc"]}</p><span class="more">{hi["read"]}{arrow}</span></a>\n')
    content=f'''<main>
<section class="legal-hero"><div class="glow"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><span>{hi["crumb"]}</span></div>
  <h1>{hi["h1"]}</h1>
  <p style="margin-top:18px; max-width:62ch; font-size:17px; color:var(--txt-on-ink-dim)">{hi["lead"]}</p>
</div></section>
<section class="legal-body"><div class="wrap wide">
  <div class="grid">
{cards}  </div>
  <div class="note" style="margin-top:44px"><p>{hi["contact"]} <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a></p></div>
</div></section>
</main>'''
    return shell(c,L,other,hi["title"],hi["meta"],'',content,navscrolled=True,pair=("help/index.html","no/hjelp/index.html"))

def render_help_article(lang, slug):
    c=CH[lang]; root="../" if lang=="en" else "../../"; L=links(lang,root)
    other = (f'../no/hjelp/{slug}.html' if lang=="en" else f'../../help/{slug}.html')
    doc=HELPDOC[slug]; d=doc[lang]; hi=HELP_INDEX[lang]
    note=f'<div class="note"><p>{help_fill(d["note"], L)}</p></div>\n  ' if d.get("note") else ""
    body=help_fill(d["body"], L)
    content=f'''<main>
<section class="legal-hero"><div class="glow"></div><div class="wrap">
  <div class="crumb"><a href="{L["home"]}">Sunday Suite</a><span>/</span><a href="index.html">{hi["crumb"]}</a><span>/</span><span>{d["tag"]}</span></div>
  <h1>{d["h1"]}</h1><div class="updated">{d["sub"]}</div>
</div></section>
<section class="legal-body"><div class="wrap">
  {note}<div class="prose">
{body}
    <p style="margin-top:40px"><a href="index.html">{c["back_help"]}</a> &middot; <a href="{L["home"]}">Sunday Suite</a></p>
  </div>
</div></section>
</main>'''
    title=f'{d["h1"]} — {hi["crumb"]} | Sunday Suite'
    return shell(c,L,other,title,d["desc"],'',content,navscrolled=True,pair=(f"help/{slug}.html",f"no/hjelp/{slug}.html"))

# ===================================================================== WRITE
def W(path, html):
    full=os.path.join(ROOTDIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(html)
    print("wrote", path)

def page_pairs():
    """(EN html path, NO html path) for every page — drives hreflang and the sitemap."""
    pairs=[("index.html","no/index.html"),("toolbox.html","no/verktoykasse.html"),("build.html","no/bygg.html")]
    pairs+=[(f"apps/{s}.html", f"no/apps/{s}.html") for s in SLUGS]
    pairs+=[("legal/terms.html","no/legal/terms.html"),("legal/privacy.html","no/legal/privacy.html")]
    pairs+=[("help/index.html","no/hjelp/index.html")]
    pairs+=[(f"help/{hs}.html", f"no/hjelp/{hs}.html") for hs in HELP_ORDER]
    return pairs

def sitemap_xml():
    rows=[]
    for en,no in page_pairs():
        eu, nu = clean_url(en), clean_url(no)
        alts=(f'<xhtml:link rel="alternate" hreflang="en" href="{eu}"/>'
              f'<xhtml:link rel="alternate" hreflang="no" href="{nu}"/>'
              f'<xhtml:link rel="alternate" hreflang="x-default" href="{eu}"/>')
        for own in (eu, nu):
            rows.append(f'  <url><loc>{own}</loc>{alts}</url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")

for lang in ("en","no"):
    pre = "" if lang=="en" else "no/"
    hpre = "help/" if lang=="en" else "no/hjelp/"
    W(pre+"index.html", render_home(lang))
    W(pre+("toolbox.html" if lang=="en" else "verktoykasse.html"), render_toolbox_page(lang))
    W(pre+("build.html" if lang=="en" else "bygg.html"), render_build_page(lang))
    for s in SLUGS:
        W(pre+f"apps/{s}.html", render_app(lang,s))
    W(pre+"legal/terms.html",   terms_en()   if lang=="en" else terms_no())
    W(pre+"legal/privacy.html", privacy_en() if lang=="en" else privacy_no())
    W(hpre+"index.html", render_help_index(lang))
    for hs in HELP_ORDER:
        W(hpre+f"{hs}.html", render_help_article(lang,hs))
W("sitemap.xml", sitemap_xml())
W("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
W("_redirects", "".join(f"/help/{s} /help/ 301\n/no/hjelp/{s} /no/hjelp/ 301\n" for s in REMOVED_HELP))
print("done")
