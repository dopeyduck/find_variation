# find_variation
This script finds all variation units where a set of witnesses (>=1) agrees against another set (>=1) with a defined upper limit of agreeing witnesses with set 1.

In the terminal:
1. Navegate to the directory in which the script is saved.
2. Start the script: ```python3 -m find_variations``` [Mac]; for Windows ```python find_variations.py```
3. Provide the requested details in the prompts.

```
Please enter the path of the XML file: your_collation.xml
Please enter the set of included witnesses (space or comma-separated): "Witness(es)"
Please enter the set of excluded witnesses (space or comma-separated, or leave blank if none): "Excluded Witness(es)"
Please enter the maximum number of other witnesses that may be present: "Upper Limit"
```
Here is an example from a collation of ECM witness in Jude.
```
Please enter the path of the XML file: ecmCatFinal.xml
Please enter the set of included witnesses (space or comma-separated): 1881
Please enter the set of excluded witnesses (space or comma-separated, or leave blank if none): A
Please enter the maximum number of other witnesses that may be present: 2
```

The script will return the following data.

"Variation Unit"  "From"  "To"  "Variation ID"  "Witnesses"  "Reading"

The "From" and "To" columns may read "None" depending on the format of the collation file. For some collation files, the "From" and "To" columns will be specified for the variant unit address. In the example, I have given, that information is contained in the Unit ID, for example B26K1V1U4-8, which means B26 (Book 26 = Jude), K1 (Chapter 1), V1 (Verse 1), U4–8 (Unit ID 4-8). The Unit ID refers to the numbers assigned to words in the text. This is the convention followed for the printed text in the Editio Critica Maior.

```
B26K1V1U4-8	None	None	c	180 1751 1881	δουλος ιησου χριστου
B26K1V4U48-58	None	None	l	1881	δεσποτην και κυριον ιησουν χριστον
B26K1V5U4	None	None	c	1881 2186	None
B26K1V15U48-50	None	None	b	1881	κατα θεου
B26K1V16U14-16	None	None	d	1881 2805	ιδιας επιθυμιας αυτων
B26K1V17U32	None	None	b	1881	None
B26K1V18U8-14	None	None	r	1881	επ εσχατου των ημερων ελευσονται
B26K1V23U24	None	None	b	1881	None
```
In the above example, the script is in the same directory as the xml collation file. This is not necessary, as you can provide the location of the directory for the collation file.
