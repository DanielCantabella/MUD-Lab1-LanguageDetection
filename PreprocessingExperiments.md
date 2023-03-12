# Preprocessing experiments
```bash
python ./source/langdetect.py -i ./data/dataset.csv -v 1000 -a word
```
## Raw data
```
het internationale rode kruis kent twee onderscheidingen en meerdere penningen en spelden van verdienste zoals de medaille voor het eeuwfeest in  en de in  geslagen medaille ter ere van het vijftigjarig bestaan van de liga van het rode kruis en de halve rode maanverenigingen dat zijn legpenningen draagbare onderscheidingen zijn

年，以電影《永遠的三丁目的夕陽》等片的表現獲得該年度elandor奬新人奬，並獲得第回日本電影金像獎新演員獎、第屆金箭獎最佳新人獎。同年月，再度與山下智久共演《詐欺獵人》。月，與同事務所的黑木美沙共演電影《鬼來電final》，飾演主角松田明日香，亦於此年首次主演無線台的地上波連續劇《鐵板少女小茜》。

 entire web was loosely based on the premise of citation—after all what is a link but a citation? if he could devise a method to count and qualify each backlink on the web as page puts it "the web would become a more valuable place"

د کیفیت تضمین کوونکی دی د عایداتو د زیاتوالی سبب کرځی د ښه اعتماد د پیدا کوولو منبه بلل کیږی ډیر مفید او مؤثر عملیات برابروی د مشتریانو رضایت زیاتوی بازار یا مارکیت ته کی د ډیری ودی لامل کیږی د کثافاتو یا اضافه مصرف څخه مخنیوی کوی د معیاری کولو یو معمول او اسانه وسیله ده

eind  gaf shahini aan dat ze opnieuw een gooi wilde doen naar een songfestivalticket ze deed daarom in december van dat jaar wederom mee bij festivali i këngës maar verloor daarin van zanger en idolswinnaar luiz ejlli die op zijn beurt een jaar eerder verloren had van ledina çelo ejlli vertegenwoordigde albanië tijdens het songfestival in athene met het nummer zjarr e ftohtë daarbij geflankeerd door een groep oude heren met traditionele instrumenten het was het eerste lied in de geschiedenis van het eurovisiesongfestival dat in het albanees werd gezongen kwalificatie voor de finale werd echter niet afgedwongen ejlli eindigde in de halve finale als de ook het eurovisiesongfestival van  verliep teleurstellend voor albanië het land probeerde de finale te bereiken met het duo aida  frederik ndoci maar hun liedje hear my plea een ballade met traditionele invloeden vergaarde niet meer dan  punten en strandde in de halve finale op de de plek

```
## REMOVING SYMBOLS AND NUMBERS
```
het i ter atio ale rode kruis ke t twee o derscheidi ge  e  meerdere pe  i ge  e  spelde  va  verdie ste zoals de medaille voor het eeuwfeest i   e  de i   geslage  medaille ter ere va  het vijftigjarig bestaa  va  de liga va  het rode kruis e  de halve rode maa vere igi ge  dat zij  legpe  i ge  draagbare o derscheidi ge  zij 

年，以電影《永遠的三丁目的夕陽》等片的表現獲得該年度ela dor奬新人奬，並獲得第回日本電影金像獎新演員獎、第屆金箭獎最佳新人獎。同年月，再度與山下智久共演《詐欺獵人》。月，與同事務所的黑木美沙共演電影《鬼來電fi al》，飾演主角松田明日香，亦於此年首次主演無線台的地上波連續劇《鐵板少女小茜》。

 e tire web was loosely based o  the premise of citatio —after all what is a li k but a citatio   if he could devise a method to cou t a d qualify each backli k o  the web as page puts it  the web would become a more valuable place 

د کیفیت تضمین کوونکی دی د عایداتو د زیاتوالی سبب کرځی د ښه اعتماد د پیدا کوولو منبه بلل کیږی ډیر مفید او مؤثر عملیات برابروی د مشتریانو رضایت زیاتوی بازار یا مارکیت ته کی د ډیری ودی لامل کیږی د کثافاتو یا اضافه مصرف څخه مخنیوی کوی د معیاری کولو یو معمول او اسانه وسیله ده

ei d  gaf shahi i aa  dat ze op ieuw ee  gooi wilde doe   aar ee  so gfestivalticket ze deed daarom i  december va  dat jaar wederom mee bij festivali i kë gës maar verloor daari  va  za ger e  idolswi  aar luiz ejlli die op zij  beurt ee  jaar eerder verlore  had va  ledi a çelo ejlli vertege woordigde alba ië tijde s het so gfestival i  athe e met het  ummer zjarr e ftohtë daarbij gefla keerd door ee  groep oude here  met traditio ele i strume te  het was het eerste lied i  de geschiede is va  het eurovisieso gfestival dat i  het alba ees werd gezo ge  kwalificatie voor de fi ale werd echter  iet afgedwo ge  ejlli ei digde i  de halve fi ale als de ook het eurovisieso gfestival va   verliep teleurstelle d voor alba ië het la d probeerde de fi ale te bereike  met het duo aida  frederik  doci maar hu  liedje hear my plea ee  ballade met traditio ele i vloede  vergaarde  iet meer da   pu te  e  stra dde i  de halve fi ale op de de plek

```
## Tokenization
```
0        สัมประสิทธิ์ฮอลล์ ฟิสิกส์ไฟฟ้า เกี่ยวกับสนามแม...
1        เกิดวันที่ พฤศจิกายน ภาคอะนิเมะ คดีฆาตกรรมบนจอ...
2        i omgivningarna runt manigotagan river park re...
3        நிஞ்சா ஹட்டோரி 忍者ハットリくん ninja hattori என்பது க...
4        эта страница деятельности м в ломоносова — ярк...
```

```
5207         Thai
4450         Thai
7033      Swedish
487         Tamil
19537     Russian

```
## Sentence splitting

## Normalization
