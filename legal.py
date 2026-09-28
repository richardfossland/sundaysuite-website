# -*- coding: utf-8 -*-
"""Legal text for sundaysuite.app — Terms of Use and Privacy Policy, EN + NO.

Each function returns (title, updated, note, toc_items, prose_html); build.py
wraps it in the page shell. The prose is kept close to the reviewed wording —
change it deliberately, not as part of a design pass.

terms_*() take `rows` (pre-rendered <tr> rows for the programme table) and
`names` (the product names, comma-separated) so the lists can never go stale.
"""

UPDATED = {"en": "Last updated: 28 September 2026", "no": "Sist oppdatert: 28. september 2026"}

def h2(n,i,t): return f'<h2 id="{i}"><span class="num">{n}.</span>{t}</h2>'

# ---- Terms EN
def terms_en(rows, names):
    note='<strong>Note:</strong> This document is a good-faith template and is not legal advice. Have it reviewed by a lawyer before relying on it commercially — especially the sections on intellectual property, liability and consumer protection.'
    items=[("s1","About these Terms"),("s2","The Service"),("s3","Price, beta and availability"),("s4","Licence"),("s5","Intellectual property and trademarks"),("s6","Your content"),("s7","Third-party services"),("s8","Acceptable use"),("s9","Disclaimer of warranties"),("s10","Limitation of liability"),("s11","Changes to these Terms"),("s12","Governing law and venue"),("s13","Contact")]
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
    <p>Subject to your compliance with these Terms, we grant you a non-exclusive, non-transferable and revocable licence to download and use the Sunday programs, as distributed via sundaysuite.app, for your organization's own purposes.</p>
    <h3>Open source</h3>
    <p>Sunday Suite is built in the open: much of the suite's source code is published in public repositories on <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a> under open-source licences — MIT where a licence file is present. For that code, the repository's own licence governs your rights, and nothing in these Terms limits what that licence grants you, including the rights to use, study, modify and redistribute the code.</p>
    <p>Except to the extent an applicable open-source licence expressly permits it, you may not:</p>
    <ul><li>redistribute, sell, rent or sublicense the software;</li><li>decompile, reverse-engineer or attempt to derive the source code, except to the extent mandatory law permits;</li><li>remove or alter any copyright notices, trademarks or other proprietary markings;</li><li>use the "Sunday" names, logos or trade dress in a way likely to cause confusion about origin or endorsement; or</li><li>use the Service for any unlawful purpose.</li></ul>
    {h2(5,"s5","Intellectual property and trademarks")}
    <p>The website, design, graphics, the golden cross, logos, names and text are owned by Richard Fossland and protected by applicable law on copyright, trademarks and other intellectual property rights. The source code of the Sunday programs — <strong>{names}</strong> — is &copy; Richard Fossland and contributors. A public Sunday repository that contains a licence file is published under the <strong>MIT Licence</strong>, and that licence governs your rights to the code it contains. A public repository without a licence file is published for reading only, and no licence to that code is granted until one is added.</p>
    <h3>Trademarks</h3>
    <p>The names "Sunday Suite", the "Sunday" family of product names listed above, and the associated cross and gold symbol, are our trademarks (registered or being established). You are granted no right to use these trademarks, and you must not use them — or names, logos or designs likely to be confused with them — without prior written consent. This also applies to product, domain, app-store and company names. The open-source licences cover the code — they grant no rights to the "Sunday" names, the cross-and-gold mark or the logos.</p>
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
    return ("Terms of Use", UPDATED["en"], note, items, prose)

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
    <p>The free games and group activities on subdomains of sundaysuite.app (such as SundayQuiz, SundayChess and SundayPanel) are designed to store as little as possible: sessions are anonymous for participants and expire after use. Two exceptions are worth knowing. <strong>SundayWelcome</strong> stores the contact details a newcomer chooses to submit so the church team can follow up; that data belongs to the church in question, and deletion can be requested at any time from the church or via <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. <strong>SundayBasar</strong> never touches money — payments happen directly in Vipps between you and the organiser, and the app only records what the organiser confirms manually.</p>
    {h2(11,"p11","Third-party services")}
    <p>When you enable an integration, the relevant third party's privacy rules apply to that part of the processing. Examples may be Google (Drive/YouTube), a podcast host or an email provider. You choose whether and when these are used.</p>
    {h2(12,"p12","Your rights")}
    <p>Since most data lives locally on your machine, you have direct control and can view, change, export and delete it yourself. For personal data we may process (for example an email enquiry), you have the right under the privacy regulation (GDPR) to access, rectification, erasure and restriction. Contact us to exercise these rights.</p>
    {h2(13,"p13","Changes")}
    <p>We may update this policy. Material changes are notified by updating the date at the top of the page.</p>
    {h2(14,"p14","Contact")}
    <p>Questions about privacy? Contact the data controller Richard Fossland at <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return ("Privacy Policy", UPDATED["en"], note, items, prose)

