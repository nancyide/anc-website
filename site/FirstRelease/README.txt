----------------------------------------------------------------------

AMERICAN NATIONAL CORPUS FIRST RELEASE

09/12/03 
Keith Suderman 
Nancy Ide 

CONTACT: anc@cs.vassar.edu

----------------------------------------------------------------------

   The data directory contains four gnu-tar compressed subdirectories:

   standoff -  Corpus files annotated using standoff markup. 

   merged   -  Corpus files with all annotations in one file. 

   schemas  -  XCES schemas and supporting files. 

   xml      -  The ANC header and header fragments. 

   To decompress and extract the files from these directories on a
   Unix system run the following two commands:

      gunzip -d filename.tgz
      gnu-tar xvf filename.tar		
   
   Each of the standoff and merged directories contains seven
   sub-directories, one for each of the sub-corpora.  Please refer to the online 
   documentation (http://AmericanNationalCorpus.org/FirstRelease/structure.html)
   for a full description of the ANC First Release.

   The schemas directory contains the XCES schemas for the ANC data. 
   If you need these files for validation purposes, rename the schemas
   directory as ANC on the root drive. On Unix/MacOSX systems this
   will be /ANC, and on Windows systems this will be X:\ANC, where X is the
   drive on which the corpus is located. (Note that the ANC files have already
   been validated against the schemas.)
   
   Contents of the schemas directory:
   
     xcesAna.xsd    : XCES schema for the stand-off annotation files 
                     (files in the stand-off directory named
                     XXX-ana.xml)

     xcesDoc.xsd    : XCES schema for primary text data in stand-off
                      format (files in the stand-off directory named
                      XXX.xml)

     xcesGlobal.xsd : XCES schema for global type definitions

     xcesHeader.xsd : XCES schema for the headers

     xcesLink.xsd   : XCES schema for the attributes in the XLINK
                      namespace

     xcesMerged.xsd : XCES schema for primary text data in merged format
                      (files in the merged directory named XXX.xml)

     xcesSpoken.xsd : XCES schema for primary spoken data in stand-off
                      format (files in the stand-off directory named
                      XXX.xml)

     xcesSpokenMerged.xsd : XCES schema for primary spoken data in
                            merged format (files in the merged directory named XXX.xml)

     ISOents.dtd    : Character entity definitions taken from iso9573-2003.

   The following W3C files are required for XML validation of the ANC
   data, and are included here for convenience. Also available from
   http://www.w3c.org. 

     xml.xsd        : W3C schema defining attributes in the xml namespace. 
      
     XMLSchema.dtd  : DTD for XMLSchemas
   
     datatypes.dtd  : DTD for XML schemas : Part 2 Datatypes.
   
   Each header file in the First Release contains xlinks to /ANC/respStmt.xml
   and /ANC/publicationStmt.xml. These files need to be installed only
   if you want to process the headers and include the information in these
   files. In this case, rename the xml directory as ANC on the root drive (see
   above). 

   The xml directory also contains the header for the full ANC First
   Release corpus (ANC-header.xml). This header does not refer to /ANC/respStmt.xml
   and /ANC/publicationStmt.xml.

CONTACT anc@cs.vassar.edu with questions or problems.   
--------------------------------------------------------------------------
Copyright (c) 2003. American National Corpus Project. All rights reserved.


