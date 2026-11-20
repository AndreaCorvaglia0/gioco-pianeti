# Gioco dei pianeti: note di progetto

Aggiornato al 20 novembre 2026.

## L'idea

Una storiella che si srotola pagina dopo pagina, come un teatrino di carta, per un bambino di 4 anni che non sa leggere.
Su ogni pianeta succede una cosa sola, che è la nozione. Il narratore accoglie, racconta una curiosità e invita a provare.

## Il giro

Terra → mappa → volo (ciao Venere) → Mercurio → mappa → volo → Sole → mappa → volo (ciao Mercurio, Venere, Terra, Marte)
→ Giove → mappa → volo → Saturno → mappa (Urano e Nettuno da lontano) → casa.

| Pagina | Cosa si fa | Nozione |
|---|---|---|
| Terra | Si tocca il razzo | Casa; la Luna gira intorno |
| Mappa | Si guarda (un tocco la salta) | Il Sole al centro, i pianeti in ordine |
| Volo | Il razzo segue il dito; turbo facoltativo | Il Sole cresce o rimpicciolisce; i pianeti saltati passano e si salutano |
| Mercurio | Si cammina dal lato al sole al lato in ombra | Un lato scotta, uno gela |
| Sole | Si tocca il bordo: escono fiammate | È una stella, non si atterra; dà luce a tutti |
| Giove | Si galleggia col palloncino; il vento porta via; la Macchia Rossa fa girare | Gigante di nuvole e vento, senza pavimento |
| Saturno | Si guida il razzo tra i pezzi degli anelli, che suonano | Gli anelli sono pezzetti di ghiaccio |

## Regole di interfaccia

1. Un solo gesto per pagina.
2. Il gioco non dipende mai dal tenere premuto qualcosa.
3. Una sola cosa pulsa: quella da fare adesso.
4. Dopo quattro secondi fermi, un dito fantasma mostra il gesto.
5. Non si sbaglia mai: l'errore è una gag (il razzo supera il pianeta, gira e torna).
6. Il punteggio sono due o tre stelle grandi in alto a destra.
7. Niente volti: l'astronauta è grande e parla col corpo; un fumetto con una sola icona dice cosa sente.
8. Comandi grandi e lontani dai bordi.
9. Deve capirsi anche a volume spento: ogni frase del narratore compare scritta, per l'adulto.

## Narratore

- Copione in `narration/lines.json`. Le frasi aspettano il loro turno; quelle di reazione interrompono.
- Voce: ElevenLabs, "Antonio Farina", modello Eleven v4. Generata dal sito in un file unico e poi tagliata frase per frase
  (con il piano gratuito le voci della libreria non si possono usare tramite chiave).
- Il nome del bambino è in tre frasi: `intro`, `bravo`, `fine`. Per una versione senza nome basta rigenerare quelle.

## Dati reali e licenze

- Dimensioni in volo: raggi veri, compressi con esponente 0,85.
- Distanze e durata dei viaggi: radice quadrata delle distanze vere.
- Sole: grandezza apparente inversa alla distanza, rapporto vero.
- Anelli di Saturno: bordo esterno a 2,27 raggi del pianeta, rapporto vero. Lune: raggi veri in rapporto tra loro.
- Non in scala: l'astronauta, le palline su cui si cammina, la mappa (ordine vero, distanze molto compresse).

## Verifiche

- Fatte: partita intera giocata da un programma (`tools/playthrough.py`) senza errori; ogni frase audio ricontrollata con una trascrizione automatica.
- Non fatte da strumenti: dita vere, due dita insieme, ascolto, telefono in verticale.

## Prossimi passi

- Rifinitura dopo le prove dal telefono.
- Il sassolino: lanciarlo su un pianeta roccioso rimbalza, su uno gassoso sprofonda.
- Venere, Marte, Urano e Nettuno come pagine vere.
- Una cornice di storia: perché si parte.
