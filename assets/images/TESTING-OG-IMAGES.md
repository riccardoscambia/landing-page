# Test Open Graph Images - Quick Guide

## ⚡ Test Velocissimo (1 minuto)

### Metodo 1: WhatsApp
1. Apri WhatsApp sul telefono
2. Apri una chat con te stesso o un amico
3. Incolla questo link: `https://khloegrace.com/`
4. Aspetta 2-3 secondi
5. ✅ Dovresti vedere l'immagine OG apparire!

---

## ⚠️ IMPORTANTE: Il Sito Deve Essere Online!

Le OG images funzionano SOLO se:
- ✅ Il sito è pubblicato e accessibile online
- ✅ Le immagini sono caricate sul server
- ✅ L'URL è pubblico (https://khloegrace.com/)

❌ NON funziona:
- Con file locali (file:///)
- Con localhost
- Con server di development non pubblici

---

## 🧪 Test Professionale (3 minuti)

### Facebook Sharing Debugger
1. Vai su: https://developers.facebook.com/tools/debug/
2. Incolla URL: `https://khloegrace.com/`
3. Clicca "Debug"
4. ✅ Vedrai la preview con l'immagine OG

**Nota**: Se è la prima volta, clicca "Scrape Again" per forzare Facebook a ricaricare.

### Twitter Card Validator
1. Vai su: https://cards-dev.twitter.com/validator
2. Incolla URL: `https://khloegrace.com/`
3. Clicca "Preview card"
4. ✅ Vedrai la Twitter Card con l'immagine

---

## 📱 Instagram - Come Funziona

### ❌ NON Funziona:
- Post caption (testo del post)
- Commenti
- Bio

### ✅ Funziona:
- DM/Messaggi Diretti (mostra preview)
- Stories con link (se hai 10k+ follower)

### Come Testare su Instagram:
1. Invia il link a te stesso in DM
2. O mandalo a un amico in chat privata
3. ✅ Lì dovresti vedere la preview con OG image

---

## 🔍 Troubleshooting

### "Non vedo l'immagine":

**1. Il sito è pubblicato online?**
   - Deve essere su https://khloegrace.com/
   - Non localhost o file locale

**2. Le immagini sono caricate?**
   - Verifica che esistano su: https://khloegrace.com/assets/images/og-image.jpg
   - Prova ad aprire l'URL direttamente nel browser

**3. Cache dei social:**
   - I social potrebbero aver già salvato una vecchia versione
   - Usa i debugger per forzare refresh:
     - Facebook: https://developers.facebook.com/tools/debug/
     - Twitter: https://cards-dev.twitter.com/validator

**4. Tempo di propagazione:**
   - Dopo il deploy, aspetta 5-10 minuti
   - I social potrebbero impiegare tempo a scaricare le immagini

---

## ✅ Checklist Pre-Test

Prima di testare, verifica:

- [ ] Sito pubblicato online (non localhost)
- [ ] File og-image.jpg caricato su server
- [ ] URL immagini accessibili pubblicamente
- [ ] Meta tags OG presenti nell'HTML
- [ ] Aspettato 5-10 min dopo deploy

---

## 💡 Piattaforme con Migliore Supporto OG

**Excellent (100%):**
- Facebook
- WhatsApp
- Telegram
- LinkedIn
- Twitter/X
- Discord
- Slack

**Parziale:**
- Instagram (solo DM)
- TikTok (limitato)

**Non Supportato:**
- SMS
- Email standard

---

## 🎯 Conclusione

**Instagram nei commenti = NON funziona mai**  
**Prova invece su:**
1. WhatsApp (test più veloce)
2. Facebook (test più affidabile)
3. Twitter Card Validator (test tecnico)

Se il sito non è ancora pubblicato online, le OG images non funzioneranno da nessuna parte!
