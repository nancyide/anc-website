MASC-1.03   2010-09-19
----------------------

Full documentation for the MASC data and processing tools is
available at http://www.anc.org/MASC.

DATA DESCRIPTION
----------------
See http://www.anc.org/MASC/mascI_contents.html

CONTENTS
--------

data - 
   spoken - data and annotations for spoken data
   written - data and annotations for written data

   See http://www.anc.org/MASC/MASC_Structure.html for 
   details on the organization of MASC data and annotation files
 
   original-annotations - Contains annotations contributed to MASC in 
        their original format, as prepared by an external annotation 
        project. These annotations are transduced to GrAF format for 
        inclusion in MASC. In general, errors in the originals are left 
        uncorrected.

MASC-corpus-header.xml - 
   Comprehensive information about the corpus, contents, 
   organization, domain codes, naming conventions, etc.

RAEDME.txt - This document.

 
RELEASE 1.0.3 NOTES
-------------------
Nature of the changes: Minor

Revision:

 - fixes additional misaligned Penn Treebank tokens

 - adds missing references to associated annotation files in the 
   document headers for the ICIC data.

Known Problems
--------------

Penn Treebank Tokens

There remain a few problems with the Penn Treebank tokenizations, 
primarily due to corrections to the texts made by the Treebank project
in the course of generating the original annotations. In some cases,
we have corrected the tokenizations to refer to the faulty text 
segment (e.g., "o" for "off" due to removal of ligatures in the 
course of transduction from original Quark Express files) and added 
an annotation named "corrected" whose value provides the correction to 
the text.


Event co-reference

The original GATE annotations done at Carnegie-Mellon University used the 
annotation set name internal to GATE to group events that co-refer. This information 
is lost once the annotations are rendered in any format apart from GATE-readable 
output. The event co-reference annotations included in MASC are therefore a
subset of those in the originals, and do not include the grouping information contained
in the annotation set names. The differences can be seen by loading both the MASC event 
annotations and the original annotations into GATE. 


CONTACT
-------

MASC is a product of the ANC project. 

Email: anc@anc.org

Department of Computer Science
Vassar College
Poughkeepsie, New York 12604-0520 
USA


