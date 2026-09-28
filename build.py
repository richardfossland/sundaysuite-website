#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sunday Suite — static site generator for sundaysuite.app.

Norwegian at the site root, English under /en/. Standard library only:

    python3 build.py && python3 check_links.py

All program text lives in PROGRAMS below; UI strings in T; legal text in legal.py.
Links between pages are relative and extensionless, matching how Cloudflare
Pages serves the files (apps/sundayrec.html is served at /apps/sundayrec).
"""
import os
import posixpath
import re

import legal

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
SITE = "https://sundaysuite.app"
EMAIL = "dev@sundaysuite.app"
GITHUB_ORG = "https://github.com/SundaySuite-app"
# Vipps: the business number plus the official QR Vipps generated
# (assets/vipps-qr.png). Vipps documents no stable public "pay to number" link,
# so there is deliberately no payment URL.
VIPPS = {"number": "24288", "name": "Fossland Media"}

LANGS = ("no", "en")
PREFIX = {"no": "", "en": "en/"}
HTML_LANG = {"no": "nb", "en": "en"}

# ----------------------------------------------------------------- programs
# group: "download" (beta, direct download) · "web" (open in the browser) ·
#        "dev" (in development).
# parked: True moves the program out of the main lists into the collapsed
#       "not a priority" section at the bottom of the front page. It keeps its
#       page and its group's action (Open link, source link).
# logo: True uses assets/logos/<slug>.svg; otherwise a flat tile in `color`
#       with the `glyph` below.
# testbuild: "aarch64" or "universal" — the /download/<slug>/{mac,windows}
#       Pages Functions serve an unfinished test build; the program page links
#       to it quietly. Never linked from the front page.
# repo: only repositories with a licence file are linked as source code.
# Body blocks: a string is a paragraph, a list is a bullet list. "@PRIVACY@"
# becomes a link to the privacy policy.
PROGRAMS = [
 {"slug": "sundayrec", "name": "SundayRec", "group": "download", "logo": True,
  "repo": "SundaySuite-app/sundayrec",
  "no": {"line": "Tar opp gudstjenesten automatisk etter en tidsplan, og kan strømme den direkte og legge den ut som podkast.",
         "body": ["SundayRec er et program for Mac og Windows. Du legger inn når gudstjenestene er, så starter og stopper opptaket av seg selv.",
                  ["Planlagt opptak av lyd og bilde",
                   "Direktestrømming til YouTube, Facebook og andre tjenester som tar imot RTMP",
                   "Talen skrives ut som tekst på din egen maskin",
                   "Enkel lydredigering og jevn lydstyrke før publisering",
                   "Tar imot bilde og lyd over nettverket med NDI, for eksempel fra ProPresenter eller OBS",
                   "Opplasting til YouTube og podkast-RSS, med gjennomsyn før noe publiseres"],
                  "Opptakene blir liggende på maskinen din. Ingenting lastes opp med mindre du selv slår på strømming, sikkerhetskopi eller publisering. Programmet finnes på sju språk, blant annet bokmål og nynorsk.",
                  "SundayRec er i beta. Test noen opptak før du bruker det til en viktig gudstjeneste."]},
  "en": {"line": "Records the church service automatically on a schedule, and can stream it live and publish it as a podcast.",
         "body": ["SundayRec is a program for Mac and Windows. You enter when the services are, and recording starts and stops by itself.",
                  ["Scheduled audio and video recording",
                   "Live streaming to YouTube, Facebook and other services that accept RTMP",
                   "The sermon is transcribed on your own computer",
                   "Simple audio editing and even loudness before publishing",
                   "Receives video and audio over the network with NDI, for example from ProPresenter or OBS",
                   "Upload to YouTube and a podcast RSS feed, with a review step before anything is published"],
                  "Recordings stay on your computer. Nothing is uploaded unless you turn on streaming, backup or publishing yourself. The program is available in seven languages, including Norwegian Bokmål and Nynorsk.",
                  "SundayRec is in beta. Test a few recordings before you rely on it for an important service."]}},

 # ---- web programs
 {"slug": "sundayinfo", "parked": True, "name": "SundayInfo", "group": "web", "logo": True,
  "url": "https://info.sundaysuite.app",
  "no": {"line": "Infoskjerm for kirka. Viser gudstjenestetider, kunngjøringer, vær og et bibelvers på en TV.",
         "body": ["Skjermen kan være en TV med nettleser, en Chromecast, en PC eller en Raspberry Pi. Du kobler den til med en kode og redigerer innholdet fra mobil eller PC. Flere personer kan redigere.",
                  "Utseendet følger kirkeåret. Hvis nettet faller ut, fortsetter skjermen å vise det siste innholdet.",
                  "Du logger inn med en Sunday-konto."]},
  "en": {"line": "An information screen for the church. Shows service times, notices, weather and a Bible verse on a TV.",
         "body": ["The screen can be a TV with a browser, a Chromecast, a PC or a Raspberry Pi. You connect it with a code and edit the content from a phone or computer. Several people can edit.",
                  "The look follows the church year. If the network drops, the screen keeps showing the latest content.",
                  "You sign in with a Sunday account."]}},
 {"slug": "sundaybooking", "parked": True, "name": "SundayBooking", "group": "web", "logo": True,
  "url": "https://booking.sundaysuite.app",
  "no": {"line": "Booking av rom, utstyr og avtaler i menigheten, uten dobbeltbooking.",
         "body": ["Stab og frivillige booker rom og utstyr i en felles kalender. Kalenderen tillater ikke to bookinger på samme tid, heller ikke når det er satt av tid til rigging og rydding.",
                  "Folk utenfra kan be om å leie via en lenke, uten å lage konto. Forespørslene havner i en kø som staben godkjenner eller avslår.",
                  "Kalenderen for hvert rom kan abonneres på (ICS). Du logger inn med en Sunday-konto."]},
  "en": {"line": "Booking of rooms, equipment and appointments for the church, without double bookings.",
         "body": ["Staff and volunteers book rooms and equipment in a shared calendar. The calendar does not allow two bookings at the same time, including the time set aside for setting up and clearing away.",
                  "People from outside can ask to rent through a link, without creating an account. Requests go into a queue that the staff approve or decline.",
                  "Each room's calendar can be subscribed to (ICS). You sign in with a Sunday account."]}},
 {"slug": "sundaywelcome", "parked": True, "name": "SundayWelcome", "group": "web", "glyph": "welcome", "color": "#C96A50",
  "url": "https://welcome.sundaysuite.app",
  "no": {"line": "Digital velkomstlapp for nye besøkende, så menigheten kan følge dem opp.",
         "body": ["Den besøkende skanner en QR-kode, for eksempel på en lapp i benken eller på en skjerm, og fyller ut et kort skjema på sin egen mobil. Teamet i menigheten ser svarene og kan ta kontakt.",
                  "Opplysningene tilhører menigheten. Se <a href=\"@PRIVACY@\">personvernerklæringen</a>."]},
  "en": {"line": "A digital welcome card for first-time visitors, so the church can follow up.",
         "body": ["The visitor scans a QR code, for example on a card in the pew or on a screen, and fills in a short form on their own phone. The church team sees the answers and can get in touch.",
                  "The details belong to the church. See the <a href=\"@PRIVACY@\">privacy policy</a>."]}},
 {"slug": "sundaybasar", "name": "SundayBasar", "group": "web", "glyph": "basar", "color": "#CF4C86",
  "url": "https://basar.sundaysuite.app",
  "no": {"line": "Digital basar. Selg lodd og trekk premiene på storskjerm.",
         "body": ["Betalingen skjer i Vipps, direkte til arrangøren. Programmet håndterer ikke penger: arrangøren bekrefter selv hver betaling.",
                  "Trekningen vises på storskjerm."]},
  "en": {"line": "A digital church bazaar. Sell raffle tickets and draw the prizes on the big screen.",
         "body": ["Payment happens in Vipps, directly to the organiser. The program does not handle money: the organiser confirms each payment.",
                  "The draw is shown on the big screen."]}},
 {"slug": "sundaypanel", "name": "SundayPanel", "group": "web", "glyph": "panel", "color": "#2E9E8F",
  "url": "https://panel.sundaysuite.app",
  "no": {"line": "Anonyme spørsmål fra salen til et panel, vist på storskjerm.",
         "body": ["Publikum sender spørsmål fra mobilen med en ordkode eller QR-kode. De trenger ingen app og ingen innlogging.",
                  "Den som leder, velger hvilke spørsmål som vises på skjermen."]},
  "en": {"line": "Anonymous questions from the audience to a panel, shown on the big screen.",
         "body": ["The audience sends questions from their phones using a word code or a QR code. No app and no sign-in.",
                  "The person leading chooses which questions are shown on the screen."]}},
 {"slug": "sundayschool", "name": "SundaySchool", "group": "web", "glyph": "school", "color": "#3D8B66",
  "url": "https://school.sundaysuite.app", "repo": "richardfossland/sundayschool",
  "no": {"line": "Musikk- og teologiskole for menigheten, med undervisning i elleve fag.",
         "body": ["Fagene er blant annet piano, gitar, bass, trommer, lovsangsledelse, bladspill, rytme, lydteknikk og teologi.",
                  "Skolen har et bibliotek med 51 salmer i 104 arrangementer som kan spilles av. Rettighetene til dem er avklart."]},
  "en": {"line": "A music and theology school for the church, with lessons in eleven subjects.",
         "body": ["The subjects include piano, guitar, bass, drums, leading worship, sight-reading, rhythm, sound engineering and theology.",
                  "The school has a library of 51 hymns in 104 arrangements that can be played back. The rights to them have been cleared."]}},
 {"slug": "sundaylicks", "name": "SundayLicks", "group": "web", "glyph": "licks", "color": "#E8A33D",
  "url": "https://licks.sundaysuite.app",
  "no": {"line": "Øvingsbibliotek med gospel- og lovsangslicks for piano, gitar og bass.",
         "body": ["Du kan endre tempo og transponere til hvilken som helst toneart mens du øver.",
                  "Alt spilles av fra noter, ikke fra lydfiler."]},
  "en": {"line": "A practice library of gospel and worship licks for piano, guitar and bass.",
         "body": ["You can change the tempo and transpose to any key while you practise.",
                  "Everything is played from notation, not from audio files."]}},
 {"slug": "sundayquiz", "name": "SundayQuiz", "group": "web", "glyph": "quiz", "color": "#FF8A5C",
  "url": "https://quiz.sundaysuite.app",
  "no": {"line": "Bli-kjent-bingo for første samling.",
         "body": ["Alle får et brett med ruter og skal finne folk i rommet som passer til rutene. Det tar rundt fem minutter og passer for alle slags grupper."]},
  "en": {"line": "Get-to-know-you bingo for a first gathering.",
         "body": ["Everyone gets a card of squares and looks for people in the room who match them. It takes about five minutes and works for any kind of group."]}},
 {"slug": "sundaychess", "name": "SundayChess", "group": "web", "glyph": "chess", "color": "#7C5CCB",
  "url": "https://chess.sundaysuite.app", "repo": "richardfossland/sundaychess",
  "no": {"line": "Sjakkturnering for klasserommet, styrt fra én skjerm.",
         "body": ["Turneringen går med sveitsiske runder og sluttspill, og stillingen vises på storskjerm. Elevene kan spille alene eller på lag.",
                  "Det finnes også en datamotstander å øve mot."]},
  "en": {"line": "A chess tournament for the classroom, run from one screen.",
         "body": ["The tournament uses Swiss rounds and a knockout, and the standings are shown on the big screen. Pupils can play alone or in teams.",
                  "There is also a computer opponent to practise against."]}},
 {"slug": "sundaytictactoe", "name": "SundayTicTacToe", "group": "web", "glyph": "tictactoe", "color": "#4C63D2",
  "url": "https://tictactoe.sundaysuite.app",
  "no": {"line": "Bondesjakk som turnering for klasserommet.",
         "body": ["Brettet kan være 3×3, 4×4 eller 5×5. Turneringen går med sveitsiske runder og sluttspill, styrt fra én skjerm.",
                  "Det finnes også en datamotstander å øve mot."]},
  "en": {"line": "Tic-tac-toe as a tournament for the classroom.",
         "body": ["The board can be 3×3, 4×4 or 5×5. The tournament uses Swiss rounds and a knockout, run from one screen.",
                  "There is also a computer opponent to practise against."]}},
 {"slug": "sundayturnering", "name": "SundayTurnering", "group": "web", "glyph": "trophy", "color": "#E07A2F",
  "url": "https://turnering.sundaysuite.app",
  "no": {"line": "Turneringstavle for idrett og spill, med serie, cup og sluttspill.",
         "body": ["Resultatene føres fra mobilen og vises på storskjerm. Den kan brukes til hvilken som helst idrett eller lek."]},
  "en": {"line": "A tournament board for sports and games, with league, cup and playoffs.",
         "body": ["Results are entered from a phone and shown on the big screen. It works for any sport or game."]}},
 {"slug": "sundaymarket", "name": "SundayMarket", "group": "web", "glyph": "trade", "color": "#C9952F",
  "url": "https://marked.sundaysuite.app",
  "no": {"line": "Handelsspill for en gruppe, spilt i raske runder.",
         "body": ["Deltakerne kjøper og selger varer seg imellom og prøver å komme best ut før tida er ute. Underveis kan det komme hungersnød."]},
  "en": {"line": "A trading game for a group, played in quick rounds.",
         "body": ["Players buy and sell goods between themselves and try to come out ahead before time runs out. A famine may strike along the way."]}},
 {"slug": "sundayharvest", "name": "SundayHarvest", "group": "web", "glyph": "wheat", "color": "#7BA23F",
  "url": "https://harvest.sundaysuite.app",
  "no": {"line": "Selskapsspill om hveten og ugresset (Matteus 13).",
         "body": ["Et spill for 5–10 spillere der man skal finne ut hvem som er hvem. Ingen blir slått ut underveis, så alle er med til slutt."]},
  "en": {"line": "A party game about the wheat and the weeds (Matthew 13).",
         "body": ["A game for 5–10 players about working out who is who. Nobody is knocked out along the way, so everyone plays to the end."]}},

 # ---- in development
 {"slug": "sundayscreen", "name": "SundayScreen", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundayscreen", "testbuild": "aarch64",
  "no": {"line": "Klasseromsskjerm uten nett, med klokke, nedtelling, navnetrekker, grupper og beskjeder.",
         "body": ["Et program for Mac og Windows. Læreren setter opp på forhånd hva skjermen skal vise i hver time, for eksempel klokke, nedtelling, trafikklys, en lenke med QR-kode eller et bilde.",
                  "Hver klasse har sin egen navneliste og sine egne oppsett. Alt kjører på maskinen, uten konto og uten nett."]},
  "en": {"line": "An offline classroom screen with a clock, countdown, name picker, groups and messages.",
         "body": ["A program for Mac and Windows. The teacher sets up in advance what the screen shows in each lesson, for example a clock, a countdown, a traffic light, a link with a QR code or a picture.",
                  "Each class has its own name list and its own layouts. Everything runs on the computer, with no account and no internet."]}},
 {"slug": "sundaystage", "name": "SundayStage", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundaystage", "testbuild": "aarch64",
  "no": {"line": "Viser sangtekster, bibelvers og bilder på storskjermen i kirka.",
         "body": ["Et program for Mac og Windows, i samme kategori som ProPresenter. Du setter opp rekkefølgen for gudstjenesten på forhånd og styrer den med tastaturet.",
                  "Det menigheten ser, kan låses, slik at et feiltrykk ikke havner på skjermen. Programmet fører også en logg over sangene som ble vist, med CCLI- og TONO-opplysninger, til bruk i rapporteringen."]},
  "en": {"line": "Shows lyrics, Bible verses and images on the big screen in church.",
         "body": ["A program for Mac and Windows, in the same category as ProPresenter. You set up the order of the service in advance and run it from the keyboard.",
                  "What the congregation sees can be locked, so a wrong click does not end up on the screen. The program also keeps a log of the songs that were shown, with CCLI and TONO details, for reporting."]}},
 {"slug": "sundayedit", "name": "SundayEdit", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundayedit", "testbuild": "universal",
  "no": {"line": "Teksting av video. Talen skrives ut automatisk, og du retter det programmet er usikker på.",
         "body": ["Hvert ord blir fargemerket etter hvor sikker gjenkjenningen er, så du kan gå rett til ordene som bør sjekkes. Du kan legge inn navn og ord som går igjen.",
                  "Gjenkjenningen kjører på din egen maskin, og videoen lastes ikke opp. Tekstene kan eksporteres som SRT, VTT, ASS og TXT."]},
  "en": {"line": "Video captioning. Speech is transcribed automatically, and you correct what the program is unsure of.",
         "body": ["Each word is coloured by how confident the recognition is, so you can go straight to the words worth checking. You can add names and words that come up often.",
                  "Recognition runs on your own computer, and the video is not uploaded. Captions can be exported as SRT, VTT, ASS and TXT."]}},
 {"slug": "sundaysync", "name": "SundaySync", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundaysync", "testbuild": "aarch64",
  "no": {"line": "Synkroniserer opptak fra flere kameraer ved hjelp av lyden, og lager en tidslinje for DaVinci Resolve.",
         "body": ["Du legger inn filene fra kameraer, mobiler og lydopptakere. Programmet sammenligner lyden i klippene og plasserer dem riktig i forhold til hverandre, uten timekode eller klapper.",
                  "Resultatet eksporteres som FCPXML, som kan åpnes i DaVinci Resolve. Alt skjer lokalt på maskinen."]},
  "en": {"line": "Syncs recordings from several cameras using their audio, and builds a timeline for DaVinci Resolve.",
         "body": ["You add the files from cameras, phones and audio recorders. The program compares the audio in the clips and lines them up with each other, without timecode or a clapper.",
                  "The result is exported as FCPXML, which opens in DaVinci Resolve. Everything happens locally on the computer."]}},
 {"slug": "sundaystudio", "name": "SundayStudio", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundaystudio",
  "no": {"line": "Podkastproduksjon med flere mikrofoner, redigering og ferdig MP3.",
         "body": ["Et program for å ta opp flere mikrofoner samtidig, jevne ut lyden, klippe og eksportere en ferdig podkastepisode med riktig lydstyrke. Det skal også kunne lage en kort kjenningsmelodi."]},
  "en": {"line": "Podcast production with several microphones, editing and a finished MP3.",
         "body": ["A program for recording several microphones at once, evening out the sound, editing and exporting a finished podcast episode at the right loudness. It is also meant to make a short theme tune."]}},
 {"slug": "sundaytranslate", "name": "SundayTranslate", "group": "dev", "logo": True,
  "repo": "SundaySuite-app/sundaytranslate",
  "no": {"line": "Tolking av gudstjenesten rett til mobilen, og bedre lyd for dem som hører dårlig.",
         "body": ["En tolk snakker inn i sin mobil, og de som lytter, hører tolkingen i egne ørepropper, omtrent ett sekund forsinket. Den samme løsningen kan sende romlyden rett til mobilen for dem som hører dårlig, og vise undertekster.",
                  "Lytterne blir med via en kode eller en QR-kode, uten app og uten konto. Det blir et nettprogram."]},
  "en": {"line": "Interpretation of the service straight to people's phones, and clearer sound for the hard of hearing.",
         "body": ["An interpreter speaks into their phone, and listeners hear the interpretation in their own earphones, about a second behind. The same setup can send the room sound straight to the phones of people who hear poorly, and show subtitles.",
                  "Listeners join with a code or a QR code, with no app and no account. It will be a web program."]}},
 {"slug": "sundayplan", "parked": True, "name": "SundayPlan", "group": "dev", "logo": True,
  "no": {"line": "Planlegging av gudstjenester og vaktlister for frivillige.",
         "body": ["Målet er å samle gudstjenesteplanen, rollene og de frivillige på ett sted, med forslag til en rettferdig vaktliste og påminnelser på SMS og e-post. Arbeidet er i en tidlig fase."]},
  "en": {"line": "Service planning and rotas for volunteers.",
         "body": ["The aim is to keep the service plan, the roles and the volunteers in one place, with suggestions for a fair rota and reminders by text message and email. The work is at an early stage."]}},
 {"slug": "sundaysong", "parked": True, "name": "SundaySong", "group": "dev", "logo": True,
  "no": {"line": "Sangdatabase med opplysningene som trengs til TONO og CCLI.",
         "body": ["Målet er en sangdatabase der du kan søke på tema og ikke bare tittel, og der hver sang har med opplysningene som trengs for rapportering til TONO og CCLI. Arbeidet er i en tidlig fase."]},
  "en": {"line": "A song database with the details needed for TONO and CCLI.",
         "body": ["The aim is a song database you can search by theme and not only by title, where each song carries the details needed for reporting to TONO and CCLI. The work is at an early stage."]}},
 {"slug": "sundaypaper", "parked": True, "name": "SundayPaper", "group": "dev", "logo": True,
  "no": {"line": "Verktøy for trykksaker som gudstjenesteprogram, menighetsblad og storskrift.",
         "body": ["Målet er et program for å lage gudstjenesteprogram, menighetsblad, storskriftutgaver og skjemaer, og for å dele skannede sangbøker opp i enkeltsanger. Arbeidet er i en tidlig fase."]},
  "en": {"line": "A tool for print, such as service programmes, parish magazines and large print.",
         "body": ["The aim is a program for making service programmes, parish magazines, large-print editions and forms, and for splitting scanned songbooks into single songs. The work is at an early stage."]}},
]
BY = {p["slug"]: p for p in PROGRAMS}
GROUPS = ("download", "web", "dev")

# Line icons for the web programs that have no app-icon file (24×24, stroked).
GLYPH = {
 "quiz": '<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9h18M9 3v18"/><path d="M12.5 13.5l1.5 1.5 3-3.5"/>',
 "chess": '<circle cx="12" cy="5.5" r="2.5"/><path d="M9.5 8.5h5l-1 5h-3z"/><path d="M7 21h10l-1.5-4.5h-7z"/>',
 "trophy": '<path d="M7 4h10v4.5a5 5 0 0 1-10 0z"/><path d="M7 6.5H4.5v1a3 3 0 0 0 3 3M17 6.5h2.5v1a3 3 0 0 1-3 3"/><path d="M12 13.5V17M9 21h6M10.5 17h3"/>',
 "trade": '<path d="M3.5 8.5h13l-3.2-3.2M20.5 15.5h-13l3.2 3.2"/>',
 "wheat": '<path d="M12 21.5V8.5"/><path d="M12 8.5c2.1 0 3.6-1.6 3.6-3.6C13.5 4.9 12 6.5 12 8.5zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 4.9 12 6.5 12 8.5z"/><path d="M12 13c2.1 0 3.6-1.6 3.6-3.6C13.5 9.4 12 11 12 13zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 9.4 12 11 12 13z"/><path d="M12 17.5c2.1 0 3.6-1.6 3.6-3.6C13.5 13.9 12 15.5 12 17.5zm0 0c-2.1 0-3.6-1.6-3.6-3.6C10.5 13.9 12 15.5 12 17.5z"/>',
 "tictactoe": '<path d="M9 3v18M15 3v18M3 9h18M3 15h18"/><path d="M4.7 4.7l2.6 2.6M7.3 4.7L4.7 7.3"/><circle cx="18" cy="18" r="1.9"/>',
 "basar": '<circle cx="12" cy="13" r="8.2"/><path d="M12 4.8v16.4M3.8 13h16.4M6.2 7.2l11.6 11.6M17.8 7.2L6.2 18.8"/><circle cx="12" cy="13" r="1.3" fill="currentColor" stroke="none"/><path d="M12 1.6l2.3 3.2h-4.6z" fill="currentColor" stroke="none"/>',
 "panel": '<path d="M21 4H3a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h4v4l5-4h9a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1z"/><path d="M9.6 9.2a2.4 2.4 0 1 1 3.1 2.5c-.8.3-1.2.8-1.2 1.5v.3"/><path d="M11.5 15.4v.3"/>',
 "licks": '<rect x="3" y="5.5" width="18" height="13" rx="1.6"/><path d="M8 5.5v13M12.5 5.5v13M17 5.5v13"/><rect x="6.8" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/><rect x="11.3" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/><rect x="15.8" y="5.5" width="2.4" height="6" rx="0.5" fill="currentColor" stroke="none"/>',
 "welcome": '<path d="M13.5 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h7.5"/><path d="M13.5 21l5.5-1.8V4.8L13.5 3z"/><circle cx="15.6" cy="12" r="0.9" fill="currentColor" stroke="none"/><path d="M8 12h3M9.7 10.3L8 12l1.7 1.7"/>',
 "school": '<path d="M12 3.5 2.5 8 12 12.5 21.5 8 12 3.5z"/><path d="M6 10.4V15c0 1.6 2.7 3 6 3s6-1.4 6-3v-4.6"/><path d="M21.5 8v5"/>',
}
CROSS = '<svg class="cross" viewBox="0 0 20 26" aria-hidden="true"><path d="M8 0h4v8h8v4h-8v14H8V12H0V8h8z"/></svg>'

# ----------------------------------------------------------------- UI text
T = {
 "no": {
  "other_label": "English", "other_lang": "en",
  "home_title": "Sunday Suite — programmer for kirke og klasserom",
  "home_desc": "Gratis programmer for kirke og klasserom, med åpen kildekode. Last ned SundayRec, eller åpne nettprogrammene i nettleseren.",
  "h1": "Programmer for kirke og klasserom",
  "intro": (f'Sunday Suite er gratis programmer for menigheter og skoler, laget i Norge. Kildekoden ligger på <a href="{GITHUB_ORG}">GitHub</a>. '
            f'Har du spørsmål, har du funnet en feil eller ønsker du deg noe, kan du skrive til <a href="mailto:{EMAIL}">{EMAIL}</a>.'),
  "h_download": ("last-ned", "Last ned"), "h_web": ("nettprogrammer", "Nettprogrammer"),
  "h_dev": ("under-utvikling", "Under utvikling"), "h_support": ("stotte", "Støtte"),
  "beta": "beta",
  "dl_mac": "Last ned for Mac", "dl_win": "Last ned for Windows",
  "mac_req": "Mac-versjonen krever Apple Silicon (M1 eller nyere).",
  "more_rec": "Mer om SundayRec og installasjon",
  "open": "Åpne", "open_sub": "Åpne {sub}",
  "back": "← Alle programmer",
  "dev_status": "Under utvikling. Ikke klar til vanlig bruk ennå.",
  "testbuild": "Vil du prøve likevel? Her er en uferdig testversjon for {mac} og {win}. Regn med feil og mangler.",
  "mac": "Mac", "mac_as": "Mac (Apple Silicon)", "win": "Windows",
  "source": "Kildekode på GitHub",
  "all_versions": "Alle versjoner og endringer på GitHub",
  "install_h": "Installasjon",
  "install_mac": "<strong>Mac:</strong> krever Apple Silicon (M1 eller nyere). Programmet er signert, men ikke notarisert ennå. Første gang du starter det, må du derfor høyreklikke på programmet og velge Åpne.",
  "install_win": "<strong>Windows:</strong> første gang kan Windows vise et SmartScreen-varsel. Velg Mer info og deretter Kjør likevel.",
  "support": [f"Programmene er gratis. Det koster likevel penger å drive dem: servere, domener og sertifikater for å signere programmene. Vil du bidra til det, kan du vippse til #{VIPPS['number']} ({VIPPS['name']}).",
              f"{VIPPS['name']} er enkeltpersonforetaket som står bak Sunday Suite. Det er ikke en veldedig organisasjon, så gaver gir ikke skattefradrag."],
  "vipps_alt": f"QR-kode for Vipps til #{VIPPS['number']} {VIPPS['name']}",
  "vipps_caption": f"Skann koden med mobilen, eller søk opp #{VIPPS['number']} i Vipps.",
  "terms": "Vilkår", "privacy": "Personvern",
  "legal_back": "← Til forsiden", "contents": "Innhold",
  "status": {"download": "Beta", "web": "På nett", "dev": "Under utvikling", "parked": "Ikke prioritert"},
  "parked_h": "Andre programmer (ikke prioritert)",
  "parked_p": "Disse programmene er ikke prioritert for øyeblikket.",
  "parked_web": "Kan brukes, men er ikke prioritert for øyeblikket.",
  "parked_dev": "Ikke prioritert for øyeblikket.",
  "and": "og",
  "terms_desc": "Vilkår for bruk av Sunday Suite og sundaysuite.app.",
  "privacy_desc": "Personvernerklæring for Sunday Suite og sundaysuite.app.",
 },
 "en": {
  "other_label": "Norsk", "other_lang": "nb",
  "home_title": "Sunday Suite — software for church and classroom",
  "home_desc": "Free, open-source programs for church and classroom. Download SundayRec, or open the web programs in your browser.",
  "h1": "Software for church and classroom",
  "intro": (f'Sunday Suite is a set of free programs for churches and schools, made in Norway. The source code is on <a href="{GITHUB_ORG}">GitHub</a>. '
            f'Questions, bug reports and requests go to <a href="mailto:{EMAIL}">{EMAIL}</a>.'),
  "h_download": ("download", "Download"), "h_web": ("web", "Web programs"),
  "h_dev": ("in-development", "In development"), "h_support": ("support", "Support"),
  "beta": "beta",
  "dl_mac": "Download for Mac", "dl_win": "Download for Windows",
  "mac_req": "The Mac version needs Apple Silicon (M1 or newer).",
  "more_rec": "More about SundayRec and installing it",
  "open": "Open", "open_sub": "Open {sub}",
  "back": "← All programs",
  "dev_status": "In development. Not ready for regular use yet.",
  "testbuild": "Want to try it anyway? There is an unfinished test build for {mac} and {win}. Expect bugs and missing pieces.",
  "mac": "Mac", "mac_as": "Mac (Apple Silicon)", "win": "Windows",
  "source": "Source code on GitHub",
  "all_versions": "All versions and changes on GitHub",
  "install_h": "Installing",
  "install_mac": "<strong>Mac:</strong> needs Apple Silicon (M1 or newer). The app is signed but not notarized yet, so the first time you open it, right-click the app and choose Open.",
  "install_win": "<strong>Windows:</strong> the first time, Windows may show a SmartScreen warning. Choose More info, then Run anyway.",
  "support": [f"The programs are free. Running them still costs money: servers, domains and certificates for signing the apps. If you would like to help with that, you can send a Vipps payment to #{VIPPS['number']} ({VIPPS['name']}). Vipps needs a Norwegian bank account; from abroad, write to <a href=\"mailto:{EMAIL}\">{EMAIL}</a>.",
              f"{VIPPS['name']} is the sole proprietorship behind Sunday Suite. It is not a charity, so gifts are not tax-deductible."],
  "vipps_alt": f"Vipps QR code for #{VIPPS['number']} {VIPPS['name']}",
  "vipps_caption": f"Scan the code with your phone, or search for #{VIPPS['number']} in Vipps.",
  "terms": "Terms", "privacy": "Privacy",
  "legal_back": "← Front page", "contents": "Contents",
  "status": {"download": "Beta", "web": "Online", "dev": "In development", "parked": "Not a priority"},
  "parked_h": "Other programs (not a priority)",
  "parked_p": "These programs are not a priority at the moment.",
  "parked_web": "Usable, but not a priority at the moment.",
  "parked_dev": "Not a priority at the moment.",
  "and": "and",
  "terms_desc": "Terms of Use for Sunday Suite and sundaysuite.app.",
  "privacy_desc": "Privacy Policy for Sunday Suite and sundaysuite.app.",
 },
}

# ----------------------------------------------------------------- paths
def page_path(lang, name):
    """Repo path of a page: name is 'index', 'apps/<slug>' or 'legal/<doc>'."""
    return PREFIX[lang] + name + ".html"

def clean(path):
    """Repo html path -> served path: 'index.html' -> '', 'apps/x.html' -> 'apps/x'."""
    if path.endswith("index.html"):
        return path[:-len("index.html")]
    return path[:-len(".html")] if path.endswith(".html") else path

def link(frm, to):
    """Relative, extensionless link from page `frm` to page `to` (repo paths)."""
    here = posixpath.dirname(frm) or "."
    target = clean(to)
    if target == "" or target.endswith("/"):
        r = posixpath.relpath(target.rstrip("/") or ".", here)
        return "./" if r == "." else r + "/"
    return posixpath.relpath(target, here)

def asset(frm, name):
    return posixpath.relpath("assets/" + name, posixpath.dirname(frm) or ".")

def counterpart(path):
    """The same page in the other language."""
    return path[len("en/"):] if path.startswith("en/") else "en/" + path

def url(path):
    return SITE + "/" + clean(path)

# ----------------------------------------------------------------- pieces
def icon(p, frm):
    if p.get("logo"):
        return f'<img class="ic" src="{asset(frm, "logos/" + p["slug"] + ".svg")}" alt="" width="32" height="32">'
    return (f'<span class="ic tile" style="background:{p["color"]}" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{GLYPH[p["glyph"]]}</svg></span>')

def blocks(body, frm, lang):
    privacy = link(frm, page_path(lang, "legal/privacy"))
    out = []
    for b in body:
        if isinstance(b, list):
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in b) + "</ul>")
        else:
            out.append(f"<p>{b}</p>")
    return "\n".join(out).replace("@PRIVACY@", privacy)

def plain(s):
    """Strip tags for meta descriptions."""
    return re.sub(r"<[^>]+>", "", s).replace('"', "&quot;")

def shell(lang, path, title, desc, main, script=False):
    t = T[lang]
    no_path = path[len("en/"):] if lang == "en" else path
    en_path = "en/" + no_path
    other = counterpart(path)
    home = link(path, page_path(lang, "index"))
    foot = " · ".join([
        f'<a href="mailto:{EMAIL}">{EMAIL}</a>',
        f'<a href="{GITHUB_ORG}">GitHub</a>',
        f'<a href="{link(path, page_path(lang, "legal/terms"))}">{t["terms"]}</a>',
        f'<a href="{link(path, page_path(lang, "legal/privacy"))}">{t["privacy"]}</a>',
    ])
    js = f'\n<script src="{asset(path, "site.js")}" defer></script>' if script else ""
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(path)}">
<link rel="alternate" hreflang="nb" href="{url(no_path)}">
<link rel="alternate" hreflang="en" href="{url(en_path)}">
<link rel="alternate" hreflang="x-default" href="{url(no_path)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(path)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sunday Suite">
<link rel="icon" href="{asset(path, "favicon.svg")}" type="image/svg+xml">
<link rel="stylesheet" href="{asset(path, "site.css")}">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{home}">{CROSS}Sunday Suite</a>
<a class="lang" href="{link(path, other)}" hreflang="{t["other_lang"]}" lang="{t["other_lang"]}">{t["other_label"]}</a>
</div></header>
<main class="wrap">
{main}
</main>
<footer class="wrap"><p>{foot}</p></footer>{js}
</body>
</html>
'''

def rec_downloads(lang):
    t = T[lang]
    return (f'<p class="actions"><a class="btn" href="/download/sundayrec/mac">{t["dl_mac"]}</a>'
            f'<a class="btn" href="/download/sundayrec/windows">{t["dl_win"]}</a></p>')

def row(p, lang, frm):
    t = T[lang]
    name = f'<a href="{link(frm, page_path(lang, "apps/" + p["slug"]))}">{p["name"]}</a>'
    act = (f'<a class="open" href="{p["url"]}">{t["open"]}<span aria-hidden="true"> ↗</span></a>'
           if p["group"] == "web" else "")
    return (f'<li class="row">{icon(p, frm)}<div class="txt"><p class="name">{name}</p>'
            f'<p class="desc">{p[lang]["line"]}</p></div>{act}</li>')

# ----------------------------------------------------------------- pages
def render_home(lang):
    t = T[lang]
    path = page_path(lang, "index")
    rec = BY["sundayrec"]
    rec_page = link(path, page_path(lang, "apps/sundayrec"))
    sid = lambda k: f'<h2 id="{t[k][0]}">{t[k][1]}</h2>'
    ul = lambda ps: '<ul class="list">\n' + "\n".join(row(p, lang, path) for p in ps) + "\n</ul>"
    rows = lambda g: ul(p for p in PROGRAMS if p["group"] == g and not p.get("parked"))
    parked = ul(p for g in GROUPS for p in PROGRAMS if p["group"] == g and p.get("parked"))
    support = "\n".join(f"<p>{s}</p>" for s in t["support"])
    main = f'''<h1>{t["h1"]}</h1>
<p class="intro">{t["intro"]}</p>

<section>
{sid("h_download")}
<div class="feature">{icon(rec, path)}<div class="txt">
<p class="name"><a href="{rec_page}">SundayRec</a> <span class="tag">{t["beta"]}</span></p>
<p>{rec[lang]["line"]}</p>
{rec_downloads(lang)}
<p class="small"><span data-app-version="sundayrec" hidden></span>{t["mac_req"]} <a href="{rec_page}">{t["more_rec"]}</a></p>
</div></div>
</section>

<section>
{sid("h_web")}
{rows("web")}
</section>

<section>
{sid("h_dev")}
{rows("dev")}
</section>

<section>
{sid("h_support")}
<div class="vipps"><img src="{asset(path, "vipps-qr.png")}" alt="{t["vipps_alt"]}" width="120" height="120"><div>
{support}
<p class="small">{t["vipps_caption"]}</p>
</div></div>
</section>

<details class="more">
<summary>{t["parked_h"]}</summary>
<p class="small">{t["parked_p"]}</p>
{parked}
</details>'''
    return shell(lang, path, t["home_title"], t["home_desc"], main, script=True)

def render_program(lang, p):
    t = T[lang]
    d = p[lang]
    path = page_path(lang, "apps/" + p["slug"])
    home = link(path, page_path(lang, "index"))
    tag = f' <span class="tag">{t["beta"]}</span>' if p["group"] == "download" else ""
    parts = [f'<p class="back"><a href="{home}">{t["back"]}</a></p>',
             f'<div class="phead">{icon(p, path)}<div><h1>{p["name"]}{tag}</h1><p class="line">{d["line"]}</p></div></div>']
    if p.get("parked"):
        parts.append(f'<p class="status">{t["parked_" + p["group"]]}</p>')
    elif p["group"] == "dev":
        parts.append(f'<p class="status">{t["dev_status"]}</p>')
    parts.append(blocks(d["body"], path, lang))
    source = (f'<a href="https://github.com/{p["repo"]}">{t["source"]}</a>' if p.get("repo") else "")
    if p["group"] == "download":
        parts.append(rec_downloads(lang))
        parts.append(f'<h2>{t["install_h"]}</h2>\n<p>{t["install_mac"]}</p>\n<p>{t["install_win"]}</p>')
        parts.append(f'<p class="small"><span data-app-version="{p["slug"]}" hidden></span>'
                     f'<a href="https://github.com/{p["repo"]}/releases">{t["all_versions"]}</a> · {source}</p>')
    elif p["group"] == "web":
        sub = p["url"].replace("https://", "")
        parts.append(f'<p class="actions"><a class="btn" href="{p["url"]}">{t["open_sub"].format(sub=sub)}</a></p>')
        if source:
            parts.append(f'<p class="small">{source}</p>')
    else:
        extra = []
        if p.get("testbuild"):
            mac_label = t["mac"] if p["testbuild"] == "universal" else t["mac_as"]
            extra.append(t["testbuild"].format(
                mac=f'<a href="/download/{p["slug"]}/mac">{mac_label}</a>',
                win=f'<a href="/download/{p["slug"]}/windows">{t["win"]}</a>'))
        if source:
            extra.append(source)
        if extra:
            parts.append(f'<p class="small">{" ".join(extra)}</p>')
    title = f'{p["name"]} — Sunday Suite'
    return shell(lang, path, title, plain(d["line"]), "\n".join(parts), script=(p["group"] == "download"))

def render_legal(lang, doc):
    t = T[lang]
    path = page_path(lang, "legal/" + doc)
    ordered = ([p for g in GROUPS for p in PROGRAMS if p["group"] == g and not p.get("parked")]
               + [p for g in GROUPS for p in PROGRAMS if p["group"] == g and p.get("parked")])
    rows = "".join(f'<tr><td>{p["name"]}</td><td>{p[lang]["line"]}</td>'
                   f'<td>{t["status"]["parked" if p.get("parked") else p["group"]]}</td></tr>' for p in ordered)
    names = [p["name"] for p in PROGRAMS]
    names = ", ".join(names[:-1]) + f' {t["and"]} ' + names[-1]
    fn = {("terms", "en"): lambda: legal.terms_en(rows, names), ("terms", "no"): lambda: legal.terms_no(rows, names),
          ("privacy", "en"): legal.privacy_en, ("privacy", "no"): legal.privacy_no}[(doc, lang)]
    title, updated, note, items, prose = fn()
    prose = (prose.replace('href="privacy.html"', 'href="privacy"')
                  .replace("<table", '<div class="table"><table').replace("</table>", "</table></div>"))
    toc = "".join(f'<li><a href="#{i}">{h}</a></li>' for i, h in items)
    main = f'''<p class="back"><a href="{link(path, page_path(lang, "index"))}">{t["legal_back"]}</a></p>
<article class="legal">
<h1>{title}</h1>
<p class="small">{updated}</p>
<p class="small note">{note}</p>
<nav class="toc" aria-label="{t["contents"]}"><ol>{toc}</ol></nav>
{prose}
</article>'''
    return shell(lang, path, f"{title} — Sunday Suite", t[doc + "_desc"], main)

def render_404():
    # Served by Pages for any unknown path at any depth, so links are absolute.
    return f'''<!DOCTYPE html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fant ikke siden — Sunday Suite</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/">{CROSS}Sunday Suite</a>
<a class="lang" href="/en/" hreflang="en" lang="en">English</a>
</div></header>
<main class="wrap">
<h1>Fant ikke siden</h1>
<p>Adressen finnes ikke, eller siden er flyttet. <a href="/">Gå til forsiden</a>.</p>
<p lang="en">Page not found. <a href="/en/">Go to the English front page</a>.</p>
</main>
<footer class="wrap"><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></footer>
</body>
</html>
'''

# ----------------------------------------------------------------- site files
def pages():
    """Every page name; both languages use the same names."""
    return (["index"] + [f"apps/{p['slug']}" for p in PROGRAMS] + ["legal/terms", "legal/privacy"])

def sitemap_xml():
    rows = []
    for name in pages():
        nu, eu = url(page_path("no", name)), url(page_path("en", name))
        alts = (f'<xhtml:link rel="alternate" hreflang="nb" href="{nu}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{eu}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{nu}"/>')
        for own in (nu, eu):
            rows.append(f"  <url><loc>{own}</loc>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")

# Old addresses from earlier versions of the site (Norwegian under /no/, English
# at the root, toolbox/build/help pages). /apps/* and /legal/* keep their
# address and now show Norwegian. Specific rules must come before splats.
REDIRECTS = """\
/no / 301
/no/ / 301
/no/index.html / 301
/no/verktoykasse / 301
/no/verktoykasse.html / 301
/no/bygg / 301
/no/bygg.html / 301
/no/hjelp / 301
/help/recording-with-sundayrec /en/apps/sundayrec 301
/help/recording-with-sundayrec.html /en/apps/sundayrec 301
/help /en/ 301
/toolbox /en/ 301
/toolbox.html /en/ 301
/build /en/ 301
/build.html /en/ 301
/no/apps/* /apps/:splat 301
/no/legal/* /legal/:splat 301
/no/hjelp/* / 301
/help/* /en/ 301
"""

def W(path, text):
    full = os.path.join(ROOTDIR, path)
    os.makedirs(os.path.dirname(full) or ROOTDIR, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    n = 0
    for lang in LANGS:
        W(page_path(lang, "index"), render_home(lang)); n += 1
        for p in PROGRAMS:
            W(page_path(lang, "apps/" + p["slug"]), render_program(lang, p)); n += 1
        for doc in ("terms", "privacy"):
            W(page_path(lang, "legal/" + doc), render_legal(lang, doc)); n += 1
    W("404.html", render_404())
    W("sitemap.xml", sitemap_xml())
    W("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    W("_redirects", REDIRECTS)
    print(f"wrote {n} pages + 404, sitemap, robots, _redirects")

if __name__ == "__main__":
    main()