# ---- Terms NO
def terms_no(rows, names):
    note='<strong>Merk:</strong> Dette dokumentet er en mal levert i god tro og er ikke juridisk rådgivning. Få det gjennomgått av en advokat før du stoler på det kommersielt — særlig avsnittene om immaterielle rettigheter, ansvar og forbrukervern.'
    items=[("s1","Om vilkårene"),("s2","Tjenesten"),("s3","Pris, beta og tilgjengelighet"),("s4","Lisens"),("s5","Immaterielle rettigheter og varemerker"),("s6","Ditt innhold"),("s7","Tredjepartstjenester"),("s8","Akseptabel bruk"),("s9","Fraskrivelse av garantier"),("s10","Ansvarsbegrensning"),("s11","Endringer i vilkårene"),("s12","Lovvalg og verneting"),("s13","Kontakt")]
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
    <p>Under forutsetning av at du følger disse Vilkårene, gir vi deg en ikke-eksklusiv, ikke-overførbar og gjenkallelig lisens til å laste ned og bruke Sunday-programmene, slik de distribueres via sundaysuite.app, for din organisasjons egne formål.</p>
    <h3>Åpen kildekode</h3>
    <p>Sunday Suite bygges i det åpne: mye av suitens kildekode er publisert i offentlige repositorier på <a href="https://github.com/SundaySuite-app" target="_blank" rel="noopener">GitHub</a> under åpen kildekode-lisenser — MIT der lisensfil foreligger. For den koden er det repositoriets egen lisens som styrer rettighetene dine, og ingenting i disse Vilkårene innskrenker det lisensen gir deg, herunder retten til å bruke, studere, endre og videredistribuere koden.</p>
    <p>Med mindre en gjeldende åpen kildekode-lisens uttrykkelig tillater det, har du ikke lov til å:</p>
    <ul><li>videredistribuere, selge, leie ut eller viderelisensiere programvaren;</li><li>dekompilere, reversutvikle eller forsøke å utlede kildekoden, unntatt i den grad ufravikelig lov tillater det;</li><li>fjerne eller endre opphavsrettsmerker, varemerker eller andre rettighetsmerker;</li><li>bruke «Sunday»-navnene, logoene eller utformingen på en måte som er egnet til å skape forveksling om opphav eller tilknytning; eller</li><li>bruke Tjenesten til ulovlige formål.</li></ul>
    {h2(5,"s5","Immaterielle rettigheter og varemerker")}
    <p>Nettstedet, designet, grafikken, det gylne korset, logoene, navnene og teksten eies av Richard Fossland og er beskyttet av gjeldende lovgivning om opphavsrett, varemerker og andre immaterielle rettigheter. Kildekoden til Sunday-programmene — <strong>{names}</strong> — er &copy; Richard Fossland og bidragsytere. Et offentlig Sunday-repositorium som inneholder en lisensfil, er publisert under <strong>MIT-lisensen</strong>, og den lisensen styrer rettighetene dine til koden det inneholder. Et offentlig repositorium uten lisensfil er publisert kun for lesing, og ingen lisens til den koden gis før en legges til.</p>
    <h3>Varemerker</h3>
    <p>Navnene «Sunday Suite», «Sunday»-familien av produktnavn nevnt over, samt det tilhørende kors- og gull-symbolet, er våre varemerker (registrerte eller under etablering). Du får ingen rett til å bruke disse varemerkene, og du må ikke bruke dem — eller navn, logoer eller utforming som er egnet til å forveksles med dem — uten skriftlig forhåndssamtykke. Dette gjelder også produkt-, domene-, app-butikk- og selskapsnavn. Åpen kildekode-lisensene dekker koden — de gir ingen rett til «Sunday»-navnene, kors-og-gull-merket eller logoene.</p>
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
    return ("Vilkår for bruk", UPDATED["no"], note, items, prose)

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
    <p>De gratis spillene og gruppeaktivitetene på underdomener av sundaysuite.app (som SundayQuiz, SundayChess og SundayPanel) er designet for å lagre minst mulig: økter er anonyme for deltakerne og utløper etter bruk. To unntak er verdt å kjenne til. <strong>SundayWelcome</strong> lagrer kontaktinformasjonen en nykommer selv velger å legge igjen, slik at menighetens team kan følge opp; disse dataene tilhører den aktuelle menigheten, og sletting kan når som helst kreves hos menigheten eller via <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>. <strong>SundayBasar</strong> rører aldri penger — betalinger skjer direkte i Vipps mellom deg og arrangøren, og appen registrerer bare det arrangøren selv bekrefter manuelt.</p>
    {h2(11,"p11","Tredjepartstjenester")}
    <p>Når du aktiverer en integrasjon, gjelder den aktuelle tredjepartens personvernregler for den delen av behandlingen. Eksempler kan være Google (Drive/YouTube), en podkast-host eller en e-postleverandør. Du velger selv om og når disse tas i bruk.</p>
    {h2(12,"p12","Dine rettigheter")}
    <p>Siden de fleste dataene ligger lokalt på din maskin, har du direkte kontroll og kan se, endre, eksportere og slette dem selv. For personopplysninger vi måtte behandle (for eksempel en e-posthenvendelse), har du etter personvernregelverket (GDPR) rett til innsyn, retting, sletting og begrensning. Kontakt oss for å utøve disse rettighetene.</p>
    {h2(13,"p13","Endringer")}
    <p>Vi kan oppdatere denne erklæringen. Vesentlige endringer varsles ved å oppdatere datoen øverst på siden.</p>
    {h2(14,"p14","Kontakt")}
    <p>Spørsmål om personvern? Kontakt behandlingsansvarlig Richard Fossland på <a href="mailto:dev@sundaysuite.app">dev@sundaysuite.app</a>.</p>'''
    return ("Personvernerklæring", UPDATED["no"], note, items, prose)
